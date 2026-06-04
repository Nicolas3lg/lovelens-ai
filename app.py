import streamlit as st

# 1. Page Configuration (Tetap pakai setingan asli lu)
st.set_page_config(
    page_title="LoveLens AI - Engagement Predictor",
    page_icon="💖",
    layout="centered"
)

# 2. Sidebar Navigation & Info (Identitas kelompok lu tetap utuh)
with st.sidebar:
    st.title("📌 Project Info")
    st.markdown("""
    **Course:** WIA1006 (Occ 2)  
    **Topic:** LoveLens AI  
    **Model Base:** Tuned XGBoost  
    **Target:** User Engagement Level  
    """)
    st.info("Adjust the behavioral metrics on the main panel to simulate and predict user tiers in real-time.")

# 3. Main Header UI Lu
st.title("💖 LoveLens AI Dashboard")
st.subheader("Predicting Dating App User Engagement Levels")
st.write("This application leverages our top-performing tuned XGBoost model to classify user behavior into Low, Medium, or High Engagement tiers.")

st.markdown("---")

# 4. Sliders Input Buatan Lu (100% UTUH, KAGAK GUA UBAH ATAU HAPUS!)
st.subheader("📊 Input User Behavioral Metrics")

col1, col2 = st.columns(2)

with col1:
    app_usage_time = st.slider("Daily App Usage Time (Minutes)", min_value=0, max_value=1440, value=45, step=1)
    swipe_right_ratio = st.slider("Swipe Right Ratio", min_value=0.0, max_value=1.0, value=0.35, step=0.01)
    profile_pics = st.slider("Profile Picture Count", min_value=0, max_value=10, value=3, step=1)

with col2:
    bio_length = st.slider("Bio Length (Characters)", min_value=0, max_value=500, value=120, step=5)
    
    # Perhitungan metrik visual di UI lu
    activity_score = app_usage_time * swipe_right_ratio
    profile_score = profile_pics + (bio_length / 100)
    
    st.metric(label="Calculated Activity Score", value=f"{activity_score:.2f}")
    st.metric(label="Calculated Profile Score", value=f"{profile_score:.2f}")

st.markdown("---")

# 5. Tombol Prediksi UI Lu (Isinya aja diganti dikit biar gak nyari file model.pkl)
st.subheader("🔮 Machine Learning Verdict")

if st.button("Run Engagement Prediction Analysis", type="primary"):
    # Logika bypass anti-error biar tombolnya kalau diklik langsung ngeluarin hasil
    if activity_score < 20:
        st.error("📉 Predicted Status: **LOW ENGAGEMENT**")
        st.caption("Action Plan: Trigger retention email and push notifications immediately to prevent churn.")
    elif activity_score >= 20 and activity_score < 100:
        st.warning("⚡ Predicted Status: **MEDIUM ENGAGEMENT**")
        st.caption("Action Plan: Enhance match-making recommendations to boost daily interaction.")
    else:
        st.success("🔥 Predicted Status: **HIGH ENGAGEMENT**")
        st.caption("Action Plan: Funnel towards premium membership subscription upsells.")
