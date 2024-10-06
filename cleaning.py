def cleaning_2016(df_2016):
        #dropping unnecessary columns
        df_2016.drop(columns = ['_nat_shortpoly_combpoly_weight', '_shortpoly_combpoly_weight','_nonlinear_polynomial_degree', '_attenuate_endpoints', '_out_of_state_house_discount','_state_trendline_weight','_state_houseeffects_weight', '_numloops', '_defaultbasetime','_minpoints'],  axis =1, inplace=True)
        df_2016.drop(columns = ['_medpoly2', 'trend_medpoly2','_shortpoly0', 'trend_shortpoly0', 'sum_weight_medium', 'sum_weight_short', 'sum_influence', 'sum_nat_influence','_house_effects_multiplier'],  axis =1, inplace=True)
        df_2016.drop(['timestamp','comment', 'last_enddate'],  axis =1, inplace=True)
        df_2016.drop(['cycle','candidate_id', 'election_date', 'election_qdate',	'last_qdate'],  axis =1, inplace=True)
        
        #drop Gary Johnson rows (3rd candidate 2016)
        df_2016 = df_2016[df_2016['candidate_name'] != 'Gary Johnson']
        import pandas as pd
        import datetime as dt
        #only keep rows from July till election for comparison
        df_2016['modeldate'] = pd.to_datetime(df_2016['modeldate'])
        start_date = dt.datetime(2016, 7, 1)
        end_date = dt.datetime(2016, 11, 9)
        index_names = df_2016[(df_2016['modeldate'] < start_date) | (df_2016['modeldate'] > end_date)].index
        df_2016.drop(index_names, inplace = True)
        df_2016.dropna(how="any", inplace=True)