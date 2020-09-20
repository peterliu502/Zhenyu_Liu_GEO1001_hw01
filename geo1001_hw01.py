#-- GEO1001.2020--hw01
#-- Zhenyu Liu
#-- 5386586


import hw01_A1 as a1
import hw01_A2 as a2
import hw01_A3 as a3
import hw01_A4 as a4
import hw01_BQ as bq
import hw01_preprocess as pp

# Lession A1
# A1.1
a1.mean_statistics("HEAT - A_final.csv")
a1.mean_statistics("HEAT - B_final.csv")
a1.mean_statistics("HEAT - C_final.csv")
a1.mean_statistics("HEAT - D_final.csv")
a1.mean_statistics("HEAT - E_final.csv")

# A1.2
sensor_name = pp.list_sensor_name("ABCDE")
a1.multi_hist(sensor_name, "Temperature", 5)
a1.multi_hist(sensor_name, "Temperature", 50)

# A1.3
a1.freq_polygons(sensor_name, "Temperature")

# A1.4
a1.boxplot(sensor_name, "Wind Speed")
a1.boxplot(sensor_name, "Direction True")
a1.boxplot(sensor_name, "Temperature")

# Lession A2
# A2.1
a2.pmf_plot(sensor_name, "Temperature")
a2.pdf_plot(sensor_name, "Temperature")
a2.cdf_plot(sensor_name, "Temperature")

# A2.2
a2.pdf_and_kde(sensor_name, "Wind Speed")

# Lession A3
# A3.1
a3.correlations(sensor_name, "Temperature")
a3.correlations(sensor_name, "WBGT")
a3.correlations(sensor_name, "Crosswind Speed")

# Lession A4
# A4.1
a4.multi_pd_2_csv("confidence_intervals",
                  a4.cdf_ci(sensor_name, "Temperature", 0.95),
                  a4.cdf_ci(sensor_name, "Wind Speed", 0.95))

# A4.2
a4.sensors_t_test(pp.list_sensor_name("ED"), "Temperature")
a4.sensors_t_test(pp.list_sensor_name("ED"), "Wind Speed")
a4.sensors_t_test(pp.list_sensor_name("DC"), "Temperature")
a4.sensors_t_test(pp.list_sensor_name("DC"), "Wind Speed")
a4.sensors_t_test(pp.list_sensor_name("CB"), "Temperature")
a4.sensors_t_test(pp.list_sensor_name("CB"), "Wind Speed")
a4.sensors_t_test(pp.list_sensor_name("BA"), "Temperature")
a4.sensors_t_test(pp.list_sensor_name("BA"), "Wind Speed")

# Bonus question
bq.date_of_extremum(sensor_name, "Temperature")