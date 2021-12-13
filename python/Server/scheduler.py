import schedule # 스케줄러 라이브러리
import pymysql
import time
import datetime
import sys
import random

# 스케줄러가 수행할 함수
def schedulerJob():
    
    time1  = str(datetime.datetime.now())
    print(time1 + ' >> Scheduler Start')

    conn = pymysql.connect(
        user = 'zaba',
        passwd = '0000',
        host = '211.253.100.186',
        port = 8081,
        db = 'health',
        charset = 'utf8'
)

    sql = "INSERT INTO count_table_bak (date,user_name,squat,plank,pushup,lunge,situp) SELECT CURDATE(), user_name, count(case when squat=1 then 1 end) as squat,count(case when plank=1 then 1 end) as plank, count(case when pushup=1 then 1 end) as pushup, count(case when lunge=1 then 1 end) as lunge, count(case when situp=1 then 1 end) as situp FROM count_table GROUP BY user_name"
    sql2 = "DELETE FROM count_table"
    #sql2 = "DELETE FROM test" # 테스트용

    squat_insert = "INSERT INTO count_table(user_name, squat, plank, pushup, lunge, situp) values(%s, 1, 0, 0, 0, 0)"
    plank_insert = "INSERT INTO count_table(user_name, squat, plank, pushup, lunge, situp) values(%s, 0, 1, 0, 0, 0)"
    pushup_insert = "INSERT INTO count_table(user_name, squat, plank, pushup, lunge, situp) values(%s, 0, 0, 1, 0, 0)"
    lunge_insert = "INSERT INTO count_table(user_name, squat, plank, pushup, lunge, situp) values(%s, 0, 0, 0, 1, 0)"
    situp_insert = "INSERT INTO count_table(user_name, squat, plank, pushup, lunge, situp) values(%s, 0, 0, 0, 0, 1)"

    curs = conn.cursor()
    curs.execute(sql)
    curs.execute(sql2)
    conn.commit()
    
    for i in range(1, random.randrange(3, 101)):
        curs.execute(squat_insert, 'lsw1234')
        curs.execute(squat_insert, 'lklk12')
        curs.execute(squat_insert, 'kkaac')
        curs.execute(squat_insert, 'kcals')
        curs.execute(squat_insert, 'rainyday')
    for i in range(1, random.randrange(3, 101)):
        curs.execute(plank_insert, 'lsw1234')
        curs.execute(plank_insert, 'lklk12')
        curs.execute(plank_insert, 'kkaac')
        curs.execute(plank_insert, 'kcals')
        curs.execute(plank_insert, 'rainyday')

    for i in range(1, random.randrange(3, 101)):
        curs.execute(pushup_insert, 'lsw1234')
        curs.execute(pushup_insert, 'lklk12')
        curs.execute(pushup_insert, 'kkaac')
        curs.execute(pushup_insert, 'kcals')
        curs.execute(pushup_insert, 'rainyday')

    for i in range(1, random.randrange(3, 101)):
        curs.execute(lunge_insert, 'lsw1234')
        curs.execute(lunge_insert, 'lklk12')
        curs.execute(lunge_insert, 'kkaac')
        curs.execute(lunge_insert, 'kcals')
        curs.execute(lunge_insert, 'rainyday')

    for i in range(1, random.randrange(3, 101)):
        curs.execute(situp_insert, 'lsw1234')
        curs.execute(situp_insert, 'lklk12')
        curs.execute(situp_insert, 'kkaac')
        curs.execute(situp_insert, 'kcals')
        curs.execute(situp_insert, 'rainyday')

    conn.commit()

    time.sleep(0.5)
    conn.close()

    time2 = str(datetime.datetime.now())
    print(time2 + ' >> Scheduler End')
    print('===============================')

#매일 특정시간에 동작(23:55)
schedule.every().day.at("09:53").do(schedulerJob)

print('========== Scheduler ==========')
while True :
    schedule.run_pending()
    time.sleep(1)
