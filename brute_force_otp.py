def brute_force_otp(target_otp):
    for guess in range(10000):  
        otp = str(guess).zfill(4) 
        print(f"Trying OTP: {otp}")
        if otp == target_otp:
            print(f"OTP matched: {otp}")
            return otp
    print("OTP not found.")
    return None
target = "1234"
brute_force_otp(target)
