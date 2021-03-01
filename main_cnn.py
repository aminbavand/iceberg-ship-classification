import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from data_construction import data_construction
from model import getModel
from tensorflow import keras



train,X_train= data_construction()



target_train=train['is_iceberg']

X_train_cv, X_valid, y_train_cv, y_valid = train_test_split(X_train, target_train, random_state=1, train_size=0.75)




gmodel=getModel()
gmodel.fit(X_train_cv, y_train_cv,
	  batch_size=24,
	  epochs=50,
	  verbose=1,
	  validation_data=(X_valid, y_valid))





score = gmodel.evaluate(X_valid, y_valid, verbose=1)
print('validation loss:', score[0])
print('validation accuracy:', score[1])

y_pred = gmodel.predict(X_valid)
plt.plot(y_pred, 'bo')
plt.show()



predicted_test=gmodel.predict_proba(X_test)


submission = pd.DataFrame()
submission['id']=test['id']
submission['is_iceberg']=predicted_test.reshape((predicted_test.shape[0]))
submission.to_csv('sub.csv', index=False)



