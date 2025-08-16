def count_pages(n):
    cnt = [0] * 10
    start, end, digit = 1, n, 1

    while start <= end:
        while start % 10 != 0 and start <= end:
            for x in str(start):
                cnt[int(x)] += digit
            start += 1

        if start > end:
            break

        while end % 10 != 9 and start <= end:
            for x in str(end):
                cnt[int(x)] += digit
            end -= 1

        q = end // 10 - start // 10 + 1
        for i in range(10):
            cnt[i] += q * digit

        start //= 10
        end //= 10
        digit *= 10

    return cnt


n = int(input())
print(*count_pages(n))
