**<span style="font-size:larger;">数据</span>**

train_data.mat 包含3000张尺寸为28×28的灰度图片，其中共 200 种字母，每种字母 15 张图片，字母类别的标签按顺序编号为 1-200。

test_data.mat 包含 1000 张无标注的测试图片。

**<span style="font-size:larger;">要求</span>**

请自行划分train_data中的数据，训练和验证基于SVM的分类器，并对1000张无标注测试图片进行预测。请将预测结果（类别id:1-200）填充到submission.csv对应列。