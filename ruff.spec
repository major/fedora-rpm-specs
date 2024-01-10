%bcond_without check

# reduce peak memory usage
%constrain_build -m 4096

Name:           ruff
Version:        0.1.11
Release:        %autorelease
Summary:        Extremely fast Python linter

SourceLicense:  MIT
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD
# Apache-2.0
# Apache-2.0 OR BSD-2-Clause
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-2-Clause-Views
# CC0-1.0
# ISC
# MIT
# MIT AND PSF-2.0
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR BSD-3-Clause
# MPL-2.0
# Unlicense OR MIT
# WTFPL
# Zlib OR Apache-2.0 OR MIT
License:        MIT AND 0BSD AND Apache-2.0 AND BSD-2-Clause-Views AND CC0-1.0 AND ISC AND MPL-2.0 AND PSD-2.0 AND Unicode-DFS-2016 AND WTFPL AND (Apache-2.0 OR BSD-2-Clause) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR BSD-3-Clause) AND (Unlicense OR MIT)

URL:            https://github.com/astral-sh/ruff
Source:         %{url}/archive/v%{version}/ruff-%{version}.tar.gz

# * drop Windows-specific dependencies (non-upstreamable), generated with:
#   "for i in $(find -name Cargo.toml) ; do rust2rpm-helper strip-foreign $i -o $i ; done"
Patch:          0001-drop-Windows-specific-dependencies.patch
# * drop unavailable compile-time diagnostics feature for UUIDs (non-upstreamable)
Patch:          0002-drop-unavailable-features-from-uuid-dependency.patch
# * drop unavailable custom memory allocators (non-upstreamable)
Patch:          0003-remove-unavailable-custom-allocators.patch
# * do not strip debuginfo from the built executable (non-upstreamable)
Patch:          0004-do-not-strip-debuginfo-from-built-binary-executable.patch

ExcludeArch:	%{ix86}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  python3-devel

%description
An extremely fast Python linter, written in Rust.

Ruff aims to be orders of magnitude faster than alternative tools while
integrating more functionality behind a single, common interface.

Ruff can be used to replace Flake8 (plus dozens of plugins), isort,
pydocstyle, yesqa, eradicate, pyupgrade, and autoflake, all while
executing tens or hundreds of times faster than any individual tool.

%prep
%autosetup -n ruff-%{version} -p1
%cargo_prep
# drop unused subprojects
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
target/rpm/ruff --generate-shell-completion bash > ruff.bash
target/rpm/ruff --generate-shell-completion fish > ruff.fish
target/rpm/ruff --generate-shell-completion zsh > _ruff

install -Dpm 0644 ruff.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 ruff.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _ruff -t %{buildroot}/%{zsh_completions_dir}

%if %{with check}
%check
# ignore false positive snapshot test failures
export INSTA_UPDATE=always
# reduce peak memory usage
%cargo_test -- -- --test-threads 2
%endif

%files -f %{pyproject_files}
%license LICENSE
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
