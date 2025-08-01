# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate glutin

Name:           rust-glutin
Version:        0.32.3
Release:        %autorelease
Summary:        Cross-platform OpenGL context provider

License:        Apache-2.0
URL:            https://crates.io/crates/glutin
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          glutin-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Cross-platform OpenGL context provider.}

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

%package     -n %{name}+egl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+egl-devel %{_description}

This package contains library source intended for building other packages which
use the "egl" feature of the "%{crate}" crate.

%files       -n %{name}+egl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+glutin_egl_sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glutin_egl_sys-devel %{_description}

This package contains library source intended for building other packages which
use the "glutin_egl_sys" feature of the "%{crate}" crate.

%files       -n %{name}+glutin_egl_sys-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+glutin_glx_sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glutin_glx_sys-devel %{_description}

This package contains library source intended for building other packages which
use the "glutin_glx_sys" feature of the "%{crate}" crate.

%files       -n %{name}+glutin_glx_sys-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+glx-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glx-devel %{_description}

This package contains library source intended for building other packages which
use the "glx" feature of the "%{crate}" crate.

%files       -n %{name}+glx-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libloading-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libloading-devel %{_description}

This package contains library source intended for building other packages which
use the "libloading" feature of the "%{crate}" crate.

%files       -n %{name}+libloading-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wayland-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wayland-devel %{_description}

This package contains library source intended for building other packages which
use the "wayland" feature of the "%{crate}" crate.

%files       -n %{name}+wayland-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wayland-sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wayland-sys-devel %{_description}

This package contains library source intended for building other packages which
use the "wayland-sys" feature of the "%{crate}" crate.

%files       -n %{name}+wayland-sys-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wgl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wgl-devel %{_description}

This package contains library source intended for building other packages which
use the "wgl" feature of the "%{crate}" crate.

%files       -n %{name}+wgl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+x11-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+x11-devel %{_description}

This package contains library source intended for building other packages which
use the "x11" feature of the "%{crate}" crate.

%files       -n %{name}+x11-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+x11-dl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+x11-dl-devel %{_description}

This package contains library source intended for building other packages which
use the "x11-dl" feature of the "%{crate}" crate.

%files       -n %{name}+x11-dl-devel
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
