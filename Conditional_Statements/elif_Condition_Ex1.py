billamt=400

if billamt>=800:
    print("40% discount coupon applied")
elif billamt>=600 and billamt<800:                  #billamt>=600 and billamt<800:......the range between is 600 to 800
    print("20% discount coupnn applied")
elif billamt>=500 and billamt<600:                  #billamt>=500 and billamt<600:......the range between is 500 to 600
    print("15% discount coupon applied")
elif billamt>=300 and billamt<500:                  #billamt>=300 and billamt<500:......the range between is 300 to 500
    print("5% discount coupon applied")
elif billamt>=100 and billamt<300:                  #billamt>=100 and billamt<300:......the range between is 100 to 300
    print("No Discount")
else:
    print("Pay Full Amount")
