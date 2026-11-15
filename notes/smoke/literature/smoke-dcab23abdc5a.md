# A Simple Numerical Algorithm and Software for Solution of Nucleation, Surface Growth, and Coagulation Problems

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-dcab23abdc5a | original numerical-method article | 7page author-hosted publisher-formatted article,2003; paper header DOI10.1080/02786820390225826 differs from current publisher record10.1080/02786820300933; both retained. | dcab23abdc5aeaa5e6745958ac3f305b94a26fab192ac817ee07a1be665092a3 | {"physical_pdf_pages": 7} | prior_primary_audit_reused_source_bytes_reverified |


- https://doi.org/10.1080/02786820390225826
- https://mrzgroup.engr.ucr.edu/ngde-softwarengde-software-solution-nucleation-surface-growth-and-coagulation-problems
- https://mrzgroup.engr.ucr.edu/sites/g/files/rcwecm2316/files/2019-02/2003_AST_nodal.pdf
- https://www.tandfonline.com/doi/abs/10.1080/02786820300933


DOI：10.1080/02786820390225826

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/earth_space_transfer_20261114/phase5_shared_document_review/role_E/modeling/Prakash2003_NGDE_UCR_author.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-dcab23abdc5a-C01 | 零寬度節點算子把合併粒子的體積分配到相鄰體積節點，並與單體平衡耦合。原方法用 40 節點、體積比 2；PSI-115 採 45 節點、比值 2.25，須用自己的 DBP 常數，不能把鋁粒子範例當成 DBP 驗證。 | calculation | pp2-3 Eqs1-9,Fig2 | original method uses40nodes and volume ratio2 | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-115"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- {"factor": "source_conditions", "values": {"original_example_material": "aluminum", "original_node_count": 40, "original_volume_ratio": 2, "SAME115_node_count": 45, "SAME115_volume_ratio": 2.25}, "status": "source_condition_context_not_per_trial_controls", "source_locator": ["p1 title/abstract", "p2 Eqs1-4 node/nucleation formulation", "p3 Eqs6-9 andFig2 coagulation/monomer balance"]}


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- Method/theory source, not an independent actual1g counterpart.
- Retrieved author package readme is datedMay14,2005; source files and56,858byte zip were inspected but not installed/executed.
- Generic NGDE code lacks the PSI115 two-dimensional coupled flow/thermal boundary implementation and matching local initial state.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

| 模型ID／名稱 | 來源公式 | 可執行／比較角色 | 展示 code 名稱 | 適用限制 |
| --- | --- | --- | --- | --- |
| SMK-E115-NODE-SPLIT | v_i=vm*r^(i-1); vnew=vi+vj; chi_lo=(vhi-vnew)/(vhi-vlo); chi_hi=(vnew-vlo)/(vhi-vlo) | executable_component_only; conservation_operator_diagnostic | physics.py::node_volume_split; viewer.js | \["No largest-node clipping/reinjection/discard invented.", "Sourceexisting1849interiorpairsclose;87overflowpairsremainunresolved.", "This does not validate the archived solver implementation or experimental smoke."\] |
