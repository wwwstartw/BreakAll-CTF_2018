#flag = "22018851055521226267262148556363617755281586116780375842715627567171281568550741134"
flag = "7321220882727148614146324234228704807877070277506860386366162783026234012262881477314066708506488056526536412513540180263"
k=0
for i in range(len(flag)):
	k += int(flag[i]) * 9 ** i


print(bytes(k.to_bytes(len(flag),'big')))