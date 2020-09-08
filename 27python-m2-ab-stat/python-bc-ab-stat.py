import statistics

def get_rate_stat(records):
    rates = []
    stat = {"mean": None, "min": None, "max": None, "item_number": 0}
    for record in records:
        rate = record.get_rate()
        if rate:
            rates.append(rate)
    if rates:
        stat = {"mean": statistics.mean(rates), "min": min(rates), "max": max(rates), "item_number": len(rates)}        
    return stat
