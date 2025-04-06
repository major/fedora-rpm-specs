%bcond check 1

Name:           python-uv-build
Version:        0.6.12
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
#
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSD-2-Clause
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 OR MIT OR Zlib
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSL-1.0
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MIT-0 OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib
# Zlib OR Apache-2.0 OR MIT
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
                (Apache-2.0 OR MIT-0)
                (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND
                BSD-3-Clause AND
                BSL-1.0 AND
                MIT AND
                (MIT OR Unlicense) AND
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
%global pubgrub_rev b70cf707aa43f21b32f3a61b8a0889b15032d5c4
%global pubgrub_snapdate 20250202
%global version_ranges_baseversion 0.1.1
Source200:      %{pubgrub_git}/archive/%{pubgrub_rev}/pubgrub-%{pubgrub_rev}.tar.gz

# This patch is for the forked, bundled pubgrub crate.
#
# Downstream-only: Revert "feat: ensure successful round-trip of RON (#193)"
#   This reverts commit 21c6a215432fea9a75b7d15d9a9936af9ccc17cb.
# We will not be packaging an alpha version of rust-ron. We can adjust this
# after ron 0.9.x is released.
Patch200:       0001-Downstream-only-Revert-feat-ensure-successful-round-.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# Also, there are a couple of test failures on 32-bit platforms.
ExcludeArch:   %{ix86}

BuildRequires:  python3-devel
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

# Collect license files of vendored dependencies in the main source archive
install -t LICENSE.bundled/pep440_rs -D -p -m 0644 crates/uv-pep440/License-*
install -t LICENSE.bundled/pep508_rs -D -p -m 0644 crates/uv-pep508/License-*

# Patch out foreign (e.g. Windows-only) dependencies.
find . -type f -name Cargo.toml -print \
    -execdir rust2rpm-helper strip-foreign -o '{}' '{}' ';'

# Do not strip the compiled executable; we need useful debuginfo. Upstream set
# this intentionally, so this change makes sense to keep downstream-only.
tomcli set pyproject.toml false tool.maturin.strip
tomcli set Cargo.toml false profile.release.strip

%cargo_prep


%generate_buildrequires
# For unclear reasons, maturin checks for all crate dependencies when it is
# invoked as part of %%pyproject_buildrequires – including those corresponding
# to optional features.
#
# Since maturin always checks for dev-dependencies, we need -t so that they are
# generated even when the “check” bcond is disabled.
%cargo_generate_buildrequires -a -t
%pyproject_buildrequires


%build
%pyproject_wheel

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies


%install
%pyproject_install
%pyproject_save_files -l uv_build


%check
%pyproject_check_import
%if %{with check}
# These tests require files from scripts/packages/built-by-uv/, which are not
# included in the sdist.
skip="${skip-} --skip tests::built_by_uv_building"
skip="${skip-} --skip wheel::test::test_prepare_metadata"

%cargo_test -- -- --exact ${skip-}
%endif


%files -n python3-uv-build -f %{pyproject_files}
# The main license files, LICENSE-APACHE and LICENSE-MIT, are already in the
# .dist-info directory. However, we still need to include these manually:
%license LICENSE.dependencies LICENSE.bundled/
%doc README.md

%{_bindir}/uv-build
# Output of uv-build --help:
#   uv_build contains only the PEP 517 build backend for uv and can't be used
#   on the CLI. Use `uv build` or another build frontend instead.
# Therefore, it does not make sense to package a man page.


%changelog
%autochangelog
