# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate vhost-user-backend

Name:           rust-vhost-user-backend
Version:        0.17.0
Release:        %autorelease
Summary:        Framework to build vhost-user backend service daemon

License:        Apache-2.0
URL:            https://crates.io/crates/vhost-user-backend
Source0:        %{crates_source}
Source1:        https://raw.githubusercontent.com/rust-vmm/vhost/main/LICENSE

# We depend on rust-vmm crates that don't support 32 bit targets
ExcludeArch:    %{ix86}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A framework to build vhost-user backend service daemon.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
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

%package     -n %{name}+postcopy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+postcopy-devel %{_description}

This package contains library source intended for building other packages which
use the "postcopy" feature of the "%{crate}" crate.

%files       -n %{name}+postcopy-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+userfaultfd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+userfaultfd-devel %{_description}

This package contains library source intended for building other packages which
use the "userfaultfd" feature of the "%{crate}" crate.

%files       -n %{name}+userfaultfd-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+xen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xen-devel %{_description}

This package contains library source intended for building other packages which
use the "xen" feature of the "%{crate}" crate.

%files       -n %{name}+xen-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
cp -pav %{SOURCE1} .

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
