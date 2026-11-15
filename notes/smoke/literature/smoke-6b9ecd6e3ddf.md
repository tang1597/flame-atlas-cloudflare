# Early Results from the SAME Experiment

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-6b9ecd6e3ddf | preliminary research/status presentation toNASAHeadquarters,withmeasurements,simulationandfuturework | {"source": "OriginallegacyPPT,status11-16-2007;publishedasprogressreport,notfinalpostflightanalysis.", "reading_copy": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\output\\earth_space_transfer_20261114\\phase5_shared_document_review\\role_E\\same\\source_extracts\\EarlyResults2007_deck_reading_copy.pdf", "reading_copy_sha256": "be3f33920213f8972a60adb97f7f9f584b2500356fcc362eb65aa5232b487cac"} | 6b9ecd6e3ddf220fce9b52d6158eca450a920b854b0a9018c62d06b76416aa92 | {"slides": 48, "physical_pdf_pages": 48} | prior_primary_audit_reused_source_bytes_reverified |


- https://psi-curation-prod.s3.amazonaws.com/legacy/Filestreamdb/20464/Same%20progress%20report%20to%20HQ%2011-16-07%20%20%2011%2015%2007%20%20updated.ppt


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/補下載/PSI-102/Presentations/a9bf9e5a0cd96356_PSI-102_Presentations_SAME_EarlyResults.ppt>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-6b9ecd6e3ddf-C01 | 簡報包含初步飛行統計與部分相對 1g 數目比較，早於後續校正分析。此版 Silicone 的平均質量對應直徑 983 nm 仍屬初步值，不應取代最終 2010 年表格或 2018 年比較資料。 | measurement | s40-42 | Slide39 says1g comparisons had started using the engineering/training model. Slide45 still lists1g comparisons,sample mass loss and scattering analysis as further work. | Unknown（來源未提供／尚未核對） |
| SMOKE-6b9ecd6e3ddf-C02 | 作者將老化趨勢解釋為與凝聚及有限壁面損失相容：800 s 內數目下降因子為 1.7–2.7，數目平均直徑約增至 1.5 倍。但未提供固定數值動態定律，也未獨立辨識壁面損失。 | author_interpretation | s43 | Slide43 reports800s,count reduction factors1.7-2.7 and approximately1.5count-mean diameter increase. No numerical kernel,value or governing equation is printed. | Unknown（來源未提供／尚未核對） |
| SMOKE-6b9ecd6e3ddf-C03 | 障礙物、煙霧輸送與警報時間結果來自 CFD 計算，不是實際地面偵測時間的驗證。 | calculation | s14-19 | \["P5S-M4", "P5S-M5"\] | Unknown（來源未提供／尚未核對） |
| SMOKE-6b9ecd6e3ddf-C04 | 在簡報發表時，TEM、質量損失、散射訊號換算及 1g 比較仍列為未完成工作，須保留當時的進度狀態。 | future_work | s45,s48 | Slide39 says1g comparisons had started using the engineering/training model. Slide45 still lists1g comparisons,sample mass loss and scattering analysis as further work. | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-102"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- {"factor": "source_conditions", "values": {"flight": "ISS increment15,September9-October5,2007. Slide39 reports47test runs including repeated DBP cases; samples and TEM grids returned on STS120.", "material_sources": ["silicone rubber", "Teflon", "Kapton", "cellulose lamp wick", "dibutyl phthalate (DBP)"], "ground_status": "Slide39 says1g comparisons had started using the engineering/training model. Slide45 still lists1g comparisons,sample mass loss and scattering analysis as further work.", "aging": "Slide43 reports800s,count reduction factors1.7-2.7 and approximately1.5count-mean diameter increase. No numerical kernel,value or governing equation is printed.", "models": ["P5S-M4", "P5S-M5"]}, "status": "source_condition_context_not_per_trial_controls", "source_locator": ["s1-6date,team,objectives/history", "s11-13CSDpriorresults", "s14-19FDSmodel", "s21-24moments", "s25-28DAFT", "s38-39materials/operations", "s40-43preliminaryresults/aging", "s45-48unfinishedwork/implications"]}


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- A preliminary progress presentation must remain distinct from final analysis.
- The stated15%repeatability does not supply numerical coagulation coefficients or raw calibration data.
- No normal-gravity DBP measurement can be inferred from the material list on slide38.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

來源尚未提供可核對的項目；不填成 0。
