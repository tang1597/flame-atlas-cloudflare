# SMK-MASS-DIAMETER Source mass/number/density diameter

## 公式與來源

`dm_um=(6000*Cmass_mg_m3/(pi*rho_g_cm3*N_cm3))^(1/3); M3_um3_cm3=6000*Cmass_mg_m3/(pi*rho_g_cm3)`

- study_ids: ["PSI-101"]
- report: Smoke Aerosol Measurement Experiment Re-flight (SAMER)
- edition: June2,2014 FinalReport
- sha256: 65381e2715eb7379113dd1b9c550baaa5fa5a247dba00419123143aa98ef80d6
- locators: ["AppendixFphysicalp74Eqs1–2", "physicalp75Eq6", "physicalp77calibration/density", "physicalpp28–30finite-range moments"]


## 使用哪些量與單位

### 輸入

- number: #/cm3
- mass_concentration: mg/m3, already source-calibrated
- density: g/cm3, source fixed assumption


### 輸出

- dm: um
- m3: um3/cm3


## 對應展示程式

- physics.py::mass_to_m3
- physics.py::mass_moment_diameter


互動入口為 `viewer.html`；圖形邏輯為 `viewer.js`。沒有 planned_functions 的條目沒有完整數值求解器，不能宣稱已算出預測。

## 比較分類與獨立性

狀態：executable_for_source_approved_rows。比較角色：same_source_algebraic_reproduction。

- BJ is derived from BD/BH/BW by the same relation; cached-vs-calculated error is closure, not independent physical validation.


## 限制與消防解讀

- Do not reapply TEOM/DustTrak correction already included in BH.
- Density is an author assumption, not an independently measured aerosol density.
- Raw optical proxy alone is not admissible as calibrated mass.


這個公式只能支持其觀測量與閉合假設範圍；不直接輸出警報效能、通用消防安全或產品資格。
