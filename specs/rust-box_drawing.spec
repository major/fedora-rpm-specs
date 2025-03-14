# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate box_drawing

Name:           rust-box_drawing
Version:        0.1.2
Release:        %autorelease
Summary:        Very simple library containing constants for UTF-8 box drawing

License:        MIT
URL:            https://crates.io/crates/box_drawing
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
A very simple library containing constants for UTF-8 box drawing.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
