from transitions.extensions import GraphMachine

from utils import send_text_message, send_IP12_carousel, send_fsm, send_go_to_menu_button,send_Apple_carousel, send_Menu_carousel, send_info, send_IP12_Pro_carousel, send_IP12_Mini_carousel

from Apple import *

class TocMachine(GraphMachine):
    def __init__(self):
        self.machine = GraphMachine(
            model=self,
            **{
                "states" : [
                    'start',
                    'Menu',
                    'Apple',
                    'IP12_Mini',
                    'IP12_Mini_Price',
                    'IP12_Mini_Specs',
                    'IP12_Mini_Pros_Cons',
                    'IP12_Mini_Benchmark_Score',
                    'IP12_Pro',
                    'IP12_Pro_Price',
                    'IP12_Pro_Specs',
                    'IP12_Pro_Pros_Cons',
                    'IP12_Pro_Benchmark_Score',
                    'IP12',
                    'IP12_Price',
                    'IP12_Specs',
                    'IP12_Pros_Cons',
                    'IP12_Benchmark_Score',
                    'fsm'
                ],
                "transitions" : [
                    {
                        'trigger': 'advance',
                        'source': '*',
                        'dest': 'fsm',
                        'conditions': 'is_going_to_fsm'
                    },
                    {
                        'trigger': 'advance',
                        'source': '*',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    #Apple

                    {
                        'trigger': 'advance',
                        'source': 'Menu',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Apple',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    #Iphone 12

                    {
                        'trigger': 'advance',
                        'source': 'Apple',
                        'dest': 'IP12',
                        'conditions': 'is_going_to_IP12'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12',
                        'dest': 'IP12_Price',
                        'conditions': 'is_going_to_IP12_Price'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Price',
                        'dest': 'IP12',
                        'conditions': 'go_back_to_IP12'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12',
                        'dest': 'IP12_Specs',
                        'conditions': 'is_going_to_IP12_Specs'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Specs',
                        'dest': 'IP12',
                        'conditions': 'go_back_to_IP12'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12',
                        'dest': 'IP12_Pros_Cons',
                        'conditions': 'is_going_to_IP12_Pros_Cons'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pros_Cons',
                        'dest': 'IP12',
                        'conditions': 'go_back_to_IP12'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12',
                        'dest': 'IP12_Benchmark_Score',
                        'conditions': 'is_going_to_IP12_Benchmark_Score'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Benchmark_Score',
                        'dest': 'IP12',
                        'conditions': 'go_back_to_IP12'
                    },

                    #Iphone 12 Pro

                    {
                        'trigger': 'advance',
                        'source': 'Apple',
                        'dest': 'IP12_Pro',
                        'conditions': 'is_going_to_IP12_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro',
                        'dest': 'IP12_Pro_Price',
                        'conditions': 'is_going_to_IP12_Pro_Price'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Price',
                        'dest': 'IP12_Pro',
                        'conditions': 'go_back_to_IP12_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro',
                        'dest': 'IP12_Pro_Specs',
                        'conditions': 'is_going_to_IP12_Pro_Specs'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Specs',
                        'dest': 'IP12_Pro',
                        'conditions': 'go_back_to_IP12_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro',
                        'dest': 'IP12_Pro_Pros_Cons',
                        'conditions': 'is_going_to_IP12_Pro_Pros_Cons'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Pros_Cons',
                        'dest': 'IP12_Pro',
                        'conditions': 'go_back_to_IP12_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro',
                        'dest': 'IP12_Pro_Benchmark_Score',
                        'conditions': 'is_going_to_IP12_Pro_Benchmark_Score'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Benchmark_Score',
                        'dest': 'IP12_Pro',
                        'conditions': 'go_back_to_IP12_Pro'
                    },

                    #Iphone 12 Mini

                    {
                        'trigger': 'advance',
                        'source': 'Apple',
                        'dest': 'IP12_Mini',
                        'conditions': 'is_going_to_IP12_Mini'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini',
                        'dest': 'IP12_Mini_Price',
                        'conditions': 'is_going_to_IP12_Mini_Price'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini_Price',
                        'dest': 'IP12_Mini',
                        'conditions': 'go_back_to_IP12_Mini'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini',
                        'dest': 'IP12_Mini_Specs',
                        'conditions': 'is_going_to_IP12_Mini_Specs'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini_Specs',
                        'dest': 'IP12_Mini',
                        'conditions': 'go_back_to_IP12_Mini'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini',
                        'dest': 'IP12_Mini_Pros_Cons',
                        'conditions': 'is_going_to_IP12_Mini_Pros_Cons'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini_Pros_Cons',
                        'dest': 'IP12_Mini',
                        'conditions': 'go_back_to_IP12_Mini'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini',
                        'dest': 'IP12_Mini_Benchmark_Score',
                        'conditions': 'is_going_to_IP12_Mini_Benchmark_Score'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini_Benchmark_Score',
                        'dest': 'IP12_Mini',
                        'conditions': 'go_back_to_IP12_Mini'
                    },

                    {
                        'trigger': 'advance',
                        'source': 'fsm',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                   
                ],
                "initial" : 'start',
                "auto_transitions" : False,
                "show_conditions": True,
            },
        )

    def is_going_to_Menu(self, event):
        text = event.message.text
        return "Menu" in text
    
    def is_going_to_fsm(self, event):
        text = event.message.text
        return "fsm" in str(text).lower()

    #on enter
    def on_enter_Menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        #text = ("Iphone 12 Menu")
        #send_text_message(reply_token, text)
        #send_go_to_menu_button(reply_token)
        send_Menu_carousel(reply_token)

    def on_enter_fsm(self, event):
        print("I'm entering fsm")
        reply_token = event.reply_token
        send_fsm(reply_token)