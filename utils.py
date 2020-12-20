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
                            text="Alright! Let's check the price!"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Specs",
                    text="Wanna see what is the internal and external hardware of the device?",
                    thumbnail_image_url="https://www.gsma.com/esim/wp-content/uploads/2012/10/Specifications.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Alright! Let's check the specs!"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Pros and Cons",
                    text="Wanna know what is bad and good about the device?。",
                    thumbnail_image_url="https://ardas-it.com/uploads/images/blogs/Pros-And-Cons-blog.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="Inquire",
                            text="Alright! Let's check the Pros and Cons!"
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
                            text="Alright! Let's check the Antutu Benchmark Score of Iphone 12!"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
