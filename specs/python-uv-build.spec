%bcond check 1

Name:           python-uv-build
Version:        0.9.17
Release:        %autorelease
Summary:        The uv build backend

# The license of the uv project is (MIT OR Apache-2.0), except:
#
# Apache-2.0 OR BSD-2-Clause:
#   - crates/uv-pep440/ is vendored and forked from crate(pep440_rs)
#   - crates/uv-pep508/ is vendored and forked from crate(pep508_rs)
#
# Rust crates compiled into the executable contribute additional license terms.
# To obtain the following list of licenses, build the package and note the
# output of %%{cargo_license_summary}.
#
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSD-2-Clause
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 OR MIT OR Zlib
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# MIT-0 OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib
License:        %{shrink:
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 OR BSD-2-Clause) AND
                MPL-2.0
                }
%global extra_crate_licenses %{shrink:
                0BSD AND
                (0BSD OR MIT OR Apache-2.0) AND
                Apache-2.0 AND
                (Apache-2.0 OR BSL-1.0) AND
                (Apache-2.0 OR MIT OR Zlib) AND
                (Apache-2.0 OR MIT-0) AND
                (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND
                BSD-3-Clause AND
                MIT AND
                (MIT OR Unlicense) AND
                Unicode-3.0 AND
                Unicode-DFS-2016 AND
                Zlib
                }
URL:            https://pypi.org/project/uv-build
Source:         %{pypi_source uv_build}

# This package is ultimately built from the same source tree as uv, i.e.
# https://github.com/astral-sh/uv, and belongs to the same cargo workspace.
#
# The PyPI sdist includes a small subset of the same workspace crates as uv.
# (Note that these are not published on crates.io, and are neither intended for
# separate distribution nor suitable for separate packaging.)
#
# We choose not to build uv-build from the uv source package because this spec
# file can be much simpler than the one for uv, because the separation helps to
# keep track of which patches, licenses, additional sources, etc. apply to
# uv-build, and because – while it normally makes sense to synchronize updates
# of this package with uv updates – there will likely be times when we want to
# keep updating uv (primarily a developer tool) while holding uv-build
# (primarily used for building packages) at an older version for compatibility.

BuildSystem:            pyproject
BuildOption(install):   -l uv_build

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# Also, there are a couple of test failures on 32-bit platforms.
ExcludeArch:   %{ix86}

BuildRequires:  tomcli
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust2rpm-helper

%global common_description %{expand:
This package is a slimmed down version of uv containing only the build
backend.}

%description
%{common_description}


%package -n     python3-uv-build
Summary:        %{summary}
License:        %{license} AND %{extra_crate_licenses}
# LICENSE.dependencies contains a full license breakdown

# In https://github.com/astral-sh/uv/issues/5588#issuecomment-2257823242,
# upstream writes “These have diverged significantly and the upstream versions
# are only passively maintained, uv requires these custom versions and can't
# use a system copy.”
#
# crates/uv-pep440/
# Version number from Cargo.toml:
Provides:       bundled(crate(pep440_rs)) = 0.7.0
# crates/uv-pep508/
# Cargo.toml has 0.6.0, but Changelog.md shows 0.7.0, and the source reflects
# the changes for 0.7.0:
Provides:       bundled(crate(pep508_rs)) = 0.7.0

%description -n python3-uv-build
%{common_description}


%prep
%autosetup -n uv_build-%{version} -p1

# Collect license files of vendored dependencies in the main source archive
install -t LICENSE.bundled/pep440_rs -D -p -m 0644 crates/uv-pep440/License-*
install -t LICENSE.bundled/pep508_rs -D -p -m 0644 crates/uv-pep508/License-*

# Patch out foreign (e.g. Windows-only) dependencies.
find -L . -type f -name Cargo.toml -print \
    -execdir rust2rpm-helper strip-foreign -o '{}' '{}' ';'

# Do not strip the compiled executable; we need useful debuginfo. Upstream set
# this intentionally, so this change makes sense to keep downstream-only.
tomcli set pyproject.toml false tool.maturin.strip
tomcli set Cargo.toml false profile.release.strip

# We retain the following example even when there are currently no dependencies
# that need to be adjusted.
#
# # foocrate
# #   wanted: 0.2.0
# #   currently packaged: 0.1.2
# #   https://bugzilla.redhat.com/show_bug.cgi?id=1234567
# tomcli set Cargo.toml str workspace.dependencies.foocrate.version 0.1.2

# spdx
#   wanted: 0.12.0
#   currently packaged: 0.13.2
#   Update spdx dependency to 0.13
#   https://github.com/astral-sh/uv/pull/17129
tomcli set Cargo.toml str workspace.dependencies.spdx.version '0.13.0'

%cargo_prep


%generate_buildrequires -p
# For unclear reasons, maturin checks for all crate dependencies when it is
# invoked as part of %%pyproject_buildrequires – including those corresponding
# to optional features.
#
# Since maturin always checks for dev-dependencies, we need -t so that they are
# generated even when the “check” bcond is disabled.
%cargo_generate_buildrequires -a -t


%build -p
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies


%check -a
%if %{with check}
# These tests require files from scripts/packages/built-by-uv/, which are not
# included in the sdist.
skip="${skip-} --skip tests::built_by_uv_building"
skip="${skip-} --skip wheel::test::test_prepare_metadata"

%cargo_test -- -- --exact ${skip-}
%endif


%files -n python3-uv-build -f %{pyproject_files}
# The other license files (LICENSE-APACHE, LICENSE-MIT, and
# LICENSE.dependencies) are already handled in the .dist-info directory.
%license LICENSE.bundled/
%doc README.md

%{_bindir}/uv-build
# Output of uv-build --help:
#   uv_build contains only the PEP 517 build backend for uv and can't be used
#   on the CLI. Use `uv build` or another build frontend instead.
# Therefore, it does not make sense to package a man page.


%changelog
%autochangelog
