# 固體模型與閉合條件索引

可執行的固定公式、來源一致性比較、尚未閉合的方程分開。沒有新訓練或新R²。

## SOLID-PMMA-THIN-THERMAL

Vf=(2.34e-8 m²/s)×F_adb/τ_half；F_adb=4.89；τ_half=t_full/2

- 程式：`reproduce_solid_models.py`
- 狀態：runnable
- 限制：['Original numeric front-position/spread trajectories, exact trial IDs and per-point statistics', 'Case-specific proof of thermal-regime eligibility; low-flow radiation/high-flow kinetics are not modeled', 'F_adb and prefactor are fixed by source; no coefficient is estimated. Original numeric spread trajectories/trial IDs are missing. R2 N/A.']

## SOLID-PMMA-M8-SOURCE-VARIANTS

來源表速率對來源位置–時間斜率；M8雙面2mm×1.2cm；非新擬合

- 程式：`reproduce_solid_models.py`
- 狀態：runnable
- 限制：['Original position-time data and exact reduction-window definitions to resolve the10cm/s discrepancy', 'Physicalp65contains both processed spread table values and author regression slopes. This tool preserves their difference; source-published R2 is not new validation.']

## BASS-SIBAL-CORRELATION-REPLAY

width2cm: V_F[mm/s]=-0.20*U_inf[cm/s]+0.56; width1cm: V_F[mm/s]=-0.15*U_inf[cm/s]+0.07

- 程式：`reproduce_solid_models.py`
- 狀態：目前未執行／尚未閉合
- 限制：['Original image-derived numeric spread targets with same steady-flow segment', 'Exact source-fit point membership and geometry/flow sign mapping', 'Published width-specific signed-flow lines exist; no original numeric spread-target pair is joined in the local matrices. Missing target stays unavailable.']

## SOLID-PSI62-FGM-BLOCKED

PSI62 BASS flamelet/tomography model

- 程式：`reproduce_solid_models.py`
- 狀態：目前未執行／尚未閉合
- 限制：['Exact solver/manifold version and chemistry/transport files', 'Matched simulation/experimental trial, fields and boundary conditions', 'No complete verified manifold, chemistry, transport, boundary bundle or compatible numeric target pair. A generic PDE is not a reproduced model.']

## SAFFIRE-I-SEALED-ENERGY-BLOCKED

Saffire-I enclosure energy balance

- 程式：`reproduce_solid_models.py`
- 狀態：目前未執行／尚未閉合
- 限制：['Time-resolved inflow/outflow and leakage', 'Independent heat-release/burn history, wall heat transfer and radiation state', 'Related2012model is a sealed ground chamber; actual flight requires vent/leak, heat-release and heat-transfer closure. Conditional O2 diagnostic is a separate reconstruction, not a pressure/flame prediction.']

## SAFFIRE-II-SEALED-ENERGY-BLOCKED

Saffire-II material and enclosure data

- 程式：`reproduce_solid_models.py`
- 狀態：目前未執行／尚未閉合
- 限制：['Compatible numeric front position/time and source-bound thick-slab closure', 'Actual flow/vent and heat-release/heat-transfer histories', 'Reported burn duration is not a front-traverse time; no generic spread or pressure prediction is fabricated from it. Thick slab/rod/thin-sheet regimes remain separate.']

## SAFFIRE-III-SEALED-ENERGY-BLOCKED

Saffire-III enclosure data

- 程式：`reproduce_solid_models.py`
- 狀態：目前未執行／尚未閉合
- 限制：['Independent heat-release/burn history', 'Compatible sensor histories, vent flow and thermal boundaries', 'The sealed-chamber formula cannot be applied without actual ventilation, burn and thermal boundary inputs.']

## BRE-AUXILIARY-ONLY

BRE auxiliary material emulator

- 程式：`reproduce_solid_models.py`
- 狀態：目前未執行／尚未閉合
- 限制：['Exact matched geometry/flow/composition/pressure/property state', 'Calorimeter thermal/sensor definitions and material-boundary heat flux for transfer', 'Gas-emulator and calorimeter conventions require their own closure; command-off is not measured physical flow-off. No source constants are transferred to PMMA/SIBAL.']

## PMMA-ROD-BOUNDARY-REPLAY

BASS-II PMMA rod boundary and steady profile

- 程式：`reproduce_solid_models.py`
- 狀態：目前未執行／尚未閉合
- 限制：['Matched original stable/extinction numeric pairs with calibrated local velocity', 'Independent profile/temperature measurements and resolved heat-feedback closure', 'Eq6.1 coefficients are source-calibrated. Eq6.6-6.8 uses measured regression as input; it cannot independently predict that regression. Full Eq6.5 feedback closure/signs remain unresolved.']

## 文獻方程 B-MODEL-SEALED-2012

- 來源：SB-5c9badcc8f05 / None
- 角色：related_ground_sealed_chamber_model_not_executable_Saffire_flight_closure

```text
['dQ/dt = q_comb - q_rad - q_conv - q_cond', 'dQ/dt = C_v,g * d(n_g*T_g)/dt', 'C6H10O5 + 6 O2 -> 6 CO2 + 5 H2O', 'q_comb = 13.1e6 * oxygen_mass_consumption_rate', 'q_rad = a_P * V_f * sigma * (T_f^4 - T_w^4)', 'q_conv = h_w * A_w * (T_g - T_w)', 'Nu_L = h_w*L/lambda_g = 0.664 * Pr^(1/3) * Re_L^(1/2)', 'q_cond = lambda_g * (T_f - T_p) * A_f / s_f', 'q_rad approximately a_P * V_t * sigma * (T_g^4 - T_w^4)', 'P(t) = n_g(t)*R*T_g(t)/V_t']
```

- 缺輸入：Numerical a_P(T,CO2,H2O) closure and its implementation from reference4; explicitly selected gas-property functions/C_v,g; required wall temperature/geometry for the37L case; measured or fully prescribed per-case q_comb and combustion completeness. Present flight CSV/logs lack a complete independently measured input/output bundle.
- 適用限制：Unknown Cygnus free volume, distributed/ventilated mixing and heat/mole closure cannot be replaced by this sealed chamber model.

## 文獻方程 SAFFIRE-THIN-THERMAL-SCALING

- 來源：SB-ffe6664bb8a8 / physical4 Eqs2/6
- 角色：source approximate thin-solid explanation, not a universal fire-state predictor

```text
['V_f ≈ l_p h(T_f-T_p)/[rho_s c_s tau(T_p-T_o)]', 'V_f proportional to P^(1/2) l_p^(1/2) U_f^(1/2) (T_f-T_p)']
```

- 缺輸入：['matched net heat feedback and surface/gas states', 'kinetic/extinction closure', 'char/smoldering and geometry-specific transport']
- 適用限制：None

## 文獻方程 A20_dynamic_slug_energy

- 來源：SB-52b0b7aaa14e / [3, 4, 6]
- 角色：dynamic energy conservation and author-calibrated heat-flux reconstruction

```text
{'eq6': 'q_abs*A_total = C_Cu*dT/dt + epsilon*sigma*A_total*(T^4-T_inf^4) + h*A_Cu*(T-T_inf) + Q_g + Q_rod + Q_b', 'eq7': 'Q_g=m_dot_g*c_g*(T-T_0)', 'eq8': 'Q_rod=h_rod*A_h*(T-T_rod)', 'eq9': 'Q_b=h_0*A_total*(T-T_0)', 'eq18': 'q_abs*A_total = C_Cu*dT/dt + epsilon*sigma*A_total*(T^4-T_inf^4) + Q_g+Q_rod+Q_b', 'eq19': 'q_net=(C_Cu*dT/dt+Q_g+Q_rod+Q_b)/A_total'}
```

- 缺輸入：['matched T(t) and dt/timebase', 'full T_0 history/kernel and initial condition', 'T_rod(t)', 'flow and c_g matched to mixture', 'A_Cu/A_h geometric values', 'per-run calibration coefficients and source traces']
- 適用限制：Do not apply ground BRE2 constants to ISS BRE1 or corrected flight calorimeter.

## 文獻方程 A20_steady_burning_identity

- 來源：SB-52b0b7aaa14e / [5, 6]
- 角色：steady boundary energy balance / effective property definition

```text
{'eq14': 'm_F_doubleprime = q_net_doubleprime / L', 'eq15': 'q_net = q_flame_radiative_absorbed + q_flame_convective + q_external - epsilon*sigma*(T_s^4-T_inf^4)', 'eq16': 'q_abs = q_flame_radiative_absorbed + q_flame_convective', 'eq17': 'q_net = q_abs - epsilon*sigma*(T_s^4-T_inf^4), assuming q_external=0'}
```

- 缺輸入：Tables report m and source-computed L but not independent full q_net trace; reconstructing q_net=mL is an identity and does not validate a prediction.
- 適用限制：Tables report m and source-computed L but not independent full q_net trace; reconstructing q_net=mL is an identity and does not validate a prediction.

## 文獻方程 L17_flash_low_burning_rate

- 來源：SB-568b600aecd4 / [4]
- 角色：steady low-burning-rate stagnant-layer approximation with author fixed heat-transfer correlation

```text
{'eq2': 'm_ig_LFL_doubleprime ~= h_c*(T_f-T_0)/Delta_h_c', 'eq3': 'Nu_D=0.43+0.60*Ra_D^(1/4)', 'definitions': 'Nu_D=h_c*D/k; Ra_D=g*beta*DeltaT*D^3/(alpha*nu)'}
```

- 缺輸入：['Run-matched fuel/diluent composition and mixture heat of combustion for point-level comparison; the earlier source-fixed aggregate replay is available but is not independent trial-level validation.']
- 適用限制：None

## 文獻方程 L17_extinction_and_fire

- 來源：SB-568b600aecd4 / [5, 6]
- 角色：steady flame-temperature extinction approximation; fire-point transfer explicitly uncertain

```text
原式尚未完整轉錄，未執行
```

- 缺輸入：['tabulated exact mixture Y_F and independently defined Delta_h_c for each plotted point', 'numeric point-level critical mass flux and protocol repeats', 'matched fire-point surface T rather than extinction average', 'published source data behind Figs5/7; no digitization in this audit']
- 適用限制：None

## 文獻方程 D22_diffusive_transient_flame_position

- 來源：SB-2ada277f4acc / [55, 56, 57, 58, 59, 60, 61, 79]
- 角色：author analytical thin-sheet, constant-property, Le=1 oblate-ellipsoidal diffusion solution

```text
{'eq4_4': 'lambda=m_doubleprime/(4*k/(pi*c_p*R))', 'alpha_definition': 'alpha=S/Y_O_inf (not thermal diffusivity)', 'eq4_18': 'x_f/R=tan{(pi/2)*[1+ln(alpha/(alpha+1))/lambda]}', 'eq4_19': 'r_f/R=sqrt(1+(x_f/R)^2)', 'eq4_20': 'r_f/R=sqrt(1+c*(x_f/R)^2), c=0.35 is author empirical correction'}
```

- 缺輸入：['Unresolved printed k/cp units; verified SI value is null.', 'Run-matched oxygen mass fraction, actual gas mixture and selected flame-height definition.', 'Transient timebase and diffusivity for the erfc solution; empirical aspect correction and property choice are source-data dependent.']
- 適用限制：['flat porous disk idealized as one side of oblate ellipsoid', 'pure diffusion, zero-buoyancy approximation is regime assumption, not measured g=0', 'base radius mismatch; thesis prose on pp58/physical61 is internally mixed about direction, so retain figure and formula rather than assign universal bias', 'same original data inform property selection; any replication must carry that dependency']

## 文獻方程 D22_thermal_and_radiation_closure

- 來源：SB-2ada277f4acc / [59, 65, 66, 69, 71, 73, 76, 79]
- 角色：analytic convection plus author empirical radiation closure

```text
{'eq4_15': 'cp*(Tf-Tinf)=[cp*(Ts-Tinf)+Y_Fb*(1-Xr)*Delta_hc]/(alpha*Y_Fb+1)', 'eq4_16': 'q_c_avg=[4*k/(pi*R*cp)]*[lambda/(exp(lambda)-1)]*[(Delta_hc*(1-Xr)*Y_O_inf/S)-cp*(Ts-Tinf)]', 'eq4_37': 'Xr=0.0633*ln(Omega)+0.452', 'eq4_43': 'q_rr=epsilon_s*sigma*(Ts^4-Tinf^4), source epsilon_s=1'}
```

- 缺輸入：['k/cp units unresolved even after published-author-fulltext section7 corroboration; not silently rescaled', 'numeric exact Eq4.35/4.36 absorption/path-length closure and all source coefficients', 'matched cp/Ts/Tinf/mixture oxygen mass basis per row', 'independent heldout measurements separated from source correlation and property-selection cohort']
- 適用限制：['Xr/Tf/heatflux/L are computed quantities, distinct from radiometer/gauge measurements', 'fixed-correlation replication would not be blind first-principles validation', 'source p76 states flight calorimeter confidence lower because operation compromised and theoretical correction imposed; two-point arithmetic-average sensor heatflux is different spatial observable']

## 文獻方程 GUIDE22_chamber_balance

- 來源：SB-6187d07f3add / [8, 19, 20]
- 角色：source mass/species bookkeeping rather than kinetic reactor prediction

```text
原式尚未完整轉錄，未執行
```

- 缺輸入：['complete matched operation history and start inventory', 'calibrated MFC conversion factors by actual gas mixture', 'validated burn-fraction history', 'gas-species measurements for checking calculator, not supplied as analyzed GCIP concentration in this guide']
- 適用限制：['chamber composition is source-computed estimate, not measured per-run ambient record', 'CIR PT16/PT17 chamber pressure preferred to stale ACME PTA3', 'standard MFC0C/760torr and groundAlicat25C/1atm references differ; actual volumetric velocity requires state conversion']

## 文獻方程 SCR12_steady_energy_and_scaling

- 來源：SB-7de4c32c80fb / [4, 17, 18, 37, 41, 42, 43]
- 角色：2012 steady energy identity plus illustrative extinction scaling, not flight-validated forward model

```text
Source unnumbered formulas on specified pages; steady balance consistent with L=(q_flame-q_rr+q_external)/m and L_eff=L-(q_external-q_rr)/m. Complex extinction formula/geometry factor not implemented from text extraction.
```

- 缺輸入：['source geometric coefficient C_f and matched applicability', 'actual initial/chamber state and gas mixture', 'independent measured mass/heatflux for a chosen scaling case']
- 適用限制：['p43material-class outcomes computed from scaling; not observed individual material trials', 'p37L is reconstructed from measured quantities, not independent prediction', 'prototype ground morphology/property comparisons later published; editions not pooled as independent data']
