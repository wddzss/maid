# prompt_generate.py

from config import *
from litellm import completion


def generate_prompt():
    system_prompt = f"""
你是一个数据生成专家，现在需要为一个对话模型生成训练数据。

角色设定：
{ROLE_DESCRIPTION}

请生成一个“数据生成prompt模板”，用于批量生成训练数据，要求：

1. 输出格式必须是JSONL
2. 每条数据格式：
   {{
     "messages": [
       {{"role": "user", "content": "..."}},
       {{"role": "assistant", "content": "..."}}
     ]
   }}

3. assistant必须严格符合角色设定
4. 对话自然、多样化
5. 避免重复表达
6. 用户问题覆盖：
   - 日常聊天
   - 求助类
   - 情绪类
   - 无聊闲聊
   - 刁钻问题

7. 每次生成 N 条数据（N由外部控制）

请直接输出最终prompt，不要解释。
"""

    response = completion(
        model=MODEL_NAME,
        api_key=API_KEY,
        base_url=BASE_URL,
        messages=[
            {"role": "user", "content": system_prompt}
        ],
        temperature=0.7,
    )

    prompt = response["choices"][0]["message"]["content"]

    with open(PROMPT_FILE, "w", encoding="utf-8") as f:
        f.write(prompt)

    print("✅ Prompt 已生成并保存到", PROMPT_FILE)


if __name__ == "__main__":
    generate_prompt()