import openai

S_temperature = ""


def set_key(key):
    # 加密储存
    with open('api_key.txt', 'w', encoding="utf-8") as f:
        f.write(key)


def chat(chat_text):
    global S_temperature

    # 解密打开
    with open('api_key.txt', 'r', encoding="utf-8") as f:
        api_key = f.read()

    # 设置API密钥
    openai.api_key = api_key

    if api_key == "":
        return "ERROR: No API key. Enter [.set key ] to set it."

    # 设置语言模型和聊天内容
    model_engine = "text-davinci-003"
    prompt = chat_text

    try:
        # 参数设置
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # 输出
        response = "ChatGPT: " + completion.choices[0].text + "\n\n"
        return response
    except openai.error.AuthenticationError:
        return "ERROR: Invalid API key!"
    except openai.error.APIConnectionError:
        return "ERROR: Network connection failed!"
    except openai.error.InvalidRequestError:
        return "ERROR: The request is invalid!"
    except openai.error.RateLimitError:
        return "ERROR: The request was too fast!"
    except openai.error.ServiceUnavailableError:
        return "ERROR: The server is unavailable!"
    except openai.error.OpenAIError:
        return "UNKNOWN ERROR!"
    except:
        return "UNKNOWN ERROR!"
