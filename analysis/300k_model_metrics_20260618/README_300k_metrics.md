# 300K qkhead model MAE/R2 summary

Source portable: `D:\OptimizationNewMLP\OptimizationNewMLP_original12_qmission_fixedpoint_mlp10_experimental_portable`

Dataset split sizes:

| model_type | n_train | n_val | n_test | n_total | epochs | batch_size | cx_weight | k_weight | promoted_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| common | 240000 | 30000 | 30000 | 300000 | 400 | 256 | 3 | 2.5 | best_combo |
| duck | 91520 | 11440 | 11440 | 114400 | 400 | 256 | 4 | 3 | best_combo |
| normal | 148480 | 18560 | 18560 | 185600 | 400 | 256 | 3 | 2 | best_combo |

Test metrics for paper:

| Model | Output | R2_test | MAE_test | RMSE_test |
| --- | --- | --- | --- | --- |
| common | cx | 0.997889 | 0.000622118 | 0.00129012 |
| common | cy | 0.999477 | 0.0102181 | 0.0148586 |
| common | mz_ref | 0.998447 | 0.0384025 | 0.0582619 |
| common | mx_beta | 0.997209 | 4.81337e-05 | 6.99156e-05 |
| common | my_beta | 0.97724 | 0.000140126 | 0.000571699 |
| common | K | 0.999252 | 0.341074 | 0.467331 |
| normal | cx | 0.997747 | 0.000630151 | 0.00131893 |
| normal | cy | 0.999481 | 0.010345 | 0.0151957 |
| normal | mz_ref | 0.998826 | 0.0275397 | 0.0422372 |
| normal | mx_beta | 0.998262 | 4.25843e-05 | 6.14991e-05 |
| normal | my_beta | 0.980027 | 0.000118736 | 0.000503882 |
| normal | K | 0.999285 | 0.355903 | 0.484866 |
| duck | cx | 0.997505 | 0.000608186 | 0.0014087 |
| duck | cy | 0.999361 | 0.0107677 | 0.0157581 |
| duck | mz_ref | 0.998895 | 0.0389516 | 0.0585533 |
| duck | mx_beta | 0.996767 | 3.25253e-05 | 5.17744e-05 |
| duck | my_beta | 0.976786 | 0.000163352 | 0.000647503 |
| duck | K | 0.999419 | 0.274771 | 0.369391 |

Note: MAE values are in the native units of each aerodynamic output; do not average MAE across outputs as a physical score.
