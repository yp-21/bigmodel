from openai import OpenAI

client = OpenAI(
    api_key="sk-K3DELa7jSs70NbGojfgYFRcAtqzD5ksYyaEYq8o2JYx4iXyp",
    base_url="https://api.moonshot.cn/v1",
)

def ask_kimi(user_question: str) -> str:
    """向 Kimi 发送用户问题，返回模型回答"""
    completion = client.chat.completions.create(
        model="kimi-k2-turbo-preview",
        messages=[
            {
                "role": "system",
                "content": (
                     "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"

                ),
            },
            {"role": "user", "content": user_question},
        ],
        temperature=0.6,
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    try:
        while True:
            question = input("\n请输入你的问题（直接回车退出）：").strip()
            if not question:
                break
            answer = ask_kimi(question)
            print("\nKimi 回答：", answer)
    except KeyboardInterrupt:
        print("\n已退出。")