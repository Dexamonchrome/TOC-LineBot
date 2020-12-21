from transitions.extensions import GraphMachine

from utils import send_text_message

from utils import send_text_message, send_IP12_carousel, send_fsm, send_go_to_menu_button,send_Apple_carousel, send_Menu_carousel, send_info, send_IP12_Pro_carousel, send_IP12_Mini_carousel



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
    
    #Apple
    def is_going_to_Apple(self, event):
        text = event.message.text
        return "Apple" in text 
    
    # Iphone 12
    def is_going_to_IP12(self, event):
        text = event.message.text
        return "Iphone 12" == text
    
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

    def go_back_to_IP12(self, event):
        text = event.message.text
        return "Iphone 12" == text
    
    # Iphone 12 Pro
    def is_going_to_IP12_Pro(self, event):
        text = event.message.text
        return "Iphone 12 Pro" == text
    
    def is_going_to_IP12_Pro_Price(self, event):
        text = event.message.text
        return "Iphone 12 Pro Price" in text 

    def is_going_to_IP12_Pro_Specs(self, event):
        text = event.message.text
        return "Iphone 12 Pro Specs" in text 

    def is_going_to_IP12_Pro_Pros_Cons(self, event):
        text = event.message.text
        return "Iphone 12 Pro Pros and Cons" in text 

    def is_going_to_IP12_Pro_Benchmark_Score(self, event):
        text = event.message.text
        return "Iphone 12 Pro Benchmark Score" in text 

    def go_back_to_IP12_Pro(self, event):
        text = event.message.text
        return "Iphone 12 Pro" == text

    # Iphone 12 Mini
    def is_going_to_IP12_Mini(self, event):
        text = event.message.text
        return "Iphone 12 Mini" == text
    def is_going_to_IP12_Mini_Price(self, event):
        text = event.message.text
        return "Iphone 12 Mini Price" in text 

    def is_going_to_IP12_Mini_Specs(self, event):
        text = event.message.text
        return "Iphone 12 Mini Specs" in text 

    def is_going_to_IP12_Mini_Pros_Cons(self, event):
        text = event.message.text
        return "Iphone 12 Mini Pros and Cons" in text 

    def is_going_to_IP12_Mini_Benchmark_Score(self, event):
        text = event.message.text
        return "Iphone 12 Mini Benchmark Score" in text 

    def go_back_to_IP12_Mini(self, event):
        text = event.message.text
        return "Iphone 12 Mini" == text

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
        send_info(reply_token, word, information, current)

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
        send_info(reply_token, word, information, current)

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
        send_info(reply_token, word, information, current)

    def on_enter_IP12_Benchmark_Score(self, event):
        print("I'm entering Iphone 12's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Iphone 12 is 598,478."
        word = "Benchmark Score"
        information = x
        current = "Iphone 12"
        send_info(reply_token, word, information, current) 
    
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
        information = "The Price of Iphone 12 Pro is\n 128GB: NTD 33900.00\n 256GB: NTD 37400.00\n, 512GB: NTD 44000.00"
        current = "Iphone 12 Pro"
        send_info(reply_token, word, information, current)

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
        send_info(reply_token, word, information, current)

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
        send_info(reply_token, word, information, current)

    def on_enter_IP12_Pro_Benchmark_Score(self, event):
        print("I'm entering Iphone 12 Pro's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Iphone 12 Pro is 599059."
        word = "Benchmark Score"
        information = x
        current = "Iphone 12 Pro"
        send_info(reply_token, word, information, current) 
    
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
        send_info(reply_token, word, information, current)

    def on_enter_IP12_Specs(self, event):
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
        send_info(reply_token, word, information, current)

    def on_enter_IP12_Pros_Cons(self, event):
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
        send_info(reply_token, word, information, current)

    def on_enter_IP12_Benchmark_Score(self, event):
        print("I'm entering Iphone 12 Mini's Benchmark Score")
        reply_token = event.reply_token
        x = "The Antutu Benchmark score of Iphone 12 Mini is 614169."
        word = "Benchmark Score"
        information = x
        current = "Iphone 12 Mini"
        send_info(reply_token, word, information, current) 

    def on_enter_fsm(self, event):
        print("I'm entering fsm")
        reply_token = event.reply_token
        send_fsm(reply_token)