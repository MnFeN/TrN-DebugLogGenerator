**该程序已经使用 C# 重写，并集成到 Triggernometry 1.2.0.7+ 中，用户无需再单独使用此程序。**  

---  

# Triggernometry 调试日志生成器
本工具用于生成模拟战斗的触发器，以供其它 Triggernometry 触发器调试。  
当你写好副本触发器后，可用本工具模拟副本战斗中的日志，免于实际进入副本战斗测试。
     
## · 触发器设置
- ACT - Triggernometry - 选项 - 编辑配置 - 其它：
     - [x] 开发者模式
     - [x] 使用操作系统剪贴板

## · 使用说明
1. 从项目主页右侧 [Releases](https://github.com/MnFeN/TrN-DebugLogGenerator/releases) 下载最新的 exe 程序。打开后应如下图所示：  

<div align=center>
    <img src="https://user-images.githubusercontent.com/85232361/202853243-4be82906-893b-4795-b534-e78c56b552a3.png" height="300px">
</div>

2. 在战斗记录中正则搜索待测试的机制的相关日志（详见下文：如何搜索机制相关的日志），复制结果并粘贴到程序中；

3. 设置速度倍率，默认为 1，必须为正数。该数值代表生成的调试日志的速度会加快到几倍。以下方两行日志为例：
    ```
    [19:36:55.279] StartsCasting 14:40024364:Hephaistos:79DC:Orogenic Shift:......
    [19:37:01.279] StartsCasting 14:4002435D:Hephaistos:79DC:Orogenic Shift:......
    ```
    在默认速度倍率 `1` 下，生成的调试日志的时间间隔与日志起始的时间间隔相同（6.0 s）。  
    当设置速度倍率 `3` 时，则调试日志会加快到 3 倍（时间间隔 2.0 s）。  
4. 转换。  
    若提示有错误，返回检查输入的日志是否存在格式、时间顺序等问题。  
    若提示无错误，生成的调试触发器 xml 会复制到系统剪贴板。
5. 在 Triggernometry 中直接接粘贴触发器，右键 - 执行 开始模拟副本机制，测试触发器是否正常工作。  

## · 如何搜索机制相关的日志
1. 找到所有触发器的正则。 
例：我在写龙诗 P5 二运检测谁站歪导致吃天火/圣锁的触发器。所有触发器包含以下内容的检测：索尼图标点名、天火判定、圣锁判定、二运读条。下面是对应的正则（省略了后面与搜索无关的玩家名与坐标等内容）：
    - 索尼点名：`^.{15}\S+ 1B:` 
    - 圣锁判定：`^.{15}\S+ 1[56]:4.{7}:[^:]+:62E0:`
    - 天火判定：`^.{15}\S+ 1[56]:4.{7}:[^:]+:62DF:`
    - 二运读条：`^.{15}\S+ 14:4.{7}:[^:]+:6B92:`
2. 复制全部正则，以 `|` 隔开（不加空格）。右键 ACT 主页的战斗记录，查看 ACT 战斗日志，粘贴合并的正则并以正则搜索。
例：合并后的正则如下：   
`^.{15}\S+ 1B:|^.{15}\S+ 1[56]:4.{7}:[^:]+:62E0:|^.{15}\S+ 1[56]:4.{7}:[^:]+:62DF:|^.{15}\S+ 14:4.{7}:[^:]+:6B92:`  
在战斗记录中搜索：
<div align=center>
    <img src="https://user-images.githubusercontent.com/85232361/202985528-8323b5b1-1fc5-442a-99ba-29490fe9cba4.png" height="300px">
</div>  

3. 复制所有搜索结果，在本工具中粘贴。删除全部与机制无关的日志行，有需要的话可以调整日志行的时间。
例：在二运范围外的全部 `TargetIcon 1B` 点名日志行与机制无关，只保留二运期间的点名。故以下为我需要的全部用于测试的日志行：
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

## · 注意事项
1. 时间轴根据日志前的时间 `[hh:mm:ss.xxx]` 自动生成，部分日志行（如 00 03 04）的时间不准确，可能需要手动更改；
2. 只能模拟日志行，不能模拟实体。如果触发器存在 `${_ffxiventity[玩家名].job}` `${_ffxiventity[40123456].hp}` 之类调用实体信息的写法，会因无法找到实体而无法正常工作；  
（或者也可以想些办法，比如用了实体坐标，可以把待测试的对象的 ID 换成你或其他人的 ID，然后站在对应的位置上开启调试）
3. 如果待调试的触发器的分组限制了地图 ID 或地图名，调试前关掉对应选项。
4. Tips: 可以新建一个触发器，如下图所示。这样在游戏中就可以用自定义的 `/e xml` 指令快捷启动这个工具。
<div align=center>
    <img src="https://user-images.githubusercontent.com/85232361/202989911-b760ae4c-2570-4548-bbfd-db14c35def7e.png" height="200px">
</div>  

## · To-do List
- 增加网络日志行的支持
- 优化图形界面

## · NGA 发布页
https://nga.178.com/read.php?&tid=33617575
