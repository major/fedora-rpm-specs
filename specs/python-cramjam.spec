%bcond tests 1

#global commit xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#global snapdate YYYYMMDD

Name:           python-cramjam
Version:        2.11.0
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

BuildSystem:            pyproject
BuildOption(install):   -l cramjam

BuildRequires:  tomcli >= 0.8.0
BuildRequires:  cargo-rpm-macros >= 24

%if %{with tests}
# These (along with some unwanted dependencies like linters) are listed in the
# dev extra in pyproject.toml.
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist hypothesis}
%endif

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n     python3-cramjam
Summary:        %{summary}
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
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


%prep -a
# Downstream-only: patch out the generate-import-lib feature, which is only
# relevant on Windows, and which depends on the corresponding pyo3 feature –
# which is not packaged for that reason.
tomcli set Cargo.toml del 'features.generate-import-lib'

# Downstream-only: patch out the wasm-compat feature, which is unnecessary and
# would bring in unwanted dependencies
tomcli set Cargo.toml del 'features.wasm32-compat'

# Downstream-only: patch out the "experimental" feature and all of the features
# related to blosc2 and isa-l support. We only want to build the Python
# extension with the default features, and we only want maturin to check
# dependencies for those features.
blosc2_isal_features="$(
  tomcli get Cargo.toml features -F newline-keys |
    grep -E 'blosc2|ideflate|igzip|isal|izlib' |
    tr '\n' ' '
)"
for feature in experimental ${blosc2_isal_features}
do
  tomcli set Cargo.toml del "features.${feature}"
done

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

%cargo_prep


%generate_buildrequires -a
%cargo_generate_buildrequires


%build -p
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies


%check -a
%if %{with tests}
# Test failures in test_variants_decompress_into with recent hypothesis
# versions: https://github.com/milesgranger/cramjam/issues/201
#
# It is hard to be really sure what is going on here. The failures are
# concerning, and might (or might not) reflect a serious problem. Nevertheless,
# since the problem appears to be linked to newer hypothesis versions, there’s
# not reason to believe that the package has *new* problems. It *might* have
# newly *revealed* problems. This merits further investigation.
k="${k-}${k+ and }not test_variants_decompress_into"

# Regression with miniz_oxide>0.8.5
# https://github.com/milesgranger/cramjam/issues/211
# Failed: DID NOT RAISE <class 'cramjam.DecompressionError'>
k="${k-}${k+ and }not test_variants_raise_exception[deflate]"

%pytest -k "${k-}" --ignore=benchmarks/test_bench.py -v
%endif


%files -n python3-cramjam -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
