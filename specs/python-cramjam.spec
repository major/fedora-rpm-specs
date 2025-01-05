%bcond tests 1

Name:           python-cramjam
Version:        2.9.1
Release:        %autorelease
Summary:        Thin Python bindings to de/compression algorithms in Rust

# SPDX
License:        MIT
URL:            https://github.com/milesgranger/cramjam

%if !%{defined commit}

# This handles pre-release versioning:
%global srcversion %(echo '%{version}' | tr -d '~')
# Future PyPI sdists should not include benchmark data (some of which has
# complicated or unclear license status). See: “Consider excluding benchmarks
# from PyPI sdists” https://github.com/milesgranger/cramjam/issues/178
Source:         %{pypi_source cramjam %{srcversion}}

%else

%global srcversion %{commit}
# For snapshots, we must filter the source archive from GitHub using the script
# in Source1, since some of the benchmark data has complicated or unclear
# license status.
Source0:        cramjam-%{commit}-filtered.tar.gz
# ./get_source ${COMMIT} (or ${TAG})
Source1:        get_source

%endif

# Updates for Maturin 1.8: add a version key in the project metadata
# https://github.com/milesgranger/cramjam/pull/196
Patch:          %{url}/pull/196.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  tomcli
BuildRequires:  cargo-rpm-macros >= 24

%if %{with tests}
# These (along with some unwanted dependencies like linters) are listed in the
# dev extra in pyproject.toml.
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-xdist}
BuildRequires:  %{py3_dist hypothesis}
%endif

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n     python3-cramjam
Summary:        %{summary}
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# BSD-3-Clause
# BSD-3-Clause AND MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
License:        %{shrink:
                (0BSD OR MIT OR Apache-2.0) AND
                Apache-2.0 AND
                BSD-3-Clause AND
                MIT AND
                (MIT OR Zlib OR Apache-2.0)
                }
# LICENSE.dependencies contains a full license breakdown

%description -n python3-cramjam %{common_description}


%prep
%autosetup -n cramjam-%{srcversion}

# Do not strip the compiled Python module; we need useful debuginfo. Upstream
# set this intentionally, so this makes sense to keep downstream-only.
tomcli set pyproject.toml false 'tool.maturin.strip'
tomcli set pyproject.toml false 'profile.release.strip'

# Downstream-only: patch out the generate-import-lib feature, which is only
# relevant on Windows, and which depends on the corresponding pyo3 feature –
# which is not packaged for that reason.
tomcli set Cargo.toml del 'features.generate-import-lib'

# Downstream-only: remove all the static-linking features, and make the
# dynamic-linking ones default, as we do in rust-libcramjam.
static_features="$(
  tomcli get Cargo.toml features -F newline-keys |
    grep -E '.-static$' |
    tr '\n' ' '
)"
for sf in ${static_features}
do
  tomcli set Cargo.toml del "features.${sf}"
  if ! echo "${sf}" | grep -E '^use-system-' >/dev/null
  then
    binding="$(echo "${sf}" | sed -r 's/-static//')"
    tomcli set Cargo.toml lists replace --type regex \
        "features.${binding}" "${binding}-static" "${binding}-shared"
  fi
done

# Downstream-only: patch out the wasm-compat feature, which requires an
# unavailable blosc2 crate feature.
tomcli set Cargo.toml del 'features.wasm32-compat'

%cargo_prep


%generate_buildrequires
%pyproject_buildrequires
%cargo_generate_buildrequires


%build
export RUSTFLAGS='%{build_rustflags}'
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files cramjam


%check
%pyproject_check_import
%if %{with tests}
%ifarch s390x
# Even after serious effort by upstream (see
# https://github.com/milesgranger/blosc2-rs/issues/23), several blosc2-rs tests
# still fail on s390x, and therefore blosc2-related tests may also fail in this
# package. Making this package ExcludeArch would have a ripple effect on
# a whole tree of packages that depend on it, and which probably do not even
# use its blosc2 support. We consider that outcome even worse than shipping
# broken blosc2 support on s390x. Note that the endianness issues are probably
# in the C blosc2 library (and that the blosc2 package ignores any and all
# test failures on s390x), and see also:
# https://github.com/Blosc/c-blosc2/issues/467.
#
# […]
# E       cramjam.DecompressionError: Blosc2(InvalidHeader)
# […]
# tests/test_variants.py:55: DecompressionError
k="${k-}${k+ and }not test_variants_different_dtypes[blosc2]"
%endif
# Some tests in test_variants.py may produce segmentation faults
# https://github.com/milesgranger/cramjam/issues/190
k="${k-}${k+ and }not (test_variants and [blosc2)"

%pytest -k "${k-}" -v -n auto
%endif


%files -n python3-cramjam -f %{pyproject_files}
%license LICENSE LICENSES.dependencies
%doc README.md


%changelog
%autochangelog
