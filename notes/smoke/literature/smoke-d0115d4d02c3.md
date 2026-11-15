# Dust and Aerosol measurement Feasibility Test (DAFT), Joint NASA/ESA Increment13 Science Symposium

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-d0115d4d02c3 | Research progress presentation with measurements, design diagrams and planned operations | Slide1 date22March2006. Local read-only PowerPoint PDF export used for slide inspection; original shared PPT unchanged. | d0115d4d02c37032851200c84a6f524cbb4555ecaad338f1927b0276628c8a06 | 17 | prior_primary_audit_reused_source_bytes_reverified |


- https://psi.nasa.gov/physci/repo/data/investigations/PSI-47


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/第一批下載/PSI-47_DAFT _ DAFT-2/Presentations/PSI-47_Presentations_DAFT_Increment13SciSymposium_2006.ppt>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-d0115d4d02c3-C01 | 早期 ISS 艙內空氣與分離魔鬼氈的量測顯示儀器有響應，但準確度仍須靠計畫中的已知氣膠比較確認。此處的實驗室指 ISS 美國實驗艙，不是地面正常重力試驗。 | measurement | slides6,8,9; limitation slide10 | ISS operations22February/4March2005; cabin air and manually separated Velcro. | Unknown（來源未提供／尚未核對） |
| SMOKE-d0115d4d02c3-C02 | 簡報列出 STS-32 與住家、辦公室、實驗室依粒徑分級的質量濃度比較表；這是環境背景比較，不是 ARD 來源匹配的氣膠袋試驗，表格確切出處與原始地面採樣方法仍未確認。 | measurement | slide7 table | {"table_units": "microgram/m3", "terrestrial_named_environment_totals": {"Home": 8.5, "Office": 11.2, "Laboratory": 12.1}, "source_dust_composition": null, "ground_method": null, "attribution": "Liu1991 is a plausible trace through spacecraft aerosol literature; deck slide7 has no explicit bibliographic caption, so exact table provenance remains unconfirmed."} | Unknown（來源未提供／尚未核對） |
| SMOKE-d0115d4d02c3-C03 | 改裝冷凝器具有 60 道、各深 0.009 inch 的溝槽，作者以毛細作用說明異丙醇回流。僅有幾何尺寸仍不足以決定回流速率，尚缺接觸角、溫度、液量及壓力歷程。 | design_or_operations | slides3-4 | Commercial P-Trak condenser modification; working fluid is isopropanol. | Unknown（來源未提供／尚未核對） |
| SMOKE-d0115d4d02c3-C04 | 簡報規劃以氮氣與 ARD（Fine）經支架產生氣膠並收集於 15 L 袋中。這是灰塵校正計畫，不是火煙試驗，也不能證明 2006 年 8 月的在軌試驗當時已完成。 | future_work | slides5,11-16 | Calibration ARD(Fine), not fire smoke; N2 carrier;15-L bag. | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-47"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- {"factor": "source_conditions", "values": {"S1": "ISS operations22February/4March2005; cabin air and manually separated Velcro.", "S2": {"table_units": "microgram/m3", "terrestrial_named_environment_totals": {"Home": 8.5, "Office": 11.2, "Laboratory": 12.1}, "source_dust_composition": null, "ground_method": null, "attribution": "Liu1991 is a plausible trace through spacecraft aerosol literature; deck slide7 has no explicit bibliographic caption, so exact table provenance remains unconfirmed."}, "S3": "Commercial P-Trak condenser modification; working fluid is isopropanol.", "S4": "Calibration ARD(Fine), not fire smoke; N2 carrier;15-L bag."}, "status": "source_condition_context_not_per_trial_controls", "source_locator": ["all17slides text", "slides3-10 complete figures and tables", "slides11-16 hardware/operation layouts"]}


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- No author byline; contacts include David Urban,Gary Ruff,William Sheredy,Greg Funk.
- No independently predictive bag mass/count or particle-loss equation.
- Nominal operation is not a complete accuracy validation.
- Indoor table does not identify same chemical composition as ARD.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

來源尚未提供可核對的項目；不填成 0。
