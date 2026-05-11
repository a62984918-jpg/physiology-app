import streamlit as st
import time

# 1. إعدادات الصفحة والتصميم
st.set_page_config(page_title="BioLive XR | Future of Bio", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); color: #00f2fe; }
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 242, 254, 0.3);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
    }
    .neon-text { color: #00f2fe; text-shadow: 0 0 10px #00f2fe; text-align: center; }
    .stButton>button { background: linear-gradient(45deg, #00f2fe, #4facfe); color: white; border-radius: 12px; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='neon-text'>⚡ BioLive XR</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚀 AR Scanner", "🔬 Virtual Lab", "🧠 AI Tutor"])

with tab1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("📸 محاكي الماسح الضوئي (AR Scanner)")
    uploaded_file = st.file_uploader("ارفع صورة الكتاب هنا...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        with st.spinner("جاري المسح الضوئي بتقنية AR..."):
            time.sleep(2)
            st.success("✅ تم اكتشاف نموذج ثلاثي الأبعاد!")
            st.markdown("### 🧬 معاينة النموذج:")
            # استخدمنا "أيقونة" كبيرة بدلاً من الصورة التي قد تتعطل
            st.markdown("<h1 style='text-align:center; font-size: 100px;'>🫀</h1>", unsafe_allow_html=True)
            st.info("ملاحظة: في النسخة الكاملة، يظهر هنا قلب نابض بتقنية XR.")
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("🧪 المختبر الافتراضي")
    exp = st.selectbox("اختر التجربة:", ["تشريح القلب", "فحص كريات الدم", "الهرمونات"])
    
    if st.button("تشغيل المحاكاة"):
        progress_text = "جاري تحضير الأدوات المخبرية..."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        
        st.markdown("<h1 style='text-align:center; font-size: 100px;'>🔬</h1>", unsafe_allow_html=True)
        st.success(f"مختبر {exp} جاهز الآن. تم تفعيل واجهة التحكم التفاعلية.")
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("🤖 مساعد Bio-AI")
    user_input = st.text_input("اسألني عن أي وظيفة حيوية:")
    if user_input:
        st.markdown(f"**التحليل الذكي لـ '{user_input}':**")
        st.write("وفقاً للمراجعات العلمية، هذه العملية حيوية للحفاظ على التوازن الداخلي (Homeostasis) من خلال التغذية الراجعة.")
    st.markdown("</div>", unsafe_allow_html=True)

st.sidebar.markdown("<h2 class='neon-text'>BioLive XR</h2>", unsafe_allow_html=True)
st.sidebar.write("تكنولوجيا تعليم الأحياء - إصدار 2026")
