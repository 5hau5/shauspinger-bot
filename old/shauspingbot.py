import discord
import re 
import google_currency as google_currency
import json
import random
import re

import asyncio


#kick saadh comand
#dry meat marzin
n=31
print (not re.match(r'^.?$|^(..+?)\1+$', '1'*n))

async def handle_currency_convertion_command(message):

    current_message = message.content.lower().lstrip('//').split()
    print(current_message)
    if len(current_message) == 4:
        _from = current_message[1].upper()
        _to = current_message[2].upper()

        if _from.upper() not in google_currency.CODES: #rethink logic yes
            print (_from, 'doesnt exist')
            await message.channel.send(f"{_from} is not a valid country code")
            return
        if _to.upper() not in google_currency.CODES:
            print (_to, 'doesnt exist')
            await message.channel.send(f"{_to} is not a valid country code")
            return
        
        if _from == _to:
            await message.channel.send("yea right")
            return

        while True:
            try:
                amount = float(current_message[3])
                if  not (0.00000001 < amount < 999999999999999):
                    await message.channel.send("fuc off")
                    break
                else:
                    conversion = json.loads(google_currency.convert(_from, _to, amount))
                    if conversion['converted'] == True:
                        print(conversion['amount'])
                        await message.channel.send(f"{conversion['amount']} {_to.upper()}")
                break  
            except ValueError: 
                print("type a proper number")
                await message.channel.send(f'yes {current_message[3]} is definetly a number')
                await message.channel.send('https://cdn.discordapp.com/attachments/738831293864738975/1230621225022259270/kys.gif?ex=6633fc53&is=66218753&hm=69cd313943e1ae487e4d5176a33a1dd6c67e4660b7a319cab87c0784f2979532&')
                await message.channel.send('```//c from to amount```')
                break 
            except KeyError:
                print("Conversion data error: Converted key not found.")
                await message.channel.send('how')
                break 
    else:
        await message.channel.send('try like')
        await message.channel.send('```//c usd mvr 12```')
        return

async def handle_help_command(message):
    await message.channel.send('```//help  #lists available commands \n//c from to amount  #convert currency \n//pfp #my profile pic origin```')
    return

async def handle_profilepic_command(message):
     await message.channel.send('https://media.discordapp.net/attachments/738831293864738975/1230642032523870319/hoshino_pre_deth.png?ex=66340fb4&is=66219ab4&hm=805b6b869d18177e9b7a026a40b6152258bbfd2f80b697f36e872af07113fa7c&=&format=webp&quality=lossless&width=479&height=479 \nhttps://media.discordapp.net/attachments/738831293864738975/1230642045584933024/hoshino_deth.png?ex=66340fb7&is=66219ab7&hm=332c263568fe00eaa30b643196564b03253f960aa480f053c70076ea36542720&=&format=webp&quality=lossless&width=385&height=385')
     await message.channel.send('https://www.pixiv.net/en/users/95890407')
    #https://www.pixiv.net/en/users/95890407  https://www.pixiv.net/en/artworks/111099494

async def handle_huntshowdown_loadout_randomizer_command(message):

    async def generate_loadout(message):

        weapons = {
            None: {'price': 0},
            'Romero 77': {
                'slot_type': 'large',
                'type': ('shotgun',),
                'ammo_types': {'default_shotgun': 0, 'dragon_breath': 10, 'penny_shot': 5, 'slug': 65, 'starshell': 5},
                'ammo_types_2': {'default_shotgun': 0, 'dragon_breath': 10, 'penny_shot': 5, 'slug': 65, 'starshell': 5},
                'ammo_slot': 2,
                'melee': (False, 'blunt'),
                'levering': False,
                'fanning': False,
                'dual': False,
                'price': 66},
            'Romero 77 Talon': {
                'slot_type': 'large',
                'type': ('shotgun', 'melee'),
                'ammo_types': {'default_shotgun': 0, 'dragon_breath': 10, 'penny_shot': 5, 'slug': 65, 'starshell': 5},
                'ammo_types_2': {'default_shotgun': 0, 'dragon_breath': 10, 'penny_shot': 5, 'slug': 65, 'starshell': 5},
                'ammo_slot': 2,
                'melee': (True, 'rending', 'blunt'),
                'levering': False,
                'fanning': False,
                'dual': False,
                'price': 84},
            'Winfield M1873C': {
                'slot_type': 'large',
                'type': ('small_ammo',),
                'ammo_types': {'default_small_ammo': 0, 'dumdum_small_ammo': 50, 'full_metal_jacket_small_ammo': 50},
                'ammo_types_2': None,
                'ammo_slot': 1,
                'melee': (False, 'blunt'),
                'levering': True,
                'fanning': False,
                'dual': False,
                'price': 41}, 
            'Romero 77 Handcannon': {
                'slot_type': 'medium',
                'type': ('shotgun',),
                'ammo_types': {'default_shotgun': 0, 'dragon_breath': 10, 'penny_shot': 5, 'slug': 65, 'starshell': 5},
                'ammo_types_2': {'default_shotgun': 0, 'dragon_breath': 10, 'penny_shot': 5, 'slug': 65, 'starshell': 5},
                'ammo_slot': 2,
                'melee': (False, 'blunt'),
                'levering': False,
                'fanning': False,
                'dual': False,
                'price': 46},
            'Romero 77 Hatchet': {
                'slot_type': 'medium',
                'type': ('shotgun', 'melee'),
                'ammo_types': {'default_shotgun': 0, 'dragon_breath': 10, 'penny_shot': 5, 'slug': 65, 'starshell': 5},
                'ammo_types_2': {'default_shotgun': 0, 'dragon_breath': 10, 'penny_shot': 5, 'slug': 65, 'starshell': 5},
                'ammo_slot': 2,
                'melee': (True, 'rending'),
                'levering': False,
                'fanning': False,
                'dual': False,
                'price': 82},
            'Caldwell Rival 78 Handcannon': {
                'slot_type': 'medium',
                'type': ('shotgun',),
                'ammo_types': {'default_shotgun': 0, 'dragon_breath': 20, 'penny_shot': 10, 'slug': 130, 'flachette': 40},
                'ammo_types_2': None,
                'ammo_slot': 1,
                'melee': (False, 'blunt'),
                'levering': False,
                'fanning': False,
                'dual': False,
                'price': 125},
            'Nagant M1895': {
                'slot_type': 'small',
                'type': ('small_ammo',),
                'ammo_types': {'default_small_ammo': 0, 'dumdum_small_ammo': 50, 'poison_small_ammo': 50, 'high_velocity_small_ammo': 60},
                'ammo_types_2': None,
                'ammo_slot': 1,
                'melee': (False, 'blunt'),
                'levering': False,
                'fanning': True,
                'dual': False,
                'price': 24},
            'Nagant M1895 Silencer': {
                'slot_type': 'small',
                'type': ('small_ammo',),
                'ammo_types': {'default_small_ammo': 0, 'dumdum_small_ammo': 50, 'poison_small_ammo': 50, 'high_velocity_small_ammo': 60},
                'ammo_types_2': None,
                'ammo_slot': 1,
                'melee': (False, 'blunt'),
                'levering': False,
                'fanning': True,
                'dual': False,
                'price': 93},
            'Nagant M1895 Officer': {
                'slot_type': 'small',
                'type': ('small_ammo',),
                'ammo_types': {'default_small_ammo': 0, 'dumdum_small_ammo': 50, 'poison_small_ammo': 50, 'high_velocity_small_ammo': 60},
                'ammo_types_2': None,
                'ammo_slot': 1,
                'melee': (False, 'blunt'),
                'levering': False,
                'fanning': True,
                'dual': False,
                'price': 96},
        }

        tools = {
            None: {'price': 0},
            'Electric Lamp': {'type': 'idk', 'price': 5},
            'Decoys': {'type': 'idk', 'price': 6},
            'Spyglass': {'type': 'idk', 'price': 8},
            'Fuses': {'type': 'idk', 'price': 10},
            'Choke Bombs': {'type': 'idk', 'price': 25},
            'Alert Trip Mines': {'type': 'idk', 'price': 30},
            'Dusters': {'type': 'melee', 'price': 30},
            'Knuckle Knife': {'type': 'melee', 'price': 50},
            'Heavy Knife': {'type': 'melee', 'price': 20},
            'Knife': {'type': 'melee', 'price': 40},
            'Decoy Fuses': {'type': 'idk', 'price': 30},
            'Medkit': {'type': 'medkit', 'price': 15},
        }

        consumables = {
            None:{'price': 0},
            'Chaos Bomb': {'type': 'idk', 'price': 15},
            'Dynamite Stick': {'type': 'idk', 'price': 18},
            'Vitality Shot (Weak)': {'type': 'drug3', 'price': 20},
            'Choke Beetle': {'type': 'idk', 'price': 22},
            'Waxed Dynamite Stick': {'type': 'idk', 'price': 24},
            'Flash Bomb': {'type': 'idk', 'price': 25},
            'Poison Bomb': {'type': 'idk', 'price': 25},
            'Stamina Shot (Weak)': {'type': 'drug2', 'price': 30},
            'Regen Shot (Weak)': {'type': 'drug1', 'price': 30},
            'Antidote Shot (Weak)': {'type': 'drug4', 'price': 30},
            'Medkit': {'type': 'medkit', 'price': 15}, #chec
        }

        if str(message.author.id) == '320440994241708032':
            weapons = await deminoil(weapons)

        tags, lowest_price, highest_price = await parse_input(message)

        if not tags['default']:
            weapons, tools, consumables = await filter_weapons_tools_consumables(weapons, tools, consumables, tags, lowest_price, highest_price)


        c = 0
        limit = True
        while True:
            c+=1
            loadout = {
                    'slot_1': await select_weapon(weapons, False),
                    'slot_2': await select_weapon(weapons, True),
                    'tools': await select_tools(tools, highest_price),
                    'consumables': await select_consumables(consumables, tags, highest_price),
                    'total_price': 0
                }
            
            loadout['total_price'] = await calculate_total_price(loadout)
            
            print(loadout['total_price'])

            #print(loadout)

            if await check_constraints(loadout, tags, highest_price, lowest_price):
                print(f"rolls: {c}")
                return loadout
            
            if limit:
                if c > 1000000:
                    await message.channel.send('naah too much')
                    break

        
    async def parse_input(message):
        tags_dict = {
            'default':True,
            'tr': False,
            'qm': False,
            '-qm': False,
            'fan': False,
            '-fan': False,
            'lev': False,
            '-lev': False,
            'drug': False,
            '-drug': False,
            'melee': True,
            '-melee': False,
            'medkit': True,
            '-medkit': False,
        }
        
        lowest_price = 0
        highest_price = 9000

        current_message = [item.strip() for item in message.content.lower().lstrip('//lr').split(',')]

        if None not in current_message:
            tags_dict['default'] = False

        unrecognised_tags = []

        valid_price_re = re.compile(r'^(>\d+|<\d+|\d+>|<)$')

        for tag in current_message:
            if tag in tags_dict:
                if tag.startswith('-'):
                    tags_dict[tag] = True
                    tags_dict[tag[1:]] = False
                else:
                    tags_dict[tag] = True
                    tags_dict['-' + tag] = False     
            elif valid_price_re.match(tag):
                if tag.startswith('>') or tag.endswith('<'):
                    lowest_price = max(int(tag.lstrip('>').rstrip('<')), lowest_price)
                elif tag.startswith('<') or tag.endswith('>'):
                    highest_price = min(int(tag.lstrip('<').rstrip('>')), highest_price)
            else:
                unrecognised_tags.append(tag.strip())
        
        if tags_dict['tr']:
            for key in tags_dict:
                if key != 'tr':
                    tags_dict[key] = False

        print("Unrecognized tags:", unrecognised_tags)
        print(tags_dict)
        print("Lowest price:", lowest_price)
        print("Highest price:", highest_price)

        if unrecognised_tags and unrecognised_tags != ['']:
            await message.channel.send(f"idk wat``` {unrecognised_tags}```")

        return tags_dict, lowest_price, highest_price

    async def filter_weapons_tools_consumables(weapons, tools, consumables, tags, lowest_price, highest_price):

        filtered_weapons = weapons
        filtered_tools = tools
        filtered_consumables = consumables

        filtered_weapons = {k: v for k, v in weapons.items() if
                        (not tags['qm'] or v.get('slot_type') != 'small') and
                        (not tags['-fan'] or not v.get('fanning')) and
                        (not tags['-lev'] or not v.get('levering')) and
                        (not tags['-melee'] or not v.get('melee',[False][0])) and
                        (lowest_price - 2098) <= v.get('price', 0) <= highest_price}
        
        for weapon, details in filtered_weapons.items():
            if weapon is None:
                continue

            for ammo_set in ['ammo_types', 'ammo_types_2']:
                ammo_types = details.get(ammo_set)
                if ammo_types is not None:
                    for ammo_type, price in list(ammo_types.items()):
                        if price is not None and details['price'] + price > highest_price:
                            filtered_weapons[weapon][ammo_set].pop(ammo_type)
                            #print(ammo_type)

        filtered_tools = {k: v for k, v in tools.items() if
                        (not tags['-melee'] or v.get('type') != 'melee') and
                        (not tags['-medkit'] or v.get('type') != 'medkit')and
                        (lowest_price - 2098) <= v.get('price', 0) <= highest_price}

        filtered_consumables = {k: v for k, v in consumables.items() if
                                not tags['-drug'] or v.get('type') != 'drug'and
                        (lowest_price - 2098) <= v.get('price', 0) <= highest_price}
        
        print (filtered_weapons)

        
        return filtered_weapons, filtered_tools, filtered_consumables

    async def select_weapon(weapons, slot_1_chosen):

        if slot_1_chosen:
            weapons = {k: v for k, v in weapons.items() if v.get('slot_type') != 'large'}

        weapon_name = random.choice(list(weapons.keys()))

        weapon_ammo_type = None
        weapon_ammo_type_price = 0
        weapon_ammo_type_2 = None
        weapon_ammo_type_2_price = 0

        if weapon_name is not None:
            weapon_ammo_type = random.choice(list(weapons[weapon_name]['ammo_types'].keys()))
            weapon_ammo_type_price = weapons[weapon_name]['ammo_types'][weapon_ammo_type]
                
            if weapons[weapon_name]['ammo_types_2']:
                weapon_ammo_type_2 = random.choice(list(weapons[weapon_name]['ammo_types_2'].keys()))
                weapon_ammo_type_2_price = weapons[weapon_name]['ammo_types_2'][weapon_ammo_type_2]


        weapon_details = {
            'weapon_name': weapon_name,
            'slot_type': weapons[weapon_name]['slot_type'] if weapon_name else None,
            'weapon_type': weapons[weapon_name]['type'] if weapon_name else None,
            'ammo_type': weapon_ammo_type,
            'ammo_type_2': weapon_ammo_type_2,
            'melee': weapons[weapon_name]['melee'][0] if weapon_name else None,
            'levering': weapons[weapon_name]['levering'] if weapon_name else None,
            'fanning': weapons[weapon_name]['fanning'] if weapon_name else None,
            'total_price': weapons[weapon_name]['price'] + weapon_ammo_type_price + weapon_ammo_type_2_price if weapon_name else 0,
        }

        return weapon_details

    async def select_tools(tools, max_price):
        
        tool_template = {
            'name': None,
            'type': None,
            'price': None,
        }

        available_tools = list(tools.keys())
        selected_tools = set()

        while available_tools:
            tool_slots = {
            'slot_1': tool_template.copy(),
            'slot_2': tool_template.copy(),
            'slot_3': tool_template.copy(),
            'slot_4': tool_template.copy(),
            'total_price': 0,
            }

            for slot in ['slot_1', 'slot_2', 'slot_3', 'slot_4']:
                if not available_tools:
                    break
                tool_name = random.choice(available_tools)
                
                while tool_name in selected_tools and tool_name is not None:
                    tool_name = random.choice(available_tools)
                
                tool_details = tools[tool_name]
                
                tool_slots[slot] = {
                    'name': tool_name,
                    'type': tool_details.get('type', None),
                    'price': tool_details['price'],
                }

                tool_slots['total_price'] += tool_details['price']

                if tool_name is not None:
                    selected_tools.add(tool_name)

            if tool_slots['total_price'] < max_price:
                return tool_slots
        return None

    async def select_consumables(consumables, tags, max_price):
        consumable_rolls = 0
        while True:
            consumable_rolls +=1
            consumables_slots = {
            'slot_1': None,
            'slot_2': None,
            'slot_3': None,
            'slot_4': None,
            'total_price': 0,
            }

            for slot in ['slot_1', 'slot_2', 'slot_3', 'slot_4']:
                chosen_consumable = random.choice(list(consumables.keys()))
                
                if chosen_consumable is not None:
                    consumables_slots[slot] = {
                        'name': chosen_consumable,
                        'type': consumables[chosen_consumable]['type'],
                        'price': consumables[chosen_consumable]['price'],
                    }
                    consumables_slots['total_price'] += consumables[chosen_consumable]['price']
                else:
                    consumables_slots[slot] = {
                        'name': None,
                        'type': None,
                        'price': 0,
                    }
            if consumables_slots['total_price'] <= max_price:
                if tags.get('drug', False):
                    drug1_present = any(
                        consumables_slots[slot] and consumables_slots[slot].get('type') == 'drug1' 
                        for slot in ['slot_1', 'slot_2', 'slot_3', 'slot_4']
                    )
                    drug2_present = any(
                        consumables_slots[slot] and consumables_slots[slot].get('type') == 'drug2' 
                        for slot in ['slot_1', 'slot_2', 'slot_3', 'slot_4']
                    )
                    if drug1_present and drug2_present:
                        print (consumable_rolls)
                        return consumables_slots
                else:
                    print (consumable_rolls)
                    return consumables_slots

    async def calculate_total_price(loadout):
        def get_price(item):
            return item['total_price'] if item and 'total_price' in item and item['total_price'] is not None else 0

        total_price = (
            get_price(loadout['slot_1']) +
            get_price(loadout['slot_2']) +
            get_price(loadout['tools']) +
            get_price(loadout['consumables'])
        )

        return total_price

    async def check_constraints(loadout, tags, highest_price, lowest_price):
        price_within_range = (
           lowest_price < loadout['total_price'] < highest_price
        )
        
        if tags.get('lev', False):
            levering_constraint = (
                loadout.get('slot_1') is not None and loadout['slot_1'].get('levering', False) or
                loadout.get('slot_2') is not None and loadout['slot_2'].get('levering', False)
            )
        else:
            levering_constraint = True
        
        if tags.get('fan', False):
            fanning_constraint = (
                loadout.get('slot_1') is not None and loadout['slot_1'].get('fanning', False) or
                loadout.get('slot_2') is not None and loadout['slot_2'].get('fanning', False)
            )
        else:
            fanning_constraint = True

        
        if tags.get('melee', False):
            melee_constraint = any(
                loadout.get('tools') is not None and
                loadout['tools'].get(slot) is not None and 
                loadout['tools'][slot].get('type') == 'melee' 
                for slot in ['slot_1', 'slot_2', 'slot_3', 'slot_4']
            ) or \
            (loadout.get('slot_1') is not None and loadout['slot_1'].get('melee')) or \
            (loadout.get('slot_2') is not None and loadout['slot_2'].get('melee'))
        else:
            melee_constraint = True

        if tags.get('-qm', False):
            no_qm_constraint = (
                loadout.get('slot_1') is not None and
                loadout.get('slot_2') is not None and
                (
                    (loadout['slot_1'].get('slot_type') == 'large' and loadout['slot_2'].get('slot_type') == 'medium') or
                    (loadout['slot_1'].get('slot_type') == 'medium' and loadout['slot_2'].get('slot_type') == 'large')
                )
            )
        else:
            no_qm_constraint = True

        if tags.get('medkit', False):
            medkit_constraint = any(
                loadout.get('tools') is not None and
                loadout['tools'].get(slot) is not None and 
                loadout['tools'][slot].get('type') == 'medkit' 
                for slot in ['slot_1', 'slot_2', 'slot_3', 'slot_4']
            ) or any(
                loadout.get('consumables') is not None and
                loadout['consumables'].get(slot) is not None and 
                loadout['consumables'][slot].get('type') == 'medkit' 
                for slot in ['slot_1', 'slot_2', 'slot_3', 'slot_4'])
        else:
            medkit_constraint = True
        
 
        return \
            price_within_range \
            and levering_constraint \
            and fanning_constraint \
            and melee_constraint \
            and no_qm_constraint \
            and medkit_constraint

    async def deminoil():
        pass

    async def generate_image():
        pass

    async def print_loadout(loadout):
        await message.channel.send(f'''```
Weapon Slot 1: {loadout['slot_1']['weapon_name']} with {loadout['slot_1']['ammo_type']} and {loadout['slot_1']['ammo_type_2']}
Weapon Slot 2: {loadout['slot_2']['weapon_name']} with {loadout['slot_2']['ammo_type']} and {loadout['slot_2']['ammo_type_2']}
Tools: {loadout['tools']['slot_1']['name']}, {loadout['tools']['slot_2']['name']}, {loadout['tools']['slot_3']['name']}, {loadout['tools']['slot_4']['name']}
Consumables: {loadout['consumables']['slot_1']['name']}, {loadout['consumables']['slot_2']['name']}, {loadout['consumables']['slot_3']['name']}, {loadout['consumables']['slot_4']['name']}
Total Price: {loadout['total_price']}```''')

    generated_loadout = await generate_loadout(message)
    await print_loadout(generated_loadout)

        
command_handlers = {
    'c': handle_currency_convertion_command,  #//c usd mvr 12.99
    'convert': handle_currency_convertion_command, #//convert usd mvr 12.99
    'h': handle_help_command,
    'help': handle_help_command,
    'pfp': handle_profilepic_command,
    'lr' : handle_huntshowdown_loadout_randomizer_command,
    }

class MyClient(discord.Client):  
    def __init__(self, intents, channel_id):
        super().__init__(intents=intents)
        self.channel_id = channel_id
        self.text_input_task = None

    async def on_ready(self):
        print(f'{self.user} is online')
        await self.wait_until_ready()
        
        # Retrieve and store the general channel
        self.general_channel = self.get_channel(self.channel_id)
        if self.general_channel is None:
            print("where channel")
            await self.close()  # Close the bot session if the channel isn't found
            return

        # Start the text-sending loop as a separate async task
        await self.general_channel.send(':3')
        self.text_input_task = asyncio.create_task(self.start_text_input_loop())
        print("rediii")

    async def start_text_input_loop(self):
        while not self.is_closed():
            message = await asyncio.to_thread(input, "enter mesag: ")
            await self.general_channel.send(message)

    async def close(self):
        if self.text_input_task:  # Cancel the text input task if it exists
            self.text_input_task.cancel()
        await super().close()  # Call the superclass's close method to close the session

    async def on_message(self, message):
        role = ''
        guild = message.guild

        if message.author == self.user:
            return
        
        else:
            #role ping
            if (('<@&1221754627419017247>' in message.content) or\
                ('<@&1125004823813685358>' in message.content) or\
                ('<@&1223982339730833448>' in message.content) or\
                ('<@&1088083937722634311>' in message.content) or\
                ('<@&738831293588045889>' in message.content) or\
                ('<@&738831293609148416>' in message.content) or\
                ('<@&1224685430897643520>' in message.content) or\
                ('<@&1224885527598071919>' in message.content)) and not\
                (str(message.author.id) == '457432393146695690'):

                games = re.findall('<@&(.+?)>', message.content)
                msg = re.sub(r"<@&.*>", "", message.content)
                print(msg)
                print(games)
                for game in games:
                    print (game)
                    role = role + ' ' + str(discord.utils.get(guild.roles, id=int(game)))
                    print('role is', role)

                await message.channel.send('<@457432393146695690> '+ role + msg)

            #r6s
            if ('<@&738831293588045889>' in message.content):
                await message.channel.send('https://cdn.discordapp.com/attachments/738831293864738975/1229465125514383421/reac.gif?ex=662fc7a0&is=661d52a0&hm=665f85732c43985759fc8acbdc3a7d3a073abd94350d56d3d8d9d693083cd9cc&')
            
            #sex
            if ('sex' in message.content.lower()) or\
               ('segs' in message.content.lower()) or\
               ('seggs' in message.content.lower()):
                await message.channel.send('https://cdn.discordapp.com/attachments/738831293864738975/1229998157941833758/segs-arona.gif?ex=6631b80d&is=661f430d&hm=08dce8539c48abe0a9ccbefb101cd9309fff33148e35b546facda55cbf4fae2e&')
            
            #r6s
            if ('seeg' in message.content.lower()):
                pass

            if ('<@1224676688521199616>' in message.content):
                await message.channel.send('no')
                await message.channel.send('https://tenor.com/view/blue-archive-amd-hoshino-takanashi-hoshino-dancing-gif-10581432706103341722')

            if ('hunter' in message.content.lower()):
                await message.channel.send('HUNTERR?')
                await message.channel.send('HUNTSHOWDOWN??!!') 
                #await message.channel.send('<@&1125004823813685358> <@457432393146695690>')

            elif ('hunt' in message.content.lower()):
                await message.channel.send('HUNT??')
                await message.channel.send('HUNTSHOWDOWN??!!') 
                #await message.channel.send('<@&1125004823813685358> <@457432393146695690>')

            elif ('huner' in message.content.lower()):
                await message.channel.send('HUNTER??')
                await message.channel.send('HUNTSHOWDOWN??!!') 
                #await message.channel.send('<@&1125004823813685358> <@457432393146695690>')

            elif ('hunder' in message.content.lower()):
                await message.channel.send('HUNTER??')
                await message.channel.send('HUNTSHOWDOWN??!!') 
                #await message.channel.send('<@&1125004823813685358> <@457432393146695690>')
                
            elif ('hund' in message.content.lower()):
                await message.channel.send('HUNT??')
                await message.channel.send('HUNTSHOWDOWN??!!') 
                #await message.channel.send('<@&1125004823813685358> <@457432393146695690>')

            elif ('bounty' in message.content.lower()):
                await message.channel.send('BOUNTY??')
                await message.channel.send('AS IN BOUNTY FROM HUNTSHOWDOWN??!!') 
                #await message.channel.send('<@&1125004823813685358> <@457432393146695690>')



            #command
            if message.content.startswith('//'):             
                command_name = message.content[2:].split()[0].lower()

                if command_name in command_handlers:
                    await command_handlers[command_name](message)
                else:
                    await message.channel.send('idk dat')
                


# Initialize the bot and the text handler
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents, channel_id=738831293864738975)
#text_handler = TextHandler(client, 738831293864738975)
#client.run('')


client.run('') #lsdjbnf;lkjbsdeafb;ljuk

