from ai_translate_main import translate


while True:
    source = input("input: ")
    question = '你是一个语言大师，请将下面的文字进行中英互译，要求简介明了，优雅得体。文字是：'+source
    answere = translate(question)

