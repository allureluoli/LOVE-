from nonebot import get_driver, logger

source_group=0
dest_group=0
prefix=0
explict=0

config =[source_group,dest_group,prefix,explict]

#这个配置是让利用外部配置的，那么我需要将其改为内部
#

if 'forwarder_source_group' not in config:
    logger.warning('[转发姬] 未发现配置项 `forwarder_source_group` , 采用默认值: []')
if 'forwarder_dest_group' not in config:
    logger.warning('[转发姬] 未发现配置项 `forwarder_dest_group` , 采用默认值: []')
if 'forwarder_prefix' not in config:
    logger.warning('[转发姬] 未发现配置项 `forwarder_prefix` , 采用默认值: [""]')
if 'forwarder_explict' not in config:
    logger.warning('[转发姬] 未发现配置项 `forwarder_explict` , 采用默认值: [""]')

forwarder_source_group = config[0]
forwarder_dest_group = config[1]
forwarder_prefix = config[2]
forwarder_explict = config[3]