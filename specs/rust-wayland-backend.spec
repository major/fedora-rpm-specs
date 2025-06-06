# Generated by rust2rpm 27
# * tests can only be run in-tree
%bcond check 0
%global debug_package %{nil}

%global crate wayland-backend

Name:           rust-wayland-backend
Version:        0.3.10
Release:        %autorelease
Summary:        Low-level bindings to the Wayland protocol

License:        MIT
URL:            https://crates.io/crates/wayland-backend
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Low-level bindings to the Wayland protocol.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
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

%package     -n %{name}+client_system-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+client_system-devel %{_description}

This package contains library source intended for building other packages which
use the "client_system" feature of the "%{crate}" crate.

%files       -n %{name}+client_system-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dlopen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dlopen-devel %{_description}

This package contains library source intended for building other packages which
use the "dlopen" feature of the "%{crate}" crate.

%files       -n %{name}+dlopen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+raw-window-handle-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+raw-window-handle-devel %{_description}

This package contains library source intended for building other packages which
use the "raw-window-handle" feature of the "%{crate}" crate.

%files       -n %{name}+raw-window-handle-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rwh_06-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rwh_06-devel %{_description}

This package contains library source intended for building other packages which
use the "rwh_06" feature of the "%{crate}" crate.

%files       -n %{name}+rwh_06-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+server_system-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+server_system-devel %{_description}

This package contains library source intended for building other packages which
use the "server_system" feature of the "%{crate}" crate.

%files       -n %{name}+server_system-devel
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
