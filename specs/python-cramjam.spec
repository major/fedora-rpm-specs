%bcond tests 1

# Workaround for ppc64 vectorization bug in LLVM 23:
# https://bugzilla.redhat.com/show_bug.cgi?id=2553620
#
# This can be removed in F45 after the fix is backported, and in F46+ after the
# fix is backported and/or LLVM is updated to version 24. Set the conditional
# for F45/F46 only, expecting that this will be fixed before F46 branching.
%if %{defined fc45} || %{defined fc46}
%ifarch ppc64le
%global build_rustflags %{build_rustflags} -Cno-vectorize-loops
%endif
%endif

# Note: cramjam and cramjam_pure_rust are developed together in the same git
# repository and are released synchronously with the same version numbers.
# Therefore, this source RPM produces both python3-cramjam and
# python3-httpcore2.
Name:           python-cramjam
Version:        2.14.0
Release:        %autorelease
Summary:        Thin Python bindings to de/compression algorithms in Rust

# SPDX
%global upstream_license MIT
License:        %{upstream_license}
# tests/data/integration/plaintext.txt and its various compressed forms contain
# the text of The Zen of Python, from https://peps.python.org/pep-0020/, which
# carries the declaration “This document has been placed in the public domain.”
SourceLicense:  %{upstream_license} AND LicenseRef-Fedora-Public-Domain
# From %%{cargo_license_summary}:
#
# 0BSD OR MIT OR Apache-2.0
# BSD-3-Clause
# BSD-3-Clause AND MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# bzip2-1.0.6
%global rust_additional_licenses %{shrink:
    BSD-3-Clause AND
    bzip2-1.0.6 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (MIT OR Zlib OR Apache-2.0)
    }
# LICENSE.dependencies contains a full license breakdown
URL:            https://github.com/milesgranger/cramjam

# We must filter the source archive from GitHub using the script in Source1,
# since some of the benchmark data has complicated or unclear license status.
# The PyPI sdists do not have this problem, since they exclude benchmarks and
# benchmark data (see: “Consider excluding benchmarks from PyPI sdists,”
# https://github.com/milesgranger/cramjam/issues/178), but we would have to
# have two separate sources, which isn’t desirable.
Source0:        cramjam-%{version}-filtered.tar.gz
# ./get_source ${COMMIT} (or ${TAG})
Source1:        get_source

BuildRequires:  tomcli
BuildRequires:  cargo-rpm-macros

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
License:        %{license} AND %{rust_additional_licenses}

%description -n python3-cramjam %{common_description}


%pyproject_extras_subpkg --name python3-cramjam --dist-name cramjam pure-rust


%package -n     python3-cramjam-pure-rust
Summary:        Pure-Rust backend for cramjam
License:        %{license} AND %{rust_additional_licenses}

%description -n python3-cramjam-pure-rust
The pure-Rust backend for cramjam: the same API, with zstd, lz4, bzip2, xz and
deflate/gzip/zlib from libcramjam’s pure-Rust implementations instead of the C
libraries.


%prep
%autosetup -p1 -C

# Downstream-only: patch out the wasm-compat feature, which is unnecessary and
# would bring in unwanted dependencies; similarly, remove cramjam-js from the
# workspace.
tomcli set Cargo.toml del features.wasm32-compat
tomcli set Cargo.toml lists delitem workspace.members cramjam-js

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
  if ! printf '%s\n' "${sf}" | grep --extended-regexp '^use-system-' >/dev/null
  then
    binding="$(echo "${sf}" | sed --regexp-extended 's/-static//')"
    tomcli set Cargo.toml lists replace --type regex \
        "features.${binding}" "${binding}-static" "${binding}-shared"
  fi
done

# Include LICENSE.dependencies in the .dist-info metadata and mark it %%license
tomcli set pyproject.toml append project.license-files LICENSE.dependencies

%cargo_prep


%generate_buildrequires
%pyproject_buildrequires
%cargo_generate_buildrequires -f pure-rust

cd pure-rust
%pyproject_buildrequires


%build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%pyproject_wheel

cd pure-rust
cp --preserve ../LICENSE ../LICENSE.dependencies .
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files --assert-license --dist-name cramjam cramjam
%pyproject_save_files --assert-license --dist-name cramjam-pure-rust cramjam_pure_rust


%check
%pyproject_verify_license %{upstream_license}
# If upstream starts listing license files explicitly, LICENSE.dependencies may
# be dropped from the .dist-info directory. Guard against this.
[ -n "$(find '%{buildroot}%{python3_sitearch}' -name LICENSE.dependencies)" ]

%if %{with tests}
# Test failures in test_variants_decompress_into with recent hypothesis
# versions: https://github.com/milesgranger/cramjam/issues/201
#
# It is hard to be really sure what is going on here. The failures are
# concerning, and might (or might not) reflect a serious problem. Nevertheless,
# since the problem appears to be linked to newer hypothesis versions, there’s
# not reason to believe that the package has *new* problems. It *might* have
# newly *revealed* problems. This merits further investigation.
#k="${k-}${k+ and }not test_variants_decompress_into"

# Regression with miniz_oxide>0.8.5
# https://github.com/milesgranger/cramjam/issues/211
# Failed: DID NOT RAISE <class 'cramjam.DecompressionError'>
k="${k-}${k+ and }not test_variants_raise_exception[deflate]"

%pytest -k "${k-}" --ignore=benchmarks/test_bench.py --verbose
export CRAMJAM_BACKEND=pure-rust
%pytest -k "${k-}" --ignore=benchmarks/test_bench.py --verbose
%endif


%files -n python3-cramjam -f %{pyproject_files --dist-name cramjam}
%doc README.md


%files -n python3-cramjam-pure-rust -f %{pyproject_files %{shrink:
     --dist-name cramjam-pure-rust}}
%doc pure-rust/README.md


%changelog
%autochangelog
