Name:    libcamera-apps
Version: 1.1.1
Release: 3%{?dist}
Summary: A small suite of libcamera-based apps
License: BSD
URL:     https://github.com/raspberrypi/libcamera-apps
Source0: https://github.com/raspberrypi/libcamera-apps/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExcludeArch:   %{power64} s390x
BuildRequires: cmake
BuildRequires: boost-devel
BuildRequires: gcc-c++
BuildRequires: libcamera-devel
BuildRequires: libdrm-devel
BuildRequires: libexif-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libX11-devel
BuildRequires: qt5-qtbase-devel
# Omitting ffmpeg due to needed pieces not in Fedora
# BuildRequires: ffmpeg-devel
# Will review OpenCV support in the future
# BuildRequires: opencv-devel

%description
This is a small suite of libcamera-based apps that aim to copy the functionality
of the existing "raspicam" apps.

%prep
%autosetup -p1

%build

%cmake -DENABLE_LIBAV=OFF -DENABLE_OPENCV=OFF -DENABLE_TFLITE=OFF
%cmake_build

%install
%cmake_install
# Still installs the unversioned sonames
find %{buildroot} -name '*.so' -delete

%ldconfig_scriptlets

%files
%license license.txt
%{_bindir}/camera-bug-report
%{_bindir}/libcamera-*
%{_libdir}/libcamera_app.so.*
%{_libdir}/libencoders.so.*
%{_libdir}/libimages.so.*
%{_libdir}/liboutputs.so.*
%{_libdir}/libpost_processing_stages.so.*
%{_libdir}/libpreview.so.*

%changelog
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
