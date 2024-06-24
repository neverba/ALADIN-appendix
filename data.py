
coef_elebuy = np.array([35.8, 35.8, 35.8, 35.8, 35.8, 35.8, 35.8, 45.8, 45.8, 55.8, 55.8, 55.8, 55.8, 55.8, 55.8, 45.8, 45.8, 55.8, 55.8, 55.8, 55.8, 55.8, 45.8, 35.8])

# 调整开始的时段
coef_elebuy = coef_elebuy[tt:]

coef_gasbuy = 6 * np.ones(T)

coef_cabuy = 240 * np.ones(T)
coef_casell = 80 * np.ones(T)
coef_caload = 0.5 * coef_cabuy



coef_windcut = 20

# 区域1参数
coef_heatbuy_1 = np.array([44.75, 44.75, 44.75, 44.75, 44.75, 44.75, 44.75, 
                           57.25, 57.25, 69.75, 69.75, 69.75, 69.75, 69.75, 
                           69.75, 57.25, 57.25, 69.75, 69.75, 69.75, 69.75, 
                           69.75, 57.25, 44.75])

coef_coolbuy_1 = np.array([44.75, 44.75, 44.75, 44.75, 44.75, 44.75, 44.75, 
                           57.25, 57.25, 69.75, 69.75, 69.75, 69.75, 69.75, 
                           69.75, 57.25, 57.25, 69.75, 69.75, 69.75, 69.75, 
                           69.75, 57.25, 44.75])
# 调整开始的时段
coef_heatbuy_1 = coef_heatbuy_1[tt:]
coef_coolbuy_1 = coef_coolbuy_1[tt:]


alpha_eload_1 = 10
alpha_hload_1 = 16
alpha_cload_1 = 16

gt_eta_1 = 0.8
gb_eta_1 = 0.8
eb_eta_1 = 0.8
ec_eta_1 = 0.8

gt_min_1 = 16
gt_max_1 = 40
gt_ramp_1 = 10

gb_min_1 = 10
gb_max_1 = 30
gb_ramp_1 = 8

eb_min_1 = 0
eb_max_1 = 20

ec_min_1 = 0
ec_max_1 = 30

# 调整开始的时段
windfore_1 = np.array([16.2, 17.0, 12.6, 8.6, 5.8, 6.7, 11.4, 18.9, 21.6, 23.0, 
                       24.0, 25.2, 26.8, 30.4, 32.1, 32.7, 30.4, 26.8, 22.2, 
                       16.9, 14.7, 13.1, 11.9, 11.2])

eloadfore_1 = np.array([32.0, 34.5, 37.0, 39.5, 43.0, 48.0, 51.5, 52.0, 51.0, 49.5, 
                        47.0, 44.0, 41.0, 39.0, 37.5, 38.0, 39.0, 42.0, 45.0, 
                        49.0, 50.5, 50.0, 48.0, 44.0])

hloadfore_1 = np.array([20.0, 21.5, 22.0, 22.5, 23.5, 26.0, 28.5, 29.5, 30.0, 29.8, 
                        29.0, 28.0, 27.0, 26.0, 25.5, 25.8, 26.2, 27.0, 28.0, 
                        29.0, 29.2, 28.8, 27.5, 25.0])

cloadfore_1 = np.array([13.2, 14.1, 15.0, 15.1, 15.9, 16.3, 15.5, 14.6, 14.5, 14.2, 
                        14.1, 14.0, 14.2, 14.3, 14.5, 14.6, 15.0, 16.1, 16.7, 
                        17.2, 16.3, 15.7, 14.9, 13.8])


windfore_1  = windfore_1[tt:]
eloadfore_1 = eloadfore_1[tt:]
hloadfore_1 = hloadfore_1[tt:]
cloadfore_1 = cloadfore_1[tt:]

windfore_1[:T] += 25  # 注意风电加25


eleline_max_1 = 100
heatline_max_1 = 100
windtrade_max_1 = 100

elebuy_max_1 = 200
gasbuy_max_1 = 250

eload_min_1 = 0.8 * eloadfore_1[:T]
eload_max_1 = 1.2* eloadfore_1[:T]

hload_min_1 = 0.8 * hloadfore_1[:T]
hload_max_1 = 1.2 * hloadfore_1[:T]

cload_min_1 = 0.8 * cloadfore_1[:T]
cload_max_1 = 1.2 * cloadfore_1[:T]





# 区域2参数
coef_heatbuy_2 = np.array([44.75, 44.75, 44.75, 44.75, 44.75, 44.75, 44.75,
                           57.25, 57.25, 69.75, 69.75, 69.75, 69.75, 69.75,
                           69.75, 57.25, 57.25, 69.75, 69.75, 69.75, 69.75,
                           69.75, 57.25, 44.75])

coef_coolbuy_2 = np.array([44.75, 44.75, 44.75, 44.75, 44.75, 44.75, 44.75,
                           57.25, 57.25, 69.75, 69.75, 69.75, 69.75, 69.75,
                           69.75, 57.25, 57.25, 69.75, 69.75, 69.75, 69.75,
                           69.75, 57.25, 44.75])

# 调整开始的时段
coef_heatbuy_2 = coef_heatbuy_2[tt:]
coef_coolbuy_2 = coef_coolbuy_2[tt:]

alpha_eload_2 = 10
alpha_hload_2 = 16
alpha_cload_2 = 16

gt_eta_2 = 0.8
gb_eta_2 = 0.8
eb_eta_2 = 0.8
ec_eta_2 = 0.8

gt_min_2 = 5
gt_max_2 = 20
gt_ramp_2 = 8

gb_min_2 = 5
gb_max_2 = 20
gb_ramp_2 = 8

eb_min_2 = 0
eb_max_2 = 20

ec_min_2 = 0
ec_max_2 = 20


windfore_2 = np.array([7.4, 8.9, 6.5, 3.3, 1.3, 1.9, 4.7, 9.2, 11.0, 12.0, 12.6, 13.5,
                       14.6, 16.9, 18.0, 18.5, 16.9, 14.6, 11.6, 7.1, 5.6, 4.5, 3.7, 3.2])

eloadfore_2 = np.array([30.0, 32.5, 35.0, 37.5, 41.0, 46.0, 49.5, 50.0, 49.0, 47.5, 
                        45.0, 42.0, 39.0, 37.0, 35.5, 36.0, 37.0, 40.0, 43.0, 47.0, 
                        48.5, 48.0, 46.0, 42.0])

hloadfore_2 = np.array([18.0, 19.5, 20.0, 20.5, 21.5, 24.0, 26.5, 27.5, 28.0, 27.8, 
                        27.0, 26.0, 25.0, 24.0, 23.5, 23.8, 24.2, 25.0, 26.0, 27.0, 
                        27.2, 26.8, 25.5, 23.0])

cloadfore_2 = np.array([8.2, 9.1, 10.0, 10.5, 11.2, 12.0, 12.8, 13.5, 14.2, 14.8, 
                        15.3, 15.7, 15.9, 16.0, 16.0, 16.0, 15.8, 15.6, 15.3, 14.9, 
                        14.5, 14.1, 13.6, 13.0])

# 调整开始的时段
windfore_2  = windfore_2[tt:]
eloadfore_2 = eloadfore_2[tt:]
hloadfore_2 = hloadfore_2[tt:]
cloadfore_2 = cloadfore_2[tt:]

eleline_max_2 = 100
heatline_max_2 = 100
windtrade_max_2 = 100

elebuy_max_2 = 200
gasbuy_max_2 = 250

eload_min_2 = 0.8 * eloadfore_2[:T]
eload_max_2 = 1.2 * eloadfore_2[:T]

hload_min_2 = 0.8 * hloadfore_2[:T]
hload_max_2 = 1.2 * hloadfore_2[:T]

cload_min_2 = 0.8 * cloadfore_2[:T]
cload_max_2 = 1.2 * cloadfore_2[:T]

