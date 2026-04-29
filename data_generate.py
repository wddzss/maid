# data_generate.py

import json
from config import *
from litellm import completion


def load_prompt():
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read()


def generate_batch(prompt, batch_size):
    full_prompt = prompt.replace("N", str(batch_size))

    response = completion(
        model=MODEL_NAME,
        api_key=API_KEY,
        base_url=BASE_URL,
        messages=[
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.9,
    )

    return response["choices"][0]["message"]["content"]


def parse_jsonl(text):
    lines = text.strip().split("\n")
    valid = []

    for line in lines:
        try:
            obj = json.loads(line)
            valid.append(obj)
        except:
            continue

    return valid


def main():
    prompt = load_prompt()

    total = DATA_SIZE
    batch = BATCH_SIZE

    all_data = []

    for i in range(0, total, batch):
        print(f"🚀 正在生成第 {i} - {i+batch} 条数据")

        raw = generate_batch(prompt, batch)
        parsed = parse_jsonl(raw)

        all_data.extend(parsed)

    # 写入文件
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for item in all_data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"✅ 数据生成完成，共 {len(all_data)} 条")


if __name__ == "__main__":
    main()