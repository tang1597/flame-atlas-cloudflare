# SMK-E115-COUPLED Garrick DBP gas/particle transport and phase change

## 公式與來源

`Source gas balancesEqs1,10; nodeGDEEqs11,19,22–30; coagEq23 andvaporEq30`

- card: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase5_shared_document_review\role_E\modeling\source_cards.json#/0
- inventory: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase5_shared_document_review\role_E\modeling\model_inventory.json
- locators: ["physicalpp5–8Eqs1–30", "p9fixedmodelconditions", "p21Table3", "p25Table4modifiedcases"]


## 使用哪些量與單位

### 輸入

- state: collocatedT,velocity,vapor,nodepopulations
- properties: DBPthermo/transportlaws
- boundary: mesh,sourceflux,initial/boundaryhistory,largestnodehandling


### 輸出

- PSD_and_fields: source simulation outputs


## 對應展示程式

Unknown；此處沒有補入推測值。


互動入口為 `viewer.html`；圖形邏輯為 `viewer.js`。沒有 planned_functions 的條目沒有完整數值求解器，不能宣稱已算出預測。

## 比較分類與獨立性

狀態：no_new_solver; archived_source_curves_only。比較角色：source_calculation_not_measurement。

- Existing sixPSD.dat files are simulation snapshots, no independent measuredtarget or complete dynamicstate. Unknown absolutePSDordinateunits/normalization must remainUnknown.


## 限制與消防解讀

- EarthGravity directories are calculations, not1gmeasurements.
- DBPsurrogate is notDOPcalibration,polymerpyrolysis orDAFTdust.
- Grid-known normalized shape or volume ratios maybedisplayed with explicit sourcecalc labels.
- equation_inventory noverifiedequation status is scope-incomplete relative tophase5sourceaudit; preserveoldinventory and record this distinction.


這個公式只能支持其觀測量與閉合假設範圍；不直接輸出警報效能、通用消防安全或產品資格。
