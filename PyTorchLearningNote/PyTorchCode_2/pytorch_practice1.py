#_*_coding:utf-8_*_
import torch
from torch.autograd import Variable
 
# 批量输入的数据量
batch_n = 100
# 通过隐藏层后输出的特征数
hidden_layer = 100
# 输入数据的特征个数
input_data = 1000
# 最后输出的分类结果数
output_data = 10
 
x = Variable(torch.randn(batch_n , input_data) , requires_grad = False)
y = Variable(torch.randn(batch_n , output_data) , requires_grad = False)
 
models = torch.nn.Sequential(
    # 首先通过其完成从输入层到隐藏层的线性变换
    torch.nn.Linear(input_data,hidden_layer),
    # 经过激活函数
    torch.nn.ReLU(),
    # 最后完成从隐藏层到输出层的线性变换
    torch.nn.Linear(hidden_layer,output_data)
)
print(models)