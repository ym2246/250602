import streamlit as st
import random

st.set_page_config(page_title="MBTI 친구 궁합", page_icon="🤝")
st.title("🤝 MBTI 친구 궁합 테스트")

def calculate_compatibility(mbti1, mbti2):
    mbti1 = mbti1.upper()
    mbti2 = mbti2.upper()

    score = 0
    explanation = []

    if len(mbti1) != 4 or len(mbti2) != 4:
        return None, "둘 다 정확한 4자리 MBTI를 입력해주세요!"

    # E-I: 다르면 +10
    if mbti1[0] != mbti2[0]:
        score += 10
        explanation.append("외향과 내향이 잘 보완돼요!")
    else:
        explanation.append("둘 다 같은 에너지 타입이라 편할 수도 있어요.")

    # N-S: 같으면 +20
    if mbti1[1] == mbti2[1]:
        score += 20
        explanation.append("비슷한 정보 해석 스타일을 가지고 있어요!")
    else:
        explanation.append("세상을 보는 시각이 달라서 신선해요.")

    # T-F: 다르면 +15
    if mbti1[2] != mbti2[2]:
        score += 15
        explanation.append("감성과 이성이 서로 보완돼요!")
    else:
        explanation.append("감정선 또는 논리선이 비슷해요.")

    # J-P: 같으면 +10
    if mbti1[3] == mbti2[3]:
        score += 10
        explanation.append("비슷한 라이프스타일을 가졌어요!")
    else:
        explanation.append("계획형과 즉흥형의 시너지에 도전해보세요.")

    # 약간의 유머/랜덤 가산점
    score += random.randint(-5, 5)
    score = max(0, min(100, score))  # 점수 범위 제한

    return score, explanation

# 사용자 입력
col1, col2 = st.columns(2)
with col1:
    mbti1 = st.text_input("나의 MBTI", value="", max_chars=4)
with col2:
    mbti2 = st.text_input("친구의 MBTI", value="", max_chars=4)

if mbti1 and mbti2:
    score, explanation = calculate_compatibility(mbti1, mbti2)

    if score is not None:
        st.subheader(f"🌟 궁합 점수: {score} / 100")
        
        if score >= 80:
            st.success("우와! 완전 찰떡 궁합이에요! ❤️")
        elif score >= 60:
            st.info("꽤 잘 맞는 편이에요! 😊")
        elif score >= 40:
            st.warning("친해질 수 있지만 노력이 필요해요 🤔")
        else:
            st.error("성격 차이가 있을 수 있어요... ⚡")

        with st.expander("🧠 궁합 해설 보기"):
            for line in explanation:
                st.write("- " + line)
    else:
        st.warning(explanation)
