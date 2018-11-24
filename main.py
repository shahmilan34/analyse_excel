import pandas as pd
from urllib import parse

#create dataframe from excel file
df = pd.read_excel("C:\\Users\\Milan Shah\\shubham\\dummy.xls",sheet_name = 'Sheet1')
keys_list = ['twlnew','intent']

#iterating through each row in csv file
for index, row in df.iterrows():
	#To get params(arguments) from url
	params = dict(parse.parse_qsl(parse.urlsplit(row['secondannualfee']).query))
	
	if "utm_campaign" in params:
		#to split string
		list_campaign = params['utm_campaign'].split('-')

		#To getcampaign name
		for key_list in keys_list:
			#To check key exist in campaign
			if key_list in list_campaign:
				#Get index of key
				key_index = list_campaign.index(key_list)
				campaign_name = ''
				#To create full campaign name
				for idx,val in enumerate(list_campaign[:key_index+1]):
					#uppercase first char of word
					campaign_name += val.title()
					#append - in campaign name
					if idx < key_index:
						campaign_name += "-"  
				df.loc[index,'Campaign Name'] = campaign_name
	else:
		df.loc[index,'Campaign Name'] = 'No Attribute'

df.to_csv('.\\new_dummy.csv', sep=',', encoding='utf-8')
