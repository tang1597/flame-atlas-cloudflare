# Detection of Smoke from Microgravity Fires

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-67ede025a6cf | research conference article in legacyWord DOC, not a slide deck | {"source": "Original shared .doc; read-onlyWord export used for physical pagination. Not claimed identical to publisher PDF.", "reading_copy": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\output\\earth_space_transfer_20261114\\phase5_shared_document_review\\role_E\\same\\source_extracts\\Detection2005_paper_reading_copy.pdf", "reading_copy_sha256": "efe0bc83646f61b5e722217dd5978330bc94cf2e3a5e373aa9969f4c0c748615"} | 67ede025a6cf79ac8857172243334d9cb7550565384178a1351cef34edbc2347 | {"physical_pdf_pages": 10} | prior_primary_audit_reused_source_bytes_reverified |


- https://doi.org/10.4271/2005-01-2930
- https://psi.nasa.gov/physci/repo/data/investigations/PSI-102


DOI：10.4271/2005-01-2930

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/第一批下載/PSI-102_SAME/Presentations/PSI-102_Presentations_Detection of Smoke from Microgravity Fires_paper.2005.doc>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-67ede025a6cf-C01 | 地面正常重力比較試驗以飛行樣品的質量損失作匹配；在這組 STS-75 CSD 試驗中，TEM 表格顯示低重力下的固體粒子尺寸較大。其設備與來源形態不同於 SAME，液滴也未留下可解讀的 TEM 粒子。 | measurement | pp5-7,Table2 | Source identifies the STS-75 CSD experiment. Sources are paper, Teflon, Kapton, silicone rubber and candle wax. Kanthal wire heating/ignition lasts15-60s; each event approximately2min. After flight, normal-gravity operating conditions were chosen to match measured flight sample mass loss. | Unknown（來源未提供／尚未核對） |
| SMOKE-67ede025a6cf-C02 | 不同偵煙技術對受測熱裂解氣膠的響應不同。各次試驗的偵測次數只適用於當時的條件與門檻；ISS 偵測器採用飛行標準的 6.6 倍增益，不能換成一般警報失敗機率。 | measurement | pp5-7,Figs6-12,Table3 | Near-field glovebox and far-field detector box connected by Teflon hoses. ISS detector gain was6.6times the flight standard. | Unknown（來源未提供／尚未核對） |
| SMOKE-67ede025a6cf-C03 | 這篇 2005 年文章把 SAME 矩方法與設備列為後續研究計畫，當時尚非已完成的 SAME 實驗結果。 | future_work | pp7-9 | \["P5S-M1", "P5S-M3"\] | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-102"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- {"factor": "source_conditions", "values": {"CSD": "Source identifies the STS-75 CSD experiment. Sources are paper, Teflon, Kapton, silicone rubber and candle wax. Kanthal wire heating/ignition lasts15-60s; each event approximately2min. After flight, normal-gravity operating conditions were chosen to match measured flight sample mass loss.", "hardware": "Near-field glovebox and far-field detector box connected by Teflon hoses. ISS detector gain was6.6times the flight standard.", "material_caveat": "Kapton wire may include Kapton/Teflon layers; paper pyrolysis is not automatically the SAME cotton lamp wick. Silicone formulation and Teflon coloring agents are unknown.", "DAFT": "Four early ISS2005tests:three ambient-air samples and one Velcro challenge, not calibration dust or fire-smoke equivalence.", "models": ["P5S-M1", "P5S-M3"]}, "status": "source_condition_context_not_per_trial_controls", "source_locator": ["p1 title/abstract", "pp3-6 CSD materials,apparatus,procedure and ground/flight traces", "p7 Tables2-3 and limitations", "p8 Eqs1-7", "pp9-10 DAFT2005results,conclusion,bibliography"]}


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- Actual research article stored in a Presentations folder; folder category does not determine document type.
- Earlier moment/lognormal equations contain literal typesetting issues; seeP5S-M1.
- Ground raw signals and complete matched thermal/flow histories were not acquired.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

來源尚未提供可核對的項目；不填成 0。
