from classifier import predict
samples = [
    'Stock market soars as tech earnings beat expectations',
    'Local team wins championship after dramatic overtime',
    'Government passes new education reform bill affecting millions',
    'New movie breaks box office records worldwide',
    'Scientists discover new method for renewable energy storage'
]
for s in samples:
    print(s[:60], '->', predict(s))
