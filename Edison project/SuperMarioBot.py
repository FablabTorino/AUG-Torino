#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

''' This is the Offiacial Bot of AUG Torino Team ''' 

import telegram
import time
import calendar
import datetime
from conversation import *
import pywapi
import string


# Telegram Bot Authorization Token
# SuperMario_bot
bot = telegram.Bot('134502559:AAEitHOxBS0Kz5IdLobu9iD-40OB20gDKwA')
#AUGChatId=str(-22985187)
AUGChatId=str(-26538515)

# This will be our global variable to keep the latest update_id when requesting
# for updates. It starts with the latest update_id if available.
try:
    LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
except IndexError:
    LAST_UPDATE_ID = None


   # custom_keyboard = [[ telegram.Emoji.THUMBS_UP_SIGN,   telegram.Emoji.THUMBS_DOWN_SIGN ]]
   # reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
   # bot.sendMessage(chat_id=chat_id, text="Stay here, I'll be back.", reply_markup=reply_markup)

#----------------------------------------------------------------------
#  eliza.py
#
#  a cheezy little Eliza knock-off by Joe Strout <joe@strout.net>
#  with some updates by Jeff Epler <jepler@inetnebr.com>
#  hacked into a module and updated by Jez Higgins <jez@jezuk.co.uk>
#  last revised: 28 February 2005
#----------------------------------------------------------------------

import string
import re
import random

class eliza:
  def __init__(self):
    self.keys = map(lambda x:re.compile(x[0], re.IGNORECASE),gPats)
    self.values = map(lambda x:x[1],gPats)

  #----------------------------------------------------------------------
  # translate: take a string, replace any words found in dict.keys()
  #  with the corresponding dict.values()
  #----------------------------------------------------------------------
  def translate(self,str,dict):
    words = string.split(string.lower(str))
    keys = dict.keys();
    for i in range(0,len(words)):
      if words[i] in keys:
        words[i] = dict[words[i]]
    return string.join(words)

  #----------------------------------------------------------------------
  #  respond: take a string, a set of regexps, and a corresponding
  #    set of response lists; find a match, and return a randomly
  #    chosen response from the corresponding list.
  #----------------------------------------------------------------------
  def respond(self,str):
    # find a match among keys
    for i in range(0,len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        resp = random.choice(self.values[i])
        # we've got a response... stuff in reflected text where indicated
        pos = string.find(resp,'%')
        while pos > -1:
          num = string.atoi(resp[pos+1:pos+2])
          resp = resp[:pos] + \
            self.translate(match.group(num),gReflections) + \
            resp[pos+2:]
          pos = string.find(resp,'%')
        # fix munged punctuation at the end
        if resp[-2:] == '?.': resp = resp[:-2] + '.'
        if resp[-2:] == '??': resp = resp[:-2] + '?'
        return resp


def echo():
    global LAST_UPDATE_ID
    therapist = eliza();
    # Request updates from last updated_id
    try:
        for update in bot.getUpdates(offset=LAST_UPDATE_ID):
            if LAST_UPDATE_ID < update.update_id:
                # chat_id is required to reply any message
                chat_id = update.message.chat_id
                from_user = update.message.from_user
                if update.message.text!=None:
                    # message = update.message.text.encode('utf-8')
                    message = update.message.text
                    message = message.encode('utf-8')
                    print(message)
                else: message=None
                print(from_user)
                if (message):
                    if '\AUGcalendar' in message:
                        AUGCalendar()
                        LAST_UPDATE_ID = update.update_id
                        return
                if (message):
                    if '\weather' in message:
                        weather_info()
                        LAST_UPDATE_ID = update.update_id
                        return
                if 'Giancarlo' in from_user['first_name']:
                    if (message):
                        if '\say' in message:
                            message=message.partition(" ")
                            type(message)
                            bot.sendMessage(chat_id=AUGChatId, text=message[2])
                            #bot.sendMessage(chat_id='-6581067', text=message[2])
                            LAST_UPDATE_ID = update.update_id
                            return
                if 'Giancarlo' in from_user['first_name']:
                    if (message):
                        if '\calendar' in message:
                            message=message.partition(" ")
                            type(message)
                            message=message[2].partition(" ")
                            type(message)
                            c = calendar.TextCalendar(calendar.SUNDAY)
                            calen=c.formatmonth(int(message[0]),int(message[2]))
                            calen=calen.replace("  ", "   ")
                            calen=calen.replace(" ", " ")
                            bot.sendMessage(chat_id=AUGChatId, text=calen)
                            LAST_UPDATE_ID = update.update_id
                            return
                if 'Giancarlo' in from_user['first_name']:
                    if update.message.photo!=None:
                        bot.sendPhoto(chat_id=AUGChatId, photo=update.message.photo)
                        LAST_UPDATE_ID = update.update_id
                        return
                if (message):
                    # Reply the message
                    bot.sendMessage(chat_id=chat_id, text=therapist.respond(message))

                    LAST_UPDATE_ID = update.update_id
    except:
        pass


def AUGCalendar():
    # Compute the dates for each week that overlaps the month
    now = datetime.datetime.now()
    print str(now)
    year=now.year
    month=now.month
    c = calendar.monthcalendar(year, month)
    first_week = c[0]
    second_week = c[1]
    third_week = c[2]
    fourth_week = c[3]
    fifth_week = c[4]

    # If there is a WEDNESDAY in the first week, the second WEDNESDAY
    # is in the second week.  Otherwise the second Thursday must 
    # be in the third week.
    if first_week[calendar.WEDNESDAY]:
        Ameeting_date = second_week[calendar.WEDNESDAY]
        Bmeeting_date = fourth_week[calendar.WEDNESDAY]
    else:
        Ameeting_date = third_week[calendar.WEDNESDAY]
        Bmeeting_date = fifth_week[calendar.WEDNESDAY]
    message='Gli appuntamenti di AUG di questo mese sono:\n Mercoledì %2s e Mercoledì %2s' % (Ameeting_date, Bmeeting_date)
    bot.sendMessage(chat_id=AUGChatId, text=message)
    c = calendar.TextCalendar(calendar.SUNDAY)
    calen=c.formatmonth(year,month)
    calen=calen.replace("  ", "   ")
    calen=calen.replace(" ", " ")
    print(calen)
    bot.sendMessage(chat_id=AUGChatId, text=calen)
    today = datetime.date.today()
    someday = datetime.date(year, month, Ameeting_date)
    diff = someday - today
    message='Più precisamente, mancano %2s giorni al prossimo AUG meeting!!' %(diff.days)
    bot.sendMessage(chat_id=AUGChatId, text=message)



def weather_info():
    #!/usr/bin/env python
    therapist = eliza();
    from urllib2 import urlopen
    from contextlib import closing
    import json
    now = datetime.datetime.now()
    day=str(now.day)
    year=str(now.year)
    month=str(now.month)
    today = str(datetime.datetime.today().weekday())
    today=therapist.translate(today,gDayEn)
    month=therapist.translate(month,gMonthIta)
    weather_com_result = pywapi.get_weather_from_weather_com('ITPM3241')
    weathernow=therapist.translate(string.lower(weather_com_result['current_conditions']['text']),gWeatherIta)
    for i in weather_com_result['forecasts']:
        if i['day_of_week']==today:
            print i
            dayfore= therapist.translate(string.lower(i['day']['text']),gWeatherIta)
            nightfore=therapist.translate(string.lower(i['night']['text']),gWeatherIta)
            maxtemp=string.lower(i['high'])
            mintemp=string.lower(i['low'])
            break
    temp=str(weather_com_result['current_conditions']['temperature'])
    today=therapist.translate(str(datetime.datetime.today().weekday()),gDayIta)
    message= "Oggi é "+today+", "+day+" "+month+" "+year+"\n in questo momento sono le "+str(now.hour)+" e "+str(now.minute)+" minuti"
    bot.sendMessage(chat_id=AUGChatId, text=message)
    message= "tempo "+weathernow+", temperatura di "+temp+"C"
    if now.hour<12:
        message=message+"\n durante la giornata "+dayfore
    message=message+"\n in serata "+nightfore
    message=message+"\n temperatura massima: "+maxtemp+"C"
    message=message+"\n temperatura minima: "+mintemp+"C"
    bot.sendMessage(chat_id=AUGChatId, text=message)
    
    



if __name__ == '__main__':
    while True:
        echo()
        time.sleep(3)


