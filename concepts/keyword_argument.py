# 키워드 값 (keyword argument)
# 키워드는 매개변수의 이름 
# 값/인자는 매개변수에 전달되는 실제 데이터

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang = "자바", age = 25, name = "김태호")
