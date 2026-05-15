import google.generativeai as genai
MY_KEY = "AIzaSyAxLuq8wtcbr_cLjXcOZ3scIOgNZV_lTs4"
genai.configure(api_key=MY_KEY)
print("--- 조회 시작 ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ 사용 가능 모델명: {m.name}")
            
except Exception as e:
    print(f"⚠️ 에러 발생: {e}")
    