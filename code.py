pathToVS2022 = ''    #add paths to program(s) desired here ***BACKSLASHES INDICATING DIRECTORY MUST BE DOUBLED***
pathToVS2019 = ''
fop = ''   
fop1 = ''
sp = ''
sp1 = ''
zd = ''
zd1 = ''
wo = ''
wo1 = ''
print("""
******************************************************************************************* 
*   _____     ______     __    __      ______     ______     ______   __  __     ______   *   
*  /\  __-.  /\  ___\   /\ \  / /     /\  ___\   /\  ___\   /\__  _\ /\ \/\ \   /\  -- \  *   
*  \ \ \/\ \ \ \  __\   \ \ \/ /      \ \___  \  \ \  __\   \/_/\ \/ \ \ \_\ \  \ \  __/  *   
*   \ \____/  \ \_____\  \ \__/        \/\_____\  \ \_____\    \ \_\  \ \_____\  \ \_\    *  
*    \/___/    \/_____/   \/_/          \/_____/   \/_____/     \/_/   \/_____/   \/_/    *  
*                                                                                         *
*******************************************************************************************""")
app = str(input("Select application (fop,sp,zd,wo):"))
print("Opening File(s)...")

if app == 'fop':
    subprocess.Popen([pathToVS2022, fop])
    subprocess.Popen([pathToVS2022, fop1])
    print("Success!")
elif app == 'sp':
    subprocess.Popen([pathToVS2019, sp])
    subprocess.Popen([pathToVS2019, sp1])
    print("Success!")
elif app == 'zd':
    subprocess.Popen([pathToVS2019, zd])
    subprocess.Popen([pathToVS2019, zd1])
    print("Success!")
elif app == 'wo':
    subprocess.Popen([pathToVS2019, wo])
    subprocess.Popen([pathToVS2019, wo1])
    print("Success!")
else:
    print("Application Not Found.")
