## 关键进展与遗留问题


#### 供应商管理

###### SLA

通过 SLA 区分供应商的星级.

SLA 目前只设 order, name, desc 三个基本字段.
其中, order 字段用于排序, 是优先级的体现, 方便程序对比 2 个等级的好坏.
用户常用字段为 name

###### 供应商信息

分为基本信息 + 公司主页(图文介绍)
其中, 主页后续再纳入计划.

不包含字段 营业时间

地址信息, 后续可能需要跟高德或者百度地图结合.

目前只支持上传一张图片, 后续可能需要支持多张. 室内外, 经典案例

是否支持站外的供应商主页, 一些大的供应商有自己的公司网站. 系统中暂未考虑单独支持该字段.

#### 专业技能管理

1. 化妆师 / 摄影师的归属地信息.

    Expert 中增加归属地字段, 或者关联到 privider, 在 provider 中体现归属地信息

2. 化妆师 / 摄影师的等级信息

    level, 类似供应商的 level, 可以考虑也放在 provider 中实现.

#### 归属地信息

关键, STD 产品, 选择供应商阶段, 直接关注供应商归属地即可, 选产品阶段不涉及.

专业技能的产品, 选人的阶段, 就已经包含了归属地信息.

专业之技能, 是否需要关联到 provider?

为了设计而设计, 意义不大.

专业技能与标准化产品的购买, 也没有统一的必要.

provider 与 STD product 整合为 1 个 APP

Expert 自身构成一个 APP

#### 档期

专业技能, 选择 服务提供者 时, 存在档期的概念.

档期需要结合订单状态来处理.

#### 抢购摄影师与拆单

一套婚礼方案, 从筛选到决定, 可能会持续很长时间. 几天, 甚至几周.

好的摄影师 / 司仪要抢购. 尤其是十一假期这种结婚高峰期.

花艺则比较复杂, 可以慢慢筛选, 不着急决定.

所以, 用户拆单的概率很高.

一次购买就是一套完整的婚礼方案, 概率太低.

#### 多婚礼方案的支持

专业的婚礼策划师, 很容易成为网站的重度用户.

从运营角度看, 可能是最有价值的核心目标用户群体.

所以, 是否需要重点照顾这个群体.

网站跟婚礼策划师, 是不是竞争的关系.
