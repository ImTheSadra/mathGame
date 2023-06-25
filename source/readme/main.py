import os, time
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


text = """{3}
╔═══════════════╦════════════════════════════════╦══════════════════════════╗
║{4} Coffee | Z3R0{3} ║ {4}Email: m.sadra.gorji@gmail.com {3}║ {4}shad : @sadra_gorji     {3} ║
╠═══════════════╩════════════════════════════════╩══════════════════════════╣
║ {5}       {2}                                                        {3}  ║         
║{5}        {1}                                                       {3}   ║         
║  {5}      {0}                                             {3}             ║         
║ {5}       _____________                                  {3}                    ║
║ {5}      <_____________> ___      {3}                                           ║
║  {5}     |             |/ _ \\      {3}                                          ║
║  {5}     |               | | |      {3}                                         ║
║{5}       |               |_| |         {3}                                      ║
║{5}    ___|             |\\___/         {3}                                       ║
║{5}   /    \\___________/    \\         {3}                                        ║
║{5}   \\_____________________/          {3}                                       ║
╠═══════════════════════════════════╦═══════════════════════════════════════╣
║{4} Shop : https://discord.gg/animeh {3} ║ {4}github : https://github.com/SadraZ3R0{3} ║
╚═══════════════════════════════════╩═══════════════════════════════════════╝
"""

loading = """
╔═══════════════╗
║               ║
║     {0}%      ║
║               ║
╠═══════════════╣
║  Z3R0 - Sadra ║
║               ║
╚═══════════════╝
"""

n = 100

def clear():
	try:os.system("cls")
	except:
		try:os.system("clear")
		except:print("==========================================")

while n > -1:
	clear()
	n_ = str(n)
	if len(n_) == 1:
		n_ = "  "+n_
	elif len(n_) == 2:
		n_ = " "+n_
	print(loading.format(n_))
	if n == 0:
		time.sleep(3)
	n -= 1



clear()

b = [
	[
		"  )   (  ",
		" (  (  ) ",
		"  )  )   "
	],
	[
		"(   (  ) ",
		" )   )   ",
		"    (    "
	],
	[
		" )   )   ",
		"    (    ",
		"  (    ) "
	]
]

try:
	while True:
		for i in b:
			clear()
			print(text.format(i[0], i[1], i[2], Fore.MAGENTA, Fore.RESET, Fore.BLUE))
			time.sleep(0.30)
	time.sleep(3)
except KeyboardInterrupt:
	pass