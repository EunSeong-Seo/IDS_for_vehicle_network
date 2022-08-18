import pandas as pd
import warnings
from preprocessing import make_train_xy_df, make_train_xy_df_with_D
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
warnings.filterwarnings('ignore')

# set data paths
can_dataset_path_for_D_1 = 'dataset/Pre_train_D_attack_1.csv'
can_dataset_path_for_D_2 = 'dataset/Pre_train_D_attack_2.csv'

# Load dataset
X_train, Y_train = make_train_xy_df_with_D(can_dataset_path_for_D_1)
X_test, Y_test = make_train_xy_df_with_D(can_dataset_path_for_D_2)


# Use Decision Tree
DT = DecisionTreeClassifier()
DT = DT.fit(X_train,Y_train)
Y_pred = DT.predict(X_test)

print(metrics.accuracy_score(Y_test, Y_pred))
print(metrics.confusion_matrix(Y_test, Y_pred))
print(metrics.classification_report(Y_test, Y_pred))