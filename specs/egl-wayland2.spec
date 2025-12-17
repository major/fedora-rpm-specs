%global commit0 ada1c37041002f4f009a33d6d285eae39bf9ad02
%global date 20251213
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:           egl-wayland2
Version:        1.0.1%{!?tag:~%{date}git%{shortcommit0}}
Release:        %autorelease
Summary:        Dma-buf-based Wayland external platform library
# src/wayland/dma-buf.h is GPL 2, rest is Apache 2.0
License:        Apache-2.0 and GPL-2.0
URL:            https://github.com/NVIDIA/%{name}

%if 0%{?tag:1}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
%endif

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  libtool
BuildRequires:  pkgconfig(egl) >= 1.5
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.1
BuildRequires:  pkgconfig(gbm) >= 21.2.0
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
BuildRequires:  pkgconfig(wayland-protocols) >= 1.38
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)

# Required for directory ownership
Requires:       libglvnd-egl%{?_isa}

%description
This is a new implementation of the EGL External Platform Library for Wayland
(EGL_KHR_platform_wayland), using the NVIDIA driver's new platform surface
interface, which simplifies a lot of the library and improves window resizing.

%prep
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}%{_libdir}/libnvidia-egl-wayland2.so

%files
%doc README.md
%license LICENSE
%{_libdir}/libnvidia-egl-wayland2.so.1
%{_libdir}/libnvidia-egl-wayland2.so.1.*
%{_datadir}/egl/egl_external_platform.d/09_nvidia_wayland2.json

%changelog
%autochangelog
