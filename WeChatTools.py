import itchat

itchat.auto_login()

boy, girl = 0,0

for user in itchat.get_friends():
    if user.Sex == 1:
        boy = boy + 1
    else:
        girl = girl + 1

itchat.send('Hi , There have ' + str(boy) + ' boys and ' + str(girl) + ' girls in your wechat contacts list , bye ~', 'filehelper')

itchat.logout()
