from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime as T
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'Django_Telegram_ChatBot.settings'
django.setup()

from App import models

x = T.datetime.now()
today_date = x.strftime('%Y-%m-%d')
token = '6274241906:AAHDlICC24tn_uSsgvML3smeVYHPMwHUEqs'

print("Bot is Running...")


def userMessageLogs(update):
    print(f'"{update.message.chat.username}" says: {update.message.text}\n')


def start(update, context):
    userMessageLogs(update)
    update.message.reply_text(
        f'Hello {update.message.chat.first_name} I am your Bot I can help you create and manage your work.\n\n'
        'You can control me by sending these commands:\n\n'
        '/Clockin - Clock into Work \n'
        '/After_Clockin - Punch In After Work Get Off Work \n'
        '/Leave_Clockin - Leave Clock In \n'
        '/Back_Clockin - Come Back and Punch In \n\n\n\n'
        'Copyright© 2023. Developed By Fawad')


def clockin(update, context):
    userMessageLogs(update)
    user = update.message.chat.username
    emp = models.Employee.objects.filter(username=user).last()
    if emp:
        if not models.EmpClockin.objects.filter(emp=emp, clockinDate=today_date):
            models.EmpClockin(emp=emp).save()
            update.message.reply_text('You Have Been Check In Today')
        else:
            update.message.reply_text('You Have Clocked In Today, Please Do Not Repeat The Operation')
    else:
        update.message.reply_text(f'Sorry! The Company Does Not Have The Employee @{user}')


def afterClockin(update, context):
    userMessageLogs(update)
    user = update.message.chat.username
    if models.Employee.objects.filter(username=user):
        update.message.reply_text('You Are Checked In')
    else:
        update.message.reply_text(f'Sorry! Your Username @{user} is Not Registerd')


def leaveClockin(update, context):
    userMessageLogs(update)
    user = update.message.chat.username
    if models.Employee.objects.filter(username=user):
        update.message.reply_text('You Are Checked In')
    else:
        update.message.reply_text(f'Sorry! The Company Does Not Have The Employee @{user}')


def backClockin(update, context):
    userMessageLogs(update)
    user = update.message.chat.username
    if models.Employee.objects.filter(username=user):
        update.message.reply_text('You Are Checked In')
    else:
        update.message.reply_text(f'Sorry! The Company Does Not Have The Employee @{user}')


def handle_message(update, context):
    userMessageLogs(update)
    if update.message.text:
        update.message.reply_text('Sorry Cannot Undestand Try Again\n\n')
        start(update, context)


def error(update, context):
    userMessageLogs(update)
    print(f'@{update.message.chat.username} Caused An Error That is {context.error}')


if __name__ == "__main__":
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("clockin", clockin))
    dp.add_handler(CommandHandler("after_clockin", afterClockin))
    dp.add_handler(CommandHandler("leave_clockin", leaveClockin))
    dp.add_handler(CommandHandler("back_clockin", backClockin))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling(1.0)
    updater.idle()
