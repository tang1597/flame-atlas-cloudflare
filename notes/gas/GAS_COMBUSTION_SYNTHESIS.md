# 氣體火焰跨資料集結論與消防洞見

先確認數據與observable，再比較同源或相近機制。策略／產品構想均另列驗證需求，不把數據端點當艙室安全認證。

## GAS-I01　同燃料也沒有通用的安全焰長

SPICE具體兩條件對照顯示，同燃料、同噴口與同日的煙點發光長度仍隨共流條件不同。燃料流率是各自調到煙點，不能解作固定熱功率下的火焰變長。 具體例：同日丙烷、1.6002mm噴口的兩個已核煙點，Uco約22.288→44.853cm/s，Lsp約45.523→71.384mm，增約56.81%；這不是重複試驗信賴區間。

- 組合資料：[JET-SPICE-C3H6-050-N2-050-D1P6002-COFLOW](datasets/JET-SPICE-C3H6-050-N2-050-D1P6002-COFLOW.md), [JET-SPICE-C3H6-075-N2-025-D0P762-COFLOW](datasets/JET-SPICE-C3H6-075-N2-025-D0P762-COFLOW.md), [JET-SPICE-C3H6-075-N2-025-D1P6002-COFLOW](datasets/JET-SPICE-C3H6-075-N2-025-D1P6002-COFLOW.md), [JET-SPICE-C2H4-100-D0P762-COFLOW](datasets/JET-SPICE-C2H4-100-D0P762-COFLOW.md), [JET-SPICE-C2H4-100-D1P6002-COFLOW](datasets/JET-SPICE-C2H4-100-D1P6002-COFLOW.md), [JET-SPICE-C3H8-100-D0P762-COFLOW](datasets/JET-SPICE-C3H8-100-D0P762-COFLOW.md), [JET-SPICE-C3H8-100-D1P6002-COFLOW](datasets/JET-SPICE-C3H8-100-D1P6002-COFLOW.md), [JET-SPICE-C3H6-100-D0P4064-COFLOW](datasets/JET-SPICE-C3H6-100-D0P4064-COFLOW.md), [JET-SPICE-C3H6-100-D0P762-COFLOW](datasets/JET-SPICE-C3H6-100-D0P762-COFLOW.md), [JET-SPICE-C3H6-100-D1P6002-COFLOW](datasets/JET-SPICE-C3H6-100-D1P6002-COFLOW.md)
- 結論定位：尚未取得／不適用
- 共同處：文獻、原工作簿與本次固定係數比較都保留燃料、噴口與流動對煙點端點的關係。
- 差異／適用條件：4個配對比較沒有重複試驗信賴區間；這些是兩條件算術差，不是隔離所有混雜的因果估計。
- 新增消防洞見：預防／偵測工具同時標出流況與端點；用熱流與煙生成真值測試新監測判據，避免一條焰長規則跨所有工況。
- 證據身份：有範圍的來源比較／固定原式與數據診斷；新策略須另測，非產品效能或完整安全認證
- 判別試驗：補相同供料策略、局部熱流、煙粒／警報與鄰材點燃；現有資料不給安全距離。

## GAS-I02　流量降低與增加可能走向不同的熄滅機制

指定s-Flame乙烯/N2源系列兩端皆有熄滅，而FD也區分小型長時火焰、成長與輻射熄滅。不能將單一旋鈕的方向當作所有氣體火源的單調安全指標。

- 組合資料：[FD-NORMAL-C2H4-fixed](datasets/FD-NORMAL-C2H4-fixed.md), [FD-NORMAL-C2H4-ramped](datasets/FD-NORMAL-C2H4-ramped.md), [FD-NORMAL-C3H8-fixed](datasets/FD-NORMAL-C3H8-fixed.md), [FD-INVERSE-C2H4-fixed](datasets/FD-INVERSE-C2H4-fixed.md), [FD-INVERSE-C2H4-ramped](datasets/FD-INVERSE-C2H4-ramped.md), [SF-C2H4-N2](datasets/SF-C2H4-N2.md), [SF-CH4-N2](datasets/SF-CH4-N2.md), [SF-H2-N2](datasets/SF-H2-N2.md), [SF-H2_CH4-N2](datasets/SF-H2_CH4-N2.md), [SF-H2_CH4-He](datasets/SF-H2_CH4-He.md), [SF-H2-He](datasets/SF-H2-He.md), [SF-CH4-He](datasets/SF-CH4-He.md), [SF-C2H4-He](datasets/SF-C2H4-He.md)
- 結論定位：SF-F01；SF-F02；FD-F01
- 共同處：來源均要求保留成分、幾何、熱歷史與操作端點。
- 差異／適用條件：球形火焰、氣體盤及共流噴口的閉合不同；有些端點是時間或燃燒器溫度限制。
- 新增消防洞見：抑制研究先辨識反應／傳輸／輻射限制，再以可觀測狀態回饋測試介入。
- 證據身份：有範圍的來源比較／固定原式與數據診斷；新策略須另測，非產品效能或完整安全認證
- 判別試驗：同火源的流量介入、局部流場、反應真值與再燃；不產生通用風扇關閉閾值。

## GAS-I03　可見熄焰、燃料終止與反應終止要分開

CFI-G特定butane組的熱焰／冷焰紀錄，與BRE自然熄滅／供料終止的不同標記，共同要求分開操作命令、可見火焰與反應狀態。

- 組合資料：[BRE-AUX-ETHYLENE-DISK25-ISS](datasets/BRE-AUX-ETHYLENE-DISK25-ISS.md), [BRE-AUX-ETHYLENE-DISK50-ISS](datasets/BRE-AUX-ETHYLENE-DISK50-ISS.md), [BRE-AUX-METHANE-DISK25-ISS](datasets/BRE-AUX-METHANE-DISK25-ISS.md), [CFIG-NORMAL-ethane](datasets/CFIG-NORMAL-ethane.md), [CFIG-NORMAL-50_butane](datasets/CFIG-NORMAL-50_butane.md), [CFIG-NORMAL-propane](datasets/CFIG-NORMAL-propane.md), [CFIG-NORMAL-30_butane](datasets/CFIG-NORMAL-30_butane.md), [CFIG-NORMAL-30_propane](datasets/CFIG-NORMAL-30_propane.md), [CFIG-NORMAL-30_ethane](datasets/CFIG-NORMAL-30_ethane.md), [CFIG-INVERSE-ethane](datasets/CFIG-INVERSE-ethane.md), [CFIG-INVERSE-propane](datasets/CFIG-INVERSE-propane.md), [CFIG-INVERSE-butane](datasets/CFIG-INVERSE-butane.md)
- 結論定位：CG-F01；CG-F02；BRE-F03
- 共同處：來源端點分類比單一可見焰圖更能表達介入後狀態。
- 差異／適用條件：CFI-G冷焰未證實存在於每種燃料或壓力；BRE命令資料不是已對時的零流量／零反應真值。
- 新增消防洞見：設計介入後的熱／物種／光學確認流程，再評估偵測或解除監測條件。
- 證據身份：有範圍的來源比較／固定原式與數據診斷；新策略須另測，非產品效能或完整安全認證
- 判別試驗：匹配試次、階段、可靠時間及獨立反應訊號；目前沒有通用等待時間與安全解除值。

## GAS-I04　soot場、煙點與警報輸出不能互相替代

光學反算的soot／溫度場、SPICE煙點與警報響應是不同observable；成分、空間分布及輸運會影響能看到什麼。

- 組合資料：[CLD-CH4-original_coflow](datasets/CLD-CH4-original_coflow.md), [CLD-C2H4-original_coflow](datasets/CLD-C2H4-original_coflow.md), [CLD-C2H4-improved_coflow2021](datasets/CLD-C2H4-improved_coflow2021.md), [CLD-CH4-improved_coflow2021](datasets/CLD-CH4-improved_coflow2021.md)
- 結論定位：CLD-F01；CLD-F02
- 共同處：不同來源可協助選偵測器的挑戰煙源與流況。
- 差異／適用條件：共享甲烷／乙烯或共流硬體，不代表是同一火焰、同一煙粒來源或共同感測器試驗。
- 新增消防洞見：建立多區域／多訊號的研究挑戰庫，將煙生成與送達感測器分開。
- 證據身份：有範圍的來源比較／固定原式與數據診斷；新策略須另測，非產品效能或完整安全認證
- 判別試驗：同煙源粒徑／濃度、取樣與啟用警報真值；不能由焰長或soot反演直接算漏報率。

## GAS-I05　相同氧百分比必須先對流股

瓶內成分、實際送出混合物、氧化劑流與艙內氣氛不同；normal／inverse也不是正常／微重力。

- 組合資料：[FD-NORMAL-C2H4-fixed](datasets/FD-NORMAL-C2H4-fixed.md), [FD-NORMAL-C2H4-ramped](datasets/FD-NORMAL-C2H4-ramped.md), [FD-NORMAL-C3H8-fixed](datasets/FD-NORMAL-C3H8-fixed.md), [FD-INVERSE-C2H4-fixed](datasets/FD-INVERSE-C2H4-fixed.md), [FD-INVERSE-C2H4-ramped](datasets/FD-INVERSE-C2H4-ramped.md), [SF-C2H4-N2](datasets/SF-C2H4-N2.md), [SF-CH4-N2](datasets/SF-CH4-N2.md), [SF-H2-N2](datasets/SF-H2-N2.md), [SF-H2_CH4-N2](datasets/SF-H2_CH4-N2.md), [SF-H2_CH4-He](datasets/SF-H2_CH4-He.md), [SF-H2-He](datasets/SF-H2-He.md), [SF-CH4-He](datasets/SF-CH4-He.md), [SF-C2H4-He](datasets/SF-C2H4-He.md), [CFIG-NORMAL-ethane](datasets/CFIG-NORMAL-ethane.md), [CFIG-NORMAL-50_butane](datasets/CFIG-NORMAL-50_butane.md), [CFIG-NORMAL-propane](datasets/CFIG-NORMAL-propane.md), [CFIG-NORMAL-30_butane](datasets/CFIG-NORMAL-30_butane.md), [CFIG-NORMAL-30_propane](datasets/CFIG-NORMAL-30_propane.md), [CFIG-NORMAL-30_ethane](datasets/CFIG-NORMAL-30_ethane.md), [CFIG-INVERSE-ethane](datasets/CFIG-INVERSE-ethane.md), [CFIG-INVERSE-propane](datasets/CFIG-INVERSE-propane.md), [CFIG-INVERSE-butane](datasets/CFIG-INVERSE-butane.md)
- 結論定位：FD-F03；CG-F03；SF-F03
- 共同處：來源要求以完整反應物角色與基準表達氧／燃料條件。
- 差異／適用條件：Tad／Zst是計算描述量，不是實測燃燒器、焰溫或局部氧場。
- 新增消防洞見：環境搜尋先確認哪一股氣體與哪個位置，再排序最像實驗，防止把局部高氧測試搬成基地設定。
- 證據身份：有範圍的來源比較／固定原式與數據診斷；新策略須另測，非產品效能或完整安全認證
- 判別試驗：完整流股P/T與組成、校準流量以及材料實際暴露；不由氧分壓單量判設備合格。

## GAS-I06　電場相似外形不是月球或火星重力驗證

E-FIELD來源提供極性、配置與影像比較；選定影像相近只約束部分observable，不能推成完整重力或輸運等價。

- 組合資料：[EF-100_CH4-coflow-negative](datasets/EF-100_CH4-coflow-negative.md), [EF-40_CH4-coflow-negative](datasets/EF-40_CH4-coflow-negative.md), [EF-100_C2H4-coflow-negative](datasets/EF-100_C2H4-coflow-negative.md), [EF-30_C2H4-coflow-negative](datasets/EF-30_C2H4-coflow-negative.md), [EF-30_C2H4-coflow-positive](datasets/EF-30_C2H4-coflow-positive.md), [EF-40_CH4-coflow-positive](datasets/EF-40_CH4-coflow-positive.md), [EF-100_CH4-coflow-positive](datasets/EF-100_CH4-coflow-positive.md), [EF-100_C2H4-coflow-positive](datasets/EF-100_C2H4-coflow-positive.md), [EF-40_CH4-gasjet-negative](datasets/EF-40_CH4-gasjet-negative.md), [EF-30_C2H4-gasjet-negative](datasets/EF-30_C2H4-gasjet-negative.md), [EF-100_CH4-gasjet-negative](datasets/EF-100_CH4-gasjet-negative.md), [EF-100_C2H4-gasjet-negative](datasets/EF-100_C2H4-gasjet-negative.md), [EF-40_CH4-gasjet-positive](datasets/EF-40_CH4-gasjet-positive.md), [EF-30_C2H4-gasjet-positive](datasets/EF-30_C2H4-gasjet-positive.md), [EF-100_CH4-gasjet-positive](datasets/EF-100_CH4-gasjet-positive.md), [EF-100_C2H4-gasjet-positive](datasets/EF-100_C2H4-gasjet-positive.md)
- 結論定位：EF-F01；EF-F02；EF-F03
- 共同處：實際重力、電場與局部流動各自保留。
- 差異／適用條件：地面、落塔、ISS的網格／間距與場定義不同；日摘要與無身份續列也不增加試驗數。
- 新增消防洞見：用電場研究可控輸運介入，與獨立速度／熱／soot場比較後再研究預防或抑制用途。
- 證據身份：有範圍的來源比較／固定原式與數據診斷；新策略須另測，非產品效能或完整安全認證
- 判別試驗：同幾何、成分及場定義的配對；不能按E=V/d換算月／火星安全預測。

## GAS-I07　原式重現得好仍要看分組與observable

固定原式可與既有點比較，但同來源校準、來源火焰面、可見尖端與圖上讀值有不同身份；整體分數不保證每種燃料／尺寸都可靠。

- 組合資料：[BRE-AUX-ETHYLENE-DISK25-ISS](datasets/BRE-AUX-ETHYLENE-DISK25-ISS.md), [BRE-AUX-ETHYLENE-DISK50-ISS](datasets/BRE-AUX-ETHYLENE-DISK50-ISS.md), [BRE-AUX-METHANE-DISK25-ISS](datasets/BRE-AUX-METHANE-DISK25-ISS.md), [BRE-GROUND-DROP-NASA67](datasets/BRE-GROUND-DROP-NASA67.md), [WANG2019-GROUND-JET-NDF](datasets/WANG2019-GROUND-JET-NDF.md), [WANG2019-GROUND-JET-IDF](datasets/WANG2019-GROUND-JET-IDF.md)
- 結論定位：DROP-F01；GROUND-F01；BRE-F05；BRE-F06
- 共同處：本包保留失配、來源雙版本與缺閉合，不用挑較接近模型的目標或重估係數消掉差異。
- 差異／適用條件：SPICE是真ISS同源相關式，BRE是短落塔單例，Roper是地面共流噴口；不能互當跨架構驗證。
- 新增消防洞見：模型搜尋先按可預測量與幾何選模型，展示分組殘差與資料缺口，再決定需補哪種消防測試。
- 證據身份：有範圍的來源比較／固定原式與數據診斷；新策略須另測，非產品效能或完整安全認證
- 判別試驗：獨立新條件、同observable與預先指定端點；由同一熱流反算再重建不算獨立驗證。

## GAS-I08　來源資料組的身份是消防洞見的前提

逐日報告能支持部分原瓶標對照；空白尾列不增加火焰；臭氧條件互相矛盾則先隔離。數據整理會決定哪些機制結論目前可以比較。

- 組合資料：[CLD-CH4-original_coflow](datasets/CLD-CH4-original_coflow.md), [CLD-C2H4-original_coflow](datasets/CLD-C2H4-original_coflow.md), [CLD-C2H4-improved_coflow2021](datasets/CLD-C2H4-improved_coflow2021.md), [CLD-CH4-improved_coflow2021](datasets/CLD-CH4-improved_coflow2021.md), [CFIG-NORMAL-ethane](datasets/CFIG-NORMAL-ethane.md), [CFIG-NORMAL-50_butane](datasets/CFIG-NORMAL-50_butane.md), [CFIG-NORMAL-propane](datasets/CFIG-NORMAL-propane.md), [CFIG-NORMAL-30_butane](datasets/CFIG-NORMAL-30_butane.md), [CFIG-NORMAL-30_propane](datasets/CFIG-NORMAL-30_propane.md), [CFIG-NORMAL-30_ethane](datasets/CFIG-NORMAL-30_ethane.md), [CFIG-INVERSE-ethane](datasets/CFIG-INVERSE-ethane.md), [CFIG-INVERSE-propane](datasets/CFIG-INVERSE-propane.md), [CFIG-INVERSE-butane](datasets/CFIG-INVERSE-butane.md), [G142-DATAID-1](datasets/G142-DATAID-1.md), [G142-DATAID-2](datasets/G142-DATAID-2.md), [G142-DATAID-3](datasets/G142-DATAID-3.md), [G142-DATAID-4](datasets/G142-DATAID-4.md), [G142-DATAID-5](datasets/G142-DATAID-5.md), [G142-DATAID-6](datasets/G142-DATAID-6.md), [G142-DATAID-7](datasets/G142-DATAID-7.md), [G142-DATAID-8](datasets/G142-DATAID-8.md)
- 結論定位：CLD-F03；CG-F02；G142-F01
- 共同處：來源原值、版本與試次／操作階段保留，不補零、不向前填、不挑方便的版本。
- 差異／適用條件：原表修正的證據粒度不同；G142有數字也不代表臭氧或火焰模式已配對清楚。
- 新增消防洞見：建立可追溯的材料／燃料搜尋與實驗配對，優先補會改變消防判斷的來源衝突。
- 證據身份：有範圍的來源比較／固定原式與數據診斷；新策略須另測，非產品效能或完整安全認證
- 判別試驗：先核原paper圖表、TestDay／Test、單位與觀測定義，再做跨條件機制或產品比較。 文獻索引有兩個已證錯主題的DOI，已隔離；另一premixed冷／熱焰文獻只缺Figure join，不同列錯鏈。

## GAS-I09　固定理想寬度式揭露了缺少的群內物理

21筆歷史NASA無共流飛行表值與原式(9/16)d/Zst比較，整體R²約0.506；各燃料×噴口群為負R²。理想式每群只給常數，不能抓到群內量得的發光直徑變化。

- 組合資料：[JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR](datasets/JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR.md), [JET-RELATED-LSP-LIN1999-C2H4-D2P7-STILL-AIR](datasets/JET-RELATED-LSP-LIN1999-C2H4-D2P7-STILL-AIR.md), [JET-RELATED-LSP-LIN1999-C3H8-D1P6-STILL-AIR](datasets/JET-RELATED-LSP-LIN1999-C3H8-D1P6-STILL-AIR.md)
- 結論定位：JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-TABLE；JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-ENDPOINT；JET-RELATED-LSP-LIN1999-C2H4-D2P7-STILL-AIR-TABLE；JET-RELATED-LSP-LIN1999-C2H4-D2P7-STILL-AIR-ENDPOINT；JET-RELATED-LSP-LIN1999-C3H8-D1P6-STILL-AIR-TABLE；JET-RELATED-LSP-LIN1999-C3H8-D1P6-STILL-AIR-ENDPOINT
- 共同處：原論文數字表、原理想式與本次前向比較都保留同一觀測定義與來源條件。
- 差異／適用條件：該式有等擴散、定物性與忽略輻射等假設；可見最大直徑亦不同於完整反應面。現有失配不能唯一歸因為某一機理。
- 新增消防洞見：預防模型選擇需保留壓力、流量及可觀測量，不用一個幾何相似式給所有操作點的接觸／安全距離。
- 證據身份：有範圍的來源比較／固定原式與數據診斷；新策略須另測，非產品效能或完整安全認證
- 判別試驗：以原條件做配對壓力／流量比較及獨立反應面／發光寬度量測；本次不重估係數。

## GAS-I10　地面吹熄不能直接當微重力抑制保證

SLICE來源在指定燃料與噴口圖板顯示1g／微重力的抬升、吹熄及稀釋穩定界線不同；低速稀釋與高速案例的差異方向與大小也不一致。

- 組合資料：[JET-SLICE-CH4-070-N2-030-NOMINAL-D0P8-COFLOW](datasets/JET-SLICE-CH4-070-N2-030-NOMINAL-D0P8-COFLOW.md), [JET-SLICE-C2H4-020-N2-080-GEOMETRY-UNKNOWN-COFLOW](datasets/JET-SLICE-C2H4-020-N2-080-GEOMETRY-UNKNOWN-COFLOW.md), [JET-SLICE-C2H6-100-GEOMETRY-UNKNOWN-COFLOW](datasets/JET-SLICE-C2H6-100-GEOMETRY-UNKNOWN-COFLOW.md), [JET-SLICE-C2H4-100-GEOMETRY-UNKNOWN-SPICE-MODE](datasets/JET-SLICE-C2H4-100-GEOMETRY-UNKNOWN-SPICE-MODE.md), [JET-SLICE-CH4-100-NOMINAL-D0P4-COFLOW](datasets/JET-SLICE-CH4-100-NOMINAL-D0P4-COFLOW.md), [JET-SLICE-CH4-070-N2-030-NOMINAL-D0P4-COFLOW](datasets/JET-SLICE-CH4-070-N2-030-NOMINAL-D0P4-COFLOW.md), [JET-SLICE-C2H4-020-N2-080-NOMINAL-D0P8-COFLOW](datasets/JET-SLICE-C2H4-020-N2-080-NOMINAL-D0P8-COFLOW.md), [JET-SLICE-C2H4-020-N2-080-NOMINAL-D1P6-COFLOW](datasets/JET-SLICE-C2H4-020-N2-080-NOMINAL-D1P6-COFLOW.md), [JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW](datasets/JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW.md), [JET-SLICE-C2H6-100-NOMINAL-D0P4-COFLOW](datasets/JET-SLICE-C2H6-100-NOMINAL-D0P4-COFLOW.md), [JET-SLICE-C2H4-100-NOMINAL-D0P4-COFLOW](datasets/JET-SLICE-C2H4-100-NOMINAL-D0P4-COFLOW.md)
- 結論定位：JET-SLICE-STABILITY-GRAVITY-SCOPE
- 共同處：來源與幾何研究都要求分開燃料／共流速度及火焰端點。
- 差異／適用條件：此處為已定位的原圖板／作者觀察，未重新取出數字門檻；不能把3.2mm幾何論文的參數搬到0.4mm穩定圖。
- 新增消防洞見：抑制策略以實際火源及兩股速度的狀態辨識選介入，不直接移用地面風速；優先補低速稀釋穩定火焰的介入試驗。
- 證據身份：有範圍的來源比較／固定原式與數據診斷；新策略須另測，非產品效能或完整安全認證
- 判別試驗：相同幾何、成分、重力與操作程序的數值界線及化學熄滅／再燃真值。
