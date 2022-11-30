import pymysql
import pandas as pd
 
file_name = r'Data\Data_info\data.xlsx'
df = pd.DataFrame(pd.read_excel(file_name))
conn = pymysql.connect(host='localhost',user="root",password="123456",port=3306,database="tourism_system")
cursor = conn.cursor()
sql="""
CREATE TABLE IF NOT EXISTS scenicSpot_info(
   scenicSpot VARCHAR(100) NOT NULL,
   url VARCHAR(100) NOT NULL,
   score VARCHAR(10),
   comment VARCHAR(10),
   heat VARCHAR(10),
   address VARCHAR(100)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
cursor.execute(sql)
insert="""
INSERT INTO scenicspot_info ( scenicSpot,url,score,comment,heat,address )
                       VALUES
                       ( %s,%s,%d,%d,%d,%s);
"""
print(df.iloc[12,2])

print(conn)
for i in range(5613):
    scenicSpot=df.iloc[i,0]
    url=df.iloc[i,1]
    score=df.iloc[i,2]
    comment=df.iloc[i,3]
    heat=df.iloc[i,4]
    address=df.iloc[i,5]
    list=[scenicSpot,url,score,comment,heat,address]
    cursor.execute(insert,list)
    


