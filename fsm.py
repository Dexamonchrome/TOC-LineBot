from transitions.extensions import GraphMachine

from utils import send_text_message

from utils import send_text_message, send_IP12_carousel, send_fsm, send_go_to_menu_button



class TocMachine(GraphMachine):
    def __init__(self):
        self.machine = GraphMachine(
            model=self,
            **{
                "states" : [
                    'start',
                    'Menu',
                    'Apple',
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
                    {
                        'trigger': 'advance',
                        'source': 'Menu',
                        'dest': 'IP12',
                        'conditions': 'is_going_to_IP12'
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
                        'dest': 'IP12',
                        'conditions': 'is_going_to_IP12'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'fsm',
                        'dest': 'menu',
                        'conditions': 'is_going_to_menu'
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
    
    def is_going_to_Apple(self, event):
        text = event.message.text
        return "Apple" in text 

    def is_going_to_IP12(self, event):
        text = event.message.text
        return "Iphone 12 Menu" in text 
    
    def is_going_to_IP12_Price(self, event):
        text = event.message.text
        return "Iphone 12 Price" in text 

    def is_going_to_IP12_Specs(self, event):
        text = event.message.text
        return "Iphone 12 Specs" in text 

    def is_going_to_IP12_Pros_Cons(self, event):
        text = event.message.text
        return "Iphone 12 Pros and Cons" in text 

    def is_going_to_IP12_Benchmark_Score(self, event):
        text = event.message.text
        return "Iphone 12 Benchmark Score" in text 

    def is_going_to_fsm(self, event):
        text = event.message.text
        return "fsm" in str(text).lower()


    #on enter
    def on_enter_Menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        #send_text_message(reply_token, text)
        #send_go_to_menu_button(reply_token)
        send_IP12_carousel(reply_token)


    def on_enter_Apple(self, event):
        print("I'm entering Apple")
        reply_token = event.reply_token
        text = "Please choose an Apple smartphone that you want to know about!"
        send_text_message(reply_token, text)

    def on_enter_IP12(self, event):
        print("I'm entering Iphone 12")
        reply_token = event.reply_token
        text = "Please choose which information you want to know!"
        send_IP12_carousel(reply_token)

    def on_enter_IP12_Price(self, event):
        print("I'm entering Iphone 12's price")
        reply_token = event.reply_token
        text = "The Price of Iphone 12 is $1,129.00"
        send_text_message(reply_token, text)

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

        text = x
        send_text_message(reply_token, text)

    def on_enter_IP12_Pros_Cons(self, event):
        print("I'm entering Iphone 12's pros and cons")
        reply_token = event.reply_token
        myTuple = (
        "Pros",
        "Attractive design with exquisite fit and premium finish",
        "Excellent OLED screen, very bright",
        "Loud stereo speakers, superb audio quality",
        "The fastest smartphone chip on the planet, 5G, too",
        "Good photo quality across the board, day and night",
        "LiDAR Scanner has varied applications and use cases (albeit quite niche)",
        "Consistently good video quality",
        "Apple iOS 14 is fast and easy to use, 5 years of guaranteed major updates",
        "MagSafe is a promising accessory concept"
        )

        x = "\n\n".join(myTuple)
        
        text = x
        send_text_message(reply_token, text)

    def on_enter_IP12_Benchmark_Score(self, event):
        print("I'm entering Iphone 12's price")
        reply_token = event.reply_token
        text = "The Antutu Benchmark score of Iphone 12 is 598,478."
        send_text_message(reply_token, text) 

    def on_enter_fsm(self, event):
        print("I'm entering fsm")
        reply_token = event.reply_token
        send_fsm(reply_token)