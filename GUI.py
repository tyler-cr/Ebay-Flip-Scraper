import PySimpleGUI as sg
import decider as dec
import lists
import pandas

'''
This is what runs the GUI, and what you run for the actual functionality of this program. Uses PySimpleGUI for GUI, and pandas as well for making the list windows.
'''

#the toggle button images as data
toggle_btn_off = b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAABmJLR0QA/wD/AP+gvaeTAAAED0lEQVRYCe1WTWwbRRR+M/vnv9hO7BjHpElMKSlpqBp6gRNHxAFVcKM3qgohQSqoqhQ45YAILUUVDRxAor2VAweohMSBG5ciodJUSVqa/iikaePEP4nj2Ovdnd1l3qqJksZGXscVPaylt7Oe/d6bb9/svO8BeD8vA14GvAx4GXiiM0DqsXv3xBcJU5IO+RXpLQvs5yzTijBmhurh3cyLorBGBVokQG9qVe0HgwiXLowdy9aKsY3g8PA5xYiQEUrsk93JTtjd1x3siIZBkSWQudUK4nZO1w3QuOWXV+HuP/fL85klAJuMCUX7zPj4MW1zvC0Ej4yMp/w++K2rM9b70sHBYCjo34x9bPelsgp/XJksZ7KFuwZjr3732YcL64ttEDw6cq5bVuCvgy/sje7rT0sI8PtkSHSEIRIKgCQKOAUGM6G4VoGlwiqoVd2Za9Vl8u87bGJqpqBqZOj86eEHGNch+M7otwHJNq4NDexJD+59RiCEQG8qzslFgN8ibpvZNsBifgXmFvJg459tiOYmOElzYvr2bbmkD509e1ylGEZk1Y+Ssfan18n1p7vgqVh9cuiDxJPxKPT3dfGXcN4Tp3dsg/27hUQs0qMGpRMYjLz38dcxS7Dm3nztlUAb38p0d4JnLozPGrbFfBFm79c8hA3H2AxcXSvDz7/+XtZE1kMN23hjV7LTRnKBh9/cZnAj94mOCOD32gi2EUw4FIRUMm6LGhyiik86nO5NBdGRpxYH14bbjYfJteN/OKR7UiFZVg5T27QHYu0RBxoONV9W8KQ7QVp0iXdE8fANUGZa0QAvfhhXlkQcmjJZbt631oIBnwKmacYoEJvwiuFgWncWnXAtuVBBEAoVVXWCaQZzxmYuut68b631KmoVBEHMUUrJjQLXRAQVSxUcmrKVHfjWWjC3XOT1FW5QrWpc5IJdQhDKVzOigEqS5dKHMVplnNOqrmsXqUSkn+YzWaHE9RW1FeXL7SKZXBFUrXW6jIV6YTEvMAUu0W/G3kcxPXP5ylQZs4fa6marcWvvZfJu36kuHjlc/nMSuXz+/ejxgqPFpuQ/xVude9eu39Jxu27OLvBGoMjrUN04zrNMbgVmOBZ96iPdPZmYntH5Ls76KuxL9NyoLA/brav7n382emDfHqeooXyhQmARVhSnAwNNMx5bu3V1+habun5nWdXhwJZ2C5mirTesyUR738sv7g88UQ0rEkTDlp+1wwe8Pf0klegUenYlgyg7bby75jUTITs2rhCAXXQ2vwxz84vlB0tZ0wL4NEcLX/04OrrltG1s8aOrHhk51SaK0us+n/K2xexBxljcsm1n6x/Fuv1PCWGiKOaoQCY1Vb9gWPov50+fdEqd21ge3suAlwEvA14G/ucM/AuppqNllLGPKwAAAABJRU5ErkJggg=='
toggle_btn_on = b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAABmJLR0QA/wD/AP+gvaeTAAAD+UlEQVRYCe1XzW8bVRCffbvrtbP+2NhOD7GzLm1VoZaPhvwDnKBUKlVyqAQ3/gAkDlWgPeVQEUCtEOIP4AaHSI0CqBWCQyXOdQuRaEFOk3g3IMWO46+tvZ+PeZs6apq4ipON1MNafrvreTPzfvub92bGAOEnZCBkIGQgZOClZoDrh25y5pdjruleEiX+A+rCaQo05bpuvJ/+IHJCSJtwpAHA/e269g8W5RbuzF6o7OVjF8D3Pr4tSSkyjcqfptPDMDKSleW4DKIggIAD5Yf+Oo4DNg6jbUBlvWLUNutAwZu1GnDjzrcXzGcX2AHw/emFUV6Sfk0pqcKpEydkKSo9q3tkz91uF5aWlo1Gs/mYc+i7tz4//19vsW2AU9O381TiioVCQcnlRsWeQhD3bJyH1/MiFLICyBHiuzQsD1arDvypW7DR9nzZmq47q2W95prm+I9fXfqXCX2AF2d+GhI98Y8xVX0lnxvl2UQQg0csb78ag3NjEeD8lXZ7pRTgftmCu4864OGzrq+5ZU0rCa3m+NzXlzvoAoB3+M+SyWQuaHBTEzKMq/3BMbgM+FuFCDBd9kK5XI5PJBKqLSev+POTV29lKB8rT0yMD0WjUSYLZLxzNgZvIHODOHuATP72Vwc6nQ4Uiw8MUeBU4nHS5HA6TYMEl02wPRcZBJuv+ya+UCZOIBaLwfCwQi1Mc4QXhA+PjWRkXyOgC1uIhW5Qd8yG2TK7kSweLcRGKKVnMNExWWBDTQsH9qVmtmzjiThQDs4Qz/OUSGTwcLwIQTLW58i+yOjpXDLqn1tgmDzXzRCk9eDenjo9yhvBmlizrB3V5dDrNTuY0A7opdndStqmaQLPC1WCGfShYRgHdLe32UrV3ntiH9LliuNrsToNlD4kruN8v75eafnSgC6Luo2+B3fGKskilj5muV6pNhk2Qqg5v7lZ51nBZhNBjGrbxfI1+La5t2JCzfD8RF1HTBGJXyDzs1MblONulEqPDVYXgwDIfNx91IUVbAbY837GMur+/k/XZ75UWmJ77ou5mfM1/0x7vP1ls9XQdF2z9uNsPzosXPNFA5m0/EX72TBSiqsWzN8z/GZB08pWq9VeEZ+0bjKb7RTD2i1P4u6r+bwypo5tZUumEcDAmuC3W8ezIqSGfE6g/sTd1W5p5bKjaWubrmWd29Fu9TD0GlYlmTx+8tTJoZeqYe2BZC1/JEU+wQR5TVEUPptJy3Fs+Vkzgf8lemqHumP1AnYoMZSwsVEz6o26i/G9Lgitb+ZmLu/YZtshfn5FZDPBCcJFQRQ+8ih9DctOFvdLIKHH6uUQnq9yhFu0bec7znZ+xpAGmuqef5/wd8hAyEDIQMjAETHwP7nQl2WnYk4yAAAAAElFTkSuQmCC'

#function that open news window. This allows us to use windows with identical loadouts without actually using the same ones
def open_window(layout):
    window = sg.Window("EBAY FLIPPER", layout, icon='ebaylogo.ico', element_justification= 'l', margins=(0,0), resizable= True, finalize = True)
    window.BringToFront()

#leftmost loadout
def splashl():
    return [[sg.InputText('INPUT ITEM HERE',enable_events=True,key = '-input-')],[sg.Text("", size=(45,1), key='-output-', pad=(5,10), background_color= 'white',text_color='black')],
            [sg.Submit('Average Price Sold'), sg.Submit('Quick Profit Calculator'), sg.Submit('Average Shipping Cost')],[sg.Submit('Current Average Price on Auction'),
             sg.Submit('Current Average Price on Buy Now')],
            [sg.Submit('Create Buy Now List'), sg.Submit('Create Auction List'), sg.Submit('Create Sold List') ]]

#loadout for when you make a list
def listl(item, bnacsol):
    if bnacsol == 'bn':
        headers = {'Name':lists.createnamelistbnact(item), 'Price':lists.createpricelistbnact(item)}
    elif bnacsol == 'ac':
        headers = {'Name':lists.createnamelistacact(item), 'Price':lists.createpricelistacact(item)}
    elif bnacsol == 'sol':
        headers = {'Name':lists.createnamelistacsold(item), 'Price':lists.createpricelistacsold(item)}
    table = pandas.DataFrame(headers)
    headings = list(headers)
    values = table.values.tolist()
    return [[sg.Table(values = values, headings = headings, expand_x=True, expand_y=True, font = ("Helvetica", 16))]]

#loadout for rightside 
def profl():
    return [[sg.Submit('Profit Based off Buy'), sg.Submit('Profit Based off Sell')],
            [sg.Text('By Dollar'),
            sg.Button(image_data=toggle_btn_off, key='-TOGGLE-GRAPHIC-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, metadata=False),
            sg.Text('By Percent')],
            [sg.InputText('INPUT DESIRED BUY/SELL PRICE',enable_events=True,key = '-BSinput-')],
            [sg.InputText('DOLLAR/PERCENT HERE',size = (22, 1),enable_events=True,key = '-DPinput-'), sg.InputText('SHIPPING HERE',size = (21, 1), enable_events=True,key = '-SHinput-')],
            [sg.Text('', key='-PROFIT-', size=(45,1), background_color= 'white',text_color='black')]]

#setting up the main window.
sg.ChangeLookAndFeel('black')
layout = [[sg.Column(splashl()), sg.Column(profl())]]
window= sg.Window("EBAY FLIPPER", layout, icon='ebaylogo.ico', element_justification= 'l', margins=(0,0), resizable= True, finalize = True)


#open up the window
while True:
    event, values = window.read()
    #changes the image and the bool value of the button when it is pressed. This is used for finding profit with dollar or percent
    if event == '-TOGGLE-GRAPHIC-':  # if the graphical button that changes images
        window['-TOGGLE-GRAPHIC-'].metadata = not window['-TOGGLE-GRAPHIC-'].metadata
        window['-TOGGLE-GRAPHIC-'].update(image_data=toggle_btn_on if window['-TOGGLE-GRAPHIC-'].metadata else toggle_btn_off)
        
    #most of these buttons are self explanitory.
    if event == 'Average Price Sold':
        window['-output-'].update(round(dec.getavg(lists.createpricelistacsold(values['-input-'])),2))
    if event == 'Quick Profit Calculator':
        window['-output-'].update(value=dec.needforprofit(values['-input-']))
    if event == 'Current Average Price on Auction':
        window['-output-'].update(value=dec.getavg(lists.createpricelistacact(values['-input-'])))
    if event == 'Current Average Price on Buy Now':
        window['-output-'].update(value=dec.getavg(lists.createpricelistbnact(values['-input-'])))
    if event == 'Average Shipping Cost':
        window['-output-'].update(value=dec.getavg(lists.createshippinglistacsold(values['-input-'])))
    if event == 'Create Buy Now List':
        open_window(listl(values['-input-'], 'bn'))
    if event == 'Create Auction List':
        open_window(listl(values['-input-'], 'ac'))
    if event == 'Create Sold List':
        open_window(listl(values['-input-'], 'sol'))

    #these are for displaying profitability on the right side. Looks at buy/sell button, and bool value of dollar / percent button
    if event == 'Profit Based off Buy' and not window['-TOGGLE-GRAPHIC-'].metadata:
        window['-PROFIT-'].update(value=dec.finddesiredprofper(float(values['-BSinput-']), float(values['-SHinput-']), 1+ float(values['-DPinput-'])*.01))
    if event == 'Profit Based off Buy' and window['-TOGGLE-GRAPHIC-'].metadata:
        window['-PROFIT-'].update(value=dec.finddesiredprofdol(float(values['-BSinput-']), float(values['-SHinput-']), float(values['-DPinput-'])))
    if event == 'Profit Based off Sell' and not window['-TOGGLE-GRAPHIC-'].metadata:
        window['-PROFIT-'].update(value=dec.buypricedesiredprofdol(float(values['-BSinput-']), float(values['-SHinput-']), float(values['-DPinput-'])))
    if event == 'Profit Based off Sell' and window['-TOGGLE-GRAPHIC-'].metadata:
        window['-PROFIT-'].update(value=dec.buypricedesiredprofper(float(values['-BSinput-']), float(values['-SHinput-']), 1+ float(values['-DPinput-'])*.01))

    #kills the window
    if event == 'OK' or event == sg.WIN_CLOSED:
        break
window.close()
