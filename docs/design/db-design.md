# 数据库设计说明

详细的字段说明, 见对应的 models.py

## 公共组件 base

#### Scenaio 业务类型表

业务类型信息的森林结构. 目前有 2 棵树:

- 婚礼人 expert
- 场地布置 std_product

更多说明:

1. name 与 parent 字段, 可读, 可改.
2. sid 是代码的识别码, 运营人员只读.
3. 没有新增权限, 即, 不允许运营人员新增大类信息. 代码没有对应类别的处理规则, 新增无意义
4. 没有删除权限. 

可扩展性:

1. 增加 status 字段, 标识是否对用户呈现. 即, 懒惰删除功能.
