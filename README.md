# pythonCSV2XMLElement
using python3 to convert a csv file to a file of empty content xml element with attributes

#### csv sample
```
"ID","PHONE","age","AA","bb"
1,2822,"45",,
2,,,,
,,38,"H","Q"
```

#### usage
```
python3 csv2xmlElement.py --csv="AAA/XXX.csv" --xml="BBB/WWW.xml" --element=XYZ
```

#### xml result
```
<XYZ ID="1" PHONE="2822" age="45" />
<XYZ ID="2" />
<XYZ age="38" AA="H" bb="Q" />
```

#### optional
##### with ignoring and default element name
```
# default element will be CSV filename
# ignoring will shell the CSV key in list
python3 csv2xmlElement.py --csv="AAA/XXX.csv" --xml="BBB/WWW.xml" --ignoring=AA,bb
```
##### xml result
```
<XXX ID="1" PHONE="2822" age="45" />
<XXX ID="2" />
<XXX age="38" />
```
##### with filter
```
# collect the CSV key in filter only
python3 csv2xmlElement.py --csv="AAA/XXX.csv" --xml="BBB/WWW.xml" --filter=ID,bb
```
##### xml result
```
<XXX ID="1" />
<XXX ID="2" />
<XXX bb="Q" />
```
