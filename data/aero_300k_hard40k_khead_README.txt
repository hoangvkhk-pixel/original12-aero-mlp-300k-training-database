300k Aerodynamic Dataset Export

Source CSV: aero_labeled_v2_300k_hard40k_khead.csv
Rows exported: 300000
Status filter: status == ok
Missing-value filter: rows with NaN in required columns were removed
Data type in .npy files: float32

Saved files
- aero_300k_hard40k_khead_input.npy: input matrix with shape (300000, 20)
- aero_300k_hard40k_khead_output.npy: output matrix with shape (300000, 6)
- aero_300k_hard40k_khead_input_output.npy: concatenated [input | output] matrix with shape (300000, 26)
- aero_300k_hard40k_khead_input_columns.txt: input column names in saved order
- aero_300k_hard40k_khead_output_columns.txt: output column names in saved order
- aero_300k_hard40k_khead_input_output_columns.txt: combined column names in saved order

Input columns and value ranges
- f_aspect: min=4.00011, max=15
- f_sweep: min=5.41513e-05, max=44.9993
- f_taper: min=1, max=3
- f_twist: min=-4.99999, max=4.99998
- a_aspect: min=3.80018, max=15
- a_sweep: min=-44.9999, max=44.999
- a_taper: min=1.00002, max=3
- a_twist: min=-4.99997, max=4.99998
- a_x_loc: min=2.00001, max=5.99999
- a_S_rel: min=0.200001, max=0.799999
- v_aspect: min=2.00001, max=3.99999
- v_S_rel: min=0.0500001, max=0.3
- scheme_fuse: min=0, max=1
- scheme_vertical: min=0, max=1
- a_dihedral_mag: min=0, max=49.9997
- S_ref: min=1.00003, max=49.9999
- V: min=30.0006, max=89.9991
- H: min=200.009, max=4999.91
- alpha: min=-20, max=19.9997
- delta: min=-4.99995, max=4.99998

Output columns and value ranges
- cx: min=0.00807614, max=0.282744
- cy: min=-1.81256, max=2.01209
- mz_ref: min=-9.39263, max=8.52555
- mx_beta: min=-0.009456, max=0.009408
- my_beta: min=-0.024732, max=0.08725
- K: min=-44.7656, max=33.8286

Input column order
- f_aspect
- f_sweep
- f_taper
- f_twist
- a_aspect
- a_sweep
- a_taper
- a_twist
- a_x_loc
- a_S_rel
- v_aspect
- v_S_rel
- scheme_fuse
- scheme_vertical
- a_dihedral_mag
- S_ref
- V
- H
- alpha
- delta

Output column order
- cx
- cy
- mz_ref
- mx_beta
- my_beta
- K

Combined column order
- f_aspect
- f_sweep
- f_taper
- f_twist
- a_aspect
- a_sweep
- a_taper
- a_twist
- a_x_loc
- a_S_rel
- v_aspect
- v_S_rel
- scheme_fuse
- scheme_vertical
- a_dihedral_mag
- S_ref
- V
- H
- alpha
- delta
- cx
- cy
- mz_ref
- mx_beta
- my_beta
- K
