# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate mktemp

Name:           rust-mktemp
Version:        0.5.1
Release:        %autorelease
Summary:        Create temporary files and directories

License:        MPL-2.0
URL:            https://crates.io/crates/mktemp
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * relax uuid dependency
Patch:          mktemp-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Mktemp files and directories.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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
%cargo_test
%endif

%changelog
%autochangelog
