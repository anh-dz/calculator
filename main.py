from xulypheptinh import *

while True:
	pheptinh = input("Nhập phép tính: ").replace(" ", "")
	lis_so, lis_dau, so = [], [], ""
	for elem in range(len(pheptinh)):
		if pheptinh[elem].isdigit():
			so+=pheptinh[elem]
			try:
				if not pheptinh[elem+1].isdigit():
					lis_so.append(int(so))
					so = ""
			except:
				lis_so.append(int(so))
		else:
			lis_dau.append(pheptinh[elem])

	print(f"Kết quả là {xulypheptinh(lis_so, lis_dau)}")

	x = input("Bạn có muốn tiếp tục chương trình không? (Y/N): ").upper()
	if x == "Y":
		continue
	else:
		break