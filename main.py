import streamlit as st
import random
from datetime import date

# MBTI별 이미지와 캡션
mbti_memes = {
    "INFP": [("https://i.imgur.com/Z9QZ1Zs.jpeg", "감성폭발하는 INFP 🥺")],
    "INFJ": [("https://i.imgur.com/A7Zn5vz.jpeg", "사람을 다 읽고 있는 INFJ 🧠")],
    "INTJ": [("https://i.imgur.com/ndzRq4T.jpeg", "치밀하게 계획하는 INTJ 📊")],
    "INTP": [("https://i.imgur.com/WlmfhCW.jpeg", "논리에 빠진 천재 INTP 🧪")],
    "ENFP": [("https://i.imgur.com/kSK1fbW.jpeg", "갑자기 춤추는 ENFP 💃")],
    "ENFJ": [("https://i.imgur.com/5OGuh6g.jpeg", "모두의 멘토 ENFJ 👩‍🏫")],
    "ENTJ": [("https://i.imgur.com/m2rqFvu.jpeg", "리더십 폭발 ENTJ 💼")],
    "ENTP": [("https://i.imgur.com/HcN6qjT.jpeg", "말싸움 1등 ENTP 🎤")],
    "ISFP": [("https://i.imgur.com/Yi0iQRM.jpeg", "예술에 취한 ISFP 🎨")],
    "ISFJ": [("https://i.imgur.com/nZ0QciN.jpeg", "다 챙겨주는 ISFJ 🍲")],
    "ISTJ": [("https://i.imgur.com/Nr5x1Xa.jpeg", "규칙을 사랑하는 ISTJ 🧾")],
    "ISTP": [("https://i.imgur.com/Br1FVbK.jpeg", "손으로 직접 해보는 ISTP 🔧")],
    "ESFP": [("https://i.imgur.com/dWtwWCL.jpeg", "파티의 중심 ESFP 🎉")],
    "ESFJ": [("https://i.imgur.com/p5tsPoV.jpeg", "모두를 챙기는 ESFJ 🍪")],
    "ESTJ": [("https://i.imgur.com/fMo9xFl.jpeg", "팀장을 맡는 ESTJ 🫡")],
    "ESTP": [("https://i.imgur.com/fEVgclm.jpeg", "오늘도 돌진하는 ESTP 🏍️")],
}

st.set_page_config(page_title="MBTI 밈 추천기", page_icon="🎭")
st.title("🎭 MBTI 기반 오늘의 밈")

mbti_input = st.text_input("당신의 MBTI를 입력해주세요 (예: INFP, ESTJ 등)").upper()

if mbti_input:
    if mbti_input in mbti_memes:
        # 오늘 날짜 기반 랜덤 고정
        today = str(date.today())
        random.seed(today + mbti_input)
        meme = random.choice(mbti_memes[mbti_input])

        st.image(meme[0], caption=meme[1], use_column_width=True)
        st.success(f"{mbti_input}에게 어울리는 오늘의 밈이에요!")

        if st.button("다른 밈도 보여줘 🔁"):
            meme = random.choice(mbti_memes[mbti_input])
            st.image(meme[0], caption=meme[1], use_column_width=True)
    else:
        st.error("입력한 MBTI는 유효하지 않아요! (예: INFP, ENTP, ISTJ 등)")
else:
    st.info("위에 당신의 MBTI를 입력해보세요! ✨")
