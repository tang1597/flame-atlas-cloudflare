# SMK-E115-NODE-SPLIT Garrick/Prakash per-collision node volume split

## 公式與來源

`v_i=vm*r^(i-1); vnew=vi+vj; chi_lo=(vhi-vnew)/(vhi-vlo); chi_hi=(vnew-vlo)/(vhi-vlo)`

- report: Garrick2020 FinalReport
- sha256: 487108f951ba8ec9042464ae7c70a8190fa63c4b1141f8b1dfe19d697bd9752c
- locator: physicalp7Eqs23–24,p9grid; Prakash2003p3Eqs6–7
- audit: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase5_shared_document_review\role_E\modeling\model_audit.json


## 使用哪些量與單位

### 輸入

- vm: 4.44e-28m3
- volume_ratio: 2.25
- nodes: 45includingmonomer; particle2..45


### 輸出

- weights: dimensionless
- volume_residual: relative


## 對應展示程式

- physics.py::node_volume_split


互動入口為 `viewer.html`；圖形邏輯為 `viewer.js`。沒有 planned_functions 的條目沒有完整數值求解器，不能宣稱已算出預測。

## 比較分類與獨立性

狀態：executable_component_only。比較角色：conservation_operator_diagnostic。

- Per-collision identity requires no beta. A rate/timeprediction requires beta and fullstate; overflow is Unknown without a rule.


## 限制與消防解讀

- No largest-node clipping/reinjection/discard invented.
- Sourceexisting1849interiorpairsclose;87overflowpairsremainunresolved.
- This does not validate the archived solver implementation or experimental smoke.


這個公式只能支持其觀測量與閉合假設範圍；不直接輸出警報效能、通用消防安全或產品資格。
