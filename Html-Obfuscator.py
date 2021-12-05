from subprocess import check_call
import os
import sys
import pip
import time
import platform


def Banners():
    try:
        from colorama import Fore, Style, init
    except Exception:
        try:
            pip.main(["install",  "colorama"])
        except AttributeError:
            check_call([sys.executable, '-m', 'pip', 'install', "colorama"])
            time.sleep(10)
            init()
        else:
            time.sleep(10)
            init()
    else:
        init()
    
    cg = Fore.GREEN
    cy = Fore.YELLOW
    cb = Fore.BLUE
    cyn = Fore.MAGENTA
    sd = Style.DIM

    banner = f"""
        {cb+sd}██{cyn+sd}╗  {cb+sd}██{cyn+sd}╗{cb+sd}████████{cyn+sd}╗{cb+sd}███{cyn+sd}╗{cb+sd}   ███{cyn+sd}╗{cb+sd}██{cyn+sd}╗     
        {cb+sd}██{cyn+sd}║{cb+sd}  ██{cyn+sd}║╚══{cb+sd}██{cyn+sd}╔══╝{cb+sd}████{cyn+sd}╗{cb+sd} ████{cyn+sd}║{cb+sd}██{cyn+sd}║     
        {cb+sd}███████{cyn+sd}║{cb+sd}   ██{cyn+sd}║{cb+sd}   ██{cyn+sd}╔{cb+sd}████{cyn+sd}╔{cb+sd}██{cyn+sd}║{cb+sd}██{cyn+sd}║     
        {cb+sd}██{cyn+sd}╔══{cb+sd}██{cyn+sd}║{cb+sd}   ██{cyn+sd}║{cb+sd}   ██{cyn+sd}║╚{cb+sd}██{cyn+sd}╔╝{cb+sd}██{cyn+sd}║{cb+sd}██{cyn+sd}║     
        {cb+sd}██{cyn+sd}║{cb+sd}  ██{cyn+sd}║{cb+sd}   ██{cyn+sd}║{cb+sd}   ██{cyn+sd}║ ╚═╝{cb+sd} ██{cyn+sd}║{cb+sd}███████{cyn+sd}╗
        {cyn+sd}╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚══════╝
    """

    banner2 = f"""
        {cg+sd} .d88888b.  888       .d888                                     888                    
        {cy+sd}d88P" "Y88b 888      d88P"                                      888                    
        {cg+sd}888     888 888      888                                        888                    
        {cy+sd}888     888 88888b.  888888 888  888 .d8888b   .d8888b  8888b.  888888 .d88b.  888d888 
        {cg+sd}888     888 888 "88b 888    888  888 88K      d88P"        "88b 888   d8P  Y8b 888P"   
        {cy+sd}888     888 888  888 888    888  888 "Y8888b. 888      .d888888 888   88888888 888     
        {cg+sd}Y88b. .d88P 888 d88P 888    Y88b 888      X88 Y88b.    888  888 Y88b. Y8b.     888     
        {cy+sd} "Y88888P"  88888P"  888     "Y88888  88888P'  "Y8888P "Y888888  "Y888 "Y8888  888     \033[0;m
    """

    if platform.uname()[0] == "Windows":
        os.system("cls")
    if platform.uname()[0] == "Linux":
        os.system("clear")

    time.sleep(3)
    print(banner)
    time.sleep(2)
    print(banner2)
    time.sleep(2)
    print("              \033[29;1m==================== \033[36;1mCreated By \033[34;1m: \033[32;1mDr.Linux\033[0;m \033[29;1m==================== \033[0;m")
    time.sleep(1)
    print("          \033[29;1m==================== \033[35;1mMy GitHub \033[34;1m: \033[33;1mDrLinuxOfficial \033[31;1m!\033[0;m \033[29;1m==================== \033[0;m")
        


class Obfuscator:
    def __init__(self, Source):
        self.Source = Source
    
    def DataObfuscator(self, char):
        data = {
                " " : "%20",
                "!" : "%21",
                '"' : "%22",
                "#" : "%23",
                "$" : "%24",
                "%" : "%25",
                "&" : "%26",
                "'" : "%27",
                "(" : "%28",
                ")" : "%29",
                "*" : "%2A",
                "+" : "%2B",
                "," : "%2C",
                "-" : "%2D",
                "." : "%2E",
                "/" : "%2F",
                "0" : "%30",
                "1" : "%31",
                "2" : "%32",
                "3" : "%33",
                "4" : "%34",
                "5" : "%35",
                "6" : "%36",
                "7" : "%37",
                "8" : "%38",
                "9" : "%39",
                ":" : "%3A",
                ";" : "%3B",
                "<" : "%3C",
                "=" : "%3D",
                ">" : "%3E",
                "?" : "%3F",
                "@" : "%40",
                "A" : "%41",
                "B" : "%42",
                "C" : "%43",
                "D" : "%44",
                "E" : "%45",
                "F" : "%46",
                "G" : "%47",
                "H" : "%48",
                "I" : "%49",
                "J" : "%4A",
                "K" : "%4B",
                "L" : "%4C",
                "M" : "%4D",
                "N" : "%4E",
                "O" : "%4F",
                "P" : "%50",
                "Q" : "%51",
                "R" : "%52",
                "S" : "%53",
                "T" : "%54",
                "U" : "%55",
                "V" : "%56",
                "W" : "%57",
                "X" : "%58",
                "Y" : "%59",
                "Z" : "%5A",
                "[" : "%5B",
                "]" : "%5D",
                "^" : "%5E",
                "_" : "%5F",
                "`" : "%60",
                "a" : "%61",
                "b" : "%62",
                "c" : "%63",
                "d" : "%64",
                "e" : "%65",
                "f" : "%66",
                "g" : "%67",
                "h" : "%68",
                "i" : "%69",
                "j" : "%6A",
                "k" : "%6B",
                "l" : "%6C",
                "m" : "%6D",
                "n" : "%6E",
                "o" : "%6F",
                "p" : "%70",
                "q" : "%71",
                "r" : "%72",
                "s" : "%73",
                "t" : "%74",
                "u" : "%75",
                "v" : "%76",
                "w" : "%77",
                "x" : "%78",
                "y" : "%79",
                "z" : "%7A",
                "{" : "%7B",
                "|" : "%7C",
                "}" : "%7D",
                "~" : "%7E",
                "‚" : "%82",
                "ƒ" : "%83",
                "„" : "%84",
                "…" : "%85",
                "‘" : "%91",
                "’" : "%92",
                "“" : "%93",
                "”" : "%94",
                "–" : "%96",
                "—" : "%97",
                "˜" : "%98",
                "™" : "%99",
                "©" : "%A9",
               }
        try:
            datas = data[char]
        except Exception:
            datas = "%20"
            return datas
        else:
            return datas
    
    def ObfuscaterGenerator(self):
        file_source = self.Source
        with open(file_source, "r") as rd:
            data_file = rd.read()
        data_obfuscated = ""
        for i in data_file:
            char_data = self.DataObfuscator(i)
            data_obfuscated += char_data
        new_file = "Output-HtmlObf/Generated-HtmlObf-" + (str(len(data_obfuscated))) + ".html"
        if not os.path.isdir("Output-HtmlObf"):
            os.mkdir("Output-HtmlObf")
        with open(new_file, "w") as wr:
            wr.write("<!-- Created By : Dr.Linux -->")
            wr.write("\n")
            wr.write("<!-- Obfuscated With : HtmlObf -->")
            wr.write("\n")
            wr.write("<!-- My GitHub : DrLinuxOfficial -->")
            wr.write("\n")
            wr.write("\n")
            wr.write('<script language="javascript">')
            wr.write("\n")
            wr.write(f'   document.write(unescape("{data_obfuscated}"));')
            wr.write("\n")
            wr.write('</script>')
        print("\033[32;1mObfuscated !!! \033[0;m")
        print(f"\033[32;1mPlease Check \033[34;1m: \033[29;1m{new_file} \033[0;m")


Banners()
print("\n")
print("\n")
print("\033[31;1mExample \033[32;1m=\033[33;1m> \033[36;1m/MyData/index.html \033[0;m")
input_file = input("\033[36;1mYoure Html File Directory For Obfuscatering : \033[0;m")
Obfuscate = Obfuscator(input_file)
Obfuscate.ObfuscaterGenerator()
