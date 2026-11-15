# SMK-LOGNORMAL-FORWARD Source lognormal size distribution / analytic moments

## 公式與來源

`f_N(D)=N/[sqrt(2*pi)*D*ln(sigma)]*exp[-(ln(D/Dg))^2/(2*ln(sigma)^2)]; M_k=N*Dg^k*exp(0.5*k^2*ln(sigma)^2)`

- study_ids: ["PSI-102", "PSI-101"]
- report: Smoke Aerosol Measurement Experiment (SAME): Final Report
- edition: March15,2010; physicalpp15–19 correspond to printedpp5–9
- sha256: af91c96d22d93bbefbc0f2c5e1cc06e24813f532e5379b3fec9f121cccb22193
- locators: ["physicalp15Eqs1–2d", "physicalp16Eq2f,Eq3", "physicalp17Eq6", "physicalp18Eqs7–9", "physicalp19Eqs10–13", "physicalpp22–24calibrationFigs7–9"]


## 使用哪些量與單位

### 輸入

- N: #/cm3
- Dg: um
- sigma_g: dimensionless>1
- D: um


### 輸出

- f_N: #/cm3/um
- dN_dlnD: #/cm3
- moments: #/cm3 * um^k


## 對應展示程式

- physics.py::lognormal_pdf
- physics.py::lognormal_moment


互動入口為 `viewer.html`；圖形邏輯為 `viewer.js`。沒有 planned_functions 的條目沒有完整數值求解器，不能宣稱已算出預測。

## 比較分類與獨立性

狀態：executable_as_reconstruction_or_declared_sensitivity。比較角色：same_source_reconstruction_if_inverse_inputs。

- Only independently prescribed/measured unused PSD or TEM/sample-linked targets could support independent validation. If parameters came from the same moments, forwardM3 is an identity.


## 限制與消防解讀

- The moment formula is an explicit mathematical integral of sourceEq3, not a new calibrated transport law.
- Do not mix f_N,dN/dlnD,anddN/dlog10D y-axis units.
- Arbitrary PSD not determined by three moments; morphology/size-range assumptions remain.


這個公式只能支持其觀測量與閉合假設範圍；不直接輸出警報效能、通用消防安全或產品資格。
