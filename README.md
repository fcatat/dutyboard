## 员工假期值班排班表（2026）

本项目基于国务院办公厅发布的 **2026 年部分节假日安排**（[国办发明电〔2025〕7 号](https://www.gov.cn/zhengce/zhengceku/202511/content_7047091.htm)）制作，可快速生成覆盖节假日及延伸日期的在线排班表。

### 部署方式

1. **Cloudflare Pages**：在 Pages 后台新建项目，仓库指向本代码库。
   - Build command 留空。
   - Build output directory 设置为 `web`。
   - 构建完成后，Pages 会把 `web/` 里的静态资源原样部署到全球 CDN。
2. **本地预览**：项目已内置 Wrangler 依赖与脚本，本地运行与 Pages 行为一致。

```bash
npm install               # 安装依赖
npm run dev               # 启动本地预览（默认 8787 端口）
```

如需手动部署，可运行 `npm run deploy`，Wrangler 将把 `web/` 目录直接推送至 Cloudflare Pages。Wrangler 支持自动刷新、正确的 MIME 类型和未来若引入 Edge Functions 时的本地调试体验，使用上好于 `python -m http.server`。

在页面中可以：

- 选择 2026 年的法定节假日；
- 设置展示的员工行数（可直接编辑单元格录入姓名）；
- 调整假期前后延伸天数（默认 3 天，最大 14 天），周末自动标记为放假；
- 点击单元格在“休”“班”“值”“空”之间循环标记，辅助排班；
- 导出排班结果为 PDF（含图例）或 Excel（包含图例工作表）。

本项目为纯前端实现，所有排班信息仅在浏览器本地生成，不会上传至任何服务器，请放心使用。

在线体验地址：https://dutyboard.nops.icu

![界面效果示例](docs/screenshot.png)
