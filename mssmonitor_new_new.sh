#!/bin/bash

hms_pid=`ps -ef | grep -v grep | grep org.apache.hadoop.hive.metastore.HiveMetaStore | awk '{print $2}'`
echo $hms_pid;

for i in {0..260000}; do
  echo "--------------------------------------------" >> result.txt
  echo "Date : "`date` >> result.txt;
  echo "hms con(allconnect):"`netstat -pan | grep 10.120.193.20:9083 | wc -l;` >> result.txt;
  echo "hms con(sql_server):"`netstat -pan | grep 10.120.193.20:9083 | grep 10.120.193.17 | wc -l;` >> result.txt;
  pidstat_result=`pidstat -udrh -p ${hms_pid} | grep -v it.leap.com | grep -v '^$'`
  echo "${pidstat_result}" >> result.txt;
  sleep 1;
done
