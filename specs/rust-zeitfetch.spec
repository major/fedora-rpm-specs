# Generated by rust2rpm 26
%bcond_without check

%global crate zeitfetch

Name:           rust-zeitfetch
Version:        0.1.14
Release:        %autorelease
Summary:        Instantaneous snapshots of cross-platform system information

License:        MIT
URL:            https://crates.io/crates/zeitfetch
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          zeitfetch-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Instantaneous snapshots of cross-platform system information.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# BSD-3-Clause
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        MIT AND BSD-3-Clause AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/zeitfetch

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
