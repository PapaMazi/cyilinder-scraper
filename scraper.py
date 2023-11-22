import pyautogui, math, csv
import pyperclip, time, re

def main():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

    field = ['Cylinder', 'Radius', 'Height', 'Volume']
    with open('tree_data.csv', mode='w', newline='') as csv_file:
        cwriter = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        cwriter.writerow(field)

        for i in range(113): # should be # of cylinders
            pyautogui.hotkey('ctrl', 'c')
            title = pyperclip.paste()

            pyautogui.press('down') 
            pyautogui.hotkey('ctrl', 'c')
            value = pyperclip.paste()
            value = value.replace('(', '')
            value = value.replace(')', '')
            value = value.replace('Cylinder ', '')
            value = value.split('/')
            cylinder_list = [title] + re.findall(r'[+-]?\d+\.\d+', value[0]) + re.findall(r'[+-]?\d+\.\d+', value[1])
            cylinder_list.append(calculate_volume(cylinder_list[1], cylinder_list[2]))
            print(cylinder_list)
            cwriter.writerow(cylinder_list)
            pyautogui.press('down') 
            pyautogui.press('down') 
            pyautogui.press('down') 


def calculate_volume(radius, height):
    volume = math.pi * float(radius) ** 2 * float(height)
    return volume


if __name__ == "__main__":
    main()