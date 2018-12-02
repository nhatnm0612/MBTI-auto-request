from urllib.error import URLError
from socket import timeout
import urllib.request
import urllib.parse
import pandas as pd
import numpy as np
import json


def personality_type(forms, url="https://www.16personalities.com/test-results"):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36")
    method = urllib.parse.urlencode({"_token":"8mTxGLIQeboCvPsjAUerjN6rsQm2LzvoxwGRbLVO",
                                     "options":"on","code":"",
                                     "a1":forms[0],"a2":forms[1],"a3":forms[2],"a4":forms[3],"a5":forms[4],
                                     "a6":forms[5],"a7":forms[6],"a8":forms[7],"a9":forms[8],"a10":forms[9],
                                     "a11":forms[10],"a12":forms[11],"a13":forms[12],"a14":forms[13],"a15":forms[14],
                                     "a16":forms[15],"a17":forms[16],"a18":forms[17],"a19":forms[18],"a20":forms[19],
                                     "a21":forms[20],"a22":forms[21],"a23":forms[22],"a24":forms[23],"a25":forms[24],
                                     "a26":forms[25],"a27":forms[26],"a28":forms[27],"a29":forms[28],"a30":forms[29],
                                     "a31":forms[30],"a32":forms[31],"a33":forms[32],"a34":forms[33],"a35":forms[34],
                                     "a36":forms[35],"a37":forms[36],"a38":forms[37],"a39":forms[38],"a40":forms[39],
                                     "a41":forms[40],"a42":forms[41],"a43":forms[42],"a44":forms[43],"a45":forms[44],
                                     "a46":forms[45],"a47":forms[46],"a48":forms[47],"a49":forms[48],"a50":forms[49],
                                     "a51":forms[50],"a52":forms[51],"a53":forms[52],"a54":forms[53],"a55":forms[54],
                                     "a56":forms[55],"a57":forms[56],"a58":forms[57],"a59":forms[58],"a60":forms[59],}).encode("utf-8")
    try:
        resp = urllib.request.urlopen(req, data = method, timeout = 3).read()
        TYPE = resp.decode("utf-8")
        return json.loads(TYPE)["type"]
    except (timeout, TimeoutError, URLError):
        print("[Timeout Error]", end=' ')
        personality_type(forms, url="https://www.16personalities.com/test-results")


df = pd.read_csv("MBTI .csv", skiprows=0).iloc[:, 2:62].astype(dtype='int32', errors='ignore')
rows, cols = df.shape

dummy_array = np.array([-3] * rows * cols).reshape(rows, cols)
final_array = np.array(df + dummy_array)
for i, forms in enumerate(final_array):
    print(f'> REMAINING: {rows - i - 1}/{rows}', end=' ')
    t = personality_type(forms)
    print(t)
