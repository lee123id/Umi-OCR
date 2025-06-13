# ========================================
# =============== 批量OCR页 ===============
# ========================================

import os
import time
from typing import Dict, List, Any, Optional, Deque
from collections import deque

from umi_log import logger
from .page import Page
from ..mission.mission_ocr import MissionOCR
from ..utils.utils import allowedFileName, get_common_parent_directory
from ..ocr.output import Output

class BatchOCR(Page):
    def __init__(self, *args):
        super().__init__(*args)
        self.config: Optional[Dict[str, Any]] = None
        self.active_tasks: Deque[str] = deque()  # 使用队列管理多个任务
        self.outputList: List[Any] = []  # 输出器列表
        self.task_status: Dict[str, Dict] = {}  # 任务状态跟踪

    # ========================= 【qml调用python】 =========================

    def msnPaths(self, paths: List[str], argd: Dict[str, Any]) -> str:
        """接收路径列表和配置参数，开始OCR任务"""
        # 输入验证
        if not paths:
            self._onEnd(None, "[Error] 没有传入任何文件路径。")
            return ""
        
        if not isinstance(argd, dict):
            self._onEnd(None, "[Error] 配置参数格式不正确。")
            return ""

        # 任务信息
        msnInfo = {
            "onStart": self._onStart,
            "onReady": self._onReady,
            "onGet": self._onGet,
            "onEnd": self._onEnd,
            "argd": argd,
        }
        
        # 预处理参数字典
        if not self._preprocessArgd(argd, paths):
            return ""
            
        # 构造输出器
        if not self._initOutputList(argd):
            return ""
            
        # 路径转为任务列表格式，加载进任务管理器
        msnList = [{"path": x} for x in paths]
        msnID = MissionOCR.addMissionList(msnInfo, msnList)
        
        if msnID.startswith("[Error]"):  # 添加任务失败
            self._onEnd(None, f"{msnID}\n添加任务失败。")
            return msnID
            
        # 添加成功，管理任务状态
        logger.debug(f"添加任务成功 {msnID}")
        self.active_tasks.append(msnID)
        self.task_status[msnID] = {
            "start_time": time.time(),
            "total_files": len(paths),
            "completed": 0,
            "errors": 0
        }
        return msnID

    def _preprocessArgd(self, argd: Dict[str, Any], paths: List[str]) -> bool:
        """预处理参数字典，无异常返回True"""
        self.config = None
        
        if argd["mission.dirType"] == "source":  # 若保存到原目录
            # 获取所有文件的共同父目录
            common_dir = get_common_parent_directory(paths)
            argd["mission.dir"] = common_dir if common_dir else os.getcwd()
        else:  # 若保存到用户指定目录
            d = os.path.abspath(argd["mission.dir"])
            try:
                os.makedirs(d, exist_ok=True)
            except OSError as e:
                logger.error(f"批量OCR无法创建目录：{d}", exc_info=True)
                self._onEnd(
                    None,
                    f'[Error] Failed to create directory: "{d}"\n【异常】无法创建目录: {str(e)}'
                )
                return False
            argd["mission.dir"] = d

        startTimestamp = time.time()
        argd["startTimestamp"] = startTimestamp
        argd["startDatetime"] = time.strftime(r"%Y-%m-%d %H:%M:%S", time.localtime(startTimestamp))
        
        # 使用第一个文件路径获取文件名元素
        path0 = paths[0]
        fileNameEle = os.path.basename(os.path.dirname(path0))
        
        # 处理文件名
        fileName = argd["mission.fileNameFormat"]
        fileName = fileName.replace(r"%date", argd["startDatetime"])
        fileName = fileName.replace("%name", fileNameEle)
        
        if not allowedFileName(fileName):
            self._onEnd(
                None,
                f'[Error] The file name is illegal.\n【错误】文件名【{fileName}】含有不允许的字符。\n不允许含有下列字符： \  /  :  *  ?  "  <  >  |'
            )
            return False
            
        argd["mission.fileName"] = fileName
        self.config = argd
        return True

    def _initOutputList(self, argd: Dict[str, Any]) -> bool:
        """初始化输出器列表，无异常返回True"""
        self.outputList = []
        outputArgd = {
            "outputDir": argd["mission.dir"],
            "outputDirType": argd["mission.dirType"],
            "outputFileName": argd["mission.fileName"],
            "startDatetime": argd["startDatetime"],
            "ignoreBlank": argd["mission.ignoreBlank"],
        }
        
        try:
            output_types = []
            for key in argd:
                if key.startswith("mission.filesType.") and argd[key]:
                    output_type = key.split('.')[-1]
                    output_types.append(output_type)
            
            for otype in output_types:
                if hasattr(Output, otype):
                    output_class = getattr(Output, otype)
                    self.outputList.append(output_class(outputArgd))
        except Exception as e:
            logger.error(f"初始化输出器失败: {str(e)}", exc_info=True)
            self._onEnd(
                None,
                f"[Error] Failed to initialize output file.\n【错误】初始化输出文件失败。\n{str(e)}"
            )
            return False
            
        return True

    def msnStop(self, msnID: Optional[str] = None) -> None:
        """停止指定任务或所有任务"""
        if not msnID:
            for task_id in list(self.active_tasks):
                MissionOCR.stopMissionList(task_id)
                self._cleanup_task(task_id)
        elif msnID in self.active_tasks:
            MissionOCR.stopMissionList(msnID)
            self._cleanup_task(msnID)

    def msnPause(self, msnID: str) -> None:
        """暂停任务"""
        if msnID in self.active_tasks:
            MissionOCR.pauseMissionList(msnID)

    def msnResume(self, msnID: str) -> None:
        """恢复任务"""
        if msnID in self.active_tasks:
            MissionOCR.resumeMissionList(msnID)

    def msnPreview(self, path: str, argd: Dict[str, Any]) -> str:
        """快速进行一次任务，主要用于预览"""
        msnInfo = {
            "onGet": self._onPreview,
            "argd": argd,
        }
        msnList = [{"path": path}]
        return MissionOCR.addMissionList(msnInfo, msnList)

    def _cleanup_task(self, msnID: str) -> None:
        """清理任务资源"""
        if msnID in self.active_tasks:
            self.active_tasks.remove(msnID)
        if msnID in self.task_status:
            del self.task_status[msnID]

    # ========================= 【任务控制器的异步回调】 =========================

    def _onStart(self, msnInfo: Dict[str, Any]) -> None:
        """任务队列开始"""
        pass

    def _onReady(self, msnInfo: Dict[str, Any], msn: Dict[str, Any]) -> None:
        """单个任务准备"""
        msnID = msnInfo.get("msnID", "")
        if msnID not in self.active_tasks:
            logger.warning(f"_onReady 任务ID未在记录: {msnID}")
            return
            
        self.callQmlInMain("onOcrReady", msn["path"])
        
        # 更新任务状态
        if msnID in self.task_status:
            self.task_status[msnID]["started"] = True

    def _onGet(self, msnInfo: Dict[str, Any], msn: Dict[str, Any], res: Dict[str, Any]) -> None:
        """单个任务完成"""
        msnID = msnInfo.get("msnID", "")
        if msnID not in self.active_tasks:
            logger.warning(f"_onGet 任务ID未在记录: {msnID}")
            return
            
        # 补充参数
        res["dir"], res["fileName"] = os.path.split(msn["path"])
        
        # 输出器输出
        success = True
        for o in self.outputList:
            try:
                o.print(res)
            except Exception as e:
                logger.error(f"结果输出失败：{str(e)}", exc_info=True)
                success = False
                
        # 更新任务状态
        if msnID in self.task_status:
            self.task_status[msnID]["completed"] += 1
            if not success:
                self.task_status[msnID]["errors"] += 1
                
        # 通知qml更新UI
        self.callQmlInMain("onOcrGet", msn["path"], res, success)

    def _onEnd(self, msnInfo: Optional[Dict[str, Any]], msg: str) -> None:
        """任务队列完成或失败"""
        msnID = msnInfo.get("msnID", "") if msnInfo else ""
        
        if msnID and msnID not in self.active_tasks:
            logger.warning(f"_onEnd 任务ID未在记录: {msnID}")
            return
            
        # 结束输出器，保存文件
        for o in self.outputList:
            try:
                o.onEnd()
            except Exception as e:
                msg += f"\n[Error] 输出器异常：{str(e)}"
                logger.error(f"输出器结束异常: {str(e)}", exc_info=True)
                
        # 清理任务资源
        if msnID:
            self._cleanup_task(msnID)
            
        # 发送结束消息
        self.callQmlInMain("onOcrEnd", msg, msnID)
        
        # 清空输出器
        self.outputList = []

    def _onPreview(self, msnInfo: Dict[str, Any], msn: Dict[str, Any], res: Dict[str, Any]) -> None:
        """预览任务回调"""
        self.callQmlInMain("onPreview", msn["path"], res)