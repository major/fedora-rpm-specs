# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate hyperlocal

Name:           rust-hyperlocal
Version:        0.9.1
Release:        %autorelease
Summary:        Hyper bindings for Unix domain sockets

License:        MIT
URL:            https://crates.io/crates/hyperlocal
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Hyper bindings for Unix domain sockets.}

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

%package     -n %{name}+client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+client-devel %{_description}

This package contains library source intended for building other packages which
use the "client" feature of the "%{crate}" crate.

%files       -n %{name}+client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http-body-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-body-util-devel %{_description}

This package contains library source intended for building other packages which
use the "http-body-util" feature of the "%{crate}" crate.

%files       -n %{name}+http-body-util-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hyper-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hyper-util-devel %{_description}

This package contains library source intended for building other packages which
use the "hyper-util" feature of the "%{crate}" crate.

%files       -n %{name}+hyper-util-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+server-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+server-devel %{_description}

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%files       -n %{name}+server-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tower-service-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tower-service-devel %{_description}

This package contains library source intended for building other packages which
use the "tower-service" feature of the "%{crate}" crate.

%files       -n %{name}+tower-service-devel
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
