import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class LuaGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Balatro Challenge Generator by HoneySoakedSeagull")

        self.joker_entries = []
        self.card_entries = []
        self.consumable_entries = []
        self.voucher_entries =[]

        # Joker Section
        self.joker_frame = ttk.LabelFrame(self.root, text='Jokers')
        self.joker_frame.pack(padx=5, pady=5, fill='x')

        self.joker_scroll = ttk.Scrollbar(self.joker_frame, orient='vertical')
        self.joker_scroll.pack(side='right', fill='y')

        self.joker_canvas = tk.Canvas(self.joker_frame, yscrollcommand=self.joker_scroll.set, height=100)
        self.joker_canvas.pack(fill='both', expand=True)

        self.joker_scroll.config(command=self.joker_canvas.yview)

        self.joker_frame_inner = ttk.Frame(self.joker_canvas)
        self.joker_canvas.create_window((0, 0), window=self.joker_frame_inner, anchor='nw')

        self.joker_scroll.bind('<Configure>', lambda e: self.joker_scroll.config(command=self.joker_canvas.yview))
        self.joker_frame_inner.bind('<Configure>', lambda e: self.joker_canvas.config(scrollregion=self.joker_canvas.bbox('all')))

        self.add_joker_btn = ttk.Button(self.joker_frame, text='Add Joker', command=self.add_joker)
        self.add_joker_btn.pack(side='top', padx=5, pady=5)

        # Map Joker Names to Lua Variable Names
        self.joker_mapping = {
			"Joker": "j_joker",
			"Greedy Joker": "j_greedy",
			"Lusty Joker": "j_lusty",
			"Wrathful Joker": "j_wrathful",
			"Gluttonous Joker": "j_gluttonous",
			"Jolly Joker": "j_jolly",
			"Zany Joker": "j_zany",
			"Mad Joker": "j_mad",
			"Crazy Joker": "j_crazy",
			"Droll Joker": "j_droll",
			"Sly Joker": "j_sly",
			"Wily Joker": "j_wily",
			"Clever Joker": "j_clever",
			"Devious Joker": "j_devious",
			"Crafty Joker": "j_crafty",
			"Half Joker": "j_half",
			"Joker Stencil": "j_stencil",
			"Four Fingers": "j_four_fingers",
			"Mime": "j_mime",
			"Credit Card": "j_credit_card",
			"Ceremonial Dagger": "j_ceremonial",
			"Banner": "j_banner",
			"Mystic Summit": "j_mystic_summit",
			"Marble Joker": "j_marble",
			"Loyalty Card": "j_loyalty_card",
			"8 Ball": "j_8_ball",
			"Misprint": "j_misprint",
			"Dusk": "j_dusk",
			"Raised Fist": "j_raised_fist",
			"Chaos the Clown": "j_chaos",
			"Fibonacci": "j_fibonacci",
			"Steel Joker": "j_steel",
			"Scary Face": "j_scary_face",
			"Abstract Joker": "j_abstract",
			"Delayed Gratification": "j_delayed_grat",
			"Hack": "j_hack",
			"Pareidolia": "j_pareidolia",
			"Gros Michel": "j_gros_michel",
			"Even Steven": "j_even_steven",
			"Odd Todd": "j_odd_todd",
			"Scholar": "j_scholar",
			"Business Card": "j_business",
			"Supernova": "j_supernova",
			"Ride the Bus": "j_ride_the_bus",
			"Space Joker": "j_space",
			"Egg": "j_egg",
			"Burglar": "j_burglar",
			"Blackboard": "j_blackboard",
			"Runner": "j_runner",
			"Ice Cream": "j_ice_cream",
			"DNA": "j_dna",
			"Splash": "j_splash",
			"Blue Joker": "j_blue_joker",
			"Sixth Sense": "j_sixth_sense",
			"Constellation": "j_constellation",
			"Hiker": "j_hiker",
			"Faceless Joker": "j_faceless",
			"Green Joker": "j_green_joker",
			"Superposition": "j_superposition",
			"To Do List": "j_todo_list",
			"Cavendish": "j_cavendish",
			"Card Sharp": "j_card_sharp",
			"Red Card": "j_red_card",
			"Madness": "j_madness",
			"Square Joker": "j_square",
			"Séance": "j_seance",
			"Riff-Raff": "j_riff_raff",
			"Vampire": "j_vampire",
			"Shortcut": "j_shortcut",
			"Hologram": "j_hologram",
			"Vagabond": "j_vagabond",
			"Baron": "j_baron",
			"Cloud 9": "j_cloud_9",
			"Rocket": "j_rocket",
			"Obelisk": "j_obelisk",
			"Midas Mask": "j_midas_mask",
			"Luchador": "j_luchador",
			"Photograph": "j_photograph",
			"Gift Card": "j_gift",
			"Turtle Bean": "j_turtle_bean",
			"Erosion": "j_erosion",
			"Reserved Parking": "j_reserved_parking",
			"Mail-In Rebate": "j_mail",
			"To the Moon": "j_to_the_moon",
			"Hallucination": "j_hallucination",
			"Fortune Teller": "j_fortune_teller",
			"Juggler": "j_juggler",
			"Drunkard": "j_drunkard",
			"Stone Joker": "j_stone",
			"Golden Joker": "j_golden",
			"Lucky Cat": "j_lucky_cat",
			"Baseball Card": "j_baseball",
			"Bull": "j_bull",
			"Diet Cola": "j_diet_cola",
			"Trading Card": "j_trading",
			"Flash Card": "j_flash",
			"Popcorn": "j_popcorn",
			"Spare Trousers": "j_trousers",
			"Ancient Joker": "j_ancient",
			"Ramen": "j_ramen",
			"Walkie Talkie": "j_walkie_talkie",
			"Seltzer": "j_seltzer",
			"Castle": "j_castle",
			"Smiley Face": "j_smiley",
			"Campfire": "j_campfire",
			"Golden Ticket": "j_ticket",
			"Mr. Bones": "j_mr_bones",
			"Acrobat": "j_acrobat",
			"Sock and Buskin": "j_sock_and_buskin",
			"Swashbuckler": "j_swashbuckler",
			"Troubadour": "j_troubadour",
			"Certificate": "j_certificate",
			"Smeared Joker": "j_smeared",
			"Throwback": "j_throwback",
			"Hanging Chad": "j_hanging_chad",
			"Rough Gem": "j_rough_gem",
			"Bloodstone": "j_bloodstone",
			"Arrowhead": "j_arrowhead",
			"Onyx Agate": "j_onyx_agate",
			"Glass Joker": "j_glass",
			"Showman": "j_ring_master",
			"Flower Pot": "j_flower_pot",
			"Blueprint": "j_blueprint",
			"Wee Joker": "j_wee",
			"Merry Andy": "j_merry_andy",
			"Oops! All 6s": "j_oops",
			"The Idol": "j_idol",
			"Seeing Double": "j_seeing_double",
			"Matador": "j_matador",
			"Hit the Road": "j_hit_the_road",
			"The Duo": "j_duo",
			"The Trio": "j_trio",
			"The Family": "j_family",
			"The Order": "j_order",
			"The Tribe": "j_tribe",
			"Stuntman": "j_stuntman",
			"Invisible Joker": "j_invisible",
			"Brainstorm": "j_brainstorm",
			"Satellite": "j_satellite",
			"Shoot the Moon": "j_shoot_the_moon",
			"Driver's License": "j_drivers_license",
			"Cartomancer": "j_cartomancer",
			"Astronomer": "j_astronomer",
			"Burnt Joker": "j_burnt",
			"Bootstraps": "j_bootstraps",
			"Canio": "j_caino",
			"Triboulet": "j_triboulet",
			"Yorick": "j_yorick",
			"Chicot": "j_chicot",
			"Perkeo": "j_perkeo",
		}

        # Map Joker Edition Names to Lua Variable Names
        self.joker_edition_mapping = {
            "Base": "base",
            "Foil": "foil",
            "Holographic": "holo",
            "Polychrome": "polychrome",
            "Negative": "negative",
        }

        self.add_joker()  # Add initial joker entry

        # Card Section
        self.card_frame = ttk.LabelFrame(self.root, text='Cards')
        self.card_frame.pack(padx=5, pady=5, fill='x')

        self.card_scroll = ttk.Scrollbar(self.card_frame, orient='vertical')
        self.card_scroll.pack(side='right', fill='y')

        self.card_canvas = tk.Canvas(self.card_frame, yscrollcommand=self.card_scroll.set, height=100)
        self.card_canvas.pack(fill='both', expand=True)

        self.card_scroll.config(command=self.card_canvas.yview)

        self.card_frame_inner = ttk.Frame(self.card_canvas)
        self.card_canvas.create_window((0, 0), window=self.card_frame_inner, anchor='nw')

        self.card_scroll.bind('<Configure>', lambda e: self.card_scroll.config(command=self.card_canvas.yview))
        self.card_frame_inner.bind('<Configure>', lambda e: self.card_canvas.config(scrollregion=self.card_canvas.bbox('all')))

        self.add_card_btn = ttk.Button(self.card_frame, text='Add Card', command=self.add_card)
        self.add_card_btn.pack(side='top', padx=5, pady=5)

        # Map Suit Names to Lua Variable Names
        self.suit_mapping = {
            "Hearts": "H",
            "Diamonds": "D",
            "Spades": "S",
            "Clubs": "C",
        }  

        # Map Rank Names to Lua Variable Names
        self.rank_mapping = {
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "10": "T",
            "Jack": "J",
            "Queen": "Q",
            "King": "K",
            "Ace": "A",
        }  

        # Map Enhancement Names to Lua Variable Names
        self.enhancement_mapping = {
            "None": "",
			"Bonus": "c_bonus",
			"Mult": "m_mult",
            "Wild Card": "m_wild",
            "Glass Card": "m_glass",
            "Steel Card": "m_steel",
            "Stone Card": "m_stone",
            "Gold Card": "m_gold",
            "Lucky Card": "m_lucky",
        }

        # Map Card Edition Names to Lua Variable Names, currently not functional
        self.card_edition_mapping = {
            "Base": "e_base",
            "Foil": "e_foil",
            "Holographic": "e_holo",
            "Polychrome": "e_polychrome",
        }    

        # Map Seal Names to Lua Variable Names
        self.seal_mapping = {
            "None": "",
            "Gold": "Gold",
            "Red": "Red",
            "Blue": "Blue",
            "Purple": "Purple",
        }        

        self.add_card()  # Add initial card entry

        # Consumables Section
        self.consumable_frame = ttk.LabelFrame(self.root, text='Consumables')
        self.consumable_frame.pack(padx=5, pady=5, fill='x')

        self.consumable_scroll = ttk.Scrollbar(self.consumable_frame, orient='vertical')
        self.consumable_scroll.pack(side='right', fill='y')

        self.consumable_canvas = tk.Canvas(self.consumable_frame, yscrollcommand=self.consumable_scroll.set, height=100)
        self.consumable_canvas.pack(fill='both', expand=True)

        self.consumable_scroll.config(command=self.consumable_canvas.yview)

        self.consumable_frame_inner = ttk.Frame(self.consumable_canvas)
        self.consumable_canvas.create_window((0, 0), window=self.consumable_frame_inner, anchor='nw')

        self.consumable_scroll.bind('<Configure>', lambda e: self.consumable_scroll.config(command=self.consumable_canvas.yview))
        self.consumable_frame_inner.bind('<Configure>', lambda e: self.consumable_canvas.config(scrollregion=self.consumable_canvas.bbox('all')))

        self.add_consumable_btn = ttk.Button(self.consumable_frame, text='Add Consumable', command=self.add_consumable)
        self.add_consumable_btn.pack(side='top', padx=5, pady=5)

        self.consumable_mapping = {
        # Tarot Cards
			"The Fool": "c_fool",
			"The Magician": "c_magician",
			"The High Priestess": "c_high_priestess",
			"The Empress": "c_empress",
			"The Emperor": "c_emperor",
			"The Hierophant": "c_heirophant",
			"The Lovers": "c_lovers",
			"The Chariot": "c_chariot",
			"Justice": "c_justice",
			"The Hermit": "c_hermit",
			"The Wheel of Fortune": "c_wheel_of_fortune",
			"Strength": "c_strength",
			"The Hanged Man": "c_hanged_man",
			"Death": "c_death",
			"Temperance": "c_temperance",
			"The Devil": "c_devil",
			"The Tower": "c_tower",
			"The Star": "c_star",
			"The Moon": "c_moon",
			"The Sun": "c_sun",
			"Judgement": "c_judgement",
			"The World": "c_world",

        # Planet Cards
			"Mercury": "c_mercury",
			"Venus": "c_venus",
			"Earth": "c_earth",
			"Mars": "c_mars",
			"Jupiter": "c_jupiter",
			"Saturn": "c_saturn",
			"Uranus": "c_uranus",
			"Neptune": "c_neptune",
			"Pluto": "c_pluto",
			"Planet X": "c_planet_x",
			"Ceres": "c_ceres",
			"Eris": "c_eris",

        # Spectral Cards
			"Familiar": "c_familiar",
			"Grim": "c_grim",
			"Incantation": "c_incantation",
			"Talisman": "c_talisman",
			"Aura": "c_aura",
			"Wraith": "c_wraith",
			"Sigil": "c_sigil",
			"Ouija": "c_ouija",
			"Ectoplasm": "c_ectoplasm",
			"Immolate": "c_immolate",
			"Ankh": "c_ankh",
			"Deja Vu": "c_deja_vu",
			"Hex": "c_hex",
			"Trance": "c_trance",
			"Medium": "c_medium",
			"Cryptid": "c_cryptid",
			"Soul": "c_soul",
			"Black Hole": "c_black_hole",           
        }

        self.add_consumable()  # Add initial consumable entry

        # Voucher Section
        self.voucher_frame = ttk.LabelFrame(self.root, text='Vouchers')
        self.voucher_frame.pack(padx=5, pady=5, fill='x')

        self.voucher_scroll = ttk.Scrollbar(self.voucher_frame, orient='vertical')
        self.voucher_scroll.pack(side='right', fill='y')

        self.voucher_canvas = tk.Canvas(self.voucher_frame, yscrollcommand=self.voucher_scroll.set, height=100)
        self.voucher_canvas.pack(fill='both', expand=True)

        self.voucher_scroll.config(command=self.voucher_canvas.yview)

        self.voucher_frame_inner = ttk.Frame(self.voucher_canvas)
        self.voucher_canvas.create_window((0, 0), window=self.voucher_frame_inner, anchor='nw')

        self.voucher_scroll.bind('<Configure>', lambda e: self.voucher_scroll.config(command=self.voucher_canvas.yview))
        self.voucher_frame_inner.bind('<Configure>', lambda e: self.voucher_canvas.config(scrollregion=self.voucher_canvas.bbox('all')))
        
        # Map Voucher Names to Lua Variable Names
        self.voucher_mapping = {
            "Overstock": ["v_overstock_norm", "v_overstock_plus"],
            "Clearance Sale": ["v_clearance_sale", "v_liquidation"],
            "Hone": ["v_hone", "v_glow_up"],
            "Reroll Surplus": ["v_reroll_surplus", "v_reroll_glut"],
            "Crystal Ball": ["v_crystal_ball", "v_omen_globe"],
            "Telescope": ["v_telescope", "v_observatory"],
            "Grabber": ["v_grabber", "v_nacho_tong"],
            "Wasteful": ["v_wasteful", "v_recyclomancy"],
            "Tarot Merchant": ["v_tarot_merchant", "v_tarot_tycoon"],
            "Planet Merchant": ["v_planet_merchant", "v_planet_tycoon"],
            "Seed Money": ["v_seed_money", "v_money_tree"],
            "Blank": ["v_blank", "v_antimatter"],
            "Magic Trick": ["v_magic_trick", "v_illusion"],
            "Hieroglyph": ["v_hieroglyph", "v_petroglyph"],
            "Directors Cut": ["v_directors_cut", "v_retcon"],
            "Paint Brush": ["v_paint_brush", "v_pallete"]
        }
        
        # Store the BooleanVars for voucher checkbox states
        self.voucher_vars = []

        # Create labels for titles
        for i, title in enumerate(self.voucher_mapping.keys()):
            voucher_label = ttk.Label(self.voucher_frame_inner, text=title)
            voucher_label.grid(row=i, column=0, padx=5, pady=5, sticky='w')

            base_var = tk.BooleanVar()
            upgrade_var = tk.BooleanVar()

            # Add the variables to keep track of them
            self.voucher_vars.append((base_var, upgrade_var, title))
            
            # Callback to manage the Checkbutton interactions
            def update_checkbuttons(*args, base_var=base_var, upgrade_var=upgrade_var):
                if upgrade_var.get():  # If Upgrade is checked
                    base_var.set(True)  # Check Base
                if not base_var.get():  # If Base is unchecked
                    upgrade_var.set(False)  # Uncheck Upgrade

            base_checkbutton = ttk.Checkbutton(self.voucher_frame_inner, variable=base_var, text='Base')
            base_checkbutton.grid(row=i, column=1, padx=5, pady=5, sticky='w')

            upgrade_checkbutton = ttk.Checkbutton(self.voucher_frame_inner, variable=upgrade_var, text='Upgrade')
            upgrade_checkbutton.grid(row=i, column=2, padx=5, pady=5, sticky='w')

            # Trace the base variable to update the upgrade checkbox
            base_var.trace_add('write', update_checkbuttons)
            upgrade_var.trace_add('write', update_checkbuttons)
        
        # Save Button
        self.save_btn = ttk.Button(self.root, text='Save to Lua File', command=self.save_to_file)
        self.save_btn.pack(pady=5)
        

    def add_joker(self):
        entry = JokersEntry(self.joker_frame_inner, self.remove_joker, self.joker_mapping, self.joker_edition_mapping)
        self.joker_entries.append(entry)

    def remove_joker(self, entry):
        entry.destroy()
        self.joker_entries.remove(entry)

    def add_card(self):
        entry = CardsEntry(self.card_frame_inner, self.remove_card, self.suit_mapping, self.rank_mapping, self.enhancement_mapping, self.seal_mapping)
        self.card_entries.append(entry)

    def remove_card(self, entry):
        entry.destroy()
        self.card_entries.remove(entry)

    def add_consumable(self):
        entry = ConsumablesEntry(self.consumable_frame_inner, self.remove_consumable, self.consumable_mapping)
        self.consumable_entries.append(entry)

    def remove_consumable(self, entry):
        entry.destroy()
        self.consumable_entries.remove(entry)

    def save_to_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".lua", filetypes=[("Lua files", "*.lua")])
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write(self.generate_lua_code())
                messagebox.showinfo("Success", "Lua file saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def generate_lua_code(self):
        lua_code = "--- STEAMODDED HEADER\n"
        lua_code += "--- MOD_NAME: Generated Challenge\n"
        lua_code += "--- MOD_ID: GenChal\n"
        lua_code += "--- MOD_AUTHOR: [HoneySoakedSeagull's Challenge Generator]\n"
        lua_code += "--- MOD_DESCRIPTION: A challenge generated with HoneySoakedSeagull's Challenge Generator.\n\n"
        lua_code += "----------------------------------------------\n"
        lua_code += "------------MOD CODE -------------------------\n\n"
        lua_code += "function SMODS.INIT.HSSCGCC ()\n\n"
        lua_code += "   G.localization.misc.challenge_names['c_mod_genchal'] = 'General Challenge'\n"
        lua_code += "   table.insert(G.CHALLENGES,1,{\n"
        lua_code += "       name = 'Custom Generated Challenge',\n"
        lua_code += "       id = 'c_mod_genchal',\n\n"
        lua_code += "       rules = {\n"
        lua_code += "           custom = {\n"
        lua_code += "           },\n"
        lua_code += "           modifiers = {\n"
        lua_code += "           }\n"
        lua_code += "       },\n"
        
        # Generate Joker code
        if self.joker_entries:
            lua_code += "       jokers = {\n"
            for entry in self.joker_entries:
                joker_name = entry.jokerdd.get()
                edition_name = entry.jokereddd.get()
                joker_lua = self.joker_mapping.get(joker_name, joker_name)
                eternal_value = entry.eternal_var.get()
                edition_lua = self.joker_edition_mapping.get(edition_name, edition_name)
                lua_code += f"          {{id = '{joker_lua}', eternal = {str(eternal_value).lower()}, edition = '{edition_lua}'}} ,\n"
            lua_code += "       },\n"

        # Generate Consumable code
        if self.consumable_entries:
            lua_code += "       consumeables = {\n"
            for entry in self.consumable_entries:
                consumable_name = entry.consumabledd.get()
                consumable_lua = self.consumable_mapping.get(consumable_name, consumable_name)
                lua_code += f"          {{id = '{consumable_lua}'}} ,\n"
            lua_code += "       },\n"

        # Generate Voucher code
        if self.voucher_vars:
            lua_code += "       vouchers = {\n"
            for base_var, upgrade_var, title in self.voucher_vars:
                # Only include if either base or upgrade is checked
                if base_var.get() or upgrade_var.get():
                    lua_var_list = self.voucher_mapping[title]
                    if base_var.get():
                        lua_code += f"          {{id = '{lua_var_list[0]}'}} ,\n"
                    if upgrade_var.get():
                        lua_code += f"          {{id = '{lua_var_list[1]}'}} ,\n"
            lua_code += "       },\n"
          
        # Generate Card code
        if self.card_entries:
            lua_code += "       deck = {\n"
            lua_code += "           cards = {"
            for entry in self.card_entries:
                # Get Selected Inputs
                suit_name = entry.suitdd.get()
                rank_name = entry.rankdd.get()
                enhancement_name = entry.enhancementdd.get()
                seal_name = entry.sealdd.get()

                # Get Dictionary Names
                suit_lua = self.suit_mapping.get(suit_name, suit_name)
                rank_lua = self.rank_mapping.get(rank_name, rank_name)
                enhancement_lua = self.enhancement_mapping.get(enhancement_name, enhancement_name)
                seal_lua = self.seal_mapping.get(seal_name, seal_name)

                # Generate Card Code Without Enhancements or Seals
                lua_code += f"{{s='{suit_lua}', r='{rank_lua}'"

                # Add Enhancement code if applicable
                if enhancement_lua:
                    lua_code += f",e='{enhancement_lua}'"

                # Add Seal code if applicable
                if seal_lua:
                    lua_code += f",g='{seal_lua}'"

                lua_code += "},"
            lua_code += "}, \n"
            lua_code += "           type = 'Challenge Deck'\n      },\n"

        # Bottom code
        lua_code += "       restrictions = {\n"    
        lua_code += "           banned_cards = {\n"
        lua_code += "           },\n"
        lua_code += "           banned_tags = {\n"
        lua_code += "           },\n"
        lua_code += "           banned_other = {\n"
        lua_code += "           }\n"
        lua_code += "       }\n"
        lua_code += "   })\n\n"
        lua_code += "end\n\n"
        lua_code += "----------------------------------------------\n"
        lua_code += "------------MOD CODE END----------------------"

        return lua_code


class JokersEntry(ttk.Frame):
    def __init__(self, parent, remove_callback, joker_mapping, joker_edition_mapping):
        super().__init__(parent)
        self.remove_callback = remove_callback
        self.joker_mapping = list(joker_mapping.keys())
        self.joker_edition_mapping = list(joker_edition_mapping.keys())

        # Joker Name Drop Down
        self.jokerdd = ttk.Combobox(self, values=self.joker_mapping, width=20)
        self.jokerdd.grid(row=0, column=0, padx=5, pady=5)
        self.jokerdd.current(0)

        # Joker Edition Drop Down
        self.jokereddd = ttk.Combobox(self, values=self.joker_edition_mapping, width=20)
        self.jokereddd.grid(row=0, column=1, padx=5, pady=5)
        self.jokereddd.current(0)

        # Joker Eternal Checkbox
        self.eternal_var = tk.BooleanVar()
        self.eternal = tk.Checkbutton(self, variable=self.eternal_var)
        self.eternal.grid(row=0, column=2)

        self.remove_btn = ttk.Button(self, text='Remove', command=self.remove)
        self.remove_btn.grid(row=0, column=3, padx=5, pady=5)

        self.pack(fill='x')

    def remove(self):
        self.remove_callback(self)


class CardsEntry(ttk.Frame):
    def __init__(self, parent, remove_callback, suit_mapping, rank_mapping, enhancement_mapping, seal_mapping):
        super().__init__(parent)
        self.remove_callback = remove_callback
        self.suit_mapping = list(suit_mapping.keys())
        self.rank_mapping = list(rank_mapping.keys())
        self.enhancement_mapping = list(enhancement_mapping.keys())
        self.seal_mapping = list(seal_mapping.keys())

        self.suitdd = ttk.Combobox(self, values=self.suit_mapping, width=9)
        self.suitdd.grid(row=0, column=0, padx=5, pady=5)
        self.suitdd.current(0)

        self.rankdd = ttk.Combobox(self, values=self.rank_mapping, width=6)
        self.rankdd.grid(row=0, column=1, padx=5, pady=5)
        self.rankdd.current(0)

        self.enhancementdd = ttk.Combobox(self, values=self.enhancement_mapping, width=10)
        self.enhancementdd.grid(row=0, column=2, padx=5, pady=5)
        self.enhancementdd.current(0)

        self.sealdd = ttk.Combobox(self, values=self.seal_mapping, width=6)
        self.sealdd.grid(row=0, column=3, padx=5, pady=5)
        self.sealdd.current(0)

        self.remove_btn = ttk.Button(self, text='Remove', command=self.remove)
        self.remove_btn.grid(row=0, column=4, padx=5, pady=5)

        self.pack(fill='x')

    def remove(self):
        self.remove_callback(self)

class ConsumablesEntry(ttk.Frame):
    def __init__(self, parent, remove_callback, consumable_mapping):
        super().__init__(parent)
        self.remove_callback = remove_callback
        self.consumable_mapping = list(consumable_mapping.keys())

        self.consumabledd = ttk.Combobox(self, values=self.consumable_mapping, width=20)
        self.consumabledd.grid(row=0, column=0, padx=5, pady=5)
        self.consumabledd.current(0)

        self.remove_btn = ttk.Button(self, text='Remove', command=self.remove)
        self.remove_btn.grid(row=0, column=3, padx=5, pady=5)

        self.pack(fill='x')

    def remove(self):
        self.remove_callback(self)

if __name__ == "__main__":
    root = tk.Tk()
    app = LuaGeneratorApp(root)
    root.mainloop()
