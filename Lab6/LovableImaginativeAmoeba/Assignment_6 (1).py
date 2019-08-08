import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import math

def read_dataset(file_name):
  return pd.read_csv(file_name)

dataset = read_dataset("banknote.csv")
trainset, testset = train_test_split(dataset, test_size=0.2)

total_item = trainset['y'].count()
forge_means = np.mean(trainset[trainset['y'] == 0], axis=0)
forge_variances = np.var(trainset[trainset['y'] == 0], axis=0)
forge_prob = trainset['y'][trainset['y'] == 0].count() / total_item 
auth_means = np.mean(trainset[trainset['y'] == 1], axis=0)
auth_variances = np.var(trainset[trainset['y'] == 1], axis=0)
auth_prob = trainset['y'][trainset['y'] == 1].count() / total_item

def gaussian_probability(x, means, variances):
  #variance is a value which is calculated in square units. So it doesn't need to be squared again.
  total_prob = 1;
  
  for i in range(4):
    total_prob *= (1/ math.sqrt(2 * math.pi * variances[i])) * (math.exp(-1 * ((((x[i] - means[i]) ** 2) / (2 * variances[i])))))
  return total_prob

def target_value(x):
  p_x_given_a = gaussian_probability(x, auth_means, auth_variances)
  p_x_given_f = gaussian_probability(x, forge_means, forge_variances)
  p_a_given_x = (p_x_given_a * auth_prob) / ((p_x_given_a * auth_prob) + (p_x_given_f * forge_prob))
  if p_a_given_x > 0.5:
    return 1
  else:
    return 0

TrNeg = 0
FlNeg = 0
TrPos = 0
FlPos = 0

for index, row in testset.iterrows():
  print(row)
  predict_target = target_value(row)
  print("Predicted Target: ", predict_target)
  if row['y'] == 0:
    if predict_target == 0:
      TrNeg += 1
    else:
      FlPos += 1
  else:
    if predict_target == 1:
      TrPos += 1
    else:
      FlNeg += 1

print("Errors: ", TrNeg, FlPos, TrPos, FlNeg)
