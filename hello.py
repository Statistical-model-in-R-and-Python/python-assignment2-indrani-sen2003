
def hello_world():
    import pandas as pd;
    df=pd.read_csv("Walmart2.csv");
    df.dtypes
    df.head(15)
    import os
    import pandas as pd
    import numpy as np
    import warnings
    warnings.simplefilter("ignore")
    # Get the directory and extract the data
    #os.chdir('C:/Users/Dell/MBA/VCU_Course/SCMA/Data')
    # ## ASSIGNMENT 1a
    nsso_df = pd.read_csv('4. NSSO68 data set.csv')
    nsso_df.info()
    nsso_df.isnull().any()
    nsso_df.isnull().sum()
    nsso_df.shape
    nsso_df.head()
    list(nsso_df.columns)
    featuresCol = ['Sector','state','State_Region','District','Religion','Social_Group',
               'MPCE_URP','MPCE_MRP','Sex','Age','Marital_Status','Education','ricetotal_q',
               'wheattotal_q','cerealstt_q','pulsestt_q','milkprott_q','edibletotal_q','emftt_q','goatmeat_q',
               'ricetotal_v','wheattotal_v','cerealtot_v','pulsestt_v','milkprott_v','edibletotal_v','goatmeat_v',
               'emftt_v','fv_tot','state_1']
    nsso_df_ReqData = nsso_df[featuresCol]
    nsso_df_ReqData.shape
# Viewing all columns
    pd.set_option('display.max_columns', None)
    nsso_df_ReqData.head()
    nsso_df_ReqData.describe()
    nsso_df_ReqData.info()
    nsso_df_ReqData.isnull().any()
    nsso_df_ReqData.isnull().sum()
# Handling Missing Values
# There are very small amount of na values i.e. 26 values out of 101662 so, we can drop these points or can also
# be removed using imputing, but as all the features having na values are categorical columns so it is best to drop those 
# rows for any baisness in future
    nsso_df_ReqData.dropna(inplace = True)
    nsso_df_ReqData.isnull().sum()
    nsso_df_ReqData.info()
# Checking for duplicate records
    nsso_df_ReqData.duplicated().any()
    nsso_df_ReqData.duplicated().sum()
#All the duplicated rows
    nsso_df_ReqData[nsso_df_ReqData.duplicated()]
    nsso_df_ReqData.drop_duplicates(inplace=True)
    nsso_df_ReqData.duplicated().any()
# SUBSETTING
    megh = nsso_df_ReqData[nsso_df_ReqData['state_1'] == 'MEG']
    megh.head()
    megh.shape
    megh.describe()
    megh['District'].unique()
    dist_names = {1:'West Garo Hills', 2:'East Garo Hills', 3:'South Garo Hills', 4:'West Khasi Hills', 
     5:'Ri Bhoi', 6:'East Khasi Hills', 7: 'jaintia Hills'}
    megh['Districts_Name'] = megh['District'].map(dist_names)
    megh.shape
    megh.head()
    megh['Districts_Name'].unique()
    division_names = {1:'Tura', 2:'Tura',3:'Tura', 4:'Shillong',5:'Shillong',6:'Shillong',7:'Shillong'}
    megh['division_names'] = megh['District'].map(division_names)
    megh.head()
    division_index = {'Tura':1, 'Shillong':2}
    megh['division_index'] = megh['division_names'].map(division_index)
    megh.head()
    megh['MPCE_MRP'].describe()
    megh['cerealstt_q'].describe()
    megh['cerealtot_v'].describe()
    megh['goatmeat_q'].describe()
    megh['goatmeat_v'].describe()
    megh['milkprott_q'].describe()
    megh['milkprott_v'].describe()
    megh['pulsestt_q'].describe()
    megh['pulsestt_v'].describe()
    megh['MPCE_MRP'].describe()
    tura_Data = megh[megh['division_index'] == 1]
    shillong_Data = megh[megh['division_index'] == 2]
    tura_Data.shape
    tura_Data['MPCE_MRP'].describe()
    shillong_Data['MPCE_MRP'].describe()
    tura_Data[['ricetotal_q', 'wheattotal_q', 'pulsestt_q', 'milkprott_q', 'edibletotal_q']].describe()
    shillong_Data[['ricetotal_q', 'wheattotal_q', 'pulsestt_q', 'milkprott_q', 'edibletotal_q']].describe()
    shillong_Data.shape
# VISUALIZATION
    plt.hist(megh['Age']);
    plt.hist(tura_Data['Age']);
    sns.histplot(x = megh['cerealtot_v'],color = 'green');
    sns.histplot(x = tura_Data['cerealtot_v'], color = 'green');
    sns.histplot(x = megh['pulsestt_v']);
    sns.histplot(x = megh['goatmeat_v']);
    sns.barplot(x = megh['division_index'], y = megh['Age']);
    plt.figure(figsize = (14,8))
    sns.barplot(x = megh['Districts_Name'], y = megh['Age']);
    plt.figure(figsize = (14,8))
    sns.barplot(x = megh['Districts_Name'], y = megh['cerealtot_v']);
    plt.figure(figsize = (14,8))
    sns.barplot(x = megh['Districts_Name'], y = megh['milkprott_v']);
    plt.figure(figsize = (14,8))
    sns.barplot(x = megh['Districts_Name'], y = megh['pulsestt_v']);
    plt.figure(figsize = (14,8))
    sns.barplot(x = megh['Districts_Name'], y = megh['milkprott_q']);
# OUTLIERS
    sns.boxplot(y = 'MPCE_MRP', data = megh);
    sns.boxplot(y = 'pulsestt_v', data = megh);
    sns.boxplot(y = 'milkprott_q', data = megh);
    sns.boxplot(y = 'cerealtot_v', data = megh);
    sns.boxplot(y = 'Age', data = megh);
# milkprott_q variables
    megh['milkprott_q'].min(), megh['MPCE_MRP'].max()
    def remove_outlier (col):
        sorted(col)
        Q1, Q3 = col.quantile([0.25,0.75])
        IQR = Q3-Q1
        lower_range = Q1 - (1.5*IQR)
        upper_range = Q3 + (1.5*IQR)
        return lower_range, upper_range
    remove_outlier(megh['milkprott_q'])
    lowerlimit_milk, upperlimit_milk = remove_outlier(megh['milkprott_q'])
    megh['milkprott_q'] = np.where(megh['milkprott_q'] > upperlimit_milk, upperlimit_milk, megh['milkprott_q'])
    megh['milkprott_q'] = np.where(megh['milkprott_q'] < lowerlimit_milk, lowerlimit_milk, megh['milkprott_q'])
    sns.boxplot(y = 'milkprott_q', data = megh);
    sns.distplot(megh['milkprott_q']);
    lowerlimit_age, upperlimit_age = remove_outlier(megh['Age'])
    megh['Age'] = np.where(megh['Age'] > upperlimit_milk, upperlimit_milk, megh['Age'])
    megh['Age'] = np.where(megh['Age'] < lowerlimit_milk, lowerlimit_milk, megh['Age'])
    sns.boxplot(y = 'milkprott_q', data = megh);
    sns.distplot(megh['milkprott_q']);
    return(1)
    
