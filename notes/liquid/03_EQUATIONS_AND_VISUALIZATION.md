# 方程、來源曲線與物理—實驗視覺化

工具把來源實測/分析曲線、原作者模型輸出和條件式D²重建分開。**液滴直徑不是火焰尺寸；重播模型資料不是執行原求解器；同源K重建不是獨立驗證。** 缺完整物性/初始場時，不會補標準值產生看似完整的理論曲線。**來源單位未核定、audit標為blocked的曲線不畫物理比較圖；仍可在可展開的raw-coordinate table查原值與缺件說明。**

## 方程與目標

| ID／來源定位 | 公式與目標 | 必要輸入、單位與係數來源 | 本輪可稱什麼 |
|---|---|---|---|
| D2／FEQ01 | D_l²(t)=D_l²(t0)−K(t−t0)，K=−d(D_l²)/dt | D_l為液滴長度；t為s；K為一致的mm²/s或m²/s。來源同軌跡分析/擬合K不是獨立物性。 | stage-local近似及同源重建；不是Df(t)或化學溫度預測。 |
| FLEX-MEOH2013 Eq1，physicalp5 | Kcal=8λg/(ρl cp,g)ln(1+B) | λ[W/(mK)]、ρl[kg/m³]、cp[J/(kgK)]；SI產生m²/s，×10^6成mm²/s。 | 來源準穩態正向式；目前沒有matched完整物性表。 |
| 同Eq2，physicalpp5–6 | B=[qf YO,∞ f+cp,g(T∞−Tb)]/L | qf[J/kgfuel]；YO,∞是氧**質量**分率；f是化學計量**fuel/oxygen質量比**；T為K，L[J/kg]。Law–Williams物性評估配方需另取得。 | 不能直接帶入dataset氧molefraction；positiveB也不單獨證明點燃/火焰存在。 |
| 同Eq3/4，physicalp7 | FSR=Df/D的來源半經驗關係；代數轉寫未充分核定，未猜式 | 需要**實驗K**、傳輸/密度/水效應等輸入。 | response-conditioned correlation，不是獨立flame-size預測。 |
| CFI FEQ02／Aspects2015，physicalpp9,13 | K=8λ/(cpρl)ln[1+(2Tb−Tl−T∞)/(L/cp)] | 此Tb是**NTC midpoint有效溫度**，不是前述fuelboiling temperature。Tl/T∞[K]、L[J/kg]與其他SI物性需matchedclosure。 | 部分燃燒/半經驗模型，缺NTC/物性及溫度時不能封閉當前rawcase。 |
| CFI FEQ03／FLEX-EXTCONF2014，physicalpp7–8 | τext=Dce²/Kc，來源相關τext∝C_O2^(-3/2)、Dce∝C_O2^(-3/4) | Dce[cm]配Kc[cm²/s]；C_O2是氧的molar concentration[mol/cm³]，不是CO2分子。Kc仍為實驗分析量。 | 已觀測extinction的來源相關，不是獨立時間/熄滅預測律。 |
| CFI FEQ04／dodecane kinetics2020，Table1physicalp2 | k_i=A_i exp(−Ta_i/T) | 來源mol,s,cm³,K制；雙分子steps1–3的A是cm³/(mol·s)，單分子steps4–6為1/s。原作者step4等有校準。 | 反應率係數與已校準簡化化學；不等於完整D(t)求解器。Table轉寫尚非全部visual-mathverified。 |
| CFI FEQ05／EXTDECK2022physicalp9 | FSR=Dflame/Dliquid；(d/d0)²；t/d0² | FSR及normalizedD²無因次；當d0為mm時normalized time為s/mm²，**不是秒**。 | 座標定義，不是新物理預測。 |
| Optical2014 Eqs6–7，physicalp8 | Q=D_matrix⁻¹E；d²=4(A²+B²+C) | D_matrix為矩陣，不是液滴D；x/y為pixel時d²為pixel²，需frame-scale轉物理長度。 | 影像量測處理，不是燃燒定律。 |
| FLEX2 SRD Eq2，physicalp44 | Gr/Re²=gβΔTD/U∞²≪1 | g[m/s²]、β[1/K]、ΔT[K]、尺度D[m]、U∞[m/s]；原文為設計需求。 | 不能把需求g當實測g，也不保證ignition/extinction可跨重力。 |

同符號可能在不同來源扮演不同角色，尤其Tb、D、K；必須跟著來源定義，不按名字合併。更完整的未知輸入與文獻公式見 [FLEX公式卡](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/flex_flex2_literature.json>)、[CFI FEQ01–05](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/cfi_literature.json>)。

## 可執行程式與原作者程式的區別

| 精確程式名稱 | 本輪作用 | 與原作者模型的關係 |
|---|---|---|
| [physics_models.py](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/physics_models.py>)::d2_history | 來源D0、K的D²正向重建；域外回傳null | 不是重新擬合，也不是獨立Kclosure。 |
| 同檔::classical_burning_constant | 原MeOH2013 Eqs1–2，要求明示SI輸入，輸出mm²/s | 無內建燃料物性/配方或自動mole→mass替換。 |
| 同檔::cool_stage_rate | source半經驗NTC式，獨立命名effective_ntc_temperature | 沒有補反應機制或由target估NTC。 |
| 同檔::same_source_errors | 僅相同供給x的同源診斷，沒有插值/逐列配對 | 不是held-out/independent validation，不能按frame n當burn n。 |
| [prepare_visualization.py](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/prepare_visualization.py>) | 保留sourcecolumns、單位、獨立座標、版本與point annotations | 重播9份PSI117來源表；**不是執行原solver**。 |
| [web/viewer.js](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/web/viewer.js>) | case/quantity/series互動，source/limits與原頁連結 | 不推論未知條件，不產生safetyverdict。 |
| [serve.py](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/serve.py>) | 只讀loopback offlineviewer | 不載入ML或啟動訓練。 |

9份來源CSV是author-computed output及comparison blocks；沒有取得對應原始solver source filename、版本、完整case dictionaries/機制/物性/初始場與點火配置。PSI117 umbrella提到OpenFOAM，不足以替較早明示1D論文指定同一求解器。原作者code目前應記為 unavailable/unknown，不能拿上述新寫的viewer當original code。

## 可看的來源對照

| case | 能看什麼 | 不能省略的差異 |
|---|---|---|
| Test002／20CAL10，methanol | sourceD²窗142frame和兩版K/D0重建；UV191、visible140點獨立通道 | 142frame屬一burn；t0是sourceframe時間；workbookK=.5356與summaryK=.60mm²/s不擇優。 |
| PSI117 extinction/rate vsP | 來源experimental點及已計算model線 | 不逐列配對；unit由原頁核定才overlay，未知仍null；3atm experimentalcool零是無finite endpoint，不是精確De=0。 |
| Stable/Oscillatory cool | 原作者D、K、Tmax和normalizedratios的動態輸出 | 這些可為model-only，沒有自動增加flight觀測；source負K可反映初期D²變化，不能一律刪掉。 |
| ThreeStage | C12 source實驗與不同C7model的publishedcomparison；D²、Df、radiance與cool opticalsizes分開 | 共圖/normalizedaxis不等於同fuel或matchedcase；HWFM與peak-peak不是液滴熄滅De。 |

資料輸入：[visualization_data.json](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/visualization_data.json>)；顯示投影：[visualization_view.json](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/visualization_view.json>)；單位/端點核對：[unit_audit.json](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/unit_audit.json>)。九表67條source series加Test002三通道，共70條原來源series；準備視圖另加兩條條件重建，不代表多兩次實驗。

## 圖表與離線預覽

由root提供的獨立本機預覽入口為 [http://127.0.0.1:8808/](http://127.0.0.1:8808/)；需要該離線服務正在執行。本輪沒有重啟正式atlas或把資料傳上Git。程式使用說明見 [README](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/README.md>)。

- [01_test002_source_editions PNG](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/figures/01_test002_source_editions.png>)／[SVG](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/figures/01_test002_source_editions.svg>)：Measured source curves and two D² reconstructions from reported source editions. UV / visible channels are not row-paired; one burn is not 142 independent trials.
- [02_c12_pressure_endpoints PNG](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/figures/02_c12_pressure_endpoints.png>)／[SVG](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/figures/02_c12_pressure_endpoints.svg>)：Units traced to the author extinction presentation, physical PDF page15. Experimental zero at G7/H7 is a non-finite endpoint; model 0.03 mm is retained. No trial-level independent-validation metric.
- [03_three_stage_source_comparison PNG](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/figures/03_three_stage_source_comparison.png>)／[SVG](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/figures/03_three_stage_source_comparison.svg>)：Replays published normalized D² blocks. Experimental and model inputs are not asserted identical; the associated source discusses n-dodecane ISS data and a distinct n-heptane numerical case.

圖與資料綁定SHA見 [figure_manifest.json](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/figures/figure_manifest.json>)。若view版本更新，圖的manifest也要對齊，不能把舊圖說當新資料驗收。

## 圖表解讀的必要條件

- 每圖同時保留target定義、units、sourceID/SHA、physicalPDFpage/figure、trialgroup及每series角色。
- LiquidD、opticalDf、sootluminosity、radiometeroutput與computedT分開；來源header寫Radiance(W)不自動建立W/(m²sr)的物理radiance、HRR或heatflux。
- 實驗與model各保留原x，時間s與t/d0²的s/mm²不混；未知時鐘/單位不由另一block借用。單位未核定的整組曲線不渲染物理圖，改提供raw座標表與unknown說明。
- Raw0/negative值保留sourcecells；censor/no-finiteendpoint或非物理光學讀值以pointnote/plot-onlymask呈現，不默改來源值。
- Sourceerrorbar/bound/uncertainty readout不混成獨立experimentalpoint；source估計與digitization uncertainty不同，不任設誤差通過門檻。
- 曲線接近只能表示特定來源/定義下的agreement；不證明獨立模型效度、機制唯一、設備安全或載人艙批准。

最終科學/投影狀態見 [獨立QA](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/qa/independent_physics_visualization_review.json>)。本文件沒有另跑模型、擬合或新增誤差分數。
