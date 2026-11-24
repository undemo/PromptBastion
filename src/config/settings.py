# -*- coding: utf-8 -*-
"""
应用配置设置
"""

import os
from typing import Dict


class Config:
    """应用配置"""
    
    # 服务器配置
    HOST = "0.0.0.0"
    PORT = 6006
    DEBUG = True
    
    # vLLM服务配置
    VLLM_BASE_URL = "http://127.0.0.1:6007"
    VLLM_TIMEOUT = 60
    VLLM_MAX_RETRIES = 5
    VLLM_RETRY_DELAY = 1
    VLLM_RETRY_BACKOFF = 1.0
    
    # LoRA适配器配置
    LORA_ADAPTERS: Dict[str, str] = {
        "classify": "classify",
        "china": "china"
    }
    
    # 敏感词模块配置
    SENSITIVE_WORDS_FILE = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
        "program", "sensitive", "中文互联网敏感词.txt"
    )
    
    # 其他配置
    SECURITY_CHECK_ENABLED = True
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # CORS配置
    CORS_ORIGINS = ["*"]
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_METHODS = ["*"]
    CORS_ALLOW_HEADERS = ["*"]
    
    # 数据净化模块配置
    DATA_PURIFICATION_MODEL = "gemini-2.5-flash"
    DATA_PURIFICATION_API_KEY = os.getenv("DATA_PURIFICATION_API_KEY", "").strip()
    if not DATA_PURIFICATION_API_KEY:
        raise RuntimeError("请设置环境变量 DATA_PURIFICATION_API_KEY")
    DATA_PURIFICATION_API_URL = "https://api.yourapi.cn/v1/chat/completions"
    DATA_PURIFICATION_BAK_MODEL = "gemini-2.5-pro"
    DATA_PURIFICATION_API_BAK_URL = "https://api.yourapi.cn/v1/chat/completions"
    DATA_PURIFICATION_API_BAK_KEY = (
        os.getenv("DATA_PURIFICATION_API_BAK_KEY", "").strip() or DATA_PURIFICATION_API_KEY
    )
    DATA_PURIFICATION_TIMEOUT = 15
    
    # 超时配置
    TOTAL_TIMEOUT = 60
    SAFETY_MARGIN = 2
    
    # 日志配置
    MAX_LOGS_HISTORY = 1000
    SNAPSHOT_DIR = "snapshots"


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False


def get_config(env: str = "development") -> Config:
    """获取配置"""
    configs = {
        "development": DevelopmentConfig,
        "production": ProductionConfig
    }
    return configs.get(env, DevelopmentConfig)()


# 默认配置实例
config = Config()
