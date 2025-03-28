# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

# prevent executables from being installed
%global cargo_install_bin 0

%global crate uu_whoami

Name:           rust-uu_whoami
Version:        0.0.27
Release:        %autorelease
Summary:        whoami ~ (uutils) display user name of current effective user ID

License:        MIT
URL:            https://crates.io/crates/uu_whoami
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          uu_whoami-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
whoami ~ (uutils) display user name of current effective user ID.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/whoami.md
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
%autosetup -n %{crate}-%{version} -p1
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
