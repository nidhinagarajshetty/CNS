def detect_phishing(email_content):
    phishing_keywords=['win','free','urgent','click','claim','password']
    found_keywords=[word for word in phishing_keywords if word in email_content.lower()]
    if found_keywords:
        return f"Potential phishing detected! Keywords found:{found_keywords}"
    else:
        return "Email seems safe."
email="Cxcvbn"
print(detect_phishing(email))