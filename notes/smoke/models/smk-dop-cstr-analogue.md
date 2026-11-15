# SMK-DOP-CSTR-ANALOGUE External complete-mixing step analogue

## 公式與來源

`V*dC/dt=Q*(Cin-C); x=1-exp(-Q*t/V);t95=-ln(0.05)*V/Q`

- doi: 10.6028/jres.085.014
- title: Response of Smoke Detectors to Monodisperse Aerosols
- locator: physicalpp5–6/printed227–228Section3.4/Figs6–7
- note: Analyst derivation of authorcomplete-mixingdescription, not printednumberedequation


## 使用哪些量與單位

### 輸入

- V: cm3constant
- Q: cm3/sconstant
- boundary: knownstep
- x0: 0


### 輸出

- normalizedC: dimensionless
- time: s


## 對應展示程式

Unknown；此處沒有補入推測值。


互動入口為 `viewer.html`；圖形邏輯為 `viewer.js`。沒有 planned_functions 的條目沒有完整數值求解器，不能宣稱已算出預測。

## 比較分類與獨立性

狀態：optional_context_only_not_NASA_same_material。比較角色：external_source_assumption_replay。

- Do not use this curve asSAMEpistondynamics orNASApolymer/dustvalidation.


## 限制與消防解讀

- No deposition/coagulation/detectordelayterms.
- No newvaluesdefaulted; ifrootdoesnotprovidefrozenanalogueinputs,omitthenumericcurve.


這個公式只能支持其觀測量與閉合假設範圍；不直接輸出警報效能、通用消防安全或產品資格。
