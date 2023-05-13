import requests

url = "https://pu.vk.com/c842728/ss2109/upload.php?act=do_add&mid=399833079&aid=-14&gid=0&hash=39bf218af1e6cab2a8d1656cce17d34a&rhash=697559e8aedb9465c76ff9058f72b587&swfupload=1&api=1&wallphoto=1"

payload={}
files=[
  ('file1',('postImage.jpg',open('D:/IDE Projects/IdeaProjects/t.toleubekov/src/test/resources/postImage.jpg','rb'),'image/jpeg'))
]
headers = {
  'Cookie': 'remixff=0; remixlang=0; remixlgck=dfacb86165ffb1b901; remixstid=737800984_Czzir2u2PAL6ABZOAnwgve9U31VCzPBMGYR5413zfJg; remixstlid=9067673423403931853_663ZUhnICmd2dnArXBbke3HM04OgLlWVnwISgEMqNFX; remixua=-1%7C-1%7C-1%7C1327222316'
}

response = requests.Request("POST", url, headers=headers, data=payload, files=files)
prepared = response.prepare()
print(prepared.url)
# print(response.text)
