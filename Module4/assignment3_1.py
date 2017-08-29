import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import assignment2_helper as helper

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


# Do * NOT * alter this line, until instructed!
#scaleFeatures = False
#For Lab Question 3:
scaleFeatures = True

# TODO: Load up the dataset and remove any and all
# Rows that have a nan. You should be a pro at this
# by now ;-)
#
# QUESTION: Should the id column be included as a
# feature?
#
# .. your code here .. 
raw_data = pd.read_csv('Datasets/kidney_disease.csv', sep=',')

raw_data = raw_data.dropna(axis=0)  # remove any row with nans

# Create some color coded labels; the actual label feature
# will be removed prior to executing PCA, since it's unsupervised.
# You're only labeling by color so you can see the effects of PCA
labels = ['red' if i=='ckd' else 'green' for i in raw_data.classification]

# TODO: For the remaining 10 nominal features, properly encode them by as 
#explained in the Feature Representation section by creating new, boolean 
#columns using Pandas .get_dummies(). You should be able to carry that out 
#with a single line of code. Run your assignment again and see if your 
#results have changed at all:
#
# .. your code here ..

raw_data.rbc.unique()
#array(['normal', 'abnormal'], dtype=object)
raw_data.pc.unique()
#array(['abnormal', 'normal'], dtype=object)
raw_data.pcc.unique()
#array(['present', 'notpresent'], dtype=object)
raw_data.ba.unique()
#array(['notpresent', 'present'], dtype=object)
raw_data.htn.unique()
#array(['yes', 'no'], dtype=object)
raw_data.dm.unique()
#array(['no', 'yes'], dtype=object)
raw_data.cad.unique()
#array(['no', 'yes'], dtype=object)
raw_data.appet.unique()
#array(['poor', 'good'], dtype=object)
raw_data.pe.unique()
#array(['yes', 'no'], dtype=object)
raw_data.ane.unique()
#array(['yes', 'no'], dtype=object)

raw_data.rbc = pd.get_dummies(raw_data.rbc).normal
raw_data.pc = pd.get_dummies(raw_data.pc).abnormal
raw_data.pcc = pd.get_dummies(raw_data.pcc).present
raw_data.ba = pd.get_dummies(raw_data.ba).notpresent
raw_data.htn = pd.get_dummies(raw_data.htn).yes
raw_data.dm = pd.get_dummies(raw_data.dm).no
raw_data.cad = pd.get_dummies(raw_data.cad).no
raw_data.appet = pd.get_dummies(raw_data.appet).poor
raw_data.pe = pd.get_dummies(raw_data.pe).yes
raw_data.ane = pd.get_dummies(raw_data.ane).yes

df = raw_data.drop(['id', 'classification'], axis=1) 

#df.drop(['Cochice', 'Pima'])

# TODO: Print out and check your dataframe's dtypes. You'll might
# want to set a breakpoint after you print it out so you can stop the
# program's execution.
#
# You can either take a look at the dataset webpage in the attribute info
# section: https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease
# or you can actually peek through the dataframe by printing a few rows.
# What kind of data type should these three columns be? If Pandas didn't
# properly detect and convert them to that data type for you, then use
# an appropriate command to coerce these features into the right type.
#
# .. your code here ..
df.dtypes
#exit()
#output: 
#    age      float64
#    bp       float64
#    sg       float64
#    al       float64
#    su       float64
#    rbc        uint8
#    pc         uint8
#    pcc        uint8
#    ba         uint8
#    bgr      float64
#    bu       float64
#    sc       float64
#    sod      float64
#    pot      float64
#    hemo     float64
#    pcv       object
#    wc        object
#    rc        object
#    htn        uint8
#    dm         uint8
#    cad        uint8
#    appet      uint8
#    pe         uint8
#    ane        uint8
#    dtype: object

df.pcv = pd.to_numeric(df.pcv, errors='coerce')
df.wc = pd.to_numeric(df.wc, errors='coerce')
df.rc = pd.to_numeric(df.rc, errors='coerce')

# TODO: PCA Operates based on variance. The variable with the greatest
# variance will dominate. Go ahead and peek into your data using a
# command that will check the variance of every feature in your dataset.
# Print out the results. Also print out the results of running .describe
# on your dataset.
#
# Hint: If you don't see all three variables: 'bgr','wc' and 'rc', then
# you probably didn't complete the previous step properly.
#
# .. your code here ..
df.describe()

# TODO: This method assumes your dataframe is called df. If it isn't,
# make the appropriate changes. Don't alter the code in scaleFeatures()
# just yet though!
#
# .. your code adjustment here ..
if scaleFeatures: df = helper.scaleFeatures(df)


# TODO: Run PCA on your dataset and reduce it to 2 components
# Ensure your PCA instance is saved in a variable called 'pca',
# and that the results of your transformation are saved in 'T'.
#
# .. your code here ..
from sklearn.decomposition import PCA

pca = PCA(n_components=2, svd_solver='full')
pca.fit(df)
PCA(copy=True, n_components=2, whiten=False)
T = pca.transform(df)

# Plot the transformed data as a scatter plot. Recall that transforming
# the data will result in a NumPy NDArray. You can either use MatPlotLib
# to graph it directly, or you can convert it to DataFrame and have pandas
# do it for you.
#
# Since we've already demonstrated how to plot directly with MatPlotLib in
# Module4/assignment1.py, this time we'll convert to a Pandas Dataframe.
#
# Since we transformed via PCA, we no longer have column names. We know we
# are in P.C. space, so we'll just define the coordinates accordingly:
ax = helper.drawVectors(T, pca.components_, df.columns.values, plt, scaleFeatures)
T = pd.DataFrame(T)
T.columns = ['component1', 'component2']
T.plot.scatter(x='component1', y='component2', marker='o', c=labels, alpha=0.75, ax=ax)

plt.show()
