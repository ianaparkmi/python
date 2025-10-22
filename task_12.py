basic = 24.99
minutes_free = 60
sms_free = 30
internet_free = 1024
minute_extra = 0.89
sms_extra = 0.59
internet_extra = 0.79

used_minutes = int(input("Minutes used: "))
used_sms = int(input("SMS used: "))
used_internet = int(input("Internet used (MB): "))

extra_minutes = 0
if used_minutes > minutes_free:
    extra_minutes = used_minutes - minutes_free
extra_sms = 0
if used_sms > sms_free:
    extra_sms = used_sms - sms_free
extra_internet = 0
if used_internet > internet_free:
    extra_internet = used_internet - internet_free

cost_minutes = extra_minutes * minute_extra
cost_sms = extra_sms * sms_extra
cost_internet = extra_internet * internet_extra
total = basic + cost_minutes + cost_sms + cost_internet
print("\n--- Your Bill ---")
print("Basic plan:", basic, "rub")
if extra_minutes > 0:
    print("Extra minutes:", cost_minutes, "rub")
if extra_sms > 0:
    print("Extra SMS:", cost_sms, "rub")
if extra_internet > 0:
    print("Extra internet:", cost_internet, "rub")
print(f"Sum all extra: {cost_minutes+cost_sms+cost_internet} rub")
print("Total:", total, "rub") 