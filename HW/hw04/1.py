def fab(n):
    pre = 1
    now = 1
    count = 0
    while count < n:
        pre, now = now,pre + now
        count += 1
    return now
fab(5)