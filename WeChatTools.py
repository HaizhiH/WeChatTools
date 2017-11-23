import itchat

itchat.auto_login()

boy, girl = 0,0

selfName = itchat.search_friends().UserName

noNameList = []

for user in itchat.get_friends():
    if user.UserName == selfName:
        continue
    if user.Sex == 1:
        boy = boy + 1
    elif user.Sex == 2:
        girl = girl + 1
    else:
	noNameList.append( (user.NickName + '(') + ('NoRemarkName' if user.RemarkName=='' else user.RemarkName) + ')')

itchat.send('Hi , There have ' + str(boy) + ' boys and ' + str(girl) + ' girls in your wechat contacts list , bye ~', 'filehelper')

if len(noNameList) != 0:
    noNameStr = ''
    for userName in noNameList:
        noNameStr = noNameStr + userName + '\n'

    itchat.send('The name in the below list(' + str(len(noNameList)) + ') has no sex , they are :\n'+noNameStr, 'filehelper')

itchat.logout()
