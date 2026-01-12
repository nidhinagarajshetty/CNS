cybersecurity_incidents=[
    "The Morris Worm disrupted computers in 1988, one of the first computer worms distrupted via the interent.",
    " In 2007, Estonia suffered a massive DDoS attack that crippled the nations digital infrastructure.",
    "In 2013, Target experienced a major data breach where millions of credit card details were stolen.",
    "The WannaCry ransomware attack in 2017 affected thousand of computers globally, encrypting data and demanding ransom.",
    "A phishing Attack in 2016 compromised the email accounts of several high-profile figures, leading to the release of sensitive information.",
    "The Mirai botnet in 2016 launched DDos attacks using IoT devices, bringing down large parts of the internet."
]
categories={"virus":[],"phishing":[],"DDoS":[],"ransomware":[],"data breach":[]}

for incident in cybersecurity_incidents:
    for category in categories:
        if category in incident.lower():
            categories[category].append(incident)

for category, incidents in categories.items():
    print(f"\nCategory: {category.capitalize()}")
    print("\n".join(incidents) if incidents else "No incidents in this category.")