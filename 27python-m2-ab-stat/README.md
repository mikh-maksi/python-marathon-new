import statistics  

def get_rate_stat(records):  
&nbsp;&nbsp;&nbsp;&nbsp;rates = []  
&nbsp;&nbsp;&nbsp;&nbsp;stat = {"mean": None, "min": None, "max": None, "item_number": 0}  
&nbsp;&nbsp;&nbsp;&nbsp;for record in records:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate = record.get_rate()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if rate:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rates.append(rate)  
&nbsp;&nbsp;&nbsp;&nbsp;if rates:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stat = {"mean": statistics.mean(rates), "min": min(rates), "max": max(rates), "item_number": len(rates)}         
&nbsp;&nbsp;&nbsp;&nbsp;return stat  
