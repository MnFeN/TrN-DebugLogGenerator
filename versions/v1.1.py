import re
from xml.dom.minidom import Document
import pyperclip

print("============================================================")
print("日志调试XML生成器 v1.0 by MnFeN")

while 1:
    print("============================================================")

    try:
        tl_file = open("在此存储需要转换的日志行.txt", encoding='UTF-8')
    except FileNotFoundError:
        print("【错误】 同目录下 \"在此存储需要转换的日志行.txt\" 文件不存在。（按回车重试）")
        input("============================================================")
        continue
    prev_time = -99999

    xml = "<TriggernometryExport><ExportedTrigger Name=\"调试日志\"><Actions>\n"
    count = 0

    for line in tl_file:
        line = line.strip('\n')
        if re.match(r'^\[\d{2}:\d{2}:\d{2}\.\d{3}\] ', line):
            re_line = re.match(r'^\[(?P<h>..):(?P<m>..):(?P<s>..\....)\] ', line)
            time = int(re_line.group("h")) * 3600 + int(re_line.group("m")) * 60 + float(re_line.group("s"))
            count += 1
            if prev_time == -99999:
                dt = 0
            elif time >= prev_time:
                dt = time - prev_time
            elif (time <= 120) and (time < prev_time) and (time + 86400 - prev_time <= 120):
                dt = time + 86400 - prev_time
            else:
                dt = time - prev_time
                print("\"" + line + "\" 行时间异常：time = " + str(time) +"; prev_time = " + str(prev_time))
            xml += "<Action OrderNumber=\"" + str(count) + "\" LogMessageText=\"" + line + "\" LogProcess=\"True\" ActionType=\"LogMessage\" ExecutionDelayExpression=\"" + "{:.1f}".format(dt) + " * 1000\" />\n"
            prev_time = time
    
        elif re.match(r'^ *$', line):
            continue
        else:
            print("【警告】 \"" + line + "\" 无法识别为 ACT 解析日志行格式，已跳过本行。")
    tl_file.close()
    xml += "</Actions></ExportedTrigger></TriggernometryExport>"
    pyperclip.copy(xml)
    input("已复制 XML 到剪贴板，按回车继续\n")

