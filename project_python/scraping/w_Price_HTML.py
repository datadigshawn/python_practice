# -*- coding: utf-8 -*-
import datetime
import sqlite3 as lite
import array
import scraping
f = open('price.html','w')
date = "date"
copper = "copper"
al = "al"
nick = "nick"
zinc = "zinc"
message = """<html>
<head><meta charset="UTF-8"></head>
<body style="font-family:'新細明體'; font-size:'24px'" >
<p style="color:blue">各位長官好:</p>
<p style="color:blue">LME國際金屬行情CASH BUYER價格(USD/TON):</p>
<p style="color:#FF3399"><a>%s&nbsp&nbsp&nbsp 銅</a>
<a>%s,鋁%s,鎳%s,鋅%s</a></p>
<p style="color:blue">滬銅行情價格(CNY/TON):</p>

<p style="color:blue">美國西德州原油價格(USD/桶):</p>
<p style="color:blue">前日匯率(2015/8/6)</p>
<p style="color:blue">中鋼2015年第二季7月盤價:</p>
<p style="color:blue">燁聯2015/7月份盤價:</p>
<p style="color:blue">燁聯2015/7月份盤價:/<p>
<p style="color:blue">華文專業鋼鐵網台灣地區一週鋼市(TWD/TON):</p>
<p style="color:blue">(當日匯率：USD/TWD31.70) 每週四更新/<p>
<p style="color:blue">以下附件 </p>
<p style="color:blue">LME國際金屬銅、鋁、鎳最近30天行情價格    (資料擷取台灣區電線電纜工業同業公會)</p>
<p style="color:blue"> 銅、鋁、鎳、鋅CASH BUYER價格       (資料擷取LME網站)</p>
<p style="color:blue">銅、鋁、鎳、鋅技術線圖                  (資料擷取LME網站)</p>
<p style="color:blue">美國西德州原油價格                                  (資料擷取經濟部能源局油價資訊管理與分析系統)</p>
<p style="color:blue">前日匯率                                               (資料擷取兆豐國際商業銀行)</p>
<p style="color:blue">Steelnet華文專業鋼鐵網鋼材價格                   (資料擷取華文鋼鐵鋼台灣地區一週鋼市)</p>
<p style="color:blue">請參考.</p>
<p style="color:blue">(以上資料由專案管理部提供)</p>


</body>
</html>"""%(date,copper,al,nick,zinc)




f.write(message)
f.close()

lme = scraping.ScrapingLMELogin()
lme.LoginGetValue()
lmeValues =  lme.LoginGetValue()
sh = scraping.ScrapingSHCopper()
sh.SHGetValue()
shValues = sh.SHGetValue()

#time
DailyNow= datetime.datetime.today()
print DailyNow 
print DailyNow.year
mm = '{:02d}'.format(DailyNow.month)
dd = '{:02d}'.format(DailyNow.day)
date_stamp = ("%s-%s-%s"%(DailyNow.year,mm,dd))
print date_stamp


#SQLite
con = lite.connect('daily_price.db')
with con:
    cur=con.cursor()
    sql_action='SELECT Record_Date FROM daily WHERE Record_Date=?'
    parameters = [date_stamp]
    for row in con.execute(sql_action,parameters):
        print "find",row[0]
        break
    else:
        sql_InsertDate = 'INSERT INTO daily(Record_Date) VALUES (?)'
        con.execute(sql_InsertDate, parameters)
        
    #update LME LOGIN DATA
    sql_LMEaction='SELECT Record_Date FROM daily WHERE Record_Date=?'
    sql_LMEupdate='UPDATE daily SET LME_Copper=?, LME_AL=?, LME_Nick=?, LME_Zinc=? WHERE Record_Date=?'
    LME_parameters = [lmeValues[0]]
    LME_Upparameters = [lmeValues[1],lmeValues[2],lmeValues[3],lmeValues[4],lmeValues[0]]
    for row in con.execute(sql_LMEaction,LME_parameters):
        print "find",row[0]
        con.execute(sql_LMEupdate,LME_Upparameters)
        break
    else:
        sql_LME_InsertDate = 'INSERT INTO daily(Record_Date) VALUES (?)'
        con.execute(sql_LME_InsertDate, LME_parameters)
        con.execute(sql_LMEupdate,LME_Upparameters)
    
    #update ShangHai Copper Price
    sql_SHaction='SELECT Record_Date FROM daily WHERE Record_Date=?'
    sql_SHupdate='UPDATE daily SET Shang_Hai_Copper=? WHERE Record_Date=?'
    SH_parameters = [shValues[0]]
    SH_Upparameters = [shValues[1], shValues[0]]
    for row in con.execute(sql_SHaction, SH_parameters):
        print "find",row[0]
        con.execute(sql_SHupdate,SH_Upparameters)
        break
    else:
        sql_SH_InsertDate = 'INSERT INTO daily(Record_Date) VALUES (?)'
        con.execute(sql_SH_InsertDate, SH_parameters)
        con.execute(sql_SHupdate,SH_Upparameters)
    
        
