employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

ans = {}
for employee in employees:
    ans[employee] = defaults

print(ans)
