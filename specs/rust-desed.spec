# Generated by rust2rpm 27
%bcond check 1

%global crate desed

Name:           rust-desed
Version:        1.2.2
Release:        %autorelease
Summary:        Sed script debugger

License:        GPL-3.0-or-later
URL:            https://crates.io/crates/desed
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          desed-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * Update inotify dependency from 0.10.0 to 0.11.0:
#   https://github.com/SoptikHa2/desed/pull/35
# * Bump ratatui dependency to 0.29 https://github.com/SoptikHa2/desed/pull/36
Patch:          desed-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Sed script debugger. Debug and demystify your sed scripts with TUI
debugger.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# GPL-3.0-or-later
# ISC
# MIT
# MIT OR Apache-2.0
# Zlib
License:        GPL-3.0-or-later AND ISC AND MIT AND Zlib AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
# LICENSE.dependencies contains a full license breakdown
Requires:       sed >= 4.6

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/desed

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
