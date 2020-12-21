import os
import json

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, FlexSendMessage, TextSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction, TemplateSendMessage, ConfirmTemplate, QuickReply, QuickReplyButton, MessageAction, ImageSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(str(channel_access_token))

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_go_to_menu_button(reply_token):
    confirm_template = TemplateSendMessage(
        alt_text="Go back to Menu",
        template=ConfirmTemplate(
            text="Go back to Menu and explore other phones!",
            actions=[
                MessageTemplateAction(
                    label="Go back to Menu",
                    text="Menu"
                ),
                MessageTemplateAction(
                    label="Do we have to?",
                    text="Menu"
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, confirm_template)
    return "OK"

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
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

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
                    title="Samsung",
                    text="Wanna own a Samsung phone?",
                    thumbnail_image_url="https://www.designyourway.net/blog/wp-content/uploads/2019/10/s1-57.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Samsung"
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
                    title="Huawei",
                    text="Wanna own a Huawei phone?",
                    thumbnail_image_url="https://3axis.co/user-images/e1gkwldo.png",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Huawei"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

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
                    title="Iphone 12 pro",
                    text="Wanna own an Iphone 12 pro?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-12-pro--.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 pro"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Iphone 12 mini",
                    text="Wanna own an Iphone 12 mini?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-12-mini.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 mini"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Iphone 12 pro max",
                    text="Wanna own an Iphone 12 pro max?",
                    thumbnail_image_url="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-12-pro-max-.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Iphone 12 pro max"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

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

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass

{
                        'trigger': 'advance',
                        'source': 'Apple',
                        'dest': 'IP12',
                        'conditions': 'is_going_to_IP12'
                    },

                    {
                        'trigger': 'advance',
                        'source': '*',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Menu',
                        'dest': 'IP12',
                        'conditions': 'is_going_to_IP12'
                    },
                
"""
