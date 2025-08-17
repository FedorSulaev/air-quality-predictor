# Data sources

## OpenAQ sensor data

- Source: https://explore.openaq.org/
- Downloaded using the OpenAQ API and data archives on AWS S3  https://docs.openaq.org/
- Updated on Aug 17 2025

Example:
```
location_id,sensors_id,location,datetime,lat,lon,parameter,units,value
9369,28602,RO0083A-9369,2020-07-30T23:00:00+03:00,47.1567664986992,27.5748656243897,no2,µg/m³,51.44521273
9369,28602,RO0083A-9369,2020-08-04T01:00:00+03:00,47.1567664986992,27.5748656243897,no2,µg/m³,4.15590495
9369,28602,RO0083A-9369,2020-08-04T02:00:00+03:00,47.1567664986992,27.5748656243897,no2,µg/m³,2.6868661
```
