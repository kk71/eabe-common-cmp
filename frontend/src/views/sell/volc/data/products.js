// Shared products data used across ProductsPage, NavBar mega menu, and ProductDetailPage
// Each product has a unique slug for routing

export var productsData = [
  {
    id: 'compute', name: '计算', desc: '弹性高性能计算资源', icon: 'server',
    color: 'var(--color-brand)', bgColor: 'rgba(51,112,255,0.1)',
    items: [
      {
        slug: 'gpu-server',
        name: 'GPU云服务器',
        desc: '搭载高性能GPU的云服务器，适用于AI训练推理、科学计算、图形渲染等场景',
        icon: 'cpu', tag: 'HOT',
        color: 'var(--color-brand)', bgColor: 'rgba(51,112,255,0.1)',
        features: ['A100/H100', '弹性扩缩', '高速互联'],
        detail: {
          banner: '面向AI时代的高性能GPU云计算',
          intro: '羿贝引擎GPU云服务器搭载NVIDIA最新一代A100/H100 GPU，提供强劲的并行计算能力。适用于深度学习训练与推理、高性能计算(HPC)、图形图像渲染、视频转码等GPU密集型场景。结合弹性扩缩、高速RDMA互联网络，助力企业高效完成AI模型训练与推理任务。',
          highlights: [
            { title: '旗舰GPU算力', desc: '搭载NVIDIA A100/H100 Tensor Core GPU，单卡最高提供80GB HBM3显存，支持FP64/FP32/TF32/FP16/INT8多精度计算' },
            { title: '高速RDMA互联', desc: '基于RoCE v2网络，GPU间通信带宽高达400Gbps，满足大规模分布式训练对低延迟高带宽的需求' },
            { title: '弹性按需伸缩', desc: '支持分钟级创建和释放GPU实例，按需/预留/竞价多计费模式灵活组合，有效降低算力成本' },
            { title: '全栈AI工具链', desc: '预装CUDA、cuDNN、NCCL等AI框架，集成PyTorch、TensorFlow等主流训练框架，开箱即用' }
          ],
          specs: [
            { label: 'GPU型号', value: 'NVIDIA A100 80G / H100 80G' },
            { label: '最大GPU数', value: '8卡/实例' },
            { label: 'GPU互联', value: 'NVLink + NVSwitch' },
            { label: '网络带宽', value: '最高 100Gbps' },
            { label: '存储', value: 'NVMe SSD 本地盘' },
            { label: '操作系统', value: 'Ubuntu / CentOS / Windows' }
          ],
          scenarios: [
            { title: '大模型训练', desc: '千亿参数大语言模型预训练与微调，支持多节点分布式并行训练' },
            { title: 'AI推理部署', desc: '高并发低延时的模型推理服务部署，支持动态Batch和模型并行' },
            { title: '科学计算', desc: '分子动力学模拟、气象预测、基因组分析等HPC场景' },
            { title: '图形渲染', desc: '云端实时3D渲染、影视后期特效、建筑可视化' }
          ]
        }
      },
      {
        slug: 'ecs',
        name: '云服务器 ECS',
        desc: '安全稳定、弹性可伸缩的云服务器，支持多种实例规格满足不同业务需求',
        icon: 'server', tag: 'HOT',
        color: 'var(--color-accent)', bgColor: 'rgba(20,201,201,0.1)',
        features: ['多规格可选', '秒级弹性', '高可用'],
        detail: {
          banner: '安全稳定的弹性云服务器',
          intro: '羿贝引擎云服务器ECS提供安全可靠、弹性可伸缩的计算服务，支持通用型、计算型、内存型、高主频型等多种实例规格。内置云监控与安全防护，配合镜像、快照、弹性IP等能力，助力企业快速构建并灵活管理云上业务。',
          highlights: [
            { title: '丰富实例规格', desc: '涵盖通用型、计算型、内存型、GPU型等十余种实例系列，匹配Web服务、数据库、AI训练等不同负载需求' },
            { title: '秒级弹性伸缩', desc: '结合弹性伸缩服务，秒级创建和释放实例，轻松应对业务高峰与低谷，降低资源浪费' },
            { title: '99.975% 可用性', desc: '基于分布式架构，支持跨可用区部署和自动故障迁移，保障业务连续性' },
            { title: '一站式安全防护', desc: '内置DDoS防护、安全组、密钥对管理，配合云安全中心实现全方位安全加固' }
          ],
          specs: [
            { label: 'CPU', value: 'Intel Xeon / AMD EPYC' },
            { label: '内存', value: '最大 3072 GB' },
            { label: '网络', value: '最高 64Gbps' },
            { label: '存储', value: '云盘 / 本地SSD' },
            { label: 'SLA', value: '99.975%' },
            { label: '计费模式', value: '按量 / 预留 / 竞价' }
          ],
          scenarios: [
            { title: 'Web应用托管', desc: '运行企业官网、电商平台、内容管理系统等Web应用' },
            { title: '开发测试环境', desc: '快速创建临时开发测试环境，按需计费节省成本' },
            { title: '数据库运行', desc: '作为MySQL、Redis等数据库的运行宿主，提供高性能IO' },
            { title: '大数据计算', desc: '运行Hadoop、Spark等大数据框架进行海量数据处理' }
          ]
        }
      },
      {
        slug: 'bare-metal',
        name: '弹性裸金属服务器',
        desc: '兼顾物理机性能与云计算便捷性，适合对性能有极致追求的业务场景',
        icon: 'hard-drive',
        color: 'var(--color-yellow)', bgColor: 'rgba(247,186,30,0.1)',
        features: ['物理级性能', '弹性部署', '安全隔离'],
        detail: {
          banner: '物理机性能与云端弹性的完美结合',
          intro: '弹性裸金属服务器(EBM)提供独享物理服务器级别的计算性能，同时具备云计算的弹性和便捷管理能力。无虚拟化开销，无性能损耗，适合对性能、安全隔离有极致需求的高性能计算、数据库及合规类业务场景。',
          highlights: [
            { title: '零虚拟化开销', desc: '独享物理服务器全部算力，无hypervisor性能损耗，适合对计算性能有极致要求的场景' },
            { title: '分钟级交付', desc: '分钟级自动化交付裸金属实例，支持通过API和控制台灵活管理生命周期' },
            { title: '安全物理隔离', desc: '物理级别的资源隔离，满足金融、政务等对安全合规有严格要求的业务场景' },
            { title: '混合组网灵活', desc: '与云服务器ECS、VPC无缝互通，支持公有云与私有云混合部署架构' }
          ],
          specs: [
            { label: 'CPU', value: 'Intel Xeon 最高 128核' },
            { label: '内存', value: '最大 2048 GB DDR5' },
            { label: '存储', value: 'NVMe SSD 最高 30TB' },
            { label: '网络', value: '最高 100Gbps' },
            { label: '隔离级别', value: '物理隔离' },
            { label: '交付时间', value: '分钟级' }
          ],
          scenarios: [
            { title: '高性能数据库', desc: 'Oracle RAC、SAP HANA等对IO和延迟有极高要求的数据库' },
            { title: '安全合规', desc: '金融交易系统、政务系统等需要物理隔离的合规场景' },
            { title: '高性能计算', desc: '基因测序、地震勘探、风洞模拟等HPC场景' },
            { title: '容器宿主机', desc: '作为大规模Kubernetes集群的高性能宿主节点' }
          ]
        }
      },
      {
        slug: 'serverless-function',
        name: '函数服务',
        desc: '无需管理基础设施，按实际使用资源计费的无服务器函数计算托管平台',
        icon: 'zap',
        color: 'var(--color-green)', bgColor: 'rgba(159,219,29,0.1)',
        features: ['事件驱动', '自动扩缩', '按量计费'],
        detail: {
          banner: '无服务器架构，专注业务逻辑',
          intro: '函数服务(vFunction)是事件驱动的无服务器计算平台。用户只需编写核心业务代码，无需管理服务器等基础设施。系统根据请求量自动扩缩至零到千万级并发，按实际函数执行时长和内存用量计费，大幅降低运维成本。',
          highlights: [
            { title: '免运维', desc: '无需管理服务器、操作系统和运行环境，只需专注业务代码开发' },
            { title: '毫秒级弹性', desc: '根据请求量毫秒级自动扩缩，从0到百万并发无需预置资源' },
            { title: '丰富触发器', desc: '支持HTTP、定时任务、消息队列、对象存储等多种事件触发方式' },
            { title: '极致性价比', desc: '按实际调用次数和执行时长计费，空闲时不产生任何费用' }
          ],
          specs: [
            { label: '运行时', value: 'Node.js / Python / Go / Java' },
            { label: '内存', value: '128MB ~ 3072MB' },
            { label: '超时时间', value: '最长 900秒' },
            { label: '并发', value: '单函数百万级' },
            { label: '触发器', value: 'HTTP / Timer / MQ / OSS' },
            { label: '计费', value: '调用次数 + 执行时长' }
          ],
          scenarios: [
            { title: 'API后端', desc: '快速构建RESTful API和微服务后端' },
            { title: '数据处理', desc: '文件上传后自动触发图片处理、视频转码等任务' },
            { title: '定时任务', desc: '定时执行数据清理、报表生成、监控告警等周期性任务' },
            { title: 'IoT数据处理', desc: '处理海量IoT设备上报的消息和事件' }
          ]
        }
      },
      {
        slug: 'auto-scaling',
        name: '弹性伸缩',
        desc: '根据业务需求自动调整计算资源数量，确保应用始终运行在最佳性能状态',
        icon: 'bar-chart',
        color: 'var(--color-brand)', bgColor: 'rgba(51,112,255,0.1)',
        features: ['自动伸缩', '定时策略', '健康检查'],
        detail: {
          banner: '智能弹性，高效利用每一份资源',
          intro: '弹性伸缩服务(AS)根据预设策略自动调整ECS实例数量。支持目标追踪、步进伸缩、定时伸缩等多种策略类型，结合健康检查和冷却机制，确保业务在流量高峰时自动扩容、低谷时自动缩容，实现资源利用率最大化。',
          highlights: [
            { title: '多维伸缩策略', desc: '支持基于CPU利用率、内存使用率、网络流量等指标的目标追踪和步进伸缩' },
            { title: '定时伸缩', desc: '支持Cron表达式配置定时伸缩策略，提前应对可预期的业务高峰' },
            { title: '智能健康检查', desc: '自动检测不健康实例并替换，保障业务持续可用' },
            { title: '与负载均衡集成', desc: '新增实例自动挂载到负载均衡后端组，缩容时平滑移除并等待连接排空' }
          ],
          specs: [
            { label: '伸缩策略', value: '目标追踪 / 步进 / 定时' },
            { label: '最大实例数', value: '2000 台/组' },
            { label: '伸缩速度', value: '分钟级' },
            { label: '冷却时间', value: '自定义 60~86400秒' },
            { label: '健康检查', value: 'ECS + CLB 双重检查' },
            { label: '计费', value: '服务免费，按实例计费' }
          ],
          scenarios: [
            { title: '电商大促', desc: '大促活动前自动扩容至预期峰值，活动结束后平滑缩容节省成本' },
            { title: '游戏开服', desc: '新服上线时自动增加服务器资源，玩家减少后逐步释放' },
            { title: '流媒体直播', desc: '直播高峰期自动扩展编解码和分发资源' },
            { title: '定时批处理', desc: '每日凌晨自动扩容执行ETL任务，完成后自动缩容' }
          ]
        }
      }
    ]
  },
  {
    id: 'network', name: '网络与CDN', desc: '全球加速与网络互联', icon: 'globe',
    color: 'var(--color-accent)', bgColor: 'rgba(20,201,201,0.1)',
    items: [
      {
        slug: 'eip',
        name: '公网IP',
        desc: '弹性、灵活、安全可靠的公网访问服务，支持带宽随时调整',
        icon: 'globe', tag: 'HOT',
        color: 'var(--color-brand)', bgColor: 'rgba(51,112,255,0.1)',
        features: ['弹性带宽', 'BGP多线', 'DDoS防护'],
        detail: {
          banner: '弹性灵活的公网访问能力',
          intro: '公网IP(EIP)提供独立的公网IP地址资源，可灵活绑定到ECS、NAT网关、CLB等资源。支持按流量或按带宽计费，带宽可实时调整，配合DDoS基础防护，保障业务安全稳定地接入互联网。',
          highlights: [
            { title: 'BGP多线接入', desc: '优质BGP多线网络，自动选择最优运营商路由，全国访问低延迟' },
            { title: '带宽弹性调整', desc: '带宽峰值可实时在线调整，无需释放重建，灵活应对业务变化' },
            { title: '灵活绑定解绑', desc: '独立IP资源可随时绑定到不同云资源，支持秒级切换，业务不中断' },
            { title: '安全防护内置', desc: '默认提供5Gbps DDoS基础防护能力，保障公网入口安全' }
          ],
          specs: [
            { label: '带宽', value: '1Mbps ~ 10Gbps' },
            { label: '线路', value: 'BGP多线' },
            { label: '协议', value: 'IPv4 / IPv6' },
            { label: '绑定资源', value: 'ECS / NAT / CLB' },
            { label: '计费', value: '按流量 / 按带宽' },
            { label: 'DDoS防护', value: '基础5Gbps' }
          ],
          scenarios: [
            { title: 'Web服务公网访问', desc: '为ECS实例提供公网访问入口，承载网站和API流量' },
            { title: 'NAT网关出口', desc: '作为NAT网关的出口IP，提供VPC内资源的Internet访问能力' },
            { title: '故障切换', desc: '高可用架构中IP快速切换到备用节点，保障业务连续性' },
            { title: '混合云互联', desc: '作为混合云架构中公有云与本地数据中心的互联出口' }
          ]
        }
      },
      {
        slug: 'clb',
        name: '负载均衡 CLB',
        desc: '高可用流量分发服务，将访问流量自动分发到多个后端服务器',
        icon: 'network',
        color: 'var(--color-accent)', bgColor: 'rgba(20,201,201,0.1)',
        features: ['四层/七层', '健康检查', '会话保持'],
        detail: {
          banner: '高可用流量分发引擎',
          intro: '负载均衡CLB将访问流量自动分配到多台后端服务器，提升应用系统可用性和处理能力。支持四层(TCP/UDP)和七层(HTTP/HTTPS)负载均衡，内置健康检查机制，自动隔离故障节点，保障业务连续性。',
          highlights: [
            { title: '四层+七层均衡', desc: '同时支持TCP/UDP四层和HTTP/HTTPS七层负载均衡，满足不同协议需求' },
            { title: '智能健康检查', desc: '自动检测后端实例健康状态，秒级发现并隔离故障节点' },
            { title: '丰富调度算法', desc: '支持加权轮询、最小连接数、源IP Hash等多种调度策略' },
            { title: '灵活会话保持', desc: '基于Cookie或源IP的会话保持，确保同一用户请求发送到相同后端' }
          ],
          specs: [
            { label: '类型', value: '四层 CLB / 七层 ALB' },
            { label: '最大并发', value: '5000万连接' },
            { label: '新建连接', value: '100万/秒' },
            { label: '协议', value: 'TCP / UDP / HTTP / HTTPS' },
            { label: 'SLA', value: '99.99%' },
            { label: 'SSL卸载', value: '支持' }
          ],
          scenarios: [
            { title: 'Web应用分发', desc: '将HTTP/HTTPS请求分发到多台Web服务器，提升并发处理能力' },
            { title: '微服务网关', desc: '作为微服务架构的流量入口，实现服务发现和负载均衡' },
            { title: '跨可用区容灾', desc: '跨AZ部署后端实例，单AZ故障时自动切换流量' },
            { title: '游戏接入层', desc: '四层负载均衡分发游戏长连接，保障低延迟和高并发' }
          ]
        }
      },
      {
        slug: 'cdn',
        name: 'CDN 内容分发',
        desc: '全球 2800+ 加速节点，毫秒级响应，为网站和应用提供极速体验',
        icon: 'zap', tag: 'HOT',
        color: 'var(--color-yellow)', bgColor: 'rgba(247,186,30,0.1)',
        features: ['全球加速', 'HTTPS', '智能调度'],
        detail: {
          banner: '全球2800+节点极速内容分发',
          intro: '羿贝引擎CDN拥有全球2800+加速节点，总储备带宽超150Tbps。通过智能调度系统将用户请求导向最近的边缘节点，实现毫秒级响应。支持全站加速、HTTPS、WebSocket、HTTP/3等特性，助力网站和应用提供极致用户体验。',
          highlights: [
            { title: '全球海量节点', desc: '2800+加速节点覆盖全球六大洲，总储备带宽超150Tbps' },
            { title: '智能调度引擎', desc: '基于实时链路质量、节点负载、用户位置等多维数据智能选路' },
            { title: '全站加速', desc: '静态资源缓存加速与动态请求智能回源结合，全面提升站点性能' },
            { title: '安全防护', desc: '集成WAF、DDoS防护、防盗链、IP黑白名单等安全能力' }
          ],
          specs: [
            { label: '节点数', value: '2800+全球节点' },
            { label: '总带宽', value: '150Tbps+' },
            { label: '协议', value: 'HTTP/2 / HTTP/3 / WebSocket' },
            { label: 'SSL', value: '免费HTTPS / 自定义证书' },
            { label: '缓存', value: '边缘缓存 / 预热回源' },
            { label: '计费', value: '按流量 / 按带宽峰值' }
          ],
          scenarios: [
            { title: '网站加速', desc: '企业官网、电商平台、资讯站点的静态资源和页面加速' },
            { title: '下载分发', desc: '软件安装包、游戏客户端、固件升级等大文件分发' },
            { title: '音视频点播', desc: '在线视频、音乐流媒体的分发加速' },
            { title: '全站加速', desc: '动静混合站点的全链路加速优化' }
          ]
        }
      },
      {
        slug: 'vpc',
        name: '私有网络 VPC',
        desc: '逻辑隔离的安全虚拟私有云网络，自定义网络拓扑和安全策略',
        icon: 'lock',
        color: 'var(--color-green)', bgColor: 'rgba(159,219,29,0.1)',
        features: ['网络隔离', '安全组', '路由表'],
        detail: {
          banner: '逻辑隔离的安全云上专属网络',
          intro: '私有网络VPC让您在羿贝引擎上构建逻辑隔离的虚拟网络环境。可自定义IP地址段、子网划分、路由策略和安全组规则。VPC间完全隔离，配合NAT网关、VPN网关、对等连接等组件，灵活构建混合云和多VPC网络架构。',
          highlights: [
            { title: '完全逻辑隔离', desc: '不同VPC间网络完全隔离，确保租户间数据安全与隐私' },
            { title: '灵活网络规划', desc: '自定义CIDR地址段、子网划分、路由表配置，满足各类网络架构需求' },
            { title: '丰富安全策略', desc: '安全组（有状态）和网络ACL（无状态）双重网络访问控制' },
            { title: '多种互联方式', desc: '支持VPC对等连接、VPN网关、专线等多种VPC互联和混合云方案' }
          ],
          specs: [
            { label: '地址段', value: '10/172/192段自定义' },
            { label: '子网数', value: '最多200个/VPC' },
            { label: '路由表', value: '自定义路由规则' },
            { label: '安全组', value: '最多500个' },
            { label: '互联', value: '对等连接 / VPN / 专线' },
            { label: '计费', value: '免费' }
          ],
          scenarios: [
            { title: '业务隔离', desc: '为开发、测试、生产环境创建独立VPC，网络完全隔离' },
            { title: '混合云组网', desc: '通过VPN或专线将VPC与本地数据中心打通' },
            { title: '多地域部署', desc: '不同地域VPC通过云企业网实现全球互联' },
            { title: '安全合规', desc: '精细化的安全组和ACL规则，满足等保合规要求' }
          ]
        }
      }
    ]
  },
  {
    id: 'storage', name: '存储', desc: '海量安全云端存储', icon: 'hard-drive',
    color: 'var(--color-yellow)', bgColor: 'rgba(247,186,30,0.1)',
    items: [
      {
        slug: 'tos',
        name: '对象存储 TOS',
        desc: '10EB级数据规模，高可用、高可靠的海量对象存储服务',
        icon: 'hard-drive', tag: 'HOT',
        color: 'var(--color-brand)', bgColor: 'rgba(51,112,255,0.1)',
        features: ['海量存储', '多级冗余', '智能分层'],
        detail: {
          banner: '10EB级海量对象存储服务',
          intro: '对象存储TOS提供安全、稳定、高效、易用的云存储服务，支持任意数量和类型的数据存储。具备11个9的数据持久性和99.995%的服务可用性，配合智能分层存储、生命周期管理，帮助企业大幅降低存储成本。',
          highlights: [
            { title: '超高数据持久性', desc: '基于纠删码和多副本冗余，提供12个9的数据持久性保障' },
            { title: '智能分层存储', desc: '根据数据访问频率自动流转到标准、低频、归档存储层，最大化降低成本' },
            { title: '强一致性', desc: '写入立即可读的强一致性语义，无需等待数据同步' },
            { title: '丰富的数据处理', desc: '内置图片处理、视频截帧、数据解压等数据处理能力' }
          ],
          specs: [
            { label: '容量', value: '10EB+ 无限扩展' },
            { label: '持久性', value: '12个9' },
            { label: '可用性', value: '99.995%' },
            { label: '存储类型', value: '标准/低频/归档/深度归档' },
            { label: 'API', value: 'S3兼容' },
            { label: '加密', value: 'SSE-KMS / SSE-TOS' }
          ],
          scenarios: [
            { title: '数据湖底座', desc: '作为大数据和AI的统一数据底座，存放训练数据集和分析数据' },
            { title: '备份归档', desc: '企业数据备份归档，搭配生命周期策略自动降冷' },
            { title: '静态资源托管', desc: '网站图片、视频、下载文件等静态资源托管与分发' },
            { title: '日志存储', desc: '海量应用日志和审计日志的持久化存储与分析' }
          ]
        }
      },
      {
        slug: 'nas',
        name: '文件存储 NAS',
        desc: '全托管高性能共享文件存储服务，支持NFS/SMB协议',
        icon: 'file-text',
        color: 'var(--color-accent)', bgColor: 'rgba(20,201,201,0.1)',
        features: ['高吞吐', '共享访问', '自动扩容'],
        detail: {
          banner: '高性能共享文件存储服务',
          intro: '文件存储NAS提供全托管、高性能、高可靠的共享文件存储。支持NFS和SMB协议，可被多台ECS实例同时挂载访问。容量自动弹性伸缩，配合多种存储类型，满足AI训练数据共享、内容管理、开发协作等场景。',
          highlights: [
            { title: '高性能', desc: '最高支持20GB/s吞吐和100万IOPS，满足AI训练等高性能场景' },
            { title: '共享访问', desc: '支持数千台ECS实例同时挂载访问，无需额外数据同步' },
            { title: '弹性扩容', desc: '存储容量按需自动扩展，无需预置容量，按实际使用量计费' },
            { title: '数据保护', desc: '支持快照备份和跨可用区冗余，保障数据安全' }
          ],
          specs: [
            { label: '协议', value: 'NFSv3 / NFSv4 / SMB' },
            { label: '吞吐', value: '最高 20GB/s' },
            { label: 'IOPS', value: '最高 100万' },
            { label: '容量', value: '自动弹性扩展 PB级' },
            { label: '类型', value: '通用型 / 极速型' },
            { label: '冗余', value: '跨AZ多副本' }
          ],
          scenarios: [
            { title: 'AI训练数据共享', desc: '多GPU实例共享训练数据集，无需数据拷贝' },
            { title: '内容管理', desc: 'CMS、媒资管理系统的共享文件存储后端' },
            { title: '开发协作', desc: '多开发者共享代码仓库和构建产物' },
            { title: '容器持久化', desc: 'Kubernetes Pod的ReadWriteMany持久化卷' }
          ]
        }
      },
      {
        slug: 'evs',
        name: '云盘 EVS',
        desc: '高可靠云硬盘块存储服务，适配不同IO性能需求',
        icon: 'database',
        color: 'var(--color-yellow)', bgColor: 'rgba(247,186,30,0.1)',
        features: ['三副本', 'SSD/HDD', '快照备份'],
        detail: {
          banner: '高可靠弹性块存储服务',
          intro: '云盘EVS提供高性能、高可靠的块存储服务。基于分布式存储架构，数据三副本冗余，提供99.9999999%的数据可靠性。支持SSD和HDD两种介质类型，满足从高性能数据库到冷数据归档的各类存储需求。',
          highlights: [
            { title: '三副本高可靠', desc: '数据自动三副本存储，跨故障域分布，9个9的数据可靠性' },
            { title: '多种性能规格', desc: '提供极速型SSD、通用型SSD、高效型HDD等多种规格' },
            { title: '在线扩容', desc: '支持在线扩容云盘容量和变更性能规格，业务不中断' },
            { title: '快照与备份', desc: '支持手动和自动快照策略，快速回滚和创建新盘' }
          ],
          specs: [
            { label: '类型', value: '极速SSD / 通用SSD / 高效HDD' },
            { label: '容量', value: '20GB ~ 32TB' },
            { label: 'IOPS', value: '最高 100万' },
            { label: '吞吐', value: '最高 4GB/s' },
            { label: '可靠性', value: '99.9999999%' },
            { label: '快照', value: '手动 + 自动策略' }
          ],
          scenarios: [
            { title: '数据库存储', desc: 'MySQL、PostgreSQL等关系型数据库的高性能存储' },
            { title: '系统盘', desc: '云服务器ECS的操作系统和应用程序存储' },
            { title: '日志存储', desc: '应用运行日志的高效写入存储' },
            { title: '开发测试', desc: '快照快速创建测试环境的数据盘' }
          ]
        }
      }
    ]
  },
  {
    id: 'database-cat', name: '数据库', desc: '高可靠云端数据库', icon: 'database',
    color: 'var(--color-green)', bgColor: 'rgba(159,219,29,0.1)',
    items: [
      {
        slug: 'mysql',
        name: '云数据库 MySQL 版',
        desc: '即开即用、稳定可靠的弹性MySQL数据库服务，兼容主流MySQL版本',
        icon: 'database', tag: 'HOT',
        color: 'var(--color-brand)', bgColor: 'rgba(51,112,255,0.1)',
        features: ['高可用', '自动备份', '读写分离'],
        detail: {
          banner: '企业级全托管MySQL云数据库',
          intro: '云数据库MySQL版提供即开即用的全托管MySQL服务，完全兼容MySQL 5.7/8.0。基于高可用架构，支持主备自动切换、读写分离、自动备份恢复。内置智能DBA诊断和慢查询分析，帮助开发者高效管理数据库。',
          highlights: [
            { title: '高可用架构', desc: '主备双节点自动切换，切换时间秒级，RTO < 30秒' },
            { title: '读写分离', desc: '内置只读节点和读写分离代理，透明分离读写请求，提升读性能' },
            { title: '自动备份恢复', desc: '支持全量备份和Binlog增量备份，精确恢复到任意秒级时间点' },
            { title: '智能运维', desc: '内置慢查询分析、全量SQL审计、智能诊断和性能优化建议' }
          ],
          specs: [
            { label: '版本', value: 'MySQL 5.7 / 8.0' },
            { label: '规格', value: '1核1G ~ 64核512G' },
            { label: '存储', value: '20GB ~ 32TB 自动扩容' },
            { label: '只读节点', value: '最多 10个' },
            { label: 'SLA', value: '99.99%' },
            { label: '备份', value: '自动备份 + 任意时间点恢复' }
          ],
          scenarios: [
            { title: 'Web应用', desc: '电商、CMS、SaaS等Web应用的核心关系型数据存储' },
            { title: '金融交易', desc: '订单系统、支付系统等对数据一致性要求极高的场景' },
            { title: '数据分析', desc: '通过只读节点分担OLAP查询压力，OLTP和OLAP混合负载' },
            { title: '微服务', desc: '微服务架构中每个服务独立数据库实例，实现数据解耦' }
          ]
        }
      },
      {
        slug: 'postgresql',
        name: '云数据库 PostgreSQL',
        desc: '高兼容性关系型数据库，支持丰富的数据类型和高级特性',
        icon: 'database',
        color: 'var(--color-accent)', bgColor: 'rgba(20,201,201,0.1)',
        features: ['高兼容', 'JSONB', '扩展支持'],
        detail: {
          banner: '功能强大的高兼容性关系型数据库',
          intro: '云数据库PostgreSQL版提供完全兼容PostgreSQL的全托管服务。支持丰富的数据类型(JSONB、GIS、数组等)、高级特性(CTE、窗口函数、全文检索)和扩展生态(PostGIS、pg_vector等)，是最具扩展性的企业级关系型数据库。',
          highlights: [
            { title: '丰富数据类型', desc: '原生支持JSONB、数组、范围、几何、网络地址等20+数据类型' },
            { title: '向量检索', desc: '通过pg_vector扩展支持向量存储和检索，构建AI应用知识库' },
            { title: 'GIS空间数据', desc: '集成PostGIS扩展，支持地理空间数据存储和地理围栏查询' },
            { title: '高级SQL特性', desc: '支持CTE递归查询、窗口函数、物化视图、并行查询等高级特性' }
          ],
          specs: [
            { label: '版本', value: 'PG 13 / 14 / 15 / 16' },
            { label: '规格', value: '1核2G ~ 64核512G' },
            { label: '存储', value: '20GB ~ 32TB' },
            { label: '扩展', value: 'pg_vector / PostGIS / 100+' },
            { label: 'SLA', value: '99.99%' },
            { label: '复制', value: '流复制 + 逻辑复制' }
          ],
          scenarios: [
            { title: 'AI应用知识库', desc: '使用pg_vector存储向量Embedding，实现RAG检索增强生成' },
            { title: 'GIS地图应用', desc: '地理围栏、轨迹分析、POI检索等位置服务' },
            { title: 'SaaS多租户', desc: '利用Schema隔离实现多租户SaaS数据架构' },
            { title: '数据仓库', desc: '利用分区表和并行查询能力进行数据分析' }
          ]
        }
      },
      {
        slug: 'redis',
        name: '缓存数据库 Redis 版',
        desc: '兼具缓存的高性能与存储的持久化，支持多种数据结构',
        icon: 'memory-stick', tag: 'HOT',
        color: 'var(--color-yellow)', bgColor: 'rgba(247,186,30,0.1)',
        features: ['亚毫秒延迟', '持久化', '集群模式'],
        detail: {
          banner: '亚毫秒级高性能缓存数据库',
          intro: '缓存数据库Redis版提供全兼容Redis的云端缓存服务。亚毫秒级读写延迟，支持主从、哨兵、集群多种架构。内置数据持久化、自动备份、在线扩容能力，满足缓存加速、会话管理、实时排行榜等高性能场景需求。',
          highlights: [
            { title: '极致性能', desc: '单节点10万+ QPS，集群模式线性扩展，读写延迟低至亚毫秒级' },
            { title: '多种架构', desc: '支持主从、哨兵、集群三种架构模式，灵活匹配不同规模需求' },
            { title: '数据持久化', desc: 'AOF + RDB双重持久化，故障恢复秒级完成，数据不丢失' },
            { title: '在线变配', desc: '在线变更内存规格、增减分片节点、主从切读写分离，业务无感' }
          ],
          specs: [
            { label: '版本', value: 'Redis 5.0 / 6.0 / 7.0' },
            { label: '内存', value: '256MB ~ 4TB' },
            { label: 'QPS', value: '10万+ / 节点' },
            { label: '延迟', value: '< 1ms' },
            { label: '架构', value: '主从 / 哨兵 / 集群' },
            { label: '分片数', value: '最多 256个' }
          ],
          scenarios: [
            { title: '缓存加速', desc: 'Web应用热点数据缓存，大幅降低数据库读压力' },
            { title: '会话管理', desc: '分布式系统的Session共享和Token存储' },
            { title: '实时排行榜', desc: '利用Sorted Set实现游戏排名、热搜榜等实时排行' },
            { title: '消息队列', desc: '利用List/Stream实现轻量级异步消息队列' }
          ]
        }
      },
      {
        slug: 'mongodb',
        name: '云数据库 MongoDB 版',
        desc: '全托管文档型NoSQL数据库，弹性扩展、高度兼容',
        icon: 'database',
        color: 'var(--color-green)', bgColor: 'rgba(159,219,29,0.1)',
        features: ['文档存储', '弹性伸缩', '自动备份'],
        detail: {
          banner: '弹性灵活的文档型NoSQL数据库',
          intro: '云数据库MongoDB版提供全兼容MongoDB的文档型数据库服务。灵活的文档数据模型无需预定义Schema，支持副本集和分片集群两种架构，内置自动备份和监控告警，适合内容管理、IoT、游戏等需要灵活数据模型的场景。',
          highlights: [
            { title: '灵活文档模型', desc: '无需预定义Schema，支持嵌套文档和数组，适应快速变化的业务数据结构' },
            { title: '水平扩展', desc: '分片集群架构实现数据和请求的水平扩展，轻松应对TB-PB级数据' },
            { title: '丰富查询', desc: '支持聚合管道、全文索引、地理空间查询等丰富的查询方式' },
            { title: '高可用', desc: '副本集三节点架构，自动选主和故障切换，保障数据可用性' }
          ],
          specs: [
            { label: '版本', value: 'MongoDB 4.4 / 5.0 / 6.0' },
            { label: '架构', value: '副本集 / 分片集群' },
            { label: '规格', value: '1核2G ~ 64核512G' },
            { label: '存储', value: '10GB ~ 32TB' },
            { label: '分片数', value: '最多 32个' },
            { label: '备份', value: '自动备份 + 时间点恢复' }
          ],
          scenarios: [
            { title: '内容管理', desc: 'CMS、博客平台等内容结构多变的应用' },
            { title: 'IoT数据', desc: '海量传感器时序数据的存储与查询' },
            { title: '游戏数据', desc: '玩家档案、游戏进度等半结构化数据存储' },
            { title: '日志分析', desc: '应用日志的采集存储和聚合分析' }
          ]
        }
      },
      {
        slug: 'es',
        name: '云搜索服务',
        desc: '全托管AI信息检索和分析平台，基于Elasticsearch构建',
        icon: 'search', tag: 'HOT',
        color: 'var(--color-brand)', bgColor: 'rgba(51,112,255,0.1)',
        features: ['全文检索', '向量检索', '实时分析'],
        detail: {
          banner: '全托管AI信息检索与实时分析平台',
          intro: '云搜索服务基于Elasticsearch构建，提供全托管的信息检索和数据分析平台。支持全文搜索、向量检索、日志分析等能力。配合Kibana可视化，帮助企业快速搭建搜索引擎、日志分析平台和AI知识检索系统。',
          highlights: [
            { title: '全文+向量混合检索', desc: '同时支持BM25全文检索和KNN向量检索，实现语义级搜索' },
            { title: 'Kibana可视化', desc: '内置Kibana组件，提供丰富的数据可视化和仪表盘能力' },
            { title: '弹性伸缩', desc: '在线增减节点和磁盘扩容，自动平衡分片数据' },
            { title: '全托管免运维', desc: '内核版本升级、集群监控、慢日志分析等自动化运维' }
          ],
          specs: [
            { label: '版本', value: 'ES 7.x / 8.x' },
            { label: '节点数', value: '1 ~ 50节点' },
            { label: '存储', value: 'SSD 最高 20TB/节点' },
            { label: '检索', value: '全文 + 向量 + 混合' },
            { label: '可视化', value: 'Kibana内置' },
            { label: 'SLA', value: '99.9%' }
          ],
          scenarios: [
            { title: '站内搜索', desc: '电商商品搜索、内容平台文章检索、企业知识搜索' },
            { title: '日志分析', desc: 'ELK架构下的应用日志实时分析和可视化' },
            { title: 'AI知识检索', desc: 'RAG场景下的文档向量化存储与语义检索' },
            { title: '业务监控', desc: '实时监控业务指标异常和告警' }
          ]
        }
      }
    ]
  },
  {
    id: 'container-cat', name: '容器与中间件', desc: '云原生容器服务', icon: 'container',
    color: 'var(--color-brand)', bgColor: 'rgba(51,112,255,0.1)',
    items: [
      {
        slug: 'vke',
        name: '容器服务 VKE',
        desc: '高性能Kubernetes容器集群管理服务，简化容器化应用部署与运维',
        icon: 'container', tag: 'HOT',
        color: 'var(--color-brand)', bgColor: 'rgba(51,112,255,0.1)',
        features: ['K8s托管', '弹性伸缩', '服务网格'],
        detail: {
          banner: '全托管Kubernetes容器服务',
          intro: '容器服务VKE提供全托管的Kubernetes容器集群服务。控制面高可用免运维，支持GPU/ARM等异构节点池、Serverless容器(VCI)、服务网格等云原生能力。帮助企业快速构建容器化应用的持续交付和自动化运维体系。',
          highlights: [
            { title: '控制面全托管', desc: '控制面组件三AZ高可用部署，免运维，SLA 99.95%' },
            { title: 'Serverless容器', desc: '基于VCI无需管理节点，Pod秒级启动，按需计费' },
            { title: '弹性节点池', desc: '支持GPU、ARM、竞价等多种节点池类型，自动扩缩节点' },
            { title: '生态兼容', desc: '兼容原生K8s API和Helm/Kubectl工具链，无缝迁移现有应用' }
          ],
          specs: [
            { label: 'K8s版本', value: '1.24 ~ 1.30' },
            { label: '最大节点', value: '5000节点/集群' },
            { label: '最大Pod', value: '15万Pod/集群' },
            { label: '容器运行时', value: 'containerd' },
            { label: '网络插件', value: 'VPC-CNI / Flannel' },
            { label: 'SLA', value: '99.95%控制面' }
          ],
          scenarios: [
            { title: '微服务架构', desc: '容器化微服务的部署、灰度发布和弹性伸缩' },
            { title: 'CI/CD流水线', desc: '结合镜像仓库实现代码到容器的自动化交付' },
            { title: 'AI训练任务', desc: 'GPU节点池运行分布式训练Job，训练完自动释放' },
            { title: '批量计算', desc: '利用竞价实例和Serverless容器运行批处理任务' }
          ]
        }
      },
      {
        slug: 'cr',
        name: '镜像仓库 CR',
        desc: '安全稳定的容器镜像托管服务，支持多种镜像格式',
        icon: 'layers',
        color: 'var(--color-accent)', bgColor: 'rgba(20,201,201,0.1)',
        features: ['镜像托管', '安全扫描', '多区域'],
        detail: {
          banner: '安全高效的容器镜像托管服务',
          intro: '镜像仓库CR提供安全、稳定的容器镜像全生命周期管理。支持Docker和OCI镜像格式，内置漏洞扫描、镜像签名、跨区域同步等企业级能力，与容器服务VKE无缝集成，加速容器化应用的开发和交付流程。',
          highlights: [
            { title: '安全漏洞扫描', desc: '自动扫描镜像中的CVE漏洞和安全风险，提供修复建议' },
            { title: '多地域同步', desc: '支持镜像跨地域自动同步，就近拉取提升部署速度' },
            { title: '细粒度权限', desc: '命名空间级别的RAM权限控制，安全隔离不同团队的镜像' },
            { title: 'P2P分发加速', desc: '基于P2P技术加速大规模集群的镜像拉取，避免仓库带宽瓶颈' }
          ],
          specs: [
            { label: '格式', value: 'Docker V2 / OCI' },
            { label: '存储', value: '无限容量' },
            { label: '漏洞库', value: 'CVE实时更新' },
            { label: '地域', value: '支持多地域同步' },
            { label: '加速', value: 'P2P镜像分发' },
            { label: 'SLA', value: '99.9%' }
          ],
          scenarios: [
            { title: 'CI/CD集成', desc: '流水线构建镜像后自动推送，触发部署' },
            { title: '安全合规', desc: '镜像安全扫描+签名验证，确保只部署可信镜像' },
            { title: '多集群分发', desc: '跨地域同步镜像，多集群同时拉取' },
            { title: '开源镜像代理', desc: '代理Docker Hub等公共仓库，加速国内拉取' }
          ]
        }
      },
      {
        slug: 'kafka',
        name: '消息队列 Kafka',
        desc: '全托管高吞吐分布式消息队列服务',
        icon: 'workflow',
        color: 'var(--color-yellow)', bgColor: 'rgba(247,186,30,0.1)',
        features: ['高吞吐', '低延迟', '持久化'],
        detail: {
          banner: '全托管高吞吐分布式消息队列',
          intro: '消息队列Kafka版提供全兼容Apache Kafka的全托管消息中间件服务。百万级TPS消息吞吐，毫秒级端到端延迟。支持消息持久化存储、消费组管理和消息回溯，帮助企业构建实时数据流水线和事件驱动架构。',
          highlights: [
            { title: '百万级吞吐', desc: '单集群支持百万级TPS消息吞吐，轻松应对海量数据流' },
            { title: '全兼容Kafka', desc: '100%兼容Apache Kafka协议，现有应用零改造迁移' },
            { title: '消息持久化', desc: '消息多副本持久化存储，支持7天内任意时间点消息回溯' },
            { title: '弹性扩容', desc: '在线增加分区数和Broker节点，不影响现有业务' }
          ],
          specs: [
            { label: '版本', value: 'Kafka 2.x / 3.x' },
            { label: '吞吐', value: '百万级TPS' },
            { label: '延迟', value: '毫秒级' },
            { label: '副本', value: '2~3副本' },
            { label: '保留', value: '最长7天' },
            { label: 'SLA', value: '99.95%' }
          ],
          scenarios: [
            { title: '日志收集', desc: '集中收集应用日志，下游对接ES、数仓进行分析' },
            { title: '实时数据流', desc: '构建实时ETL流水线，数据实时同步到数据湖' },
            { title: '事件驱动', desc: '微服务间异步通信和事件溯源架构的消息总线' },
            { title: '流计算', desc: '结合Flink实现实时数据流处理和聚合分析' }
          ]
        }
      }
    ]
  },
  {
    id: 'bigdata', name: '大数据', desc: '一站式大数据平台', icon: 'bar-chart',
    color: 'var(--color-accent)', bgColor: 'rgba(20,201,201,0.1)',
    items: [
      {
        slug: 'ai-datalake',
        name: 'AI 数据湖服务',
        desc: '大模型时代AI数据基建，统一管理海量异构数据',
        icon: 'brain', tag: 'NEW',
        color: 'var(--color-brand)', bgColor: 'rgba(51,112,255,0.1)',
        features: ['湖仓一体', 'AI优化', '多格式'],
        detail: {
          banner: '大模型时代的AI数据基础设施',
          intro: 'AI数据湖服务为大模型训练和AI应用提供统一的数据管理平台。支持文本、图片、音视频等多模态数据的采集、清洗、标注和管理，内置数据质量评估和去重能力，帮助企业高效构建高质量AI训练数据集。',
          highlights: [
            { title: '多模态数据管理', desc: '统一管理文本、图片、音频、视频等多种格式的AI训练数据' },
            { title: '数据质量评估', desc: '内置数据质量评分、去重检测、毒性检测等数据治理能力' },
            { title: '智能标注', desc: 'AI辅助标注+人工审核，大幅提升数据标注效率和质量' },
            { title: '安全合规', desc: '数据脱敏、访问审计、权限管理，确保数据安全合规' }
          ],
          specs: [
            { label: '数据类型', value: '文本/图片/音频/视频' },
            { label: '存储', value: 'PB级无限扩展' },
            { label: '格式', value: 'Parquet / JSON / CSV / 自定义' },
            { label: '标注', value: 'AI辅助 + 人工审核' },
            { label: '对接', value: '羿贝方舟 / PyTorch / HuggingFace' },
            { label: '安全', value: '脱敏 + 审计 + RBAC' }
          ],
          scenarios: [
            { title: '大模型预训练', desc: '构建和管理千亿Token级预训练语料库' },
            { title: 'SFT微调数据', desc: '高质量指令微调数据集的制作和版本管理' },
            { title: 'RLHF标注', desc: '人类偏好标注数据的众包管理和质量控制' },
            { title: '多模态训练', desc: '图文配对、视频理解等多模态训练数据管理' }
          ]
        }
      },
      {
        slug: 'emr',
        name: 'EMR',
        desc: '全托管弹性MapReduce大数据处理平台',
        icon: 'server',
        color: 'var(--color-accent)', bgColor: 'rgba(20,201,201,0.1)',
        features: ['Spark', 'Flink', 'Hive'],
        detail: {
          banner: '全托管弹性大数据处理平台',
          intro: 'EMR(弹性MapReduce)提供基于开源大数据生态的全托管集群计算服务。集成Spark、Flink、Hive、Presto等主流引擎，支持分钟级集群创建和弹性伸缩，按需使用计算资源，大幅降低大数据处理的运维复杂度和成本。',
          highlights: [
            { title: '丰富引擎生态', desc: '集成Spark、Flink、Hive、Presto、HBase等10+大数据组件' },
            { title: '弹性伸缩', desc: '支持任务节点弹性扩缩和竞价实例，降低60%以上计算成本' },
            { title: '存算分离', desc: '计算与存储分离架构，数据存储于TOS，集群按需创建释放' },
            { title: '一键运维', desc: '自动化集群部署、监控、日志收集和组件版本管理' }
          ],
          specs: [
            { label: '引擎', value: 'Spark / Flink / Hive / Presto' },
            { label: '节点', value: '最多 1000节点' },
            { label: '存储', value: 'TOS / HDFS / 本地盘' },
            { label: '调度', value: 'YARN / K8s' },
            { label: '伸缩', value: '分钟级弹性扩缩' },
            { label: '计费', value: '按量 / 预留 / 竞价' }
          ],
          scenarios: [
            { title: '离线ETL', desc: 'T+1数据仓库ETL流水线，每日增量数据处理' },
            { title: '实时流计算', desc: 'Flink实时处理Kafka数据流，输出到数据库和搜索引擎' },
            { title: '数据分析', desc: 'Spark SQL和Presto进行交互式即席查询' },
            { title: '机器学习', desc: 'Spark MLlib进行大规模特征工程和模型训练' }
          ]
        }
      },
      {
        slug: 'lakehouse',
        name: '数据湖仓',
        desc: '湖仓一体化数据分析平台，融合数据湖与数据仓库优势',
        icon: 'database',
        color: 'var(--color-yellow)', bgColor: 'rgba(247,186,30,0.1)',
        features: ['统一分析', '实时查询', '开放格式'],
        detail: {
          banner: '湖仓一体化数据分析平台',
          intro: '数据湖仓融合数据湖的灵活性和数据仓库的高性能分析能力。基于开放表格式(Apache Iceberg/Hudi)，支持结构化和半结构化数据的统一存储与分析。实现ACID事务、时间旅行、增量查询等高级能力，告别数据孤岛。',
          highlights: [
            { title: '湖仓融合', desc: '统一数据湖和数据仓库，消除数据搬运和冗余存储' },
            { title: 'ACID事务', desc: '基于Iceberg/Hudi开放格式，支持行级更新和ACID事务' },
            { title: '时间旅行', desc: '查询任意历史版本的数据快照，支持数据回滚和审计' },
            { title: '多引擎对接', desc: '同一份数据支持Spark、Flink、Presto、StarRocks等多引擎查询' }
          ],
          specs: [
            { label: '表格式', value: 'Apache Iceberg / Hudi' },
            { label: '存储', value: 'TOS对象存储' },
            { label: '引擎', value: 'Spark / Flink / Presto / StarRocks' },
            { label: '事务', value: 'ACID行级更新' },
            { label: '时间旅行', value: '支持历史版本查询' },
            { label: '数据类型', value: '结构化 + 半结构化' }
          ],
          scenarios: [
            { title: '实时数仓', desc: '流批一体的实时数据仓库，分钟级数据新鲜度' },
            { title: '统一分析', desc: '一份数据同时服务BI报表、即席查询和机器学习' },
            { title: '数据合规', desc: '利用行级更新实现GDPR数据删除和修正' },
            { title: '增量计算', desc: '基于变更数据捕获(CDC)实现增量ETL流水线' }
          ]
        }
      }
    ]
  },
  {
    id: 'video-cat', name: '视频与通信', desc: '视频云与实时音视频', icon: 'video',
    color: 'var(--color-yellow)', bgColor: 'rgba(247,186,30,0.1)',
    items: [
      {
        slug: 'vod',
        name: '视频点播',
        desc: '一站式音视频点播服务，覆盖上传、转码、分发全流程',
        icon: 'video', tag: 'HOT',
        color: 'var(--color-brand)', bgColor: 'rgba(51,112,255,0.1)',
        features: ['智能转码', 'AI审核', '全球加速'],
        detail: {
          banner: '一站式音视频点播服务',
          intro: '视频点播提供从上传、存储、转码、审核到分发播放的全链路音视频服务。内置智能转码引擎、AI内容审核、多码率自适应等能力。基于羿贝引擎全球CDN加速，提供流畅的点播观看体验，服务覆盖全球200+国家和地区。',
          highlights: [
            { title: '智能转码', desc: '极智超清转码降低30%带宽成本，支持H.265/AV1编码' },
            { title: 'AI智能审核', desc: '自动识别涉黄、暴恐、政治敏感等内容，审核准确率99.9%+' },
            { title: '多码率自适应', desc: 'HLS/DASH自适应码率，根据网络状况自动切换清晰度' },
            { title: '全球分发', desc: '全球2800+CDN节点分发，200+国家地区覆盖' }
          ],
          specs: [
            { label: '编码', value: 'H.264 / H.265 / AV1' },
            { label: '分辨率', value: '最高 8K' },
            { label: '协议', value: 'HLS / DASH / MP4' },
            { label: 'DRM', value: 'Widevine / FairPlay' },
            { label: '审核', value: 'AI智能审核 99.9%' },
            { label: '加速', value: '全球2800+节点' }
          ],
          scenarios: [
            { title: '在线教育', desc: '课程视频的上传转码、加密播放和观看统计' },
            { title: '短视频平台', desc: '海量UGC短视频的处理分发和内容审核' },
            { title: '企业培训', desc: '内部培训视频的安全存储和权限管理' },
            { title: '媒资管理', desc: '广电/媒体机构的音视频资产管理' }
          ]
        }
      },
      {
        slug: 'live',
        name: '视频直播',
        desc: '低延时高并发直播服务，覆盖推流、转码、分发、播放全链路',
        icon: 'monitor',
        color: 'var(--color-accent)', bgColor: 'rgba(20,201,201,0.1)',
        features: ['超低延时', '连麦互动', '实时录制'],
        detail: {
          banner: '低延时高并发视频直播服务',
          intro: '视频直播提供从推流、转码、分发到播放的全链路直播服务。支持标准直播、低延时直播、快直播等多种延迟档位。内置连麦互动、实时录制、AI审核等能力，保障百万级并发的流畅直播体验。',
          highlights: [
            { title: '超低延时', desc: '快直播模式端到端延迟低至1秒，标准直播3~5秒' },
            { title: '连麦互动', desc: '主播间PK连麦、观众上麦互动，延迟低至200ms' },
            { title: '实时录制', desc: '直播流实时录制为MP4/FLV文件，无缝转为点播内容' },
            { title: '弹幕与SEI', desc: '支持弹幕消息和SEI信令透传，丰富互动体验' }
          ],
          specs: [
            { label: '协议', value: 'RTMP / FLV / HLS / WebRTC' },
            { label: '延迟', value: '快直播1s / 标准3~5s' },
            { label: '并发', value: '百万级同时在线' },
            { label: '转码', value: '实时转码多码率' },
            { label: '录制', value: 'MP4 / FLV / HLS' },
            { label: '审核', value: 'AI实时截帧审核' }
          ],
          scenarios: [
            { title: '电商直播', desc: '商品讲解直播，支持连麦砍价、弹幕互动' },
            { title: '游戏直播', desc: '高帧率游戏画面直播，低延迟弹幕互动' },
            { title: '在线教育', desc: '大班课直播+互动白板，万人同时在线听课' },
            { title: '活动直播', desc: '发布会、峰会等企业活动的全球直播分发' }
          ]
        }
      },
      {
        slug: 'rtc',
        name: '实时音视频 RTC',
        desc: '全球低延时实时通信服务，支持音视频通话、互动直播等场景',
        icon: 'headphones',
        color: 'var(--color-yellow)', bgColor: 'rgba(247,186,30,0.1)',
        features: ['全球覆盖', '超低延时', '端侧AI'],
        detail: {
          banner: '全球低延时实时音视频通信',
          intro: '实时音视频RTC提供全球低延时(< 200ms)的实时音视频通信服务。基于羿贝引擎全球分布式传输网络，支持1v1通话、多人会议、互动直播等场景。集成AI降噪、美颜滤镜、虚拟背景等端侧AI能力，提供高品质通信体验。',
          highlights: [
            { title: '全球低延时', desc: '全球200+国家覆盖，端到端延迟低于200ms' },
            { title: 'AI降噪', desc: '深度学习降噪算法，有效消除键盘、风扇等环境噪声' },
            { title: '超高清画质', desc: '支持4K/60fps视频通话，自适应码率控制' },
            { title: '跨平台SDK', desc: '覆盖iOS、Android、Web、Windows、Mac等全平台' }
          ],
          specs: [
            { label: '延迟', value: '< 200ms 端到端' },
            { label: '清晰度', value: '最高 4K 60fps' },
            { label: '并发', desc: '单房间最高万人', value: '万人/房间' },
            { label: '平台', value: 'iOS/Android/Web/桌面' },
            { label: 'AI能力', value: '降噪/美颜/虚拟背景' },
            { label: '录制', value: '服务端合流录制' }
          ],
          scenarios: [
            { title: '视频会议', desc: '企业远程会议、屏幕共享和协作白板' },
            { title: '在线问诊', desc: '医患视频问诊、远程会诊等互联网医疗场景' },
            { title: '社交娱乐', desc: '语音聊天室、视频交友、K歌合唱' },
            { title: '智能硬件', desc: '智能门铃、监控摄像头的实时音视频对讲' }
          ]
        }
      }
    ]
  },
  {
    id: 'security-cat', name: '安全', desc: '全方位安全防护', icon: 'shield',
    color: 'var(--color-red)', bgColor: 'rgba(245,63,63,0.1)',
    items: [
      {
        slug: 'llm-firewall',
        name: '大模型应用防火墙',
        desc: '针对大语言模型推理服务的安全防护产品，防止提示注入等攻击',
        icon: 'shield', tag: 'NEW',
        color: 'var(--color-brand)', bgColor: 'rgba(51,112,255,0.1)',
        features: ['提示注入防护', '内容安全', '实时监控'],
        detail: {
          banner: '大模型时代的AI应用安全守护者',
          intro: '大模型应用防火墙(LLM Firewall)是专为大语言模型推理服务设计的安全防护产品。实时检测和拦截提示注入(Prompt Injection)、越狱攻击(Jailbreak)、敏感信息泄露等AI特有安全威胁，保障AI应用的安全合规运行。',
          highlights: [
            { title: '提示注入防护', desc: '基于深度语义理解检测Direct/Indirect Prompt Injection攻击' },
            { title: '越狱攻击拦截', desc: '识别并拦截试图绕过模型安全对齐的越狱攻击手法' },
            { title: '敏感信息过滤', desc: '自动检测和脱敏输入输出中的个人隐私、商业机密等敏感信息' },
            { title: '实时监控告警', desc: '安全事件实时Dashboard和告警通知，快速响应安全威胁' }
          ],
          specs: [
            { label: '防护类型', value: '注入/越狱/泄露/有害内容' },
            { label: '延迟', value: '< 50ms 检测延迟' },
            { label: '准确率', value: '99.5%+ 攻击识别' },
            { label: '部署', value: 'API网关/SDK/Sidecar' },
            { label: '协议', value: 'OpenAI兼容 / 自定义' },
            { label: '日志', value: '全量安全审计日志' }
          ],
          scenarios: [
            { title: 'AI客服', desc: '防止用户通过恶意提示让AI客服泄露内部信息' },
            { title: 'AI编程助手', desc: '防止代码生成过程中泄露训练数据中的敏感代码' },
            { title: '企业AI应用', desc: '保障企业内部知识库问答应用的数据安全' },
            { title: 'AI内容生成', desc: '过滤有害内容输出，确保AIGC内容安全合规' }
          ]
        }
      },
      {
        slug: 'ddos',
        name: 'DDoS 高防',
        desc: 'T级DDoS流量清洗能力，保障业务可用性',
        icon: 'shield-check',
        color: 'var(--color-accent)', bgColor: 'rgba(20,201,201,0.1)',
        features: ['T级防护', '智能调度', '秒级生效'],
        detail: {
          banner: 'T级DDoS流量清洗防护',
          intro: 'DDoS高防提供最高T级的DDoS攻击流量清洗能力。基于全球分布式清洗中心和智能调度引擎，秒级检测和自动防护各类DDoS攻击(SYN Flood、UDP Flood、CC攻击等)，确保业务在大规模攻击下仍然正常可用。',
          highlights: [
            { title: 'T级防护能力', desc: '全球清洗中心总防护带宽超20Tbps，轻松应对大规模DDoS攻击' },
            { title: '秒级响应', desc: '攻击秒级自动检测和流量牵引，业务无感切换至清洗模式' },
            { title: 'CC攻击防护', desc: '智能识别和拦截CC/HTTP Flood等应用层攻击' },
            { title: '弹性防护', desc: '基础防护+弹性防护双重保障，攻击峰值自动提升防护上限' }
          ],
          specs: [
            { label: '防护带宽', value: '最高 T级' },
            { label: '清洗能力', value: '20Tbps+' },
            { label: '防护类型', value: 'SYN/UDP/ICMP/CC Flood' },
            { label: '响应时间', value: '秒级自动防护' },
            { label: '线路', value: 'BGP高防' },
            { label: 'SLA', value: '99.99%' }
          ],
          scenarios: [
            { title: '游戏防护', desc: '游戏服务器抗DDoS，保障玩家低延迟体验' },
            { title: '电商大促', desc: '大促活动期间防止竞争对手DDoS攻击' },
            { title: '金融服务', desc: '交易系统和支付网关的安全防护' },
            { title: 'SaaS平台', desc: '保障SaaS服务的持续可用性' }
          ]
        }
      },
      {
        slug: 'waf',
        name: 'Web应用防火墙 WAF',
        desc: '一站式Web应用安全防护，抵御OWASP Top 10等常见攻击',
        icon: 'lock',
        color: 'var(--color-yellow)', bgColor: 'rgba(247,186,30,0.1)',
        features: ['规则防护', 'Bot管理', 'API安全'],
        detail: {
          banner: '一站式Web应用安全防护',
          intro: 'Web应用防火墙(WAF)为Web应用提供全面的安全防护能力。基于规则引擎+AI智能检测双引擎，有效防御SQL注入、XSS跨站脚本、文件包含等OWASP Top 10攻击。同时提供Bot管理、CC防护、API安全防护等进阶能力。',
          highlights: [
            { title: 'AI+规则双引擎', desc: '传统规则匹配+AI语义分析双重检测，极低误报率' },
            { title: 'Bot智能管理', desc: '识别和管理爬虫、扫描器、刷单机器人等自动化威胁' },
            { title: 'API安全', desc: '自动发现API资产，检测API参数篡改、越权访问等风险' },
            { title: '0Day虚拟补丁', desc: '新漏洞爆发24小时内下发虚拟补丁，无需修改应用代码' }
          ],
          specs: [
            { label: '防护', value: 'OWASP Top 10全覆盖' },
            { label: '引擎', value: 'AI语义 + 规则匹配' },
            { label: 'QPS', value: '10万+ / 实例' },
            { label: 'Bot管理', value: '爬虫/扫描器/自动化工具' },
            { label: 'API发现', value: '自动化API资产发现' },
            { label: '虚拟补丁', value: '24小时内下发' }
          ],
          scenarios: [
            { title: '电商网站', desc: '防止SQL注入、XSS攻击和恶意爬虫抓取' },
            { title: 'API网关', desc: 'API接口的参数校验、频率限制和越权防护' },
            { title: '政企门户', desc: '政府和企业官网的网页防篡改和安全加固' },
            { title: '游戏服务', desc: '游戏登录和支付接口的CC防护和Bot拦截' }
          ]
        }
      }
    ]
  }
]

// Helper: find a product by slug across all categories
export function findProductBySlug(slug) {
  for (var i = 0; i < productsData.length; i++) {
    var cat = productsData[i]
    for (var j = 0; j < cat.items.length; j++) {
      if (cat.items[j].slug === slug) {
        return { product: cat.items[j], category: cat }
      }
    }
  }
  return null
}

// Helper: get all product slugs
export function getAllProductSlugs() {
  var slugs = []
  productsData.forEach(function (cat) {
    cat.items.forEach(function (item) {
      slugs.push(item.slug)
    })
  })
  return slugs
}
