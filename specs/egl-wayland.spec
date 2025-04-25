%global commit0 3acc51828aceba310081c72a18f938f04d4487de
%global date 20250407
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}

Name:           egl-wayland
Version:        1.1.19%{!?tag:~%{date}git%{shortcommit0}}
Release:        3%{?dist}
Summary:        EGLStream-based Wayland external platform
License:        MIT
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
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
# Explicit synchronization since 1.34:
BuildRequires:  pkgconfig(wayland-protocols) >= 1.34
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)

# Required for directory ownership
Requires:       libglvnd-egl%{?_isa}

%description
EGL External Platform library to add client-side Wayland support to EGL on top
of EGLDevice and EGLStream families of extensions.

This library implements an EGL External Platform interface to work along with
EGL drivers that support the external platform mechanism.

%package devel
Summary:        EGLStream-based Wayland external platform development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
EGL External Platform library to add client-side Wayland support to EGL on top
of EGLDevice and EGLStream families of extensions.

This library implements an EGL External Platform interface to work along with
EGL drivers that support the external platform mechanism.

This package contains development files.

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

%files
%doc README.md
%license COPYING
%{_libdir}/libnvidia-egl-wayland.so.1
%{_libdir}/libnvidia-egl-wayland.so.1.1.19
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json

%files devel
%{_datadir}/pkgconfig/wayland-eglstream-protocols.pc
%{_datadir}/wayland-eglstream/
%{_libdir}/libnvidia-egl-wayland.so
%{_libdir}/pkgconfig/wayland-eglstream.pc

%changelog
* Wed Apr 23 2025 Simone Caronni <negativo17@gmail.com> - 1.1.19-3
- Update to 1.1.19 final.
- Trim changelog.

* Sun Apr 13 2025 Simone Caronni <negativo17@gmail.com> - 1.1.19~20250407git3acc518-2
- Update to latest snapshot.

* Mon Mar 17 2025 Simone Caronni <negativo17@gmail.com> - 1.1.19~20250313gitf1fd514-1
- Update to latest snapshot.

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.18~20250114git26ba0e3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Simone Caronni <negativo17@gmail.com> - 1.1.18~20250114git26ba0e3-2
- Update to latest snapshot.

* Mon Dec 16 2024 Simone Caronni <negativo17@gmail.com> - 1.1.18~20241210git0c6f823-1
- Update to 1.1.18 pre-release snapshot.

* Mon Dec 09 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17-6
- Update to final 1.1.17 (no change to the codebase).

* Mon Nov 18 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20241118giteeb29e1-5
- Update to latest snapshot.

* Sun Nov 03 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20241101git218f678-4
- Update to latest snapshot.

* Wed Oct 16 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20241016git0cd471d-3
- Update to latest snapshot.

* Mon Oct 07 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20240924gitc10c530-2
- Update to latest snapshot.

* Fri Sep 20 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20240919gitf5d9c69-1
- Update to latest snapshot.
- ICD is installed directly from sources.

* Thu Sep 19 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20240918git845568c-1
- Update to latest snapshot.
- Switch to more recent packaging guidelines for snapshot versions.
- Move egl-gbm ICD to egl-gbm package.

* Tue Sep 03 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17-2.20240828git2d5ecff
- Update to latest snapshot.

* Fri Aug 23 2024 Simone Caronni <negativo17@gmail.com> - 1.1.16-1
- Switch to 1.1.16 final.

* Wed Aug 21 2024 Simone Caronni <negativo17@gmail.com> - 1.1.15-2.20240819git8188db9
- Update to latest snapshot (#2305705).

* Fri Aug 09 2024 Simone Caronni <negativo17@gmail.com> - 1.1.15-1
- Update to 1.1.15 final.

* Thu Aug 08 2024 Simone Caronni <negativo17@gmail.com> - 1.1.14-3.20240808git4480345
- Update to latest snapshot.

* Wed Aug 07 2024 Simone Caronni <scaronni@nvidia.com> - 1.1.14-2.20240805gitc439cd5
- Update to latest snapshot with commits required for NVIDIA driver 560+ with
  explicit sync support.

* Thu Jul 18 2024 Leigh Scott <leigh123linux@gmail.com> - 1.1.14-1
- Update to 1.1.14

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 21 2024 Leigh Scott <leigh123linux@gmail.com> - 1.1.13-4
- Add Wayland explicit sync support

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild
