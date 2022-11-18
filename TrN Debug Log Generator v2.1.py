__author__ = 'MnFeN'
__version__ = '2.1'

import re
from pyperclip import copy
import tkinter as tk
import tkinter.messagebox
from tkinter.ttk import *
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)                  #使用程序自身的dpi适配
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)     #获取屏幕的缩放因子

lang = '中文'

window = tk.Tk()
window.tk.call('tk', 'scaling', ScaleFactor/100)                #设置程序缩放


#默认全屏幕 70% 尺寸居中
screen_x = window.winfo_screenwidth()
screen_y = window.winfo_screenheight()
window.geometry('%dx%d+%d+%d' % (int(screen_x*0.7), int(screen_y*0.7), int(screen_x*0.15), int(screen_y*0.12)))

var_lang = tk.IntVar()
font = tk.StringVar()
text_header = tk.StringVar()
text_convert = tk.StringVar()
text_speed = tk.StringVar()
var_lang = tk.IntVar()
var_lang.set(0)

def lang_switch():
    lang = ['中文','English'][var_lang.get()]
    if lang == '中文':
        window.title('Triggernometry 调试日志生成器 v' + __version__ + ' by ' + __author__)
        text_header.set('在下方粘贴需要测试的日志行')
        text_convert.set('  转换！')
        text_speed.set('时间倍率')
    if lang == 'English':
        window.title('Triggernometry Debug Log Generator v' + __version__ + ' by ' + __author__)
        text_header.set('Paste the log lines to be tested below')
        text_convert.set(' Convert!')
        text_speed.set('Speed')
lang_switch()

def xml_convert():
    speed = entry_speed.get()
    try:
        speed = float(speed)
    except:
        if lang == '中文':
            tkinter.messagebox.showerror(title='', message = '【错误】时间倍率无法识别为数字。')
        if lang == 'English':
            tkinter.messagebox.showerror(title='', message = '【Error】Speed multiplier is not a number.')
    if speed <= 0:
        if lang == '中文':
            tkinter.messagebox.showerror(title='', message = '【错误】时间倍率必须为正数。')
        if lang == 'English':
            tkinter.messagebox.showerror(title='', message = '【Error】Speed multiplier should be positive.')
        return

    # 获取 log 文本框内从开始到终止的全部文本，每行存入列表
    log_text = log.get('1.0', 'end')  
    log_lines = log_text.split('\n')
    xml = '<TriggernometryExport><ExportedTrigger Name="Debug Log"><Actions>\n'
    if lang == '中文':
        note = '已复制 XML 到剪贴板，可在 Triggernometry 中粘贴导入'
    if lang == 'English':
        note = 'XML saved to clipboard. Paste in Triggernometry to import the trigger.'
    note_level = 0      #最终消息框的提示等级：0=info 1=warning 2=error
    OrderNumber = 0     #有效输入行计数，用于触发器
    line_count = 0      #总输入行计数
    
    for line in log_lines:
        line = line.strip('\n')
        line_count += 1

        if re.match(r'^\[\d{2}:\d{2}:\d{2}\.\d{3}\] ', line):
            re_line = re.match(r'^\[(?P<h>..):(?P<m>..):(?P<s>..\....)\] ', line)
            time = int(re_line.group("h")) * 3600 + int(re_line.group("m")) * 60 + float(re_line.group("s"))
            OrderNumber += 1
            
            if OrderNumber == 1:                #the first line
                dt = 0
            else:                               #time ∈ [time_prev, time_prev + 1 h]: correct
                dt = (time - time_prev + 86400 + 3600) % 86400 - 3600 
                if dt > 3600:                   #time ∈ (time_prev + 1 h, time_prev + 23 h)
                    if lang == '中文':
                        note += '\n【警告】第' + str(line_count) + '行"' + line + '" 行与上一行时间间隔较高：time = ' + str(time) + ' s; time_prev = ' + str(time_prev) + ' s'
                    if lang == 'English':
                        note += '\n【Warning】Line' + str(line_count) + ': "' + line + '" and the previous line has high time interval: time = ' + str(time) + ' s; time_prev = ' + str(time_prev) + ' s'
                    note_level = max(note_level, 1)
                elif dt < 0:                    #time ∈ [time_prev - 1 h, time_prev)
                    if lang == '中文':
                        note += '\n【错误】第' + str(line_count) + '行"' + line + '" 行早于上一行：time = ' + str(time) + ' s; time_prev = ' + str(time_prev) + ' s'
                    if lang == 'English':
                        note += '\n【Error】Line' + str(line_count) + ': "' + line + '" is earlier than the previous line: time = ' + str(time) + ' s; time_prev = ' + str(time_prev) + ' s'
                    note_level = 2
            
            dt /= speed
            xml += '<Action OrderNumber="' + str(OrderNumber) + '" '
            xml += 'LogMessageText="' + line + '\" '
            xml += 'LogProcess="True" ActionType="LogMessage" '
            xml += 'ExecutionDelayExpression="' + '{:.1f}'.format(dt) + ' * 1000" />\n'
            
            time_prev = time

        elif re.match(r'^ *$', line):
            continue
        else:
            if lang == '中文':
                note += '\n【错误】第' + str(line_count) + '行"' + line + '" 无法识别为 ACT 解析日志行格式，已跳过本行。'
            if lang == 'English':
                note += '\n【Error】Line' + str(line_count) + ': "' + line + '" does not match the ACT log line format. Skipped.'
            note_level = max(note_level, 1)
            
    xml += '</Actions></ExportedTrigger></TriggernometryExport>'
    copy(xml)
    if note_level == 0:
        tkinter.messagebox.showinfo(title='', message = note)
    elif note_level == 1:
        tkinter.messagebox.showwarning(title='', message = note)
    elif note_level == 2:
        tkinter.messagebox.showerror(title='', message = note)

#标题提示语
header = tk.Label(window, textvariable = text_header, font=('微软雅黑', 20,'bold'))
header.place(relx=0.1,relwidth=0.8,rely=0,relheight=0.1)

#输入log的文本框
log = tk.Text(window, font=('Consolas', 10), undo = True)
log.place(relx=0.1,relwidth=0.8,rely=0.1,relheight=0.75)
log.insert('end','[00:00:00.000] ChatLog 00:0038::XXX\n')
log.insert('end','[00:00:01.000] ChatLog 00:0038::YYY\n')
log.insert('end','[00:00:03.000] ChatLog 00:0038::ZZZ\n')

#时间倍率
tk.Label(window, textvariable=text_speed, font=('微软雅黑', 15,'bold'), width=200, height=1).place(relx=0.08,relwidth=0.08,rely=0.9,relheight=0.06)
entry_speed = tk.Entry(window, font=('Arial', 15), justify='center')
entry_speed.place(relx=0.16,relwidth=0.04,rely=0.91,relheight=0.04)
entry_speed.insert(0,'1')

#语言选项
tk.Radiobutton(window, text="中文", font=('微软雅黑','12','bold'), variable=var_lang, value=0, command=lang_switch).place(relx=0.75,relwidth=0.15,rely=0.9,relheight=0.03)
tk.Radiobutton(window, text="English", font=('Arial','12','bold'), variable=var_lang, value=1, command=lang_switch).place(relx=0.75,relwidth=0.15,rely=0.93,relheight=0.03)

#转换按钮
tk.Button(window, textvariable=text_convert, font=('微软雅黑', 20,'bold'), width=10, height=1, command=xml_convert).place(relx=0.42,relwidth=0.16,rely=0.9,relheight=0.06)

window.mainloop()