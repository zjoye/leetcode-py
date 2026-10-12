## 🚀 快速开始 (Quick Start)

### 1. 环境准备

推荐在项目内部创建虚拟环境以隔离依赖：


``` Bash
# 1. 创建虚拟环境 (在项目根目录下执行)
python -m venv venv

# 2. 激活虚拟环境
# ▹ macOS / Linux:
source venv/bin/activate
# ▹ Windows (CMD / PowerShell):
venv\Scripts\activate

# 3. 安装所需依赖 (pytest, ruff 等)
pip install -r requirements.txt
```

### 2. 测试用例使用说明

本项目使用 `pytest` 的 `@pytest.mark.parametrize` 参数化注解。核心优势：你不需要写任何对象的实例化和方法调用代码，只需将测试数据填入数组即可。


#### 标准刷题模板

新建文件时，按以下结构复制粘贴。你只需要关注题目逻辑和测试数据：

``` Python
import pytest
from typing import List

# ================= 1. 粘贴力扣原题代码 =================
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        return 0  # 此处编写核心逻辑

# ================= 2. 配置测试用例 =================
@pytest.mark.parametrize("args, expected", [
    # 格式规范: ( (参数1, 参数2, 参数3...), 预期结果 )
    ( ([4,2,8], [-1,0,1], 2), 10 ),
    ( ([5,4,3], [1,1,0], 2),  9 ),
    ( ([4,7,13], [-1,-1,0], 2), 30 ),
])
def test_solution(args, expected):
    # ================= 3. 修改这里的方法名 =================
    assert Solution().maxProfit(*args) == expected
```

> **⚠️ 避坑指南：单参数的“逗号”法则**
>
> 如果题目**只有一个输入参数**（如传入一个字符串），由于 Python 的基础语法限制，**必须在参数后加一个逗号**使其成为真正的元组，或者直接使用**列表**，否则 `*args` 会将字符串错误解包。
>
> - ❌ **错误写法**：`( ("111000"), 2 )` —— *Python 会忽略括号将其视为纯字符串，导致解包报错。*
> - ✅ **正确写法 1（元组加逗号）**：`( ("111000",), 2 )`
> - ✅ **正确写法 2（改用列表，防错推荐）**：`( ["111000"], 2 )`