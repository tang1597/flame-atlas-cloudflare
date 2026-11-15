# Dust and Aerosol Measurement Feasibility Test (DAFT)

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-3e50d1d643ba | NASA public fact sheet with early results and future-test plan | Undated printed fact sheet; PDF creation2005-10-27, modification2006-01-04. Metadata dates are not asserted publication dates. | 3e50d1d643ba0511a70986e26798dbcac1a9b4b0528d3c47db22615e9d7b4e6e | {"physical_pdf_pages": 2} | prior_primary_audit_reused_source_bytes_reverified |


- https://psi.nasa.gov/physci/repo/data/investigations/PSI-47


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/第一批下載/PSI-47_DAFT _ DAFT-2/Presentations/PSI-47_Presentations_Daft_FactSheet.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-3e50d1d643ba-C01 | Reports early undisturbed ISS cabin readings below 0.005 mg/m3 on DustTrak and 15 particles/cm3 on P-Trak. | measurement | p2 Results So Far | February/March2005 ISS cabin and Velcro-debris tests, not ARD combustion or a terrestrial laboratory. | Unknown（來源未提供／尚未核對） |
| SMOKE-3e50d1d643ba-C02 | Plans ARD/nitrogen tests inside a15-liter Mylar bag to assess modified P-Trak accuracy. | future_work | p2 Future DAFT Tests | Proposed Arizona Road Dust with nitrogen,15-L Mylar bag. | Unknown（來源未提供／尚未核對） |
| SMOKE-3e50d1d643ba-C03 | Microgrooved condenser is intended to return isopropanol to the wick without gravitational drainage. | design_or_operations | p1 The Challenge and cross-section photo | Modified P-Trak condensation counter; DustTrak scattering-mass comparator. | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-47"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- {"factor": "source_conditions", "values": {"F1": "February/March2005 ISS cabin and Velcro-debris tests, not ARD combustion or a terrestrial laboratory.", "F2": "Proposed Arizona Road Dust with nitrogen,15-L Mylar bag.", "F3": "Modified P-Trak condensation counter; DustTrak scattering-mass comparator."}, "status": "source_condition_context_not_per_trial_controls", "source_locator": ["pp1-2 complete text and figures"]}


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- No numbered predictive or dynamic mass-balance model.
- P-Trak is the condensation counter; DustTrak is the optical mass monitor.
- Particle-size instrument specification is not measured aerosol PSD.
- Fact-sheet arrival wording February2005 differs from symposium December2004 launch/delivery chronology; preserve editions, do not harmonize silently.
- No named author byline; contact list is not treated as authorship.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

來源尚未提供可核對的項目；不填成 0。
