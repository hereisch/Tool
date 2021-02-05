# Tool
###Translation.py

​	论文翻译工具，自动替换回车为空格，调用有道web api翻译。谷歌语音合成gTTS实现英文朗读。

​	PS：

​	1.修改tts.py 源码中com->cn以解决google translate无法访问

​	2.[playground中播放mp3占用问题](<https://www.freesion.com/article/3021123386/>)，修改playsound.py源码

```python
    if block:
        sleep(float(durationInMS) / 1000.0)
        winCommand('close',alias)  #add this code
```

