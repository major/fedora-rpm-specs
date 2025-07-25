# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate ashpd

Name:           rust-ashpd
Version:        0.11.0
Release:        %autorelease
Summary:        XDG portals wrapper in Rust using zbus

License:        MIT
URL:            https://crates.io/crates/ashpd
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
XDG portals wrapper in Rust using zbus.}

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

%package     -n %{name}+async-std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-std-devel %{_description}

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%files       -n %{name}+async-std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-trait-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-trait-devel %{_description}

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%files       -n %{name}+async-trait-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backend-devel %{_description}

This package contains library source intended for building other packages which
use the "backend" feature of the "%{crate}" crate.

%files       -n %{name}+backend-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gdk4wayland-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gdk4wayland-devel %{_description}

This package contains library source intended for building other packages which
use the "gdk4wayland" feature of the "%{crate}" crate.

%files       -n %{name}+gdk4wayland-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gdk4x11-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gdk4x11-devel %{_description}

This package contains library source intended for building other packages which
use the "gdk4x11" feature of the "%{crate}" crate.

%files       -n %{name}+gdk4x11-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+glib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glib-devel %{_description}

This package contains library source intended for building other packages which
use the "glib" feature of the "%{crate}" crate.

%files       -n %{name}+glib-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gtk4-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gtk4-devel %{_description}

This package contains library source intended for building other packages which
use the "gtk4" feature of the "%{crate}" crate.

%files       -n %{name}+gtk4-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gtk4_wayland-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gtk4_wayland-devel %{_description}

This package contains library source intended for building other packages which
use the "gtk4_wayland" feature of the "%{crate}" crate.

%files       -n %{name}+gtk4_wayland-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gtk4_x11-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gtk4_x11-devel %{_description}

This package contains library source intended for building other packages which
use the "gtk4_x11" feature of the "%{crate}" crate.

%files       -n %{name}+gtk4_x11-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pipewire-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pipewire-devel %{_description}

This package contains library source intended for building other packages which
use the "pipewire" feature of the "%{crate}" crate.

%files       -n %{name}+pipewire-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+raw-window-handle-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+raw-window-handle-devel %{_description}

This package contains library source intended for building other packages which
use the "raw-window-handle" feature of the "%{crate}" crate.

%files       -n %{name}+raw-window-handle-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+raw_handle-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+raw_handle-devel %{_description}

This package contains library source intended for building other packages which
use the "raw_handle" feature of the "%{crate}" crate.

%files       -n %{name}+raw_handle-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tracing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tracing-devel %{_description}

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%files       -n %{name}+tracing-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wayland-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wayland-devel %{_description}

This package contains library source intended for building other packages which
use the "wayland" feature of the "%{crate}" crate.

%files       -n %{name}+wayland-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wayland-backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wayland-backend-devel %{_description}

This package contains library source intended for building other packages which
use the "wayland-backend" feature of the "%{crate}" crate.

%files       -n %{name}+wayland-backend-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wayland-client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wayland-client-devel %{_description}

This package contains library source intended for building other packages which
use the "wayland-client" feature of the "%{crate}" crate.

%files       -n %{name}+wayland-client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wayland-protocols-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wayland-protocols-devel %{_description}

This package contains library source intended for building other packages which
use the "wayland-protocols" feature of the "%{crate}" crate.

%files       -n %{name}+wayland-protocols-devel
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
