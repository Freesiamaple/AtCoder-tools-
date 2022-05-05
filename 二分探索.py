def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    return #ここに条件入れる　例) arg+arg**2<n


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    https://twitter.com/meguru_comp/status/697008509376835584?s=20
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok 