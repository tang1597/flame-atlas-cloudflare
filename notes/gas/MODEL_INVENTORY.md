# 氣體固定模型、原式與資料比較

所有係數保持來源固定。原始量測、來源分析、表格與圖上讀值各自保留；沒有新擬合。

## SPICE-PUBLISHED-EQ7

Axial luminous flame length at incipient soot emission (mm)

```text
Lsp_mm=Af_mixture*(d_mm)^a*(Uair_cm_s)^b
```

- 展示程式：`producer.py`
- 數學核心：`fixed_models.py`（僅可執行的固定模型）
- 狀態：runnable
- 分數身份：same_source_reproduction
- 模型全群R²：0.8997756724470198（None為N/A；非安全分數）
- 限制：Five independent source mixture constants; no shared fitted dilution adjustment is introduced.；Fuel flow was manually adjusted to find each smoke point; this is not a fixed-fuel-flow flame-length predictor.；No prediction at zero coflow, for methane, or at new pressure/oxygen/gravity conditions.；Nozzle and flow controls are restricted to actually represented mixture/nozzle groups and their observed coflow intervals; this does not establish a full joint safety envelope.；55source records are indexed; seven remain excluded for prior calibration-provenance reasons, not their residual size.；Published author uncertainties are estimates, not calibrated model prediction intervals.；direct_PSI107_ISS_source_campaign；published same-campaign correlation replay against original source-reduced measurements

## BRE-MARKAN-C2-RELATED

Computed stoichiometric-sheet height compared descriptively with source visible-tip height (mm)

```text
D_model=k/(rho*cp); Pe=M_author/(4*pi*c*rho*D_model)
Z(xi,tau)=[1-exp(Pe*(atan(xi)-pi/2))]/[1-E0] * erfc((xi-xi0)/(2*sqrt(tau)))
Solve Z=Y_O2/(S*Y_F_b+Y_O2); height_mm=c*xi*1000
M_author includes the original factor2; thermal diffusivity is not inferred from target height.
```

- 展示程式：`producer.py`
- 數學核心：`fixed_models.py`（僅可執行的固定模型）
- 狀態：runnable
- 分數身份：same-source fixed author numerical example with source-analyzed table and qualified figure comparators
- 模型全群R²：None（None為N/A；非安全分數）
- 限制：One fully specified same-source example, not an independently validated ISS flight architecture.；Source Table3.2 lists21.7mm; independent Fig5.13 readout is25-27mm. Neither comparator is selected based on closeness to the model.；Modeled stoichiometric sheet is not directly measured by the visible highest-tip method.；Model starts at the burner while the experiment was ignited under1g before release; no time shift is fitted.；Source script32C and tables32.9C remain distinct; fixed properties are not pressure-corrected.；The original factor2 model mass flow is not relabeled as measured single-face meter flow.；Eq5.90 heat-flux extension with these constants does not reproduce the source Fig5.11 flux curves; closure linkage remains unresolved.；related_ground_short_drop_BRE_program_not_PSI20_ISS_raw_trial；same-source fixed author numerical example with source-analyzed table and qualified figure comparators

## EARTH-ROPER-RELATED

Legacy-model stoichiometric length versus qualified optical closure proxy (mm)

```text
L_mm=Q_total_mm3_s/[4*pi*D0_mm2_s*ln(1+1/S)]*(T0_legacy/Tf_characteristic)^exponent
Q uses source component mass flow, component mole fraction and actual ambient ideal-gas conversion.
NDF S=nu*X_CH4/X_O2; IDF S=X_O2/(nu*X_CH4).
```

- 展示程式：`producer.py`
- 數學核心：`fixed_models.py`（僅可執行的固定模型）
- 狀態：runnable
- 分數身份：fixed previously calibrated correlation compared with qualified source-figure optical proxies
- 模型全群R²：None（None為N/A；非安全分數）
- 限制：Legacy D0/T0/Tf parameters came from prior calibration, not independently measured flame temperature or pure first-principles constants.；The extended alpha model was calibrated on the current287cases and is not substituted.；Both author dashed annotation and restricted grayscale readout remain separate.；NDF has a stronger near-base grayscale feature; its closure ROI is not the global grayscale maximum. IDF has a broad plateau.；Reading bounds are not experimental confidence intervals; no favored endpoint or error gate is chosen.；These methane ground jets are related literature, not FlameDesign spherical burner flight records or Earth-to-space validation.；related_ground_coflow_jet_not_PSI10_spherical_or_ISS_measurement；fixed previously calibrated correlation compared with qualified source-figure optical proxies

## SHUTTLE-STILLAIR-IDEAL-WIDTH

Maximum FULL luminous flame diameter (mm), compared with ideal flame-sheet maximum diameter; not radius or full contour

```text
w_max * Z_st / d = 9/16; therefore w_max = (9/16) * d / Z_st. d and w_max in mm. Inputs use source Table1 nozzle diameter and stoichiometric mixture fraction only. Luminous length, mass flow and pressure are not predictors in this ideal width law.
```

- 展示程式：`producer.py`
- 數學核心：`fixed_models.py`（僅可執行的固定模型）
- 狀態：runnable
- 分數身份：same_source_reproduction
- 模型全群R²：0.5064696499327288（None為N/A；非安全分數）
- 限制：Equal species diffusivities, constant properties, negligible radiation and ideal nonbuoyant boundary-layer approximation. The original source states these assumptions cannot all be satisfied by practical laminar flames.；Source Z_st describes the source burner fluid/ambient composition; it is not a material constant transferable to arbitrary oxygen fraction or habitat atmosphere.；The model predicts one constant diameter per fuel/nozzle cohort, while the observed luminous diameter varies across source pressure and flow conditions. Cohort scores retain this failure.；No new luminous-width calibration is made. The source empirical width factors are not used. A theoretical stoichiometric sheet is not a directly measured luminous chemical boundary.；Original published numeric table is available; original image frames and per-point uncertainty are not supplied. This comparison is not an independent held-out campaign or a full-shape validation.；Source Table1 Test17E velocity1690mm/s conflicts with body range1630mm/s; both are preserved in the source ledger and this velocity is unused by Eq3.；related_NASA_shuttle_flight_still_air_not_SPICE_or_SLICE_raw_campaign；Fixed ideal source width law versus original published processed numeric luminous-width table; no newly estimated coefficient

## READINESS-PSI-106

SLICE geometry (inputs missing)

```text
原文方程／模型參見MODEL_INVENTORY；本次尚未閉合
```

- 展示程式：`尚未有本次可執行的閉合重現`
- 數學核心：`fixed_models.py`（僅可執行的固定模型）
- 狀態：未執行／缺閉合輸入
- 分數身份：來源就緒度盤點，不是數值預測
- 模型全群R²：None（None為N/A；非安全分數）
- 限制：Paper-digitized scalar geometry exists, but no closed source-fixed L/R model can be forward-compared fairly.；Full MC-Smooth solver, chemistry/transport/radiation and matched boundary conditions；Original numeric geometry and trial P/O2/T; measured liftoff for lifted flames

## READINESS-PSI-10

FlameDesign spherical flames (inputs missing)

```text
原文方程／模型參見MODEL_INVENTORY；本次尚未閉合
```

- 展示程式：`尚未有本次可執行的閉合重現`
- 數學核心：`fixed_models.py`（僅可執行的固定模型）
- 狀態：未執行／缺閉合輸入
- 分數身份：來源就緒度盤點，不是數值預測
- 模型全群R²：None（None為N/A；非安全分數）
- 限制：Related Earth Roper jets are available separately; they do not close the actual spherical flame experiment.；Case-matched sphere geometry, reaction/transport/radiation closure and original measured geometry targets

## READINESS-PSI-20

BRE ISS flight cases (inputs missing)

```text
原文方程／模型參見MODEL_INVENTORY；本次尚未閉合
```

- 展示程式：`尚未有本次可執行的閉合重現`
- 數學核心：`fixed_models.py`（僅可執行的固定模型）
- 狀態：未執行／缺閉合輸入
- 分數身份：來源就緒度盤點，不是數值預測
- 模型全群R²：None（None為N/A；非安全分數）
- 限制：The ground-drop fixed example is separate from the flight raw-data comparison.；Matched flight geometry/flow/composition/property convention and original target trace

## READINESS-PSI-21

ACME CLD (inputs missing)

```text
原文方程／模型參見MODEL_INVENTORY；本次尚未閉合
```

- 展示程式：`尚未有本次可執行的閉合重現`
- 數學核心：`fixed_models.py`（僅可執行的固定模型）
- 狀態：未執行／缺閉合輸入
- 分數身份：來源就緒度盤點，不是數值預測
- 模型全群R²：None（None為N/A；非安全分數）
- 限制：No complete audited source-fixed scalar geometry comparison is presently joined.；Exact model/transport/chemistry version and compatible original flame target/case inputs

## READINESS-PSI-22

E-FIELD Flames (inputs missing)

```text
原文方程／模型參見MODEL_INVENTORY；本次尚未閉合
```

- 展示程式：`尚未有本次可執行的閉合重現`
- 數學核心：`fixed_models.py`（僅可執行的固定模型）
- 狀態：未執行／缺閉合輸入
- 分數身份：來源就緒度盤點，不是數值預測
- 模型全群R²：None（None為N/A；非安全分數）
- 限制：Nominal E-field descriptors and observations do not constitute a closed flame-shape or suppression predictor.；Local field/charge/flow/chemical and thermal closure with paired measured flame response

## READINESS-PSI-23

s-Flame (inputs missing)

```text
原文方程／模型參見MODEL_INVENTORY；本次尚未閉合
```

- 展示程式：`尚未有本次可執行的閉合重現`
- 數學核心：`fixed_models.py`（僅可執行的固定模型）
- 狀態：未執行／缺閉合輸入
- 分數身份：來源就緒度盤點，不是數值預測
- 模型全群R²：None（None為N/A；非安全分數）
- 限制：Published moving-front conservation equations require full closure; measured front speed cannot become an independent predictor of itself.；Chemistry, transport, radiation, initial/boundary fields and independent front history

## READINESS-PSI-159

CFI-G (inputs missing)

```text
原文方程／模型參見MODEL_INVENTORY；本次尚未閉合
```

- 展示程式：`尚未有本次可執行的閉合重現`
- 數學核心：`fixed_models.py`（僅可執行的固定模型）
- 狀態：未執行／缺閉合輸入
- 分數身份：來源就緒度盤點，不是數值預測
- 模型全群R²：None（None為N/A；非安全分數）
- 限制：Event-timing recurrence or source descriptors do not establish a general continuous geometry or ignition/extinction predictor.；Case-linked original geometry/transition data and a complete fixed physical forward closure

## READINESS-PSI-60

SPICE secondary analysis (inputs missing)

```text
原文方程／模型參見MODEL_INVENTORY；本次尚未閉合
```

- 展示程式：`尚未有本次可執行的閉合重現`
- 數學核心：`fixed_models.py`（僅可執行的固定模型）
- 狀態：未執行／缺閉合輸入
- 分數身份：來源就緒度盤點，不是數值預測
- 模型全群R²：None（None為N/A；非安全分數）
- 限制：This reuses SPICE observations and is not an independent flight experiment or extra validation set.；A separately defined original target/model pair not duplicating the source SPICE campaign

## SPICE-PUBLISHED-EQ7 分組誤差

整體與每個分組均保留；負R²不隱藏，R²≥0.85只是貼合門檻，不表示獨立驗證。

### overall

| 來源群 | 筆數 | R² | MAE mm | RMSE mm | 身份 |
| --- | --- | --- | --- | --- | --- |
| 尚未取得／不適用；尚未取得／不適用 | 48 | 0.8997756724470198 | 5.488593318028182 | 7.163166666607282 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |

### by_mixture

| 來源群 | 筆數 | R² | MAE mm | RMSE mm | 身份 |
| --- | --- | --- | --- | --- | --- |
| Ethylene；尚未取得／不適用 | 6 | 0.8389381034689878 | 7.1431778229953125 | 8.618026905904095 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| Propane；尚未取得／不適用 | 6 | 0.7704826467596796 | 7.811801553628086 | 8.742629810253963 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| 75 % Propylene；尚未取得／不適用 | 10 | 0.7067181456148782 | 4.0140819238364 | 5.559338843152119 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| 50 % Propylene；尚未取得／不適用 | 4 | 0.9309468996269441 | 1.695167405852291 | 2.2926432220490396 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| Propylene；尚未取得／不適用 | 22 | 0.6410803898848911 | 5.763687006538145 | 7.4730266573983455 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |

### by_nozzle

| 來源群 | 筆數 | R² | MAE mm | RMSE mm | 身份 |
| --- | --- | --- | --- | --- | --- |
| 尚未取得／不適用；1.6002 | 28 | 0.9262778457604649 | 3.7431989082342776 | 4.966777132510786 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| 尚未取得／不適用；0.762 | 16 | 0.920634065943256 | 7.4648749391389195 | 8.257706582148536 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| 尚未取得／不適用；0.4064 | 4 | -1.6858411090056769 | 9.801227702142565 | 13.049539560745524 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |

### by_mixture_and_nozzle

| 來源群 | 筆數 | R² | MAE mm | RMSE mm | 身份 |
| --- | --- | --- | --- | --- | --- |
| Ethylene；1.6002 | 5 | 0.7552570996980558 | 5.3225959951618735 | 6.0280508445628564 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| Ethylene；0.762 | 1 | 尚未取得／不適用 | 16.246086962162508 | 16.246086962162508 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| Propane；1.6002 | 3 | 0.30440031704172354 | 7.592338475455527 | 8.867583822791477 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| Propane；0.762 | 3 | 0.753452159614235 | 8.031264631800644 | 8.615863807190163 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| 75 % Propylene；1.6002 | 6 | 0.7017884135591169 | 2.9810753165841533 | 4.719555023871411 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| 75 % Propylene；0.762 | 4 | 0.6007294986678318 | 5.563591834714771 | 6.622259546214194 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| 50 % Propylene；1.6002 | 4 | 0.9309468996269441 | 1.695167405852291 | 2.2926432220490396 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| Propylene；1.6002 | 10 | 0.4079332365398478 | 3.075245250546974 | 3.44193752634319 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| Propylene；0.762 | 8 | -0.8585882268594729 | 7.105468853724899 | 7.322768712599026 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |
| Propylene；0.4064 | 4 | -1.6858411090056769 | 9.801227702142565 | 13.049539560745524 | Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score. |

## SHUTTLE-STILLAIR-IDEAL-WIDTH 分組誤差

整體與每個分組均保留；負R²不隱藏，R²≥0.85只是貼合門檻，不表示獨立驗證。

### overall

| 來源群 | 筆數 | R² | MAE mm | RMSE mm | 身份 |
| --- | --- | --- | --- | --- | --- |
| 尚未取得／不適用；尚未取得／不適用 | 21 | 0.5064696499327288 | 1.7939697862471002 | 2.1114878258176053 | Fixed ideal maximum-width prediction compared with original published processed luminous-width table; no new calibration, held-out validation or safety claim. |

### by_fuel_and_nozzle

| 來源群 | 筆數 | R² | MAE mm | RMSE mm | 身份 |
| --- | --- | --- | --- | --- | --- |
| C2H4；1.6 | 10 | -1.0113193625437793 | 0.9705660377358489 | 1.2000436090331659 | Fixed ideal maximum-width prediction compared with original published processed luminous-width table; no new calibration, held-out validation or safety claim. |
| C2H4；2.7 | 4 | -17.220384470249936 | 3.0547169811320742 | 3.1421602178782435 | Fixed ideal maximum-width prediction compared with original published processed luminous-width table; no new calibration, held-out validation or safety claim. |
| C3H8；1.6 | 7 | -8.240062240701176 | 2.2498338870431884 | 2.382443752446965 | Fixed ideal maximum-width prediction compared with original published processed luminous-width table; no new calibration, held-out validation or safety claim. |

## 來源方程 FD-ZST

Stoichiometric mixture-fraction design

```text
Zst=[1+YF_inf*WO*nuO/(YO_inf*WF*nuF)]^(-1)
```

- 物理角色：composition_bookkeeping
- 來源：title: Science Requirements Document for FLAME DESIGN；edition: Version1.3, April1,2010；publication_doi: 尚未確認；ntrs_id: 尚未確認；official_url: https://psi.nasa.gov/physci/repo/data/investigations/PSI-10；local_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\其他研究文件_正文類型待確認\第一批下載\PSI-10_ACME_Flame Design\Science Documents\PSI-10_Science Documents_SRD_ACMEFlameDesign.pdf；sha256: e783fc0da3d388b567654c109b2595a5a74218de6ccd641241f13b091a5448eb；physical_pdf_pages: 8；equation_numbers: 1.1；1.2；locator: 尚未確認；file_exists_now: True；sha256_verified_now: True；audit_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase5_shared_document_review\role_D\psi10_author_models.json；audit_sha256: db06d5e229f3eb13a5196d78deb20fd647d19f660984c58bddb98ade51d8a5c9；verification_scope: Reuse exact earlier source equation/page/visual audit and recheck source bytes; no new model execution or equation repair
- 閉合／缺件：closed_given_composition_basis；Exact species/mole-to-mass conventions and time history for RAMP cases；Existingexactsourceledger,notanewfit/validatedfullflame/safetyclassifier.

## 來源方程 FD-SPHERICAL-TRANSPORT

Transient spherical reacting mass/energy/species model

```text
partial_t rho+r^(-2)*partial_r(r^2*rho*u)=0; energy/species/radiation and burner-flux conditions are source Eqs1.6-1.9 (not replaced by a generic F)
```

- 物理角色：geometry
- 來源：title: Science Requirements Document for FLAME DESIGN；edition: Version1.3, April1,2010；publication_doi: 尚未確認；ntrs_id: 尚未確認；official_url: https://psi.nasa.gov/physci/repo/data/investigations/PSI-10；local_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\其他研究文件_正文類型待確認\第一批下載\PSI-10_ACME_Flame Design\Science Documents\PSI-10_Science Documents_SRD_ACMEFlameDesign.pdf；sha256: e783fc0da3d388b567654c109b2595a5a74218de6ccd641241f13b091a5448eb；physical_pdf_pages: 16；17；equation_numbers: 1.5；1.6；1.7；1.8；1.9；locator: 尚未確認；file_exists_now: True；sha256_verified_now: True；audit_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase5_shared_document_review\role_D\psi10_author_models.json；audit_sha256: db06d5e229f3eb13a5196d78deb20fd647d19f660984c58bddb98ade51d8a5c9；verification_scope: Reuse exact earlier source equation/page/visual audit and recheck source bytes; no new model execution or equation repair
- 閉合／缺件：requires_missing_chemistry_transport_radiation_and_initial_boundary_files；exactmechanism/transport/radiationfiles and versionmatched code；run-specificT/initialfields/wallhistory/burnerboundary and RAMPtimehistory；measuredtime-aligned radius/temperature outputs with endpoint/reductionuncertainty；Existingexactsourceledger,notanewfit/validatedfullflame/safetyclassifier.

## 來源方程 FD-A10-VIBRATION

Source vibration-amplitude requirement

```text
A/g <= 0.007225 * (m_g_s / rf_mm^2) * (Tinf_K + 0.5*Tf_K) / (1-Tinf_K/Tf_K)
```

- 物理角色：transport_diagnostic
- 來源：title: Science Requirements Document for FLAME DESIGN；edition: Version1.3, April1,2010；publication_doi: 尚未確認；ntrs_id: 尚未確認；official_url: https://psi.nasa.gov/physci/repo/data/investigations/PSI-10；local_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\其他研究文件_正文類型待確認\第一批下載\PSI-10_ACME_Flame Design\Science Documents\PSI-10_Science Documents_SRD_ACMEFlameDesign.pdf；sha256: e783fc0da3d388b567654c109b2595a5a74218de6ccd641241f13b091a5448eb；physical_pdf_pages: 37；38；39；equation_numbers: A1-A10；locator: 尚未確認；file_exists_now: True；sha256_verified_now: True；audit_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase5_shared_document_review\role_D\psi10_author_models.json；audit_sha256: db06d5e229f3eb13a5196d78deb20fd647d19f660984c58bddb98ade51d8a5c9；verification_scope: Reuse exact earlier source equation/page/visual audit and recheck source bytes; no new model execution or equation repair
- 閉合／缺件：conditional_on_supplied_flame_geometry_temperature；；Existingexactsourceledger,notanewfit/validatedfullflame/safetyclassifier.

## 來源方程 BRE-L17-FLASH

Low-burning-rate flash threshold approximation

```text
m_ig_LFL_pp~=hc*(Tf-T0)/Delta_hc; Nu_D=hc*D/k=0.43+0.60*Ra_D^(1/4)
```

- 物理角色：ignition_flux
- 來源：title: Study of ignition and extinction of small-scale fires in experiments with an emulating gas burner；edition: Fire Safety Journal 87 (2017) 18-24; author-hosted publisher PDF; seven physical pages；publication_doi: 10.1016/j.firesaf.2016.11.003；ntrs_id: 尚未確認；official_url: https://terpconnect.umd.edu/~pbs/2017%20Lundstrom%20et%20al.%20FSJ.pdf；local_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase5_shared_document_review\role_D\assets\Lundstrom2017_BRE_ignition_extinction_FSJ.pdf；sha256: 568b600aecd435d71b8784a437b5c7aa12561d9b3d04f9283b08b466daded682；physical_pdf_pages: 3；4；equation_numbers: 2；3；locator: 尚未確認；file_exists_now: True；sha256_verified_now: True；audit_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase5_shared_document_review\role_D\psi20_author_models.json；audit_sha256: 6017a2546331aeef4fdc9fb22d5bde24702fadb13e1a578beb9ae1a0ce479318；verification_scope: Reuse exact earlier source equation/page/visual audit and recheck source bytes; no new model execution or equation repair
- 閉合／缺件：closed_for_published_source_assumptions；；Existingexactsourceledger,notanewfit/validatedfullflame/safetyclassifier.

## 來源方程 BRE-MARKAN-TRANSIENT

Mixture-fraction transient flame-sheet height

```text
diffusivity: dif=k/(rho*cp), as original code; not inferred from measured flame growth; geometry: R=D/2/1000; c=R*sqrt(1-eps^2); xi0=eps/sqrt(1-eps^2); M_code: 2*m0*pi*R^2/1000 kg/s; retain exact author model convention, do not equate this doubled-model quantity with the physical one-face meter flow; Pe: M_code/(4*pi*c*rho*dif); Y_O2: X_O2*32/(X_O2*32+(1-X_O2)*28), author O2/N2 model-basis assumption; Y_F_b: 1-(Y_O2+S)*exp(Pe*(atan(xi0)-pi/2))/S; Z_flame: Y_O2/(S*Y_F_b+Y_O2); Z: (1-exp(Pe*(atan(xi)-pi/2)))/(1-exp(Pe*(atan(xi0)-pi/2)))*erfc((xi-xi0)/(2*sqrt(tau))); tau: dif*t/c^2; height_mm: c*xi_flame*1000 for the centerline, solving Z(xi,tau)=Z_flame
```

- 物理角色：geometry
- 來源：title: Development and analysis of a Burning Rate Emulator (BRE) for study in microgravity；edition: Exact local file identified by SHA256; see source audit for edition details；publication_doi: 10.13016/M2R49GD0F；ntrs_id: 尚未確認；official_url: https://drum.lib.umd.edu/bitstreams/6cb996b9-06ae-4413-9051-d65eec4a1637/download；local_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase7\role_D\assets\Markan2018_dissertation.pdf；sha256: 006c9492c99d0dba6afe43cb40b9bb052816410df01a67430d4c83a8b9a68e1d；physical_pdf_pages: 114；115；117；139；140；141；142；equation_numbers: 5.67；5.70；5.77；AppendixC.2；locator: 尚未確認；file_exists_now: True；sha256_verified_now: True；audit_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase7\role_D\root_case\source_contract.json；audit_sha256: 624d7d42515301322b858a9452be7d516939ddd2af81c032a797afde5f960b52；verification_scope: Reuse exact earlier source equation/page/visual audit and recheck source bytes; no new model execution or equation repair
- 閉合／缺件：closed_fixed_original_appendix_case；；Existingexactsourceledger,notanewfit/validatedfullflame/safetyclassifier.

## 來源方程 BRE-MARKAN-HEATFLUX

Published transient surface heat flux

```text
surface_flux_outward_W_m2: k/R*((Ts-Tinf)-d_hc*Y_O2/(S*cp))*(1/sqrt(pi*tau)+Pe*exp(-pi*Pe/2)/(1-exp(-pi*Pe/2))); surface_flux_into_burner_W_m2: -surface_flux_outward_W_m2; explicit coordinate-direction conversion, not a fitted sign correction; offset_flux: q_center/sqrt(1-(r_offset/R)^2); surface_average_into_flux: 2*q_center_into, integrating the published inverse-square-root disc distribution
```

- 物理角色：heat_balance
- 來源：title: Development and analysis of a Burning Rate Emulator (BRE) for study in microgravity；edition: Exact local file identified by SHA256; see source audit for edition details；publication_doi: 10.13016/M2R49GD0F；ntrs_id: 尚未確認；official_url: https://drum.lib.umd.edu/bitstreams/6cb996b9-06ae-4413-9051-d65eec4a1637/download；local_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase7\role_D\assets\Markan2018_dissertation.pdf；sha256: 006c9492c99d0dba6afe43cb40b9bb052816410df01a67430d4c83a8b9a68e1d；physical_pdf_pages: 119；120；equation_numbers: 5.89；5.90；locator: 尚未確認；file_exists_now: True；sha256_verified_now: True；audit_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase7\role_D\root_case\source_contract.json；audit_sha256: 624d7d42515301322b858a9452be7d516939ddd2af81c032a797afde5f960b52；verification_scope: Reuse exact earlier source equation/page/visual audit and recheck source bytes; no new model execution or equation repair
- 閉合／缺件：closed_conditional_fixed_case_but_output_alignment_unresolved；；Existingexactsourceledger,notanewfit/validatedfullflame/safetyclassifier.

## 來源方程 BRE-AUTH-SENSOR-ENERGY

Radiation/convection reference-to-embedded sensor balance

```text
q_abs=alpha*q_inc-epsilon*sigma*(T_s^4-T_ambient^4)-h*(T_s-T_ambient)=C*E; q_inc1=[C1*E1+epsilon1*sigma*(T_s1^4-T_ambient^4)+h1*(T_s1-T_ambient)]/alpha1; q_inc2=q_inc1 when each gauge is centered on the same radiant source; q_abs2=alpha2*q_inc2-epsilon2*sigma*(T_s2^4-T_ambient^4)-h2*(T_s2-T_copper2)=C2*E2; E2_pred=q_abs2_pred/C2
```

- 物理角色：heat_balance
- 來源：title: Using a Burning Rate Emulator (BRE) to Emulate Condensed Fuels and Study Pool Fire Behavior in1G；edition: UMD MS thesis,105physicalpages；publication_doi: 10.13016/3gfb-yhqp；ntrs_id: 尚未確認；official_url: https://drum.lib.umd.edu/items/d8167a16-6982-4945-a42b-716b18f2d1ec；local_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase4_earth_experiment_search\role_D\assets\Auth2019_BRE_1g_thesis.pdf；sha256: 22b0ccfa2c694978ce07c8dc4fea55ffb2be689bf27035a6c74b6cb62b5a2bb7；physical_pdf_pages: 26；27；28；82；83；equation_numbers: 2.1；2.4；2.5；2.6；Table2-1；locator: 尚未確認；file_exists_now: True；sha256_verified_now: True；audit_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase7\role_D\psi20_case\author_model.json；audit_sha256: d0e91e6cf8501f680affc08493f0c5edf4e22c47c65c46d81ec717756094fcee；verification_scope: Reuse exact earlier source equation/page/visual audit and recheck source bytes; no new model execution or equation repair
- 閉合／缺件：conditional_on_measured_thermal_states_and_author_sensor_calibration；；Existingexactsourceledger,notanewfit/validatedfullflame/safetyclassifier.

## 來源方程 BRE-DEHGHANI-SHAPE

Oblate-ellipsoidal flame height/base radius

```text
eq4_4: lambda=m_doubleprime/(4*k/(pi*c_p*R)); alpha_definition: alpha=S/Y_O_inf (not thermal diffusivity); eq4_18: x_f/R=tan{(pi/2)*[1+ln(alpha/(alpha+1))/lambda]}; eq4_19: r_f/R=sqrt(1+(x_f/R)^2); eq4_20: r_f/R=sqrt(1+c*(x_f/R)^2), c=0.35 is author empirical correction
```

- 物理角色：geometry
- 來源：title: PSI-20_Reports_Dissertation-PD-revised_.pdf；edition: Exact local file identified by SHA256; see source audit for edition details；publication_doi: 尚未確認；ntrs_id: 尚未確認；official_url: https://psi.nasa.gov/physci/repo/data/investigations/PSI-20；local_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\研究報告與書章\第一批下載\PSI-20_ACME BRE\Reports\PSI-20_Reports_Dissertation-PD-revised_.pdf；sha256: 2ada277f4accf3ff7dca0c4701609480a32c76141fe008d8253c341848b28cf0；physical_pdf_pages: 55；56；57；58；59；60；61；79；equation_numbers: 4.2；4.3；4.4；4.10；4.11；4.12；4.13；4.14；4.18；4.19；4.20；locator: 尚未確認；file_exists_now: True；sha256_verified_now: True；audit_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase5_shared_document_review\role_D\psi20_author_models.json；audit_sha256: 6017a2546331aeef4fdc9fb22d5bde24702fadb13e1a578beb9ae1a0ce479318；verification_scope: Reuse exact earlier source equation/page/visual audit and recheck source bytes; no new model execution or equation repair
- 閉合／缺件：blocked_source_property_units_and_case_binding；Exact k/cp unit convention: source prints65 and21.5g/(s m)；paired source-case oxygen mass fraction and flow；transient/property closure files；Existingexactsourceledger,notanewfit/validatedfullflame/safetyclassifier.

## 來源方程 BRE-AUTH-CALORIMETER

Porous-copper dynamic calorimeter reconstruction

```text
{'eq6': 'q_abs*A_total = C_Cu*dT/dt + epsilon*sigma*A_total*(T^4-T_inf^4) + h*A_Cu*(T-T_inf) + Q_g + Q_rod + Q_b', 'eq7': 'Q_g=m_dot_g*c_g*(T-T_0)', 'eq8': 'Q_rod=h_rod*A_h*(T-T_rod)', 'eq9': 'Q_b=h_0*A_total*(T-T_0)', 'eq18': 'q_abs*A_total = C_Cu*dT/dt + epsilon*sigma*A_total*(T^4-T_inf^4) + Q_g+Q_rod+Q_b', 'eq19': 'q_net=(C_Cu*dT/dt+Q_g+Q_rod+Q_b)/A_total'}
```

- 物理角色：heat_balance
- 來源：title: Emulation of condensed fuel flames with gaseous fuels supplied through a porous copper calorimeter；edition: Fire and Materials44:935–942,8-page publisher edition on author UMD host；publication_doi: 10.1002/fam.2896；ntrs_id: 尚未確認；official_url: https://terpconnect.umd.edu/~pbs/2020%20Auth%20et%20al.%20FAM.pdf；local_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase4_earth_experiment_search\role_D\assets\Auth2020_BRE_FAM.pdf；sha256: 52b0b7aaa14eb083222d1cbaba3379adf940f1e618b46aabdf0aa3181c97a953；physical_pdf_pages: 3；4；6；equation_numbers: 6；7；8；9；18；19；locator: 尚未確認；file_exists_now: True；sha256_verified_now: True；audit_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase5_shared_document_review\role_D\psi20_author_models.json；audit_sha256: 6017a2546331aeef4fdc9fb22d5bde24702fadb13e1a578beb9ae1a0ce479318；verification_scope: Reuse exact earlier source equation/page/visual audit and recheck source bytes; no new model execution or equation repair
- 閉合／缺件：requires_missing_temperature_history_and_geometry；matched T(t) and dt/timebase；full T_0 history/kernel and initial condition；T_rod(t)；flow and c_g matched to mixture；A_Cu/A_h geometric values；per-run calibration coefficients and source traces；Existingexactsourceledger,notanewfit/validatedfullflame/safetyclassifier.

## 來源方程 EFIELD-NOMINAL-E

Nominal imposed electric field

```text
Eave=-DeltaV_app/H
```

- 物理角色：transport_diagnostic
- 來源：title: Characterizing I-V Curves for Non-Premixed Methane Flames Stabilized on Different Burner Configurations；edition: ASGSR32ndAnnualMeeting,October26-29,2016;18-page Beamer presentation, not2017journalarticle；publication_doi: 尚未確認；ntrs_id: 尚未確認；official_url: https://psi.nasa.gov/physci/repo/data/investigations/PSI-22；local_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\簡報與海報\第一批下載\PSI-22_ACME E-FIELD Flames\Presentations\PSI-22_Presentations_Tinajero et al 2016 characterizing i-v curves for non-premixed methane flames.pdf；sha256: 71132d684969a4b6d15fbec694f2314e1c9edd86509a91bda1bb66c4c9167dcd；physical_pdf_pages: 6；equation_numbers: ；locator: Average Field Strength；file_exists_now: True；sha256_verified_now: True；audit_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase5_shared_document_review\role_D\psi22_author_models.json；audit_sha256: dc3a440cd58abba17c55862665ea7c96c09c64bfd0a69c4b49ae92920a3dcbe7；verification_scope: Reuse exact earlier source equation/page/visual audit and recheck source bytes; no new model execution or equation repair
- 閉合／缺件：closed_algebraic_condition_descriptor；；Existingexactsourceledger,notanewfit/validatedfullflame/safetyclassifier.

## 來源方程 SFLAME-MOVING-FRONT

Quasi-steady moving-front conservation

```text
{'mass': 'partial(mdot)/partial(x) + 2*(A/r)*rho*U_f = 0', 'energy': 'mdot*partial(T)/partial(x) - (1/c_p)*partial[A*lambda_g*partial(T)/partial(x)]/partial(x) + (A/c_p)*sum_k[rho*Y_k*V_k*c_p,k]*partial(T)/partial(x) + (A/c_p)*sum_k[omega_dot_k*h_k*W_k] = 0', 'species': 'mdot*partial(Y_k)/partial(x) + partial(rho*A*Y_k*V_k)/partial(x) - A*omega_dot_k*W_k = 0', 'mass_flux_definition': 'mdot = rho*(u-U_f)*A', 'spherical_area': 'A=4*pi*r^2', 'moving_coordinate_differential': 'dx=dr-U_f*dt'}
```

- 物理角色：geometry
- 來源：title: s-Flame SCR at NASA Glenn；edition: 20February2008; PI C.K.Law, Co-Is S.D.Tse and K.R.Sacksteder. Distinct from the2010SRD text document.；publication_doi: 尚未確認；ntrs_id: 尚未確認；official_url: 尚未確認；local_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\其他研究文件_正文類型待確認\第一批下載\PSI-23_ACME s-Flame\Science Documents\PSI-23_Science Documents_s-Flame SCR 200802.pdf；sha256: 2b93ce4409df9559af37cb4a319cc0536e77fb36abadaa4a68f18bff3b0a4c47；physical_pdf_pages: 34；equation_numbers: ；locator: printedslide33；file_exists_now: True；sha256_verified_now: True；audit_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase5_shared_document_review\role_D\root_author_models.json；audit_sha256: 946e9ff841023fff5a36d4a2f743c3ba4385841415b5adfc64bc9e9eb5036caf；verification_scope: Reuse exact earlier source equation/page/visual audit and recheck source bytes; no new model execution or equation repair
- 閉合／缺件：requires_missing_chemistry_transport_radiation_and_joined_boundaries；run_join；initial_fields；local_density_transport；reaction_thermochemistry_implementation；radiative_closure；Existingexactsourceledger,notanewfit/validatedfullflame/safetyclassifier.

## 來源方程 CFIG-CHAMBER-CALCULATOR

Original event-wise species inventory recurrence

```text
['Vfuel = R296 * GCF(SourceTable!P118)', 'b = IF(EventData!B296="Yes",1,0)', 'deltaV_i = nu_i * Vfuel * b; other incomingMFC branches produce zero in the original arithmetic from source blanks', 'V_i,next = V_i,carry_in + deltaV_i', 'x_i,next = V_i,next / SUM_j(V_j,next)']
```

- 物理角色：composition_bookkeeping
- 來源：title: cf9cba0abc20f3fd_PSI-159_Raw Data_Final ACME Chamber Calculator - 2021-03-09 to 2021-10-21.xlsx；edition: Exact local file identified by SHA256; see source audit for edition details；publication_doi: 尚未確認；ntrs_id: 尚未確認；official_url: https://psi-repo-prod.s3.amazonaws.com/psi-data/PSI-159/Raw%20Data/PSI-159_Raw%20Data_Final%20ACME%20Chamber%20Calculator%20-%202021-03-09%20to%202021-10-21.xlsx；local_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\補下載\PSI-159\Raw Data\cf9cba0abc20f3fd_PSI-159_Raw Data_Final ACME Chamber Calculator - 2021-03-09 to 2021-10-21.xlsx；sha256: f0bfe65050df7c12c33355452f093f5f8c478ac04cc5e7237abc5b281b3f32a6；physical_pdf_pages: ；equation_numbers: EventDataBX296:CH296；StoichTable；MFC/GCF；locator: Case21174C3/EventData296；file_exists_now: True；sha256_verified_now: True；audit_path: C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase7\role_C\mass_balance_reproduction.json；audit_sha256: 156505ace8e3bee3e8d417f7ab59f120cded0feea5f6178e5f64c96f6f4bb5a0；verification_scope: Reuse exact earlier source equation/page/visual audit and recheck source bytes; no new model execution or equation repair
- 閉合／缺件：closed_local_source_event_recurrence_given_cached_prior_inventory；；Existingexactsourceledger,notanewfit/validatedfullflame/safetyclassifier.
