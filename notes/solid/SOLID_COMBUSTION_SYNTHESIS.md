# 固體燃燒跨資料集結論與消防洞見

依材料、幾何與實驗模式整理相同與不同結論，再連到預防、偵測及抑制。以下是有範圍的跨來源整合與待驗證設計構想，不是把不同試驗合成同一火災。

## SOLID-I01　火焰尺寸受限與燃料路徑阻斷要分開

受限尺寸的火焰或熱解區仍可造成材料持續消耗與向前傳播；不能用一個火焰長度宣告相鄰材料安全。

- 組合資料：[SAF98-SIBAL-LARGE-CONCURRENT](datasets/SAF98-SIBAL-LARGE-CONCURRENT.md), [SAF99-SIBAL-NARROW-CONCURRENT](datasets/SAF99-SIBAL-NARROW-CONCURRENT.md), [SAF99-PMMA-GROOVED-CONCURRENT](datasets/SAF99-PMMA-GROOVED-CONCURRENT.md), [SAF99-PMMA-FLAT-CONCURRENT](datasets/SAF99-PMMA-FLAT-CONCURRENT.md)
- 共同處：SIBAL與PMMA來源都保留了尺寸、前緣移動、總損傷不同端點。
- 差異／適用條件：布材可燒過試片；厚板較錨定。幾何、holder與入口發展亦不同。
- 新增消防洞見：預防產品可把燃料路徑連續性、受熱暴露與傳播前緣列為材料配置的獨立評估項目。
- 證據身份：跨來源機制整合；產品效果尚未共同驗證
- 判別試驗：同材料與幾何下測隔斷距離、局部熱流／熱劑量及對鄰材點燃；目前沒有通用安全距離。

## SOLID-I02　降低通風的方向取決於材料與火焰狀態

指定SIBAL案例降流後熄滅，其他來源在低流仍燃或局部脫離後恢復包覆；一個固定降流閾值不能代表所有火。

- 組合資料：[B25-SIBAL-flat-concurrent](datasets/B25-SIBAL-flat-concurrent.md), [B26-SIBAL-opposed](datasets/B26-SIBAL-opposed.md), [B25-PMMA-clear-rod-opposed](datasets/B25-PMMA-clear-rod-opposed.md), [b26-pmma-sphere-wake](datasets/b26-pmma-sphere-wake.md)
- 共同處：氧輸運與固相熱歷史都關聯到介入後端點。
- 差異／適用條件：T20、O18、Test9與球尾流是不同材料／幾何／試次；不計混合成功率。
- 新增消防洞見：抑制策略先辨識材料、流向與局部／全局火焰狀態，再以回饋觀測評估介入；通風重啟另作確認階段。
- 證據身份：跨來源機制整合；產品效果尚未共同驗證
- 判別試驗：同幾何、氧與初始熱歷史的控制比較；同步實際流場、火焰包覆、溫度與全局熄滅。

## SOLID-I03　滅火劑化學與送入火場的流動要各自測

局部惰性氣體射流與幾何改變都可能改變氧輸運及熱回授，藥劑流量本身不足描述抑制效果。

- 組合資料：[b26-pmma-sphere-wake](datasets/b26-pmma-sphere-wake.md), [SAF99-PMMA-GROOVED-CONCURRENT](datasets/SAF99-PMMA-GROOVED-CONCURRENT.md), [SAF99-PMMA-FLAT-CONCURRENT](datasets/SAF99-PMMA-FLAT-CONCURRENT.md)
- 共同處：來源指出尾流維持燃燒及厚板基部熱回授的角色。
- 差異／適用條件：捲入空氣與熱回授是作者解釋，尚無共同局部氧場與熱流真值。
- 新增消防洞見：可研究低捲吸或包覆式的局部抑制頭，將局部氧／流速與殘餘熱監測納入設計。
- 證據身份：跨來源機制整合；產品效果尚未共同驗證
- 判別試驗：同一火源幾何比較噴流動量、局部氣體組成、熱流與再燃；不能以現有跨案例排序藥劑效能。

## SOLID-I04　熄焰後重啟通風是獨立的偵測情境

Saffire-II原文同序列記錄殘留煙在通風重啟後產生強散射；BRE又提醒命令關閉不是實際流量或反應歸零。

- 組合資料：[SAF99-PMMA-GROOVED-CONCURRENT](datasets/SAF99-PMMA-GROOVED-CONCURRENT.md), [SAF99-PMMA-FLAT-CONCURRENT](datasets/SAF99-PMMA-FLAT-CONCURRENT.md), [BRE-AUX-ETHYLENE-DISK25-ISS](datasets/BRE-AUX-ETHYLENE-DISK25-ISS.md)
- 共同處：命令、火焰可見端點、煙／氣體運送到感測器是不同層級。
- 差異／適用條件：Saffire-II為同操作序列的作者觀察；BRE是另一裝置的邊界紀錄，不是共同感測測試。現有Cygnus時鐘配對未重現該峰。 原煙工作表與RawData一段逐點重複；正SaffireTimestamp段的煙欄全0，非零煙值全在SaffireTimestamp=0段，不能據此判斷同期無煙。
- 新增消防洞見：偵測／抑制產品可設計熄火後監測階段，將通風重啟、殘餘熱與煙訊號分開處理，避免過早解除監測。
- 證據身份：同序列來源觀察＋跨裝置端點約束；新產品判據未驗證
- 判別試驗：先補精確時鐘對照與啟用狀態，再測真實警報、殘餘反應真值和取樣路徑；目前不給監測秒數。 Sample8/9風扇、風速、CO2可各自作圖，煙仍需可靠對時。

## SOLID-I05　同一PMMA名稱要先選熱控、厚板或棒狀模型

薄片的厚度反比式可重現指定熱控極限；厚板、棒狀、低流輻射與高流動力學區需要不同閉合條件。

- 組合資料：[B25-PMMA-film-opposed](datasets/B25-PMMA-film-opposed.md), [B25-PMMA-slab-one-sided](datasets/B25-PMMA-slab-one-sided.md), [B25-PMMA-clear-rod-opposed](datasets/B25-PMMA-clear-rod-opposed.md), [SAF99-PMMA-FLAT-CONCURRENT](datasets/SAF99-PMMA-FLAT-CONCURRENT.md), [B62-PMMA100um-opposed-FGM-benchmark](datasets/B62-PMMA100um-opposed-FGM-benchmark.md)
- 共同處：尺寸與熱回授均是模型選擇因子。
- 差異／適用條件：熱控式、FGM、DNS及條件剖面並非同一預測器；其中來源模型也有過預測。
- 新增消防洞見：預防工具先判斷材料形狀、厚度、支撐與適用區域，再展示可計算量及資料缺口；不把薄片滑桿外推成設備安全。
- 證據身份：跨來源機制整合；產品效果尚未共同驗證
- 判別試驗：取得同observable原始軌跡、獨立物性與未參與參數估計的幾何條件，再做預測驗證。

## SOLID-I06　地球資料可轉移的部分必須逐個observable核對

地面篩選、微重力延燒與改壓力對照能提供不同約束，不能用材料同名或兩個統計量直接換算重力效應。

- 組合資料：[B25-PMMA-black-rod-opposed](datasets/B25-PMMA-black-rod-opposed.md), [B26-SIBAL-concurrent](datasets/B26-SIBAL-concurrent.md), [B26-SIBAL-opposed](datasets/B26-SIBAL-opposed.md), [SAF99-PMMA-FLAT-CONCURRENT](datasets/SAF99-PMMA-FLAT-CONCURRENT.md)
- 共同處：已有來源顯示流向、氧、壓與幾何會改變比較結果。
- 差異／適用條件：同微重力順／逆流差異不是1g控制；厚板改壓力對照也不等於完整匹配ISS艙內條件。
- 新增消防洞見：以匹配觀測量的地面預防篩選矩陣縮小太空試驗範圍，保留低浮力端仍須補測的組合。
- 證據身份：跨來源機制整合；產品效果尚未共同驗證
- 判別試驗：同配方、幾何、流向及氧／壓條件的地面與低重力對照，分別驗延燒、熱流與偵測端點。

## SOLID-I07　配方與點火程序比材料商品名更重要

Nomex相關名稱在不同配方、支撐、先導火與流況有不同點燃／維持／延燒端點。

- 組合資料：[B25-NomexIII-concurrent](datasets/B25-NomexIII-concurrent.md), [b26-nomexblend-unknownformulation-fabric-not-recorded-in-csv](datasets/b26-nomexblend-unknownformulation-fabric-not-recorded-in-csv.md), [b26-nomexiii-fabric-not-recorded-in-csv](datasets/b26-nomexiii-fabric-not-recorded-in-csv.md), [SAF99-NOMEX-TARGET-PMMA-PILOT](datasets/SAF99-NOMEX-TARGET-PMMA-PILOT.md)
- 共同處：不點燃、不持續燃燒、瞬間閃燃與下游目標未點燃需要分開記錄。
- 差異／適用條件：未確認blend配方的原表不能自動連到另一篇NomexIII實驗；Saffire試驗還有PMMA先導段。
- 新增消防洞見：材料篩選產品應記錄完整配方與先導熱暴露，分開顯示點燃、維持與傳播，防止錯誤替代材料。
- 證據身份：跨來源機制整合；產品效果尚未共同驗證
- 判別試驗：先補同配方／支撐與同點火程序的試驗，再比較艙內氧／流況；原表未對應者不作合格判定。

## SOLID-I08　氣體與煙訊號要連到傳輸及量測定義

熄焰後混合、端點濃度、計算熱回授與實際殘餘反應各自有不同解釋；單一訊號不能完成所有狀態判定。 本次以raw材料明寫PMMA的39列比較端點（薄片15／板20／棒4），保留缺值與近零差值；未證實39個獨立火災。

- 組合資料：[SAF99-PMMA-GROOVED-CONCURRENT](datasets/SAF99-PMMA-GROOVED-CONCURRENT.md), [SAF99-PMMA-FLAT-CONCURRENT](datasets/SAF99-PMMA-FLAT-CONCURRENT.md), [B25-PMMA-film-opposed](datasets/B25-PMMA-film-opposed.md), [BRE-AUX-ETHYLENE-DISK25-ISS](datasets/BRE-AUX-ETHYLENE-DISK25-ISS.md)
- 共同處：來源均要求保留量測或計算的定義與輸入。
- 差異／適用條件：濃度近似不是完整莫耳平衡；由同一量反算再重建也不是獨立預測。 5:6參考採共同基準與近似固定總莫耳數；接近該線不能推出完全燃燒或無CO。
- 新增消防洞見：偵測工具可把流動／取樣狀態與煙、熱、氣體訊號放在同一時間基準上，提供端點一致性檢查。
- 證據身份：跨來源機制整合；產品效果尚未共同驗證
- 判別試驗：時鐘、校準、濕／乾基準、通風與獨立反應真值；目前不建立假警率或漏報率。
