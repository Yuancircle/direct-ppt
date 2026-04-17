# direct-ppt

> English and 中文 in one README.

`direct-ppt` is a blueprint-first PPTX skill for generating polished, editable PowerPoint slides directly from approved page blueprints.

`direct-ppt` 是一个**蓝图优先**的 PPTX 技能：先确认页面蓝图，再直接产出可编辑、可交付的 `.pptx`。

---

## English

### What it is

`direct-ppt` is designed for **any PPT page**, not just a single slide type.

Use it when you want:
- editable `.pptx` output
- blueprint-first workflow
- approval before rendering
- stronger visual structure for cover pages, report pages, roadmap pages, timeline pages, action-plan pages, and more

### Core value

- Blueprint first
- Editable PPTX output
- Offline-friendly bundled runtime
- Built-in presentation design lens
- Better defaults for title systems, grouped tables, containers, and editable text

### Built-in design lens

`direct-ppt` now includes a built-in presentation design lens. You do **not** need to load a separate design skill just to get this methodology.

Before rendering, the skill should explicitly define:
- **Color System**
- **Typography**
- **Layout System**
- **Visual Elements**
- **Mood & Tone**

It also includes stronger design rules for:
- choosing a stable **title system** instead of patching title cards repeatedly
- making large rounded containers truly carry the content
- using **row-group / full-band color grouping** for table-heavy slides
- keeping the top-left corner from becoming a visual conflict zone

### Integration boundary

The design methodology is already built into `direct-ppt`.

What is included:
- design thinking framework
- hierarchy rules
- title / grouping / container guidance

What is **not** included:
- any external presentation-generation API service
- remote paid generation workflows
- third-party API credentials

If you explicitly want an external API workflow, handle that separately.

### Editable-text default

`direct-ppt` defaults to:
- fixed `fontSize`
- reasonable text box sizes
- manual line breaks when needed
- **no blanket `fit: 'shrink'`** for titles, paragraphs, tables, timelines, and other user-editable core content

This improves actual editability in PowerPoint.

### Repo structure

```text
.
├── SKILL.md
├── README.md
├── assets/
│   └── runtime/
├── scripts/
└── references/
```

### Quick install

1. Copy this repository folder into your agent workspace as `direct-ppt/`, or download the files directly.
2. Keep `assets/runtime/` next to `SKILL.md`.
3. If the environment already has `pptxgenjs`, it can use that.
4. Otherwise, the bundled offline runtime will be used.

### Typical workflow

1. Collect the brief
2. Define the design lens
3. Draft the blueprint
4. Get approval
5. Render PPTX
6. Check overlap, clipping, wraps, pale/tiny text, and visual conflicts

---

## 中文

### 这是什么

`direct-ppt` 面向的是**任何 PPT 页面**，不是只做某一种单页。

适合这些场景：
- 需要直接交付可编辑 `.pptx`
- 先出蓝图，再确认，再出成品
- 封面页、汇报页、目录页、路线图页、时间线页、行动计划页等

### 核心价值

- 蓝图优先
- 直接输出可编辑 PPTX
- 自带离线运行时
- 内建设计镜头
- 对标题系统、分组表格、主容器、可编辑文字有更稳的默认标准

### 内建设计理念

现在 `direct-ppt` 已经内置了一套演示文稿设计镜头，正常做 PPT 时**不需要再额外加载别的设计 skill** 才能拿到这套方法。

在蓝图阶段，会先明确这五件事：
- **Color System（颜色系统）**
- **Typography（字体层级）**
- **Layout System（版式结构）**
- **Visual Elements（视觉元素）**
- **Mood & Tone（页面气质）**

同时，skill 里已经固化了这几类设计规则：
- 标题系统要先定，不要靠补丁式加标题卡片和装饰去救场
- 大圆角主容器如果存在，就必须真正承载内容
- 表格型页面默认用**整组 / 整行分组色**，不是只染第一列
- 避免左上角同时堆圆角、标题卡片、装饰条，造成视觉打架

### 集成边界

已经内置进 `direct-ppt` 的，是这套**设计方法论和设计判断逻辑**。

没有内置进来的，是：
- 外部在线生成 API
- 第三方远程生稿服务
- 任何需要单独 API key 的能力

也就是说：
- **设计理念已经内置**
- **外部 API 能力没有内置**

### 可编辑文字默认策略

`direct-ppt` 默认采用：
- 固定 `fontSize`
- 合理文本框尺寸
- 必要时手动换行
- 对标题 / 正文 / 表格 / 时间线 / 行动计划等核心内容，默认**禁用**大面积 `fit: 'shrink'`

这样生成出来的 PPT，后续在 PowerPoint 里更容易真正编辑。

### 仓库结构

```text
.
├── SKILL.md
├── README.md
├── assets/
│   └── runtime/
├── scripts/
└── references/
```

### 快速安装

1. 把当前仓库整体复制到 agent workspace 中，目录名建议为 `direct-ppt/`
2. 保持 `assets/runtime/` 与 `SKILL.md` 同级存在
3. 如果环境里已有 `pptxgenjs`，会优先使用
4. 如果没有，就走仓库自带的离线 runtime

### 典型工作流

1. 收集页面 brief
2. 先定义设计镜头
3. 写蓝图
4. 等确认
5. 直接渲染 PPTX
6. 交付前检查重叠、裁切、换行、浅字、小字和视觉冲突
