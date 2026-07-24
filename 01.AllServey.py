#주제보단 배운거 다 집어넣어서 설문 조사하는 거 만들어라
#이걸로 정보 얻어서 나중에 서버에 저장하는 걸 연동할거다

"""입력 받을 사항
-이름 또는 닉네임
-관심 주제
-체크박스 또는 슬라이더 최소 1개이상 사용
"""
"""진행 방향
-로그인 화면
-로그인 시 아래 다양한 컴포넌트를 이용한 설문지 작성 후
-설문 화면이 없어지고 결과를 화면에 출력
-로그인 비정상 시 다시 로그인 화면으로 진행

"""


import streamlit as st
# 01_login.py
import streamlit as st

# 선언 --------------------------
loginout = st.query_params.get("loginout","logout")

if "input_login_id" not in st.session_state:
    st.session_state.input_login_id = ""

if "input_login_pwd" not in st.session_state:
    st.session_state.input_login_pwd = ""

def reset():
    st.session_state.input_login_id = ""
    st.session_state.input_login_pwd = ""

# 화면 --------------------------
if loginout == "logout":
    st.title("LOGIN")
    with st.form("login_form"):
        input_id = st.text_input("ID입력", key="input_login_id")
        input_pwd = st.text_input("PWD입력",type="password", key="input_login_pwd")

        submit_area , reset_area = st.columns(2)
        with submit_area:
            login_submit = st.form_submit_button("LOGIN")
        with reset_area:
            reset_submit = st.form_submit_button("RESET", on_click=reset)

        if login_submit:
            if input_id == "id01" and input_pwd == "pwd01":
               st.query_params["loginout"] = "login"
               st.rerun()
            else:
                st.toast("로그인 실패")
else:
    if st.session_state.get("survey_submitted", False):
        st.info("설문이 완료됐습니다.")

    else:
        st.info("로그인 했습니다.")

        logout = st.button("LOGOUT")
        if logout:
            st.session_state.survey_submitted = False
            st.query_params["loginout"] = "logout"
            st.rerun()

        st.title("What's your name?")
        st.text_input("이름을 입력해주세요: ")

        age = st.slider("나이:", min_value=30, max_value=80, value=60)
        if age==0: 
            st.warning("설문을 입력해주세요.")
            
        if age >= 80 or age < 50:
            st.warning("설문 조사 대상이 아닙니다.")

        st.subheader("당신의 관심사를 알려주세요")
        restplay = st.text_area("관심사 입력")

        st.subheader("자녀는 몇 명인가요")
        B = st.number_input("명")

        st.subheader("직업은 무엇인가요")
        Jobs = st.selectbox(
            "직업:",
            ["개발자","공무원", "의사", "그 외 전문직", "없음"]
        )

        if Jobs == "없음":
            st.warning("설문 조사 대상이 아닙니다.")

        options = st.multiselect(
            "어떤 색 조합을 좋아하세요?",
            ["Green", "Yellow", "Red", "Blue"],
            ["Yellow", "Red"]
        )

        if st.button("제출"):
            st.session_state.survey_submitted = True
            st.rerun()
