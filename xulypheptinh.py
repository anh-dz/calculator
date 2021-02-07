def xulypheptinh(lis_so, lis_dau):
	ans, temp = 0, len(lis_dau)
	if len(lis_so)>temp:
		lis_dau.insert(0, "+")
		temp+=1
	for i in range(temp):
		if lis_dau[i]=='+':
			ans+=lis_so[i]
		elif lis_dau[i]=='-':
			ans-=lis_so[i]
		elif lis_dau[i]=='*':
			ans*=lis_so[i]
		elif lis_dau[i]=='/':
			ans/=lis_so[i]
		elif lis_dau[i]=='^':
			ans**=lis_so[i]
	return ans