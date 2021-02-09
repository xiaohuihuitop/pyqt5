## 按键

![image-20210208185820277](README.assets/image-20210208185820277.png)

### 设置颜色

![image-20210208190049430](README.assets/image-20210208190049430.png)

![image-20210208190108010](README.assets/image-20210208190108010.png)











## 数字LCD

![image-20210208190200305](README.assets/image-20210208190200305.png)

![image-20210208190223767](README.assets/image-20210208190223767.png)

设置  个数  进制  样式  值

### 修改颜色

同按键的颜色设置



## 单行文字

![image-20210208190357140](README.assets/image-20210208190357140.png)

![image-20210208191508411](README.assets/image-20210208191508411.png)

![image-20210208200742517](README.assets/image-20210208200742517.png)

设置 数据 长度 模式 提示 对齐

### 其他设置

在Frame中的 的按钮无法控制大小 可以在下面更改

设置固定的 然后固定最大与最小大小

![image-20210208201436037](README.assets/image-20210208201436037.png)



字体大小

![image-20210208212324499](README.assets/image-20210208212324499.png)

字体方向

![image-20210208215839086](README.assets/image-20210208215839086.png)



## Tab Widget

![image-20210208232214433](README.assets/image-20210208232214433.png)



![image-20210208232351222](README.assets/image-20210208232351222.png)

![image-20210208232437002](README.assets/image-20210208232437002.png)

![image-20210208232557548](README.assets/image-20210208232557548.png)

这个设置比较简单 就是icon设置好看点就行  图标的大小会影响整个页面选择的大小

![image-20210208232732755](README.assets/image-20210208232732755.png)

这里是更换页面标签显示的位置 下面那个是样式

### 简单使用

Tab Widget内部的小控件 是通过名字访问的

获取当前页面与判断

```python
self.tabWidget.currentChanged.connect(self.Tab_Call)
if self.tabWidget.currentIndex() == 0:
```





## 添加资源文件

![image-20210209121512548](README.assets/image-20210209121512548.png)

![image-20210209121535817](README.assets/image-20210209121535817.png)

全部新建即可 然后加入 png图片  前缀设置无 

[阿里巴巴矢量图标库](https://www.iconfont.cn/)  可GitHub登录

### 转换

![image-20210209121639315](README.assets/image-20210209121639315.png)



### 文件分层

![image-20210209121737495](README.assets/image-20210209121737495.png)

### 修改 win.ui 转换后的文件

![image-20210209121821931](README.assets/image-20210209121821931.png)

