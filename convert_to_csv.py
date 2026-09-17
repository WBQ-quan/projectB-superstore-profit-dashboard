import pandas as pd
import os
import glob

# 1. 智能定位：脚本无论在根目录还是 data 目录，都找对根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(BASE_DIR) == "data":
    BASE_DIR = os.path.dirname(BASE_DIR)

# 2. 锁定 data 目录
data_dir = os.path.join(BASE_DIR, "data")
if not os.path.isdir(data_dir):
    raise FileNotFoundError(f"找不到 data 目录: {BASE_DIR}")

# 3. 同时匹配 .xls 和 .xlsx（完美兼容空格/下划线）
xls_list = glob.glob(os.path.join(data_dir, "*.xls")) + glob.glob(os.path.join(data_dir, "*.xlsx"))
if not xls_list:
    raise FileNotFoundError(f"在 {data_dir} 下找不到任何 .xls/.xlsx 文件")

input_file = xls_list[0]
output_file = os.path.join(data_dir, "global_superstore.csv")

print(f"找到输入文件: {input_file}")

# 4. 读取 Excel（自动兼容 xlrd / openpyxl）
try:
    df = pd.read_excel(input_file, sheet_name="Orders", engine="xlrd")
except Exception:
    df = pd.read_excel(input_file, sheet_name="Orders", engine="openpyxl")

# 5. 转存 CSV（utf-8-sig 兼容中文）
df.to_csv(output_file, index=False, encoding="utf-8-sig")
print(f"转换成功！共读取 {df.shape[0]} 行，{df.shape[1]} 列。")
print(f"CSV 已保存至: {output_file}")
