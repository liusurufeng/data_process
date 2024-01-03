import scipy.io
from PIL import Image
import numpy as np
import os

# 指定位深（比特深度）
bit_depth = 16

# 设置MAT文件所在的文件夹路径
mat_folder_path = '/mnt/data/hhong/data/CoNSeP/Test/Labels'  # 替换为MAT文件所在的文件夹路径

# 设置PNG图像保存的文件夹路径
png_folder_path = '/mnt/data/hhong/data/CoNSeP/Test/newlabel'  # 替换为PNG图像保存的文件夹路径
os.makedirs(png_folder_path, exist_ok=True)

# 遍历MAT文件夹中的所有MAT文件
mat_files = [f for f in os.listdir(mat_folder_path) if f.endswith('.mat')]
for mat_file in mat_files:
    # 加载MAT文件
    mat_data = scipy.io.loadmat(os.path.join(mat_folder_path, mat_file))

    # 获取MAT文件中的图像数据mat_data
    #我需要实例的掩膜，这里取用inst_map,不同的需求更改不同的关键字
    #查看mat文件中关键字的类型python代码为：readmat.py
    image_data = mat_data['inst_map']  

    # 将图像数据转换为整数类型
    image_array = (image_data * 65535).astype(np.uint16)

    # 将图像数据保存为PNG图像，并指定位深
    image = Image.fromarray(image_array)
    
    # 构建PNG文件名（保留原始文件名，只修改扩展名）
    png_file_name = os.path.splitext(mat_file)[0] + '.png'
    
    # 保存PNG图像
    png_file_path = os.path.join(png_folder_path, png_file_name)
    image.save(png_file_path, bitdepth=bit_depth)
    print(f'{mat_file} 转换并保存为 {png_file_path}')
