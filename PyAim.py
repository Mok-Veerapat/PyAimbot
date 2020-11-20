import autopy as ap
import time
import math

def user():
    line()
    while True:
        print("type 1 for capture screen")
        print("type 2 for aimbot")
        print("Type 3 for check mouse position")
        print("type 4 for close program")
        a = int(input())
        if a == 1:
            ap.bitmap.capture_screen().save("mok.png")
        elif a == 2:
            tick = int(input("Enter Aimbot time tick:"))
            aimbot(tick)
        elif a == 3:
            try:
                print("\"Ctrl - c\" to stop")
                while True:
                    mouse_pos = ap.mouse.location()
                    mai_string = str(mouse_pos)
                    print(mai_string, end="")
                    print('\b'*len(mai_string), end="", flush=True)
            except KeyboardInterrupt:
                break       
        else:
            break

def get_color():
    while True:
        a = int(input("Selecter color \"press\" 1 :"))
        if a == 1:
            pos = ap.mouse.location()
            pic = ap.bitmap.capture_screen()
            color = pic.get_color(pos[0],pos[1])
            print("Color is : ",color)
        else:
            break
    return color

def line():
    print("*"*30)
    

def aimbot(tick):

    line()
    Target_color = get_color()
    line()

    center = (0, 0)
    topleft = (0, 0)
    width, height = 1919, 1079
    while True:
        print("1  Set_Center")
        print("2  Set_TopLeft")
        print("3  Set_bottomRight")
        print("4  i already set it")
        a = int(input("Enter :"))
        if a == 1:
            center = ap.mouse.location()
            print("center is :",center)
        elif a == 2:
            topleft = ap.mouse.location()
            print("Topleft is :",topleft)
        elif a == 3:
            bottomright = ap.mouse.location()
            print("bottomright is :",bottomright)
    
            width = bottomright[0] - topleft[0]
            height = bottomright[1] - topleft[1]
            print(width, height)
        else:
            break
    line()  

    count = 0
    try:
        for i in range(tick):
            time.sleep(0)
    
            picture = ap.bitmap.capture_screen()
            color_pos = picture.find_color(Target_color, 0.08, (topleft, (width, height)), center)
    
            if color_pos == None:
                print("Cant Detected")
                pass
                #ap.mouse.move(mouse_pos_x, mouse_pos_y)
            else:
                #เลื่อนเมาส์
                count += 1
                print("Target lock --> ",color_pos,"+ ",count)
                ap.mouse.move(color_pos[0], color_pos[1])
                ap.mouse.click()
    except KeyboardInterrupt:
        print('\n')



user()



'''screen = autopy.bitmap.capture_screen()  #get_color HEXVALUE
print(screen.get_color(600, 600))
position = screen.find_color(2698558,0.03)
print(position)'''


