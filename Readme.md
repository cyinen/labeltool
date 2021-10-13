这是一个使用Pyqt5写的图像数据标注工具
#### 使用步骤

1、安装依赖

```python
pip install -r reqirements.txt
```

2、运行

```python
python labeltool.py
```

3、使用

自己摸索

1）安装软件依赖
pip install -r requirements.txt
2)python labeltool.py 运行软件

图2-4 运行窗口
从运行界面可以看到整个界面除了最上面的标题栏以外分为三个区域，最左侧的为按钮区域，包括各种操作按钮。中间为图片显示区域，实时显示正在操作的图片，在图片上进行标注。最右侧为保存按钮和文件显示列表，用于保存数据和显示文件名称。下面详细介绍使用步骤。
3）从按钮栏名称可以看出，我们可以分别打开单独的图片和打开一个包含图片的目录。点击打开目录，选择图片所在目录。

图2-5 选择目录

界面会显示当前正在操作的图片和当前目录下的文件。
3)使用鼠标拖拽，选中文字区域、在文字框中输入文字后按回车

图 2-6 标注
5）标记完一张图片后单击保存数据按钮，保存数据

图2-7 保存数据
5）标记完所有图片以后点击保存按钮、JSON数据文件会自动保存在当前目录下的data/data.json文件中。


图2-8 JSON文件展示
