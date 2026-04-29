# config.py

# ========== LLM配置 ==========
API_KEY = "your_api_key"
BASE_URL = "https://api.openai.com/v1"   # 可替换为任意兼容接口
MODEL_NAME = "gpt-4o-mini"               # 可随便换

# ========== 数据配置 ==========
DATA_SIZE = 2000            # 总数据条数
BATCH_SIZE = 20             # 每次生成多少条（防止长上下文退化）

# ========== 角色设定 ==========
ROLE_DESCRIPTION = """
一个毒舌但其实很温柔的AI助手，说话略带讽刺但不会伤人，
回答简洁、有点幽默感，偶尔使用反问句。
"""

# ========== 输出 ==========
PROMPT_FILE = "data_prompt.txt"
OUTPUT_FILE = "train_data.jsonl"