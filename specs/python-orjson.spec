# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT.html
# Copyright (c) 2023 Maxwell G <maxwell@gtmx.me>
# Copyright (c) Fedora Project Authors

# Specfile compatability: EPEL >= 9 or Fedora >= 37 and RPM >= 4.16

%bcond tests 1
# Not yet in EPEL10: https://bugzilla.redhat.com/show_bug.cgi?id=2356387
%bcond pendulum %{undefined el10}

# By default, orjson uses a bundled copy of the C library yyjson,
# https://github.com/ibireme/yyjson, as the JSON deserialization backend. It is
# forked (customized) and compiled with a particular set of options via
# preprocessor defines (see build.rs), so it is not a candidate for unbundling.
#
# We do have the option to disable the yyjson backend, in which case the json
# crate from the Rust standard library, https://docs.rs/json, is used instead.
%bcond yyjson 0

Name:           python-orjson
Version:        3.11.2
Release:        %autorelease
Summary:        Fast, correct Python JSON library

# The entire source is (Apache-2.0 OR MIT), except:
#
%if %{with yyjson}
# MIT:
# - include/yyjson/yyjson.c
# - include/yyjson/yyjson.h
#
%endif
# Apache-2.0:
# - src/serialize/writer/str/mod.rs
# - src/serialize/writer/str/sse2.rs
License:        (Apache-2.0 OR MIT) AND Apache-2.0%{?with_yyjson: AND MIT}
%if %{without yyjson}
# Additionally, the following are removed in %%prep and do not contribute to
# the licenses of the binary RPMs:
#
# MIT:
# - include/yyjson/yyjson.c
# - include/yyjson/yyjson.h
%endif
SourceLicense:  (Apache-2.0 OR MIT) AND Apache-2.0 AND MIT
URL:            https://github.com/ijl/orjson
# We must be careful about the source archive.
#
# The PyPI releases have a vendored Rust dependency bundle in include/cargo/,
# which we would remove in %%prep, but which we must still check to make sure
# everything has a license acceptable for distribution in Fedora before
# uploading to the lookaside cache.
# Source:         %%{pypi_source orjson}
# The GitHub archives from
# %%{url}/archive/%%{version}/orjson-%%{version}.tar.gz do not have the
# vendored crates, but they contain benchmark data in data/, some of which is
# lacking its license text (e.g.  data/blns.txt.xz, which is from
# https://github.com/minimaxir/big-list-of-naughty-strings and should carry the
# corresponding MIT license text), and some of which looks like it might have
# at best unclear license status. Since the benchmark data is potentially
# problematic, we would need to filter the GitHub archives with a script.
Source0:        orjson-%{version}-filtered.tar.xz
# ./get_source ${COMMIT} (or ${TAG})
Source1:        get_source

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
# Output of %%{cargo_license_summary}:
#
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# BSL-1.0
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
#
# Note that this must include the terms of the base package License expression.
License:        %{shrink:
                (Apache-2.0 OR MIT) AND
                Apache-2.0 AND
                (Apache-2.0 OR BSL-1.0) AND
                BSD-3-Clause AND
                BSL-1.0 AND
                MIT AND
                (Unlicense OR MIT)
                }

%if %{with yyjson}
# Version from YYJSON_VERSION_STRING in include/yyjson/yyjson.h
Provides:       bundled(yyjson) = 0.9.0
%endif

%description -n python3-orjson %{_description}


%prep
%autosetup -p1 -n orjson-%{version}
%cargo_prep

# Remove unwind feature, which is not useful here: the comment above it says
# “Avoid bundling libgcc on musl.”
tomcli-set Cargo.toml del 'features.unwind'
tomcli-set Cargo.toml del 'dependencies.unwinding'
%if %{without yyjson}
# Remove bundled yyjson.
rm -rv include/yyjson/
%endif

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


%build
export RUSTFLAGS='%{build_rustflags}'
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies
%if %{without yyjson}
export ORJSON_DISABLE_YYJSON=1
%endif
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
%doc README.md


%changelog
%autochangelog
