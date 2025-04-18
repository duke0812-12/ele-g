
import streamlit as st
import random
import time
from PIL import Image

# 遊戲設定
GAME_DURATION = 30  # 遊戲秒數
GRID_SIZE = 3       # 3x3 格子

# 載入象象圖片
elephant_img = Image.open("elephant.png")

# 初始化 session state
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_position' not in st.session_state:
    st.session_state.current_position = random.randint(0, GRID_SIZE**2 - 1)

# 重新開始遊戲
def restart_game():
    st.session_state.start_time = time.time()
    st.session_state.score = 0
    st.session_state.current_position = random.randint(0, GRID_SIZE**2 - 1)

# 顯示標題與說明
st.title("🐘 打象象 Whack-an-Elephant")
st.markdown("點擊突然出現的象象圖片來得分！遊戲時間：30 秒")

# 開始按鈕
if st.button("🚀 開始遊戲！"):
    restart_game()

# 計時與主邏輯
if st.session_state.start_time:
    elapsed = time.time() - st.session_state.start_time
    remaining_time = max(0, int(GAME_DURATION - elapsed))
    st.markdown(f"⏰ 剩餘時間：**{remaining_time} 秒**")
    st.markdown(f"🎯 分數：**{st.session_state.score}**")

    # 顯示 3x3 格子
    cols = st.columns(GRID_SIZE)
    for i in range(GRID_SIZE):
        with cols[i]:
            for j in range(GRID_SIZE):
                idx = i * GRID_SIZE + j
                if idx == st.session_state.current_position:
                    if st.button(" ", key=f"elephant_{idx}"):
                        st.session_state.score += 1
                        st.session_state.current_position = random.randint(0, GRID_SIZE**2 - 1)
                    st.image(elephant_img, width=80)
                else:
                    st.button(" ", key=f"empty_{idx}", disabled=True)

    # 結束條件
    if elapsed >= GAME_DURATION:
        st.success(f"🎉 時間到！你打中了 **{st.session_state.score}** 隻象象！")
        st.button("🔁 再玩一次", on_click=restart_game)
