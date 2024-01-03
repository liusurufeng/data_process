import scipy.io

# 用于读取MAT文件的路径
mat_file_path = '/mnt/data/hhong/data/CoNSeP/Train/train_1.mat'

# 使用loadmat函数加载MAT文件
mat_data = scipy.io.loadmat(mat_file_path)

# 打印MAT文件中的所有键
print("MAT文件中的键：", mat_data.keys())
