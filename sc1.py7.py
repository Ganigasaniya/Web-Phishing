import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn.feature_selection import mutual_info_classif as MIC
df=pd.read_csv("phishing.csv")
x=df.drop(['class','Index'],axis=1)
df['class']=df['class'].fillna(df['class'].median())
y=df['class']
mi_score = MIC(x,y,random_state=1)
l=[]
c=0
l1=list(x.columns.values.tolist())
print(len(mi_score))
l2=[]
for i in mi_score:
  if(i>0.05):
    l.append(c)
    l2.append(l1[c])
  c=c+1
#arr = np.where(mi_score>7)[0]
print(c)
print(l2)
print(mi_score)
str=" https://www.f_Efw.com"
ps=0
sd=0
htt=0
uoa=0
webt=0
##########################################################################################
#prefix and sufix 
from urllib.parse import urlparse
dash=urlparse(str).netloc
if("-" not in dash):
    ps=0
    print("True")
else:
    ps=1
    print("False")

##########################################################################################
#subdomains
from urllib.parse import urlparse

def count_dots_in_domain(url):
    try:
        # Parse the URL to get the hostname
        parsed_url = urlparse(url)
        hostname = parsed_url.netloc

        # Count the dots in the hostname
        dot_count = hostname.count('.')
        
        return dot_count
    except ValueError:
        # Handle invalid URLs
        return -1
# Example usage
url =str
dot_count = count_dots_in_domain(url)

if dot_count >= 0:
    print(f"Number of dots in the domain: {dot_count}")
    sd=-1

else:
    print("Invalid URL")
    sd=1
######################################################################################3##########
#url of anchor
from urllib.parse import urlparse

def calculate_anchor_percentage(url):
    # Parse the URL using urlparse
    parsed_url = urlparse(url)
    
    # Extract the anchor (fragment) from the parsed URL
    anchor = parsed_url.fragment
    
    # Calculate the length of the anchor
    anchor_length = len(anchor)
    
    # Calculate the total length of the URL (excluding the anchor)
    total_length = len(url) - anchor_length
    
    # Calculate the percentage
    if total_length > 0:
        percentage = (anchor_length / total_length) * 100
    else:
        percentage = 0.0  # Handle division by zero
    
    return percentage

# Example usage:
url_to_parse = str
percentage = calculate_anchor_percentage(url_to_parse)

print(f"The anchor represents {percentage:.2f}% of the URL.")

if(percentage<31):
    uoa=0
elif(percentage>=31 and percentage<=67):
    uoa=-1
else:
    uoa=1
###############################################################################################################
import requests

def check_https(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            if response.url.startswith("https://"):
                print(f"{url} is using HTTPS.")
                htt=1
            else:
                print(f"{url} is not using HTTPS.")
                htt=0
        else:
            print(f"Failed to access {url}.")
            htt=-1
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
check_https(str)
############################################################################################
para=[ps,sd,uoa,htt,webt]
cols=df[['PrefixSuffix-', 'SubDomains', 'HTTPS', 'AnchorURL', 'WebsiteTraffic']]
npara=np.array([para])
npara=np.array([para])
npara=npara.reshape(1,-1)
print(npara)
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
model_random_forest = RandomForestClassifier(n_estimators=350,random_state=0)
X_train, X_test, y_train, y_test = train_test_split(cols,y,test_size=0.3,random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model=model_random_forest.fit(X_train,y_train)
y_predicted = model.predict(X_test)
pred=model.predict((npara))
accuracy = accuracy_score(y_test,y_predicted)
print('model accuracy: {0:4f}'.format(accuracy))
print(pred)