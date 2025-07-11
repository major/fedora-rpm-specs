# Generated by rust2rpm 27
%bcond check 1

%global crate coreutils

Name:           rust-coreutils
Version:        0.0.27
Release:        %autorelease
Summary:        coreutils ~ GNU coreutils reimplementation in Rust

License:        MIT
URL:            https://crates.io/crates/coreutils
Source:         %{crates_source}
# * Script to list available coreutils commands
Source1:        coreutils-ls-commands.sh
# Manually created patch for downstream crate metadata changes
# * drop uudoc, unneeded
# * allow up to rstest 0.23
# * enable feat_acl
# * TODO: enable unix
# * allow procfs 0.17
Patch:          coreutils-fix-metadata.diff
# * Fix seq tests that pass negative numbers
Patch2:         coreutils-fix-seq-neg-num-tests.diff

# leaf package, SIGABRT on compile
ExcludeArch:    %{ix86}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
coreutils ~ GNU coreutils (updated); implemented as universal (cross-platform) utils, written in Rust.}

%description %{_description}

%package     -n uutils-coreutils
Summary:        %{summary}
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# CC0-1.0
# ISC
# MIT
# MIT OR Apache-2.0
# MIT-0 OR Apache-2.0
# Unlicense OR MIT
License:        MIT AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND Apache-2.0 AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND ISC AND (MIT-0 OR Apache-2.0) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

# Fedora up to 40 and EPEL up to 9 has individual uu_* packages
# support upgrading Fedora from 40->42 and EL 9->10

%if 0%{?rhel} && 0%{?rhel} < 11
%global obsolete_uu_nvr 0.0.23-2

Obsoletes:      uu_cp < %{obsolete_uu_nvr}
Obsoletes:      uu_mkdir < %{obsolete_uu_nvr}
Obsoletes:      uu_mktemp < %{obsolete_uu_nvr}
Obsoletes:      uu_mv < %{obsolete_uu_nvr}
Obsoletes:      uu_whoami < %{obsolete_uu_nvr}
%endif

%if 0%{?fedora} && 0%{?fedora} < 43
%global obsolete_uu_nvr 0.0.23-5

Obsoletes:      uu_base32 < %{obsolete_uu_nvr}
Obsoletes:      uu_base64 < %{obsolete_uu_nvr}
Obsoletes:      uu_basename < %{obsolete_uu_nvr}
Obsoletes:      uu_basenc < %{obsolete_uu_nvr}
Obsoletes:      uu_cat < %{obsolete_uu_nvr}
Obsoletes:      uu_cksum < %{obsolete_uu_nvr}
Obsoletes:      uu_comm < %{obsolete_uu_nvr}
Obsoletes:      uu_cp < %{obsolete_uu_nvr}
Obsoletes:      uu_csplit < %{obsolete_uu_nvr}
Obsoletes:      uu_cut < %{obsolete_uu_nvr}
Obsoletes:      uu_date < %{obsolete_uu_nvr}
Obsoletes:      uu_dd < %{obsolete_uu_nvr}
Obsoletes:      uu_df < %{obsolete_uu_nvr}
Obsoletes:      uu_dir < %{obsolete_uu_nvr}
Obsoletes:      uu_dircolors < %{obsolete_uu_nvr}
Obsoletes:      uu_dirname < %{obsolete_uu_nvr}
Obsoletes:      uu_du < %{obsolete_uu_nvr}
Obsoletes:      uu_echo < %{obsolete_uu_nvr}
Obsoletes:      uu_env < %{obsolete_uu_nvr}
Obsoletes:      uu_expand < %{obsolete_uu_nvr}
Obsoletes:      uu_expr < %{obsolete_uu_nvr}
Obsoletes:      uu_factor < %{obsolete_uu_nvr}
Obsoletes:      uu_false < %{obsolete_uu_nvr}
Obsoletes:      uu_fmt < %{obsolete_uu_nvr}
Obsoletes:      uu_fold < %{obsolete_uu_nvr}
Obsoletes:      uu_hashsum < %{obsolete_uu_nvr}
Obsoletes:      uu_head < %{obsolete_uu_nvr}
Obsoletes:      uu_join < %{obsolete_uu_nvr}
Obsoletes:      uu_link < %{obsolete_uu_nvr}
Obsoletes:      uu_ln < %{obsolete_uu_nvr}
Obsoletes:      uu_ls < %{obsolete_uu_nvr}
Obsoletes:      uu_mkdir < %{obsolete_uu_nvr}
Obsoletes:      uu_mktemp < %{obsolete_uu_nvr}
Obsoletes:      uu_more < %{obsolete_uu_nvr}
Obsoletes:      uu_mv < %{obsolete_uu_nvr}
Obsoletes:      uu_nl < %{obsolete_uu_nvr}
Obsoletes:      uu_numfmt < %{obsolete_uu_nvr}
Obsoletes:      uu_od < %{obsolete_uu_nvr}
Obsoletes:      uu_paste < %{obsolete_uu_nvr}
Obsoletes:      uu_pr < %{obsolete_uu_nvr}
Obsoletes:      uu_printenv < %{obsolete_uu_nvr}
Obsoletes:      uu_printf < %{obsolete_uu_nvr}
Obsoletes:      uu_ptx < %{obsolete_uu_nvr}
Obsoletes:      uu_pwd < %{obsolete_uu_nvr}
Obsoletes:      uu_readlink < %{obsolete_uu_nvr}
Obsoletes:      uu_realpath < %{obsolete_uu_nvr}
Obsoletes:      uu_rm < %{obsolete_uu_nvr}
Obsoletes:      uu_rmdir < %{obsolete_uu_nvr}
Obsoletes:      uu_seq < %{obsolete_uu_nvr}
Obsoletes:      uu_shred < %{obsolete_uu_nvr}
Obsoletes:      uu_shuf < %{obsolete_uu_nvr}
Obsoletes:      uu_sleep < %{obsolete_uu_nvr}
Obsoletes:      uu_sort < %{obsolete_uu_nvr}
Obsoletes:      uu_split < %{obsolete_uu_nvr}
Obsoletes:      uu_sum < %{obsolete_uu_nvr}
Obsoletes:      uu_tac < %{obsolete_uu_nvr}
Obsoletes:      uu_tail < %{obsolete_uu_nvr}
Obsoletes:      uu_tee < %{obsolete_uu_nvr}
Obsoletes:      uu_test < %{obsolete_uu_nvr}
Obsoletes:      uu_touch < %{obsolete_uu_nvr}
Obsoletes:      uu_tr < %{obsolete_uu_nvr}
Obsoletes:      uu_true < %{obsolete_uu_nvr}
Obsoletes:      uu_truncate < %{obsolete_uu_nvr}
Obsoletes:      uu_tsort < %{obsolete_uu_nvr}
Obsoletes:      uu_unexpand < %{obsolete_uu_nvr}
Obsoletes:      uu_uniq < %{obsolete_uu_nvr}
Obsoletes:      uu_unlink < %{obsolete_uu_nvr}
Obsoletes:      uu_vdir < %{obsolete_uu_nvr}
Obsoletes:      uu_wc < %{obsolete_uu_nvr}
Obsoletes:      uu_whoami < %{obsolete_uu_nvr}
Obsoletes:      uu_yes < %{obsolete_uu_nvr}
%endif

%description -n uutils-coreutils %{_description}

%files       -n uutils-coreutils
%license LICENSE
%license LICENSE.dependencies
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc DEVELOPMENT.md
%doc README.md
%{_bindir}/uutils-coreutils
%{_bindir}/uu_*
%{_mandir}/man1/*
%{bash_completions_dir}/*
%{fish_completions_dir}/*
%{zsh_completions_dir}/*

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# coreutils-ls-commands.sh script
cp -p %{SOURCE1} .

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
mkdir -p data/man/man1
mkdir -p data/completions/{bash,fish,zsh}

for utility in $(./coreutils-ls-commands.sh target/rpm/coreutils); do
  target/rpm/coreutils manpage $utility > data/man/man1/uu_${utility}.1
  for s in bash zsh; do
    target/rpm/coreutils completion $utility $s > data/completions/$s/uu_${utility}
  done
  target/rpm/coreutils completion $utility fish > data/completions/fish/uu_${utility}.fish
done
target/rpm/coreutils manpage coreutils > data/man/man1/uutils-coreutils.1
for s in bash zsh; do
  target/rpm/coreutils completion coreutils $s > data/completions/$s/uutils-coreutils
done
target/rpm/coreutils completion coreutils fish > data/completions/fish/uutils-coreutils.fish


%install
%cargo_install
mv %{buildroot}/%{_bindir}/coreutils %{buildroot}/%{_bindir}/uutils-coreutils
for utility in $(./coreutils-ls-commands.sh target/rpm/coreutils); do
  ln -sr %{buildroot}%{_bindir}/uutils-coreutils  %{buildroot}%{_bindir}/uu_$utility
done
mkdir -p %{buildroot}%{_mandir}/man1
cp -p data/man/man1/* %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{fish_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
cp -p data/completions/bash/* %{buildroot}%{bash_completions_dir}/
cp -p data/completions/fish/* %{buildroot}%{fish_completions_dir}/
cp -p data/completions/zsh/* %{buildroot}%{zsh_completions_dir}/


%if %{with check}
%check
# * --test-threads 1: tests fail with permission denied error if run with too
#   many threads (currently not needed)
# * common::util::tests::test_compare_xattrs: operation not supported
# * test_chcon / test_runcon: SELinux not supported in mock
# * test_cp: operation not supported
# * test_df: needs an actual filesystem to test
# * test_du: expected sublink/symlink in output
# * test_ls: need block/char device
# * test_seq: tolerances too tight
# * test_sort: formatting differences with recent unicode-width versions
%ifarch s390x
# * test_od::test_suppress_duplicates: likely endianness issue
%endif
%{cargo_test -- -- %{shrink:
    --skip common::util::tests::test_compare_xattrs
    --skip test_chcon::
    --skip test_runcon::
    --skip test_cp::test_copy_dir_preserve_permissions
    --skip test_cp::test_copy_dir_preserve_permissions_inaccessible_file
    --skip test_cp::test_copy_through_dangling_symlink_no_dereference_permissions
    --skip test_cp::test_cp_debug_reflink_auto_sparse_always_non_sparse_file_with_long_zero_sequence
    --skip test_cp::test_cp_parents_2_dirs
    --skip test_cp::test_cp_parents_with_permissions_copy_dir
    --skip test_cp::test_cp_parents_with_permissions_copy_file
    --skip test_cp::test_cp_preserve_xattr
    --skip test_cp::test_cp_sparse_always_empty
    --skip test_cp::test_cp_sparse_always_non_empty
    --skip test_cp::test_preserve_hardlink_attributes_in_directory
    --skip test_cp::test_preserve_mode
    --skip test_df::test_file_column_width_if_filename_contains_unicode_chars
    --skip test_df::test_nonexistent_file
    --skip test_df::test_output_file_specific_files
    --skip test_df::test_output_mp_repeat
    --skip test_df::test_output_option_without_equals_sign
    --skip test_df::test_total_label_in_correct_column
    --skip test_df::test_type_option_with_file
    --skip test_du::test_du_dereference_args
    --skip test_du::test_du_no_dereference
    --skip test_ls::test_device_number
    --skip test_ls::test_ls_allocation_size
    --skip test_ls::test_ls_inode
    --skip test_ls::test_ls_long_format
    --skip test_ls::test_ls_long_formats
    --skip test_seq::test_count_down_floats
    --skip test_seq::test_float_precision_increment
    --skip test_seq::test_inf_width
    --skip test_seq::test_neg_inf_width
    --skip test_seq::test_separator_and_terminator_floats
    --skip test_seq::test_width_decimal_scientific_notation_increment
    --skip test_seq::test_width_decimal_scientific_notation_trailing_zeros_end
    --skip test_seq::test_width_decimal_scientific_notation_trailing_zeros_increment
    --skip test_seq::test_width_floats
    --skip test_seq::test_width_negative_zero_decimal_notation
    --skip test_seq::test_width_negative_zero_scientific_notation
%ifarch s390x
    --skip test_od::test_suppress_duplicates
%endif
    --skip test_sort::test_keys_closed_range
    --skip test_sort::test_keys_multiple_ranges
    --skip test_sort::test_keys_no_field_match
    --skip test_sort::test_keys_open_ended
}}
%endif
# check

%changelog
%autochangelog
