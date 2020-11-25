# wechat-miniprogram-icons
A tool for converting SVG icons to wechat miniprogram components.
Besides, there're some open source icons that I have converted in the *dist* directory.
Feel free to use them.

这是一个把SVG格式的icon转换成微信小程序组件的工具，另外我已经转换好了一些开源的SVG图标放在了*dist*目录下，可以直接拷贝到项目中使用。

## USAGE
1. Create sub folder with project name in *svg-icons*.
2. Create sub folders with icon's type name like *filled*, *outline* and *sharp* etc.
3. Put SVG files into the right folders.
4. Execute `python Convert.py` to generate wechat miniprogram component.
5. Copy the component in the *dist* folder to your wechat miniprogram project.

## 用法
1. 在*svg-icons*目录下建一个子目录，可以用开源icon项目的名称命名，比如eva-icon, fontawesome等。
2. 然后在项目文件夹下建立*filled*, *outline*, *sharp*等文件夹，用来放不同风格的icon文件。
3. 把想要转换的svg文件放到对应的文件夹里。
4. 执行`python Convert.py`即可。
5. 在*dist*目录下找到生成好的组件复制到小程序项目即可使用。

## CREDITS
* [Eva Icons](https://github.com/akveo/eva-icons)
* [WeUI](https://github.com/Tencent/weui-wxss/)