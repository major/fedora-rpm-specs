%global commit0 61e70b08ecc1e833b01f11507a74da2f3a140aee
%global date 20241213
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:           egl-x11
Version:        1.0.1%{!?tag:~%{date}git%{shortcommit0}}
Release:        2%{?dist}
Summary:        NVIDIA XLib and XCB EGL Platform Library
License:        Apache-2.0
URL:            https://github.com/NVIDIA/egl-x11

%if 0%{?tag:1}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif
# Allow building with an older meson:
Patch0:         egl-x11-meson-0.58.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.2
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 21.3.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.99
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
# Minimum version 1.17.0 for explicit sync support (Fedora 40+):
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)

# Required for directory ownership
Requires:       libglvnd-egl%{?_isa}

%description
This is an EGL platform library for the NVIDIA driver to support XWayland via
xlib (using EGL_KHR_platform_x11) or xcb (using EGL_EXT_platform_xcb).

%prep
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif

%build
%meson \
  -D xcb=true \
  -D xlib=enabled
%meson_build

%install
%meson_install

rm -fv %{buildroot}%{_libdir}/*.so

%files
%license LICENSE
%doc README.md
%{_libdir}/libnvidia-egl-xcb.so.1
%{_libdir}/libnvidia-egl-xcb.so.1.0.1
%{_libdir}/libnvidia-egl-xlib.so.1
%{_libdir}/libnvidia-egl-xlib.so.1.0.1
%{_datadir}/egl/egl_external_platform.d/20_nvidia_xcb.json
%{_datadir}/egl/egl_external_platform.d/20_nvidia_xlib.json

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1~20241213git61e70b0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 16 2024 Simone Caronni <negativo17@gmail.com> - 1.0.1~20241213git61e70b0-1
- Update to 1.0.1 pre-release snapshot.

* Thu Dec 12 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0-4
- Update to final 1.0.0 (no change).

* Mon Nov 25 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0^20241120gitc616565-3
- Update to latest snapshot.

* Mon Nov 18 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0^20241113git6092c1f-2
- Update to latest snapshot.

* Wed Sep 18 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0^20240916gitf13be94-1
- Update to latest snapshot.

* Thu Sep 12 2024 Simone Caronni <negativo17@gmail.com> - 0.1^20240910git4b333d9-1
- Update to latest packaging guidelines for snapshots.

* Wed Sep 04 2024 Simone Caronni <negativo17@gmail.com> - 0.1-1.20240828git2be2296
- First build.
