# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT.html
# Copyright (c) 2023 Maxwell G <maxwell@gtmx.me>
# Copyright (c) Fedora Project Authors

# Specfile compatability: EPEL >= 9 or Fedora >= 37 and RPM >= 4.16

%bcond tests 1
# Not yet in EPEL10: https://bugzilla.redhat.com/show_bug.cgi?id=2356387
%bcond pendulum %{undefined el10}

Name:           python-orjson
Version:        3.10.16
Release:        %autorelease
Summary:        Fast, correct Python JSON library

License:        Apache-2.0 OR MIT
URL:            https://github.com/ijl/orjson
Source:         %{pypi_source orjson}

# Manual patches for Cargo.toml
# - For now, allow compact_str 0.8;
#   https://bugzilla.redhat.com/show_bug.cgi?id=2347456
Patch:          orjson-fix-metadata.diff

BuildRequires:  tomcli
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest-forked}
# Upstream restricts these test dependencies to particular Python interpreter
# versions and architectures, but we would like to run the corresponding tests
# everywhere.
BuildRequires:  %{py3_dist numpy}
%if %{with pendulum}
BuildRequires:  %{py3_dist pendulum}
%endif
# These are not in tests/requirements.txt, but they enable additional tests
%ifnarch %{ix86}
BuildRequires:  %{py3_dist pandas}
%endif
BuildRequires:  %{py3_dist psutil}
BuildRequires:  cargo-rpm-macros >= 24


%global _description %{expand:
orjson is a fast, correct Python JSON library supporting dataclasses,
datetimes, and numpy}


%description %{_description}

%package -n     python3-orjson
Summary:        %{summary}
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# BSL-1.0
# MIT
# MIT OR Apache-2.0 (duplicate)
# Unlicense OR MIT
#
# Bundled PyO3 crates in include/pyo3/ are also (Apache-2.0 OR MIT).
License:        %{shrink:
                (Apache-2.0 OR MIT) AND
                BSD-3-Clause AND
                (Apache-2.0 OR BSL-1.0) AND
                BSL-1.0 AND
                MIT AND
                (Unlicense OR MIT)
                }

# Path to using published versions of pyo3-ffi/pyo3-build-config again?
# https://github.com/ijl/orjson/issues/524
#
# “You are welcome to work to upstream the diff if you find the vendoring
# unsuitable for your organization's own preferences.”
#
# Note that these crates are actually forked, not only bundled/vendored; see
# https://github.com/ijl/orjson/issues/524#issuecomment-2424170405 for details.
Provides:       bundled(crate(pyo3-build-config)) = 0.23.3
Provides:       bundled(crate(pyo3-ffi)) = 0.23.3

%description -n python3-orjson %{_description}


%prep
%autosetup -p1 -n orjson-%{version}
%cargo_prep

# Remove unstable features that require rust nightly; the avx512 feature also
# requires the x86_64 architecture
tomcli-set Cargo.toml del 'features.unstable-simd'
tomcli-set Cargo.toml del 'features.avx512'
# Remove unwind feature, which is not useful here: the comment above it says
# “Avoid bundling libgcc on musl.”
tomcli-set Cargo.toml del 'features.unwind'
tomcli-set Cargo.toml del 'dependencies.unwinding'
# Remove bundled rust crates
rm -r include/cargo
# Remove bundled yyjson.
rm -rv include/yyjson/

# Collect licenses for remaining vendored crates
mkdir -p LICENSES.vendored/pyo3
cp -vp include/pyo3/LICENSE* LICENSES.vendored/pyo3/

%if %{without pendulum}
sed -i '/^pendulum\b/d' test/requirements.txt
%endif
# Test dependency on arrow appears spurious
# https://github.com/ijl/orjson/issues/559
sed -i '/^arrow\b/d' test/requirements.txt
# Remove unpackaged PyPI plugin
sed -i '/pytest-random-order/d' test/requirements.txt


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:test/requirements.txt}
%cargo_generate_buildrequires
for dir in include/pyo3/*/
do
  pushd "${dir}" >/dev/null
  %cargo_generate_buildrequires
  popd >/dev/null
done


%build
export RUSTFLAGS='%{build_rustflags}'
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies
# Fedora's pyo3 is patched to not check Python version when building RPM packages.
# However, this uses a bundled version without the patch.
# Rather than patching it, we set the environment variable,
# which allows us to test this package with development Python versions.
export UNSAFE_PYO3_SKIP_VERSION_CHECK=1
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l orjson


%check
%pyproject_check_import
%if %{with tests}
# --forked: protect the pytest process against test segfaults
# -rs: print the reasons for skipped tests
%pytest --forked -rs
%endif


%files -n python3-orjson -f %{pyproject_files}
%license LICENSES.vendored/
%doc README.md


%changelog
%autochangelog
