def conver_12_to_24(time_str):
    in_time = time_str.strip().lower()
    if 'am' in in_time:
        time = in_time.replace("am", "").strip()
        hour , minute = map(int,time.split(":"))
        hour = 0 if hour==12 else hour
    elif "pm" in in_time:
        time= in_time.replace("pm","").strip()
        hour,minute = map(int , time.split(":"))
        hour = hour if hour == 12 else hour  + 12 
    else:
        return "時間は無効です。"
    return f"{hour:02}：{minute:02}"

def convert_24_to_12(time_str):
    try:
        hour,minute = map(int , time_str.split(":"))
        suffix= "AM" if hour < 12 else "PM"
        hour = hour % 12
        hour = 12 if hour==0 else hour 
        return f"{hour} : {minute:02} {suffix}"
    except Exception as e:
        return "時間は無効です。"
   
time_format = input("時間制を入力してください（12 or 24）：")
time_str = input("時間を入力してください：")          
        
if time_format =="12" :
    print(f"24時間制：{conver_12_to_24(time_str)}")
elif time_format =="24":
    print(f"12時間制は：{convert_24_to_12(time_str)}")
else:
    print("無効時間です。")