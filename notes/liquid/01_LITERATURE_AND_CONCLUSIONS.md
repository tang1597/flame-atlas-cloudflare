# 文獻、來源結論與資料重用

詳讀強度逐卡保留：本機選頁/全頁、只有封面、作者原稿、出版社摘要/圖說、索引內容、未取得全文。書目出現不代表全文已審；Presentations資料夾也不保證是投影片。

## 可搜尋的來源結論ID

FLEX使用source_id:Cnn作本文件的來源綁定摘要標記，不是原文逐字引句、原作者編號或試次ID。CFI沿用已審讀的CC01–CC10。所有中文敘述均為有界摘要。

| 結論ID | 來源支持的結論／角色 | 原頁與適用界線 |
|---|---|---|
| FLEX-TP2015:C01 | ActualD0在igniter ON定義；visible extinction diameter是剩餘液滴直徑。 | physicalp25 AppendixA.1；出FOV值可外插，不能當火焰包絡。 |
| FLEX-ISS2014:C01 | D由等面積圓定義；Df受UV/color頻段及邊界判讀影響。 | physicalp4；同campaign overview不增加獨立樣本。 |
| FLEX-MEOH2013:C01 | He/CO2氣氛改變甲醇液滴回縮；run110/263的D0也不同。 | physicalpp5–6 Fig2；不是完美matched滅火劑排名。 |
| FLEX-MEOH2013:C02 | 準穩態K未含水吸收/蒸發歷程；AEA-2 Cp調高60%屬模型修改。 | physicalpp6,9–10；不是Cp量測或盲驗證。 |
| FLEX-WATER2012:C01 | ISS與ZGF呈現水/光學訊號問題，但氣體、大小和支撐不同。 | slides7,9–14；ZGF非1g，slide9/10組成與K單位矛盾保留。 |
| FLEX-COOL2013:C01 | 作者模型捕捉兩階段趨勢，但第二階段K偏高、終端液滴D偏小。 | physicalp5；D0=3.91mm不足以完成raw試次聯結。 |
| FLEX-ALKANE-D0-2013:C01 | 纖維效應隨尺寸變化；局部近似不能延伸成所有free/fiber等效。 | physicalp9 Fig13/p10；地面臂為1.2s drop，非1g。 |
| FLEX2-PRF2020:C01 | 實驗D/radiance與計算T/K在不同panel；模型沒有soot formation。 | physicalpp4–5/Fig3；298K是模型遠場輸入，非量測液體初溫。 |
| FLEX2-PRF2020:C02 | PRF50為等體積配方；大滴可有hot→cool的局部來源行為。 | physicalpp7–9；不是池火/噴霧/所有燃料普遍轉換律。 |
| FLEX-OPTICAL2014:C01 | 邊界、繞射、背景及圓擬合影響液滴D推定。 | physicalpp4–9，Eqs6–7p8；屬量測處理，不是新燃燒trial。 |
| FLEX-SOOT2025-REMOTE:C01 | 作者報告先前heptane煙炱反演低估factor2；發光衰減與cool轉換需分開。 | 出版社indexed Abstract；直接全文403，無本機SHA/實體頁/exact run crosswalk。 |
| CC01 | Visible hot-flame disappearance, liquid consumption, low-temperature burning and radiance are distinct; a single image channel cannot establish complete oxidation.；角色 observation | CFI-REPORT2020, CFI-DIETRICH2024；原頁見來源卡。 |
| CC02 | High-pressure warm/reignition behavior must retain specific fuel, atmosphere and stage definitions.；角色 author_conclusion | CFI-DIETRICH2024, PSI117-THREEDECK2018；原頁見來源卡。 |
| CC03 | Isolated droplets do not establish pool/spray/mist suppression, cabin-material ignition or operational safety thresholds.；角色 physical_inference | CFI-REPORT2020；原頁見來源卡。 |
| CC04 | Archived author-model series permit published-model replay, not a newly executed or independently validated model.；角色 provenance | PSI117-METADATA, PSI117-EXT2023, PSI117-OSC2019；原頁見來源卡。 |
| CC05 | Source-calibrated coefficients/property closures cannot be presented as independent same-data predictions.；角色 source_calibration | FLEX-NAYAGAM2012, CFI-DODECANE-KINETICS2020, FLEX-PROPERTIES2020；原頁見來源卡。 |
| CC06 | NTC midpoint and boiling temperature have different roles; molar versus mass properties require consistent conversion.；角色 unit_audit | CFI-ASPECTS2015, PSI117-EXTDECK2022；原頁見來源卡。 |
| CC07 | Heptane chemistry plus dodecane properties does not establish dodecane kinetics.；角色 author_conclusion | CFI-DODECANE-KINETICS2020；原頁見來源卡。 |
| CC08 | Umbrella OpenFOAM metadata does not identify explicitly one-dimensional earlier solver/configurations.；角色 provenance | PSI117-METADATA, PSI117-OSC2019；原頁見來源卡。 |
| CC09 | ReadMe lacks exact FLEX test IDs and source descriptions differ; no row-aligned exact-test score is justified.；角色 comparison_limit | CFI-REPORT2020, PSI117-THREEDECK2018, PSI117-THREE2019；原頁見來源卡。 |
| CC10 | The3atm experimental cool-extinction zero denotes no finite endpoint after completion, while archived model value.03 remains separate.；角色 endpoint_semantics | PSI117-EXTDECK2022；原頁見來源卡。 |

## FLEX/FLEX2文件卡

Metadata99條形成61個查找群組；20份包內非rawPDF/Office逐SHA盤點。下表16份詳細卡不表示其餘群組或20檔都已全文審讀。

| source ID | 文件／官方位置 | 年份與文類 | 審讀範圍 |
|---|---|---|---|
| FLEX-TP2015 | [Detailed Results From the Flame Extinguishment Experiment (FLEX) March 2009 to December 2011](https://ntrs.nasa.gov/citations/20150023456) | 2015；NASA Technical Publication NASA/TP-2015-216046 | selected original pages; source SHA verified；11,25,29,34,35,160,307 |
| FLEX-ISS2014 | [Droplet Combustion Experiments Aboard the International Space Station](https://doi.org/10.1007/s12217-014-9372-2) | 2014；published journal article | selected original pages; source SHA verified；1,2,4,6,9,10 |
| FLEX-MEOH2013 | [Methanol Droplet Combustion in Oxygen-Inert Environments in Microgravity](https://ntrs.nasa.gov/citations/20130014061) | 2013；8th US National Combustion Meeting conference paper 070HE-0303 | selected original pages; source SHA verified；1,5,6,7,9,10 |
| FLEX-MEOH2011-2012 | [Methanol Droplet Extinction in Oxygen/Carbon-dioxide/Nitrogen Mixtures in Microgravity: Results from the International Space Station Experiments](https://ntrs.nasa.gov/citations/20120016855) | unknown；conference manuscript; date/edition discrepancy | official NASA abstract + limited original pages; PDF character encoding prevents reliable equation transcription；1,2 |
| FLEX-WATER2012 | [Dynamics of Water Absorption and Evaporation During Methanol Droplet Combustion in Microgravity](https://ntrs.nasa.gov/citations/20130010979) | 2012；15-slide conference presentation | SHA-bound selected-page/legacy-PPT audit reused from specified prior receipt; not new full-document read；3,4,7,9,10,11,12,13,14,15 |
| FLEX-COOL2013 | Isolated Alkane Droplet Combustion in Microgravity: “Cool Flames” | 2013；13-page full conference manuscript,not a slide deck | SHA-bound selected-page/legacy-PPT audit reused from specified prior receipt; not new full-document read；1,3,4,5,6,9,10,11,12,13 |
| FLEX-ALKANE-D0-2013 | Effect of Varying the Initial Diameter of n-Octane and n-Decane Droplets over a Wide Range on the Spherically Symmetric Combustion Process: International Space Station and Ground-based Experiments | 2013；10-page full conference experimental manuscript,not a slide deck | SHA-bound selected-page/legacy-PPT audit reused from specified prior receipt; not new full-document read；2,3,4,6,7,9,10 |
| FLEX2-HARDWARE | FLEX-2 Hardware Presentation | unknown；legacy binary PowerPoint engineering/hardware overview | SHA-bound selected-page/legacy-PPT audit reused from specified prior receipt; not new full-document read；無實體PDF頁 |
| FLEX-TESTPLAN2005 | FLEX Test Plan: excerpt from Research Requirements Document | 2005；15-page excerpted test plan from an earlier research requirements document | SHA-bound selected-page/legacy-PPT audit reused from specified prior receipt; not new full-document read；1,2,3,4,5,6,7,8,9,10,11,12,13,15 |
| FLEX2-PRF2020 | [Initial diameter effects on combustion of unsupported equi-volume n-heptane/iso-octane mixture droplets and the transition to cool flame behavior: Experimental observations and detailed numerical modeling](https://doi.org/10.1016/j.combustflame.2020.06.012) | 2020；published journal article; Combustion and Flame220:82–91 | selected original pages; source SHA verified；1,2,3,4,5,7,8,9 |
| FLEX-OPTICAL2014 | [Interpretation of Backlit Droplet Images from ISS Droplet Combustion Experiments](https://doi.org/10.2478/gsr-2014-0007) | 2014；published journal article; Gravitational and Space Research2(1) | selected original pages; source SHA verified；1,4,5,7,8,9 |
| FLEX-COOL-SLIDES2013 | “Cool Flames” in Space, a Hot Prospect on Earth! Anomalous combustion of alkane fuel droplets in space | 2013；24-slide ISS R&D conference presentation | selected original pages; source SHA verified；7,8,9,14,15,16,17,18,20,21,22,23 |
| FLEX2-SRD2010 | Science Requirements Document: Fundamental Studies in Droplet Combustion and Flame Extinguishment in Microgravity (FLEX-2) | 2010；Science Requirements Document Rev1,15March2010;68physicalpages | selected original pages; source SHA verified；1,9,10,11,12,13,14,15,16,43,44 |
| FLEX-DOD | FLEX Description of Data | unknown；DOCX data-organization description; no PDF physical pages | All nonempty text paragraphs of short DOCX read; no fabricated PDF pages；無實體PDF頁 |
| FLEX2-DOD | FLEX-2 Description of Data | unknown；DOCX data-organization description; no PDF physical pages | All nonempty text paragraphs of short DOCX read; no fabricated PDF pages；無實體PDF頁 |
| FLEX-SOOT2025-REMOTE | [Influence of Droplet Size and Fuel Composition on Sooting Behavior in Microgravity Droplet Combustion](https://www.tandfonline.com/doi/full/10.1080/00102202.2025.2595114) | 2025；original journal article; publisher-indexed abstract/method excerpts only | Primary publisher indexed excerpts verified; direct full-page request HTTP403; no acquired fulltext/PDF; no assigned physical page；無實體PDF頁 |

## CFI與相關模型文件卡

23卡包含science report、簡報、期刊/會議版、metadata及只讀封面的規劃文件。2024期刊目前僅publisher abstract、data availability及公開圖說，不能拿別版原稿或slides充作已取得該期刊全文。

| source ID | 文件／官方位置 | 審讀狀態 | 原頁／結論 |
|---|---|---|---|
| CFI-PSI39 | [Cool Flames Investigation (CFI)](https://psi.nasa.gov/physci/repo/data/investigations/PSI-39) | primary_abstract_or_metadata_reviewed_fulltext_not_obtained | ； |
| CFI-REPORT2020 | [Cool Flame Investigation (CFI): Science Final Report](https://psi.ndc.nasa.gov/mpglobal/api/athena/file/9919378/?inline=1&log=1) | all_13_physical_pages_text_reviewed | 1,3,4,6,7,8,9,10,11,12,13；CC01,CC03,CC09 |
| CFI-DIETRICH2024 | [Low Temperature n-Dodecane Droplet Combustion Experiments Aboard the International Space Station](https://link.springer.com/article/10.1007/s12217-024-10115-x) | publisher_abstract_data_availability_and_public_figure_captions_reviewed_fulltext_not_obtained | ；CC01,CC02 |
| FLEX-NAYAGAM2012 | [Can cool flames support quasi-steady alkane droplet burning?](https://www.sciencedirect.com/science/article/abs/pii/S0010218012002131) | primary_abstract_or_metadata_reviewed_fulltext_not_obtained | ；CC05 |
| FLEX-EXTCONF2014 | [Cool-flame extinction during n-alkane droplet combustion in microgravity](https://ntrs.nasa.gov/api/citations/20140006750/downloads/20140006750.pdf) | all_9_physical_pages_text_reviewed | 1,3,7,8,9； |
| FLEX-EXTJOURNAL2015 | [Cool-flame extinction during n-alkane droplet combustion in microgravity](https://www.sciencedirect.com/science/article/pii/S0010218015000152) | primary_abstract_or_metadata_reviewed_fulltext_not_obtained | ； |
| CFI-ASPECTS2015 | [Aspects of Cool-Flame Supported Droplet Combustion in Microgravity](https://ntrs.nasa.gov/api/citations/20160000344/downloads/20160000344.pdf) | 20_slide_text_review_and_p13_equation_visually_verified | 1,4,9,13,14,15,16,17；CC06 |
| CFI-HOTPROSPECT2013 | [Cool Flames in Space, a Hot Prospect on Earth!](https://www.nasa.gov/wp-content/uploads/2013/10/issrdc_2013-07-16-0945_nayagam2013.pdf) | title_page_2013_ISSRDC_identity_only | 1； |
| CFI-SCR2014 | [Cool Flames Investigation: Science Concept Review](https://psi.ndc.nasa.gov/mpglobal/api/athena/file/12716385/?inline=1&log=1) | title_page_only_not_outcome_review | 1； |
| CFI-SRD2014 | [Cool Flames Investigation: Science Requirements Document](https://psi.ndc.nasa.gov/mpglobal/api/athena/file/12700041/?inline=1&log=1) | title_page_only_not_outcome_review | 1； |
| CFI-DODECANE-KINETICS2020 | [Cool-flame dodecane-droplet extinction diameters](https://par.nsf.gov/servlets/purl/10176660) | 3page_NSF_primary_text_reviewed_no_local_payload | 1,2,3；CC05,CC07 |
| FLEX-PROPERTIES2020 | [Effects of ambient inert gas properties on cool-flame droplet combustion](https://ntrs.nasa.gov/api/citations/20205008449/downloads/Effects%20of%20ambient%20inert%20gas%20properties%20-Combustion%20Science-Nayagam-FAW.pdf) | 10page_remote_primary_PDF_text_reviewed | 6,8,9；CC05 |
| PSI117-METADATA | [Effect of External Thermo-Convective Perturbation on Cool Flame Dynamics: A Multidimensional Multi-Physics CFD Analysis](https://psi.nasa.gov/physci/repo/data/investigations/PSI-117) | primary_abstract_or_metadata_reviewed_fulltext_not_obtained | ；CC04,CC08 |
| PSI117-OSC2019 | [Oscillatory cool flame combustion behavior of submillimeter sized n-alkane droplet under near limit conditions](https://www.sciencedirect.com/science/article/abs/pii/S1540748918301573) | primary_abstract_or_metadata_reviewed_fulltext_not_obtained | ；CC04,CC08 |
| PSI117-THREE2019 | [Three stage cool flame droplet burning behavior of n-alkane droplets at elevated pressure conditions: Hot, warm and cool flame](https://www.sciencedirect.com/science/article/abs/pii/S1540748918306205) | primary_abstract_or_metadata_reviewed_fulltext_not_obtained | ；CC09 |
| PSI117-THREE-NTRS | [Three Stage Cool Flame Droplet Burning Behavior of n-Alkane Droplets at Elevated Pressure Conditions: Hot, Warm and Cool Flame](https://ntrs.nasa.gov/api/citations/20190002838/downloads/20190002838.pdf) | NASA_metadata_abstract_reviewed_direct_payload403 | ； |
| PSI117-EXT2023 | [Extinction characteristics of isolated n-alkane fuel droplets during low temperature cool flame burning in air](https://www.sciencedirect.com/science/article/abs/pii/S1540748922001134) | primary_abstract_or_metadata_reviewed_fulltext_not_obtained | ；CC04 |
| PSI117-EXTDECK2022 | [Extinction characteristics of isolated n-alkane fuel droplets during low temperature cool flame droplet burning in air](https://psi.nasa.gov/physci/repo/data/investigations/PSI-117) | 18slide_text_and_p9_p15_axes_visually_verified | 1,2,7,8,9,11,15,16；CC06,CC10 |
| PSI117-OSCDECK2018 | [Oscillatory Cool Flame Combustion Behavior of Submillimeter Sized n-Alkane Droplet under Near Limit Conditions](https://psi.nasa.gov/physci/repo/data/investigations/PSI-117) | 19slide_text_reviewed_ALE_equation_glyphs_incomplete | 1,4,5,6,13,17,18,19； |
| PSI117-THREEDECK2018 | [Three Stage Cool Flame Droplet Burning Behavior of n-Alkane Droplets at Elevated Pressure Conditions: Hot, Warm and Cool Flame](https://psi.nasa.gov/physci/repo/data/investigations/PSI-117) | 22slide_text_reviewed | 1,7,8,9,10,15,16,21,22；CC02,CC09 |
| PSI117-SEMINAR2026 | [Cool Flames in Space](https://psi.nasa.gov/physci/repo/data/investigations/PSI-117) | bounded_36slide_text_review | 1,8,9,21,25,31； |
| SCOPE-FLEX2 | [Flame Extinguishment Experiment (FLEX / FLEX-2)](https://www.nasa.gov/wp-content/uploads/2025/07/flame-extinguishment-experiment-flex.pdf) | primary_abstract_or_metadata_reviewed_fulltext_not_obtained | ； |
| SCOPE-CFIG | [Cool Flames Investigation with Gases (CFI-G)](https://psi.nasa.gov/physci/repo/data/investigations/PSI-159) | primary_abstract_or_metadata_reviewed_fulltext_not_obtained | ； |

## 同一資料、部分重疊、同族與未知

| 關係 | 已核例子 | 可說／不可說 |
|---|---|---|
| exact artifact | FLEX2015 report下載別名同SHA；Water2012 deck別名同SHA | 同文件一份，不是額外重複實驗。不同SHA僅同title不自動等版。 |
| exact ID reference | PRF2020 Table2十operation ID在PSI68檔名精確出現 | 可追原檔名；尚未完整聯結每個as-run設定、影像與校準。 |
| partial series | Test002完整D²664點中C57:C198/F57:F198為142frame窗 | 同burn子窗，不是142獨立burn；workbook/摘要K版本都保留。 |
| campaign/family | 甲醇2011/2013、水吸收slides、2014overview、2015report；CFI2020report/2024paper | 同活動/主題可能重用部分資料，逐圖點run crosswalk未完成時不稱exact共享列。 |
| related edition | extinction2014conference/2015journal/2015Aspects；ThreeStage2018conference/slides/2019journal | 分版引用；R377/FLEX1268條件差異保留，不拿一版替另一版補值。 |
| comparative, not matched | ThreeStage C12 ISS觀測對C7來源模型 | 可作機制比較，不給exact-test誤差或稱C12獨立驗證。 |
| unknown | PSI117 ReadMe圖號對每個CSV點的原FLEX/CFI ID | 缺exact trial IDs，不逐列配對，不憑D0/燃料相同補ID。 |

## 覆蓋與缺件

- 論文、報告、簡報/會議稿、規格及資料說明均進ledger；未驗證的poster沒有稱為已詳讀。
- 同資料多篇論文可提出不同機制解釋，不會增加n；理論/影像算法也不是新flight campaign。
- 2025煙炱直接fetch403；其餘未取全文狀態逐來源保留，沒有用非原始鏡站繞過。
- CFI舊canonical227列與現standardized226列尚未調和，不默併同分母。
- 路徑、SHA、DOI/NTRS、圖/原頁、條件與未知：[FLEX/FLEX2 JSON](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/flex_flex2_literature.json>)；[CFI/PSI117 JSON](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/cfi_literature.json>)。
