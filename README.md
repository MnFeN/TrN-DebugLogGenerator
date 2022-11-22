# Triggernometry Debug Log Generator

[阅读中文说明文档 (Read the document in Chinese)](https://github.com/MnFeN/TrN-DebugLogGenerator/blob/main/README-CN.md)

This tool can simulate raid mechanisms by generating debug triggers.  
Once you've written triggers for a mechanism, you can use this tool to simulate raid logs and test your triggers without actually entering the raid instance.   

## · Triggernometry Settings
ACT - Triggernometry - Options - Edit Configuration - Miscellaneous:
- [x] Use operating system clipboard
- [x] Developer mode

## · Instructions
1. Down the .exe file from the [Releases](https://github.com/MnFeN/TrN-DebugLogGenerator/releases) on the right side of this page. After running, it should look like this:  
<div align=center>
    <img src="https://user-images.githubusercontent.com/85232361/202977407-dc2a1ea3-c820-49e9-9e4a-4d5190d51dce.png" height="300px">
</div>

2. Use regular expressions to search all logs related to the mechanism in the ACT battle log (check below for details). Copy the results and paste them into the program;  

3. Set the speed multiplier. This value represents how many times faster the generated debug logs will be. Take the following two log lines as an example:
    ```
    [19:36:55.279] StartsCasting 14:40024364:Hephaistos:79DC:Orogenic Shift:......
    [19:37:01.279] StartsCasting 14:4002435D:Hephaistos:79DC:Orogenic Shift:......
    ```
    At the default speed multiplier of `1`, debug logs would have the same time interval (6.0 s) as the log lines.  
    If the speed multiplier is set to `3`, it will be accelerated to 3× speed (2.0 s time interval).
4. Convert
    If there is an error: check whether the input log has some problem in format, time order, *etc.*.  
    If there is no error, the generated debug trigger XML will be copied to the system clipboard.
5. Paste the trigger XML directly into Triggernometry. Right-click - Fire to simulate the raid mechanism and test if your triggers work.  

## · How to search for log lines related to your triggers
1. Find all your trigger regexes.  
_e.g._ I am writing a trigger for detecting who went to the wrong side in DSR P5 Death of the heavens. My triggers include the Playstation Headmarkers, Heavensflame, Holy Chain, and the casting of Death of the Heavens. The regexes are shown below (shortened to omit other info not relevant to the search):
    - PS markers:               `^.{15}\S+ 1B:`
    - Holy chain:               `^.{15}\S+ 1[56]:4.{7}:[^:]+:62E0:`
    - Heavensflame:             `^.{15}\S+ 1[56]:4.{7}:[^:]+:62DF:`
    - Death of the heavens:     `^.{15}\S+ 14:4.{7}:[^:]+:6B92:`
2. Copy and separate the regexes with `|` (no whitespace). Right-click the battle, view ACT battle logs, paste the combined regexes, and search with regex.  
_e.g._ Combined regex:   
`^.{15}\S+ 1B:|^.{15}\S+ 1[56]:4.{7}:[^:]+:62E0:|^.{15}\S+ 1[56]:4.{7}:[^:]+:62DF:|^.{15}\S+ 14:4.{7}:[^:]+:6B92:`  
Search in the battle log:  
<div align=center>
    <img src="https://user-images.githubusercontent.com/85232361/202985528-8323b5b1-1fc5-442a-99ba-29490fe9cba4.png" height="300px">
</div>  

3. Copy all results, and paste them into this tool. Delete the irrelevant log lines, and adjust the time if needed.  
_e.g._ All `TargetIcon 1B` lines before the casting of Death of the heavens are not related to this mechanism, and only the later ones are retained. So below are all the  log lines I need for testing my triggers:  
    ```
    [20:20:40.985] StartsCasting 14:40009EBA:King Thordan:6B92:Death of the Heavens:...
    [20:21:10.039] TargetIcon 1B:106A2F62:Player Name:0000:C025:019F:0000:0000:0000
    [20:21:10.039] TargetIcon 1B:106B72C6:Player Name:0000:C025:019F:0000:0000:0000
    [20:21:10.039] TargetIcon 1B:106C441A:Player Name:0000:C025:01A0:0000:0000:0000
    [20:21:10.039] TargetIcon 1B:106B0FBF:Player Name:0000:C025:01A0:0000:0000:0000
    [20:21:10.039] TargetIcon 1B:1081F1E4:Player Name:0000:C025:01A1:0000:0000:0000
    [20:21:10.039] TargetIcon 1B:1088D65D:Player Name:0000:C025:01A1:0000:0000:0000
    [20:21:10.039] TargetIcon 1B:106BF5B3:Player Name:0000:C025:01A2:0000:0000:0000
    [20:21:10.039] TargetIcon 1B:1068ED1C:Player Name:0000:C025:01A2:0000:0000:0000
    [20:21:17.745] ActionEffect 15:40009770:Ser Charibert:62DF:Heavensflame:106A2F62:...
    [20:21:17.745] ActionEffect 15:40009771:Ser Charibert:62DF:Heavensflame:106C441A:...
    [20:21:17.745] ActionEffect 15:40009772:Ser Charibert:62DF:Heavensflame:106B0FBF:...
    [20:21:17.745] ActionEffect 15:40009773:Ser Charibert:62DF:Heavensflame:1088D65D:...
    [20:21:17.745] ActionEffect 15:40009774:Ser Charibert:62DF:Heavensflame:106BF5B3:...
    [20:21:17.745] ActionEffect 15:40009775:Ser Charibert:62DF:Heavensflame:1081F1E4:...
    [20:21:17.745] ActionEffect 15:40009776:Ser Charibert:62DF:Heavensflame:106B72C6:...
    [20:21:17.745] ActionEffect 15:40009777:Ser Charibert:62DF:Heavensflame:1068ED1C:...
    ```


## · Notes
1. The debug XML timeline is generated according to the timestamp `[hh:mm:ss.xxx]` before each log line. Some types of log lines (like `00` `03` `04`) have inaccurate timestamps and might need to adjust manually.
2. This tool can only simulate log lines, not entity data. If your trigger contains functions that call an entity property, such as `${_ffxiventity[10123456].job}` `${_ffxiventity[Player Name].hp}`, it would not work properly because no such entity could be found.    
(Or you can use other ways instead, such as replacing the ID of the object to be tested with your or someone else's ID, and then standing at the corresponding position to start debugging.)
3. If your raid triggers are in a folder that restricts the raid Zone ID / Zone name, turn off those options when testing.
4. Tips: You can add a trigger to run this tool by a pseudo "in-game command", as shown below.  
Then you can enter `/e xml` in the game to run this tool.

<div align=center>
    <img src="https://user-images.githubusercontent.com/85232361/202990189-97df6ef0-f45a-43fc-824b-3baea42cb572.png" height="200px">
</div>  
