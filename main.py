import streamlit as st
import random
from datetime import date

# 모든 MBTI 유형 포함 (각 유형에 최소 하나의 이미지)
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 예시 밈 이미지 URL (나중에 진짜 밈으로 교체하세요!)
default_image = "https://i.imgur.com/JiQ9z4b.jpeg"
mbti_memes = {
    mbti: [
        (default_image, f"{mbti}의 전형적인 하루 😂"),
        (default_image, f"{mbti}가 회사에서 느끼는 감정 🫠")
    ] for mbti in mbti_types
}

st.title("🌟 MBTI 기반 오늘의 밈")

# 입력 받기
mbti_input = st.text_input("당신의 MBTI를 입력해주세요 (예: INFP, ESTJ 등)").upper()

if mbti_input:
    if mbti_input in mbti_memes:
        # 오늘 날짜 기준 랜덤 고정
        today = str(date.today())
        random.seed(today + mbti_input)
        meme = random.choice(mbti_memes[mbti_input])

        st.image(meme[0], caption=meme[1], use_column_width=True)
        st.success(f"{mbti_input}에게 어울리는 오늘의 밈이에요!")

        if st.button("다른 밈 보여줘 🔁"):
            meme = random.choice(mbti_memes[mbti_input])
            st.image(meme[0], caption=meme[1], use_column_width=True)
    else:
        st.warning("입력한 MBTI가 올바른 형식이 아니에요! (예: INFP, ESTJ 등)")
else:
    st.info("MBTI를 입력하면 오늘의 밈을 보여드릴게요!")
