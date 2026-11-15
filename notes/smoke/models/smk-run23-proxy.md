# SMK-RUN23-PROXY Existing source-window optical proxy diagnostic

## 公式與來源

`conditional_aged_proxy=fresh_window_proxy_mean; observedratio=aged_mean/fresh_mean`

- audit: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase7\role_E\run23_conservation_diagnostic\diagnostic_results.json
- locator: SAME2010physicalp27Fig13; raw trace source lineage inphase7


## 使用哪些量與單位

### 輸入

- fresh_initial_proxy: mg/m3 asstored; notgravimetricmass
- aged_proxy: unused forbaseline, measured comparison
- windows: source-fixed51rowsperwindow


### 輸出

- proxy_residual: mg/m3
- proxy_ratio: dimensionless


## 對應展示程式

Unknown；此處沒有補入推測值。


互動入口為 `viewer.html`；圖形邏輯為 `viewer.js`。沒有 planned_functions 的條目沒有完整數值求解器，不能宣稱已算出預測。

## 比較分類與獨立性

狀態：existing_result_visualization_only。比較角色：conservation_or_derived_diagnostic。

- Independent mass/transport/instrument prerequisites are not established; formal physical agreementUnknown.


## 限制與消防解讀

- No constant-number prediction: coagulation changesnumber.
- Freshwindowstraddlesexpulsionstateboundary;33freshBvalues exceedgeneric100mg/m3range. Keep allpoints withflags; no clipping to improveagreement.
- 51timestamps are not51independentfires; temporalSD is not measurementuncertainty.
- STS power0/alarm0 is masked evidence; sourcelegacyIonA must not be silently classified as ionizationM1 inSAME-R.


這個公式只能支持其觀測量與閉合假設範圍；不直接輸出警報效能、通用消防安全或產品資格。
