import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Physiology Visual Guide", layout="wide")

st.title("🔬 المرجع المرئي لفسيولوجيا الحيوان")
st.write("برنامج تعليمي تفاعلي لعرض العمليات الحيوية")

# قاموس المحتوى التعليمي
curriculum = {
    "الجهاز الهضمي (Digestive System)": {
        "video": "https://www.youtube.com/watch?v=X3TAROotFfM",
        "notes": "يركز هذا المقطع على آلية الهضم الميكانيكي والكيميائي ورحلة الطعام في القناة الهضمية."
    },
    "الجهاز التنفسي (Respiratory System)": {
        "video": "https://www.youtube.com/watch?v=mOKmjYwfDGU",
        "notes": "شرح لعملية تبادل الغازات في الحويصلات الهوائية ودور الحجاب الحاجز."
    },
    "انقباض العضلات (Muscle Contraction)": {
        "video": "https://www.youtube.com/watch?v=ousflrOzQHc",
        "notes": "يوضح نظرية الخيوط المنزلقة وتداخل الأكتين والميوسين."
    }
}

# قائمة الاختيار
option = st.selectbox("اختر الموضوع الذي تريد عرضه أمام الدكتور:", list(curriculum.keys()))

# عرض المحتوى
st.divider()
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"عرض مرئي: {option}")
    st.video(curriculum[option]["video"])

with col2:
    st.subheader("💡 ملخص فسيولوجي")
    st.info(curriculum[option]["notes"])

st.sidebar.markdown("---")
st.sidebar.write("تم تطوير هذا البرنامج لأغراض تعليمية - مقرر فسيولوجيا الحيوان")
