import streamlit as st
import random
from datetime import date

# MBTI별 이미지와 설명 (Unsplash 이미지 사용)
mbti_memes = {
    "INFP": [("https://source.unsplash.com/400x300/?dreamer", "감성적인 몽상가 INFP 💭")],
    "ENFP": [("https://source.unsplash.com/400x300/?party", "에너지 넘치는 ENFP 🎉")],
    "ISTJ": [("https://source.unsplash.com/400x300/?checklist", "계획적인 ISTJ 📋")],
    "ESTP": [("https://source.unsplash.com/400x300/?adventure", "모험을 사랑하는 ESTP 🏞️")],
    "INFJ": [("https://source.unsplash.com/400x300/?mystery", "신비로운 INFJ 🧙‍♂️")],
    "ENTJ": [("https://source.unsplash.com/400x300/?leader", "타고난 리더 ENTJ 🧠")],
    "ISFP": [("https://source.unsplash.com/400x300/?artistic", "예술 감각 넘치는 ISFP 🎨")],
    "ENTP": [("https://source.unsplash.com/400x300/?debate", "말싸움 고수 ENTP 🎤")],
}

st.set_page_config(page_title="MBTI 밈 리얼 버전", page_icon="🖼️")
st.title("🖼️ 오늘의 MBTI 밈")

mbti_input = st.text_input("당신의 MBTI를 입력해주세요 (예: INFP, ENFP 등)").upper()

if mbti_input:
    if mbti_input in mbti_memes:
        today = str(date.today())
        random.seed(today + mbti_input)
        meme = random.choice(mbti_memes[mbti_input])

        st.image(meme[0], caption=meme[1], use_column_width=True)
        st.success(f"{mbti_input}에게 어울리는 오늘의 밈이에요!")

        if st.button("다른 밈 보여줘 🔁"):
            meme = random.choice(mbti_memes[mbti_input])
            st.image(meme[0], caption=meme[1], use_column_width=True)
    else:
        st.warning("해당 MBTI는 아직 등록되지 않았어요! (현재는 일부 유형만 지원 중)")
else:
    st.info("당신의 MBTI를 입력해보세요!")

