import requests
import regex as re
from time import sleep


def download():

    with open("PARAGRAPHS.txt", "ab") as out: # Change txt file
        with open("tredjeUpplaganBokstaver.txt") as f: # Change which letter file
            for x in f:
                sleep(10)
                x = x.strip()
                if not x:
                    continue
                req = requests.get('https://runeberg.org/download.pl?mode=ocrtext&work='+x, stream=True, timeout=100)
                if req.status_code != 200:
                    print("Failed to download file, got status: " + str(req.status_code))
                else:
                    req.encoding = "utf-8"
                    te = req.text
                    #pattern = r'REALENCYKLOPEDI' #r'en del av upplagan.'
                    #matches = re.finditer(pattern, te)
                    #last = ""
                    #for m in matches:
                    #    last = m
                    #if last != "":
                    #    te = te[last.end():]

                    out.write(te.encode("utf-8"))
                    out.write(b"\n\n")
                    print("skrivning klar för",x)
                req.close()
        f.close()
    print("Done!")


if __name__ == '__main__':
    download()
