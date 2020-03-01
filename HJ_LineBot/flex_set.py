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
#=========================

#===函數庫===
import re
#===========

def Flex_FarmerOrder(uid):
    Order_Information = dict()
    place_date = []
    mission_addr = []
    mission_crop = []
    mission_area = []
    mission_item = []
    name = []
    phone = []
    mission_longtitude = []
    mission_latitude = []
    order_number = []
    order_data_info = Farmer_Order_Temp.objects.all()
    for data_info in order_data_info:
      or_num = data_info.order_number
      date = data_info.mission_date
      crop = data_info.mission_crop
      area = data_info.mission_area
      item = data_info.mission_item
      print(date,crop,area,item)
      order_number.append(or_num)
      place_date.append(date)
      mission_crop.append(crop)
      mission_area.append(area)
      mission_item.append(item)
      farmer_id = data_info.uid
      farmer_member_info = Farmer_member.objects.filter(uid=farmer_id)
      for member_info in farmer_member_info:
        print(farmer_member_info)
        get_name = member_info.name
        get_phone = member_info.phone
        print(get_name,get_phone)
        name.append(get_name)
        phone.append(get_phone)

    order_data_location = Farmer_Order_completed.objects.all()
    for data_location in order_data_location:
      addr = data_location.mission_addr
      longti = data_location.mission_longitude
      latitu = data_location.mission_latitude
      print(addr,longti,latitu)
      mission_addr.append(addr)
      mission_latitude.append(latitu)
      mission_longtitude.append(longti)
    print(
    place_date[0],
    mission_addr,
    mission_crop,
    mission_area,
    mission_item,
    name,
    phone,
    mission_longtitude,
    mission_latitude,
    order_number)
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
                        }]}]}}]}
    print(type(cotents))
    return cotents

def flex_content(uid,order_number,name,phone,mission_date,mission_crop,mission_area,mission_item,mission_addr,mission_latitude,mission_longitude):
    cotents = { "type": "bubble",
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
                      "text": mission_date,
                      "weight": "bold",
                      "size": "xxl",
                      "margin": "md"
                    },
                    {
                      "type": "text",
                      "text": mission_addr,
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
                              "text": mission_crop,
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
                              "text": str(mission_area)+"分地",
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
                              "text": mission_item,
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
                              "text": name,
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
                              "text": phone,
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
                              "text": mission_longitude,
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
                              "text": mission_latitude,
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
                          "text": order_number,
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
                            "data": "飛手接收訂單編號:\n"+"uid="+uid+"訂單編號"+order_number
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
    return cotents

def service_introduction():
    contents = {"type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://storage.googleapis.com/opinion-cms-cwg-tw/article/201909/article-5d8c7d3bb65cb.jpg",
                  "size": "full",
                  "aspectRatio": "20:13",
                  "aspectMode": "cover",
                  "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                  }
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "button",
                      "style": "primary",
                      "height": "md",
                      "action": {
                        "type": "postback",
                        "label": "如何註冊",
                        "data": "如何註冊"
                      },
                      "margin": "xxl"
                    },
                    {
                      "type": "button",
                      "style": "secondary",
                      "height": "md",
                      "action": {
                        "type": "postback",
                        "label": "如何預約",
                        "data": "如何預約"
                      },
                      "margin": "xxl"
                    },
                    {
                      "type": "button",
                      "style": "primary",
                      "height": "md",
                      "action": {
                        "type": "postback",
                        "label": "預約查詢",
                        "data": "預約查詢"
                      },
                      "margin": "xxl"
                    },
                    {
                      "type": "button",
                      "style": "secondary",
                      "height": "md",
                      "action": {
                        "type": "postback",
                        "label": "常見問題",
                        "data": "常見問題"
                      },
                      "margin": "xxl"
                    }
                  ],
                  "flex": 0
                }
              }
    message = FlexSendMessage(alt_text="使用說明",contents=contents)
    return message

def company_service():
    contents = {"type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://cnews.com.tw/wp-content/uploads/E2B22F48-CCA3-410D-AB42-B1A376AA64B8-e1544092778315.jpg",
                  "size": "full",
                  "aspectRatio": "20:13",
                  "aspectMode": "cover",
                  "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                  }
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "spacing": "none",
                  "contents": [
                    {
                      "type": "button",
                      "style": "primary",
                      "height": "md",
                      "action": {
                        "type": "postback",
                        "label": "農噴服務",
                        "data": "農噴服務介紹"
                      },
                      "margin": "xxl",
                      "position": "relative"
                    },
                    {
                      "type": "button",
                      "style": "primary",
                      "height": "md",
                      "action": {
                        "type": "postback",
                        "label": "機體銷售",
                        "data": "預約查詢"
                      },
                      "margin": "xxl"
                    }
                  ]
                }
              }
    message = FlexSendMessage(alt_text="公司服務項目",contents=contents)
    return message

#==========荔枝椿象防治資訊===========

def plant_protect():
    contents ={ "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://s.yimg.com/ny/api/res/1.2/hfME3s7j8LEDmd696nknhg--~A/YXBwaWQ9aGlnaGxhbmRlcjtzbT0xO3c9ODAw/http://media.zenfs.com/zh_hant_tw/News/newtalk/5a6d464dbcd7f.jpgimgmax1200",
                  "size": "full",
                  "aspectRatio": "20:13",
                  "aspectMode": "cover",
                  "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                  }
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "spacing": "none",
                  "contents": [
                    {
                      "type": "button",
                      "style": "primary",
                      "height": "md",
                      "action": {
                        "type": "postback",
                        "label": "荔枝椿象特徵",
                        "data": "荔枝椿象特徵"
                      },
                      "margin": "xxl",
                      "position": "relative"
                    },
                    {
                      "type": "button",
                      "style": "secondary",
                      "height": "md",
                      "action": {
                        "type": "postback",
                        "data": "荔枝椿象簡介",
                        "label": "荔枝椿象簡介"
                      },
                      "position": "relative",
                      "margin": "xxl"
                    },
                    {
                      "type": "button",
                      "style": "primary",
                      "height": "md",
                      "action": {
                        "type": "postback",
                        "label": "荔枝椿象危害",
                        "data": "荔枝椿象危害"
                      },
                      "margin": "xxl"
                    },
                    {
                      "type": "button",
                      "style": "secondary",
                      "height": "md",
                      "action": {
                        "type": "postback",
                        "label": "荔枝椿象防治",
                        "data": "荔枝椿象防治"
                      },
                      "margin": "xxl"
                    }
                  ],
                  "flex": 0,
                  "margin": "none",
                  "backgroundColor": "#FFFFFF"
                }
              }
    message = FlexSendMessage(alt_text="防治資訊",contents=contents)
    return message

def Lichi_bug_introduction():
    contents = {"type": "bubble",
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "簡介及生活史",
                      "weight": "bold",
                      "size": "xxl",
                      "margin": "md"
                    },
                    {
                      "type": "text",
                      "text": "荔枝椿象",
                      "margin": "md"
                    },
                    {
                      "type": "separator",
                      "margin": "sm"
                    },
                    {
                      "type": "text",
                      "text": "一年一世代，雌蟲每次產卵約 14 個卵，雌蟲一生當中至少產卵 5-10 次，成蟲產卵期自 3 月中旬至 10 月上旬，以 4、5 月為產卵盛期，卵粒不會有毒性。\n\n卵孵化後，初齡若蟲有群集取食現象，二齡後逐漸分散危害，蟲體受到干擾時有假死現象，並掉落於地，但很快就往樹上爬；若蟲抗飢力強，可達約 7 日不取食，若蟲期會分泌臭液惟毒性不強。\n\n五齡若蟲發育至成蟲期間，會大量取食累積脂肪，準備越冬，越冬成蟲內具較多脂肪。",
                      "margin": "xxl",
                      "wrap": True
                    },
                    {
                      "type": "separator",
                      "margin": "xxl"
                    },
                    {
                      "type": "text",
                      "text": "資料來源：農業害蟲智能管理決策系統",
                      "margin": "md",
                      "size": "xxs",
                      "align": "end"
                    }
                  ]
                },
                "styles": {
                  "footer": {
                    "separator": True
                  }
                }
              }
    message = FlexSendMessage(alt_text="荔枝椿象簡介",contents=contents)
    return message


def Lichi_bug_photo():
    contents = {"type": "carousel",
                "contents": [
                  {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                      "type": "image",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "320:213",
                      "url": "https://lh3.googleusercontent.com/proxy/zwhEb1Od5thYnGXiDjT1JsV-nWK9iTM5g2bl1AWwDH65OtAG7DAkpjexw4hs3-hqq3On-HrRUyLJdAFXisee6OrQ9NaI76yKNW4en9TUEuCB2NgqTdngUZerVLcLe8wgNAZB9ZunDrD5RHRxLTKXbXu_MHmTdAJCSB0JedU3PJkS_PbVsp95EIwLKxBkXE_z-sovuh1DSR2QsKKtJ02bKtYY6EJlm9_UINWohe5JeLaXv3mtChlGWihqzHD_72IMJYtnVC9TqaAU2IqISyNLRvJ26tH6i0NF3Ia6vIRC2pH-P9Rpm7w0oUCnwGflzlhj_WHs5TzydN8MQewPzC6ldAa6"
                    },
                    "body": {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "text",
                          "text": "荔枝椿象",
                          "weight": "bold",
                          "size": "sm",
                          "wrap": True,
                          "gravity": "top",
                          "align": "start",
                          "position": "relative"
                        },
                        {
                          "type": "text",
                          "text": "卵"
                        }
                      ],
                      "spacing": "sm",
                      "paddingAll": "10px"
                    }
                  },
                  {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                      "type": "image",
                      "url": "https://7.share.photo.xuite.net/mbbrgs/1757d34/11687359/551978869_m.jpg",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "320:213"
                    },
                    "body": {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "text",
                          "text": "荔枝椿象",
                          "weight": "bold",
                          "size": "sm",
                          "wrap": True
                        },
                        {
                          "type": "text",
                          "text": "幼蟲"
                        }
                      ],
                      "spacing": "sm",
                      "paddingAll": "13px"
                    }
                  },
                  {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                      "type": "image",
                      "url": "https://images.chinatimes.com/newsphoto/2018-05-29/900/B13A00_P_05_01.jpg",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "320:213"
                    },
                    "body": {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "text",
                          "text": "荔枝椿象",
                          "weight": "bold",
                          "size": "sm"
                        },
                        {
                          "type": "text",
                          "text": "成熟若蟲"
                        }
                      ],
                      "spacing": "sm",
                      "paddingAll": "13px"
                    }
                  },
                  {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                      "type": "image",
                      "url": "https://www.omgtw.com/upload/article/original/023ce1d13c3890e789a75c0c36a537b5.jpg",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "320:213"
                    },
                    "body": {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "text",
                          "text": "荔枝椿象",
                          "weight": "bold",
                          "size": "sm"
                        },
                        {
                          "type": "text",
                          "text": "成蟲"
                        }
                      ],
                      "spacing": "sm",
                      "paddingAll": "13px"
                    }
                  },
                  {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                      "type": "image",
                      "url": "https://1.share.photo.xuite.net/m49.k5083/115531c/8661047/1165435621_l.jpg",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "320:213"
                    },
                    "body": {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "text",
                          "text": "荔枝椿象",
                          "weight": "bold",
                          "size": "sm"
                        },
                        {
                          "type": "text",
                          "text": "果實危害"
                        }
                      ],
                      "spacing": "sm",
                      "paddingAll": "13px"
                    }
                  },
                  {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                      "type": "image",
                      "url": "https://lh3.googleusercontent.com/proxy/PjnvQ4AptyqsnIb5xBhVN0gRGOYnoM8GQafwirZ_TbHtJP9-ZGdVU3zssO6kMNVgQyeEYWIAFWFgq5jluXM0y0bi2TVcYjcm9x5UZ4ROkHmwfW_MEB0AJh4RnPXc5baN_9WX_iUZqtMoyYmRDR-qGhiPbEGAkS8PZ_iC6jJgfiyQIscOf7SoCJBcilErhMcW9yma6C52GDMx_u4KhXTUuK3QTYmx8QmrxkLXbHaQeW5ArUpW3svXS3uGK2yh8aitzfD_DLZqwNL3ZbrDaxzA2yoqRFTXjerwBk7Q9FaWEbpWZ48lNIhPwIlo10JUz-njZKfZL-0id_sjwz-CZ-Wq8h8SNRGfzIh7bLq2",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "320:213"
                    },
                    "body": {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "text",
                          "text": "荔枝椿象",
                          "weight": "bold",
                          "size": "sm"
                        },
                        {
                          "type": "text",
                          "text": "吸食嫩芽"
                        }
                      ],
                      "spacing": "sm",
                      "paddingAll": "13px"
                    }
                  }
                ]
              }
    message = FlexSendMessage(alt_text="荔枝椿象特徵",contents=contents)
    return message

def Lichi_bug_harm():
    contents ={ "type": "carousel",
                "contents": [
                  {
                    "type": "bubble",
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "危害概述",
                          "weight": "bold",
                          "size": "xxl",
                          "margin": "md"
                        },
                        {
                          "type": "text",
                          "text": "荔枝椿象",
                          "size": "md",
                          "wrap": True,
                          "margin": "md"
                        },
                        {
                          "type": "separator",
                          "margin": "xxl"
                        },
                        {
                          "type": "text",
                          "text": "危害方式： \n刺吸式口器吸食荔枝與龍眼的嫩芽、嫩梢、花穗和幼果。 \n\n危害特徵： \n落花、落果，嫩枝、幼果枯萎及果皮黑化等。嚴重時枝葉生長遲緩、花穗萎縮或脫落、甚至整個植株枯死。 \n\n後續影響： \n可傳播荔枝或龍眼鬼帚病 (Longan witch’s broom)，且其危害傷口也利於荔枝露疫病菌 (Peronophythora litchii) 入侵。\n\n\n\n",
                          "margin": "xxl",
                          "size": "md",
                          "wrap": True
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
                              "text": "資料來源：農業害蟲智能管理決策系統",
                              "size": "xs",
                              "align": "end"
                            }
                          ]
                        }
                      ]
                    },
                    "styles": {
                      "footer": {
                        "separator": True
                      }
                    }
                  },
                  {
                    "type": "bubble",
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "image",
                          "url": "https://lh3.googleusercontent.com/proxy/TeYZuO4rFKxOTTE4hK_1Crcy_rdkd4S-s8VIoROVLBkHKWFnoQHGnQpQufa_wJyUyGTPc_wo12QmvRf7xX5NMXbvgB45e2-icAfMHN0Xry_2Y6L8UsFQwFBH7-jDxTXEQogTZwyIRQFMzW1RrEiGheY6_cIHrlJGy2TANSJR5DiMbzlA3mD1YGI5NKbddH__II45qpqWbdPGcAwuPU5efalk1Ok0KqdN-YLIUImYaRemWABMO9-7D4YcL0KdxWdsGebx3chFw_VQXFlbR79T204voWU6jn--dKo1QnBiAnVIgtaeqp5ZLsjAact5G7qQ2IGFdwEg9Sg3B0dKjoXBwIGF_BA-uah-VbTVCtsCOVmSFKc",
                          "size": "full",
                          "margin": "none",
                          "offsetTop": "3px",
                          "aspectMode": "cover"
                        },
                        {
                          "type": "separator",
                          "margin": "xxl"
                        },
                        {
                          "type": "text",
                          "text": "危害作物",
                          "weight": "bold",
                          "size": "xxl",
                          "margin": "md"
                        },
                        {
                          "type": "separator",
                          "margin": "xxl"
                        },
                        {
                          "type": "text",
                          "text": "荔枝、龍眼、台灣欒樹",
                          "margin": "xxl",
                          "size": "md"
                        },
                        {
                          "type": "separator",
                          "margin": "xxl"
                        },
                        {
                          "type": "text",
                          "text": "危害部位",
                          "weight": "bold",
                          "size": "xxl",
                          "margin": "md"
                        },
                        {
                          "type": "separator",
                          "margin": "xxl"
                        },
                        {
                          "type": "text",
                          "text": "枝梢、花穗。",
                          "margin": "xxl"
                        },
                        {
                          "type": "separator",
                          "margin": "xxl"
                        }
                      ]
                    },
                    "styles": {
                      "footer": {
                        "separator": True
                      }
                    }
                  }
                ]
              }
    message = FlexSendMessage(alt_text="荔枝椿象危害",contents=contents)
    return message

def Lichi_bug_protection():
    contents ={
                "type": "carousel",
                "contents": [
                  {
                    "type": "bubble",
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "防治方法",
                          "weight": "bold",
                          "size": "xxl",
                          "margin": "md"
                        },
                        {
                          "type": "text",
                          "text": "荔枝椿象",
                          "size": "md",
                          "wrap": True,
                          "margin": "md"
                        },
                        {
                          "type": "separator",
                          "margin": "xxl"
                        },
                        {
                          "type": "text",
                          "text": "最佳防治策略係利用荔枝龍眼生長期及荔枝椿象本身生態特性來擬定，可分為化學防治、生物防治及物裡防治。\n\n尤其越冬後的成蟲因消耗體內脂肪對藥劑的容忍度降低，此時為最佳的化學防治時期。",
                          "margin": "xxl",
                          "wrap": True
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
                              "text": "資料來源：農業害蟲智能管理決策系統",
                              "size": "xs",
                              "align": "end"
                            }
                          ]
                        }
                      ]
                    },
                    "styles": {
                      "footer": {
                        "separator": True
                      }
                    }
                  },
                  {
                    "type": "bubble",
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "化學防治",
                          "weight": "bold",
                          "size": "xxl",
                          "margin": "md"
                        },
                        {
                          "type": "text",
                          "text": "荔枝椿象",
                          "size": "md",
                          "wrap": True,
                          "margin": "md"
                        },
                        {
                          "type": "separator",
                          "margin": "xxl"
                        },
                        {
                          "type": "text",
                          "text": "成蟲越冬後，極需補充食物作為交尾繁殖繁之能量，約 1 月下旬至 2-3 月開花期前，實施 2-3 次藥劑防治，依農藥資訊服務網推薦藥劑施用，並建議採區域防治觀念，同步實施防治，噴藥時最好選擇早上十點(氣溫約低於 20℃)。",
                          "margin": "xxl",
                          "wrap": True
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
                              "text": "資料來源：農業害蟲智能管理決策系統",
                              "size": "xs",
                              "align": "end"
                            }
                          ]
                        }
                      ]
                    },
                    "styles": {
                      "footer": {
                        "separator": True
                      }
                    }
                  },
                  {
                    "type": "bubble",
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "生物防治",
                          "weight": "bold",
                          "size": "xxl",
                          "margin": "md"
                        },
                        {
                          "type": "text",
                          "text": "荔枝椿象",
                          "size": "md",
                          "wrap": True,
                          "margin": "md"
                        },
                        {
                          "type": "separator",
                          "margin": "xxl"
                        },
                        {
                          "type": "text",
                          "text": "荔枝及龍眼開花期間，應停止藥劑防治，藉此提高蜜蜂授粉，同時適值荔枝椿象產卵期，可配合施放平腹小蜂或物理防治，減少族群數量。",
                          "margin": "xxl",
                          "wrap": True
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
                              "text": "資料來源：農業害蟲智能管理決策系統",
                              "size": "xs",
                              "align": "end"
                            }
                          ]
                        }
                      ]
                    },
                    "styles": {
                      "footer": {
                        "separator": True
                      }
                    }
                  },
                  {
                    "type": "bubble",
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "化學及物理防治",
                          "weight": "bold",
                          "size": "xxl",
                          "margin": "md"
                        },
                        {
                          "type": "text",
                          "text": "荔枝椿象",
                          "size": "md",
                          "wrap": True,
                          "margin": "md"
                        },
                        {
                          "type": "separator",
                          "margin": "xxl"
                        },
                        {
                          "type": "text",
                          "text": "開花期結束，進入果實發育期可配合荔枝細蛾防治藥劑，藉此時撲殺荔枝椿象。荔枝龍眼結果期，此時期荔枝椿象進入若蟲期，若蟲不具飛行能力，輕拍蟲體會掉落地上，可以樹幹基部塗黏膠，防止若蟲再爬進數梢為害。",
                          "margin": "xxl",
                          "wrap": True
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
                              "text": "資料來源：農業害蟲智能管理決策系統",
                              "size": "xs",
                              "align": "end"
                            }
                          ]
                        }
                      ]
                    },
                    "styles": {
                      "footer": {
                        "separator": True
                      }
                    }
                  },
                  {
                    "type": "bubble",
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "清園",
                          "weight": "bold",
                          "size": "xxl",
                          "margin": "md"
                        },
                        {
                          "type": "text",
                          "text": "荔枝椿象",
                          "size": "md",
                          "wrap": True,
                          "margin": "md"
                        },
                        {
                          "type": "separator",
                          "margin": "xxl"
                        },
                        {
                          "type": "text",
                          "text": "荔枝、龍眼清園整枝期間，可實施 2 次藥劑防治，可同時壓制冬眠族群的存活率。",
                          "margin": "xxl",
                          "wrap": True
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
                              "text": "資料來源：農業害蟲智能管理決策系統",
                              "size": "xs",
                              "align": "end"
                            }
                          ]
                        }
                      ]
                    },
                    "styles": {
                      "footer": {
                        "separator": True
                      }
                    }
                  }
                ]
              }
    message = FlexSendMessage(alt_text="荔枝椿象防治",contents=contents)
    return message
