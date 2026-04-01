import time

hour = int(time.strftime('%H')) 

if hour >= 5:
    if hour < 12:
        print("Good Morning 🌅")
    elif hour < 17:
        print("Good Afternoon ☀️")
    elif hour < 21:
        print("Good Evening 🌆")
    else:
        print("Good Night 🌙")
else:
    print("Good Night 🌙")
