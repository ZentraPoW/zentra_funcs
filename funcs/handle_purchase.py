
def handle_purchase(info, args):
    assert args['f'] == 'handle_purchase'
    sender = info['sender']
    handle = args['a'][0]
    assert type(handle) is str
    assert set(handle) <= set(string.digits+string.ascii_lowercase+'_')
    assert len(handle) > 4 and len(handle) < 42

    handles = get('handle', 'addr2handles', [], sender)
    if not handles:
        put(handle, 'handle', 'default', handle, sender)

    if handle not in handles:
        handles.append(handle)
        put(handle, 'handle', 'addr2handles', handles, sender)

    put(handle, 'handle', 'handle2addr', sender, handle)
