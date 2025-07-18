def token_mint(info, args):
    tick = args['a'][0]
    assert type(tick) is str
    assert len(tick) > 0 and len(tick) < 42
    assert tick[0] in string.ascii_uppercase
    assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')

    assert args['f'] == 'token_mint'
    assert args['f'] in get('asset', 'functions', [], tick)

    value = int(args['a'][1])
    assert value > 0
    sender = info['sender']
    handle = handle_lookup(sender)
    addr = handle or sender

    balance = get(tick, 'balance', 0, addr)
    balance += value
    total = get(tick, 'total', 0, addr)
    total += value

    put(addr, tick, 'balance', balance, addr)
    put(addr, tick, 'total', total)
