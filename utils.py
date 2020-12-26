import os
import json

from linebot import LineBotApi, WebhookParser
from linebot.models import *


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(str(channel_access_token))

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_go_to_menu_button(reply_token):
    confirm_template = TemplateSendMessage(
        alt_text="Are you lost?",
        template=ConfirmTemplate(
            text="Go to Menu!",
            actions=[
                MessageTemplateAction(
                    label="Go to Menu",
                    text="Menu"
                ),
                MessageTemplateAction(
                    label="Yes!",
                    text="Menu"
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, confirm_template)
    return "OK"

#Iphone 12 models
def send_IP12_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Apple",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Apple"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

def send_IP12_Pro_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Pro Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Pro Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Pro Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Pro Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Apple",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Apple"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

def send_IP12_Pro_Max_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Pro Max Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Pro Max Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Pro Max Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Pro Max Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Apple",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Apple"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

def send_IP12_Mini_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Mini Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Mini Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Mini Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Mini Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Apple",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Apple"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

#send video
def send_video(reply_token, vid_url, image):
    video_message = VideoSendMessage(
            original_content_url=vid_url,
            preview_image_url=image
        )
    
    line_bot_api.reply_message(reply_token, video_message)

    return "OK"

#send info
def send_info(reply_token, word, information, current, brand):
    line_bot_api.reply_message(reply_token, 
        FlexSendMessage(
            "Information",
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": word,
                        "weight": "bold",
                        "size": "xxl",
                        "margin": "md"
                    },
                    {
                        "type": "separator",
                        "margin": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": information,
                            "wrap": True,
                        },
                        ],
                        "spacing": "sm",
                        "margin": "xxl"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "text",
                        "text": "Where do you want to go?",
                        "size": "sm",
                        "wrap": True,
                        "margin": "xxl"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "Menu",
                        "text": "Menu"
                        },
                        "height": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": brand,
                        "text": brand
                        },
                        "height": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": current,
                        "text": current
                        },
                        "height": "sm"
                    },
                    ]
                },
                "styles": {
                    "footer": {
                    "separator": True
                    }
                }
            }
        )
    )
    return "OK"

#send info 2
def send_info_2(reply_token, word, information, current, brand, series):
    line_bot_api.reply_message(reply_token, 
        FlexSendMessage(
            "Information",
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": word,
                        "weight": "bold",
                        "size": "xxl",
                        "margin": "md"
                    },
                    {
                        "type": "separator",
                        "margin": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": information,
                            "wrap": True,
                        },
                        ],
                        "spacing": "sm",
                        "margin": "xxl"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "text",
                        "text": "Where do you want to go?",
                        "size": "sm",
                        "wrap": True,
                        "margin": "xxl"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "Menu",
                        "text": "Menu"
                        },
                        "height": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": series,
                        "text": series
                        },
                        "height": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": brand,
                        "text": brand
                        },
                        "height": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": current,
                        "text": current
                        },
                        "height": "sm"
                    },
                    ]
                },
                "styles": {
                    "footer": {
                    "separator": True
                    }
                }
            }
        )
    )
    return "OK"

#send menu
def send_Menu_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Apple",
                    text="Wanna own an Apple phone?",
                    thumbnail_image_url="https://as-images.apple.com/is/og-default?wid=1200&hei=630&fmt=jpeg&qlt=95&op_usm=0.5,0.5&.v=1525370171638",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Apple"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Asus",
                    text="Wanna own a Asus phone?",
                    thumbnail_image_url="https://www.asus.com/websites/IN/Sno/91059.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Asus"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Google",
                    text="Wanna own a Google phone?",
                    thumbnail_image_url="https://images.theconversation.com/files/93616/original/image-20150902-6700-t2axrz.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1000&fit=clip",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Google"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Sony",
                    text="Wanna own a Sony phone?",
                    thumbnail_image_url="https://i.pinimg.com/originals/b8/16/18/b81618a49af61d212187ebcb997d96e9.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Sony"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

#Apple
def send_Apple_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Apple Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Iphone 12",
                    text="Wanna own an Iphone 12?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-12.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Iphone 12 Pro",
                    text="Wanna own an Iphone 12 Pro?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-12-pro--.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Pro"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Iphone 12 Mini",
                    text="Wanna own an Iphone 12 Mini?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-12-mini.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Mini"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Iphone 12 Pro Max",
                    text="Wanna own an Iphone 12 Pro Max?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-12-pro-max-.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 Pro Max"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

#GOOGLE

def send_Google_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Google Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Pixel 5",
                    text="Wanna own a Pixel 5?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/google-pixel-5-5g.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 5"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pixel 4a",
                    text="Wanna own a Pixel 4a?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/google-pixel-4a.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 4a"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pixel 4a 5G",
                    text="Wanna own a Pixel 4a 5G?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/google-pixel-4a-5g.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 4a 5G"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

def send_Pixel_5_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 5 Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 5 Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 5 Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 5 Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="MKBHD Review",
                    text="Wanna see Pixel 5 Review?",
                    thumbnail_image_url="https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 5 Video"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Google",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Google"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

def send_Pixel_4a_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 4a Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 4a Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 4a Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 4a Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="MKBHD Review",
                    text="Wanna see Pixel 4a Review?",
                    thumbnail_image_url="https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 4a Video"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Google",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Google"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

def send_Pixel_4a_5G_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 4a 5G Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 4a 5G Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 4a 5G Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 4a 5G Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pocketnow Review",
                    text="Wanna see Pixel 4a 5G Review?",
                    thumbnail_image_url="https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Pixel 4a 5G Video"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Google",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Google"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

#Sony
def send_Sony_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Sony Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Xperia 10 II",
                    text="Wanna own a Xperia 10 II?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/sony-xperia-10-II-o.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 10 II"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Xperia 1 II",
                    text="Wanna own a Xperia 1 II?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/sony-xperia-1-II-o.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 1 II"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Xperia 5 II",
                    text="Wanna own a Xperia 5 II?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/sony-xperia-5-ii-5g-r.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 5 II"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

def send_Xperia_5_II_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 5 II Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 5 II Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 5 II Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 5 II Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="GSMArena Review",
                    text="Wanna see Xperia 5 II Review?",
                    thumbnail_image_url="https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 5 II Video"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Sony",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Sony"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

def send_Xperia_1_II_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 1 II Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 1 II Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 1 II Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 1 II Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="GSMArena Review",
                    text="Wanna see Xperia 1 II Review?",
                    thumbnail_image_url="https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 1 II Video"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Sony",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Sony"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

def send_Xperia_10_II_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 10 II Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 10 II Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 10 II Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 10 II Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="GSMArena Review",
                    text="Wanna see Xperia 10 II Review?",
                    thumbnail_image_url="https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Xperia 10 II Video"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Sony",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Sony"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

#Asus
def send_Asus_chooser(reply_token):
    line_bot_api.reply_message(reply_token, 
        FlexSendMessage(
            "Information",
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Choose which series!",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "md"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "Zenfone",
                        "text": "Zenfone"
                        },
                        "height": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "ROG",
                        "text": "ROG"
                        },
                        "height": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "Menu",
                        "text": "Menu"
                        },
                        "height": "sm"
                    },
                    ]
                },
                "styles": {
                    "footer": {
                    "separator": True
                    }
                }
            }
        )
    )
    return "OK"

def send_Zenfone_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Zenfone Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Zenfone 7",
                    text="Wanna own a Zenfone 7?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/asus-zenfone7-pro-zs670ks-zs671ks.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone 7"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Zenfone 7 Pro",
                    text="Wanna own a Zenfone 7 Pro?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/asus-zenfone7-pro-zs670ks-zs671ks-b.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone 7 Pro"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Asus",
                    text="Return Asus",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Asus"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

def send_ROG_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="ROG Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="ROG Phone 3 Strix",
                    text="Wanna own a ROG Phone 3 Strix?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/asus-rog-phone3-strix.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="ROG Phone 3 Strix"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Asus",
                    text="Return Asus",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Asus"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

#Zenfone 7 Pro
def send_Zenfone_7_Pro_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone 7 Pro Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone 7 Pro Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone 7 Pro Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone 7 Pro Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="GSMArena Review",
                    text="Wanna see Zenfone 7 Pro Review?",
                    thumbnail_image_url="https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone 7 Pro Video"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Zenfone",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Asus",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Asus"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

#Zenfone 7
def send_Zenfone_7_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone 7 Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone 7 Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone 7 Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone 7 Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Aotter Girls Review",
                    text="Wanna see Zenfone 7 Review?",
                    thumbnail_image_url="https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone 7 Video"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Zenfone",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Zenfone"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Asus",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Asus"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

#ROG Phone 3 Strix
def send_ROG_Phone_3_Strix_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Options",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="Price $$$",
                    text="Let's see if you can afford it HAHAHA",
                    thumbnail_image_url="https://everyaustraliancounts.com.au/wp-content/uploads/price-wood.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="ROG Phone 3 Strix Price"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see the specs of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="ROG Phone 3 Strix Specs"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know the pros and cons?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="ROG Phone 3 Strix Pros and Cons"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Antutu Benchmark",
                    text="Wanna see how powerful is your device?",
                    thumbnail_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkTpTs5D_l_o2c9OAvFTC7ZW4VEowytaFm0Q&usqp=CAU",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="ROG Phone 3 Strix Benchmark Score"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="its SAMthing's Review",
                    text="Wanna see ROG Phone 3 Strix Review?",
                    thumbnail_image_url="https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="ROG Phone 3 Strix Video"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return ROG",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="ROG"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Go back",
                    text="Return Asus",
                    thumbnail_image_url="https://static.thenounproject.com/png/393244-200.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Asus"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="Return Menu",
                    thumbnail_image_url="https://www.materialui.co/materialIcons/navigation/menu_grey_192x192.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

#fsm
def send_fsm(reply_token):
    line_bot_api.reply_message(
        reply_token,
        ImageSendMessage(
            original_content_url="https://lh3.googleusercontent.com/pw/ACtC-3dv0dTn-45EryPyNIWrarZAj0aD35QyV0CPNu1nTkQP1tdY5q8EvpGFuJFegz9Pkr0Le8pe6p2kNcXvHwLPAlOVJ1YvnuTlAeZoSGTwb50NGKfksvFIiYalFEEfBCssWHwDFYIl5xC_3cQn_4Ls0GE=w2258-h772-no?authuser=2",
            preview_image_url="https://lh3.googleusercontent.com/pw/ACtC-3dv0dTn-45EryPyNIWrarZAj0aD35QyV0CPNu1nTkQP1tdY5q8EvpGFuJFegz9Pkr0Le8pe6p2kNcXvHwLPAlOVJ1YvnuTlAeZoSGTwb50NGKfksvFIiYalFEEfBCssWHwDFYIl5xC_3cQn_4Ls0GE=w2258-h772-no?authuser=2",
            quick_reply=QuickReply(items=[QuickReplyButton(action = MessageAction(label='Go back to menu', text='Menu'))])
            )
        )
    return "OK"