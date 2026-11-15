# Detection of Smoke from Microgravity Fires

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-ace2a1841b1a | research conference presentation with experimental charts/tables and model explanation; not rawimagealbum | {"source": "SharedlegacyPPT,ICES/EuropeanSymposium,Rome,July11-14,2005. ThreePSIpathsarebyte-identical aliases of this one deck.", "reading_copy": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\output\\earth_space_transfer_20261114\\phase5_shared_document_review\\role_E\\same\\source_extracts\\Detection2005_deck_reading_copy.pdf", "reading_copy_sha256": "8c82800a7fdd647a1365fb5d4397b2dd4d0f04060b761c06b1fb55a64008cf29"} | ace2a1841b1ae2441f8e09741e82ab09635d2d676f76238442f44c2ce437cc30 | {"slides": 32, "physical_pdf_pages": 32} | prior_primary_audit_reused_source_bytes_reverified |


- https://psi.nasa.gov/physci/repo/data/investigations/PSI-101
- https://psi.nasa.gov/physci/repo/data/investigations/PSI-102
- https://psi.nasa.gov/physci/repo/data/investigations/PSI-47


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/第一批下載/PSI-101_SAME-R/Presentations/PSI-101_Presentations_Detection of Smoke from Microgravity Fires.ppt>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-ace2a1841b1a-C01 | 第 18 張投影片列出實際 1g TEM 初級粒徑：Kapton 35 nm、蠟燭 17 nm、Teflon 75 nm；這些重複 CSD 論文資料，不是新增獨立試驗。 | measurement | s18 | The PSI101/102/47 paths are identical copies of one presentation, not independent datasets. | Unknown（來源未提供／尚未核對） |
| SMOKE-ace2a1841b1a-C02 | 簡報展示 SAME 之前的台架校正及矩／撞擊器結果，並保留無效的烤吐司結果。第 25 張投影片粒徑欄標為 mm，而原 NASA 2003 表標為 μm；這是版次間的單位標示差異，不是新發現的千倍粒徑差。 | measurement | s23-28 | Slide25 repeats the five-smoke table in NASA2003Table1, but the deck literally labels diameter columns mm. The original NASA2003 table explicitly labels micrometers. This is a source-edition unit-label discrepancy, not a new1000-fold size result. | Unknown（來源未提供／尚未核對） |
| SMOKE-ace2a1841b1a-C03 | 簡報把工程說明、未來 SAME／DAFT 計畫與既有實測研究結果交錯呈現，閱讀時須保留各項工作的實際完成狀態。 | design_or_operations | s20,s29-32 | The PSI101/102/47 paths are identical copies of one presentation, not independent datasets. | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-101", "PSI-102", "PSI-47"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- {"factor": "source_conditions", "values": {"equations": "SeeP5S-M1/M3;slide21 contains a general scattering-kernel integral.", "ground_table": "Slide25 repeats the five-smoke table in NASA2003Table1, but the deck literally labels diameter columns mm. The original NASA2003 table explicitly labels micrometers. This is a source-edition unit-label discrepancy, not a new1000-fold size result.", "calibration": "Slide26 compares P-Trak with ELPI;slide27 compares ion chamber with calculated first moment;slide28 compares DustTrak with TEOM. The labels identify DOP calibration aerosols.", "aliases": "The PSI101/102/47 paths are identical copies of one presentation, not independent datasets."}, "status": "source_condition_context_not_per_trial_controls", "source_locator": ["s1 title/byline/meeting", "s8 detector sensitivity reference", "s9-19CSDexperiment,ground/flightcomparators,TEManddetectiontable", "s20-25SAMEplan,momentsandgroundtesttable", "s26-28actualinstrumentcalibrationplots", "s29-32earlyDAFTresults"]}


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- Same underlying2005 publication as the DOC; one shared work-level quotation and one CSD experiment family.
- The literal slide25 mm label is retained as a discrepancy; acquired numerical ground values use the original2003 article micrometer units.
- Exact bench pressure,oxygen fraction,temperature and raw traces are not supplied by these slides.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

來源尚未提供可核對的項目；不填成 0。
