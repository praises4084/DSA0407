import scipy.stats as stats
import numpy as np

data_drug = np.array([3, 5, 2, 6, 4, 8, 1, 7, 3, 5, 2, 6, 4, 8, 1, 7, 3, 5, 2, 6, 4, 8, 1, 7, 3, 5, 2, 6, 4, 8, 1, 7, 3, 5, 2, 6, 4, 8, 1, 7, 3, 5, 2, 6, 4, 8, 1, 7])

data_placebo = np.array([2, 4, 1, 5, 3, 7, 2, 6, 4, 8, 1, 5, 3, 7, 2, 6, 4, 8, 1, 5, 3, 7, 2, 6, 4, 8, 1, 5, 3, 7, 2, 6, 4, 8, 1, 5, 3, 7, 2, 6, 4, 8, 1, 5, 3, 7, 2, 6, 4, 8])

def calculate_confidence_interval(data):
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  
    sample_size = len(data)
    
    critical_value = stats.norm.ppf(0.975)  
    margin_of_error = critical_value * (std_dev / np.sqrt(sample_size))
    confidence_interval = (mean - margin_of_error, mean + margin_of_error)
    
    return confidence_interval

confidence_interval_drug = calculate_confidence_interval(data_drug)
confidence_interval_placebo = calculate_confidence_interval(data_placebo)

print("Sample Data for Drug Group:", data_drug)
print("95% Confidence Interval for Drug Group:", confidence_interval_drug)

print("\nSample Data for Placebo Group:", data_placebo)
print("95% Confidence Interval for Placebo Group:", confidence_interval_placebo)
