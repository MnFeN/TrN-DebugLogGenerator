# Triggernometry Debug Log Generator

[阅读中文说明文档 (Read the document in Chinese)](https://github.com/MnFeN/TrN-DebugLogGenerator/blob/main/README-CN.md)

This tool can simulate raid mechanisms by generating debug triggers.  
Once you've written triggers for a mechanism, you can use this tool to simulate raid logs and test your triggers without actually entering the raid instance.   

### · Triggernometry Settings
ACT - Triggernometry - Options - Edit Configuration - Miscellaneous:
- [x] Use operating system clipboard
- [x] Developer mode

### · Instructions
1. Down the exe file from the [Releases](https://github.com/MnFeN/TrN-DebugLogGenerator/releases) on the right side of this page. After running, it should look like this:  
<div align=center>
    <img src="https://user-images.githubusercontent.com/85232361/202977407-dc2a1ea3-c820-49e9-9e4a-4d5190d51dce.png" height="300px">
</div>

2. Use regular expressions to search all logs related with the mechanism in the ACT battle log. Copy the results and paste into the program;  

3. Set the speed multiplier. This value represents how many times faster the generated debug logs will be. Take the following two log lines as an example:
    ```
    [19:36:55.279] StartsCasting 14:40024364:Hephaistos:79DC:Orogenic Shift:......
    [19:37:01.279] StartsCasting 14:4002435D:Hephaistos:79DC:Orogenic Shift:......
    ```
    At the default speed multiplier of `1`, debug logs would have the same time interval (6.0 s) as the log lines.  
    If the speed multiplier is set to `3`, it will be accelerated to 3× speed (2.0 s time interval).
4. Convert
    If there is an error: check whether the input log has problem in format, time order, *etc.*.  
    If there is no error, the generated debug trigger XML will be copied to the system clipboard.
5. Paste the trigger XML directly into Triggernometry. Right click - Fire to simulate the raid mechanism and test if your triggers work.  


### · Notes
1. The debug xml timeline is generated according to the timestamp `[hh:mm:ss.xxx]` before each log line. Some types of log lines (like `00` `03` `04`) have inaccurate timestamp, might need to adjust manually.
2. This tool can only simulate log lines, not entity data. If your trigger contains functions which calls an entity properties, such as `${_ffxiventity[10123456].job}` `${_ffxiventity[Player Name].hp}`, it would not work properly because no such entity could be found.    
(Or you can use other ways instead, such as replacing the ID of the object to be tested with your or someone else's ID, and then stand at the corresponding position to start debugging.)
3. If your raid triggers are in a folder which restricts the raid Zone ID / Zone name, turn off those options when testing.
4. Tips: You can add a trigger to run this tool by a psudeo "in-game command", as shown below.  
Then you can enter `/e xml` in game to run this tool.
<div align=center>
    <img src="https://user-images.githubusercontent.com/85232361/202975668-4f98aa3b-ce8d-40ee-a517-64850800fa86.png" height="200px">
</div>




