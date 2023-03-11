xyj={'唐僧':'师傅','孙悟空':'徒弟'}
print(xyj)

xyj['孙悟空']='打怪的'
print(xyj)

xyj['猪八戒']='混吃的'
print(xyj)

xyj.update({'沙和尚':'干活的','白龙马':'禽兽'})
print(xyj)

print("找不到" if xyj.get("沙僧") == None else xyj['沙僧'])

# del(xyj['白龙马'])
# print(xyj)

a=xyj.pop('白龙马')
print(a)
print(xyj)

print(len(xyj))

print(list(xyj.keys()))

print(','.join(list(xyj.keys())))

print(list(xyj.values()))