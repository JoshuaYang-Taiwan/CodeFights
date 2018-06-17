def lateRide(n):
    hour = n // 60
    minute = n % 60
    return hour//10 + hour%10 + minute//10 + minute%10
