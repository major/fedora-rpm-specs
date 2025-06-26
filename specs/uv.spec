%bcond check 1
# Should we run integration tests, many of which require specific Python
# interpreter versions (major.minor, not major.minor.patch)? This adds a few
# dozen tests, but adds BuildRequires on more Pythons, and could reduce our
# confidence that everything works correctly in an environment that only has
# the main system Python.
#
# EPEL10 does not have alternative versions of Python, so we cannot run most of
# the integration tests there, and manually selecting those we can run would be
# far too tedious.
%bcond it %{undefined el10}

Name:           uv
Version:        0.7.13
Release:        %autorelease
Summary:        An extremely fast Python package installer and resolver, written in Rust

# The license of the uv project is (MIT OR Apache-2.0), except:
#
# Apache-2.0:
#   - crates/uv-python/src/libc.rs contains code derived from
#     crate(glibc_version)
#   - crates/uv-requirements-txt/src/shquote.rs contains code derived from
#     crate(r-shquote); the original code was (Apache-2.0 OR
#     LGPL-2.1-or-later), but the vendored copy cites only the Apache-2.0
#     option.
#
# Apache-2.0 OR BSD-2-Clause:
#   - crates/uv-pep440/ is vendored and forked from crate(pep440_rs)
#   - crates/uv-pep508/ is vendored and forked from crate(pep508_rs)
#   - crates/uv-python/packaging/ is vendored and forked from
#     python3dist(packaging)
#
# (Apache-2.0 OR MIT) AND BSD-3-CLause:
#   - The function wheel_metadata_from_remote_zip in
#     crates/uv-client/src/remote_metadata.rs is vendored and forked from the
#     function lazy_read_wheel_metadata in src/index/lazy_metadata.rs in
#     crate(rattler_installs_packages) and is BSD-3-Clause AND (Apache-2.0 OR
#     MIT): the original routine is BSD-3-CLause, and subsequent modifications
#     are explicitly (Apache-2.0 OR MIT).
#
# MIT
#   - crates/uv-virtualenv/src/activator/ is vendored and forked from
#     python3dist(virtualenv)
#
# Additionally, the following are bundled/forked but happen to be under the
# same (Apache-2.0 OR MIT) terms as uv itself:
#   - crates/uv-extract/src/vendor/cloneable_seekable_reader.rs is vendored and
#     forked from crate(ripunzip)
#
# The following are present in the source but believed not to contribute to the
# licenses of the binary RPMs. Note that ecosystem/ contains only
# pyproject.toml files used for testing, not complete bundled projects.
#
# Apache-2.0:
#   - ecosystem/airflow/
#   - ecosystem/home-assistant-core/
#   - ecosystem/transformers/
#   - ecosystem/warehouse/
# Apache-2.0 OR MIT:
#   - ecosystem/packse/
# BSD-2-Clause-Patent:
#   - ecosystem/github-wikidata-bot/
# BSD-3-Clause:
#   - ecosystem/saleor/
# MIT:
#   - crates/uv-python/fetch-download-metadata.py is derived from
#     https://github.com/mitsuhiko/rye/tree/f9822267a7f00332d15be8551f89a212e7bc9017
#     which was MIT.
#   - ecosystem/black/
#
# Rust crates compiled into the executable contribute additional license terms.
# To obtain the following list of licenses, build the package and note the
# output of %%{cargo_license_summary}. This should automatically include the
# licenses of the following bundled forks:
#   - async_zip, Source100, is MIT.
#   - pubgrub/version-ranges, Source200, is MPL-2.0.
#   - tl, Source400, is MIT.
#
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 AND ISC AND (MIT OR Apache-2.0)
# Apache-2.0 OR BSD-2-Clause
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR ISC OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 OR MIT OR Zlib
# Apache-2.0 WITH LLVM-exception
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# CDLA-Permissive-2.0
# ISC
# LGPL-3.0-or-later OR MPL-2.0
# MIT
# MIT OR Apache-2.0
# MIT OR LGPL-3.0-or-later
# MIT OR Zlib OR Apache-2.0
# MIT-0 OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib
License:        %{shrink:
                0BSD AND
                (0BSD OR Apache-2.0 OR MIT) AND
                Apache-2.0 AND
                (Apache-2.0 OR BSD-2-Clause) AND
                (Apache-2.0 OR BSD-2-Clause OR MIT) AND
                (Apache-2.0 OR BSL-1.0) AND
                (Apache-2.0 OR ISC OR MIT) AND
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 OR MIT OR Zlib) AND
                (Apache-2.0 OR MIT-0) AND
                (Apache-2.0 WITH LLVM-exception) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                BSD-3-Clause AND
                CDLA-Permissive-2.0 AND
                ISC AND
                (LGPL-3.0-or-later OR MIT) AND
                (LGPL-3.0-or-later OR MPL-2.0) AND
                MIT AND
                (MIT OR Unlicense) AND
                MPL-2.0 AND
                Unicode-3.0 AND
                Unicode-DFS-2016 AND
                Zlib
                }
# LICENSE.dependencies contains a full license breakdown
URL:            https://github.com/astral-sh/uv
Source0:        %{url}/archive/%{version}/uv-%{version}.tar.gz
# Default system-wide configuration file
# https://docs.astral.sh/uv/configuration/files
Source1:        uv.toml

# Currently, uv must use a fork of async_zip, as explained in:
#   Restore central directory buffering
#   https://github.com/charliermarsh/rs-async-zip/pull/2
# and further discussed in
#   Please consider supporting the current release of async_zip
#   https://github.com/prefix-dev/async_http_range_reader/issues/14
# We therefore bundle the fork as prescribed in
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/#_replacing_git_dependencies
%global async_zip_git https://github.com/charliermarsh/rs-async-zip
%global async_zip_rev c909fda63fcafe4af496a07bfda28a5aae97e58d
%global async_zip_baseversion 0.0.17
%global async_zip_snapdate 20241114
Source100:      %{async_zip_git}/archive/%{async_zip_rev}/rs-async-zip-%{async_zip_rev}.tar.gz

# For the foreseeable future, uv must use a fork of pubgrub (and the
# version-ranges crate, which belongs to the same project), as explained in:
#   Plans for eventually using published pubgrub?
#   https://github.com/astral-sh/uv/issues/3794
# We therefore bundle the fork as prescribed in
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/#_replacing_git_dependencies
%global pubgrub_git https://github.com/astral-sh/pubgrub
%global pubgrub_rev 06ec5a5f59ffaeb6cf5079c6cb184467da06c9db
%global pubgrub_baseversion 0.3.0
%global pubgrub_snapdate 20250523
%global version_ranges_baseversion 0.1.1
Source200:      %{pubgrub_git}/archive/%{pubgrub_rev}/pubgrub-%{pubgrub_rev}.tar.gz

# For the time being, uv must use a fork of tl. See:
#   Path back to using released tl crate dependency?
#   https://github.com/astral-sh/uv/issues/6687
# It should be possible to stop forking and bundling if tl upstream merges and
# releases the following fix:
#   Avoid truncating URLs in unquoted hrefs
#   https://github.com/y21/tl/pull/69
# We therefore bundle the fork as prescribed in
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/#_replacing_git_dependencies
%global tl_git https://github.com/astral-sh/tl
%global tl_rev 6e25b2ee2513d75385101a8ff9f591ef51f314ec
%global tl_baseversion 0.7.8
%global tl_snapdate 20240825
Source400:      %{tl_git}/archive/%{tl_rev}/tl-%{tl_rev}.tar.gz

# Downstream-only: do not override the default allocator
#
# In https://github.com/astral-sh/uv/pull/399, it was reasonably claimed that
# using tikv-jemallocator improved benchmarks by 10%. However, this would
# require packaging at least the tikv-jemalloc-sys, tikv-jemalloc-ctl, and
# tikv-jemallocator crates, and this is expected to be not quite trivial.
# We use the default allocator for now, and reserve tikv-jemallocaator
# packaging as optional future work.
Patch:          0001-Downstream-only-do-not-override-the-default-allocato.patch

# Downstream-only: Always find the system-wide uv executable
# See discussion in
#   Should uv.find_uv_bin() be able to find /usr/bin/uv?
#   https://github.com/astral-sh/uv/issues/4451
Patch:          0001-Downstream-patch-always-find-the-system-wide-uv-exec.patch

# Unpin reqwest. Reverts “Downgrade reqwest and hyper-util,”
# https://github.com/astral-sh/uv/pull/13835. The pin was due to
# https://github.com/astral-sh/uv/issues/13831, and based on discussion in that
# issue and in https://github.com/hyperium/hyper-util/pull/200, we can update
# reqwest as long as we also update hyper-util to 0.1.14 or later.
#
# The issue that the pin worked around was only reported on MacOS, but we would
# rather not assume that is the only place it occurs.
#
# This is downstream-only because it is extremely temporary: upstream is
# tracking and testing the fix in hyper-util, and we can expect that the
# version pin will be removed in the next release or two.
Patch:          uv-0.7.13-unpin-reqwest.patch

# Update sanitize-filename requirement from 0.5 to 0.6
Patch100:       https://github.com/Majored/rs-async-zip/pull/153.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# On some releases and architectures, Koji builders sometimes or always run out
# of memory in the final linking step. This cannot be fixed by adding
# "-C link-args=-Wl,--no-keep-memory" to the RUSTFLAGS (as that seems to have
# no significant effect on memory requirements), nor can it be fixed by
# reducing parallelism with e.g. the %%constrain_build macro (although we do
# need this as well), since nothing else is happening at that point in the
# build. See:
# https://doc.rust-lang.org/rustc/codegen-options/index.html#debuginfo
%global rustflags_debuginfo 1

# As a separate limitation, memory exhaustion can occur on builders with very
# many CPUs. Typical workspace crates peak out at 2-4 GB per rustc invocation.
# The uv crate needs much more memory to compile (see the RUSTFLAGS adjustment
# in %%build), but in practice it is also compiled alone after all the other
# crates have finished, so it does not need to influence (and does not benefit
# from) this setting. Even though some crates will require more than 3GB, the
# average should be below that on many-core systems. Increase as needed.
%constrain_build -m 4096

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust2rpm-helper
BuildRequires:  tomcli
BuildRequires:  python3-devel
%if %{with check} && %{with it}
# See trove classifiers in pyproject.toml for supported Pythons.
%if %{defined fc41}
# https://fedoraproject.org/wiki/Changes/RetirePython3.8
BuildRequires:  /usr/bin/python3.8
%endif
BuildRequires:  /usr/bin/python3.9
BuildRequires:  /usr/bin/python3.10
BuildRequires:  /usr/bin/python3.11
BuildRequires:  /usr/bin/python3.12
BuildRequires:  /usr/bin/python3.13
%endif

# This is a fork of async_zip; see the notes about Source100.
%global async_zip_snapinfo %{async_zip_snapdate}git%{sub %{async_zip_rev} 1 7}
%global async_zip_version %{async_zip_baseversion}^%{async_zip_snapinfo}
Provides:       bundled(crate(async_zip)) = %{async_zip_version}
# This is a fork of pubgrub/version-ranges; see the notes about Source200.
%global pubgrub_snapinfo %{pubgrub_snapdate}git%{sub %{pubgrub_rev} 1 7}
%global pubgrub_version %{pubgrub_baseversion}^%{pubgrub_snapinfo}
%global version_ranges_version %{version_ranges_baseversion}^%{pubgrub_snapinfo}
Provides:       bundled(crate(pubgrub)) = %{pubgrub_version}
Provides:       bundled(crate(version-ranges)) = %{version_ranges_version}
# This is a fork of tl; see the notes about Source400.
%global tl_snapinfo %{tl_snapdate}git%{sub %{tl_rev} 1 7}
%global tl_version %{tl_baseversion}^%{tl_snapinfo}
Provides:       bundled(crate(tl)) = %{tl_version}

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
# crates/uv-virtualenv/
# As a whole, this crate is derived from https://github.com/konstin/gourgeist
# 0.0.4, which was published as https://crates.io/crates/gourgeist. It looks
# looks like the project was subsumed into `uv`, and the link to `uv` at
# https://konstin.github.io/gourgeist/ seems to support this, so we consider
# this not to be a real case of bundling, and we do not add:
#   Provides:       bundled(crate(gourgeist)) = 0.0.4

# crates/uv-extract/src/vendor/cloneable_seekable_reader.rs
# Version number is an educated guess based on comparison of file contents,
# cross-checked with timing: the file was first introduced to uv as
# crates/puffin-installer/src/vendor/cloneable_seekable_reader.rs in
# https://github.com/astral-sh/uv/commit/2a846e76b7725633776fd08e04ce8b827bb0580f
# on 2023-10-08, and 0.4.0 was the current release of ripunzip at that time.
Provides:       bundled(crate(ripunzip)) = 0.4.0
# wheel_metadata_from_remote_zip only, in
# crates/uv-client/src/remote_metadata.rs
# Version number is, at the time of this writing, the only release of
# https://github.com/prefix-dev/rip containing the corresponding function
# lazy_read_wheel_metadata in
# (crates/rattler_installs_packages/)src/index/lazy_metadata.rs.
Provides:       bundled(crate(rattler_installs_packages)) = 0.9.0

# crates/uv-python/src/libc.rs
# This is at least partially derived (with changes) from the glibc_version
# crate, https://github.com/delta-incubator/glibc-version-rs. The last commit
# that we can match up with the file in uv is
# 5e1002dc7a3c39c0d72631cc488bef2fc5fea0fb, although it would be equally
# correct to reference any of several slightly later commits.
Provides:       bundled(crate(glibc_version)) = 0.1.2^20221117git5e1002d

# crates/uv-requirements-txt/src/shquote.rs
# The unquote implementation is vendored from the r-shquote crate because it is
# unmaintained upstream, https://github.com/astral-sh/uv/issues/11780.
Provides:       bundled(crate(r-shquote)) = 0.1.1

# The contents of crates/uv-virtualenv/src/activator/ are a bundled and
# slightly forked copy of a subset of https://pypi.org/project/virtualenv; see
# https://github.com/pypa/virtualenv/tree/main/src/virtualenv/activation.
#
# The same justification for not attempting to unbundle downstream applies as
# for the bundling from python3dist(packaging), below; additionally, some of
# the scripts have been forked. See also:
#   https://github.com/astral-sh/uv/issues/5588#issuecomment-2257474140
#
# The scripts were last updated from virtualenv upstream in
# https://github.com/astral-sh/uv/pull/3376 on 2024-05-04; the latest
# virtualenv release at that time was 20.26.0.
Provides:       bundled(python3dist(virtualenv)) = 20.26

# The contents of crates/uv-python/python/packaging/ are a bundled copy of a
# subset of https://pypi.org/project/packaging.
#
# This was added in
# https://github.com/astral-sh/uv/commit/7964bfbb2bed50a5c7b0650a7b6799a66503a33a,
# the commit message of which helps explain the rationale. In part:
#
#   The architecture of uv does not necessarily match that of the python
#   interpreter. In cross compiling/testing scenarios the operating system can
#   also mismatch. To solve this, we move arch and os detection to python,
#   vendoring the relevant pypa/packaging code, preventing mismatches between
#   what the python interpreter was compiled for and what uv was compiled for.
#
# We cannot use the system package directly because these Python sources are
# compiled into the uv executable, and the binary package does not even depend
# on the system Python interpreter. Patching uv to read the sources from the
# system package at runtime would be much too extreme for a downstream change.
# Copying sources from the system package into the build tree is feasible, but
# – especially considering that the sources are not necessarily executed with
# the system Python interpreter – the risks of deviating from upstream’s tested
# sources would seem to greatly outweigh any possible benefits of such
# “build-time unbundling.” We therefore consider this instance of bundling
# technically necessary. See also:
#   https://github.com/astral-sh/uv/issues/5588#issuecomment-2257474140
#
# README.md has the bundled commit hash, __init__.py has the version number,
# and https://github.com/pypa/packaging/tree/${commit} is the source of the
# snapshot date.
Provides:       bundled(python3dist(packaging)) = 24.1~dev0^20240310gitcc938f9

%global common_description %{expand:
An extremely fast Python package installer and resolver, written in Rust.
Designed as a drop-in replacement for common pip and pip-tools workflows.

Highlights:

  • ⚖️ Drop-in replacement for common pip, pip-tools, and virtualenv commands.
  • ⚡️ 10-100x faster than pip and pip-tools (pip-compile and pip-sync).
  • 💾 Disk-space efficient, with a global cache for dependency deduplication.
  • 🐍 Installable via curl, pip, pipx, etc. uv is a static binary that can be
    installed without Rust or Python.
  • 🧪 Tested at-scale against the top 10,000 PyPI packages.
  • 🖥️ Support for macOS, Linux, and Windows.
  • 🧰 Advanced features such as dependency version overrides and alternative
    resolution strategies.
  • ⁉️ Best-in-class error messages with a conflict-tracking resolver.
  • 🤝 Support for a wide range of advanced pip features, including editable
    installs, Git dependencies, direct URL dependencies, local dependencies,
    constraints, source distributions, HTML and JSON indexes, and more.}

%description %{common_description}


%package -n python3-uv
Summary:        Importable Python module for uv

BuildArch:      noarch

Requires:       uv = %{version}-%{release}

%description -n python3-uv %{common_description}

This package provides an importable Python module for uv.


%prep
%autosetup -N
%autopatch -p1 -M99

# Usage: git2path SELECTOR PATH
# Replace a git dependency with a path dependency in Cargo.toml
git2path() {
  tomcli set Cargo.toml del "${1}.git"
  tomcli set Cargo.toml del "${1}.rev"
  tomcli set Cargo.toml str "${1}.path" "${2}"
}

# See comments above Source100:
%setup -q -T -D -b 100 -n uv-%{version}
# Adding the crate to the workspace (in this case implicitly, by linking it
# under crates/) means %%cargo_generate_buildrequires can handle it correctly.
ln -s '../../rs-async-zip-%{async_zip_rev}' crates/async_zip
git2path workspace.dependencies.async_zip crates/async_zip
pushd crates/async_zip
%autopatch -p1 -m100 -M199
popd
install -t LICENSE.bundled/async_zip -D -p -m 0644 crates/async_zip/LICENSE
# Drop dev-dependencies that are only required for compiling the
# actix-multipart example, and remove it. Note that while “futures” is in this
# section of Cargo.toml, it is in fact also used in a test.
tomcli set crates/async_zip/Cargo.toml del dev-dependencies.actix-multipart
mv crates/async_zip/examples/actix_multipart.rs{,.disabled}
tomcli set crates/async_zip/Cargo.toml del dev-dependencies.actix-web
tomcli set crates/async_zip/Cargo.toml del dev-dependencies.derive_more
tomcli set crates/async_zip/Cargo.toml del dev-dependencies.uuid

# See comments above Source200:
%setup -q -T -D -b 200 -n uv-%{version}
ln -s '../../pubgrub-%{pubgrub_rev}' crates/pubgrub
git2path workspace.dependencies.pubgrub crates/pubgrub
pushd crates/pubgrub
%autopatch -p1 -m200 -M299
popd
install -t LICENSE.bundled/pubgrub -D -p -m 0644 crates/pubgrub/LICENSE
# Drop a benchmark-only dev-dependency.
tomcli set crates/pubgrub/Cargo.toml del dev-dependencies.criterion
# Omit tests requiring varisat; it is not packaged and has significant
# dependencies of its own.
tomcli set crates/pubgrub/Cargo.toml del dev-dependencies.varisat
mv crates/pubgrub/tests/proptest.rs{,.disabled}
mv crates/pubgrub/tests/sat_dependency_provider.rs{,.disabled}
# We can’t have two workspaces!
tomcli set crates/pubgrub/Cargo.toml del workspace
# Note that install does always dereference symlinks, which is what we want:
install -t LICENSE.bundled/version-ranges -D -p -m 0644 \
    crates/pubgrub/version-ranges/LICENSE
git2path workspace.dependencies.version-ranges crates/pubgrub/version-ranges

# See comments above Source400:
%setup -q -T -D -b 400 -n uv-%{version}
ln -s '../../tl-%{tl_rev}' crates/tl
git2path workspace.dependencies.tl crates/tl
pushd crates/tl
%autopatch -p1 -m400 -M499
popd
install -t LICENSE.bundled/tl -D -p -m 0644 crates/tl/LICENSE
# Drop a benchmark-only dev-dependency.
tomcli set crates/tl/Cargo.toml del dev-dependencies.criterion

# Collect license files of vendored dependencies in the main source archive
install -t LICENSE.bundled/packaging -D -p -m 0644 \
    crates/uv-python/python/packaging/LICENSE.*
install -t LICENSE.bundled/pep440_rs -D -p -m 0644 crates/uv-pep440/License-*
install -t LICENSE.bundled/pep508_rs -D -p -m 0644 crates/uv-pep508/License-*
install -t LICENSE.bundled/ripunzip -D -p -m 0644 \
    crates/uv-extract/src/vendor/LICENSE
# The original license text from rattler_installs_packages is present in a
# comment, but we want it in a separate file so we can ensure it is present in
# the binary RPM.
install -d LICENSE.bundled/rattler_installs_packages
awk '$2 == "BSD" { out=1 }; $2 == "```" { out=0 }; out' \
    crates/uv-client/src/remote_metadata.rs |
  sed -r 's@^///( |$)@@' |
  tee LICENSE.bundled/rattler_installs_packages/LICENSE
# Similarly for virtualenv. All files in
# crates/uv-virtualenv/src/activator/activate/ have the same license text.
install -d LICENSE.bundled/virtualenv
awk '$1 == "#" { out=1 }; $1 != "#" { out=0; exit }; out' \
    crates/uv-virtualenv/src/activator/activate |
  sed -r 's@^#( |$)@@' |
  tee LICENSE.bundled/virtualenv/LICENSE

# Patch out foreign (e.g. Windows-only) dependencies. Follow symbolic links so
# that we also patch the bundled crates we just finished setting up.
find -L . -type f -name Cargo.toml -print \
    -execdir rust2rpm-helper strip-foreign -o '{}' '{}' ';'

# The uv-trampoline crate (a fork of posy trampolines, from
# https://github.com/njsmith/posy) contains a set of trampoline Windows
# executables for launching Python scripts. We must remove these to prove they
# are not used in the build (and since they are only used on Windows, nothing
# is lost by doing so).
rm -v crates/uv-trampoline/trampolines/*.exe
# Per Cargo.toml, uv-trampoline is excluded from the workspace and not
# compiled because it still requires a nightly compiler. For now, we remove it
# entirely to show that we do not need to document bundling from posy.
rm -rv crates/uv-trampoline

# Do not strip the compiled executable; we need useful debuginfo. Upstream set
# this intentionally, so this change makes sense to keep downstream-only.
tomcli set pyproject.toml false tool.maturin.strip
tomcli set Cargo.toml false profile.release.strip

# Exclude the bench crate from the workspace. We don’t need to build and run
# benchmarks, and it brings in unwanted additional dev dependencies.
tomcli set Cargo.toml append workspace.exclude crates/uv-bench
# The uv-dev crate provides “development utilities for uv,” which should not be
# needed here, and it also brings in extra dependencies that we would prefer to
# do without.
tomcli set Cargo.toml append workspace.exclude crates/uv-dev

# Do not request static linking of anything (particularly, liblzma)
tomcli set crates/uv/Cargo.toml lists delitem \
    features.default 'uv-distribution/static'
tomcli set crates/uv-distribution/Cargo.toml del features.static
tomcli set crates/uv-extract/Cargo.toml del features.static

# Disable several default features that control which tests are compiled and
# executed, and which are not usable in offline builds:
#
# - crates-io: Introduces a testing dependency on crates.io.
# - git: Introduces a testing dependency on Git. This sounds innocuous – we
#   have git! – but in fact, it controls tests of git dependencies, which
#   implies accessing remote repositories, e.g. on GitHub.
# - pypi: Introduces a testing dependency on PyPI.
# - python-managed: Introduces a testing dependency on managed Python
#   installations. (These are pre-compiled Pythons downloaded from the
#   Internet.)
#
# These are OK:
# - python: Introduces a testing dependency on a local Python installation.
# - slow-tests: Include "slow" test cases.
# - test-ecosystem: Includes test cases that require ecosystem packages
#
# Note that the python-patch feature, which ”introduces a dependency on a local
# Python installation with specific patch versions,” is already not among the
# default features.
tomcli set crates/uv/Cargo.toml lists delitem features.default-tests \
    '(crates-io|git|pypi|python-managed)'

%if %{without it}
# Integration tests (it crate) nearly all require specific Python interpreter
# versions (major.minor, not major.minor.patch, unless the python-patch feature
# is enabled). We might choose to disable this in order to double-check that
# everything else works well with only the primary system Python in the
# environment.
# -p uv --test it:
mods="${mods-}${mods+|}branching_urls"
mods="${mods-}${mods+|}build_backend"
mods="${mods-}${mods+|}pip_(check|list|show|tree|uninstall)"
mods="${mods-}${mods+|}python_(dir|find|install|list|pin)"
mods="${mods-}${mods+|}venv"
mods="${mods-}${mods+|}version"
mods="${mods-}${mods+|}workspace"
comment='Downstream-only: skip, needs specific Python interpreter versions'
sed -r -i "s@mod (${mods});@// ${comment}\n#[cfg(any())]\n&@" \
    crates/uv/tests/it/main.rs
%endif

# For unclear reasons, maturin checks for the presence of optional crate
# dependencies that correspond to features we have not enabled. We need to
# patch out those that are not packaged, an unfortunate but straightforward
# hack. See further commentary in %%generate_buildrequires.
tomcli set crates/uv/Cargo.toml del dependencies.axoupdater
tomcli set crates/uv/Cargo.toml del features.self-update
tomcli set crates/uv/Cargo.toml del features.tracing-durations-export
tomcli set crates/uv/Cargo.toml del dependencies.tracing-durations-export

# Loosen some version bounds that were aggressively updated upstream by the
# renovate bot. We retain this comment and the following example even when
# there are currently no dependencies that need to be adjusted.
#
# # foocrate
# #   wanted: 0.2.0
# #   currently packaged: 0.1.2
# #   https://bugzilla.redhat.com/show_bug.cgi?id=1234567
# tomcli set crates/uv/Cargo.toml str dev-dependencies.foocrate.version 0.1.2

# which
#   wanted: 7.0.3
#   currently packaged: 7.0.3, but planning to update to 8.0.0
#   https://bugzilla.redhat.com/show_bug.cgi?id=1234567
#   Updated upstream in uv 0.4.13.
tomcli set Cargo.toml str workspace.dependencies.which.version \
    '>=7.0.0, <9.0.0'

%cargo_prep


%generate_buildrequires
# For unclear reasons, maturin checks for all crate dependencies when it is
# invoked as part of %%pyproject_buildrequires – including those corresponding
# to optional features.
#
# Furthermore, if we do not supply -a to %%cargo_generate_buildrequires, then
# maturin will fail looking for crates like pyo3 (and will still look for
# optional crate dependencies).
#
# Since maturin always checks for dev-dependencies, we need -t so that they are
# generated even when the “check” bcond is disabled.
%cargo_generate_buildrequires -a -t
# These crates are excluded from the workspace – upstream writes:
#   Only used to pull in features, allocators, etc. — we specifically don't
#   want them to be part of a workspace-wide cargo check, cargo clippy, etc.
#   – but they are still needed to support features, and the build will fail if
#   we do not generate their dependencies, too:
for cratedir in \
    crates/uv-performance-memory-allocator
do
  pushd "${cratedir}" >/dev/null
  %cargo_generate_buildrequires -a -t
  popd >/dev/null
done
%pyproject_buildrequires


%build
%pyproject_wheel

%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

# TODO: Since the --help output interacts well with help2man, use it to
# generate man pages: ideally, a man page for each (sub)command
# cross-referenced appropriately. (There are many subcommands, and this would
# be tedious to do manually.) This should be feasible with the --include option
# to help2man and a bit of scripting, but we choose to ship the initial package
# without man pages and defer this to a later effort.


%install
%pyproject_install
%pyproject_save_files uv

if [ '%{python3_sitearch}' != '%{python3_sitelib}' ]
then
  # Maturin is really designed to build compiled Python extensions, but (when
  # the uv executable is not bundled in the Python package) the uv Python
  # library is actually pure-Python, and the python3-uv subpackage can be
  # noarch. We can’t tell maturin to install to the appropriate site-packages
  # directory, but we can fix the installation path manually.
  install -d %{buildroot}%{python3_sitelib}
  mv %{buildroot}%{python3_sitearch}/uv* %{buildroot}%{python3_sitelib}
  sed -r -i 's@%{python3_sitearch}@%{python3_sitelib}@' %{pyproject_files}
fi

# generate and install shell completions
for cmd in uv uvx
do
  target/rpm/${cmd} --generate-shell-completion bash > ${cmd}.bash
  target/rpm/${cmd} --generate-shell-completion fish > ${cmd}.fish
  target/rpm/${cmd} --generate-shell-completion zsh > _${cmd}

  install -Dpm 0644 ${cmd}.bash -t %{buildroot}/%{bash_completions_dir}
  install -Dpm 0644 ${cmd}.fish -t %{buildroot}/%{fish_completions_dir}
  install -Dpm 0644 _${cmd} -t %{buildroot}/%{zsh_completions_dir}
done

# Install a default system-wide configuration file
install -t '%{buildroot}%{_sysconfdir}/uv' -p -m 0644 -D '%{SOURCE1}'


%check
%if %{with check}
# These tests rely on debug assertions, and fail when tests are compiled in
# release mode:
#
# cargo test -p uv-auth --lib:
skip="${skip-} --skip keyring::tests::fetch_url_no_host"
skip="${skip-} --skip keyring::tests::fetch_url_with_empty_username"
skip="${skip-} --skip keyring::tests::fetch_url_with_no_username"
skip="${skip-} --skip keyring::tests::fetch_url_with_password"

%if %{without it}
# These tests require specific Python interpreter versions, which upstream
# normally downloads, precompiled, into the build area.
# -p uv --test it:
skip="${skip-} --skip version::self_version"
skip="${skip-} --skip version::self_version_json"
skip="${skip-} --skip version::self_version_short"
%else
%ifnarch %{x86_64} %{arm64}
# On other architectures, the list of available downloads differs, e.g. pypy
# and graalpy downloads may be missing.
skip="${skip-} --skip python_list::python_list_downloads"
%endif
%endif
# -p uv-client --test it:
# This requires specific Python interpreter versions (so it would be grouped
# with the conditionalized integration tests above), but it also requires
# network access to PyPI, so it must be skipped either way until it can be
# appropriately conditionalized upstream; see
# https://github.com/astral-sh/uv/pull/13699#issuecomment-2916115588.
skip="${skip-} --skip remote_metadata::remote_metadata_with_and_without_cache"

%if %[ %{defined fc41} || %{defined fc40} || %{defined el10} || %{defined el9} ]
# Trivial difference in snapshots: packages appear in a different order.
skip="${skip-} --skip lock::tests::missing_dependency_source_unambiguous"
skip="${skip-} --skip lock::tests::missing_dependency_version_dynamic"
skip="${skip-} --skip lock::tests::missing_dependency_source_version_unambiguous"
skip="${skip-} --skip lock::tests::missing_dependency_version_unambiguous"
%endif

# TODO: What’s going wrong here? It doesn’t seem serious…
# thread 'middleware::tests::test_tracing_url' panicked at
#   crates/uv-auth/src/middleware.rs:2095:5:
# Could not set global tracing subscriber: SetGlobalDefaultError("a global
#   default trace dispatcher has already been set")
skip="${skip-} --skip middleware::tests::test_tracing_url"

# Upstream is trying to ensure platform-independent byte-for-byte deterministic
# wheels. This isn’t quite working out. It would be nice to understand this,
# but this kind of reproducibility can be brittle, and there are many possible
# innocuous reasons behind it.
# ---- tests::built_by_uv_building stdout ----
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Snapshot Summary ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Snapshot: built_by_uv_building-6
# Source: crates/uv-build-backend/src/lib.rs:516
# ────────────────────────────────────────────────────────────────────────────────
# Expression: format!("{:x}", sha2::Sha256::digest(&index_wheel_contents))
# ────────────────────────────────────────────────────────────────────────────────
# -old snapshot
# +new results
# ────────────┬───────────────────────────────────────────────────────────────────
#     0       │-ac3f68ac448023bca26de689d80401bff57f764396ae802bf4666234740ffbe3
#           0 │+7ba9bfcaf3c0354c2cb8578922a00726b1ff6bdfa85fcb738bd45978fa86fd0a
# ────────────┴───────────────────────────────────────────────────────────────────
skip="${skip-} --skip tests::built_by_uv_building"

%cargo_test -- -- --exact ${skip-}
%endif

%pyproject_check_import


%files
%license LICENSE-APACHE LICENSE-MIT LICENSE.dependencies LICENSE.bundled/
%doc CHANGELOG.md
%doc README.md
%doc PIP_COMPATIBILITY.md

%{_bindir}/uv
# Equivalent to “uv tool run”:
%{_bindir}/uvx

%{bash_completions_dir}/{uv,uvx}.bash
%{fish_completions_dir}/{uv,uvx}.fish
%{zsh_completions_dir}/_{uv,uvx}

%dir %{_sysconfdir}/uv
%config(noreplace) %{_sysconfdir}/uv/uv.toml


%files -n python3-uv -f %{pyproject_files}


%changelog
%autochangelog
