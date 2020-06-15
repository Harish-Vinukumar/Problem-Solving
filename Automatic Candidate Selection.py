"""
Selecting a candidate automatically based on
the score candidate obtained
"""
import pandas as pd
from scipy.stats import norm, zscore


candidate_details = {'Name': ['Raj', 'Ram', 'Rajesh', 'Aravind', 'Arav', 'Arjun',
                              'John', 'James', 'Joseph', 'Daniel', 'Suresh', 'Bharath'],
                     'Marks': [70, 65, 68, 75, 58, 72, 67, 62, 60, 65, 75, 70],
                     'Mail Id': ['raj@gmail.com', 'ram@gmail.com', 'rajesh@gmail.com',
                                 'aravind@gmail.com', 'arav@gmail.com', 'arjun@gmail.com',
                                 'john@gmail.com', 'james@gmail.com', 'joseph@gmail.com',
                                 'daniel@gmail.com', 'suresh@gmail.com', 'bharath@gmail.com']
                     }

candidate_df = pd.DataFrame(candidate_details)
pass_marks = 70.00
mean_marks = round(candidate_df['Marks'].mean(), 2)
sd_marks =  round(candidate_df['Marks'].std(), 2)

candidate_df['Percentile'] = round(candidate_df['Marks'].apply(lambda x: (x - mean_marks)/sd_marks).apply(norm.cdf) * 100, 2)

result_df = candidate_df[candidate_df['Percentile'] >= pass_marks].reset_index(drop=True)
print(result_df)

