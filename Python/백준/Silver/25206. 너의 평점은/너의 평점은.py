total_point=0
total_point2=0
for i in range(20):
    A,B,C=map(str, input().split())
    if C!='P':
        if C=='A+':
            total_point+=int(float(B))*4.5
            total_point2+=int(float(B))
        elif C=='A0':
            total_point+=int(float(B))*4.0
            total_point2+=int(float(B))
        elif C=='B+':
            total_point+=int(float(B))*3.5
            total_point2+=int(float(B))
        elif C=='B0':
            total_point+=int(float(B))*3.0
            total_point2+=int(float(B))
        elif C=='C+':
            total_point+=int(float(B))*2.5
            total_point2+=int(float(B))
        elif C=='C0':
            total_point+=int(float(B))*2.0
            total_point2+=int(float(B))
        elif C=='D+':
            total_point+=int(float(B))*1.5
            total_point2+=int(float(B))
        elif C=='D0':
            total_point+=int(float(B))*1.0
            total_point2+=int(float(B))
        else:
            total_point2+=int(float(B))
print(total_point/total_point2)