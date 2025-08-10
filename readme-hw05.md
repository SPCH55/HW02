# Homework 05

## a. วิธีการติดตั้งและเปิดใช้งาน ClickHouse
- ติดตั้ง ClickHouse บน Ubuntu `sudo apt-get install clickhouse-server clickhouse-client`
- เริ่มต้น ClickHouse Server: `sudo service clickhouse-server start`
- ตรวจสอบสถานะ: `sudo service clickhouse-server status`
- เข้าสู่ Client: `clickhouse-client`

## b. วิธีนำเข้าข้อมูลจากการบ้านที่ 4 (HW04)
- เตรียมข้อมูลในรูปแบบ CSV:
ให้ข้อมูลจาก HW04 อยู่ในรูปแบบ CSV ที่พร้อมใช้งาน เช่น hw04_data.csv.

- สร้างตารางใน ClickHouse:
ในการนำเข้าข้อมูล, คุณต้องสร้างตารางในฐานข้อมูลของ ClickHouse ก่อน ตัวอย่างเช่น:
`CREATE TABLE hw04_data
(
    id Int32,
    name String,
    date DateTime,
    value Float64
) ENGINE = MergeTree()
ORDER BY id;`

- นำเข้าข้อมูลจาก CSV:
`INSERT INTO hw04_data FORMAT CSV
FROM '/path/to/hw04_data.csv';`

- ตรวจสอบข้อมูล: `SELECT * FROM hw04_data LIMIT 10;`

## c. วิธีการติดตั้งและเปิดใช้งาน Superset
- ใช้คำสั่ง `git clone https://github.com/apache/superset`
- จากนั้น `cd superset`
- ขั้นตอนต่อไป ใช้คำสั่ง `git checkout tags/5.0.0`
- เปิด docker ก่อนใช้คำสั้ง `docker compose -f docker-compose-image-tag.yml up`
- เปิด http://localhost:8088 ได้เลย

## d. วิธีการเชื่อม Superset กับ ClickHouse
- เข้าสู่หน้า Superset:
- เปิดเว็บบราวเซอร์และไปที่ http://localhost:8088.
- เพิ่มฐานข้อมูล:
    ไปที่ Data > Databases > + Database.
    เลือก ClickHouse ในตัวเลือกฐานข้อมูล.
    กรอกข้อมูลการเชื่อมต่อ, ตัวอย่างเช่น: clickhouse://username:password@localhost:9000/default
- บันทึกการตั้งค่า

## e. วิธีการนำเสนอข้อมูลจากข้อมูล b. บน dashboard ของ Superset
- สร้าง Chart ใหม่:
    ไปที่ Charts > + Chart.
    เลือก Database และ Table ที่เชื่อมกับ ClickHouse.
    เลือกประเภทกราฟ เช่น Line Chart, Bar Chart, หรือ Table ตามที่ต้องการ.

- กำหนดค่า X-Axis และ Y-Axis:
    กำหนดข้อมูลที่จะใช้แสดงบนแกน X และ Y, เช่น:
    X-Axis: date
    Y-Axis: value

- สร้าง Dashboard:
    ไปที่ Dashboards > + Dashboard และตั้งชื่อแดชบอร์ด.
    เพิ่มกราฟที่สร้างขึ้นไปในแดชบอร์ด.

- ดูผลลัพธ์:
    เมื่อเพิ่มกราฟลงในแดชบอร์ดแล้ว, คุณจะสามารถดูข้อมูลจาก ClickHouse ที่แสดงผลในรูปแบบกราฟบน Superset.

## f. บทสรุปการใช้งาน
การใช้ ClickHouse และ Superset ร่วมกันทำให้การวิเคราะห์ข้อมูลขนาดใหญ่เป็นเรื่องง่ายและมีประสิทธิภาพ. ClickHouse ช่วยให้การประมวลผลข้อมูลรวดเร็ว และ Superset เป็นเครื่องมือที่มีประสิทธิภาพสำหรับการสร้างแดชบอร์ดและกราฟต่าง ๆ.

- ClickHouse: ระบบฐานข้อมูลที่มีความเร็วสูง เหมาะสำหรับการประมวลผลข้อมูลขนาดใหญ่และทำการวิเคราะห์.
- Superset: เครื่องมือสำหรับการสร้างและแสดงผลข้อมูลด้วยกราฟ, ช่วยให้การนำเสนอข้อมูลมีความเข้าใจง่าย.

## ผลลัพธ์
![alt text](image.png)