__author__ = 'MnFeN'
__version__ = '2.0'

import re
import pyperclip
import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("Triggernometry 调试日志生成器 v" + __version__ + " by MnFeN")
window.geometry('1500x800')


header = tk.Label(window, text = '在下方粘贴需要测试的日志行', font=('微软雅黑', 20), width=200, height=3)
header.pack()

def xml_convert():
    log_text = log.get('1.0', 'end')
    log_lines = log_text.split('\n')

    xml = '<TriggernometryExport><ExportedTrigger Name="调试日志"><Actions>\n'
    note = '已复制 XML 到剪贴板，可在 Triggernometry 中粘贴导入'
    note_level = 0
    OrderNumber = 0
    line_count = 0
    
    for line in log_lines:
        line = line.strip('\n')
        line_count += 1
        
        if re.match(r'^\[\d{2}:\d{2}:\d{2}\.\d{3}\] ', line):
            re_line = re.match(r'^\[(?P<h>..):(?P<m>..):(?P<s>..\....)\] ', line)
            time = int(re_line.group("h")) * 3600 + int(re_line.group("m")) * 60 + float(re_line.group("s"))
            OrderNumber += 1
            
            if OrderNumber == 1:                #是第一行
                dt = 0
            else:                               #正常：时间 ∈ [上行时间, 上行时间 + 1 h] 
                dt = (time - time_prev + 86400 + 3600) % 86400 - 3600 
                if dt > 3600:                   #时间 ∈ (上行时间 + 1 h, 上行时间 + 23 h)
                    note += '\n【警告】第' + str(line_count) + '行"' + line + '" 行与上一行时间间隔较高：time = ' + str(time) + ' s; time_prev = ' + str(time_prev) + ' s'
                    note_level = max(note_level, 1)
                elif dt < 0:                    #时间 ∈ [上行时间 - 1 h, 上行时间)
                    note += '\n【错误】第' + str(line_count) + '行"' + line + '" 行早于上一行：time = ' + str(time) + ' s; time_prev = ' + str(time_prev) + ' s'
                    note_level = 2
            
            xml += '<Action OrderNumber="' + str(OrderNumber) + '" '
            xml += 'LogMessageText="' + line + '\" '
            xml += 'LogProcess="True" ActionType="LogMessage" '
            xml += 'ExecutionDelayExpression="' + '{:.1f}'.format(dt) + ' * 1000" />\n'
            
            time_prev = time

        elif re.match(r'^ *$', line):
            continue
        else:
            note += '\n【错误】第' + str(line_count) + '行"' + line + '" 无法识别为 ACT 解析日志行格式，已跳过本行。'
            note_level = max(note_level, 1)
            
    xml += '</Actions></ExportedTrigger></TriggernometryExport>'
    pyperclip.copy(xml)
    if note_level == 0:
        tkinter.messagebox.showinfo(title='', message = note)
    elif note_level == 1:
        tkinter.messagebox.showwarning(title='', message = note)
    elif note_level == 2:
        tkinter.messagebox.showerror(title='', message = note)
        
log = tk.Text(window, width=200, height=40, undo = True)
log.pack()

blank = tk.Label(window, text = '', font=('微软雅黑', 20), width=200, height=1)
blank.pack()

button_convert = tk.Button(window, text='  转换！', font=('微软雅黑', 20), width=10, height=1, command=xml_convert)
button_convert.pack()

window.mainloop()
