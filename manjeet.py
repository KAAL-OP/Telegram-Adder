from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import (PeerFloodError, UserNotMutualContactError ,
                                          UserPrivacyRestrictedError, UserChannelsTooMuchError,
                                          UserBotError, InputUserDeactivatedError)
from telethon.tl.functions.channels import InviteToChannelRequest
import time, os, sys, json

wt = (
    '''                                              thanos-op & kaal-op
                                                     Telegram-Member-adding
    '''
)
COLORS = {
    "re": "\u001b[31;1m",
    "gr": "\u001b[32m",
    "ye": "\u001b[33;1m",
}
re = "\u001b[31;1m"
gr = "\u001b[32m"
ye = "\u001b[33;1m"
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
clearType = input('terminal or cmd. (t/c): ').lower()
if clearType == 't':
    clear = lambda:os.system('clear')
elif clearType == 'c':
    clear = lambda:os.system('cls')
else:
    print('Invalid input!!!')
    os.system('pip install requests')
    sys.exit()
    
if sys.version_info[0] < 3:
    telet = lambda :os.system('pip install -U telethon')
elif sys.version_info[0] >= 3:
    telet = lambda :os.system('pip3 install -U telethon')

telet()
time.sleep(1)
clear()

while True:
    clr()
    banner()
    print(lg+'[1] Add New Accounts'+n)
    print(lg+'[2] Filter All Banned Accounts'+n)
    print(lg+'[3] Delete specific accounts'+n)
    print(lg+'[4] add member'+n)
    print(lg+'[5] Update your Software'+n)
    print(lg+'[6] Exit'+n)
    a = int(input('\nEnter Your Choice: '))
     if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{gr} [~] Enter number of accounts to add: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{ye} [~] Enter Phone Number: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{cy} [i] Saved all accounts in vars.txt')
            clr()
            print(f'\n{gr} [*] Logging in from new accounts\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 8088717 , '7d1e0295ee1c2628f1933e9ffd2d8b78')
                c.start(number)
                print(f'{ye}[+] 𝐋𝐨𝐠𝐢𝐧 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮L')
                c.disconnect()
            input(f'\n Press enter to goto main menu...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] There are no accounts! Please add some and retry')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 8088717 , '7d1e0295ee1c2628f1933e9ffd2d8b78')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{blue}[+] {phone} is not banned{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' is banned!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Congrats! No banned accounts')
                input('\nPress enter to goto main menu...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] All banned accounts removed'+n)
                input('\nPress enter to goto main menu...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{ye}[i] Choose an account to delete\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Enter a choice: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Account Deleted{n}')
        input(f'\nPress enter to goto main menu...')
        f.close()
    elif a == 5:
        # thanks to github.com/kaal-op for the snippet below
        print(f'\n{lg}[i] Checking for updates...')
        try:
            # https://raw.githubusercontent.com/kaal0408/Telegram-adder/main/version.txt
            version = requests.get('https://raw.githubusercontent.com/kaal0408/Telegram-adder/main/version.txt')
        except:
            print(f'{r} You are not connected to the internet')
            print(f'{r} Please connect to the internet and retry')
            exit()
        if float(version.text) > 0.9:
            prompt = str(input(f'{lg}[~] Update available[Version {version.text}]. Download?[y/n]: {r}'))
            if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                print(f'{lg}[i] Downloading updates...')
                if os.name == 'nt':
                    os.system('del manjeet.py')
                else:
                    os.system('rm manjeet.py')
                #os.system('del scraper.py')
                os.system('curl -l -O https://raw.githubusercontent.com/kaal0408/Telegram-adder/main/manjeet.py')
                print(f'{gr}[*] Updated to version: {version.text}')
                input('Press enter to exit...')
                exit()
            else:
                print(f'{lg}[!] Update aborted.')
                input('Press enter to goto main menu...')
        else:
            print(f'{lg}[i] You is already up to date')
            input('Press enter to goto main menu...')
    elif a == 6:
        clr()
     

        
        print(ye+'[+] Choose your channel to Add members.')
        a=0
        for i in channel:
            print(gr+'['+str(a)+']', i.title)
            a += 1
        opt1 = int(input(ye+'Enter a number: '))
        my_participants = await client.get_participants(channel[opt1])
        target_group_entity = InputPeerChannel(channel[opt1].id, channel[opt1].access_hash)
        my_participants_id = []
        for my_participant in my_participants:
            my_participants_id.append(my_participant.id)
        with open('manjeet_members.txt', 'r') as r:
            users = json.load(r)
        count = 1
        i = 0
        for user in users:
            if count%50 == 0:
                clear()
                print(colorText(wt))
                print('')
                print('')
                print(ye+"please wait for 1 minute...")
                time.sleep(60)
            elif count >= 300:
                await client.disconnect()
                break
            elif i >= 8:
                await client.disconnect()
                break
            count+=1
            time.sleep(1)
            if user['uid'] in my_participants_id:
                print(gr+'User present. Skipping.')
                continue
            else:
                try:
                    user_to_add = InputPeerUser(user['uid'], user['access_hash'])
                    add = await client(InviteToChannelRequest(target_group_entity,[user_to_add]))
                    print(gr+'Added ', str(user['uid']))
                    
                except PeerFloodError:
                    print(re+"Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                    i += 1
                except UserPrivacyRestrictedError:
                    print(re+"The user's privacy settings do not allow you to do this. Skipping.")
                    i = 0
                except UserBotError:
                    print(re+"Can't add Bot. Skipping.")
                    i = 0
                except InputUserDeactivatedError:
                    print(re+"The specified user was deleted. Skipping.")
                    i = 0
                except UserChannelsTooMuchError:
                    print(re+"User in too much channel. Skipping.")
                except UserNotMutualContactError:
                    print(re+'Mutual No. Skipped.')
                    i = 0
                except Exception as e:
                    print(re+"Error:", e)
                    print("Trying to continue...")
                    i += 1
                    continue
    
    print(colorText(wt))
    chats = []
    channel = []
    result = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=200,
        hash=0
    ))
    chats.extend(result.chats)
    for a in chats:
        try:
            if True:
                channel.append(a)
        except:
            continue

    a = 0
    print('')
    print('')
    print(ye+'Choose a group to scrape.')
    for i in channel:
        print(gr+'['+str(a)+']', i.title)
        a += 1
    op = input(ye+'Enter a number (or press ENTER to skip): ')
    if op == '':
        print(ye+'Ok. skipping...')
        time.sleep(1)
        await getmem()
        sys.exit()
    else: 
        pass
    opt = int(op)
    print('')
    print(ye+'[+] Fetching Members...')
    time.sleep(1)
    target_group = channel[opt]
    all_participants = []
    mem_details = []
    all_participants = await client.get_participants(target_group)
    for user in all_participants:
        try:
            if user.username:
                username = user.username
            else:
                username = ""
            if user.first_name:
                firstname = user.first_name
            else:
                firstname = ""
            if user.last_name:
                lastname = user.last_name
            else:
                lastname = ""

            new_mem = {
                'uid': user.id,
                'username': username,
                'firstname': firstname,
                'lastname': lastname,
                'access_hash': user.access_hash
            }
            mem_details.append(new_mem)
        except ValueError:
            continue
    
    with open('erfan4lx_members.txt', 'w') as w:
        json.dump(mem_details, w)
    time.sleep(1)
    print(ye+'Please wait.....')
    time.sleep(3)
    done = input(gr+'[+] Members scraped successfully. (Press enter to Add members)')
    await getmem()

    await client.disconnect()

with client:
    client.loop.run_until_complete(main())
