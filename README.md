# Triggernometry Debug Log Generator

[阅读中文说明文档 (Read the document in Chinese)](https://github.com/MnFeN/TrN-DebugLogGenerator/blob/main/README-CN.md)

This tool can simulate raid mechanisms by generating debug triggers.  
Once you've written triggers for a mechanism, you can use this tool to simulate raid logs and test your triggers without actually entering the raid instance.   

### · Triggernometry Settings
ACT - Triggernometry - Options - Edit Configuration - Miscellaneous:
- [x] Use operating system clipboard
- [x] Developer mode

### · Instructions
1. Down the exe file from the [Releases](https://github.com/MnFeN/TrN-DebugLogGenerator/releases) on the right of this page. After running, it should look like this:  
<div align=center>
    <img src="https://user-images.githubusercontent.com/85232361/202853243-4be82906-893b-4795-b534-e78c56b552a3.png" height="300px">
</div>

2. Use regular expressions to search all logs related with the mechanism in the ACT battle log. Copy the results and paste into the program;  

3. Set the speed multiplier. This value represents how many times faster the generated debug logs will be. Take the following two log lines as an example:
    ```
    [19:36:55.279] StartsCasting 14:40024364:Hephaistos:79DC:Orogenic Shift:......
    [19:37:01.279] StartsCasting 14:4002435D:Hephaistos:79DC:Orogenic Shift:......
    ```
    At the default speed multiplier of `1`, debug logs would have the same time interval as the log lines (6.0 s time interval).
    If the speed multiplier is set to `3`, it will be accelerated to 3× speed (2.0 s time interval).
4. Convert
    If there is an error, check whether the input log has format, time order or other problems.
    If there is no error, the generated debug trigger XML will be copied to the system clipboard.
5. Paste the trigger XML directly into Triggernometry. Right click - Fire to simulate the raid mechanism and test if your triggers work.  


### · 注意事项
1. 时间轴根据日志前的时间自动生成，部分日志行（如 00 03 04）的时间不准确，可能需要手动更改；
2. 只能模拟日志行，不能模拟实体。如果触发器存在 _ffxiventity 之类调用实体坐标、队友职业的写法，无法正常工作；  
(或者也可以想些办法，比如用了实体坐标，可以把待测试的对象的 ID 换成你或其他人的 ID，然后站在对应的位置上开启调试)
3. 如果待调试的触发器的分组限制了地图 ID 或地图名，调试前关掉对应选项。
