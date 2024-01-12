Name:    libcamera-apps
Version: 1.4.1
Release: 1%{?dist}
Summary: A small suite of libcamera-based apps
License: BSD
URL:     https://github.com/raspberrypi/libcamera-apps
Source0: https://github.com/raspberrypi/libcamera-apps/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Compressed pixel formats are not supported by mainline libcamera
Patch01: Revert-Support-compressed-pixel-formats-when-saving-.patch

ExcludeArch:   %{power64} s390x
BuildRequires: cmake
BuildRequires: boost-devel
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: libcamera-devel
BuildRequires: libdrm-devel
BuildRequires: libexif-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libX11-devel
BuildRequires: meson
BuildRequires: qt5-qtbase-devel
# Omitting ffmpeg due to needed pieces not in Fedora
# BuildRequires: ffmpeg-devel
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

%build

%meson
%meson_build

%install
%meson_install
# Still installs the unversioned sonames
find %{buildroot} -name '*.so' -delete

%ldconfig_scriptlets

%files
%license license.txt
%{_bindir}/camera-bug-report
%{_bindir}/libcamera-*
%{_bindir}/rpicam-*
%{_libdir}/rpicam_app.so.*

%files devel
%{_includedir}/libcamera-apps
%{_includedir}/rpicam-apps/

%changelog
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
