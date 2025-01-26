%bcond_without check

# reduce peak memory usage
%constrain_build -m 4096

# replacements for git snapshot dependencies
%global lsp_types_commit    3512a9f33eadc5402cfab1b8f7340824c8ca1439
%global salsa_commit        88a1d7774d78f048fbd77d40abca9ebd729fd1f0

Name:           ruff
Version:        0.8.6
Release:        %autorelease
Summary:        Extremely fast Python linter and code formatter

# ruff:                         MIT
# bundled typeshed snapshot:    (Apache-2.0 AND MIT)
# bundled lsp-types fork:       MIT
# bundled salsa snapshot:       (Apache-2.0 OR MIT)
SourceLicense:  MIT AND Apache-2.0 AND (Apache-2.0 OR MIT)

# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 OR BSD-2-Clause
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# CC0-1.0
# ISC
# MIT
# MIT AND (MIT AND PSF-2.0)
# MIT AND BSD-3-Clause
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR BSD-3-Clause
# MIT-0 OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# WTFPL
# Zlib OR Apache-2.0 OR MIT

License:        %{shrink:
    MIT AND
    Apache-2.0 AND
    BSD-3-Clause AND
    CC0-1.0 AND
    ISC AND
    MPL-2.0 AND
    PSF-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    WTFPL AND
    (Apache-2.0 OR BSD-2-Clause) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (MIT OR BSD-3-Clause) AND
    (MIT-0 OR Apache-2.0) AND
    (Unlicense OR MIT)
}

URL:            https://github.com/astral-sh/ruff
Source:         %{url}/archive/%{version}/ruff-%{version}.tar.gz

Source1:        https://github.com/astral-sh/lsp-types/archive/%{lsp_types_commit}/lsp-types-%{lsp_types_commit}.tar.gz
Source2:        https://github.com/salsa-rs/salsa/archive/%{salsa_commit}/salsa-%{salsa_commit}.tar.gz
Source3:        avoid-duplicate-workspace-definitions.patch

# * drop non-Linux dependencies (non-upstreamable), generated with:
#   "for i in $(find -name Cargo.toml) ; do rust2rpm-helper strip-foreign $i -o $i ; done"
Patch:          0001-drop-Windows-and-macOS-specific-dependencies.patch
# * replace git snapshot dependencies with path-based dependencies from
#   unpacked additional sources (non-upstreamable)
Patch:          0002-replace-git-snapshot-dependencies-with-path-dependen.patch
# * drop unavailable custom memory allocators (non-upstreamable)
Patch:          0003-remove-unavailable-custom-allocators.patch
# * do not strip debuginfo from the built executable (non-upstreamable)
Patch:          0004-do-not-strip-debuginfo-from-built-binary-executable.patch
# * relax pyproject-toml-dependency (non-upstreamable):
Patch:          0005-relax-pyproject-toml-dependency-to-allow-0.11.-0.13.patch
# * drop unavailable compile-time diagnostics feature for UUIDs (non-upstreamable)
Patch:          0006-drop-unavailable-features-from-uuid-dependency.patch
# * temporarily downgrade pep440_rs dependency from 0.7 to 0.6 (non-upstreamable)
Patch:          0007-temporarily-downgrade-pep440_rs-from-0.7-to-0.6.patch
# * bump notify dependency from 7 to 8:
#   https://github.com/astral-sh/ruff/commit/36c90eb
Patch:          0008-bump-notify-dependency-from-7-to-8.patch

ExcludeArch:	%{ix86}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  python3-devel

# git snapshot of the python/typeshed project at commit 9e506eb:
# https://github.com/python/typeshed
Provides:       bundled(typeshed)

# forked from lsp-types upstream: https://github.com/gluon-lang/lsp-types
# with changes applied:           https://github.com/astral-sh/lsp-types/tree/notebook-support
Provides:       bundled(crate(lsp-types)) = 0.95.1

# git snapshot of unreleased upstream at some point after v0.18.0:
# https://github.com/salsa-rs/salsa/commit/b14be5c
Provides:       bundled(crate(salsa)) = 0.18.0
Provides:       bundled(crate(salsa-macros)) = 0.18.0
Provides:       bundled(crate(salsa-macro-rules)) = 0.1.0

%description
An extremely fast Python linter and code formatter, written in Rust.

Ruff aims to be orders of magnitude faster than alternative tools while
integrating more functionality behind a single, common interface.

Ruff can be used to replace Flake8 (plus dozens of plugins), Black,
isort, pydocstyle, pyupgrade, autoflake, and more, all while executing
tens or hundreds of times faster than any individual tool.

%prep
%autosetup -n ruff-%{version} -p1
%cargo_prep

# move git snapshot replacements into place
tar -xzvf %{SOURCE1}
tar -xzvf %{SOURCE2}
mv lsp-types-%{lsp_types_commit} crates/lsp-types
mv salsa-%{salsa_commit} crates/salsa

# avoid duplicate workspace definitions
pushd crates/salsa
patch -p1 < %{SOURCE3}
mv components/* ../
popd

# prepare license files under distinct names
cp -pav crates/lsp-types/LICENSE LICENSE.lsp-types
cp -pav crates/salsa/LICENSE-APACHE LICENSE-APACHE.salsa
cp -pav crates/salsa/LICENSE-MIT LICENSE-MIT.salsa
cp -pav crates/red_knot_vendored/vendor/typeshed/LICENSE LICENSE.typeshed

# drop unused subprojects
rm -rv crates/red_knot_wasm
rm -rv crates/ruff_benchmark
rm -rv crates/ruff_wasm

%generate_buildrequires
%pyproject_buildrequires
%cargo_generate_buildrequires -a

%build
export RUSTFLAGS="%{build_rustflags}"
%pyproject_wheel

# write license summary and breakdown
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%pyproject_install
%pyproject_save_files ruff

# generate and install shell completions
target/rpm/ruff generate-shell-completion bash > ruff.bash
target/rpm/ruff generate-shell-completion fish > ruff.fish
target/rpm/ruff generate-shell-completion zsh > _ruff

install -Dpm 0644 ruff.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 ruff.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _ruff -t %{buildroot}/%{zsh_completions_dir}

%if %{with check}
%check
# ignore false positive snapshot test failures
export INSTA_UPDATE=always
export TRYBUILD=overwrite
# reduce peak memory usage
%cargo_test -- -- --test-threads 2
%endif

%files -f %{pyproject_files}
%license LICENSE
%license LICENSE.lsp-types
%license LICENSE-APACHE.salsa
%license LICENSE-MIT.salsa
%license LICENSE.typeshed
%license LICENSE.dependencies
%doc README.md
%doc BREAKING_CHANGES.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md

%{_bindir}/ruff

%{bash_completions_dir}/ruff.bash
%{fish_completions_dir}/ruff.fish
%{zsh_completions_dir}/_ruff

%changelog
%autochangelog
