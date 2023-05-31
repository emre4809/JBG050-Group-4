
import pandas as pd
import statsmodels.api as sm
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt




def fit_and_test():
	df = pd.read_pickle("barnet_burglaries_agg_df.pickle")

	full_data = df.T
	# full data has index: months and columns: LSOAS

	months = full_data.index
	LSOAS  = full_data.columns
	n_months = len(months)

	results = []
	print("testing overall performance")
	D = full_data.to_numpy()

	# VAR cannot predict when there are constant columns, ensure that there are no constant columns
	# by adding a tiny amount of noise, this does not impact results on average but allows for easier
	# definition/comparison of models
	D_train = D[:n_months - 1, :].copy()
	noise = 0.000001 * np.random.randn(D_train.shape[0] * D_train.shape[1]).reshape(D_train.shape)
	D_train += noise
	D_test = D[n_months - 1:, :].copy()
	for z in range(1, 80):
		print("Testing VAR with order %s " % z)
		sub_results = {}

		model = sm.tsa.VAR(D_train)
		model_fit = model.fit(z)
		prediction = model_fit.forecast(D_train, steps=1)
		prediction[prediction < 0] = 0  # lower bound prediction
		sub_results["mean_error"] = np.mean(np.abs(prediction - D_test))
		sub_results["order"] = z
		results.append(sub_results)
	results_df = pd.DataFrame(results).set_index("order").sort_values("mean_error", ascending=True)
	print(results_df)



def reduce_dimensionality(_M):
	M = _M.copy().T
	print(M)
	pca = PCA()
	M_pca = pca.fit_transform(M)

	print(M_pca.shape)

	cumulative_var_ratio = np.cumsum(pca.explained_variance_ratio_)
	print(cumulative_var_ratio)
	plt.plot(range(1, len(cumulative_var_ratio) + 1), cumulative_var_ratio, marker='o')
	plt.xlabel('Number of Components')
	plt.ylabel('Cumulative Explained Variance Ratio')
	plt.title('Explained Variance Ratio by Number of Components')
	plt.grid(True)
	plt.show()


