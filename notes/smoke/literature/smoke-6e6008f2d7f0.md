# Dust and Aerosol measurement Feasibility Test (DAFT),30Day Report

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-6e6008f2d7f0 | Primary postflight research/operations report with measurements and source calculations | Printed title30Day Report, no internal issue date found. PDF source-modified metadata22November2006; PDF creation10May2007. These are file metadata, not silently assigned publication dates. | 6e6008f2d7f0216432f7df5579579264a34c3a29601a9f0688461019d59be1e4 | {"physical_pdf_pages": 14} | prior_primary_audit_reused_source_bytes_reverified |


- https://psi.nasa.gov/physci/repo/data/investigations/PSI-47


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-47_DAFT _ DAFT-2/Reports/PSI-47_Reports_DAFT_30Day.PostFlightReport.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-6e6008f2d7f0-C01 | 報告提供三個在軌氣膠袋的 P-Trak／DustTrak 讀值，以及 2003 年 5 月以近似飛行設備進行的地面組員訓練散點資料；這些地面資料與後續報告重複，不另計為獨立實驗。 | measurement | p11Figure5;p12Figure6orbital/7ground;ground descriptionp8 | ARD(Fine),GN2,15-L bags; shared sampling/DAFT impactor. Three orbital bags on21August2006; ground tests May2003. Exact ground P/T/Q/lot unknown. | Unknown（來源未提供／尚未核對） |
| SMOKE-6e6008f2d7f0-C02 | 作者以質量／數目關係及假設密度 1 g/cm³ 推算等效平均直徑；這不是直接量測的粒徑或粒徑分布，也不是獨立預測。 | calculation | p11Figure5;interpretationp8 | P-Trak number concentrationparticles/cm3; DustTrak mass-equivalentmg/m3;source density assumption 1 g/cm3. | Unknown（來源未提供／尚未核對） |
| SMOKE-6e6008f2d7f0-C03 | 報告記錄酒精供應有限、資料記錄失敗、光學腔可能累積粒子，以及未完成未改裝 P-Trak 測試等問題。粒子累積是作者對在軌趨勢的可能解釋，並非另行量得的損失率。 | author_interpretation | pp7,13-14 | Replacement wick could not be opened; previous wick reused.30s voiced readings; beeping could be alcohol warning or sample vacuum. | Unknown（來源未提供／尚未核對） |
| SMOKE-6e6008f2d7f0-C04 | 作者報告，地面測試曾在部分大型 ARD 粒子高負載條件下觀察到粒子累積；這是定性觀察，未提供定量系列、負載門檻或損失係數。 | measurement | p13 Sample Build Up | Large ARD particle load to P-Trak optics; threshold and loss coefficient unspecified. | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-47"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- {"factor": "source_conditions", "values": {"R1": "ARD(Fine),GN2,15-L bags; shared sampling/DAFT impactor. Three orbital bags on21August2006; ground tests May2003. Exact ground P/T/Q/lot unknown.", "R2": "P-Trak number concentrationparticles/cm3; DustTrak mass-equivalentmg/m3;source density assumption 1 g/cm3.", "R3": "Replacement wick could not be opened; previous wick reused.30s voiced readings; beeping could be alcohol warning or sample vacuum.", "R4": "Large ARD particle load to P-Trak optics; threshold and loss coefficient unspecified."}, "status": "source_condition_context_not_per_trial_controls", "source_locator": ["pp1-14 fulltext", "pp8,11-14 complete plots/table/conclusions visually inspected"]}


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- Intended15dust points were not completed.
- Unmodified-P-Trak flight control was not performed.
- No gravity-independent universal calibration proved.
- Report figures are reordered relative to later versions:groundFigure7p12 here versusFigure6p14 later.
- Source estimated25mg delivered from0.25g holder is not measured per-run suspended aerosol mass.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

來源尚未提供可核對的項目；不填成 0。
