import re
import csv

# 定義正則表達式來匹配日期 (格式: YYYY/MM/DD)
date_pattern = r'(\d{4}/\d{2}/\d{2}[^\n]*)'

def read_file(filename):
    """從檔案中讀取所有行並返回列表"""
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines, date_pattern):
    """處理輸入行資料，匹配日期並結構化輸出"""
    matches = re.findall(date_pattern, "\n".join(lines))  # 提取日期匹配
    result = []  # 使用動態列表替代固定大小陣列
    current_row = []

    for line in lines:
        if line in matches:  # 如果行匹配日期
            if current_row:  # 如果有未儲存的行，先加入結果
                result.append(current_row)
            current_row = [line]  # 開始新行
        else:  # 如果行不匹配日期
            current_row.append(line)
    
    if current_row:  # 確保最後的行也被儲存
        result.append(current_row)

    return result

def write_file(filename, data):
    """將處理後的資料寫入 CSV 檔案"""
    with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def main():
    input_file = '9-10.txt'  # 輸入檔案名稱
    output_file = 'output.csv'  # 輸出檔案名稱

    # 讀取檔案
    lines = read_file(input_file)
    # 處理資料
    structured_data = convert(lines, date_pattern)
    # 寫入檔案
    write_file(output_file, structured_data)

if __name__ == "__main__":
    main()
