# Flame Atlas 前後端交接包

這是目前 v0.10.3 主頁與其實際執行資料的離線交接包，也包含已準備的 OpenAI Responses 串接程式。原始工作區與正在運作的 demo 不會被修改。

## 檔案怎麼看

- `frontend/`：目前提供的 HTML、JavaScript、CSS、場景 SVG、字型及字型授權。主頁入口為 `atlas.html`；保留的 `index.html` 是舊搜尋頁。後端根網址 `/` 仍會開啟目前主頁。
- `backend/workspace/`：目前主搜尋、排序、摘要、來源綁定與互動模型的 Python 程式。
- `backend/retained/`：主程式實際匯入的舊版後端依賴、液體比較與場景/消防策略模組。
- `data/`：文獻目錄、29 個圖表的資料與既有模型宣告、場域與消防洞見、標準/設備條件，以及目前讀取的完整液體 CSV。使用者於 2026-11-15 已授權將這次 demo 執行資料與原始來源表放進既有私有 GitHub。完整論文與模型權重仍分開處理。
- `MANIFEST.json`：每個檔案的大小、SHA-256 及來源複製狀態。
- `PAPERS_NOT_INCLUDED.json`：未隨包附上的論文清單。完整論文、模型權重、金鑰、環境與訓練暫存均未打包。
- `PACKAGE_TRANSFORMATIONS.json`：為了移機而清除的本機 PDF 連結；原始目錄保留在 `data/original/bridge_catalog.json`，物理數據與研究結論未重算。

## 啟動

先將兩個分包解壓到同一個位置（都會建立 `Flame_Atlas/`），或直接解壓完整包。安裝 Python 3.12，於該目錄執行：

```text
python -m pip install -r requirements.txt
python run.py
```

Windows 也可執行 `start_windows.cmd`。預設為 OpenAI API：請先在執行後端的環境設定 `OPENAI_API_KEY`，不要把內容貼進聊天、放進前端或提交 GitHub。使用 gpt-6.1-sol、max、Fast。沒有金鑰會明確停止，不會自動改用 Qwen。

瀏覽器開啟 `http://127.0.0.1:8794/`。若該連接埠已被原 demo 使用，執行 `python run.py --port 8820`。設定值參考 `backend/env.example`；不要直接雙擊 HTML 期待 API 搜尋能執行。

僅驗證檔案、索引與資料能載入（不呼叫 API）：

```text
python run.py --check --ai-mode off
```

若要看離線模式的主頁，可執行 `python run.py --ai-mode off --port 8820`；這是明確的驗收/離線模式，不是 ChatGPT 摘要實測。本機 Qwen 僅能用 `--ai-mode local` 明確選擇，而且必須自行先啟動已有模型服務，本包不啟動或下載模型。

## 邊界

目前主頁的文獻搜尋、來源洞見與已連結圖表/滑桿資料都在包內。外部 DOI、NTRS、NASA PSI 原站仍需網路。原本 8793 的舊模型頁及 8784 的舊語意檢索服務在盤點時沒有啟動，未納入本包；保留舊輔助頁的外連並列於 `EXTERNAL_DEPENDENCIES.json`。完整論文留在原本離線來源集合，包內改顯示原站連結。

這是可移機驗證的本機交接包，不是已上線的雲端服務。公開部署仍要調整允許的主機/來源、HTTPS、多人請求與 API 用量保護。資料和論文的原有使用限制仍適用；本包不宣稱 NASA 背書，也不執行訓練或重新擬合。
