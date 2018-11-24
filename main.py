import pandas as pd
from urllib import parse

#create dataframe from excel file
df = pd.read_excel("C:\\Users\\Milan Shah\\shubham\\dummy.xls",sheet_name = 'Sheet1')

#iterating through each row in csv file
for index, row in df.iterrows():
	#To get params(arguments) from url
	params = dict(parse.parse_qsl(parse.urlsplit(row['secondannualfee']).query))
	
	if "utm_campaign" in params:
		#to split string
		list_campaign = params['utm_campaign'].split('-')

		#To getcampaign name
		if "twlnew" in list_campaign:
			key_index = list_campaign.index("twlnew")
			campaign_name = ''
			for idx,val in enumerate(list_campaign[:key_index+1]):
				campaign_name += val.title()
				if idx < key_index:
					campaign_name += "-"  
			print(campaign_name)
		else:
			print("found no key word")
	else:
		print("found no no utm_campaign")
	