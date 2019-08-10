import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Cookie": "anonymid=jyktjt32-41m6na; depovince=BJ; _r01_=1; jebe_key=3637201b-0de7-4dc0-ae74-56389ea5488f%7Cdefc3e2fa2f70125542a51139730b9e3%7C1564188802966%7C1%7C1564188803477; jebe_key=3637201b-0de7-4dc0-ae74-56389ea5488f%7Cdefc3e2fa2f70125542a51139730b9e3%7C1564188802966%7C1%7C1564188803480; JSESSIONID=abcQUhsdx0EHZ8X7veYWw; ick_login=46876763-05b0-4b1c-b011-12793e17b36a; loginfrom=null; wp_fold=0; t=5f559fa064a21518ab002a4f33bc18873; societyguester=5f559fa064a21518ab002a4f33bc18873; id=971650203; xnsid=cded4330; jebecookies=10490d73-4b95-43b5-bac6-bc0e70d05870|||||; ver=7.0"
}
temp_url = "http://www.renren.com/971650203/profile"
re = requests.get(temp_url, headers=headers)
print(re.content.decode())
