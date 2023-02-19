import pandas

sampleData = pandas.read_csv("pSampleData.csv", encoding = "UTF-8")

print(sampleData)
print("---------------")
print(sampleData.head(2))
print("---------------")
print(sampleData.tail(3))

print("---------------")

#split the range if rows commanded
d_split = sampleData.iloc[3:6]
print(d_split)

print("---------------")
#split splitted data
print(d_split.iloc[1:2])
