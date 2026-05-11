import streamlit as st

# إعدادات واجهة البرنامج
st.set_page_config(page_title="Bio-Visual Tutor", layout="wide")

# تصميم رأس الصفحة
st.markdown("""
    <div style="background-color:#004d4d;padding:20px;border-radius:10px">
    <h1 style="color:white;text-align:center;">🔬 منصة فسيولوجيا الحيوان التعليمية</h1>
    <p style="color:#e0e0e0;text-align:center;">مرجع مرئي تفاعلي لشرح العمليات الحيوية المعقدة</p>
    </div>
    """, unsafe_check_complete=True)

st.write("---")

# قائمة البيانات (المواضيع، الروابط، والشروحات)
# يمكنك إضافة مواضيع جديدة هنا لاحقاً بسهولة
curriculum = {
    "آلية انقباض العضلات (Sliding Filament)": {
        "video": "https://www.youtube.com/watch?v=sS6vA9u_Z24",
        "analysis": """
        ### التحليل الفسيولوجي:
        1. **التنبيه:** وصول السيال العصبي يؤدي لتحرر الكالسيوم من الشبكة الساركوبلازمية.
        2. **الارتباط:** الكالسيوم يكشف مواقع الارتباط على الأكتين، مما يسمح للميوسين بالالتصاق.
        3. **الضربة القوية:** تنزلق خيوط الأكتين فوق الميوسين مما يؤدي لقصر القطعة العضلية.
        4. **الاسترخاء:** يتم ضخ الكالسيوم للخارج وفصل الروابط باستخدام الـ ATP.
        """
    },
    "تبادل الغازات (Gas Exchange)": {
        "video": "https://www.youtube.com/watch?v=mZvzl8ot6i8",
        "analysis": """
        ### التحليل الفسيولوجي:
        1. **الانتشار:** ينتقل الأكسجين من الحويصلات الهوائية (ضغط عالي) إلى الدم (ضغط منخفض).
        2. **الهيموجلوبين:** يرتبط الأكسجين بالحديد في الهيموجلوبين لتكوين الأوكسيهيموجلوبين.
        3. **تأثير بور:** زيادة ثاني أكسيد الكربون والحموضة تساعد في تحرر الأكسجين عند الأنسجة النشطة.
        """
    }
}

# شريط جانبي لاختيار الموضوع
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3022/3022543.png", width=100)
st.sidebar.title("الفهرس العلمي")
selection = st.sidebar.selectbox("اختر موضوع الدرس:", list(curriculum.keys()))

# عرض المحتوى بناءً على الاختيار
col1, col2 = st.columns([1.5, 1])

with col1:
    st.subheader("📺 العرض التوضيحي")
    st.video(curriculum[selection]["video"])

with col2:
    st.subheader("📝 الشرح العلمي")
    st.markdown(curriculum[selection]["analysis"])
    st.divider()
    st.info("💡 نصيحة للدكتور: يمكنك استخدام هذا المقطع لشرح العمليات التي لا تُرى بالعين المجردة.")

# تذييل الصفحة
st.markdown("---")
st.caption("تم تطوير هذا البرنامج لدعم مقرر فسيولوجيا الحيوان | 2024")
