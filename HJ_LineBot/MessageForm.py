'''
LINE的各種訊息介面
使用方法舉例

from MessageForm import *
test = sticker_message(1,2)
line_bot_api.reply_message(event.reply_token,test)
'''

#lineAPI
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#文字訊息介面TextSendMessage 
def text_message(text1):
    message = TextSendMessage(text=text1)
    return message

#圖片訊息介面ImageSendMessage
def image_message(url):
    message = ImageSendMessage(
        original_content_url=url,
        preview_image_url=url
    )
    return message

#影片訊息VideoSendMessage
def vedio_message(video_url,picture_url):
    message = VideoSendMessage(
        original_content_url='https://example.com/original.mp4',
        preview_image_url='https://example.com/preview.jpg'
    )
    return message

#AudioSendMessage(音訊訊息)
def audio_message(url,during_time_ms):
    message = AudioSendMessage(
    original_content_url='https://example.com/original.m4a',
    duration=240000
)

#LocationSendMessage(位置訊息)
def Location_message(title,address,latitude,longitude):
    message = LocationSendMessage(
        title=title,
        address=address,
        latitude=latitude,
        longitude=longitude
    )
    return message

#StickerSendMessage(貼圖訊息)
def sticker_message(package_id,sticker_id):
    message = StickerSendMessage(
        package_id=package_id,
        sticker_id=sticker_id
    )
    return message

#ImagemapSendMessage(組圖訊息)
def imagemap_message(base_url,url1,url2,url3,url4):
    message = ImagemapSendMessage(
        base_url=base_url,
        alt_text='又有新的消息了！',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                link_uri=url1,
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                link_uri=url2,
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                link_uri=url3,
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                link_uri=url4,
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=1000
                )
            )
        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message_member():
    message = TemplateSendMessage(
        alt_text='確認會員資料',
        template=ButtonsTemplate(
            title='會員資料是否正確?',
            text="請確認您的會員資料",
            actions=[
                PostbackAction(
                    label="是",
                    data="會員資料正確"
                ),
                PostbackAction(
                    label="否",
                    data="會員資料錯誤"
                )
            ]
        )
    )
    return message


#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template_member():
    message = TemplateSendMessage(
        alt_text='確認會員資料',
        template=ConfirmTemplate(
            text="會員資料是否正確?",
            actions=[
                PostbackTemplateAction(
                    label="是",
                    data="會員資料正確"
                ),
                PostbackTemplateAction(
                    label="否",
                    data="會員資料錯誤"
                )
            ]
        )
    )
    return message

def Confirm_Template_order():
    message = TemplateSendMessage(
        alt_text='訂單預約資料',
        template=ConfirmTemplate(
            text="預約資料是否正確?",
            actions=[
                PostbackTemplateAction(
                    label="是",
                    data="預約資料正確"
                ),
                PostbackTemplateAction(
                    label="否",
                    data="預約資料錯誤"
                )
            ]
        )
    )
    return message


#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://www.awastea.com/App_Script/DisplayCut.ashx?file=product/201904021638240.jpg&w=353&h=353',
                    title='測試看看囉',
                    text='會長這樣',
                    actions=[
                        URITemplateAction(
                            label='點我看物件',
                            uri='http://www.twhg.com.tw/match/obj_view3.php?sid=TP130&liT=3&hash=5d2353308d3d1'
                        )
                    ]
                )
            ]
        )
    )
    return message


#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1(
    image_url0,label0,url0
):
    message = TemplateSendMessage(
        alt_text='快來看有什麼好消息！',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url=image_url0,
                    action=URITemplateAction(
                        label=label0,
                        uri=url0
                    )
                )
            ]
        )
    )
    return message


def image_carousel_message10(
    image_url0,label0,url0,
    image_url1,label1,url1,
    image_url2,label2,url2,
    image_url3,label3,url3,
    image_url4,label4,url4,
    image_url5,label5,url5,
    image_url6,label6,url6,
    image_url7,label7,url7,
    image_url8,label8,url8,
    image_url9,label9,url9
):
    message = TemplateSendMessage(
        alt_text='又有好康優惠囉！',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url=image_url0,
                    action=URITemplateAction(
                        label=label0,
                        uri=url0
                    )
                ),
                ImageCarouselColumn(
                    image_url=image_url1,
                    action=URITemplateAction(
                        label=label1,
                        uri=url1
                    )
                ),
                ImageCarouselColumn(
                    image_url=image_url2,
                    action=URITemplateAction(
                        label=label2,
                        uri=url2
                    )
                ),
                ImageCarouselColumn(
                    image_url=image_url3,
                    action=URITemplateAction(
                        label=label3,
                        uri=url3
                    )
                ),
                ImageCarouselColumn(
                    image_url=image_url4,
                    action=URITemplateAction(
                        label=label4,
                        uri=url4
                    )
                ),
                ImageCarouselColumn(
                    image_url=image_url5,
                    action=URITemplateAction(
                        label=label5,
                        uri=url5
                    )
                ),
                ImageCarouselColumn(
                    image_url=image_url6,
                    action=URITemplateAction(
                        label=label6,
                        uri=url6
                    )
                ),
                ImageCarouselColumn(
                    image_url=image_url7,
                    action=URITemplateAction(
                        label=label7,
                        uri=url7
                    )
                ),
                ImageCarouselColumn(
                    image_url=image_url8,
                    action=URITemplateAction(
                        label=label8,
                        uri=url8
                    )
                ),
                ImageCarouselColumn(
                    image_url=image_url9,
                    action=URITemplateAction(
                        label=label9,
                        uri=url9
                    )
                )
            ]
        )
    )
    return message