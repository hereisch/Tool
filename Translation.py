# -*- coding: utf-8 -*-#
import os
import re
from tkinter import scrolledtext
from urllib import request,parse
import requests
import json,time,random
import hashlib
import tkinter as tk
from gtts import gTTS
from playsound import playsound
from threading import Thread


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def md5_jiami(str_data):
    md5_obj = hashlib.md5()
    sign_bytes_data = str_data.encode('utf-8')
    # 调用update()函数，来更新md5_obj值
    md5_obj.update(sign_bytes_data)
    # 返回加密后的str
    sign_str = md5_obj.hexdigest()
    return sign_str


def youdao(word):

    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    now = time.time()
    # print(now)
    # salt = int(now * 1000 + random.randint(0, 9))
    salt_str = str(int(now * 1000)) + str(random.randint(0, 9))
    # print('salt',salt_str)
    # D = "]BjuETDhU)zqSxf-=B#7m"
    D = "Tbh5E8=q6U3EXe+&L[4c@"
    S = "fanyideskweb"
    sign_str = S + word + salt_str + D
    # print('sign',sign_str)
    # 调用加密的方法
    sign_md5_str = md5_jiami(sign_str)
    # print('lts',str(int(now * 1000)))
    # print(sign_md5_str)

    data={
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt_str,
        'sign': sign_md5_str,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
        'lts': int(now* 1000),
        'bv': 'a4da7fd2fcb0c879a8b1e37b497afb19',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        #'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        # 'Content-Length': '404',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'OUTFOX_SEARCH_USER_ID=-493176930@10.168.8.63; OUTFOX_SEARCH_USER_ID_NCOO=38624120.26076847; SESSION_FROM_COOKIE=unknown; JSESSIONID=aaabYcV4ZOU-JbQUha2uw; ___rl__test__cookies=1534210912076',
        'Cookie': 'OUTFOX_SEARCH_USER_ID="1198189498@10.169.0.81"; OUTFOX_SEARCH_USER_ID_NCOO=1009156840.6263105; _ntes_nnid=23db0df873873b73e81570e33a199689,1592908010597; JSESSIONID=aaaSG83gFJ53CgshAi9xx; ___rl__test__cookies=1607483033271',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'X-Requested-With': 'XMLHttpRequest',

    }

    resp = requests.post(url,headers=headers,data=data)
    strs_datas = resp.json()
    print(strs_datas)
    # print(strs_datas['translateResult'])
    strings = ''
    for i in strs_datas['translateResult']:
        for k in i:
            strings += k['tgt']
    # print(strings)
    return strings


def clicked():
    global temp
    text = ipt_text.get(0.0, 5000.0).strip()
    text = re.sub('\n', ' ', text)
    if text != temp:
        # print('发送。。。。。。')
        clean()
        ipt_text.insert(tk.INSERT, text)
        temp = text.strip()
        trans_text = youdao(text)
        result.delete(1.0, 5000.0)
        result.insert(tk.INSERT, trans_text)
        temp = text


def listen(event):
    global temp
    text = ipt_text.get(0.0,5000.0).strip()
    text = re.sub('\n',' ',text)
    if text != temp:
        print('发送。。。。。。')
        clean()
        ipt_text.insert(tk.INSERT, '  '+ re.sub('\. ','.\n  ',text))
        temp = text.strip()
        trans_text = youdao(text)
        trans_text = re.sub('。','。\n  ',trans_text)
        result.delete(1.0,5000.0)
        result.insert(tk.INSERT, '  '+ trans_text)
        temp = text


@async
def text2speech():
    """
    文字转语音，google tts,需修改tts.py源码中 com->cn
    :param text:
    :return: voice
    """

    text = ipt_text.get(0.0, 5000.0).strip()
    text = re.sub('\n', ' ', text)

    tts = gTTS(text,tld='cn')
    tts.save('voice.mp3')
    playsound('voice.mp3')



def clean():
    ipt_text.delete(1.0,5000.0)


if __name__ == '__main__':


    temp = ''
    window = tk.Tk()
    window.title('翻译')
    window.geometry('600x600')
    ipt_text = scrolledtext.ScrolledText(window, width=70, height=20)
    ipt_text.pack()
    ipt_text.grid(column=0, row=0)
    ipt_text.focus()
    ipt_text.bind('<Return>',listen)
    trans = tk.Button(window, text="翻译",command=clicked,font=("Microsoft YaHei", 20))
    trans.grid(column=2, row=1)
    voice = tk.Button(window, text="朗读",command=text2speech,font=("Microsoft YaHei", 20))
    voice.grid(column=2, row=1)
    clear = tk.Button(window, text="清空",command=clean,font=("Microsoft YaHei", 20))
    clear.grid(column=2, row=0)

    result = scrolledtext.ScrolledText(window, width=70, height=20,)
    # trans.pack()
    result.grid(column=0, row=30)

    window.mainloop()



