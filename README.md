# Triggernometry Debug Log Generator

[阅读中文说明文档 (Read the document in Chinese)](https://github.com/MnFeN/TrN-DebugLogGenerator/blob/main/README-CN.md)

本工具用于生成模拟战斗的触发器，以供其它 Triggernometry 触发器调试。  
当你写好副本触发器后，可用本工具模拟副本战斗中的日志，免于实际进入副本战斗测试。
     
### · 触发器设置
ACT - Triggernometry - 选项 - 编辑配置 - 其它：
- [x] 开发者模式
- [x] 使用操作系统剪贴板

### · 使用说明
1. 从右侧 [Releases](https://github.com/MnFeN/TrN-DebugLogGenerator/releases) 下载最新的 exe 程序。打开后应如下图所示：  

<div align=center>
    <img src="https://user-images.githubusercontent.com/85232361/202853243-4be82906-893b-4795-b534-e78c56b552a3.png" height="300px">
</div>

2. 在战斗记录中正则搜索待测试的机制的相关日志，复制结果并粘贴到程序中；

3. 设置速度倍率，默认为 1，必须为正数。该数值代表生成的调试日志的速度会加快到几倍。以下方两行日志为例：
    ```
    [19:36:55.279] StartsCasting 14:40024364:Hephaistos:79DC:Orogenic Shift:......
    [19:37:01.279] StartsCasting 14:4002435D:Hephaistos:79DC:Orogenic Shift:......
    ```
    在默认速度倍率 `1` 时，生成的调试日志的时间间隔与日志起始的时间间隔相同（6.0 s）。  
    若速度倍率设为 `3` 时，则调试日志会加快到 3 倍（时间间隔 2.0 s）。  
4. 转换。  
    若提示有错误，返回检查输入的日志是否存在格式、时间顺序等问题。  
    若提示无错误，生成的调试触发器 xml 会复制到系统剪贴板。
5. 在 Triggernometry 中直接接粘贴触发器，右键 - 执行 开始模拟副本机制，测试触发器是否正常工作。  


### · 注意事项
1. 时间轴根据日志前的时间自动生成，部分日志行（如 00 03 04）的时间不准确，可能需要手动更改；
2. 只能模拟日志行，不能模拟实体。如果触发器存在 _ffxiventity 之类调用实体坐标、队友职业的写法，无法正常工作；  
(或者也可以想些办法，比如用了实体坐标，可以把待测试的对象的 ID 换成你或其他人的 ID，然后站在对应的位置上开启调试)
3. 如果待调试的触发器的分组限制了地图 ID 或地图名，调试前关掉对应选项。

### · NGA 发布页
https://nga.178.com/read.php?&tid=33617575
