import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="لعبة تحدي الذكاء التعليمية", page_icon="🎮", layout="centered")

# تخصيص المظهر بالألوان والتنسيق العربي
st.markdown("""
    <style>
    .title { text-align: center; color: #4A90E2; font-family: 'Cairo', sans-serif; }
    .subtitle { text-align: center; color: #7ED321; font-family: 'Cairo', sans-serif; }
    .info-box { background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-right: 5px solid #4A90E2; margin-bottom: 20px; text-align: right; }
    .success-text { color: #2ecc71; font-weight: bold; font-size: 20px; text-align: center; }
    div.stButton > button:first-child { background-color: #4A90E2; color: white; border-radius: 8px; width: 100%; font-size: 18px; }
    </style>
""", unsafe_allow_index=True)

# واجهة اللعبة والترحيب
st.markdown("<h1 class='title'>🎮 لعبة تحدي الذكاء التعليمية 🎮</h1>", unsafe_allow_index=True)
st.markdown("<h3 class='subtitle'>أهلاً بكِ في عالم المعرفة والمرح</h3>", unsafe_allow_index=True)

# صندوق معلومات اللعبة الأساسية
st.markdown(f"""
<div class='info-box'>
    📍 <b>إعداد الطالبة المبدعة:</b> رنيم مشعل <br>
    👩‍🏫 <b>تحت إشراف معلمة المادة القديرة:</b> منيرة العبيكة <br>
    🏢 <b>الصف:</b> ثاني د <br>
    ✨ <b>مرحباً بكم في لعبتنا التفاعلية!</b>
</div>
""", unsafe_allow_index=True)

# خانة إدخال اسم الطالبة الزائرة
st.write("---")
student_name = st.text_input("✍️ عزيزتي الطالبة، يرجى كتابة اسمكِ الكريم هنا للبدء في اللعب:", placeholder="اكتبي اسمكِ هنا...")

if student_name:
    st.markdown(f"<p class='success-text'>🌟 كفو يا بطلة! مرحباً بكِ يا {student_name} في التحدي، استعدي للإجابة على الأسئلة: 🌟</p>", unsafe_allow_index=True)
    
    # تفاصيل الأسئلة والنتيجة باستخدام الـ Session State لحفظ الإجابات
    if 'score' not in st.session_state:
        st.session_state.score = 0
        
    # السؤال الأول
    st.write("### ❓ السؤال الأول:")
    q1 = st.radio("ما هو بيت الأسد المسمى في لغتنا العربية؟", ["العرين", "الجحر", "الخلية", "المرأب"], index=None)
    
    # السؤال الثاني
    st.write("### ❓ السؤال الثاني:")
    q2 = st.radio("ناتج جمع العملية الحسابية التالية ( ٣٥ + ١٥ ) يساوي:", ["٤٠", "٥٠", "٦٠", "٤٥"], index=None)
    
    # السؤال الثالث
    st.write("### ❓ السؤال الثالث:")
    q3 = st.radio("أي من الكائنات التالية يعتبر من الطيور ولكنه لا يطير؟", ["الصقر", "النعامة", "الحمامة", "العصفور"], index=None)

    # زر تصحيح الإجابات
    if st.button("🏁 عرض النتيجة النهائية"):
        score = 0
        if q1 == "العرين": score += 1
        if q2 == "٥٠": score += 1
        if q3 == "النعامة": score += 1
        
        st.write("---")
        if score == 3:
            st.balloons()
            st.success(f"🎉 مبروك يا ممتازة! {student_name} حصلتِ على الدرجة الكاملة: 3 من 3! أنتِ نجمة الصف ثاني د! ⭐")
        elif score > 0:
            st.warning(f"👍 أحسنتِ يا {student_name}، نتيجتكِ هي: {score} من 3. حاولي مرة أخرى لتحصلي على الدرجة الكاملة!")
        else:
            st.error(f"تحدي ممتاز يا {student_name}! نتيجتكِ هي 0 من 3. راجعي المعلومات وحاولي مجدداً، فالخطأ طريق التعلم! 💪")
else:
    st.info("💡 بانتظار كتابة اسمكِ بالأعلى لتفتح لكِ أسئلة المسابقة الشيقة!")
