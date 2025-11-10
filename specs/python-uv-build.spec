%bcond check 1

Name:           python-uv-build
Version:        0.9.8
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
# output of %%{cargo_license_summary}. This should automatically include the
# licenses of the following bundled forks:
#   - pubgrub/version-ranges, Source200, is MPL-2.0.
#   - reqwest-middleware/reqwest-retry, Source300, is (MIT OR Apache-2.0).
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
# BSD-2-Clause OR Apache-2.0 OR MIT
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
                (Apache-2.0 OR BSD-2-Clause OR MIT) AND
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

# For the foreseeable future, uv must use a fork of pubgrub (and the
# version-ranges crate, which belongs to the same project), as explained in:
#   Plans for eventually using published pubgrub?
#   https://github.com/astral-sh/uv/issues/3794
# We therefore bundle the fork as prescribed in
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/#_replacing_git_dependencies
# Note that uv-build currently only uses version-ranges, not pubgrub.
%global pubgrub_git https://github.com/astral-sh/pubgrub
%global pubgrub_rev d8efd77673c9a90792da9da31b6c0da7ea8a324b
%global pubgrub_snapdate 20250810
%global version_ranges_baseversion 0.1.1
Source200:      %{pubgrub_git}/archive/%{pubgrub_rev}/pubgrub-%{pubgrub_rev}.tar.gz

# Until “Report retry count on Ok results,”
# https://github.com/TrueLayer/reqwest-middleware/pull/235, is reviewed,
# merged, and released, uv must use a fork of reqwest-middleware/reqwest-retry
# to support the changes in “Show retries for HTTP status code errors,”
# https://github.com/astral-sh/uv/pull/13897. We therefore bundle the fork as
# prescribed in
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/#_replacing_git_dependencies
%global reqwest_middleware_git https://github.com/astral-sh/reqwest-middleware
%global reqwest_middleware_rev 7650ed76215a962a96d94a79be71c27bffde7ab2
%global reqwest_middleware_snapdate 20250828
%global reqwest_middleware_baseversion 0.4.2
%global reqwest_retry_baseversion 0.7.0
Source300:      %{reqwest_middleware_git}/archive/%{reqwest_middleware_rev}/reqwest-middleware-%{reqwest_middleware_rev}.tar.gz

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

# This is a fork of pubgrub/version-ranges; see the notes about Source200.
%global pubgrub_snapinfo %{pubgrub_snapdate}git%{sub %{pubgrub_rev} 1 7}
%global version_ranges_version %{version_ranges_baseversion}^%{pubgrub_snapinfo}
Provides:       bundled(crate(version-ranges)) = %{version_ranges_version}
# This is a fork of reqwest-middleware/reqwest-retry; see the notes about
# Source300.
%global reqwest_middleware_snapinfo %{reqwest_middleware_snapdate}git%{sub %{reqwest_middleware_rev} 1 7}
%global reqwest_middleware_version %{reqwest_middleware_baseversion}^%{reqwest_middleware_snapinfo}
%global reqwest_retry_version %{reqwest_retry_baseversion}^%{reqwest_middleware_snapinfo}
Provides:       bundled(crate(reqwest-middleware)) = %{reqwest_middleware_version}
Provides:       bundled(crate(reqwest-retry)) = %{reqwest_retry_version}

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
%autosetup -n uv_build-%{version} -N
%autopatch -p1 -M99

# Usage: git2path SELECTOR PATH
# Replace a git dependency with a path dependency in Cargo.toml
git2path() {
  tomcli set Cargo.toml del "${1}.git"
  tomcli set Cargo.toml del "${1}.rev"
  tomcli set Cargo.toml str "${1}.path" "${2}"
}

# See comments above Source200:
%setup -q -T -D -b 200 -n uv_build-%{version}
pushd '../pubgrub-%{pubgrub_rev}/'
%autopatch -p1 -m200 -M299
popd
ln -s '../../pubgrub-%{pubgrub_rev}/version-ranges' crates/version-ranges
# Convert the symlinked LICENSE in version-ranges to a regular file, since we
# will be removing top-level files from pubgrub.
rm -v crates/version-ranges/LICENSE
cp -p '../pubgrub-%{pubgrub_rev}/LICENSE' crates/version-ranges/
# Prove that we do not use the pubgrub crate by removing everything except the
# version-ranges subdirectory.
find '../pubgrub-%{pubgrub_rev}/' -mindepth 1 -maxdepth 1 \
    ! -name 'version-ranges' -execdir rm -rv '{}' '+'
# Note that install does always dereference symlinks, which is what we want:
install -t LICENSE.bundled/version-ranges -D -p -m 0644 \
    crates/version-ranges/LICENSE
git2path workspace.dependencies.version-ranges crates/version-ranges

# See comments above Source300:
%setup -q -T -D -b 300 -n uv_build-%{version}
pushd '../reqwest-middleware-%{reqwest_middleware_rev}'
%autopatch -p1 -m300 -M399
# The (path-based) dev-dependency on reqwest-tracing is required only for an
# example in README.md; avoid it.
tomcli set reqwest-middleware/Cargo.toml del dev-dependencies.reqwest-tracing
sed -r -i 's/^```rust$/&,ignore/' README.md
popd
ln -s '../../reqwest-middleware-%{reqwest_middleware_rev}/reqwest-middleware' \
    crates/reqwest-middleware
git2path workspace.dependencies.reqwest-middleware crates/reqwest-middleware
git2path patch.crates-io.reqwest-middleware crates/reqwest-middleware
install -t LICENSE.bundled/reqwest-middleware -D -p -m 0644 \
    crates/reqwest-middleware/LICENSE*
ln -s '../../reqwest-middleware-%{reqwest_middleware_rev}/reqwest-retry' \
    crates/reqwest-retry
git2path workspace.dependencies.reqwest-retry crates/reqwest-retry
git2path patch.crates-io.reqwest-retry crates/reqwest-retry
install -t LICENSE.bundled/reqwest-retry -D -p -m 0644 \
    crates/reqwest-retry/LICENSE*
# We do not need the reqwest-tracing crate.
rm -rv '../reqwest-middleware-%{reqwest_middleware_rev}/reqwest-tracing'

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
#   currently packaged: 0.10.9 (but we want to update to 0.12)
#   https://bugzilla.redhat.com/show_bug.cgi?id=2387258
#   Update the spdx dependency to version 0.12
#   https://github.com/astral-sh/uv/pull/16552
tomcli set Cargo.toml str workspace.dependencies.spdx.version \
    '>=0.10.9, <0.13.0'

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
