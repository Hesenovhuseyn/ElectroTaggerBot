#################################
# Electro Tagger Bot #
#################################
#  Sahib - @HuseynH 
# Reponu Öz Adına Çıxaran Peysərdi
# Reponu Açığ Görüm Oğurlama Oğlum
##################################

import heroku3
import random
import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation
from config import client, USERNAME, startmesaj, qrupstart, komutlar, sahib, support, group

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)


ozel_list = [5188815198]
anlik_calisan = []
grup_sayi = []

Husu_tag = []

Huseyn_H = {}  
  
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global Husu_tag
  Husu_tag.remove(event.chat_id)
  
  if event.chat_id in Huseyn_H:await event.respond(f"❌**Tağ Prosrsi Dayandırıldı.\n\n Tağ olunanların sayı: {Huseyn_H[event.chat_id]}**")

  
@client.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):
  global Husu_tag
  Husu_tag.remove(event.chat_id)
  
  
  
# Başlanğıc Mesajı
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     return await event.reply(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.inline("✍ Əmrlər", data="help")
                      ],
                      [Button.url('🌱 Məni Qrupa Əlavə Et', f'https://t.me/GunayRobot?startgroup=a')],
                     [Button.url('🥳 Söhbət Qrupu', f'https://t.me/SohbetFc')],
                      [Button.url('📣 Kanal', f'https://t.me/ElikoResmi')],
                       [Button.url('👨🏻‍💻 Sahib', f'https://t.me/Eliko7x7')]
                    ),
                    link_preview=False)
                    
                    
  if event.is_group:
    return await client.send_message(event.chat_id, f"{qrupstart}")


# Başlanğıc Button
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.inline("✍ Əmrlər", data="help")
                      ],
                      [Button.url('🌱 Məni Qrupa Əlavə Et', f'https://t.me/{USERNAME}?startgroup=a')],
                     [Button.url('📣 Söhbət Qrupu', f'https://t.me/{group}')],
                      [Button.url('📣 Kanal', f'https://t.me/{support}')],
                       [Button.url('👨🏻‍💻 Sahib', f'https://t.me/{sahib}')]
                    ),
                    link_preview=False)
# gece kusu
@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):
    await event.edit(f"{komutlar}", buttons=(
                      [
                      Button.inline("Geri Qayıt", data="start")
                      ]
                    ),
                    link_preview=False)
                    
#########################
    
# Emoji ilə Tağ

emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")
    
@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def etag(event):
  global Husu_tag
  if event.is_private:
    return await event.respond(f"bu emri qruoda islet")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sen admin deylsen")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhnə mesajları görə bilmirəm! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tağ mesajı yazmadın!__")
  else:
    return await event.respond("__Tağ etməy üçün bir mesaj yanıtlayın və ya bir mətn yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Emoji Tağ Başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                      Button.inline(f"dayandir", data="cancel")
                      ]
                    )
                  ) 
    Husu_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in Husu_tag:
        await event.respond("⛔ Emoji Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                      Button.inline(f"🙄Təmirdə", data="yeniden")
                      ]
                    )
                  )
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global Husu_tag
  Husu_tag.remove(event.chat_id)        

#########################
    
# 5 li tağ modulu
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def tag(event):
  global Husu_tag
  if event.is_private:
    return await event.respond(f"bu emri qruoda islet")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sen admin deylsen")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhnə mesajları görə bilmirəm! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tağ mesajı yazmadın!__")
  else:
    return await event.respond("__Tağ etməy üçün bir mesaj yanıtlayın və ya bir mətn yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ 5-li Tağ Başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                      Button.inline(f"🥳dayandir", data="cancel")
                      ]
                    )
                  ) 
    Husu_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in Husu_tag:
        await event.respond("⛔ Tək Tək Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                      Button.inline(f"🙄Təmirdə", data="yeniden")
                      ]
                    )
                  )
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global Husu_tag
  Husu_tag.remove(event.chat_id)              
        
#########################

#tek-tek tağ 

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def tektag(event):
  global Husu_tag
  if event.is_private:
    return await event.respond(f"bu emri qruoda islet")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sen admin deylsen")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhnə mesajları görə bilmirəm! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tağ mesajı yazmadın!__")
  else:
    return await event.respond("__Tağ etməy üçün bir mesaj yanıtlayın və ya bir mətn yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Tək-Tək Tağ Başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                      Button.inline(f"dayandir", data="cancel")
                      ]
                    )
                  ) 
    Husu_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in Husu_tag:
        await event.respond("⛔ Tək Tək Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                      Button.inline(f"yeniden", data="yeniden")
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
  
  
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global Husu_tag
  Husu_tag.remove(event.chat_id)        
  
#########################

# renk ile etiketleme modülü
reng = "🔴 🟠 🟡 🟢 🔵 🟣 🟤 ⚫ ⚪ " .split(" ") 
        

@client.on(events.NewMessage(pattern="^/rtag ?(.*)"))
async def rtag(event):
  global Husu_tag
  if event.is_private:
    return await event.respond(f"Bu emri qrupda isled")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sen admin deylsen")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhnə mesajları görə bilmirəm! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tağ mesajı yazmadın!__")
  else:
    return await event.respond("__Tağ etməy üçün bir mesaj yanıtlayın və ya bir mətn yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Rənglərlə Tağ Başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                      Button.inline(f"dayandir", data="cancel")
                      ]
                    )
                  ) 
    Husu_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(reng)}](tg://user?id={usr.id}) "
      if event.chat_id not in Husu_tag:
        await event.respond("⛔ Rənglərlə Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                      Button.inline(f"🙄Təmirdə", data="yeniden")
                      ]
                    )
                  )
        return
      if usrnum == 3:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global Husu_tag
  Husu_tag.remove(event.chat_id)              
        
######################

#ürəklərlə Tağ
urek = "❤️ 🧡 💛 💚 💙 💜 🖤 💘 💝 ❤️   🧡 💛 💚 💙 💜 🖤 💘 💝".split(" ") 
        
@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def utag(event):
  global Husu_tag
  if event.is_private:
    return await event.respond(f"bu emri qruoda islet")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sen admin deylsen")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhnə mesajları görə bilmirəm! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tağ mesajı yazmadın!__")
  else:
    return await event.respond("__Tağ etməy üçün bir mesaj yanıtlayın və ya bir mətn yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Ürəklərlə Tağ Başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                      Button.inline(f"dayandir", data="cancel")
                      ]
                    )
                  ) 
    Husu_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(urek)}](tg://user?id={usr.id}) "
      if event.chat_id not in Husu_tag:
        await event.respond("⛔ Ürəklərlə Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                      Button.inline(f"🙄Təmirdə", data="yeniden")
                      ]
                    )
                  )
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global Husu_tag
  Husu_tag.remove(event.chat_id)             
        
####################       
#Adlarla Tağ

ad = ( 
"🐰 Dovşan",
"🦁 Şir",
"💍 Evli",
"🐶 İT",
"🐻 Ayı",
"🐭 Siçan",
"🥰 Sevimli",
"😜 Subay",
"😎Sevgili",
"👨‍👩‍👦‍👦 Ailə",
"🤑 Varlı",
"🕵‍♂ Vəkil",
"🐒 Meymun",
"🐣 Cücə",
"🦊 Tülkü",
"👩‍⚕ Həkim",
"👨‍🏫 Müəllim",
"👨‍🍳 Aşbaz",
"👩‍🏫 Müəllimə",
"🧚‍♀ Mələk",
"😊 Dəyərli",
"Gözəl💄",
"Çirkin😒",
"Unutqan 🤕",
"🦠 Karona",
"🤭 Dəcəl",
"😡 Lovğa",
"🙈Utancaq",
"😎 Səbirli",
"🧑‍🔬 Ağıllı"
)


@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def atag(event):
  global Husu_tag
  if event.is_private:
    return await event.respond(f"bu emri qruoda islet")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sen admin deylsen")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhnə mesajları görə bilmirəm! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tağ mesajı yazmadın!__")
  else:
    return await event.respond("__Tağ etməy üçün bir mesaj yanıtlayın və ya bir mətn yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Adlarla Tağ Başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                      Button.inline(f"dayandir", data="cancel")
                      ]
                    )
                  ) 
    Husu_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(ad)}](tg://user?id={usr.id}) "
      if event.chat_id not in Husu_tag:
        await event.respond("⛔ Adlarla Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                      Button.inline(f"🙄Təmirdə", data="yeniden")
                      ]
                    )
                  )
        return
      if usrnum == 3:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global Husu_tag
  Husu_tag.remove(event.chat_id)              
        
######################

##Cümlələr lə Tağ





####ElectroTaggerBot Stat

@client.on(events.NewMessage())
async def mentionalladmin(event):
  global grup_sayi
  if event.is_group:
    if event.chat_id in grup_sayi:
      pass
    else:
      grup_sayi.append(event.chat_id)

@client.on(events.NewMessage(pattern='^/stats ?(.*)'))
async def son_durum(event):
    global anlik_calisan,grup_sayi,ozel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
      return
    await event.respond(f"**Bot Güncellendi✅\n[Electro](http://t.me/ElectroTaggerBot) Güncel Verileri 🖥️**\n\n**Toplam Grub: `{len(grup_sayi)}`\n\nAnlık Çalışan Grub: `{len(anlik_calisan)}`**")

###Broadcast

@client.on(events.NewMessage(pattern='^/broadcast ?(.*)'))
async def duyuru(event):
 
  global grup_sayi,ozel_list
  sender = await event.get_sender()
  if sender.id not in ozel_list:
    return
  reply = await event.get_reply_message()
  await event.respond(f"Toplam {len(grup_sayi)} Gruba'a mesaj gönderiliyor...")
  for x in grup_sayi:
    try:
      await client.send_message(x,f"**📣 Reklam**\n\n{reply.message}")
    except:
      pass
  await event.respond(f"Gönderildi.")


###############################

print(">> Bot Super İşləyir 😎 Sahibim 【H】【U】【S】【E】【Y】【N】 <<")
client.run_until_disconnected()
run_until_disconnected()
