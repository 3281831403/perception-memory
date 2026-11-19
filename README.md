# AI 感知与记忆：视锥、遮挡与队伍隔离

巡逻守卫的视野一进草丛就失明：视锥只看水平角、遮挡只打第一个碰撞体、听觉不算隔音、记忆立即清零、队伍不隔离、0.5 秒轮询漏目标、优先级不排序、草丛只对玩家生效、状态机抖动、批量更新没有统一时间戳。

## 目录结构

```
README.md
conftest.py
.gitignore
ai/__init__.py
ai/perception_memory.py
tests/test_perception_memory.py
```

## 当前状态

`ai/perception_memory.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_perception_memory.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 水平与垂直视锥同时参与
2. 遮挡射线做多层过滤
3. 听觉按墙体隔音衰减
4. 目标丢失后记忆按半衰期衰减
5. 队伍感知隔离
6. 连续扫掠检测替代轮询
7. 按距离与噪音排序目标优先级
8. 草丛遮蔽对双方生效
9. 追击/搜索状态滞回
10. 批量感知统一时间戳

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `ai/perception_memory.py`
后 15 条用例应全部通过。
