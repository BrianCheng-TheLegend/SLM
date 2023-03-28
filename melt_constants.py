# workpiece excel information
layer_label = ['layer']
feature = ['energy', 'entropy', 'contrast', 'idm', 'autocorrelation', 'mean_x',
           'mean_y', 'variance_x', 'variance_y', 'standard_deviation_x',
           'standard_deviation_y', 'correlation', 'dissimilarity']
proc_param = ['oxygen concentration', 'laser power', 'scanning velocity',
              'layer height', 'energy density']

# material property excel information
trail_label = ['trail']
ignore_data = 'X'
printer_param_col = 5

# output excel information
output_label = ['prediction', 'true', 'error(%)', 'train number',
                'test number', 'feature numebr', 'remove feature',
                'R2 score', 'MSE', 'MAE']

# model default parameters
xgboost_param = {'n_estimators': 1000,
                 'learning_rate': 0.3,
                 'max_depth': 5}
lightgbm_param = {'boosting_type': 'gbdt',
                  'num_leaves': 1000,
                  'learning_rate': 0.3,
                  'max_depth': 5}
logistic_param = {'max_iter': 10000,
                  'random_state': 0}
svr_param = {'C': 1000,
             'kernel': 'rbf',
             'gamma': 'auto'}

# default train and test data
bone_fp = ['./data/glcm-data/第一批狗骨頭.xlsx',
           './data/glcm-data/第二批狗骨頭.xlsx']
bone_ppfp = ['./data/glcm-data/第一批狗骨頭材料特性.xlsx',
             './data/glcm-data/第二批狗骨頭材料特性.xlsx']
ring_fp = ['./data/glcm-data/第一批圓環.xlsx',
           './data/glcm-data/第二批圓環.xlsx']
ring_ppfp = ['./data/glcm-data/第一批圓環材料特性.xlsx',
             './data/glcm-data/第二批圓環材料特性.xlsx']

# dictionary key
tensile_key = ['tensile']
pmb_key = ['pmb_50Hz', 'pmb_200Hz', 'pmb_400Hz', 'pmb_800Hz']
iron_key = ['iron_50Hz', 'iron_200Hz', 'iron_400Hz', 'iron_800Hz']
