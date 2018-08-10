from wxpy import *
import time


bot = Bot(cache_path=True)

# embed()

friend = bot.friends().search('东东')[0]

tuling = Tuling(api_key='be6f59e3f5fa43fdb145157b78f589d6')

@bot.register(friend)
def reply_friend(msg):
    print(msg)
    tuling.do_reply(msg)


# for i in range(0,100):
#     # friend.send('boom ' + str(i))
#     friend.send_image('my_picture.jpg')
#     time.sleep(1)


# @bot.register()
# def print_messages(msg):
#     print(msg)

# 堵塞线程，并进入 Python 命令行
embed()

