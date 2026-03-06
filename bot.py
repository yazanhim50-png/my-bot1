import discord
from discord.ext import commands
import asyncio

# --- إعدادات البوت الأساسية ---
# ضع التوكن الخاص بك بين العلامتين ''
TOKEN = "MTQ3ODQ5NDYxMTM2NTMwMjI3Mg.GlXALJ.YIkrMs6HQ5ePJv-l6k9tYalEL4"

# ضع ايدي الروم الصوتي هنا (أرقام فقط بدون علامات)
VOICE_ID = 1427375098041467011 

# --- تفعيل الصلاحيات (Intents) ---
intents = discord.Intents.default()
intents.voice_states = True  # ضروري جداً للدخول للصوت
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('--------------------------')
    print(f'تم تسجيل الدخول بنجاح!')
    print(f'اسم البوت: {bot.user.name}')
    print(f'معرف البوت: {bot.user.id}')
    print('--------------------------')
    
    # محاولة الاتصال بالروم الصوتي
    channel = bot.get_channel(VOICE_ID)
    
    if channel:
        try:
            # التحقق إذا كان البوت متصلاً بالفعل
            if bot.voice_clients:
                for vc in bot.voice_clients:
                    await vc.disconnect()
            
            await channel.connect()
            print(f"✅ تم دخول الروم الصوتي: {channel.name}")
        except Exception as e:
            print(f"❌ فشل الدخول للروم: {e}")
    else:
        print("⚠️ خطأ: لم يتم العثور على الروم. تأكد من الأيدي (ID).")

# تشغيل البوت
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure:
    print("❌ خطأ: التوكن غير صحيح! تأكد من نسخة من موقع المطورين.")
except Exception as e:
    print(f"❌ حدث خطأ غير متوقع: {e}")
from flask import Flask
from threading import Thread
import time

app = Flask('')

@app.route('/')
def home():
    return "I am alive!"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- ضع كودك الأساسي هنا ---
def my_main_logic():
    while True:
        print("كودك يعمل الآن في الخلفية...")
        time.sleep(60)
# -------------------------

if __name__ == "__main__":
    keep_alive() # تشغيل السيرفر الوهمي
    my_main_logic() # تشغيل كودك الأصلي

