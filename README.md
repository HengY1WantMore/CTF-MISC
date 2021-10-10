## 一个菜鸡🫑的自述

> 这里是我记录自己打CTF-杂项的记录
>
> 然在**维护中～**
>
> 最新更新时间：2021-10-10

## 思维导图:sailboat:

> 备注：出现番号的就是存在脚本的

![ctf-杂项-思维导图](https://github.com/hengyi666/CTF-MISC/blob/main/ctf-%E6%9D%82%E9%A1%B9-%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE.png)

##  大神脚本/小改脚本:footprints:

- 认识图片并且二进制转回来
- 协议流量分析
- 十六进制与ASCII
- 爬取多目标网页PDF文件并下载到指定目录
- pdf转txt并且寻找密码

##  在线网站合集:computer:

- ASCII编码在线转换  https://www.qqxiuzi.cn/bianma/ascii.htm
- 二进制转为字符  http://tool.huixiang360.com/str/from-binary.php
- 佛曰解密  https://www.keyfc.net/bbs/tools/tudoucode.aspx
- rot13等解加密  http://www.mxcz.net/tools/rot13.aspx
- 摩斯密码在线翻译  http://moersima.00cha.net/

##  小工具:tophat:

- 检测 PNG 和 BMP 中隐藏的隐写数据 **[zsteg](https://github.com/zed-0xff/zsteg)**  
- 伪加密压缩包 **[ZipCenOp](https://github.com/hengyi666/CTF-MISC/blob/main/%E5%B7%A5%E5%85%B7%E5%8C%85/ZipCenOp.jar)**
- jar反编译 **[Bytecode-Viewer](https://github.com/hengyi666/CTF-MISC/blob/main/%E5%B7%A5%E5%85%B7%E5%8C%85/Bytecode-Viewer-2.10.16.jar)**
- 图片处理  **[stegsolve-macos](https://github.com/hengyi666/CTF-MISC/blob/main/%E5%B7%A5%E5%85%B7%E5%8C%85/crark52-mac-opencl-rar.zip)** 
- RAR密码破解工具 **[crark52](https://github.com/hengyi666/CTF-MISC/blob/main/%E5%B7%A5%E5%85%B7%E5%8C%85/stegsolve.jar)**

##  做题姿势分享:zap:

###  前言：

> 鄙人为一名涉及全栈，爬虫，安全的小小工程师
>
> 以下都是我的做题感悟：
>
> **肯定是不全的**！！毕竟题量的少是摆在哪里的！
>
> 但是分享出来，大家一起进步！

###  第一步：获取信息

> 做杂项第一步肯定会给你个东西，这些东西可能是：
>
> 1. 一个压缩文件
> 2. 一个流量取证的文件
> 3. 一张图片
> 4. 一串报文
> 5. 一个pdf
> 6. 一个jar

###  第二步：经验与摸索

> 根据**思维导图**我已经在更新啦！！
>
> 打个简单的比方：（注意是比方！）
>
> 我拿到了一张**图片**
>
> ------
>
> **首先：**
>
> 我会先拿010Editor看看16进制
>
> 1. 格式是否正确
> 2. 开头结尾是否暗藏什么
> 3. 是否存在flag字眼
>
> **其次：**
>
> 根据类型去想方向：
>
> - gif  可能会一帧帧中存在flag 或者二维码残缺
> - png 可能会存在图片藏文件
> - ....
>
> **然后：**
>
> 就是根据聪明才智去处理分析拿到的东西
>
> [^东西]: 可能是二进制，可能是base，可能是二维码，可能。。。

###  拿到flag

> 祝愿各位ctf选手不要死在最后一步！
>
> - 最简单的直接给你
> - base转码给你
> - 各种解密 反复解密拿到
> - 图片上面写的
> - 扫二维码的
> - 拼凑出来的
> - ...

##  文件处理类:dove:

### 文件类型识别

#### Kail 内置

`file xxx`   查看文件类型

#### 010Editor

- 根据文件头判断类型

<img src="https://github.com/hengyi666/CTF-MISC/blob/main/%E5%B8%B8%E8%A7%81%E6%96%87%E4%BB%B6%E5%A4%B4.png" alt="image-20211010170221882" style="zoom:10%;float:left "/>

- 根据文件后缀补充文件头
- 根据文件尾部补充文件信息与类型
  - zip文件的结尾以一串504B0506**开始**
  - rar文件以C43D7B00400700**结尾**
  - JPG文件FFD9**结尾**
  - PNG文件 000049454E44AE426082**结尾**
  - Gif文件为3B**结尾**

### 文件分离

#### Binwalk

> Binwalk是一个自动提取文件系统。
>
> 该工具最大的优点就是可以自动完成指定文件的扫描，智能发掘潜藏在文件中所有可疑的文件类型及文件系统。

1. Binwalk分析文件

> binwalk +file 通过扫描能够发现目标文件中包含的所有可识别的文件类型。
>
> 比如 binwalk 1.jpg 可以发现里面内置一个zip文件

2. Binwalk提取文件

> binwalk +file -e

#### foremost(偏爱)

> foremost是基于文件开始格式，文件结束标志和内部数据结构进行恢复文件的程序。

1. foremost提取文件

> foremost file –o 输出目录名

#### dd

> dd这个工具是一种半自动化工具👇

<details>
    <summary>点击查看<code>详细使用法则</code></summary>
<pre><codes>
dd if=源文件名 bs=1 skip=开始分离的字节数 of=目标文件名
<strong>参数说明</strong>：
if=file #输入文件名，缺省为标准输入。 
of=file #输出文件名，缺省为标准输出。 
bs=bytes #同时设置读写块的大小为 bytes ，可代替 ibs 和 obs 。 
skip=blocks #从输入文件开头跳过 blocks 个块后再开始复制。</hr> 
以IDF实验室“抓到一只苍蝇”为例，需要将获得的文件去除前364个字节：
dd if=s1 bs=1 skip=364 of=d1</hr>
使用dd命令分离文件格式如下：
dd if=源文件名 bs=1 skip=开始分离的字节数 of=目标文件名
</codes></pre>
</details>

#### 010Editor

> 这个不用说了吧
>
> 我一般拿来是在别的哪里弄好了复制过来为hex保存文件

### 文件合并

> cat 是linux系统下的一个能提取文件的内容的命令，使用cat命令将文件内容提取出来再导入目标文件
>
> `cat chapter01 chapter02 chapter03 > book` 将所有以chapter开头的文件按文件名从小到大的顺序合并，输出到book文件中

