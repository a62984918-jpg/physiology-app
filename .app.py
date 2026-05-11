import streamlit as st

# 1. إعدادات الصفحة والهوية البصرية (أرجواني طبي)
st.set_page_config(page_title="HormoneInsight AI", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d0118; color: #f0e6ff; }
    .card { 
        background-color: #1b0a2e; 
        padding: 25px; 
        border-radius: 20px; 
        border: 1px solid #4b2c71;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }
    h1, h2 { color: #d4a5ff; text-align: center; font-family: 'Segoe UI'; }
    .stSlider > div > div > div { background: #d4a5ff; }
    </style>
    """, unsafe_allow_html=True)

# 2. الهيدر
st.markdown("<h1>🧬 نظام تحليل التوازن الهرموني (PCOS Insight)</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>أداة متقدمة لتحليل متلازمة تكيس المبايض والاضطرابات الهرمونية</p>", unsafe_allow_html=True)
st.write("---")

# 3. تنظيم المحتوى
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📥 إدخال البيانات المخبرية")
    lh_level = st.slider("مستوى هرمون LH (mIU/mL)", 1.0, 30.0, 5.0)
    fsh_level = st.slider("مستوى هرمون FSH (mIU/mL)", 1.0, 30.0, 5.0)
    insulin_res = st.selectbox("مقاومة الأنسولين:", ["لا يوجد", "متوسطة", "مرتفعة"])
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🔬 التحليل الفسيولوجي الذكي")
    
    if st.button("بدء تحليل الهرمونات"):
        # حساب النسبة الهرمونية (معادلة علمية حقيقية)
        ratio = lh_level / fsh_level
        
        st.write(f"**النسبة الحالية (LH/FSH):** {ratio:.2f}")
        
        if ratio >= 2.0 or (ratio > 1.5 and insulin_res != "لا يوجد"):
            st.error("⚠️ مؤشر مرتفع: القراءات تشير إلى احتمالية عالية لوجود تكيس (PCOS).")
            st.info("**التفسير العلمي:** ارتفاع هرمون LH بالنسبة لـ FSH يعطل عملية التبويض الطبيعية.")
        else:
            st.success("✅ القراءات ضمن النطاق الطبيعي المتوازن.")
            st.balloons()
            
        st.markdown("---")
        st.subheader("🥗 نصيحة النظام:")
        if insulin_res != "لا يوجد":
            st.warning("يُنصح باتباع نظام غذائي منخفض السكريات لتحسين استجابة الأنسولين.")
        else:
            st.write("استمر في الحفاظ على نمط حياة صحي لضمان توازن الغدد الصماء.")
    else:
        st.info("قم بتحريك المنزلقات واضغط على زر التحليل لمشاهدة قوة الذكاء الاصطناعي في التشخيص.")
    st.markdown("</div>", unsafe_allow_html=True)

# 4. التذييل
st.sidebar.markdown("### 🧬 كيف يعمل البرنامج؟")
st.sidebar.write("يعتمد البرنامج على خوارزمية تربط بين نسبة الهرمونات المنبهة للقشرة وبين مقاومة الأنسولين لتقديم رؤية فسيولوجية شاملة.")
st.sidebar.caption("إصدار خاص - تكنولوجيا التعليم الطبي 2026")
