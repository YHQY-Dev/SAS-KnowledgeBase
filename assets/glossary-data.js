window.SAS_GLOSSARY_DATA = {
  "scattering-vector-q": {
    "id": "scattering-vector-q",
    "titleZh": "散射矢量 q",
    "titleEn": "scattering vector",
    "abbr": "q",
    "tip": "描述散射动量转移的矢量，其模长 q = 4π sinθ/λ 决定探测的实空间尺度。",
    "aliases": [
      "q",
      "动量转移"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/02-scattering-basics.html",
      "learn/03-instruments.html",
      "learn/04-data-reduction.html",
      "topics/data-reduction/index.html",
      "topics/calibration/index.html",
      "topics/sans-contrast/index.html",
      "topics/gisaxs/index.html"
    ]
  },
  "contrast": {
    "id": "contrast",
    "titleZh": "衬度",
    "titleEn": "scattering contrast",
    "abbr": "contrast",
    "tip": "样品与溶剂（或两相）之间散射长度密度差异；衬度为零时 SAS 信号消失。",
    "aliases": [
      "散射衬度",
      "Δρ"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/02-scattering-basics.html",
      "learn/03-instruments.html",
      "learn/08-models-polydispersity.html",
      "learn/09-application-paths.html",
      "topics/sans-contrast/index.html",
      "topics/biosas/index.html",
      "topics/data-reduction/index.html",
      "topics/calibration/index.html"
    ]
  },
  "scattering-length-density": {
    "id": "scattering-length-density",
    "titleZh": "散射长度密度",
    "titleEn": "scattering length density",
    "abbr": "SLD",
    "tip": "单位体积内原子相干散射长度的总和，记作 ρ（SANS）或电子密度（SAXS）；决定散射强度量级。",
    "aliases": [
      "SLD",
      "ρ"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/02-scattering-basics.html",
      "topics/sans-contrast/index.html",
      "topics/biosas/index.html",
      "topics/calibration/index.html",
      "topics/data-reduction/index.html"
    ]
  },
  "form-factor": {
    "id": "form-factor",
    "titleZh": "形式因子",
    "titleEn": "form factor",
    "abbr": "P(q)",
    "tip": "单个散射体（粒子、链段等）的形状与尺寸引起的 q 依赖，记作 P(q)；多分散时取平均。",
    "aliases": [
      "P(q)",
      "形状因子"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/02-scattering-basics.html",
      "learn/04-data-reduction.html",
      "learn/07-real-space-ift.html",
      "learn/08-models-polydispersity.html",
      "learn/09-application-paths.html",
      "topics/sans-contrast/index.html",
      "topics/biosas/index.html",
      "topics/calibration/index.html"
    ]
  },
  "structure-factor": {
    "id": "structure-factor",
    "titleZh": "结构因子",
    "titleEn": "structure factor",
    "abbr": "S(q)",
    "tip": "粒子间空间关联引起的散射调制，记作 S(q)；稀溶液中常近似为 1。",
    "aliases": [
      "S(q)"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/02-scattering-basics.html",
      "learn/04-data-reduction.html",
      "learn/08-models-polydispersity.html",
      "learn/09-application-paths.html",
      "topics/sans-contrast/index.html",
      "topics/biosas/index.html"
    ]
  },
  "radius-of-gyration": {
    "id": "radius-of-gyration",
    "titleZh": "回转半径",
    "titleEn": "radius of gyration",
    "abbr": "Rg",
    "tip": "描述散射体质量分布展宽的特征长度，记作 Rg；低 q 区 Guinier 分析可求得。",
    "aliases": [
      "Rg",
      "回转半径"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/02-scattering-basics.html",
      "learn/06-guinier-porod.html",
      "learn/07-real-space-ift.html",
      "topics/atsas/index.html",
      "topics/biosas/index.html"
    ]
  },
  "forward-scattering": {
    "id": "forward-scattering",
    "titleZh": "前向散射",
    "titleEn": "forward scattering",
    "abbr": "",
    "tip": "小散射角（低 q）区域的散射；对应较大实空间尺度，常含 I(0) 与整体尺寸信息。",
    "aliases": [
      "低 q 散射",
      "小角散射",
      "I(0)"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/02-scattering-basics.html",
      "learn/03-instruments.html",
      "learn/04-data-reduction.html",
      "learn/05-absolute-calibration.html",
      "learn/07-real-space-ift.html",
      "topics/atsas/index.html",
      "topics/biosas/index.html",
      "topics/calibration/index.html",
      "topics/data-reduction/index.html",
      "topics/sans-contrast/index.html"
    ]
  },
  "guinier-analysis": {
    "id": "guinier-analysis",
    "titleZh": "Guinier 分析",
    "titleEn": "Guinier analysis",
    "abbr": "Guinier",
    "tip": "在 qRg ≪ 1 时 I(q) ≈ I(0) exp(−q²Rg²/3)；用于从低 q 数据估计 Rg 与 I(0)。",
    "aliases": [
      "Guinier 定律",
      "Guinier plot"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/02-scattering-basics.html",
      "learn/04-data-reduction.html",
      "learn/05-absolute-calibration.html",
      "learn/06-guinier-porod.html",
      "learn/07-real-space-ift.html",
      "learn/09-application-paths.html",
      "topics/atsas/index.html",
      "topics/biosas/index.html",
      "topics/calibration/index.html",
      "topics/data-reduction/index.html"
    ]
  },
  "porod-law": {
    "id": "porod-law",
    "titleZh": "Porod 定律",
    "titleEn": "Porod's law",
    "abbr": "Porod",
    "tip": "两相界面清晰时高 q 尾强度 ∝ q⁻⁴；可用于估计比表面积，但需扣除背景。",
    "aliases": [
      "Porod 区",
      "q⁻⁴ 衰减"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/02-scattering-basics.html",
      "learn/04-data-reduction.html",
      "learn/06-guinier-porod.html",
      "topics/biosas/index.html",
      "topics/calibration/index.html"
    ]
  },
  "pair-distance-distribution": {
    "id": "pair-distance-distribution",
    "titleZh": "距离分布函数",
    "titleEn": "pair distance distribution function",
    "abbr": "p(r)",
    "tip": "实空间中任意两点间距离 r 的概率分布 p(r)；与 I(q) 经傅里叶变换相联系。",
    "aliases": [
      "p(r)",
      "PDDF"
    ],
    "appearsIn": [
      "learn/02-scattering-basics.html",
      "learn/07-real-space-ift.html",
      "learn/08-models-polydispersity.html",
      "learn/09-application-paths.html",
      "topics/ift/index.html",
      "topics/atsas/index.html",
      "topics/biosas/index.html"
    ]
  },
  "indirect-fourier-transform": {
    "id": "indirect-fourier-transform",
    "titleZh": "间接傅里叶变换",
    "titleEn": "indirect Fourier transform",
    "abbr": "IFT",
    "tip": "从 I(q) 稳定反演 p(r) 的数值方法（如 GNOM）；无需预设粒子形状模型。",
    "aliases": [
      "IFT",
      "傅里叶变换"
    ],
    "appearsIn": [
      "learn/02-scattering-basics.html",
      "learn/07-real-space-ift.html",
      "learn/08-models-polydispersity.html",
      "topics/ift/index.html",
      "topics/atsas/index.html",
      "topics/biosas/index.html"
    ]
  },
  "gisaxs": {
    "id": "gisaxs",
    "titleZh": "掠入射小角 X 射线散射",
    "titleEn": "grazing-incidence small-angle X-ray scattering",
    "abbr": "GISAXS",
    "tip": "X 射线以小角度掠入射薄膜样品；结合面内 q 与面外 qz，探测表面与薄膜纳米结构。",
    "aliases": [
      "GISAXS",
      "掠入射 SAXS"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/03-instruments.html",
      "learn/09-application-paths.html",
      "topics/gisaxs/index.html"
    ]
  },
  "asaxs": {
    "id": "asaxs",
    "titleZh": "反常小角散射",
    "titleEn": "anomalous small-angle X-ray scattering",
    "abbr": "ASAXS",
    "tip": "在吸收边附近变能量测量 SAXS，利用反常色散分离特定元素对散射的贡献。",
    "aliases": [
      "ASAXS",
      "反常 SAXS",
      "元素特异 SAXS"
    ],
    "appearsIn": [
      "learn/03-instruments.html",
      "topics/asaxs/index.html"
    ]
  },
  "usaxs": {
    "id": "usaxs",
    "titleZh": "超小角散射",
    "titleEn": "ultra-small-angle scattering",
    "abbr": "USAXS",
    "tip": "覆盖极低 q（常至 10⁻⁴ Å⁻¹ 量级）的小角散射，可探测微米级结构；常见 Bonse–Hart 晶体几何。",
    "aliases": [
      "USAXS",
      "超小角 SAXS",
      "Bonse–Hart"
    ],
    "appearsIn": [
      "learn/03-instruments.html",
      "learn/04-data-reduction.html",
      "topics/calibration/index.html",
      "topics/usaxs/index.html"
    ]
  },
  "magnetic-sans": {
    "id": "magnetic-sans",
    "titleZh": "磁性小角中子散射",
    "titleEn": "magnetic small-angle neutron scattering",
    "abbr": "magnetic SANS",
    "tip": "利用中子磁矩与样品磁化的相互作用，分离核散射与磁散射，研究磁纳米结构。",
    "aliases": [
      "磁性 SANS",
      "磁散射",
      "magnetic scattering"
    ],
    "appearsIn": [
      "learn/02-scattering-basics.html",
      "topics/sans-contrast/index.html",
      "topics/magnetic-sans/index.html"
    ]
  },
  "instrument-smearing": {
    "id": "instrument-smearing",
    "titleZh": "仪器模糊",
    "titleEn": "instrumental smearing",
    "abbr": "smearing",
    "tip": "有限准直、波长展宽与探测器分辨率使测得 I(q) 成为真实截面与仪器权重函数的卷积。",
    "aliases": [
      "smearing",
      "分辨率函数",
      "desmearing",
      "狭缝模糊"
    ],
    "appearsIn": [
      "learn/03-instruments.html",
      "learn/04-data-reduction.html",
      "topics/data-reduction/index.html",
      "topics/usaxs/index.html"
    ]
  },
  "absolute-intensity": {
    "id": "absolute-intensity",
    "titleZh": "绝对强度",
    "titleEn": "absolute intensity",
    "abbr": "AU",
    "tip": "将 I(q) 标定到微分散射截面 dΣ/dΩ（单位 cm⁻¹），使分子量、体积分数等定量解释成为可能。",
    "aliases": [
      "绝对标定",
      "绝对尺度",
      "dΣ/dΩ",
      "cm⁻¹"
    ],
    "appearsIn": [
      "learn/05-absolute-calibration.html",
      "topics/calibration/index.html",
      "topics/usaxs/index.html"
    ]
  },
  "polydispersity": {
    "id": "polydispersity",
    "titleZh": "多分散性",
    "titleEn": "polydispersity",
    "abbr": "PD",
    "tip": "散射体尺寸（或形状）分布宽度；会抹平形式因子振荡，并使 Guinier Rg 偏向大端。",
    "aliases": [
      "多分散",
      "尺寸分布",
      "PD",
      "Schulz"
    ],
    "appearsIn": [
      "learn/08-models-polydispersity.html",
      "topics/polymers-bcp/index.html"
    ]
  },
  "dwba": {
    "id": "dwba",
    "titleZh": "畸变波玻恩近似",
    "titleEn": "distorted-wave Born approximation",
    "abbr": "DWBA",
    "tip": "GISAXS/GISANS 常用理论：以界面反射/折射场为参考波，对侧向纳米结构做微扰散射。",
    "aliases": [
      "DWBA",
      "畸变波 Born 近似"
    ],
    "appearsIn": [
      "learn/03-instruments.html",
      "learn/09-application-paths.html",
      "topics/gisaxs/index.html"
    ]
  },
  "yoneda": {
    "id": "yoneda",
    "titleZh": "Yoneda 峰",
    "titleEn": "Yoneda peak",
    "abbr": "Yoneda",
    "tip": "掠入射散射中出射角接近临界角时的强度增强带；峰位反映材料临界角与电子密度。",
    "aliases": [
      "Yoneda",
      "Yoneda wing",
      "出射临界角峰"
    ],
    "appearsIn": [
      "learn/03-instruments.html",
      "learn/09-application-paths.html",
      "topics/gisaxs/index.html"
    ]
  },
  "block-copolymer": {
    "id": "block-copolymer",
    "titleZh": "嵌段共聚物",
    "titleEn": "block copolymer",
    "abbr": "BCP",
    "tip": "由化学性质不同的聚合物嵌段共价连接而成；可微相分离形成纳米畴，是 SAS/GISAXS 的常见样品。",
    "aliases": [
      "BCP",
      "嵌段聚合物",
      "微相分离"
    ],
    "appearsIn": [
      "learn/09-application-paths.html",
      "topics/gisaxs/index.html",
      "topics/polymers-bcp/index.html"
    ]
  },
  "saxs": {
    "id": "saxs",
    "titleZh": "小角 X 射线散射",
    "titleEn": "small-angle X-ray scattering",
    "abbr": "SAXS",
    "tip": "用 X 射线在小散射角测量 I(q)，探测电子密度起伏引起的纳米到亚微米结构。",
    "aliases": [
      "SAXS",
      "小角X射线散射"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/03-instruments.html",
      "topics/biosas/index.html"
    ]
  },
  "sans": {
    "id": "sans",
    "titleZh": "小角中子散射",
    "titleEn": "small-angle neutron scattering",
    "abbr": "SANS",
    "tip": "用中子在小角测量 I(q)；核散射长度可经 H/D 同位素替换实现衬度匹配与多组分拆解。",
    "aliases": [
      "SANS",
      "小角中子散射"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "topics/sans-contrast/index.html",
      "topics/magnetic-sans/index.html"
    ]
  },
  "waxs": {
    "id": "waxs",
    "titleZh": "广角 X 射线散射",
    "titleEn": "wide-angle X-ray scattering",
    "abbr": "WAXS",
    "tip": "覆盖较高 q（晶格间距量级）的 X 射线散射/衍射；常与 SAXS/USAXS 联用做跨尺度表征。",
    "aliases": [
      "WAXS",
      "WAXD",
      "广角衍射"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/03-instruments.html",
      "topics/usaxs/index.html"
    ]
  },
  "maximum-dimension": {
    "id": "maximum-dimension",
    "titleZh": "最大尺寸",
    "titleEn": "maximum particle dimension",
    "abbr": "Dmax",
    "tip": "粒子内任意两点距离的上界；IFT 中 p(r) 在 r>Dmax 处应趋于零，是选择正则化边界的关键参数。",
    "aliases": [
      "Dmax",
      "D_max",
      "最大粒径"
    ],
    "appearsIn": [
      "learn/07-real-space-ift.html",
      "topics/ift/index.html",
      "topics/biosas/index.html"
    ]
  },
  "kratky-plot": {
    "id": "kratky-plot",
    "titleZh": "Kratky 图",
    "titleEn": "Kratky plot",
    "abbr": "Kratky",
    "tip": "作 q²I(q) 对 q（或无量纲形式）的图，用于直观判断紧凑球状、柔性链或无序蛋白的构象类型。",
    "aliases": [
      "Kratky",
      "Kratky plot",
      "无量纲 Kratky"
    ],
    "appearsIn": [
      "learn/02-scattering-basics.html",
      "topics/biosas/index.html",
      "learn/07-real-space-ift.html"
    ]
  },
  "porod-invariant": {
    "id": "porod-invariant",
    "titleZh": "Porod 不变量",
    "titleEn": "Porod invariant",
    "abbr": "Q",
    "tip": "对 q²I(q) 积分得到的不变量 Q，正比于衬度平方与体积分数乘积，用于体积/浓度类定量。",
    "aliases": [
      "Porod invariant",
      "散射不变量",
      "Q invariant"
    ],
    "appearsIn": [
      "learn/02-scattering-basics.html",
      "learn/05-absolute-calibration.html",
      "topics/polymers-bcp/index.html"
    ]
  },
  "transmission": {
    "id": "transmission",
    "titleZh": "透射率",
    "titleEn": "sample transmission",
    "abbr": "Tr",
    "tip": "透过样品的直射束强度与入射强度之比；用于吸收校正、绝对标定与判断厚度/气泡异常。",
    "aliases": [
      "透射",
      "Tr",
      "T",
      "透射系数"
    ],
    "appearsIn": [
      "learn/04-data-reduction.html",
      "topics/data-reduction/index.html",
      "topics/calibration/index.html"
    ]
  },
  "beamstop": {
    "id": "beamstop",
    "titleZh": "束阻",
    "titleEn": "beamstop",
    "abbr": "",
    "tip": "挡住未散射直射束、保护探测器的挡块；其尺寸与位置决定可用的最低 q。",
    "aliases": [
      "beam stop",
      "直射束挡块"
    ],
    "appearsIn": [
      "learn/03-instruments.html",
      "learn/04-data-reduction.html",
      "topics/data-reduction/index.html"
    ]
  },
  "radial-average": {
    "id": "radial-average",
    "titleZh": "径向平均",
    "titleEn": "radial averaging",
    "abbr": "",
    "tip": "将各向同性 2D 散射图按等 q 环积分，得到一维 I(q)；取向样品则改用扇区平均。",
    "aliases": [
      "环向平均",
      "azimuthal average",
      "一维化"
    ],
    "appearsIn": [
      "learn/04-data-reduction.html",
      "topics/data-reduction/index.html"
    ]
  },
  "contrast-matching": {
    "id": "contrast-matching",
    "titleZh": "衬度匹配",
    "titleEn": "contrast matching",
    "abbr": "",
    "tip": "调节溶剂 SLD（常用 H2O/D2O 比）使某一组分 Δρ→0，从而「熄灭」该相、突出其他组分。",
    "aliases": [
      "匹配点",
      "contrast match",
      "衬度匹配点"
    ],
    "appearsIn": [
      "topics/sans-contrast/index.html",
      "learn/01-what-is-sas.html",
      "learn/09-application-paths.html"
    ]
  },
  "contrast-variation": {
    "id": "contrast-variation",
    "titleZh": "衬度变化",
    "titleEn": "contrast variation",
    "abbr": "CV",
    "tip": "系统改变溶剂或组分氘化程度，采集多条 I(q)，以分解多组分复合物中各相的贡献。",
    "aliases": [
      "衬度变化法",
      "contrast variation",
      "多衬度"
    ],
    "appearsIn": [
      "topics/sans-contrast/index.html",
      "topics/biosas/index.html"
    ]
  },
  "coherent-scattering": {
    "id": "coherent-scattering",
    "titleZh": "相干散射",
    "titleEn": "coherent scattering",
    "abbr": "",
    "tip": "可干涉、携带结构信息的散射；SAS 结构分析默认处理的是弹性相干截面。",
    "aliases": [
      "相干截面",
      "coherent"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/02-scattering-basics.html",
      "topics/sans-contrast/index.html"
    ]
  },
  "incoherent-background": {
    "id": "incoherent-background",
    "titleZh": "不相干本底",
    "titleEn": "incoherent background",
    "abbr": "",
    "tip": "无结构干涉的散射本底；SANS 中氢的不相干截面很大，高 q 常需仔细扣除。",
    "aliases": [
      "不相干散射",
      "incoherent scattering",
      "平坦本底"
    ],
    "appearsIn": [
      "topics/sans-contrast/index.html",
      "learn/04-data-reduction.html",
      "topics/data-reduction/index.html"
    ]
  },
  "multiple-scattering": {
    "id": "multiple-scattering",
    "titleZh": "多重散射",
    "titleEn": "multiple scattering",
    "abbr": "",
    "tip": "光子/中子在样品中散射两次及以上；厚样品或极强散射体上会扭曲 I(q) 并压低表观 Rg。",
    "aliases": [
      "多次散射",
      "multiple scattering"
    ],
    "appearsIn": [
      "learn/01-what-is-sas.html",
      "learn/03-instruments.html",
      "topics/usaxs/index.html"
    ]
  },
  "radiation-damage": {
    "id": "radiation-damage",
    "titleZh": "辐射损伤",
    "titleEn": "radiation damage",
    "abbr": "",
    "tip": "同步辐射等高通量下样品被辐照引起聚集/裂解；表现为 Rg、I(0) 随曝光漂移。",
    "aliases": [
      "辐照损伤",
      "beam damage",
      "辐射损伤"
    ],
    "appearsIn": [
      "topics/biosas/index.html",
      "topics/sample-env/index.html",
      "learn/03-instruments.html"
    ]
  },
  "sec-saxs": {
    "id": "sec-saxs",
    "titleZh": "色谱联用小角散射",
    "titleEn": "size-exclusion chromatography SAXS",
    "abbr": "SEC-SAXS",
    "tip": "将尺寸排阻色谱与 SAXS 在线联用，在洗脱峰上取帧以降低聚集与组分混合物干扰。",
    "aliases": [
      "SEC-SAXS",
      "SEC-SAS",
      "凝胶过滤联用 SAXS"
    ],
    "appearsIn": [
      "topics/biosas/index.html",
      "topics/atsas/index.html",
      "topics/sample-env/index.html"
    ]
  },
  "ab-initio-reconstruction": {
    "id": "ab-initio-reconstruction",
    "titleZh": "从头形状重建",
    "titleEn": "ab initio shape reconstruction",
    "abbr": "ab initio",
    "tip": "在少原子先验下，由 I(q) 或 p(r) 重建低分辨三维形状（如 DAMMIN/DAMMIF 哑原子模型）。",
    "aliases": [
      "ab initio",
      "哑原子模型",
      "DAMMIF",
      "DAMMIN",
      "形状重建"
    ],
    "appearsIn": [
      "topics/atsas/index.html",
      "topics/biosas/index.html",
      "learn/09-application-paths.html"
    ]
  },
  "ensemble-optimization": {
    "id": "ensemble-optimization",
    "titleZh": "系综优化方法",
    "titleEn": "ensemble optimization method",
    "abbr": "EOM",
    "tip": "从大构象池中选出子系综以拟合柔性分子的 I(q)；报告的是分布而非单一结构。",
    "aliases": [
      "EOM",
      "系综拟合",
      "ensemble fitting"
    ],
    "appearsIn": [
      "topics/atsas/index.html",
      "topics/biosas/index.html"
    ]
  },
  "bonse-hart": {
    "id": "bonse-hart",
    "titleZh": "Bonse–Hart 光学",
    "titleEn": "Bonse–Hart crystal collimation",
    "abbr": "Bonse–Hart",
    "tip": "用完美晶体对做超高角分辨准直的 USAXS 经典配置；测得曲线常为狭缝模糊的一维剖面。",
    "aliases": [
      "Bonse-Hart",
      "双晶 USAXS",
      "晶体准直"
    ],
    "appearsIn": [
      "topics/usaxs/index.html",
      "learn/03-instruments.html"
    ]
  },
  "critical-angle": {
    "id": "critical-angle",
    "titleZh": "临界角",
    "titleEn": "critical angle",
    "abbr": "αc",
    "tip": "X 射线/中子在界面发生全外反射的入射角上限；GISAXS 中 αi、αf 相对 αc 决定穿透深度与 Yoneda 峰。",
    "aliases": [
      "αc",
      "critical angle",
      "全反射临界角"
    ],
    "appearsIn": [
      "topics/gisaxs/index.html",
      "learn/03-instruments.html",
      "learn/09-application-paths.html"
    ]
  },
  "order-disorder-transition": {
    "id": "order-disorder-transition",
    "titleZh": "有序–无序转变",
    "titleEn": "order–disorder transition",
    "abbr": "ODT",
    "tip": "嵌段共聚物等体系在加热/改变 χN 时，由微相有序态变为无序相关穴态的相变。",
    "aliases": [
      "ODT",
      "有序无序转变",
      "ODT temperature"
    ],
    "appearsIn": [
      "topics/polymers-bcp/index.html",
      "learn/09-application-paths.html"
    ]
  },
  "microphase-separation": {
    "id": "microphase-separation",
    "titleZh": "微相分离",
    "titleEn": "microphase separation",
    "abbr": "",
    "tip": "嵌段因不相容而局部相分离、却因共价键无法宏观分相，形成纳米畴（层状、柱状、球状等）。",
    "aliases": [
      "微相分离",
      "纳米相分离",
      "微畴"
    ],
    "appearsIn": [
      "topics/polymers-bcp/index.html",
      "topics/gisaxs/index.html"
    ]
  },
  "flory-huggins-chi": {
    "id": "flory-huggins-chi",
    "titleZh": "Flory–Huggins 相互作用参数",
    "titleEn": "Flory–Huggins interaction parameter",
    "abbr": "χ",
    "tip": "描述聚合物链段间混合焓性相互作用的参数；与聚合度 N 组成 χN，控制 BCP 分凝强度。",
    "aliases": [
      "χ",
      "chi",
      "Flory-Huggins",
      "χN"
    ],
    "appearsIn": [
      "topics/polymers-bcp/index.html"
    ]
  },
  "anomalous-dispersion": {
    "id": "anomalous-dispersion",
    "titleZh": "反常色散",
    "titleEn": "anomalous dispersion",
    "abbr": "f′, f″",
    "tip": "在吸收边附近原子形状因子的能量依赖修正 f′、f″；ASAXS 借此分离特定元素贡献。",
    "aliases": [
      "反常散射因子",
      "f'",
      "f″",
      "anomalous scattering"
    ],
    "appearsIn": [
      "topics/asaxs/index.html",
      "learn/03-instruments.html"
    ]
  },
  "glassy-carbon": {
    "id": "glassy-carbon",
    "titleZh": "玻璃碳标样",
    "titleEn": "glassy carbon calibration standard",
    "abbr": "GC",
    "tip": "常用作 SAXS/USAXS 二级绝对强度标样的稳定碳材料；NIST 亦有 SRM 3600 认证曲线。",
    "aliases": [
      "玻璃碳",
      "glassy carbon",
      "GC standard",
      "SRM 3600"
    ],
    "appearsIn": [
      "topics/calibration/index.html",
      "learn/05-absolute-calibration.html",
      "topics/usaxs/index.html"
    ]
  },
  "fractal-scattering": {
    "id": "fractal-scattering",
    "titleZh": "分形散射",
    "titleEn": "fractal scattering",
    "abbr": "",
    "tip": "在对数坐标下 I(q)∝q⁻ᵖ 的幂律区；指数 p 联系质量分形或表面分形维数。",
    "aliases": [
      "分形",
      "幂律散射",
      "fractal dimension"
    ],
    "appearsIn": [
      "topics/usaxs/index.html",
      "learn/06-guinier-porod.html",
      "learn/08-models-polydispersity.html"
    ]
  },
  "beaucage-unified": {
    "id": "beaucage-unified",
    "titleZh": "Beaucage 统一模型",
    "titleEn": "Beaucage unified scattering function",
    "abbr": "Unified Fit",
    "tip": "把 Guinier 区与幂律尾衔接的经验/半经验模型，适于多层次聚集体的宽 q 拟合。",
    "aliases": [
      "Unified model",
      "Beaucage",
      "统一拟合"
    ],
    "appearsIn": [
      "learn/08-models-polydispersity.html",
      "topics/usaxs/index.html",
      "learn/06-guinier-porod.html"
    ]
  },
  "guinier-porod-model": {
    "id": "guinier-porod-model",
    "titleZh": "Guinier–Porod 模型",
    "titleEn": "Guinier–Porod model",
    "abbr": "GP",
    "tip": "Hammouda 等提出的经验模型，用维数参数 s 与 Porod 指数衔接低 q Guinier 与高 q 幂律。",
    "aliases": [
      "Guinier-Porod",
      "GP model",
      "Hammouda model"
    ],
    "appearsIn": [
      "learn/06-guinier-porod.html",
      "learn/08-models-polydispersity.html"
    ]
  },
  "gnom": {
    "id": "gnom",
    "titleZh": "GNOM",
    "titleEn": "GNOM (regularized IFT)",
    "abbr": "GNOM",
    "tip": "ATSAS 中基于感知准则的正则化间接傅里叶变换程序，由 I(q) 求 p(r)。",
    "aliases": [
      "GNOM",
      "正则化 IFT"
    ],
    "appearsIn": [
      "topics/ift/index.html",
      "topics/atsas/index.html",
      "learn/07-real-space-ift.html"
    ]
  },
  "gift": {
    "id": "gift",
    "titleZh": "GIFT",
    "titleEn": "generalized indirect Fourier transformation",
    "abbr": "GIFT",
    "tip": "广义间接傅里叶变换，可同时处理形式因子与结构因子，适合带电胶体等相互作用体系。",
    "aliases": [
      "GIFT",
      "广义 IFT"
    ],
    "appearsIn": [
      "topics/ift/index.html",
      "learn/07-real-space-ift.html",
      "learn/08-models-polydispersity.html"
    ]
  },
  "desmearing": {
    "id": "desmearing",
    "titleZh": "去模糊",
    "titleEn": "desmearing",
    "abbr": "",
    "tip": "从狭缝模糊的实验曲线数值还原近似针孔 I(q) 的过程；亦可对模型做 smeared 拟合而避免显式反演。",
    "aliases": [
      "desmear",
      "去卷积",
      "Lake 算法"
    ],
    "appearsIn": [
      "topics/usaxs/index.html",
      "learn/03-instruments.html",
      "topics/data-reduction/index.html"
    ]
  },
  "volume-fraction": {
    "id": "volume-fraction",
    "titleZh": "体积分数",
    "titleEn": "volume fraction",
    "abbr": "φ",
    "tip": "散射相所占体积比例；绝对强度下 I(0) 与 Porod 不变量均依赖 φ 与衬度。",
    "aliases": [
      "φ",
      "phi",
      "体积浓度"
    ],
    "appearsIn": [
      "learn/02-scattering-basics.html",
      "learn/05-absolute-calibration.html",
      "topics/calibration/index.html"
    ]
  },
  "persistence-length": {
    "id": "persistence-length",
    "titleZh": "持续长度",
    "titleEn": "persistence length",
    "abbr": "lp",
    "tip": "描述半柔顺链取向关联衰减的特征长度；影响聚合物链形式因子的中间 q 行为。",
    "aliases": [
      "lp",
      "persistence length",
      "刚性长度"
    ],
    "appearsIn": [
      "topics/polymers-bcp/index.html",
      "learn/08-models-polydispersity.html"
    ]
  },
  "correlation-length": {
    "id": "correlation-length",
    "titleZh": "关联长度",
    "titleEn": "correlation length",
    "abbr": "ξ",
    "tip": "密度涨落或微畴关联衰减的特征尺度；无序 BCP 相关峰宽度与 ξ 相关。",
    "aliases": [
      "ξ",
      "xi",
      "相关长度"
    ],
    "appearsIn": [
      "topics/polymers-bcp/index.html",
      "learn/02-scattering-basics.html"
    ]
  },
  "polarization-analysis": {
    "id": "polarization-analysis",
    "titleZh": "极化分析",
    "titleEn": "neutron polarization analysis",
    "abbr": "POLARIS/SANSPOL",
    "tip": "用极化中子与自旋分析分离核相干、自旋非相干与磁散射贡献的实验技术。",
    "aliases": [
      "SANSPOL",
      "POLARIS",
      "极化 SANS",
      "自旋分析"
    ],
    "appearsIn": [
      "topics/magnetic-sans/index.html"
    ]
  },
  "data-reduction": {
    "id": "data-reduction",
    "titleZh": "数据还原",
    "titleEn": "data reduction",
    "abbr": "",
    "tip": "从原始 2D/飞行时间数据经暗电流、平场、掩膜、透射、本底到 I(q) 的校正流水线。",
    "aliases": [
      "还原",
      "数据还原",
      "reduction pipeline"
    ],
    "appearsIn": [
      "learn/04-data-reduction.html",
      "topics/data-reduction/index.html"
    ]
  }
};
