#pylint:disable=E0602
from arsein import Messenger

bot = Messenger("")


##
target = bot.getInfoByUsername("SYkuoma")["data"]["user"]["user_guid"]
print(target)
bot.sendMessage(target,"بات فعال شد")


#
list_message_seened =[]
userlisr = []
userq = []
listblo = []
while True:
	try:
		chat = bot.getChatsUpdate()
		
		if chat != []:
			for chat in chat:
				access = chat['access']
				admins = target
				m_id = chat['object_guid'] + chat['last_message']['message_id']
				
				if not m_id in list_message_seened and chat['object_guid'] in admins:
					text:str = chat['last_message']['text']
					print("text >>>>> ["+text+"]")
					if text.startswith("id"):
						id = text.split("\n")
						lir = id[1:]
						for id in lir:
							userlisr.append(id)
						print(userlisr)
					if text.startswith("mtn "):
						matn = text[4:]
						bot.sendMessage(target,"متن دریافت شد")
						print(matn)
					
						
					elif text.startswith("sand"):
						matn = matn
						print(matn)
						guid = bot.getChats()
						for guid in guid:
							group = guid["abs_object"]
							if group["type"] == "User":
								userq.append(group["object_guid"])
		
							else:
								pass
						for user in userq:
							print(user)
							if user in listblo:
								pass
							else:
								bot.sendMessage(user,matn)
								listblo.append(user)
								print(listblo)
						bot.sendMessage(target,f"تعداد پیام های ارسال شده >> [{len(userq)}]")
						group = group
					elif text.startswith("send"):
						matn = matn
						for user in userlisr:
							user = bot.getInfoByUsername(user)["data"]["user"]["user_guid"]
							bot.sendMessage(user,matn)
						bot.sendMessage(target,f"تعداد  ارسال شده >> [{len(userlisr)}]")
				list_message_seened.append(m_id)
	except:
		pass