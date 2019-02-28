# MyPyTools
自己使用Python写的小工具合集

## Contents
-[Meistertask桌面应用壁纸修改工具](##mtbgconfig)

-[北邮研究生选课捡漏工具2019](##checkoutLessonAvailable)

## mtbgconfig
Meistertask桌面应用壁纸修改工具
### 使用方法
#### 1.壁纸生成
使用Photoshop编辑壁纸，修改为特定分辨率和形式，其中./psd/wallpaper.psd为主壁纸，./psd/wallpaperblur.psd为模糊的壁纸。
均导出为web所用格式，若最终显示效果中图片显示不全或模糊，可调节导出品质（高或低）
#### 2.修改配置文件
配置文件为./config/config.json
```json
{
    "path":"C:\\Users\\98585\\AppData\\Roaming\\MeisterTask\\Cache",
    "threshold":100,
    "wallpaper":".\\config\\7.jpg",
    "wallpaperBlur":".\\config\\7b.jpg"
}
```
path为Meistertask应用缓存路径，不同平台路径不同
threshold为自动判断主壁纸和模糊壁纸的阈值，单位为Kb，（一般主壁纸大于100KB，模糊壁纸小于100KB）
wallpaper为待替换的主壁纸相对路径
wallpaperBlur为待替换的模糊壁纸相对路径
#### 3.关闭Meistertask应用
随便选择一个随机壁纸后，退出Meistertask
#### 4.运行脚本./setwallpaper.py
python版本为python3
#### 5.重启应用

## checkoutLessonAvailable
选课捡漏工具【没选到课不用愁，捡漏工具显身手，嗯】
适用于北邮研究生选课系统2019
有课微信提醒
