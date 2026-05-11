import streamlit as st
import time

# 1. إعدادات الصفحة والتصميم المستقبلي (Glassmorphism)
st.set_page_config(page_title="BioLive XR | المستقبل بين يديك", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #00f2fe;
        font-family: 'Arial';
    }
    
    /* تأثير الزجاج (Glassmorphism) */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    .neon-text {
        color: #00f2fe;
        text-shadow: 0 0 10px #00f2fe, 0 0 20px #00f2fe;
        font-family: 'Orbitron', sans-serif;
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #00f2fe, #4facfe);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 24px;
        transition: 0.3s;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px #00f2fe;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. الهيدر (Header)
st.markdown("<h1 class='neon-text' style='text-align: center;'>⚡ BioLive XR</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a1c4fd;'>الجيل القادم من تعلم فسيولوجيا الحيوان بالذكاء الاصطناعي</p>", unsafe_allow_html=True)

# 3. القائمة الرئيسية (Navigation)
tab1, tab2, tab3, tab4 = st.tabs(["🚀 AR Scanner", "🔬 Virtual Lab", "🧠 AI Tutor", "📊 Progress"])

# --- TAB 1: AR SCANNER (Simulation) ---
with tab1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("📸 محاكي الماسح الضوئي (AR Scanner)")
    st.write("قم برفع صورة من كتابك الدراسي لتحويلها إلى موديل 3D تفاعلي")
    uploaded_file = st.file_uploader("اختر صورة للتحليل...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        with st.spinner("جاري تحليل العناصر البيولوجية..."):
            time.sleep(2)
            st.success("تم التعرف على: (عضلة القلب - الدورة الدموية)")
            col1, col2 = st.columns(2)
            with col1:
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpbmZ1Nml2Znd6bmN0eHd6eHJ6eHJ6eHJ6eHJ6eHJ6eHJ6eHImZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/3o7TKVUn7iM8FMEU24/giphy.gif", caption="عرض 3D تفاعلي")
            with col2:
                st.markdown("""
                **البيانات العلمية المكتشفة:**
                - الصمامات: تعمل بكفاءة 98%
                - معدل النبض في الصورة: 72 نبضة/دقيقة
                - ملاحظة: يوجد ضيق في الشريان التاجي الأيمن.
                """)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: VIRTUAL LAB ---
with tab2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("🧪 المختبر الافتراضي (Virtual Lab)")
    exp = st.selectbox("اختر التجربة:", ["تشريح القلب", "فحص خلايا الدم", "تفاعل الإنزيمات"])
    
    if st.button("بدء التجربة الافتراضية"):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        st.info(f"تم تحميل مختبر {exp} بنجاح. استخدم أدوات التشريح الافتراضية الآن.")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmtvN3B0Znp6eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTjJp6zH6Y6O3W/giphy.gif")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: AI TUTOR ---
with tab3:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("🤖 المساعد الذكي (Bio-AI)")
    user_q = st.text_input("اسألني أي سؤال في الفسيولوجيا:")
    if user_q:
        st.write("**Bio-AI:** سأقوم بتحليل سؤالك بناءً على أحدث الأبحاث...")
        time.sleep(1)
        st.write(f"بناءً على سؤالك حول '{user_q}'، إليك التفسير المبسط: [إجابة مولدة بالذكاء الاصطناعي]")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 4: PROGRESS ---
with tab4:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("🏆 لوحة الإنجازات (Gamification)")
    c1, c2, c3 = st.columns(3)
    c1.metric("المستوى", "Lvl 14")
    c2.metric("النقاط XP", "1,250")
    c3.metric("الترتيب", "#3")
    st.write("الأوسمة المحصلة:")
    st.markdown("🏅 خبير التشريح | 🔬 عالم الأنسجة | ⚡ سريع البديهة")
    st.markdown("</div>", unsafe_allow_html=True)

# تذييل الصفحة
st.sidebar.markdown("<h2 class='neon-text'>BioLive XR</h2>", unsafe_allow_html=True)
st.sidebar.info("هذا النموذج الأولي (Prototype) يوضح واجهة وتجربة المستخدم للتطبيق المستقبلي.")
