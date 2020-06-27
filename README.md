# COVID-Internet-Speed-Analysis
During the initial stages of lockdown, home internet speeds across the US took a major hit. For a school statistics project, I decided to perform a test to determine whether internet speeds were significantly less than advertised, or it was simply due to imagination.

### Objectives:
AT&T U-verse offers an internet plan titled Internet 45, which boasts download speeds of 45 megabits per second. Many households have been noticing a significant decrease in internet speeds as people stay home and practice self-isolation with their families. The goal of this project is to determine whether AT&T’s promise of 45 mbps is accurate in a time when household internet usage is at unprecedented levels, as a large portion of the workforce in this area practices work-from-home.

### Data Description
Data was collected using a Unix tool created by Ookla (the makers of speedtest.net) called speedtest-cli to calculate download and upload speeds. Data was analyzed using a python script that parses through the outputted csv file from the speedtest tool and calculates the p-value for a one sample t-test on the download speeds of 50 samples. The shell script 'run.sh' was executed 5 times throughout a single day (11 am, 2 pm, 5 pm,  7 pm, 9 pm).

### Data
The raw data is in 'speedstats.csv', which was outputted from the shell script. Unrelated information such as ping and distance was trimmed off. Download speeds were recorded in bits per second.


### Null and Alternative Hypotheses
The goal of this project is to determine whether internet speeds collected during a data of normal data usage is less than AT&T U-verse’s claim of 45 mbps. Therefore, the null hypothesis for this test was H<sub>0</sub>: μ=45,000,000.00 bits per second and the alternative hypothesis was H<sub>1</sub>: μ<45,000,000.00 bits per second. The shell script recorded download speeds in bits per second, so to keep the units consistent, the hypotheses were also defined in bits per second. The null hypothesis is that the distribution of download speeds recorded during a single day has a mean equal to 45,000,000 bits per second, which is what AT&T U-verse claims. The alternative hypothesis is that the sample mean is less than 45,000,000 bits per second, which means the internet provider was underdelivering at the time of the test.

### Test Statistic, Conclusion, P-value
The python program 'DataCollection.py' parses through the csv and calculates the mean, standard deviation, test statistic and p-values. It utilizes the python library scipy to calculate the p-value for a one sample t-test. It reads from the outputted csv file using the pandas library and performs a t-test on the ‘Download’ column of the file.

The sample mean for the data was 16,338,643.06 bits per second (about 16.34 mpbs) and the sample standard deviation was 4,425,383.20 bits per second (about 4.43 mbps). Using the formula t<sub>0</sub>=(x-μ)/√(s<sup>2</sup>/n)  for a one sample t-test, the resulting test statistic was t<sub>0</sub>=-45.80. The p-value generated was 6.96 x 10<sup>-42</sup>. I chose an alpha value of 0.05. Below is the t distribution of the data with the p-value plotted on it. Since the p-value was significantly small, the online graphic utility used to generate this distribution labels the p-value as 0.
 
Because the p-value was significantly less than the significance level of 0.05, we have strong evidence to reject the null hypothesis. Therefore, this test concludes that from data collected throughout a full weekday, there is significant evidence to reject AT&T U-verse’s claim that it provides internet speeds of 45 megabits per second.

## References
Johnston, N. (n.d.). StatDistributions.com. Retrieved from http://www.statdistributions.com/t/
