# Generated by rust2rpm 24
%bcond_without check

%global crate heatseeker

Name:           rust-heatseeker
Version:        1.7.1
Release:        %autorelease
Summary:        Fast, robust, and portable fuzzy finder

License:        MIT
URL:            https://crates.io/crates/heatseeker
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          heatseeker-fix-metadata-auto.diff

BuildRequires:  rust-packaging >= 23

%global _description %{expand:
A fast, robust, and portable fuzzy finder.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 AND BSD-2-Clause
License:        MIT AND BSD-2-Clause AND (Apache-2.0 OR MIT)
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/hs

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
export TRAVIS=1
%cargo_test
%endif

%changelog
%autochangelog