print("👩‍💻 مرحبا يا جويس - من بنغازي!")
print("🔐 برنامج ذكاء اصطناعي V4 - مع نصائح")
print("--------------------------------------------------")

while True:
    password = input("\nاكتبي كلمة السر (أو اكتبي خروج): ")
    
    if password == "خروج":
        print("\n🎉 شهادتك يا جويس:")
        print("╔══════════════════════════════╗")
        print("║  Joyce - 14 سنة - ليبيا     ║")
        print("║  White Hat Hacker V4         ║")
        print("║  تم انجاز المشروع بنجاح 👩‍💻  ║")
        print("╚══════════════════════════════╝")
        break

    score = 0
    نصائح = []

    # 1- الطول
    if len(password) >= 8:
        score += 3
    elif len(password) >= 5:
        score += 1
    else:
        نصائح.append("❌ زيدي الطول - خليه 8 حروف على الأقل")

    # 2- أرقام
    if any(c.isdigit() for c in password):
        score += 2
    else:
        نصائح.append("❌ زيدي رقم (مثل 123)")

    # 3- حروف كبيرة
    if any(c.isupper() for c in password):
        score += 2
    else:
        نصائح.append("❌ زيدي حرف كبير (مثل A, B)")

    # 4- رموز
    if any(c in "!@#$%^&*()_-+={}[]|;:<>,.?/~`" for c in password):
        score += 3
    else:
        نصائح.append("❌ زيدي رمز خاص (مثل ! @ # $)")

    # 5- كلمات ضعيفة
    weak = ["123456", "password", "joyce", "benghazi", "libya", "qwerty"]
    if password.lower() in weak:
        score = 1
        نصائح.append("⚠️ هذه كلمة سر مشهورة جداً - غيريها بالكامل!")

    # التقييم من 10
    print("\n--- النتيجة ---")
    if score >= 8:
        print(f"✅ قوي جداً! Score: {score}/10")
    elif score >= 5:
        print(f"⚠️ متوسط Score: {score}/10")
    else:
        print(f"❌ ضعيف Score: {score}/10")

    # النصائح
    if نصائح:
        print("\n💡 نصائح باش تقويه:")
        for ن in نصائح:
            print(ن)
    else:
        print("🎉 ممتاز! باسورد قوي ما يحتاجش نصائح")
