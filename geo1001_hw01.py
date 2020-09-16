#-- GEO1001.2020--hw01
#-- Zhenyu Liu
#-- 5386586


import hw01_A1 as a1

# Lession A1
# A1.1
a1.mean_statistics("HEAT - A_final.csv")
a1.mean_statistics("HEAT - B_final.csv")
a1.mean_statistics("HEAT - C_final.csv")
a1.mean_statistics("HEAT - D_final.csv")
a1.mean_statistics("HEAT - E_final.csv")

# A1.2
sensor_name = ["HEAT - " + i + "_final.csv" for i in "ABCDE"]
a1.multi_hist(sensor_name, "Temperature", 5)
a1.multi_hist(sensor_name, "Temperature", 50)

# A1.3
sensor_name = ["HEAT - " + i + "_final.csv" for i in "ABCDE"]
a1.freq_polygons(sensor_name, "Temperature")
