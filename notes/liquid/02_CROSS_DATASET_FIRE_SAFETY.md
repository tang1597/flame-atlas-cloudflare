# 跨資料集的共同機制、差異與消防問題

這裡把來源觀察、作者解釋和待驗證構想分開。研究對象是隔離液滴及相關數值/地面機制試驗，不是現場滅火操作。沒有提出閥序列、載人艙稀釋設定或通用滅火門檻。

## 共同與差異

| 比較 | 可共用的物理問題 | 必須保留的差異／不能合併 |
|---|---|---|
| FLEX甲醇 vs烷烴 | 傳熱、擴散、液滴回縮與消失事件 | 甲醇水吸收/蒸發與烷烴低溫化學不同；同K不是同機制。FLEX-MEOH2013:C02、CC01。 |
| FLEX/FLEX2/CFI | CIR/MDCA單滴光學觀測與局部熱/質量傳輸 | 共硬體不等於同燃料、氣氛、壓力、支撐、點火及先前燃燒歷程。 |
| CFI純燃料 vs blends/farnesane | 組成與低溫反應如何改變階段持續與熄滅 | C12H26、farnesane、iso-dodecane/blends不能只按碳數合併；CFI報告blend為mass basis，PRF50文獻為volume basis。 |
| hot/cool/warm階段 | 觀察終點與熱損失/化學時間尺度 | 可見火焰消失≠所有反應停止；gasT/radiance/UV/液滴D是不同觀測。CC01、CC02。 |
| free vsfiber | 支撐造成熱/動量干擾 | 來源局部相近不證明跨所有D0等效；ground-drop/ISS的支撐、點火也不同。FLEX-ALKANE-D0-2013:C01。 |
| 壓力系列 | 低溫化學、熱損失、stage轉換及有限熄滅端點 | 不能只用氧分壓取代P和組成；完成燃燒後沒有finitecool端點不能畫成確切De=0。CC10。 |
| 地面與ISS | 浮力/停留時間/輸運條件的差別 | 目前詳讀的地面drop arm也是reducedgravity，未提供matched1g或部分重力驗證。 |
| PSI142與液滴族群 | 氣相低溫反應、對向流/預混與光學診斷相關機制 | 噴嘴/流動架構不是MDCA液滴；8個data-ID sheets不加進burn數，不替液滴補流速/時序。 |

## 具體消防洞見與研究構想

| ID／消防問題 | 原始證據與已支持判斷 | 研究構想（HYPOTHESIS） | 最小待驗證條件／不能宣稱 |
|---|---|---|---|
| LIQ-P01 預防：液體洩漏後的持續燃燒 | FLEX-TP2015、PRF2020、CFI-REPORT2020：單滴D0、氣氛、P、支撐/點火與回縮/階段結果相關。 | 為特定艙內液體配方建立matched液滴風險試驗矩陣，連到洩漏隔離/材料與儲存設計評估。 | 要有實際formulation、D0、氣/液T、P/O2、流場/actualg、支撐及點火史；不能由單滴預測任意池火、噴霧或洩漏幾何。 |
| LIQ-D01 偵測：可見火焰消失後是否仍有反應 | CC01；FLEX-COOL2013與CFI報告/簡報：影像、液滴回縮和模型低溫反應資訊並非同量。 | 多通道visible/UV/IR訊號及持續液滴消耗的聯合判讀器。 | 先建立同步時鐘、校準、background和stage真值，再測偵測/漏報；不能從變暗單獨標no-fire或no-ignition。 |
| LIQ-D02 偵測：煙炱/輻射影像如何可靠解讀 | Optical2014及2025publisher-indexed reanalysis：邊界與反演假設改變推定量。 | 具有影像品質與光學校準追蹤的研究監測系統，保留raw intensity和inferred量。 | 需原frame、pixel/mm、波段、Abel對稱/路徑、Ke選擇及不確定度；尚未驗證空間煙霧感測器或人體暴露。 |
| LIQ-S01 抑制：稀釋氣的作用能否分辨 | FLEX甲醇CO2/He/O2-N2預置氣氛改變液滴行為；尺寸/壓力/熱史仍可不同。 | 把O2稀釋與熱傳性分開的受控稀釋機制比較，作為未來設備研究依據。 | 需matchedP/O2/D0/溫度/流動與真正介入時序；目前不是噴入劑量、滅火時間或載人艙容許配方。 |
| LIQ-S02 抑制後狀態：殘液與多階段終點 | CC02、CC10：high-P warm/cool及沒有finitecool熄滅端點，與普通visible消失不同。 | 記錄殘液、反應階段與熱狀態的研究驗收流程，避免只看visible訊號。 | 需可獨立確認化學/熱狀態和後續觀察；不能給通用等候時間、復燃機率或現場操作建議。 |
| LIQ-M01 模型可移植性：同碳數是否夠 | CC05、CC07：heptane化學加dodecane物性不建立dodecane kinetics，來源參數有校準。 | 對照獨立配方/壓力/尺寸條件，辨識化學與傳輸缺口。 | 先取得原mechanism、state/properties及matched comparator，不從目標反推T/transport；低殘差不代表機制唯一或設備合格。 |

上述構想沒有在本輪建造、擬合或部署。它們是從資料缺口提出的研究方向，不是已驗證產品功能。

## 因素與量測角色：依protocol判斷

| 角色 | 本輪可見欄位 | 解讀限制 |
|---|---|---|
| 事前材料/配置 | exact fuel、mixture、volume/mass basis、support | 不把formula label當完整異構物/配方證明。 |
| across-runs操縱 | P、O2/diluent、targetD0、fuel、fiber；FLEX2規劃流動/array | Study曾改變不等於每次run都獨立操縱或其餘量恆定；規劃矩陣不當完成值。 |
| nominal/initial設定 | chamber fill、initialD、igniter command | ActualD0時鐘依來源，可能在igniterON；不自稱純preignition。 |
| raw/calibrated訊號 | camera intensity、radiometer/儀器電訊號、timestamps | 通道、單位、reference state、calibration需逐欄確認；V/A不是熱功率。 |
| image/time-series derived | D、Df、FSR、K、eventduration | K是同response分析，不是intrinsic diffusivity；stage、窗口及FOV/extrapolation保留。 |
| model output | Tmax、species、D(t)、radiation、K | 不改稱測得的T/組成或新增flightcase。 |
| confound/history/unknown | residualvapors、先前燃燒、漂移/纖維/點火擾動、actualg/溫度 | 缺值不補零，不補室溫，不把quiescent改成精確零流速。 |

完整欄位盤點有112項、12種角色；使用者Excel127列對照屬候選語義映射，不是127條已驗證numericjoin。[factor_dictionary.json](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/factor_dictionary.json>)；[factor_crosswalk.json](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/factor_crosswalk.json>)；[Excel對照Markdown](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/factor_crosswalk.md>)。

## 下一步資料優先順序

1. 先補exact圖點→runID→camera frame/calibration/clock，能分出獨立burn、來源重複與stage。
2. 再補同條件氣/液T、P與成分、actualg/流場、support/ignition/history及完整化學/物性檔。
3. 消防裝置評估要另做與目標幾何、介入方式、感測器及驗收終點相符的實驗；現有單滴結果只提供機制與設計線索。

52個來源葉節點與資料角色可逐一查：[04 子資料集索引](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/markdown/04_SUBDATASET_INDEX.md>)。
