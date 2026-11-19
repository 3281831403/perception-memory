"""AI 感知与记忆：视锥、遮挡与队伍隔离。"""


def in_frustum(angle_h, angle_v, fov_h, fov_v):
    """水平与垂直视锥同时判定。

    ``fov_h`` / ``fov_v`` 为完整视场角，目标需要同时落在水平与垂直
    半视场角之内才算可见。
    """
    return abs(angle_h) <= fov_h / 2.0 and abs(angle_v) <= fov_v / 2.0


def visible_hits(blocked):
    """多层遮挡过滤后返回可见碰撞体下标。

    ``blocked`` 是逐层遮挡结果：每一层对每个碰撞体给出是否被挡住。
    射线必须穿透所有层才能看到碰撞体，因此任意一层挡住即不可见。
    也接受单层的扁平布尔列表。
    """
    if not blocked:
        return []
    if isinstance(blocked[0], (list, tuple)):
        layers = blocked
    else:
        layers = [blocked]
    hit_count = len(layers[0])
    return [
        index
        for index in range(hit_count)
        if not any(layer[index] for layer in layers)
    ]


def sound_attenuation(distance, wall_factor):
    """听觉事件按距离与墙体隔音系数衰减。

    ``wall_factor`` 是单位距离的隔音强度，距离越远、墙体越厚，
    听到的强度越低。
    """
    return 1.0 / (1.0 + distance * wall_factor)


def memory_decay(value, dt, half_life):
    """记忆按半衰期衰减。"""
    return value * (0.5 ** (dt / half_life))


def team_visible(observer_team, target_team):
    """队伍感知隔离：同队才共享。"""
    return observer_team == target_team


def sweep_covers(start, end, target):
    """连续扫掠覆盖目标角度。

    用一帧内的起止角度构成的连续扫掠区间代替固定轮询，目标角度
    落在区间内即视为被覆盖。
    """
    low, high = min(start, end), max(start, end)
    return low <= target <= high


def priority_score(distance, noise):
    """按距离与噪音计算目标优先级。

    越近、越吵的目标得分越高；距离加一避免除零并平滑近身目标。
    """
    return noise / (distance + 1.0)


def grass_blocks(observer_in_grass, target_in_grass):
    """草丛遮蔽对观察者与目标双方生效。"""
    return observer_in_grass or target_in_grass


def state_hysteresis(state, score, enter, exit_score):
    """追击/搜索状态滞回。

    进入追击需要达到较高的 ``enter`` 阈值，退出追击则要跌破更低的
    ``exit_score`` 阈值，避免在阈值附近来回抖动。
    """
    if state == "chase":
        return "chase" if score >= exit_score else "search"
    return "chase" if score >= enter else "search"


def unified_timestamp(tick, tick_rate):
    """批量感知使用统一时间戳。"""
    return tick / tick_rate
