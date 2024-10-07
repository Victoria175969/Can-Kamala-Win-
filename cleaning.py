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


# function table scraping 

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def table_scraper(year):
    result_votes_year = {} 
    response = requests.get(f"https://en.wikipedia.org/wiki/{year}_United_States_presidential_election#Results_by_state")
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('div', style='overflow:auto')                                      # find table
    if table is None:
        print(f"no results found for year: {year}.")
        return None
    table_list = [td.text.strip() for td in table.find_all('td')]                        # loop trough tables list and get td tags
    states_data = []                                                                     # create list with numbers by states                                                                
    current_state = []   
    for element in table_list:
        if re.search(r'[a-zA-Z]', element):                                              # look for values with letters (states)
            if current_state:
                states_data.append(current_state)                                        # grouping states data into sublists   
            current_state = [element]  
        else:
            current_state.append(element)     
    if current_state:
        states_data.append(current_state)
    result_votes_year = {                                                              # create with dict with indexes
    entry[0]: {
        "Democratic Candidate": entry[2],
        "Republican Candidate": entry[5]
        }
    for entry in states_data if len(entry) > 5 }                                       # create data frame
    df_results_year = pd.DataFrame.from_dict(result_votes_year, orient='index')
    df_results_year.index.name = 'State'
    df_results_year.columns = ['Democratic Candidate', 'Republican Candidadte']
     # comprehension to get national votes 
    df_results_year.loc['National'] = [value for value in (th.get_text(strip=True) for th in soup.find_all('th', style="text-align:right") if "%" in th.get_text(strip=True)) if value != '%'][:2]
    
    return df_results_year


