# “SMOKE:” Characterization of Smoke Particulate for Spacecraft Fire Detection

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-36c89dea3ec8 | primary laboratory experimental article | Original primary PDF, linked NASA/NIST edition; exact physical locators retained in candidate. | 36c89dea3ec89b61abb10d21b7549a8784bd28daf12b1ee8bf144854823e1c8f | {"physical_pdf_pages": 4} | prior_primary_audit_reused_source_bytes_reverified |


- https://ntrs.nasa.gov/api/citations/20040053578/downloads/20040053578.pdf
- https://ntrs.nasa.gov/citations/20040053578


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/02_會議論文與預印本/Smoke_ Characterization of Smoke Particulate for Spacecraft Fire Detection__36c89dea3e.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-36c89dea3ec8-C01 | 此來源取得實際地面量測；由來源推導／預測的量與儀器實測輸出須分開。它是相關材料及校正的參考，尚不能視為 SAME／DAFT 的精確跨情境驗證。 | measurement | Primary2003PDFphysicalp3printed271Table1;visuallyverified | P5S-G2-preSAME-cotton-wick | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-101", "PSI-102"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- {"factor": "source_conditions", "values": {"material": ["cottonwick", "polyurethanefoam", "wood", "cornoil", "toast"], "protocol": "CPCzerothmoment,MICfirstmoment,TEOMthirdmoment,cascadeimpactor;aerodynamicconversionassumesunitdensitysphericalparticles.Exactsourcegrade/heatinghistorynotprovided.", "pressure": null, "oxygen_fraction": null, "source_candidate": "P5S-G2-preSAME-cotton-wick"}, "status": "source_condition_context_not_per_trial_controls", "source_locator": ["Primary2003PDFphysicalp3printed271Table1;visuallyverified"]}


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- CottonwickisrelatedtoSAMEcelluloselampwick;exactfabric/finish/heatingisnotmatched.
- PUfoamisnotautomaticallyPyrellwithitsfire-retardantformulation.
- 2005decklabelsdiametermm;primary2003articlelabelsµm.Numericalvaluesnotmultipliedorconvertedfromthefaultydecklabel.
- Toastinvalidmomentcaseisretained;notzero-filled.
- MomentderivedparametersandpredictedMMADareseparatefromimpactor-measuredMMAD.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

來源尚未提供可核對的項目；不填成 0。
