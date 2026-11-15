# SMK-MODE-INVENTORY Mode-specific aerosol inventory

## 公式與來源

`d(CV)/dt=sum(Qin*Cin)-sum(Qout*Cout)+G-R`

- audit: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase7\role_E\same_protocol\model_applicability.json
- reportLocator: SAME2010physicalpp20–23; SAME-R2014pp8–11


## 使用哪些量與單位

### 輸入

- V(t): m3
- Q: m3/s at commonreferenceP/T
- C: consistent amount/m3
- G,R: amount/s


### 輸出

- C(t): same concentrationunit


## 對應展示程式

Unknown；此處沒有補入推測值。


互動入口為 `viewer.html`；圖形邏輯為 `viewer.js`。沒有 planned_functions 的條目沒有完整數值求解器，不能宣稱已算出預測。

## 比較分類與獨立性

狀態：symbolic_only_missing_closed_inputs。比較角色：not_testable_missing_inputs。

- Require actualV(t),inletwaveform,allphysicalflows,losslaw,mixing/outlet andobservationtransfer. Sourceheateron is not a known smokeinputstep.


## 限制與消防解讀

- Analyst conservation derivation, not a printed SAME aerosol ODE.
- Pistonfill/hold/partialexpel/hold/expel is not whole-run fixed-volumeCSTR.
- Well-mixed expel with shrinkingvolume can maintainconcentration while inventorydecreases.


這個公式只能支持其觀測量與閉合假設範圍；不直接輸出警報效能、通用消防安全或產品資格。
