# -*- encoding: utf-8 -*-
import telebot, os
from random import randint

noldir = os.path.dirname(os.path.realpath(__file__))+"/"
exec(open(noldir+"phrases.py").read())

isNoolevaya = False

TOKEN = "151474657:AAEBDn1ZqfeGHVna-2FwG1kh6VjORBhNRJA"
bot = telebot.TeleBot(TOKEN)

#Для комманд существует подобный декоратор:
#	@bot.message_handler(commands=["cmdname", "cmdname2"])
#	def function()...
#В чате вызывается методом ввода в чат /cmdname и "/cmdname2"
#Кроме commands есть ещё regexp - регулярные выражения, content_types - типы получаемых ботом данных

#---------------------------------------------------------------------------------------------------------------
#В одной функции можно проверить множество слов сразу - типа find(message, "test", "huets", "ebi ovec")
def findOR(msg, *args): 
	for word in args:
		if word.lower() in msg.lower():
			return True
	return False

def findAND(msg, *args): 
	x = []
	for word in args:
		x.append(word.lower() in msg.lower())

	return not (False in x)

def check(msg, arg):
	return msg.lower() == arg.lower()

#Время и дата в логе
from time import gmtime, strftime
def logging(msg, froms=""):
	froms = "" if froms == "" else froms+": "
	print(strftime("[%d.%m.%Y %H:%M:%S]", gmtime()) + " >>> {0}{1}".format(froms, msg))


@bot.message_handler(content_types=["text"]) #Декоратор на вызов текста
def answer(message): #message в данном случае - это входящее сообщение
	global isNoolevaya, mudak

	msg, ids, usr = message.text, message.chat.id, message.from_user.username
	logging(msg, usr) # Функция на вывод лога сообщения. Без аргумента usr выведет обычный текст из переменной msg

	#здесь должно быть условие выхода нулевой - обнуление переменной isNoolevaya

	if isNoolevaya or findOR(msg, "нулевая"):
		isNoolevaya = True	
		botmsg = ""

		# Код ниже вызывает рандомную фразу из таблицы blyad
		# Здесь: randint - функция рандома, 0 - начало диапазона, len(blyad)-1 - конец диапазона. print - тупо вывод, blyad[number] - number элемент таблицы blyad
		#print(blyad[randint(0, len(blyad)-1)])


		#Начало - проверит на введенность условия включения
		if findOR(msg, "нулевая"):
			botmsg = (hey[randint(0, len(hey)-1)])

		#Здесь пишешь условия, botmsg - переменная, отвечающая за выводимое сообщение
		if check(msg, "Принеси кофе"):
			botmsg = "Идите на хуй."
		
		elif findOR(msg, "люблю", "обожаю"):
			botmsg = "Вы что, ёбаный извращенец?"
		
		if findAND(msg, "кто") and findOR(msg, "ты"):
			botmsg = "Я — часть EasyLua и создательница мира. А еще я матерюсь.\nВы мудак?"
			mudak = True

		elif findOR(msg, "да", "конечно", "естественно") or check(msg, "да"):
			if mudak:
				botmsg = "Да, я знала! Здравствуйте, мудак."
				mudak = False

		elif findOR(msg, "нет", "не знаю", "возможно", "нит") or check(msg, "нет"):
			if mudak:
				botmsg = "Что? Не надо врать мне, вы — мудак и это не обсуждается."
				mudak = False

		elif findOR(msg, "привет", "хело", "хай", "здравствуй"):
				botmsg = "Здравствуйте, "+message.from_user.first_name+"! Как дела?."

		elif findOR(msg, "что", "как") and findOR(msg, "считаешь", "считаете", "думаешь", "думаете" "кажется"):
				botmsg = "Я думаю, что это — полная хуйня."

		#Условие вывода сообщения
		if botmsg != "":
			bot.send_message(ids, botmsg)
			logging(botmsg, "Noolevaya")


#Эту ебалу лучше не чванькать
if __name__ == "__main__":
	bot.polling(none_stop=True) #Непрерывный бот

