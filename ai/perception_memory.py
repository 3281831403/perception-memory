"""AI 感知与记忆：视锥、遮挡与队伍隔离：待实现的核心模块。"""


def in_frustum(angle_h, angle_v, fov_h, fov_v):
    """水平与垂直视锥同时判定。"""
    raise NotImplementedError

def visible_hits(blocked):
    """多层遮挡过滤后返回可见碰撞体下标。"""
    raise NotImplementedError

def sound_attenuation(distance, wall_factor):
    """听觉事件按距离与墙体隔音系数衰减。"""
    raise NotImplementedError

def memory_decay(value, dt, half_life):
    """记忆按半衰期衰减。"""
    raise NotImplementedError

def team_visible(observer_team, target_team):
    """队伍感知隔离：同队才共享。"""
    raise NotImplementedError

def sweep_covers(start, end, target):
    """连续扫掠覆盖目标角度。"""
    raise NotImplementedError

def priority_score(distance, noise):
    """按距离与噪音计算目标优先级。"""
    raise NotImplementedError

def grass_blocks(observer_in_grass, target_in_grass):
    """草丛遮蔽对观察者与目标双方生效。"""
    raise NotImplementedError

def state_hysteresis(state, score, enter, exit_score):
    """追击/搜索状态滞回。"""
    raise NotImplementedError

def unified_timestamp(tick, tick_rate):
    """批量感知使用统一时间戳。"""
    raise NotImplementedError
