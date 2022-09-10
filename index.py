import requests
try:
  clothe = ""
  r=requests.get(f"https://assetdelivery.roblox.com/v1/assetId/{clothe}")
  XML = r.json()['location']
  r2=requests.get(XML)
  JUIC = str(r2.content)
  IDD = str(JUIC.split("<url>http://www.roblox.com/asset/?id=")[1].split("</url>")[0])
  SOP = str(JUIC.split('<string name="Name">')[1].split("</string>")[0])
  if SOP == "Shirt":aaa = "s"
  else:aaa="p"
  r3=requests.get(f"https://www.roblox.com/library/{IDD}").text
  URLL = r3.split("""<span class="thumbnail-span" ><img  class='' src='""")[1].split("'")[0]
  TITLE = str(r3.split("<title>")[1].split("</title>")[0]);TITLE = TITLE.replace(" ","_")
  rurl = requests.get(URLL).content
  if aaa == "s":
            with open(f"{TITLE}.jpg","wb") as f:
              f.write(rurl)
except: 
  print("Not a valid ID")
