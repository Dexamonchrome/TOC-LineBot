from transitions.extensions import GraphMachine

from utils import * #send_text_message, send_IP12_carousel, send_fsm, send_go_to_menu_button,send_Apple_carousel, send_Menu_carousel, send_info, send_IP12_Pro_carousel, send_IP12_Mini_carousel, send_IP12_Pro_Max_carousel

import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

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
                    'IP12_Pro_Max',
                    'IP12_Pro_Max_Price',
                    'IP12_Pro_Max_Specs',
                    'IP12_Pro_Max_Pros_Cons',
                    'IP12_Pro_Max_Benchmark_Score',
                    'IP12',
                    'IP12_Price',
                    'IP12_Specs',
                    'IP12_Pros_Cons',
                    'IP12_Benchmark_Score',
                    'Google',
                    'Pixel_5',
                    'Pixel_5_Price',
                    'Pixel_5_Specs',
                    'Pixel_5_Pros_Cons',
                    'Pixel_5_Benchmark_Score',
                    'Pixel_5_Video',
                    'Pixel_4a',
                    'Pixel_4a_Price',
                    'Pixel_4a_Specs',
                    'Pixel_4a_Pros_Cons',
                    'Pixel_4a_Benchmark_Score',
                    'Pixel_4a_Video',
                    'Pixel_4a_5G',
                    'Pixel_4a_5G_Price',
                    'Pixel_4a_5G_Specs',
                    'Pixel_4a_5G_Pros_Cons',
                    'Pixel_4a_5G_Benchmark_Score',
                    'Pixel_4a_5G_Video',
                    'Sony',
                    'Xperia_5_II',
                    'Xperia_5_II_Price',
                    'Xperia_5_II_Specs',
                    'Xperia_5_II_Pros_Cons',
                    'Xperia_5_II_Benchmark_Score',
                    'Xperia_5_II_Video',
                    'Xperia_1_II',
                    'Xperia_1_II_Price',
                    'Xperia_1_II_Specs',
                    'Xperia_1_II_Pros_Cons',
                    'Xperia_1_II_Benchmark_Score',
                    'Xperia_1_II_Video',
                    'Xperia_10_II',
                    'Xperia_10_II_Price',
                    'Xperia_10_II_Specs',
                    'Xperia_10_II_Pros_Cons',
                    'Xperia_10_II_Benchmark_Score',
                    'Xperia_10_II_Video',
                    'Asus',
                    'ROG',
                    'ROG_Phone_3_Strix',
                    'ROG_Phone_3_Strix_Price',
                    'ROG_Phone_3_Strix_Specs',
                    'ROG_Phone_3_Strix_Pros_Cons',
                    'ROG_Phone_3_Strix_Benchmark_Score',
                    'ROG_Phone_3_Strix_Video',
                    'Zenfone',
                    'Zenfone_7',
                    'Zenfone_7_Price',
                    'Zenfone_7_Specs',
                    'Zenfone_7_Pros_Cons',
                    'Zenfone_7_Benchmark_Score',
                    'Zenfone_7_Video',
                    'Zenfone_7_Pro',
                    'Zenfone_7_Pro_Price',
                    'Zenfone_7_Pro_Specs',
                    'Zenfone_7_Pro_Pros_Cons',
                    'Zenfone_7_Pro_Benchmark_Score',
                    'Zenfone_7_Pro_Video',
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

                    #Google

                    {
                        'trigger': 'advance',
                        'source': 'Menu',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Apple',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    #Sony
                    
                    {
                        'trigger': 'advance',
                        'source': 'Menu',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Sony',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    #Asus
                    
                    {
                        'trigger': 'advance',
                        'source': 'Menu',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Asus',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    {
                        'trigger': 'advance',
                        'source': 'Menu',
                        'dest': 'fsm_image',
                        'conditions': 'is_going_to_fsm_image'   
                    },

                    {
                        'trigger': 'advance',
                        'source': 'fsm_image',
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
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
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
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Price',
                        'dest': 'IP12',
                        'conditions': 'is_going_to_IP12'
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
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Specs',
                        'dest': 'IP12',
                        'conditions': 'is_going_to_IP12'
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
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pros_Cons',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pros_Cons',
                        'dest': 'IP12',
                        'conditions': 'is_going_to_IP12'
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
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Benchmark_Score',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Benchmark_Score',
                        'dest': 'IP12',
                        'conditions': 'is_going_to_IP12'
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
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
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
                        'conditions': 'is_going_to_IP12_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Price',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
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
                        'conditions': 'is_going_to_IP12_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Specs',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
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
                        'conditions': 'is_going_to_IP12_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Pros_Cons',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Pros_Cons',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
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
                        'conditions': 'is_going_to_IP12_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Benchmark_Score',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Benchmark_Score',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },

                    #Iphone 12 Pro Max

                     {
                        'trigger': 'advance',
                        'source': 'Apple',
                        'dest': 'IP12_Pro_Max',
                        'conditions': 'is_going_to_IP12_Pro_Max'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max',
                        'dest': 'IP12_Pro_Max_Price',
                        'conditions': 'is_going_to_IP12_Pro_Max_Price'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max_Price',
                        'dest': 'IP12_Pro_Max',
                        'conditions': 'is_going_to_IP12_Pro_Max'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max_Price',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max',
                        'dest': 'IP12_Pro_Max_Specs',
                        'conditions': 'is_going_to_IP12_Pro_Max_Specs'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max_Specs',
                        'dest': 'IP12_Pro_Max',
                        'conditions': 'is_going_to_IP12_Pro_Max'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max_Specs',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max',
                        'dest': 'IP12_Pro_Max_Pros_Cons',
                        'conditions': 'is_going_to_IP12_Pro_Max_Pros_Cons'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max_Pros_Cons',
                        'dest': 'IP12_Pro_Max',
                        'conditions': 'is_going_to_IP12_Pro_Max'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max_Pros_Cons',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max_Pros_Cons',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max',
                        'dest': 'IP12_Pro_Max_Benchmark_Score',
                        'conditions': 'is_going_to_IP12_Pro_Max_Benchmark_Score'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max_Benchmark_Score',
                        'dest': 'IP12_Pro_Max',
                        'conditions': 'is_going_to_IP12_Pro_Max'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max_Benchmark_Score',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Pro_Max_Benchmark_Score',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
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
                        'conditions': 'is_going_to_IP12_Mini'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini_Price',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
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
                        'conditions': 'is_going_to_IP12_Mini'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini_Specs',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
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
                        'conditions': 'is_going_to_IP12_Mini'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini_Pros_Cons',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini_Pros_Cons',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
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
                        'conditions': 'is_going_to_IP12_Mini'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini_Benchmark_Score',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'IP12_Mini_Benchmark_Score',
                        'dest': 'Apple',
                        'conditions': 'is_going_to_Apple'
                    },

                    {
                        'trigger': 'advance',
                        'source': 'fsm',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    #Pixel 5

                    {
                        'trigger': 'advance',
                        'source': 'Google',
                        'dest': 'Pixel_5',
                        'conditions': 'is_going_to_Pixel_5'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5',
                        'dest': 'Pixel_5_Price',
                        'conditions': 'is_going_to_Pixel_5_Price'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Price',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Price',
                        'dest': 'Pixel_5',
                        'conditions': 'is_going_to_Pixel_5'
                    },

                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5',
                        'dest': 'Pixel_5_Specs',
                        'conditions': 'is_going_to_Pixel_5_Specs'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Specs',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Specs',
                        'dest': 'Pixel_5',
                        'conditions': 'is_going_to_Pixel_5'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5',
                        'dest': 'Pixel_5_Pros_Cons',
                        'conditions': 'is_going_to_Pixel_5_Pros_Cons'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Pros_Cons',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Pros_Cons',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Pros_Cons',
                        'dest': 'Pixel_5',
                        'conditions': 'is_going_to_Pixel_5'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5',
                        'dest': 'Pixel_5_Benchmark_Score',
                        'conditions': 'is_going_to_Pixel_5_Benchmark_Score'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Benchmark_Score',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Benchmark_Score',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Benchmark_Score',
                        'dest': 'Pixel_5',
                        'conditions': 'is_going_to_Pixel_5'
                    },

                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5',
                        'dest': 'Pixel_5_Video',
                        'conditions': 'is_going_to_Pixel_5_Video'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Video',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_5_Video',
                        'dest': 'Pixel_5',
                        'conditions': 'is_going_to_Pixel_5'
                    },

                    #Pixel 4a

                    {
                        'trigger': 'advance',
                        'source': 'Google',
                        'dest': 'Pixel_4a',
                        'conditions': 'is_going_to_Pixel_4a'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a',
                        'dest': 'Pixel_4a_Price',
                        'conditions': 'is_going_to_Pixel_4a_Price'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Price',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Price',
                        'dest': 'Pixel_4a',
                        'conditions': 'is_going_to_Pixel_4a'
                    },

                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a',
                        'dest': 'Pixel_4a_Specs',
                        'conditions': 'is_going_to_Pixel_4a_Specs'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Specs',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Specs',
                        'dest': 'Pixel_4a',
                        'conditions': 'is_going_to_Pixel_4a'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a',
                        'dest': 'Pixel_4a_Pros_Cons',
                        'conditions': 'is_going_to_Pixel_4a_Pros_Cons'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Pros_Cons',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Pros_Cons',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Pros_Cons',
                        'dest': 'Pixel_4a',
                        'conditions': 'is_going_to_Pixel_4a'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a',
                        'dest': 'Pixel_4a_Benchmark_Score',
                        'conditions': 'is_going_to_Pixel_4a_Benchmark_Score'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Benchmark_Score',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Benchmark_Score',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Benchmark_Score',
                        'dest': 'Pixel_4a',
                        'conditions': 'is_going_to_Pixel_4a'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a',
                        'dest': 'Pixel_4a_Video',
                        'conditions': 'is_going_to_Pixel_4a_Video'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Video',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_Video',
                        'dest': 'Pixel_4a',
                        'conditions': 'is_going_to_Pixel_4a'
                    },

                    #Pixel 4a 5G

                    {
                        'trigger': 'advance',
                        'source': 'Google',
                        'dest': 'Pixel_4a_5G',
                        'conditions': 'is_going_to_Pixel_4a_5G'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G',
                        'dest': 'Pixel_4a_5G_Price',
                        'conditions': 'is_going_to_Pixel_4a_5G_Price'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Price',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Price',
                        'dest': 'Pixel_4a_5G',
                        'conditions': 'is_going_to_Pixel_4a_5G'
                    },

                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G',
                        'dest': 'Pixel_4a_5G_Specs',
                        'conditions': 'is_going_to_Pixel_4a_5G_Specs'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Specs',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Specs',
                        'dest': 'Pixel_4a_5G',
                        'conditions': 'is_going_to_Pixel_4a_5G'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G',
                        'dest': 'Pixel_4a_5G_Pros_Cons',
                        'conditions': 'is_going_to_Pixel_4a_5G_Pros_Cons'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Pros_Cons',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Pros_Cons',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Pros_Cons',
                        'dest': 'Pixel_4a_5G',
                        'conditions': 'is_going_to_Pixel_4a_5G'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G',
                        'dest': 'Pixel_4a_5G_Benchmark_Score',
                        'conditions': 'is_going_to_Pixel_4a_5G_Benchmark_Score'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Benchmark_Score',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Benchmark_Score',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Benchmark_Score',
                        'dest': 'Pixel_4a_5G',
                        'conditions': 'is_going_to_Pixel_4a_5G'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G',
                        'dest': 'Pixel_4a_5G_Video',
                        'conditions': 'is_going_to_Pixel_4a_5G_Video'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Video',
                        'dest': 'Google',
                        'conditions': 'is_going_to_Google'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Pixel_4a_5G_Video',
                        'dest': 'Pixel_4a_5G',
                        'conditions': 'is_going_to_Pixel_4a_5G'
                    },
                   
                    #Sony Xperia 5 II
                    {
                        'trigger': 'advance',
                        'source': 'Sony',
                        'dest': 'Xperia_5_II',
                        'conditions': 'is_going_to_Xperia_5_II'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II',
                        'dest': 'Xperia_5_II_Price',
                        'conditions': 'is_going_to_Xperia_5_II_Price'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Price',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Price',
                        'dest': 'Xperia_5_II',
                        'conditions': 'is_going_to_Xperia_5_II'
                    },

                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II',
                        'dest': 'Xperia_5_II_Specs',
                        'conditions': 'is_going_to_Xperia_5_II_Specs'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Specs',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Specs',
                        'dest': 'Xperia_5_II',
                        'conditions': 'is_going_to_Xperia_5_II'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II',
                        'dest': 'Xperia_5_II_Pros_Cons',
                        'conditions': 'is_going_to_Xperia_5_II_Pros_Cons'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Pros_Cons',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Pros_Cons',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Pros_Cons',
                        'dest': 'Xperia_5_II',
                        'conditions': 'is_going_to_Xperia_5_II'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II',
                        'dest': 'Xperia_5_II_Benchmark_Score',
                        'conditions': 'is_going_to_Xperia_5_II_Benchmark_Score'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Benchmark_Score',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Benchmark_Score',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Benchmark_Score',
                        'dest': 'Xperia_5_II',
                        'conditions': 'is_going_to_Xperia_5_II'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II',
                        'dest': 'Xperia_5_II_Video',
                        'conditions': 'is_going_to_Xperia_5_II_Video'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Video',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_5_II_Video',
                        'dest': 'Xperia_5_II',
                        'conditions': 'is_going_to_Xperia_5_II'
                    },

                    #Sony Xperia 1 II
                    {
                        'trigger': 'advance',
                        'source': 'Sony',
                        'dest': 'Xperia_1_II',
                        'conditions': 'is_going_to_Xperia_1_II'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II',
                        'dest': 'Xperia_1_II_Price',
                        'conditions': 'is_going_to_Xperia_1_II_Price'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Price',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Price',
                        'dest': 'Xperia_1_II',
                        'conditions': 'is_going_to_Xperia_1_II'
                    },

                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II',
                        'dest': 'Xperia_1_II_Specs',
                        'conditions': 'is_going_to_Xperia_1_II_Specs'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Specs',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Specs',
                        'dest': 'Xperia_1_II',
                        'conditions': 'is_going_to_Xperia_1_II'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II',
                        'dest': 'Xperia_1_II_Pros_Cons',
                        'conditions': 'is_going_to_Xperia_1_II_Pros_Cons'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Pros_Cons',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Pros_Cons',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Pros_Cons',
                        'dest': 'Xperia_1_II',
                        'conditions': 'is_going_to_Xperia_1_II'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II',
                        'dest': 'Xperia_1_II_Benchmark_Score',
                        'conditions': 'is_going_to_Xperia_1_II_Benchmark_Score'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Benchmark_Score',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Benchmark_Score',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Benchmark_Score',
                        'dest': 'Xperia_1_II',
                        'conditions': 'is_going_to_Xperia_1_II'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II',
                        'dest': 'Xperia_1_II_Video',
                        'conditions': 'is_going_to_Xperia_1_II_Video'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Video',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_1_II_Video',
                        'dest': 'Xperia_1_II',
                        'conditions': 'is_going_to_Xperia_1_II'
                    },

                    #Sony Xperia 10 II
                    {
                        'trigger': 'advance',
                        'source': 'Sony',
                        'dest': 'Xperia_10_II',
                        'conditions': 'is_going_to_Xperia_10_II'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II',
                        'dest': 'Xperia_10_II_Price',
                        'conditions': 'is_going_to_Xperia_10_II_Price'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Price',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Price',
                        'dest': 'Xperia_10_II',
                        'conditions': 'is_going_to_Xperia_10_II'
                    },

                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II',
                        'dest': 'Xperia_10_II_Specs',
                        'conditions': 'is_going_to_Xperia_10_II_Specs'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Specs',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Specs',
                        'dest': 'Xperia_10_II',
                        'conditions': 'is_going_to_Xperia_10_II'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II',
                        'dest': 'Xperia_10_II_Pros_Cons',
                        'conditions': 'is_going_to_Xperia_10_II_Pros_Cons'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Pros_Cons',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Pros_Cons',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Pros_Cons',
                        'dest': 'Xperia_10_II',
                        'conditions': 'is_going_to_Xperia_10_II'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II',
                        'dest': 'Xperia_10_II_Benchmark_Score',
                        'conditions': 'is_going_to_Xperia_10_II_Benchmark_Score'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Benchmark_Score',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Benchmark_Score',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Benchmark_Score',
                        'dest': 'Xperia_10_II',
                        'conditions': 'is_going_to_Xperia_10_II'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II',
                        'dest': 'Xperia_10_II_Video',
                        'conditions': 'is_going_to_Xperia_10_II_Video'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Video',
                        'dest': 'Sony',
                        'conditions': 'is_going_to_Sony'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Xperia_10_II_Video',
                        'dest': 'Xperia_10_II',
                        'conditions': 'is_going_to_Xperia_10_II'
                    },

                    #Zenfone
                    {
                        'trigger': 'advance',
                        'source': 'Asus',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },

                    #ROG
                    {
                        'trigger': 'advance',
                        'source': 'Asus',
                        'dest': 'ROG',
                        'conditions': 'is_going_to_ROG'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    
                    #Zenfone 7

                    {
                        'trigger': 'advance',
                        'source': 'Zenfone',
                        'dest': 'Zenfone_7',
                        'conditions': 'is_going_to_Zenfone_7'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7',
                        'dest': 'Zenfone_7_Price',
                        'conditions': 'is_going_to_Zenfone_7_Price'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Price',
                        'dest': 'Zenfone_7',
                        'conditions': 'is_going_to_Zenfone_7'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Price',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Price',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7',
                        'dest': 'Zenfone_7_Specs',
                        'conditions': 'is_going_to_Zenfone_7_Specs'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Specs',
                        'dest': 'Zenfone_7',
                        'conditions': 'is_going_to_Zenfone_7'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Specs',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Specs',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7',
                        'dest': 'Zenfone_7_Pros_Cons',
                        'conditions': 'is_going_to_Zenfone_7_Pros_Cons'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pros_Cons',
                        'dest': 'Zenfone_7',
                        'conditions': 'is_going_to_Zenfone_7'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pros_Cons',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pros_Cons',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pros_Cons',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7',
                        'dest': 'Zenfone_7_Benchmark_Score',
                        'conditions': 'is_going_to_Zenfone_7_Benchmark_Score'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Benchmark_Score',
                        'dest': 'Zenfone_7',
                        'conditions': 'is_going_to_Zenfone_7'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Benchmark_Score',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                     {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Benchmark_Score',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Benchmark_Score',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7',
                        'dest': 'Zenfone_7_Video',
                        'conditions': 'is_going_to_Zenfone_7_Video'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Video',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Video',
                        'dest': 'Zenfone_7',
                        'conditions': 'is_going_to_Zenfone_7'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Video',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    
                    
                    
                    #Zenfone 7 Pro

                    {
                        'trigger': 'advance',
                        'source': 'Zenfone',
                        'dest': 'Zenfone_7_Pro',
                        'conditions': 'is_going_to_Zenfone_7_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro',
                        'dest': 'Zenfone_7_Pro_Price',
                        'conditions': 'is_going_to_Zenfone_7_Pro_Price'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Price',
                        'dest': 'Zenfone_7_Pro',
                        'conditions': 'is_going_to_Zenfone_7_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Price',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Price',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro',
                        'dest': 'Zenfone_7_Pro_Specs',
                        'conditions': 'is_going_to_Zenfone_7_Pro_Specs'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Specs',
                        'dest': 'Zenfone_7_Pro',
                        'conditions': 'is_going_to_Zenfone_7_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                     {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Specs',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Specs',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },
                   
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro',
                        'dest': 'Zenfone_7_Pro_Pros_Cons',
                        'conditions': 'is_going_to_Zenfone_7_Pro_Pros_Cons'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Pros_Cons',
                        'dest': 'Zenfone_7_Pro',
                        'conditions': 'is_going_to_Zenfone_7_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Pros_Cons',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Pros_Cons',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Pros_Cons',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro',
                        'dest': 'Zenfone_7_Pro_Benchmark_Score',
                        'conditions': 'is_going_to_Zenfone_7_Pro_Benchmark_Score'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Benchmark_Score',
                        'dest': 'Zenfone_7_Pro',
                        'conditions': 'is_going_to_Zenfone_7_Pro'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Benchmark_Score',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Benchmark_Score',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Benchmark_Score',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },

                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro',
                        'dest': 'Zenfone_7_Pro_Video',
                        'conditions': 'is_going_to_Zenfone_7_Pro_Video'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Video',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Video',
                        'dest': 'Zenfone',
                        'conditions': 'is_going_to_Zenfone'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Zenfone_7_Pro_Video',
                        'dest': 'Zenfone_7_Pro',
                        'conditions': 'is_going_to_Zenfone_7_Pro'
                    },

                    
                    #ROG Phone 3 Strix

                    {
                        'trigger': 'advance',
                        'source': 'ROG',
                        'dest': 'ROG_Phone_3_Strix',
                        'conditions': 'is_going_to_ROG_Phone_3_Strix'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix',
                        'dest': 'ROG',
                        'conditions': 'is_going_to_ROG'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix',
                        'dest': 'ROG_Phone_3_Strix_Price',
                        'conditions': 'is_going_to_ROG_Phone_3_Strix_Price'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Price',
                        'dest': 'ROG_Phone_3_Strix',
                        'conditions': 'is_going_to_ROG_Phone_3_Strix'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Price',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Price',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Price',
                        'dest': 'ROG',
                        'conditions': 'is_going_to_ROG'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix',
                        'dest': 'ROG_Phone_3_Strix_Specs',
                        'conditions': 'is_going_to_ROG_Phone_3_Strix_Specs'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Specs',
                        'dest': 'ROG_Phone_3_Strix',
                        'conditions': 'is_going_to_ROG_Phone_3_Strix'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Specs',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Specs',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Specs',
                        'dest': 'ROG',
                        'conditions': 'is_going_to_ROG'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix',
                        'dest': 'ROG_Phone_3_Strix_Pros_Cons',
                        'conditions': 'is_going_to_ROG_Phone_3_Strix_Pros_Cons'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Pros_Cons',
                        'dest': 'ROG_Phone_3_Strix',
                        'conditions': 'is_going_to_ROG_Phone_3_Strix'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Pros_Cons',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Pros_Cons',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Pros_Cons',
                        'dest': 'ROG',
                        'conditions': 'is_going_to_ROG'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix',
                        'dest': 'ROG_Phone_3_Strix_Benchmark_Score',
                        'conditions': 'is_going_to_ROG_Phone_3_Strix_Benchmark_Score'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Benchmark_Score',
                        'dest': 'ROG_Phone_3_Strix',
                        'conditions': 'is_going_to_ROG_Phone_3_Strix'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Benchmark_Score',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Benchmark_Score',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },   
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Benchmark_Score',
                        'dest': 'ROG',
                        'conditions': 'is_going_to_ROG'
                    },
                                         

                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix',
                        'dest': 'ROG_Phone_3_Strix_Video',
                        'conditions': 'is_going_to_ROG_Phone_3_Strix_Video'
                    },
                    
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Video',
                        'dest': 'Asus',
                        'conditions': 'is_going_to_Asus'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Video',
                        'dest': 'ROG',
                        'conditions': 'is_going_to_ROG'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'ROG_Phone_3_Strix_Video',
                        'dest': 'ROG_Phone_3_Strix',
                        'conditions': 'is_going_to_ROG_Phone_3_Strix'
                    },

                ],
                "initial" : 'start',
                "auto_transitions" : False,
                "show_conditions": True,
            },
        )

    def is_going_to_Menu(self, event):
        text = event.message.text
        return "menu" in str(text).lower() 
    
    def go_back_Menu(self,event):
        text = event.message.text
        return "menu" in str(text).lower() 

    #Apple
    def is_going_to_Apple(self, event):
        text = event.message.text
        return "apple" in str(text).lower()

    def go_back_Apple(self, event):
        text = event.message.text
        return "apple" in str(text).lower() 
    
    #Google
    def is_going_to_Google(self, event):
        text = event.message.text
        return "google" in str(text).lower() 

    def go_back_Google(self, event):
        text = event.message.text
        return "google" in str(text).lower() 

    #Sony
    def is_going_to_Sony(self, event):
        text = event.message.text
        return "sony" in str(text).lower() 

    def go_back_Sony(self, event):
        text = event.message.text
        return "sony" in str(text).lower() 
    
    #Asus
    def is_going_to_Asus(self, event):
        text = event.message.text
        return "asus" in str(text).lower() 

    def go_back_Asus(self, event):
        text = event.message.text
        return "asus" in str(text).lower() 

    #Zenfone
    def is_going_to_Zenfone(self, event):
        text = event.message.text
        return "zenfone" in str(text).lower() and "7" not in str(text).lower() or "pro" not in str(text).lower()

    # Iphone 12
    def is_going_to_IP12(self, event):
        text = event.message.text
        return "iphone 12" in str(text).lower() and "mini" not in str(text).lower() and "pro" not in str(text).lower()
    
    def is_going_to_IP12_Price(self, event):
        text = event.message.text
        return "iphone 12" in str(text).lower() and "mini" not in str(text).lower() and "pro" not in str(text).lower() and "price" in str(text).lower() 

    def is_going_to_IP12_Specs(self, event):
        text = event.message.text
        return "iphone 12" in str(text).lower() and "mini" not in str(text).lower() and "pro" not in str(text).lower() and "specs" in str(text).lower()  

    def is_going_to_IP12_Pros_Cons(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Pros and Cons" in text
        return "iphone 12 pros and cons" == text.lower()  

    def is_going_to_IP12_Benchmark_Score(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "iphone 12 benchmark score" == text.lower()
    def is_going_to_fsm(self, event):
        text = event.message.text
        return "fsm" in str(text).lower()

    def go_back_IP12(self, event):
        text = event.message.text
        return "iphone 12" in str(text).lower() and "mini" not in str(text).lower() and "pro" not in str(text).lower()
    
    # Iphone 12 Pro
    def is_going_to_IP12_Pro(self, event):
        text = event.message.text
        return "iphone 12" in str(text).lower() and "mini" not in str(text).lower() and "max" not in str(text).lower() and "pro" in str(text).lower()
    
    def is_going_to_IP12_Pro_Price(self, event):
        text = event.message.text
        return "iphone 12 pro price" in str(text).lower()

    def is_going_to_IP12_Pro_Specs(self, event):
        text = event.message.text
        return "iphone 12 pro specs" in str(text).lower()

    def is_going_to_IP12_Pro_Pros_Cons(self, event):
        text = event.message.text
        return "iphone 12 pro pros and cons" in str(text).lower()

    def is_going_to_IP12_Pro_Benchmark_Score(self, event):
        text = event.message.text
        return "iphone 12 pro benchmark score" in str(text).lower() 

    def go_back_IP12_Pro(self, event):
        text = event.message.text
        return "iphone 12 pro" in str(text).lower() and "mini" not in str(text).lower() and "max" not in text and "pro" in str(text).lower()

    # Iphone 12 Pro Max
    def is_going_to_IP12_Pro_Max(self, event):
        text = event.message.text
        return "iphone 12" in str(text).lower() and "mini" not in str(text).lower() and "max" in str(text).lower()
    
    def is_going_to_IP12_Pro_Max_Price(self, event):
        text = event.message.text
        return "iphone 12 pro max price" in str(text).lower()

    def is_going_to_IP12_Pro_Max_Specs(self, event):
        text = event.message.text
        return "iphone 12 pro max specs" in str(text).lower()

    def is_going_to_IP12_Pro_Max_Pros_Cons(self, event):
        text = event.message.text
        return "iphone 12 pro max pros and cons" in str(text).lower() 

    def is_going_to_IP12_Pro_Max_Benchmark_Score(self, event):
        text = event.message.text
        return "iphone 12 pro max benchmark score" in str(text).lower() 

    def go_back_IP12_Pro_Max(self, event):
        text = event.message.text
        return "iphone 12 pro" in str(text).lower() and "mini" not in str(text).lower() and "max" in str(text).lower()
    

    # Iphone 12 Mini
    def is_going_to_IP12_Mini(self, event):
        text = event.message.text
        return "iphone 12" in str(text).lower() and "mini" in str(text).lower() and "pro" not in str(text).lower()
    def is_going_to_IP12_Mini_Price(self, event):
        text = event.message.text
        return "iphone 12 mini price" in str(text).lower()

    def is_going_to_IP12_Mini_Specs(self, event):
        text = event.message.text
        return "iphone 12 mini specs" in str(text).lower() 

    def is_going_to_IP12_Mini_Pros_Cons(self, event):
        text = event.message.text
        return "iphone 12 mini pros and cons" in str(text).lower() 

    def is_going_to_IP12_Mini_Benchmark_Score(self, event):
        text = event.message.text
        return "iphone 12 mini benchmark score" in str(text).lower() 

    def go_back_IP12_Mini(self, event):
        text = event.message.text
        return "iphone 12" in str(text).lower() and "mini" in str(text).lower() and "pro" not in str(text).lower()

    #Pixel 5
    def is_going_to_Pixel_5(self, event):
        text = event.message.text
        return "pixel 5" in str(text).lower()
    
    def is_going_to_Pixel_5_Price(self, event):
        text = event.message.text
        return "pixel 5 price" in str(text).lower() 

    def is_going_to_Pixel_5_Specs(self, event):
        text = event.message.text
        return "pixel 5 specs" in str(text).lower()  

    def is_going_to_Pixel_5_Pros_Cons(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Pros and Cons" in text
        return "pixel 5 pros and cons" == text.lower()   

    def is_going_to_Pixel_5_Benchmark_Score(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "pixel 5 benchmark score" == text.lower()

    def is_going_to_Pixel_5_Video(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "pixel 5 video" == text.lower()
    
    def go_back_Pixel_5(self, event):
        text = event.message.text
        return "pixel 5" in str(text).lower()
    
    #Pixel 4a
    def is_going_to_Pixel_4a(self, event):
        text = event.message.text
        return "pixel 4a" in str(text).lower() and "5g" not in str(text).lower()
    
    def is_going_to_Pixel_4a_Price(self, event):
        text = event.message.text
        return "pixel 4a price" in str(text).lower() 

    def is_going_to_Pixel_4a_Specs(self, event):
        text = event.message.text
        return "pixel 4a specs" in str(text).lower()  

    def is_going_to_Pixel_4a_Pros_Cons(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Pros and Cons" in text
        return "pixel 4a pros and cons" == text.lower()   

    def is_going_to_Pixel_4a_Benchmark_Score(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "pixel 4a" in str(text).lower() and "benchmark score" in str(text).lower()

    def is_going_to_Pixel_4a_Video(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "pixel 4a video" == text.lower()
    
    def go_back_Pixel_4a(self, event):
        text = event.message.text
        return "pixel 4a" in str(text).lower()

    #Pixel 4a 5G
    def is_going_to_Pixel_4a_5G(self, event):
        text = event.message.text
        return "pixel 4a" in str(text).lower() and "5g" in str(text).lower()
    
    def is_going_to_Pixel_4a_5G_Price(self, event):
        text = event.message.text
        return "pixel 4a 5g price" in str(text).lower() 

    def is_going_to_Pixel_4a_5G_Specs(self, event):
        text = event.message.text
        return "pixel 4a 5g specs" in str(text).lower()  

    def is_going_to_Pixel_4a_5G_Pros_Cons(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Pros and Cons" in text
        return "pixel 4a 5g pros and cons" == text.lower()   

    def is_going_to_Pixel_4a_5G_Benchmark_Score(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "pixel 4a 5g" in str(text).lower() and "benchmark score" in str(text).lower()

    def is_going_to_Pixel_4a_5G_Video(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "pixel 4a 5g video" == text.lower()
    
    def go_back_Pixel_4a_5G(self, event):
        text = event.message.text
        return "pixel 4a 5g" in str(text).lower()

    #Xperia 5 II
    def is_going_to_Xperia_5_II(self, event):
        text = event.message.text
        return "xperia 5 ii" == text.lower()
    
    def is_going_to_Xperia_5_II_Price(self, event):
        text = event.message.text
        return "xperia 5 ii price" == text.lower() 

    def is_going_to_Xperia_5_II_Specs(self, event):
        text = event.message.text
        return "xperia 5 ii specs" == text.lower()   

    def is_going_to_Xperia_5_II_Pros_Cons(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Pros and Cons" in text
        return "xperia 5 ii pros and cons" == text.lower()   

    def is_going_to_Xperia_5_II_Benchmark_Score(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "xperia 5 ii benchmark score" == text.lower() 

    def is_going_to_Xperia_5_II_Video(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "xperia 5 ii video" == text.lower() 
    
    def go_back_Xperia_5_II(self, event):
        text = event.message.text
        return "xperia 5 ii" == text.lower() 


    #Xperia 1 II
    def is_going_to_Xperia_1_II(self, event):
        text = event.message.text
        return "xperia 1 ii" == text.lower() 
    
    def is_going_to_Xperia_1_II_Price(self, event):
        text = event.message.text
        return "xperia 1 ii price" == text.lower() 

    def is_going_to_Xperia_1_II_Specs(self, event):
        text = event.message.text
        return "xperia 1 ii specs" == text.lower() 

    def is_going_to_Xperia_1_II_Pros_Cons(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Pros and Cons" in text
        return "xperia 1 ii pros and cons" == text.lower()    

    def is_going_to_Xperia_1_II_Benchmark_Score(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "xperia 1 ii benchmark score" == text.lower() 

    def is_going_to_Xperia_1_II_Video(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "xperia 1 ii video" == text.lower() 
    
    def go_back_Xperia_1_II(self, event):
        text = event.message.text
        return "xperia 1 ii" == text.lower() 


    #Xperia 10 II
    def is_going_to_Xperia_10_II(self, event):
        text = event.message.text
        return "xperia 10 ii" == text.lower() 
    
    def is_going_to_Xperia_10_II_Price(self, event):
        text = event.message.text
        return "xperia 10 ii price" == text.lower() 

    def is_going_to_Xperia_10_II_Specs(self, event):
        text = event.message.text
        return "xperia 10 ii specs" == text.lower()  

    def is_going_to_Xperia_10_II_Pros_Cons(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Pros and Cons" in text
        return "xperia 10 ii pros and cons" == text.lower() 

    def is_going_to_Xperia_10_II_Benchmark_Score(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "xperia 10 ii benchmark score" == text.lower() 

    def is_going_to_Xperia_10_II_Video(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "xperia 10 ii video" == text.lower() 
    
    def go_back_Xperia_10_II(self, event):
        text = event.message.text
        return "xperia 10 ii" == text.lower() 

    #Zenfone
    def is_going_to_Zenfone(self, event): 
        text = event.message.text
        return "zenfone" in str(text).lower() and "7" not in str(text).lower()

    #Zenfone 7
    def is_going_to_Zenfone_7(self, event):
        text = event.message.text
        return "zenfone 7" in str(text).lower() and "pro" not in str(text).lower()
    
    def is_going_to_Zenfone_7_Price(self, event):
        text = event.message.text
        return "zenfone" in str(text).lower() and "pro" not in str(text).lower() and "7" in str(text).lower() and "price" in str(text).lower() 

    def is_going_to_Zenfone_7_Specs(self, event):
        text = event.message.text
        return "zenfone 7" in str(text).lower() and "specs" in str(text).lower()  

    def is_going_to_Zenfone_7_Pros_Cons(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Pros and Cons" in text
        return "zenfone 7 pros and cons" == text.lower() 

    def is_going_to_Zenfone_7_Benchmark_Score(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "zenfone 7 benchmark score" == text.lower() 

    def is_going_to_Zenfone_7_Video(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "zenfone 7 video" == text.lower() 

    #Zenfone 7 Pro
    def is_going_to_Zenfone_7_Pro(self, event):
        text = event.message.text
        return "zenfone 7 pro" == text.lower() 
    
    def is_going_to_Zenfone_7_Pro_Price(self, event):
        text = event.message.text
        return "zenfone 7" in str(text).lower() and "pro price" in str(text).lower()

    def is_going_to_Zenfone_7_Pro_Specs(self, event):
        text = event.message.text
        return "zenfone 7 pro specs" == text.lower() 

    def is_going_to_Zenfone_7_Pro_Pros_Cons(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Pros and Cons" in text
        return "zenfone 7 pro pros and cons" == text.lower() 

    def is_going_to_Zenfone_7_Pro_Benchmark_Score(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "zenfone 7 pro benchmark score" == text.lower() 

    def is_going_to_Zenfone_7_Pro_Video(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "zenfone 7" in str(text).lower() and "pro" in str(text).lower() and "video" in str(text).lower()

    #ROG
    def is_going_to_ROG(self, event):
        text = event.message.text
        return "rog" in str(text).lower() and "phone" not in str(text).lower() or "3" not in str(text).lower() or "strix" not in str(text).lower()

    #ROG Phone 3 Strix
    def is_going_to_ROG_Phone_3_Strix(self, event):
        text = event.message.text
        return "rog phone 3 strix" == text.lower()
    
    def is_going_to_ROG_Phone_3_Strix_Price(self, event):
        text = event.message.text
        return "rog phone 3" in str(text).lower() and "strix" in str(text).lower() and "price" in str(text).lower()

    def is_going_to_ROG_Phone_3_Strix_Specs(self, event):
        text = event.message.text
        return "rog phone 3 strix specs" == text.lower()  

    def is_going_to_ROG_Phone_3_Strix_Pros_Cons(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Pros and Cons" in text
        return "rog phone 3 strix pros and cons" == text.lower()   

    def is_going_to_ROG_Phone_3_Strix_Benchmark_Score(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "rog phone 3 strix benchmark score" == text.lower()

    def is_going_to_ROG_Phone_3_Strix_Video(self, event):
        text = event.message.text
        #return "Iphone 12" and "Mini" not in text and "Pro" not in text or "Benchmark Score" in text  
        return "rog phone 3 strix video" == text.lower()



    #fsm
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
    # back to Iphone 12
    def on_enter_Back_IP12(self,event):
        print("I'm entering Iphone 12")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_IP12_carousel(reply_token)
    #Apple
    def on_enter_Apple(self, event):
        print("I'm entering Apple")
        reply_token = event.reply_token
        #text = "Please choose an Apple smartphone that you want to know about!"
        #send_text_message(reply_token, text)
        send_Apple_carousel(reply_token)
    #Iphone 12
    def on_enter_IP12(self, event):
        print("I'm entering Iphone 12")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_IP12_carousel(reply_token)

    def on_enter_IP12_Price(self, event):
        print("I'm entering Iphone 12's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of Iphone 12:\n 64GB: NTD 26900.00\n 128GB: NTD 28500.00\n 256GB: NTD 32000.00"
        current = "Iphone 12"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    def on_enter_IP12_Specs(self, event):
        print("I'm entering Iphone 12's specs")
        reply_token = event.reply_token
        myTuple = (
        "Body: Aluminum frame with matte finish, Ceramic Shield front with oleophobic coating, Glass back with glossy finish, IP68 certified for water and dust resistance. Black, White, Green, Blue, Red color options. 146.7 x 71.5 x 7.4 mm, 164 g.", 
        "Display: 6.1 Retina XDR OLED screen of 1170 x 2532 px resolution, 460ppi, 600 nits, 120Hz touch sensing. HDR10, Dolby Vision support, wide color gamut. True Tone.", 
        "Chipset: Apple A14 Bionic chip (5nm) - Hexa-core (2x3.1 GHz Firestorm + 4x1.8 GHz Icestorm with 3.1GHz Turboboost) Apple CPU, four-core Apple GPU, 16-core Apple NPU 4-gen",
        "Memory: 4GB of RAM; 64/128/256GB of internal storage",
        "Rear camera: Dual 12MP camera: 26mm main wide-angle, F/1.6, OIS, Dual Pixel AF; 13mm ultrawide-angle, F/2.4, 120-degree field of view; dual-LED flash with slow sync. Night Mode, Smart HDR 3, Deep Fusion.",
        "Video recording: 2160p@60/30fps, 1080p@30/60/120/240fps video recording with wider dynamic range and spatial sound, OIS + EIS, Dolby Vision (30fps only)",
        "Front camera: Dual camera - 23mm 12MP F/2.2 front-facing camera with HDR mode + 3D TOF camera; Night Mode, Smart HDR 3, Deep Fusion. 2160p@60/30fps, 1080p@30/60/120fps video recording with wider dynamic range and spatial sound, EIS.",
        "Connectivity: Dual SIM, 5G, 4G; Wi-Fi a/b/g/n/ac/6; Bluetooth 5.0; Lightning port; GPS with A-GPS, GLONASS, GALILEO, QZSS; NFC; Apple U1 chip ultrawideband",
        "Battery: 2,815 mAh battery, 20W fast charging, 15 Qi wireless charging (MagSafe)",
        "Misc: Face ID through dedicated TrueDepth camera, stereo speakers, Taptic Engine")

        x = "\n\n".join(myTuple)

        word = "Specs"
        information = x
        current = "Iphone 12"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    def on_enter_IP12_Pros_Cons(self, event):
        print("I'm entering Iphone 12's pros and cons")
        reply_token = event.reply_token
        myTuple = (
        "Pros:",
        "Attractive design with exquisite fit and premium finish",
        "Excellent OLED screen, very bright",
        "Loud stereo speakers, superb audio quality",
        "The fastest smartphone chip on the planet, 5G, too",
        "Good photo quality across the board, day and night",
        "LiDAR Scanner has varied applications and use cases (albeit quite niche)",
        "Consistently good video quality",
        "Apple iOS 14 is fast and easy to use, 5 years of guaranteed major updates",
        "MagSafe is a promising accessory concept",
        "\nCons:",
        "No charger or headphones in the box",
        "No high refresh rate screen",
        "Battery life is shorter than iPhone 11",
        "iOS needs better file management",
        "We miss TouchID as FaceID does not work with a mask on"
        )

        x = "\n\n".join(myTuple)
        
        word = "Pros and Cons"
        information = x
        current = "Iphone 12"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    def on_enter_IP12_Benchmark_Score(self, event):
        print("I'm entering Iphone 12's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Iphone 12 is 598,478."
        word = "Benchmark Score"
        information = x
        current = "Iphone 12"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)
    
    #Iphone 12 Pro
    def on_enter_Back_IP12_Pro(self,event):
        print("I'm entering Iphone 12 Pro")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_IP12_Pro_carousel(reply_token)

    def on_enter_IP12_Pro(self, event):
        print("I'm entering Iphone 12 Pro")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_IP12_Pro_carousel(reply_token)

    def on_enter_IP12_Pro_Price(self, event):
        print("I'm entering Iphone 12 Pro's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of Iphone 12 Pro is\n 128GB: NTD 33900.00\n 256GB: NTD 37400.00\n 512GB: NTD 44000.00"
        current = "Iphone 12 Pro"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    def on_enter_IP12_Pro_Specs(self, event):
        print("I'm entering Iphone 12 Pro's specs")
        reply_token = event.reply_token
        myTuple = (
        "Body: Stainless-steel frame with glossy finish, Ceramic Shield front with oleophobic coating, Glass back with frosted finish, IP68 certified for water and dust resistance. Silver, Graphite, Gold, Pacific Blue color options. 146.7 x 71.5 x 7.4 mm, 189 g.", 
        "Display: 6.1 Retina XDR OLED screen of 1170 x 2532 px resolution, 460ppi, 600 nits, 120Hz touch sensing. HDR10, Dolby Vision support, wide color gamut. True Tone.", 
        "Chipset: Apple A14 Bionic chip (5nm) - Hexa-core (2x3.1 GHz Firestorm + 4x1.8 GHz Icestorm with 3.1GHz Turboboost) Apple CPU, four-core Apple GPU, 16-core Apple NPU 4-gen",
        "Memory: 6GB of RAM; 128/256/512GB of internal storage",
        "Rear camera: Triple 12MP camera: 26mm main wide-angle, f/1.6, OIS, Dual Pixel AF; 13mm ultrawide-angle, f/2.4, 120-degree field of view; 52mm telephoto, f/2.0, OIS, 2x optical zoom; dual-LED flash with slow sync. Night Mode, Smart HDR 3, Deep Fusion.",
        "Video recording: 2160p@60/30fps, 1080p@30/60/120/240fps video recording with wider dynamic range and spatial sound, OIS + EIS, Dolby Vision",
        "Front camera: Dual camera - 23mm 12MP f/2.2 front-facing camera with HDR mode + 3D TOF camera; Night Mode, Smart HDR 3, Deep Fusion. 2160p@60/30fps, 1080p@30/60/120fps video recording with wider dynamic range and spatial sound, EIS.",
        "Connectivity: Dual SIM, 5G, 4G; Wi-Fi a/b/g/n/ac/6; Bluetooth 5.0; Lightning port; GPS with A-GPS, GLONASS, GALILEO, QZSS; NFC; Apple U1 chip ultrawideband",
        "Battery: 2,815 mAh battery, 20W fast charging, 15 Qi wireless charging (MagSafe)",
        "Misc: Face ID through dedicated TrueDepth camera, stereo speakers, Taptic Engine")

        x = "\n\n".join(myTuple)

        word = "Specs"
        information = x
        current = "Iphone 12 Pro"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    def on_enter_IP12_Pro_Pros_Cons(self, event):
        print("I'm entering Iphone 12 Pro's pros and cons")
        reply_token = event.reply_token
        myTuple = (
        "Pros:",
        "Attractive design with exquisite fit and premium finish",
        "Excellent OLED screen, very bright",
        "Loud stereo speakers, superb audio quality",
        "The fastest smartphone chip on the planet, 5G, too",
        "Good photo quality across the board, day and night",
        "LiDAR Scanner has varied applications and use cases (albeit quite niche)",
        "Consistently good video quality",
        "Apple iOS 14 is fast and easy to use, 5 years of guaranteed major updates",
        "MagSafe is a promising accessory concept",
        "\nCons:",
        "No charger or headphones in the box",
        "No high refresh rate screen",
        "Shorter battery life than the iPhone 11 Pro",
        "iOS needs better file management",
        "We miss TouchID as FaceID does not work with a mask on",
        "The best camera tech is exclusive to iPhone 12 Pro Max",
        "Few meaningful upgrades over iPhone 11 Pro and even fewer over iPhone 12"
        )

        x = "\n\n".join(myTuple)
        
        word = "Pros and Cons"
        information = x
        current = "Iphone 12 Pro"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    def on_enter_IP12_Pro_Benchmark_Score(self, event):
        print("I'm entering Iphone 12 Pro's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Iphone 12 Pro is 599059."
        word = "Benchmark Score"
        information = x
        current = "Iphone 12 Pro"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    #Iphone 12 Pro Max
    def on_enter_Back_IP12_Pro_Max(self,event):
        print("I'm entering Iphone 12 Pro Max")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_IP12_Pro_Max_carousel(reply_token)

    def on_enter_IP12_Pro_Max(self, event):
        print("I'm entering Iphone 12 Pro Max")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_IP12_Pro_Max_carousel(reply_token)

    def on_enter_IP12_Pro_Max_Price(self, event):
        print("I'm entering Iphone 12 Pro Max's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of Iphone 12 Pro Max is\n 128GB: NTD 37900.00\n 256GB: NTD 41400.00\n 512GB: NTD 48400.00"
        current = "Iphone 12 Pro Max"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    def on_enter_IP12_Pro_Max_Specs(self, event):
        print("I'm entering Iphone 12 Pro Max's specs")
        reply_token = event.reply_token
        myTuple = (
        "Body: Stainless-steel frame with glossy finish, Ceramic Shield front with oleophobic coating, Glass back with frosted finish, IP68 certified for water and dust resistance. Silver, Graphite, Gold, Pacific Blue color options. 160.8 x 78.1 x 7.4 mm, 228 g.", 
        "Display: 6.7 Retina XDR OLED screen of 1284 x 2778 px resolution, 458ppi, 800 nits, 120Hz touch sensing. HDR10, Dolby Vision support, wide color gamut. True Tone.", 
        "Chipset: Apple A14 Bionic chip (5nm) - Hexa-core (2x3.1 GHz Firestorm + 4x1.8 GHz Icestorm with 3.1GHz Turboboost) Apple CPU, four-core Apple GPU, 16-core Apple NPU 4-gen",
        "Memory: 6GB of RAM; 128/256/512GB of internal storage",
        "Rear camera: Triple 12MP camera: Primary - 1.7µm pixels, 26mm, f/1.6, IBIS, Dual Pixel AF; Ultrawide-angle - 1.0µm pixels, 13mm, f/2.4, 120-degree field of view; Telephoto -- 1.0µm pixels, 65mm, f/2.2, OIS, 2.5x optical zoom; dual-LED flash with slow sync. Night Mode, Smart HDR 3, Deep Fusion.",
        "Video recording: 2160p@60/30fps, 1080p@30/60/120/240fps video recording with wider dynamic range and spatial sound, OIS + EIS, Dolby Vision capturing",
        "Front camera: Dual camera - 23mm 12MP f/2.2 front-facing camera with HDR mode + 3D TOF camera; Night Mode, Smart HDR 3, Deep Fusion. 2160p@60/30fps, 1080p@30/60/120fps video recording with wider dynamic range and spatial sound, EIS.",
        "Connectivity: Dual SIM, 5G, 4G; Wi-Fi a/b/g/n/ac/6; Bluetooth 5.0; Lightning port; GPS with A-GPS, GLONASS, GALILEO, QZSS; NFC; Apple U1 chip ultrawideband",
        "Battery: 3,687 mAh battery, 20W fast charging, 15 Qi wireless charging (MagSafe)",
        "Misc: Face ID through dedicated TrueDepth camera, stereo speakers, Taptic Engine")

        x = "\n\n".join(myTuple)

        word = "Specs"
        information = x
        current = "Iphone 12 Pro Max"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    def on_enter_IP12_Pro_Max_Pros_Cons(self, event):
        print("I'm entering Iphone 12 Pro Max's pros and cons")
        reply_token = event.reply_token
        myTuple = (
        "Pros:",
        "Sumptuous design with jewelry-like attention to detail, durable and water-resistant",
        "Excellent OLED screen, very bright",
        "Loud stereo speakers, superb audio quality",
        "The fastest smartphone chip on the planet, 5G, too",
        "Dependable battery life, fast charging",
        "Apple iOS 14 is fast and easy to use, 5 years of guaranteed major updates",
        "Very good photo and video quality across the board, day and night"
        "LiDAR Scanner has varied applications and use cases (albeit quite niche)",
        "MagSafe is a promising accessory concept",
        "\nCons:",
        "No charger or headphones in the box",
        "No high refresh rate screen",
        "iOS needs better file management",
        "We miss TouchID as FaceID does not work with a mask on",
        "The new camera offers the same quality as the old one",
        "Few meaningful upgrades over iPhone 11 Pro Max and even fewer over iPhone 12 Pro"
        )

        x = "\n\n".join(myTuple)
        
        word = "Pros and Cons"
        information = x
        current = "Iphone 12 Pro Max"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    def on_enter_IP12_Pro_Max_Benchmark_Score(self, event):
        print("I'm entering Iphone 12 Pro Max's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Iphone 12 Pro Max is 638841."
        word = "Benchmark Score"
        information = x
        current = "Iphone 12 Pro Max"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)
    
    #Iphone 12 Mini
    def on_enter_IP12_Mini(self, event):
        print("I'm entering Iphone 12 Mini")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_IP12_Mini_carousel(reply_token)

    def on_enter_IP12_Mini_Price(self, event):
        print("I'm entering Iphone 12 Mini's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of Iphone 12 Mini:\n 64GB: NTD 23900.00\n 128GB: NTD 25500.00\n 256GB: NTD 29000.00"
        current = "Iphone 12 Mini"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    def on_enter_IP12_Mini_Specs(self, event):
        print("I'm entering Iphone 12 Mini's specs")
        reply_token = event.reply_token
        myTuple = (
        "Body: Aluminum frame with matte finish, Ceramic Shield front with oleophobic coating, Glass back with glossy finish, IP68 certified for water and dust resistance. Black, White, Green, Blue, Red color options. 131.5 x 64.2 x 7.4 mm, 135 g.", 
        "Display: 5.4 Retina XDR OLED screen of 1,080 x 2,340 px resolution, 476ppi, 600 nits, 120Hz touch sensing. HDR10, Dolby Vision support, wide color gamut. True Tone.", 
        "Chipset: Apple A14 Bionic chip (5nm) - Hexa-core (2x3.1 GHz Firestorm + 4x1.8 GHz Icestorm with 3.1GHz Turboboost) Apple CPU, four-core Apple GPU, 16-core Apple NPU 4-gen",
        "Memory: 4GB of RAM; 64/128/256GB of internal storage",
        "Rear camera: Dual 12MP camera: 26mm main wide-angle, F/1.6, OIS, Dual Pixel AF; 13mm ultrawide-angle, F/2.4, 120-degree field of view; dual-LED flash with slow sync. Night Mode, Smart HDR 3, Deep Fusion.",
        "Video recording: 2160p@60/30fps, 1080p@30/60/120/240fps video recording with wider dynamic range and spatial sound, OIS + EIS, Dolby Vision (30fps only)",
        "Front camera: Dual camera - 23mm 12MP F/2.2 front-facing camera with HDR mode + 3D TOF camera; Night Mode, Smart HDR 3, Deep Fusion. 2160p@60/30fps, 1080p@30/60/120fps video recording with wider dynamic range and spatial sound, EIS.",
        "Connectivity: Dual SIM, 5G, 4G; Wi-Fi a/b/g/n/ac/6; Bluetooth 5.0; Lightning port; GPS with A-GPS, GLONASS, GALILEO, QZSS; NFC; Apple U1 chip ultrawideband",
        "Battery: 2,227 mAh battery, 20W fast charging, 12W Qi wireless charging (MagSafe)",
        "Misc: Face ID through dedicated TrueDepth camera, stereo speakers, Taptic Engine")

        x = "\n\n".join(myTuple)

        word = "Specs"
        information = x
        current = "Iphone 12 Mini"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    def on_enter_IP12_Mini_Pros_Cons(self, event):
        print("I'm entering Iphone 12 Mini's pros and cons")
        reply_token = event.reply_token
        myTuple = (
        "Pros:",
        "The cheapest in the iPhone 12 series",
        "The most compact flagship smartphone you'd find today",
        "Attractive design with great grip and premium durability",
        "Excellent OLED screen, very bright",
        "Good battery life for such a small cell",
        "Loud stereo speakers",
        "The fastest smartphone chip on the planet, 5G, too",
        "Good photo quality across the board, day and night",
        "Apple iOS 14 is fast and easy to use, 5 years of guaranteed major updates",
        "MagSafe is a promising accessory concept",
        "\nCons:",
        "No charger or headphones in the box",
        "No high refresh rate screen",
        "Battery life is shorter than iPhone 11",
        "iOS needs better file management",
        "We miss TouchID as FaceID does not work with a mask on"
        "Prone to performance throttling",
        "The notch looks bigger than ever on this small phone",
        )

        x = "\n\n".join(myTuple)
        
        word = "Pros and Cons"
        information = x
        current = "Iphone 12 Mini"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    def on_enter_IP12_Mini_Benchmark_Score(self, event):
        print("I'm entering Iphone 12 Mini's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Iphone 12 Mini is 614169."
        word = "Benchmark Score"
        information = x
        current = "Iphone 12 Mini"
        brand = "Apple"
        send_info(reply_token, word, information, current, brand)

    #Google
    def on_enter_Google(self, event):
        print("I'm entering Google")
        reply_token = event.reply_token
        #text = "Please choose an Apple smartphone that you want to know about!"
        #send_text_message(reply_token, text)
        send_Google_carousel(reply_token)
        
    #Pixel 5
    def on_enter_Pixel_5(self, event):
        print("I'm entering Pixel 5")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_Pixel_5_carousel(reply_token)

    def on_enter_Pixel_5_Price(self, event):
        print("I'm entering Pixel 5's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of Pixel 5 is NTD 18990"
        current = "Pixel 5"
        brand = "Google"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Pixel_5_Specs(self, event):
        print("I'm entering Pixel 5's specs")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/google_pixel_5-review-2185.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-findings"})
        lis = []
        lis2 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)
                
        str1 = "\n\n"
        str1 = str1.join(lis2)
        

        word = "Specs"
        information = str1
        current = "Pixel 5"
        brand = "Google"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Pixel_5_Pros_Cons(self, event):
        print("I'm entering Pixel 5's pros and cons")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/google_pixel_5-review-2185p6.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-features"})
        containers2 = page_soup.findAll("ul",{"class":"article-blurb article-blurb-disadvantages"})
        lis = []
        lis2 = []
        lis3 = []
        lis4 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)

        lis2.append("\n")

        for ul2 in containers2:
            for li2 in ul2.findAll('li'):
                    if li2.find('ul'):
                        break
                    lis3.append(li2)

        for li in lis3:
            test2 = str(li.text.encode("utf-8"))
            mod_string2 = ""
            
            for i in range(1, len(test2)):
                mod_string2 = mod_string2 + test2[i]
                mod_string2 = mod_string2.replace("'","")
            lis4.append(mod_string2)


        str1 = "\n\n"
        str2 = str1.join(lis2) 
        str3 = "Pros\n\n\n" + str2 

        str4 = "\n\n"
        str5 = str4.join(lis4)
        str6 = "Cons\n\n\n" + str5

        str7 = str3 + str6
        word = "Pros and Cons"
        information = str7
        current = "Pixel 5"
        brand = "Google"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Pixel_5_Benchmark_Score(self, event):
        print("I'm entering Pixel 5's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Pixel 5 is 330,500."
        word = "Benchmark Score"
        information = x
        current = "Pixel 5"
        brand = "Google"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Pixel_5_Video(self, event): 
        print("I'm entering Pixel 5's Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=NBLO6RpofIU'
        send_text_message(reply_token, url)

    #Pixel 4a
    def on_enter_Pixel_4a(self, event):
        print("I'm entering Pixel 4a")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_Pixel_4a_carousel(reply_token)

    def on_enter_Pixel_4a_Price(self, event):
        print("I'm entering Pixel 4a's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of Pixel 4a is NTD 11990"
        current = "Pixel 4a"
        brand = "Google"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Pixel_4a_Specs(self, event):
        print("I'm entering Pixel 4a's specs")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/google_pixel_4a-review-2148.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-findings"})
        lis = []
        lis2 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)
                
        str1 = "\n\n"
        str1 = str1.join(lis2)
        

        word = "Specs"
        information = str1
        current = "Pixel 4a"
        brand = "Google"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Pixel_4a_Pros_Cons(self, event):
        print("I'm entering Pixel 4a's pros and cons")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/google_pixel_4a-review-2148p6.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-features"})
        containers2 = page_soup.findAll("ul",{"class":"article-blurb article-blurb-disadvantages"})
        lis = []
        lis2 = []
        lis3 = []
        lis4 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)

        lis2.append("\n")

        for ul2 in containers2:
            for li2 in ul2.findAll('li'):
                    if li2.find('ul'):
                        break
                    lis3.append(li2)

        for li in lis3:
            test2 = str(li.text.encode("utf-8"))
            mod_string2 = ""
            
            for i in range(1, len(test2)):
                mod_string2 = mod_string2 + test2[i]
                mod_string2 = mod_string2.replace("'","")
            lis4.append(mod_string2)


        str1 = "\n\n"
        str2 = str1.join(lis2) 
        str3 = "Pros\n\n\n" + str2 

        str4 = "\n\n"
        str5 = str4.join(lis4)
        str6 = "Cons\n\n\n" + str5

        str7 = str3 + str6
        word = "Pros and Cons"
        information = str7
        current = "Pixel 4a"
        brand = "Google"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Pixel_4a_Benchmark_Score(self, event):
        print("I'm entering Pixel 4a's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Pixel 4a is 268,973."
        word = "Benchmark Score"
        information = x
        current = "Pixel 4a"
        brand = "Google"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Pixel_4a_Video(self, event): 
        print("I'm entering Pixel 4a's Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=dlHnleQU9tQ'
        send_text_message(reply_token, url)

    #Pixel 4a 5G
    def on_enter_Pixel_4a_5G(self, event):
        print("I'm entering Pixel 4a 5G")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_Pixel_4a_5G_carousel(reply_token)

    def on_enter_Pixel_4a_5G_Price(self, event):
        print("I'm entering Pixel 4a 5G's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of Pixel 4a 5G is NTD 15990"
        current = "Pixel 4a 5G"
        brand = "Google"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Pixel_4a_5G_Specs(self, event):
        print("I'm entering Pixel 4a 5G's specs")
        reply_token = event.reply_token
        myTuple = (
        "Processor: Qualcomm Snapdragon 765G", 
        "RAM: 6GB", 
        "Internal Storage: 128GB",
        "Main Display: 6.2-inch OLED with transmissive hole",
        "Display resolution: 2,340 x 1,080 (19.5:9)",
        "Rear cameras: 12.2MP f/1.7 camera with HDR, optical + digital image stabilization and autofocus with dual pixel phase detection and 16MP f/2.2 ultrawide camera with 107-degree field of view",
        "Front-facing camera: 8MP f/2.0 camera with 83 degree FOV",
        "OS: Android 11",
        "Charging: USB C with USB-PD 2.0, supports 18W fast charging",
        "Battery size: 3,800mAh (min); 3,885mAh (typical)",
        "Dimensions: 6.1 x 2.9 x 0.3 inches",
        "Weight: 168g (sub-6 only) / 171g (mmWave and sub-6)",
        "Fingerprint sensor: Yes, on rear",
        "Waterproofing: No",
        "NFC: Yes",
        "Headphone jack: Yes")

        x = "\n\n".join(myTuple)
        

        word = "Specs"
        information = x
        current = "Pixel 4a 5G"
        brand = "Google"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Pixel_4a_5G_Pros_Cons(self, event):
        print("I'm entering Pixel 4a 5G's pros and cons")
        reply_token = event.reply_token
        myTuple = (
        "Pros:",
        "Large, colorful display",
        "5G phone for less than $500",
        "Excellent cameras",
        "Google's latest software",
        "\nCons:",
        "Poor battery life",
        "Subpar performance relative to similar phones"
        )

        x = "\n\n".join(myTuple)

        word = "Pros and Cons"
        information = x
        current = "Pixel 4a 5G"
        brand = "Google"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Pixel_4a_5G_Benchmark_Score(self, event):
        print("I'm entering Pixel 4a 5G's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Pixel 4a 5G is 326688."
        word = "Benchmark Score"
        information = x
        current = "Pixel 4a 5G"
        brand = "Google"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Pixel_4a_5G_Video(self, event): 
        print("I'm entering Pixel 4a 5G's Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=NXW8eHaXlvE'
        send_text_message(reply_token, url)
    
    #Sony
    def on_enter_Sony(self, event):
        print("I'm entering Sony")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_Sony_carousel(reply_token)

    #Xperia 5 II
    def on_enter_Xperia_5_II(self, event):
        print("I'm entering Xperia 5 II")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_Xperia_5_II_carousel(reply_token)

    def on_enter_Xperia_5_II_Price(self, event):
        print("I'm entering Xperia 5 II's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of Xperia 5 II is NTD 29990"
        current = "Xperia 5 II"
        brand = "Sony"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Xperia_5_II_Specs(self, event):
        print("I'm entering Xperia 5 II's specs")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/sony_xperia_5_ii-review-2173.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-findings"})
        lis = []
        lis2 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)
                
        str1 = "\n\n"
        str1 = str1.join(lis2)
        

        word = "Specs"
        information = str1
        current = "Xperia 5 II"
        brand = "Sony"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Xperia_5_II_Pros_Cons(self, event):
        print("I'm entering Xperia 5 II's pros and cons")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/sony_xperia_5_ii-review-2173p6.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-features"})
        containers2 = page_soup.findAll("ul",{"class":"article-blurb article-blurb-disadvantages"})
        lis = []
        lis2 = []
        lis3 = []
        lis4 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)

        lis2.append("\n")

        for ul2 in containers2:
            for li2 in ul2.findAll('li'):
                    if li2.find('ul'):
                        break
                    lis3.append(li2)

        for li in lis3:
            test2 = str(li.text.encode("utf-8"))
            mod_string2 = ""
            
            for i in range(1, len(test2)):
                mod_string2 = mod_string2 + test2[i]
                mod_string2 = mod_string2.replace("'","")
            lis4.append(mod_string2)


        str1 = "\n\n"
        str2 = str1.join(lis2) 
        str3 = "Pros\n\n\n" + str2 

        str4 = "\n\n"
        str5 = str4.join(lis4)
        str6 = "Cons\n\n\n" + str5

        str7 = str3 + str6
        word = "Pros and Cons"
        information = str7
        current = "Xperia 5 II"
        brand = "Sony"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Xperia_5_II_Benchmark_Score(self, event):
        print("I'm entering Xperia 5 II's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Xperia 5 II is 565,000."
        word = "Benchmark Score"
        information = x
        current = "Xperia 5 II"
        brand = "Sony"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Xperia_5_II_Video(self, event): 
        print("I'm entering Xperia 5 II's Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=fTCNzUF82cY'
        send_text_message(reply_token, url)    

    #Xperia 1 II
    def on_enter_Xperia_1_II(self, event):
        print("I'm entering Xperia 1 II")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_Xperia_1_II_carousel(reply_token)

    def on_enter_Xperia_1_II_Price(self, event):
        print("I'm entering Xperia 1 II's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of Xperia 1 II is NTD 33990"
        current = "Xperia 1 II"
        brand = "Sony"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Xperia_1_II_Specs(self, event):
        print("I'm entering Xperia 1 II's specs")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/sony_xperia_1_ii-review-2115.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-findings"})
        lis = []
        lis2 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)
                
        str1 = "\n\n"
        str1 = str1.join(lis2)
        

        word = "Specs"
        information = str1
        current = "Xperia 1 II"
        brand = "Sony"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Xperia_1_II_Pros_Cons(self, event):
        print("I'm entering Xperia 1 II's pros and cons")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/sony_xperia_1_ii-review-2115p7.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-features"})
        containers2 = page_soup.findAll("ul",{"class":"article-blurb article-blurb-disadvantages"})
        lis = []
        lis2 = []
        lis3 = []
        lis4 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)

        lis2.append("\n")

        for ul2 in containers2:
            for li2 in ul2.findAll('li'):
                    if li2.find('ul'):
                        break
                    lis3.append(li2)

        for li in lis3:
            test2 = str(li.text.encode("utf-8"))
            mod_string2 = ""
            
            for i in range(1, len(test2)):
                mod_string2 = mod_string2 + test2[i]
                mod_string2 = mod_string2.replace("'","")
            lis4.append(mod_string2)


        str1 = "\n\n"
        str2 = str1.join(lis2) 
        str3 = "Pros\n\n\n" + str2 

        str4 = "\n\n"
        str5 = str4.join(lis4)
        str6 = "Cons\n\n\n" + str5

        str7 = str3 + str6
        word = "Pros and Cons"
        information = str7
        current = "Xperia 1 II"
        brand = "Sony"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Xperia_1_II_Benchmark_Score(self, event):
        print("I'm entering Xperia 1 II's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Xperia 1 II is 535,667."
        word = "Benchmark Score"
        information = x
        current = "Xperia 1 II"
        brand = "Sony"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Xperia_1_II_Video(self, event): 
        print("I'm entering Xperia 1 II's Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=XP9hi_Lw4_Q'
        send_text_message(reply_token, url)    

    #Xperia 10 II
    def on_enter_Xperia_10_II(self, event):
        print("I'm entering Xperia 10 II")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_Xperia_10_II_carousel(reply_token)

    def on_enter_Xperia_10_II_Price(self, event):
        print("I'm entering Xperia 10 II's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of Xperia 10 II is NTD 11490"
        current = "Xperia 10 II"
        brand = "Sony"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Xperia_10_II_Specs(self, event):
        print("I'm entering Xperia 10 II's specs")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/sony_xperia_10_ii-review-2119.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-findings"})
        lis = []
        lis2 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)
                
        str1 = "\n\n"
        str1 = str1.join(lis2)
        

        word = "Specs"
        information = str1
        current = "Xperia 10 II"
        brand = "Sony"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Xperia_10_II_Pros_Cons(self, event):
        print("I'm entering Xperia 10 II's pros and cons")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/sony_xperia_10_ii-review-2119p7.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-features"})
        containers2 = page_soup.findAll("ul",{"class":"article-blurb article-blurb-disadvantages"})
        lis = []
        lis2 = []
        lis3 = []
        lis4 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)

        lis2.append("\n")

        for ul2 in containers2:
            for li2 in ul2.findAll('li'):
                    if li2.find('ul'):
                        break
                    lis3.append(li2)

        for li in lis3:
            test2 = str(li.text.encode("utf-8"))
            mod_string2 = ""
            
            for i in range(1, len(test2)):
                mod_string2 = mod_string2 + test2[i]
                mod_string2 = mod_string2.replace("'","")
            lis4.append(mod_string2)


        str1 = "\n\n"
        str2 = str1.join(lis2) 
        str3 = "Pros\n\n\n" + str2 

        str4 = "\n\n"
        str5 = str4.join(lis4)
        str6 = "Cons\n\n\n" + str5

        str7 = str3 + str6
        word = "Pros and Cons"
        information = str7
        current = "Xperia 10 II"
        brand = "Sony"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Xperia_10_II_Benchmark_Score(self, event):
        print("I'm entering Xperia 10 II's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Xperia 10 II is 170,000."
        word = "Benchmark Score"
        information = x
        current = "Xperia 10 II"
        brand = "Sony"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Xperia_10_II_Video(self, event): 
        print("I'm entering Xperia 10 II's Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=BF2HYfAmToI'
        send_text_message(reply_token, url)    

    #Asus
    def on_enter_Asus(self, event):
        print("I'm entering Asus")
        reply_token = event.reply_token
        #text = "Please choose an Apple smartphone that you want to know about!"
        #send_text_message(reply_token, text)
        send_Asus_chooser(reply_token)

    #Zenfone
    def on_enter_Zenfone(self, event):
        print("I'm entering Zenfone")
        reply_token = event.reply_token
        #text = "Please choose an Apple smartphone that you want to know about!"
        #send_text_message(reply_token, text)
        send_Zenfone_carousel(reply_token)

    #ROG
    def on_enter_ROG(self, event):
        print("I'm entering ROG")
        reply_token = event.reply_token
        #text = "Please choose an Apple smartphone that you want to know about!"
        #send_text_message(reply_token, text)
        send_ROG_carousel(reply_token)

    #Zenfone 7 Pro
    def on_enter_Zenfone_7_Pro(self, event):
        print("I'm entering Zenfone 7 Pro")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_Zenfone_7_Pro_carousel(reply_token)

    def on_enter_Zenfone_7_Pro_Price(self, event):
        print("I'm entering Zenfone 7 Pro's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of Zenfone 7 Pro is NTD 25112"
        current = "Zenfone 7 Pro"
        brand = "Asus"
        series = "Zenfone"
        send_info_2(reply_token, word, information, current, brand, series)

    def on_enter_Zenfone_7_Pro_Specs(self, event):
        print("I'm entering Zenfone 7 Pro's specs")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/asus_zenfone_7_pro-review-2156.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-findings"})
        lis = []
        lis2 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)
                
        str1 = "\n\n"
        str1 = str1.join(lis2)
        

        word = "Specs"
        information = str1
        current = "Zenfone 7 Pro"
        brand = "Asus"
        series = "Zenfone"
        send_info_2(reply_token, word, information, current, brand, series)

    def on_enter_Zenfone_7_Pro_Pros_Cons(self, event):
        print("I'm entering Zenfone 7 Pro's pros and cons")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/asus_zenfone_7_pro-review-2156p7.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-features"})
        containers2 = page_soup.findAll("ul",{"class":"article-blurb article-blurb-disadvantages"})
        lis = []
        lis2 = []
        lis3 = []
        lis4 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)

        lis2.append("\n")

        for ul2 in containers2:
            for li2 in ul2.findAll('li'):
                    if li2.find('ul'):
                        break
                    lis3.append(li2)

        for li in lis3:
            test2 = str(li.text.encode("utf-8"))
            mod_string2 = ""
            
            for i in range(1, len(test2)):
                mod_string2 = mod_string2 + test2[i]
                mod_string2 = mod_string2.replace("'","")
            lis4.append(mod_string2)


        str1 = "\n\n"
        str2 = str1.join(lis2) 
        str3 = "Pros\n\n\n" + str2 

        str4 = "\n\n"
        str5 = str4.join(lis4)
        str6 = "Cons\n\n\n" + str5

        str7 = str3 + str6
        word = "Pros and Cons"
        information = str7
        current = "Zenfone 7 Pro"
        brand = "Asus"
        series = "Zenfone"
        send_info_2(reply_token, word, information, current, brand, series)

    def on_enter_Zenfone_7_Pro_Benchmark_Score(self, event):
        print("I'm entering Zenfone 7 Pro's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Zenfone 7 Pro is 654,000."
        word = "Benchmark Score"
        information = x
        current = "Zenfone 7 Pro"
        brand = "Asus"
        series = "Zenfone"
        send_info_2(reply_token, word, information, current, brand, series)

    def on_enter_Zenfone_7_Pro_Video(self, event): 
        print("I'm entering Zenfone 7 Pro's Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=0lb1YaAxmKY'
        send_text_message(reply_token, url)    


    #Zenfone 7
    def on_enter_Zenfone_7(self, event):
        print("I'm entering Zenfone 7")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_Zenfone_7_carousel(reply_token)

    def on_enter_Zenfone_7_Price(self, event):
        print("I'm entering Zenfone 7's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of Zenfone 7:\n 6GB/128GB: NTD 18990\n 8GB/128GB: NTD 22112"
        current = "Zenfone 7"
        brand = "Asus"
        series = "Zenfone"
        send_info_2(reply_token, word, information, current, brand, series)

    def on_enter_Zenfone_7_Specs(self, event):
        print("I'm entering Zenfone 7's specs")
        reply_token = event.reply_token
        myTuple = (
        "Display:"
        "Size: 6.7 inches", 
        "Resolution: 2400 x 1080 pixels, 20:9 ratio, 395 PPI", 
        "Technology: AMOLED",
        "Screen-to-body: 84.25 %",
        "Peak brightness: 700 cd/m2 (nit)",
        "Features:	90Hz refresh rate, HDR video support, Scratch-resistant glass (Corning Gorilla Glass 6), Ambient light sensor, Proximity sensor",
        "\nHardware:",
        "System chip: Qualcomm Snapdragon 865 SM8250",
        "Processor:	Octa-core, 2840 MHz, Kryo 585, 64-bit, 7 nm",
        "GPU: Adreno 650",
        "RAM: 6GB/8GB LPDDR5",
        "Internal storage: 128GB (UFS 3.1)",
        "Storage expansion:	microSDXC up to 2000 GB",
        "Device type: Smartphone",
        "OS: Android (10), Asus Zen UI",
        "\nBattery:",
        "Capacity: 5000 mAh",
        "Charging: Qualcomm Quick Charge 4, USB Power Delivery, Reverse charging",
        "Max Charge Speed: Wired: 30.0W",
        "\nCamera",
        "Rear: Triple camera, Swivel",
        "Main camera: 64 MP (Doubles as a front camera, PDAF) Aperture size: F1.8; Focal length: 26 mm; Sensor size: 1/1.7; Pixel size: 0.8 μm",
        "Second camera: 8 MP (Telephoto, Doubles as a front camera, PDAF) Optical zoom: 3x; Aperture size: F2.4; Focal Length: 80 mm",
        "Third camera: 12 MP (Ultra-wide, Doubles as a front camera, PDAF) Aperture size: F2.2; Focal Length: 17 mm; Sensor size: 1/2.55; Pixel size: 1.4 μm",
        "Video recording: 7680x4320 (8K UHD) (30 fps), 3840x2160 (4K UHD) (120 fps), 1920x1080 (Full HD) (240 fps), 1280x720 (HD) (480 fps) Features: Time-lapse video, Picture-taking during video recording, EIS", 
        "\nDesign:",
        "Dimensions: 6.50 x 3.04 x 0.38 inches (165.08 x 77.28 x 9.6 mm)",
        "Weight: 8.11 oz (230.0 g)",
        "Materials:\n Back: Glass (Corning Gorilla Glass 3); Frame: Aluminum",
        "Keys:\n Right: Volume control, Lock/Unlock key",
        "Colors: Pastel white, Aurora black",
        "\Cellular:",
        "5G: Yes",
        "Dual SIM: Yes",
        "SIM Type: Nano SIM",
        "\nMultimedia:",
        "Headphones: No 3.5 mm jack",
        "Speakers: Earpice, Multiple speakers",
        "Features: aptX",
        "Screen mirroring: Wireless screen share",
        "Additional microphone(s): fpr Noise cancellation, Video recording",
        "\nConnectivity and Features:",
        "Bluetooth: 5.1, EDR",
        "Wi-Fi: 802.11 a, b, g, n, ac, ax (Wi-Fi 6), dual-band; MIMO, Wi-Fi Direct, Hotspot",
        "USB: Type-C(reversible) Charging, Heaphones port",
        "Location: GPS, A-GPS, Glonass, Galileo, BeiDou, Cell ID, Wi-Fi positioning",
        "Sensors: Accelerometer, Gyroscope, Compass, Hall (for flip covers)",
        "Other: NFC"
        )

        x = "\n\n".join(myTuple)
        

        word = "Specs"
        information = x
        current = "Zenfone 7"
        brand = "Asus"
        series = "Zenfone"
        send_info_2(reply_token, word, information, current, brand, series)

    def on_enter_Zenfone_7_Pros_Cons(self, event):
        print("I'm entering Zenfone 7's pros and cons")
        reply_token = event.reply_token
        myTuple = (
        "Pros:",
        "A 5000 mAh long-lasting battery capacity",
        "Fantastic integrated camera configuration",
        "Next-level performance can be estimated with the Snapdragon 865 chipset",
        "Outstanding game experience",
        "90 Hz refresh rate with HDR 10+ support",
        "Gorilla Glass 6 Protection",
        "\nCons:",
        "The Motorized flip-up main camera can easily be damaged",
        "Little expensive with this specs",
        "Without Wireless charging",
        "Bloatware problems",
        "Without a 3.5 mm jack"
        )

        x = "\n\n".join(myTuple)

        word = "Pros and Cons"
        information = x
        current = "Zenfone 7"
        brand = "Asus"
        series = "Zenfone"
        send_info_2(reply_token, word, information, current, brand, series)

    def on_enter_Zenfone_7_Benchmark_Score(self, event):
        print("I'm entering Zenfone 7's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Zenfone 7 is 590,000."
        word = "Benchmark Score"
        information = x
        current = "Zenfone 7"
        brand = "Asus"
        series = "Zenfone"
        send_info_2(reply_token, word, information, current, brand, series)

    def on_enter_Zenfone_7_Video(self, event): 
        print("I'm entering Zenfone 7's Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=OOxbMl1bYyw'
        send_text_message(reply_token, url)   

    #ROG Phone 3 Strix
    def on_enter_ROG_Phone_3_Strix(self, event):
        print("I'm entering ROG Phone 3 Strix")
        reply_token = event.reply_token
        #text = "Please choose which information you want to know!"
        #send_text_message(reply_token, text)
        send_ROG_Phone_3_Strix_carousel(reply_token)

    def on_enter_ROG_Phone_3_Strix_Price(self, event):
        print("I'm entering ROG Phone 3 Strix's price")
        reply_token = event.reply_token
        word = "Price"
        information = "The Price of ROG Phone 3 Strix:\n 8GB/128GB: NTD 19825\n 8GB/256GB: NTD 21960\n 12GB/128GB: NTD 25010"
        current = "ROG Phone 3 Strix"
        brand = "Asus"
        series = "ROG"
        send_info_2(reply_token, word, information, current, brand, series)

    def on_enter_ROG_Phone_3_Strix_Specs(self, event):
        print("I'm entering ROG Phone 3 Strix's specs")
        reply_token = event.reply_token
        myTuple = ("Body: 171mm x 78mm x9.85mm, 240g; Glass front (Gorilla Glass 6), glass back (Gorilla Glass 3), metal frame; Colors: Black.",
        "Display: 6.59 AMOLED, 1080x2340px resolution, 19.5:9 aspect ratio, 391ppi; HDR10+, 144Hz refresh rate, 270Hz touch sampling rate.",
        "Chipset: Qualcomm SM8250 Snapdragon 865 (7 nm+): Octa-core (1x2.84 GHz Kryo 585 & 3x2.42 GHz Kryo 585 & 4x1.8 GHz Kryo 585); Adreno 650.",
        "Memory: 128GB 8GB RAM, 128GB 12GB RAM, 256GB 8GB RAM; UFS 3.1 storage LPDDR5 RAM.",
        "OS/Software: Android 10, ROG UI.",
        "Rear camera: Wide (main): 64 MP, f/1.8, (wide), 1/1.7, PDAF; Ultra-wide angle: 13 MP, f/2.4, 11mm (ultrawide); Macro: 5 MP, f/2.0; LED flash, HDR, panorama.",
        "Front camera: 24 MP, f/2.0, 27mm.",
        "Video capture: Rear camera: 8K@30, 4K@30/60/120fps, 1080p@30/60/240fps, 720p@480fps; gyro-EIS; Front camera: 1080p@30fps.",
        "Battery: 6000mAh; Fast charging 30W, Direct Charge (Asus HYPERCHARGE), Power Delivery 3.0 + PPS, Quick Charge 4.0.",
        "Connectivity: 5G (Sub-6), optional Dual SIM support (5G + 4G or 4G + 4G dual standby), Dual-Band Wi-Fi a/b/g/n/ac/ax 2x2 MIMO, Wi-Fi 6, Bluetooth 5.1, GPS (GNSS, Glonass, Galileo, BeiDou, QZSS, NavIC), NFC; Side-port: 48 pin, based on Type-C",       
        "Misc: Fingerprint (under display, optical), accelerometer, gyro, proximity, e-compass, Hall sensor, ambient light sensor, Ultrasonic sensors for AirTrigger 3 and grip press; RGB logo on back; RGB illuminator LED next to flash; Dual 7-magnet front-facing speakers, dual NXP TFA9874 amplifiers; Hi-Res audio output."
        )
        
        x = "\n\n".join(myTuple)

        word = "Specs"
        information = x
        current = "ROG Phone 3 Strix"
        brand = "Asus"
        series = "ROG"
        send_info_2(reply_token, word, information, current, brand, series)

    def on_enter_ROG_Phone_3_Strix_Pros_Cons(self, event):
        print("I'm entering ROG Phone 3 Strix's pros and cons")
        reply_token = event.reply_token
        my_url = "https://www.gsmarena.com/asus_rog_phone_3-review-2137p8.php"

        #opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html, "html.parser")

        #grabs each product
        containers = page_soup.findAll("ul", {"class":"article-blurb article-blurb-features"})
        containers2 = page_soup.findAll("ul",{"class":"article-blurb article-blurb-disadvantages"})
        lis = []
        lis2 = []
        lis3 = []
        lis4 = []
        for ul in containers:
            for li in ul.findAll('li'):
                    if li.find('ul'):
                        break
                    lis.append(li)

        for li in lis:
            test = str(li.text.encode("utf-8"))
            mod_string = ""
            
            for i in range(1, len(test)):
                mod_string = mod_string + test[i]
                mod_string = mod_string.replace("'","")
            lis2.append(mod_string)

        lis2.append("\n")

        for ul2 in containers2:
            for li2 in ul2.findAll('li'):
                    if li2.find('ul'):
                        break
                    lis3.append(li2)

        for li in lis3:
            test2 = str(li.text.encode("utf-8"))
            mod_string2 = ""
            
            for i in range(1, len(test2)):
                mod_string2 = mod_string2 + test2[i]
                mod_string2 = mod_string2.replace("'","")
            lis4.append(mod_string2)


        str1 = "\n\n"
        str2 = str1.join(lis2) 
        str3 = "Pros\n\n\n" + str2 

        str4 = "\n\n"
        str5 = str4.join(lis4)
        str6 = "Cons\n\n\n" + str5

        str7 = str3 + str6
        word = "Pros and Cons"
        information = str7
        current = "ROG Phone 3 Strix"
        brand = "Asus"
        series = "ROG"
        send_info_2(reply_token, word, information, current, brand, series)

    def on_enter_ROG_Phone_3_Strix_Benchmark_Score(self, event):
        print("I'm entering ROG Phone 3 Strix's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of ROG Phone 3 Strix is 585,000."
        word = "Benchmark Score"
        information = x
        current = "ROG Phone 3 Strix"
        brand = "Asus"
        series = "ROG"
        send_info_2(reply_token, word, information, current, brand, series)

    def on_enter_ROG_Phone_3_Strix_Video(self, event): 
        print("I'm entering ROG Phone 3 Strix's Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=OuuNpp97WII'
        send_text_message(reply_token, url)  


    #FSM
    def on_enter_fsm(self, event):
        print("I'm entering fsm")
        reply_token = event.reply_token
        send_fsm(reply_token)