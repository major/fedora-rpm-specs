# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate terminfo

Name:           rust-terminfo
Version:        0.7.3
Release:        %autorelease
Summary:        Terminal information

License:        WTFPL
URL:            https://crates.io/crates/terminfo
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Terminal information.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
# FIXME: no license files detected
%doc %{crate_instdir}/README.md
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
# * doctests fail without a TTY
%cargo_test -- --lib
%endif

%changelog
%autochangelog