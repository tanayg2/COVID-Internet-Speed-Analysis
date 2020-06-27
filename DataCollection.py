from scipy import stats
from statistics import stdev
import pandas as pd

def main():
	popMean = input("Enter population mean (in bits): ")
	alpha = input("Enter alpha value: ")
	speedTTest(float(popMean), float(alpha))

def speedTTest(popMean, alpha):
	dataframe = pd.read_csv('speedStats2.csv')
	downloads = dataframe['Download'].values.tolist()

	testStat = (sampMean - popMean)/(np.sqrt(dev*dev/len(downloads)))
	print("t =", testStat)

	p = stats.ttest_1samp(downloads, popMean)[1]
	reject = p < alpha

	print("p-value =", p)

	if (reject):
		print("At a ", (1-alpha)*100, "% confidence level, we reject the null hypothesis that the sample mean is equal to ", popMean)
	else:
		print("At a ", (1-alpha)*100, "% confidence level, we fail to reject the null hypothesis that the sample mean is equal to ", popMean)

main()
