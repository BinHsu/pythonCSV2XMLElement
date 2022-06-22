# pythonCSV2XMLElement
using python3 to convert a csv file to a file of empty content xml element with attributes

#### csv sample
```
"ID", "PHONE", "age"
1, 2822, "45"
2, , 
,,38
```

#### usage
```
python3 csv2xmlElement.py --csv="AAA/XXX.csv" --xml="BBB/WWW.xml" --element=XYZ
```

#### xml result
```
<XYZ ID="1" PHONE="2822" age="45" />
<XYZ ID="2" />
<XYZ age="38"/>
```
