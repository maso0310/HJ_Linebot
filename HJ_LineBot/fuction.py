#lineAPI
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from django.conf import settings
from HJ_LineBot.models import *

#======機器人内建函數======
from HJ_LineBot.fuction import *
from HJ_LineBot.models import *
from HJ_LineBot.MessageForm import *
from HJ_LineBot.flex_set import *
#=========================

#===函數庫===
import re
import json
#===========

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def pushMessage(event,mtext):
    msg = mtext[6:]
    userall = user_message.objects.all()
    uids=[]
    for uid in userall:
        print(uid)
        if str(uid) not in uids:
            uids.append(str(uid))
        else:
            pass
    print(uids)
    message = TextSendMessage(text = msg)
    #line_bot_api.push_message(to=str(uid),messages=message)

def sign_up_pilot(uid):
    sign_up_step = 0
    data = []
    while sign_up_step < 7:
        if sign_up_step == 0:
            message = TextSendMessage(text='請問您是否有操作無人機農噴的經驗？')
            line_bot_api.push_message(to=uid,messages=message)
            data.append(event.message.text)
            sign_up_step = sign_up_step + 1
            continue
        elif sign_up_step == 1:
            message = TextSendMessage(text='請問您是否有農噴用無人機？')
            line_bot_api.push_message(to=uid,messages=message)
            data.append(event.message.text)
            sign_up_step = sign_up_step + 1
            continue
        elif sign_up_step == 2:
            message = TextSendMessage(text='請輸入您的生日')
            line_bot_api.push_message(to=uid,messages=message)
            data.append(event.message.text)
            sign_up_step = sign_up_step + 1
            continue
        elif sign_up_step == 3:
            message = TextSendMessage(text='請輸入您的email')
            line_bot_api.push_message(to=uid,messages=message)
            data.append(event.message.text)
            sign_up_step = sign_up_step + 1
            continue
        elif sign_up_step == 4:
            message = TextSendMessage(text='請輸入您的連絡電話')
            line_bot_api.push_message(to=uid,messages=message)
            data.append(event.message.text)
            sign_up_step = sign_up_step + 1
            continue
        elif sign_up_step == 5:
            message = TextSendMessage(text='請輸入您的通訊地址')
            line_bot_api.push_message(to=uid,messages=message)
            data.append(event.message.text)
            sign_up_step = sign_up_step + 1
            continue
        elif sign_up_step == 6:
            message = TextSendMessage(text='請輸入您可以希望接收任務的地區')
            line_bot_api.push_message(to=uid,messages=message)
            data.append(event.message.text)
            sign_up_step = sign_up_step + 1
            continue
        else:
            break
    return 

from liffpy import (
    LineFrontendFramework as LIFF,
    ErrorResponse
)


def main():
    liff_api = LIFF("8QntITqnfdIc7sU4kBPskoZhOBEFvl3I9a/4OSMraNubY/h3ZwcFY5aDd2O16RPIRWK1f5oY0Aew5LJL91mlnjkP9Ugq6j4c0ZmJp2hWTkGnHUodLdvVcSJj+tCzzH9iyfBrDJ8NMtGln0MwZGWmjAdB04t89/1O/w1cDnyilFU=")

    try:
        # If you want to add LIFF app
        liff_id = liff_api.add(
            view_type="compact",
            view_url="https://https://liff-for-hjuav.herokuapp.com/hotel_form.html")
            # 400 Error or 401 Error
        try:
            # If you want to update LIFF app
            liff_api.update(liff_id, 
            view_type="full",
            view_url="https://https://liff-for-hjuav.herokuapp.com/hotel_form.html")
        except ErrorResponse as err:
            # 401 Error or 404 Error
            print(err.message)
            return 
    except ErrorResponse as err:
        # 401 Error or 404 Error
        print(err.message)
        return 

    try:
        # If you want to get all LIFF apps
        apps_info = liff_api.get()
        for app_info in apps_info:
            try:
                # If you want to delete LIFF app
                liff_api.delete(app_info["liffId"])
            except ErrorResponse as err:
                # 401 Error or 404 Error
                print(err.message)
                return 
    except ErrorResponse as err:
        # 401 Error or 404 Error
        print(err.message)
        return 

def Farmer_member_info(text):
    Farmer_info = []
    pattern_name = '\姓名：.*'
    pattern_crop = '\種植作物別：.*'
    pattern_area = '\種植面積：.*'
    pattern_birth = '\生日：.*'
    pattern_phone = '\聯絡電話：.*'
    pattern_addr = '\地址：.*'
    pattern_email = '\電郵：.*'

    name = re.findall(pattern_name,text)[0][3:]
    crop = re.findall(pattern_crop,text)[0][6:]
    area = re.findall(pattern_area,text)[0][5:]
    birth = re.findall(pattern_birth,text)[0][3:]
    phone = re.findall(pattern_phone,text)[0][5:]
    addr = re.findall(pattern_addr,text)[0][3:]
    email = re.findall(pattern_email,text)[0][3:]
    print(name)
    print(crop)
    print(area)
    print(birth)
    print(phone)
    print(addr)
    print(email)
    b = [name,crop,area,birth,phone,addr,email]
    return b

def Farmer_order_info(text):
    pattern_mission_date = '\日期：.*'
    pattern_mission_crop = '\種植作物：.*'
    pattern_mission_area = '\噴灑面積：.*'
    pattern_mission_item = '\噴灑項目：.*'

    mission_date = re.findall(pattern_mission_date,text)[0][3:]
    mission_crop = re.findall(pattern_mission_crop,text)[0][5:]
    mission_area = re.findall(pattern_mission_area,text)[0][5:]
    mission_item = re.findall(pattern_mission_item,text)[0][5:]
    b = [mission_date,mission_crop,mission_area,mission_item]
    return b

def get_translate(text):
    
    translate = f'{text} 英文'
    
    url = f"https://www.google.com/search?{urllib.parse.urlencode(dict([['oq', translate], ['q', translate]]))}/"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    req = urllib.request.Request(url, headers = headers)
    conn = urllib.request.urlopen(req)

    data = conn.read()
    
    pattern = '<span tabindex="0">\S*</span>'
    match = re.search(pattern, str(data))
    
    return match.group()[19:-7]


def create_flex():
    cotents = {"type":"carousel",
               "contents":[
              { "type": "bubble",
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "農噴預約",
                      "weight": "bold",
                      "color": "#1DB446",
                      "size": "sm"
                    },
                    {
                      "type": "text",
                      "text": str(place_date[0]),
                      "weight": "bold",
                      "size": "xxl",
                      "margin": "md"
                    },
                    {
                      "type": "text",
                      "text": str(mission_addr[0]),
                      "size": "xs",
                      "color": "#aaaaaa",
                      "wrap": True
                    },
                    {
                      "type": "separator",
                      "margin": "xxl"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "margin": "xxl",
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "box",
                          "layout": "horizontal",
                          "contents": [
                            {
                              "type": "text",
                              "text": "作物別",
                              "size": "sm",
                              "color": "#555555",
                              "flex": 0
                            },
                            {
                              "type": "text",
                              "text": str(mission_crop[0]),
                              "size": "sm",
                              "color": "#111111",
                              "align": "end"
                            }
                          ]
                        },
                        {
                          "type": "box",
                          "layout": "horizontal",
                          "contents": [
                            {
                              "type": "text",
                              "text": "噴灑面積",
                              "size": "sm",
                              "color": "#555555",
                              "flex": 0
                            },
                            {
                              "type": "text",
                              "text": str(mission_area[0])+"分地",
                              "size": "sm",
                              "color": "#111111",
                              "align": "end"
                            }
                          ]
                        },
                        {
                          "type": "box",
                          "layout": "horizontal",
                          "contents": [
                            {
                              "type": "text",
                              "text": "噴灑項目",
                              "size": "sm",
                              "color": "#555555",
                              "flex": 0
                            },
                            {
                              "type": "text",
                              "text": str(mission_item[0]),
                              "size": "sm",
                              "color": "#111111",
                              "align": "end"
                            }
                          ]
                        },
                        {
                          "type": "separator",
                          "margin": "xxl"
                        },
                        {
                          "type": "box",
                          "layout": "horizontal",
                          "margin": "xxl",
                          "contents": [
                            {
                              "type": "text",
                              "text": "農友姓名",
                              "size": "sm",
                              "color": "#555555"
                            },
                            {
                              "type": "text",
                              "text": str(name[0]),
                              "size": "sm",
                              "color": "#111111",
                              "align": "end"
                            }
                          ]
                        },
                        {
                          "type": "box",
                          "layout": "horizontal",
                          "contents": [
                            {
                              "type": "text",
                              "text": "聯絡電話",
                              "size": "sm",
                              "color": "#555555"
                            },
                            {
                              "type": "text",
                              "text": str(phone[0]),
                              "size": "sm",
                              "color": "#111111",
                              "align": "end"
                            }
                          ]
                        },
                        {
                          "type": "box",
                          "layout": "horizontal",
                          "contents": [
                            {
                              "type": "text",
                              "text": "經度",
                              "size": "sm",
                              "color": "#555555"
                            },
                            {
                              "type": "text",
                              "text": str(mission_longtitude[0]),
                              "size": "sm",
                              "color": "#111111",
                              "align": "end"
                            }
                          ]
                        },
                        {
                          "type": "box",
                          "layout": "horizontal",
                          "contents": [
                            {
                              "type": "text",
                              "text": "緯度",
                              "size": "sm",
                              "color": "#555555"
                            },
                            {
                              "type": "text",
                              "text": str(mission_latitude[0]),
                              "size": "sm",
                              "color": "#111111",
                              "align": "end"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "separator",
                      "margin": "xxl"
                    },
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "margin": "md",
                      "contents": [
                        {
                          "type": "text",
                          "text": str(order_number[0]),
                          "color": "#FF0000",
                          "size": "md",
                          "align": "center",
                          "gravity": "center"
                        },
                        {
                          "type": "button",
                          "action": {
                            "type": "postback",
                            "label": "接單",
                            "data": "飛手接收訂單編號:\n"+"uid="+str(uid)+"訂單編號"+str(order_number[0])
                          },
                          "position": "relative",
                          "flex": 0,
                          "color": "#00FFFF"
                        }
                      ]
                    }
                  ]
                }
              }
            ]
          }
    return cotents

def Order_List_FlexMessage():
    #基礎設定
    i=1
    contents = dict()
    case = dict()
    flex_link_list = []
    #呼叫資料庫
    all_order = Farmer_Order_completed.objects.all()
    for order in all_order:
        case['%d'%i] = flex_content(order.uid,order.order_number,order.name,order.phone,str(order.mission_date),order.mission_crop,str(order.mission_area),order.mission_item,order.mission_addr,str(order.mission_latitude),str(order.mission_longitude))
        flex_link_list.append(case['%d'%i])
        i=i+1
    #print(flex_link_list)
    contents['type'] = 'carousel'
    contents['contents'] = flex_link_list
    print(type(contents))
    message = FlexSendMessage(alt_text="農噴任務列表",contents=contents)
    print(type(message))
    return message


#測試資料庫的函數功能
def database_info(uid):
    a = Farmer_Order_completed.objects.filter(uid=uid)
    for b in a:
        print(b)
    c = Farmer_Order_completed.objects.all()
    for d in c:
        print(d)

def FarmerMember_Order_List_FlexMessage(uid):
    #基礎設定
    i=1
    contents = dict()
    case = dict()
    flex_link_list = []
    #呼叫資料庫
    all_order = Farmer_Order_completed.objects.all()
    for order in all_order:
        if order.uid==uid:
            case['%d'%i] = flex_content(order.uid,order.order_number,order.name,order.phone,str(order.mission_date),order.mission_crop,str(order.mission_area),order.mission_item,order.mission_addr,str(order.mission_latitude),str(order.mission_longitude))
            flex_link_list.append(case['%d'%i])
            i=i+1
    #print(flex_link_list)
    contents['type'] = 'carousel'
    contents['contents'] = flex_link_list
    print(type(contents))
    message = FlexSendMessage(alt_text="農噴任務列表",contents=contents)
    print(type(message))
    return message
      

'''
這個檔案專門用來設計LINEBOT要用到的函數功能，以下為函數的功能清單：

Catch_User_Message_Info
用來獲得LINEBOT用戶在傳送訊息時的

'''