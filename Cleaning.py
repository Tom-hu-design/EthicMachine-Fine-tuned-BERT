import pandas as pd

care_df=pd.read_csv('./rawdata/Care.csv')
civility_df=pd.read_csv('./rawdata/Civility.csv')
courage_df=pd.read_csv('./rawdata/Courage.csv')
empathy_df=pd.read_csv('./rawdata/Empathy.csv')
flexibility_df=pd.read_csv('./rawdata/Flexibility.csv')
honesty_df=pd.read_csv('./rawdata/Honesty.csv')
humility_df=pd.read_csv('./rawdata/Humility.csv')
justice_df=pd.read_csv('./rawdata/Justice.csv')
magnanimity_df=pd.read_csv('./rawdata/Magnanimity.csv')
perspective_df=pd.read_csv('./rawdata/Perspective.csv')
SC_df=pd.read_csv('./rawdata/SelfControl.csv')
TW_df=pd.read_csv('./rawdata/Technomoral_Wisdom.csv')

neutral = pd.read_csv('./rawdata/Neutral.csv')
positive = pd.read_csv('./rawdata/Positive.csv')
negative = pd.read_csv('./rawdata/Negative.csv')
master_raw_df = pd.read_csv('./rawdata/Master_raw.csv')

csv_list = ["care_df","civility_df","courage_df","empathy_df","flexibility_df","honesty_df","humility_df","justice_df","magnanimity_df","perspective_df","SC_df","TW_df"]

df_master_raw = pd.DataFrame()
master_train_df = pd.DataFrame()

# df_master_raw = pd.concat([care_df,civility_df,courage_df,empathy_df,flexibility_df,honesty_df,humility_df,justice_df,magnanimity_df,perspective_df,SC_df,TW_df])
# master_raw_df['labels2']=1

neutral[['positive','negative']]=0
neutral['neutral']=1

# positive_df=master_raw_df[['Positive', 'labels2']]
# positive_df[['positive','negative']] = 0
# positive_df.to_csv('Positive.csv') 

# negative_df=master_raw_df[['Negative','labels2']]
# negative_df[['positive','negative']] = 0
# negative_df.to_csv('Negative.csv') 

master_train_df = pd.concat([positive,negative,neutral],ignore_index=True)
master_train_df = master_train_df[['text','positive','negative','neutral']]
master_train_df.to_csv('training.csv') 



