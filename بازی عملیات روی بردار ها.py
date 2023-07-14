import source
import os
from datetime import datetime

userDir = os.path.expanduser('~')

l = os.listdir(userDir+"\\Pictures\\")
if not "عملیات رو بردارها" in l:
    os.makedirs(userDir+"\\Pictures\\عملیات رو بردارها")

def run():
    try:
        source.run()
    except Exception as e:
        if e.args[0] != "display Surface quit":
            with open("err.log", "a") as f:
                now = datetime.now()
                f.write(
                    "{0} - {1}\n\n".format(now, e.args[0])
                )

if __name__ == "__main__":
    run()
    #source.run()