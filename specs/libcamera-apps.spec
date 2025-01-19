Name:    libcamera-apps
Version: 1.5.0
Release: 6%{?dist}
Summary: A small suite of libcamera-based apps
License: BSD
URL:     https://github.com/raspberrypi/libcamera-apps
Source0: https://github.com/raspberrypi/libcamera-apps/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExcludeArch:   %{power64} s390x
BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: git-core
BuildRequires: libcamera-devel
BuildRequires: libdrm-devel
BuildRequires: libepoxy-devel
BuildRequires: libexif-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libX11-devel
BuildRequires: qt6-qtbase-devel
# FFMPEG deps
BuildRequires: libavcodec-free-devel
BuildRequires: libavdevice-free-devel
BuildRequires: libavutil-free-devel
BuildRequires: libswresample-free-devel
# Will review OpenCV support in the future
# BuildRequires: opencv-devel

%description
This is a small suite of libcamera-based apps that aim to copy the functionality
of the existing "raspicam" apps.

%package devel
Summary:        libcamera-apps library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers for developing against libcamera-apps.

%prep
%autosetup -p1 -n rpicam-apps-%{version}

sed -i 's/qt5/qt6/' preview/meson.build

%build

%meson \
    -Denable_drm=enabled \
    -Denable_egl=enabled \
    -Denable_qt=enabled \
    -Denable_libav=enabled \
    -Denable_hailo=disabled

%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license license.txt
%{_bindir}/camera-bug-report
%{_bindir}/libcamera-*
%{_bindir}/rpicam-*
%{_libdir}/rpicam_app.so.*
%{_libdir}/rpicam-apps-postproc/

%files devel
%{_libdir}/rpicam_app.so
%{_libdir}/libcamera_app.so
%{_includedir}/libcamera-apps
%{_includedir}/rpicam-apps/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 16 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1.5.0-5
- Rebuild for libcamera 0.4

* Mon Sep 23 2024 Fabio Valentini <decathorpe@gmail.com> - 1.5.0-4
- Rebuild for ffmpeg 7

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 14 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.5.0-2
- Build agaainst QT6

* Sun Jun 02 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0
- Enable FFMPEG functionality

* Sat May 25 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.4-1
- Update to 1.4.4

* Thu May 23 2024 Javier Martinez Canillas <javierm@redhat.com> - 1.4.1-6
- Rebuilt for libcamera 0.3.0 bump

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 1.4.1-3
- Rebuilt for Boost 1.83

* Fri Jan 12 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.1-2
- Ship .so in -devel package

* Wed Jan 10 2024 Javier Martinez Canillas <javierm@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Mon Oct 23 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Thu Sep 28 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Sun Jul 30 2023 Javier Martinez Canillas <javierm@redhat.com> - 1.2.1-3
- Rebuilt for libcamera 0.1.0 bump

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Wed Jun 28 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0
- Add devel subpackage

* Mon May 29 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.2-2
- Rebuild for libcamra bump

* Sun Mar 12 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.1.1-4
- Rebuilt for Boost 1.81

* Thu Feb 02 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.1-3
- Rebuild for libcamera bump

* Wed Feb 01 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.1-2
- Sync changes to libcamera

* Wed Feb 01 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Thu Jan 19 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- Upstream patch for versioned sonames
- Review updates

* Tue Dec 27 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.2-1
- Initial package
