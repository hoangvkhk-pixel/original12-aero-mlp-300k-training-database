# 300k Aerodynamic Database Manifest

Committed database artifact:

- `data/aero_300k_hard40k_khead_export.zip`

The zip contains the compact float32 NPY export:

- `aero_300k_hard40k_khead_input.npy`: `(300000, 20)`
- `aero_300k_hard40k_khead_output.npy`: `(300000, 6)`
- `aero_300k_hard40k_khead_input_output.npy`: `(300000, 26)`
- column-order text files for input, output, and combined matrices

Source raw CSV:

- `aero_labeled_v2_300k_hard40k_khead.csv`
- 300000 filtered rows
- not committed because the local file is about 136 MB, above GitHub's normal
  100 MB per-file limit

Related local raw CSV components, also not committed here:

- `aero_labeled_v2_normal_300k_hard40k_khead.csv`
- `aero_labeled_v2_duck_300k_hard40k_khead.csv`
- `aero_labeled_targeted_hard40k_v2.csv`

The committed NPY export is the reproducible training database for this repo.

