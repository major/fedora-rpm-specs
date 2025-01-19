%global __provides_exclude %{python3_sitearch}/.*\.so$

Name:           libfreenect
Version:        0.7.0
Release:        13%{?dist}
Summary:        Device driver for the Kinect
# Core libfreenect is available as Apache-2.0 OR GPL-2.0-only
#
# OpenNI driver is available as Apache-2.0
License:        Apache-2.0 AND (GPL-2.0-only OR Apache-2.0)
URL:            http://www.openkinect.org/

Source0:        https://github.com/OpenKinect/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Edit udev rule to only allow access to the device from the video group
Patch0:         %{name}-0.5.7-videogroup.patch
# Freenect openni driver is a plugin lib, and doesn't need soversion symlinks
Patch1:         %{name}-openni2.patch
# Allow for proper libdir
Patch3:         %{name}-0.4.2-libdir.patch
# BZ: https://bugzilla.redhat.com/show_bug.cgi?id=1143912
Patch4:         secarch.patch
# Fix the installation path for python libs
Patch5:         %{name}-0.7.0-py3.patch
# Fix for cython3
Patch6:         %{name}-0.7.0-cython3.patch
Patch7: libfreenect-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  freeglut-devel
BuildRequires:  libusb1-devel
BuildRequires:  libGL-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  opencv-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-numpy

Requires:       udev

%description
libfreenect is a free and open source library that provides access to the
Kinect device.  Currently, the library supports the RGB webcam, the depth
image, the LED, and the tilt motor.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Development files for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains static libraries for
developing applications that use %{name}.

%package        fakenect
Summary:        Library to play back recorded data for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    fakenect
Fakenect consists of a "record" program to save dumps from the kinect sensor 
and a library that can be linked to, providing an interface compatible with 
freenect.  This allows you to save data and repeat for experiments, debug 
problems, share datasets, and experiment with the kinect without having one.

%package        opencv
Summary:        OpenCV bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    opencv
The %{name}-opencv package contains the libfreenect binding
library for OpenCV development.

%package -n     python3-%{name}
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-numpy
%{?python_provide:%python_provide python3-%{name}}

%description -n  python3-%{name}
The %{name}-python package contains python 3 bindings for %{name}

%package        openni
Summary:        OpenNI2 driver for the Kinect

%description    openni
The OpenNI2-FreenectDriver is a bridge to libfreenect implemented as an 
OpenNI2 driver. It allows OpenNI2 to use Kinect hardware on Linux and OSX. 
It was originally a separate project but is now distributed with libfreenect.

%prep
%setup -qn %{name}-%{version}
rm -rf platform/windows

%patch -P 0 -p0 -b .videogroup
%patch -P 1 -p1 -b .openni2
%patch -P 3 -p0 -b .libdir
%patch -P 4 -p1 -b .secarch
%patch -P 5 -p1 -b .py3
%patch -P 6 -p1 -b .cython3
%patch -P 7 -p1

%build
%cmake3 \
  -DBUILD_AUDIO=ON \
  -DBUILD_C_SYNC=ON \
  -DBUILD_CV=ON \
  -DBUILD_REDIST_PACKAGE=ON \
  -DBUILD_EXAMPLES=ON \
  -DBUILD_FAKENECT=ON \
  -DBUILD_PYTHON=OFF  \
  -DBUILD_PYTHON2=OFF \
  -DBUILD_PYTHON3=ON \
  -DBUILD_OPENNI2_DRIVER=ON

%cmake3_build

pushd doc
doxygen Doxyfile
popd

%install
%cmake3_install

# Install the kinect udev rule
mkdir -p %{buildroot}/lib/udev/rules.d
mkdir -p %{buildroot}%{_libdir}/openni2
install -p -m 0644 platform/linux/udev/51-kinect.rules %{buildroot}/lib/udev/rules.d

# Delete libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Move the fwfetcher script to the correct datadir
mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_datadir}/fwfetcher.py   %{buildroot}%{_datadir}/%{name}

# Move openni plugin: rhbz#1094787
mv %{buildroot}%{_libdir}/OpenNI2-FreenectDriver %{buildroot}%{_libdir}/openni2/Drivers

%files
%license APACHE20 GPL2
%doc README.md CONTRIB
/lib/udev/rules.d/*
%{_libdir}/libfreenect.so.0*
%{_libdir}/libfreenect_sync.so.0*
%exclude %{_bindir}/freenect-cvdemo
%exclude %{_bindir}/fakenect
%{_bindir}/freenect-*
%{_datadir}/%{name}

%files opencv
%{_bindir}/freenect-cvdemo
%{_libdir}/libfreenect_cv.so.*

%files devel
%doc doc/html
%doc examples/*.c wrappers/cpp/cppview.cpp
%{_includedir}/libfreenect
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/fakenect/*.so

%files static
%{_libdir}/*.a

%files -n python3-%{name}
%{python3_sitearch}/*.so

%files fakenect
%dir %{_libdir}/fakenect
%{_bindir}/fakenect-record
%{_libdir}/fakenect/*.so.*
%{_bindir}/fakenect
%{_mandir}/man1/fakenect*1.*

%files openni
%{_libdir}/openni2

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 24 2024 Orion Poplawski <orion@nwra.com> - 0.7.0-12
- Rebuild with numpy 2.x (rhbz#2333776)

* Thu Jul 25 2024 Sérgio Basto <sergio@serjux.com> - 0.7.0-11
- Rebuild for opencv 4.10.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.7.0-9
- Rebuilt for Python 3.13

* Mon Feb 05 2024 Sérgio Basto <sergio@serjux.com> - 0.7.0-8
- Rebuild for opencv 4.9.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Florian Weimer <fweimer@redhat.com> - 0.7.0-5
- Fix C compatibility issue in Cython wrapper

* Mon Aug 07 2023 Rich Mattes <richmattes@gmail.com> - 0.7.0-4
- Fix build error with cython 3

* Mon Aug 07 2023 Sérgio Basto <sergio@serjux.com> - 0.7.0-4
- Rebuild for opencv 4.8.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Rich Mattes <richmattes@gmail.com> - 0.7.0-2
- Updates for Python 3.12 compatibility
- Resolves: rhbz#2220025

* Sat Jun 17 2023 Python Maint <python-maint@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.12

* Thu May 04 2023 Nicolas Chauvet <kwizart@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sérgio Basto <sergio@serjux.com> - 0.6.4-2
- Rebuild for opencv 4.7.0

* Sat Sep 24 2022 Phil Wyett <philip.wyett@kathenas.org> - 0.6.4-1
- New upstream version 0.6.4
- Remove old globals

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 0.6.2-8
- Rebuilt for opencv 4.6.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.2-7
- Rebuilt for Python 3.11

* Wed Jan 26 2022 Phil Wyett <philip.wyett@kathenas.org> - 0.6.2-6
- Fix FTBFS. Update cmake related OpenGL GLVND and GLUT.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 01 2021 Phil Wyett <philip.wyett@kathenas.org> - 0.6.2-4
- Drop not needed Cython BuildRequires
- Resolves: #1984287

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.2-2
- Rebuilt for Python 3.10

* Thu Mar 04 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.6.2-1
- Update to 0.6.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-7
- Rebuilt for OpenCV

* Mon Aug 03 2020 Leigh Scott <leigh123linux@gmail.com> - 0.6.1-6
- Fix unversioned python
- Switch to new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-3
- Rebuilt for OpenCV 4.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-2
- Rebuilt for Python 3.9

* Mon May 25 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Tue Mar 03 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-3
- Update to new ABI

* Fri Feb 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-2
- Rebuilt to keep previous ABI

* Fri Feb 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-1
- Update to 0.6.0
- Drop Minor in APIVER (SONAME change)

* Wed Feb 19 2020 Leigh Scott <leigh123linux@gmail.com> - 0.5.7-15
- Rebuilt for OpenCV 4.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.5.7-13
- Rebuilt for OpenCV 4.2

* Mon Jan 27 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.5.7-12
- Fix for OpenCV4

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.5.7-11
- Rebuilt for opencv4

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.5.7-9
- Rebuilt for new freeglut

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.7-8
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Rich Mattes <richmattes@gmail.com> - 0.5.7-5
- Remove Python 2 support (#1634715)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.7-3
- Rebuilt for Python 3.7

* Sat May 26 2018 Rich Mattes <richmattes@gmail.com> - 0.5.7-2
- Re-enable OpenCV bindings (rhbz#1551748)
- Fix bogus obsoletes (rhbz#1537213)
- Update udev rule to allow device access to "video" group

* Mon Mar 05 2018 Adam Williamson <awilliam@redhat.com> - 0.5.7-1
- Bump to 0.5.7 (bug fixes)
- Disable openCV support for now (see #1551748)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.5.5-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Wed Mar 08 2017 Rich Mattes <richmattes@gmail.com> - 0.5.5-1
- Update to release 0.5.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Rich Mattes <richmattes@gmail.com> - 0.5.3-3
- Rebuild for opencv-3.1 changes

* Mon May 02 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.5.3-2
- Rebuild for opencv-3.1.0.

* Sun Feb 21 2016 Rich Mattes <richmattes@gmail.com> - 0.5.3-1
- Update to release 0.5.3 (rhbz#1272803)
- Fix rawhide FTBFS (rhbz#1307722)
- Patch freenct-cppview to catch exception when no freenect device is present (rhbz#1310356)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 26 2015 Rich Mattes <richmattes@gmail.com> - 0.5.2-5
- Add dependency on numpy (rhbz#1265472)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Mar 04 2015 Rich Mattes <richmattes@gmail.com> - 0.5.2-1
- Add patch for s390 and ppc (rhbz#1143912)

* Wed Mar 04 2015 Rich Mattes <richmattes@gmail.com> - 0.5.2-1
- Update to release 0.5.2 (rhbz#1160258)

* Tue Aug 19 2014 Jiri Kastner <jkastner /at/ redhat /dot/ com> - 0.5.0-1
- update to release 0.5.0 (rhbz#1124171)
- Move openni plugin to libdir/openni2/Drivers (rhbz#1094787)
 
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Rich Mattes <richmattes@gmail.com> - 0.4.3-1
- Update to release 0.4.3
- Move openni plugin to libdir/openni2/ (rhbz#1094787)

* Mon May 05 2014 Rich Mattes <richmattes@gmail.com> - 0.4.2-1
- Update to release 0.4.2
- Add platform detection for aarch64

* Fri May 02 2014 Rich Mattes <richmattes@gmail.com> - 0.4.1-1
- Update to release 0.4.1

* Fri Nov 22 2013 Rich Mattes <richmattes@gmail.com> - 0.2.0-1
- Update to release 0.2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Dan Horák <dan[at]danny.cz> - 0.1.2-4
- fixes for secondary arches

* Sat Nov 10 2012 Rich Mattes <richmattes@gmail.com> - 0.1.2-3
- Rebuild for new OpenCV

* Wed Aug 15 2012 Rich Mattes <richmattes@gmail.com> - 0.1.2-2
- Filtered private python lib provides
- Clarified that freenect_generate_tarball.sh works with a git tag

* Thu Apr 26 2012 Rich Mattes <richmattes@gmail.com> - 0.1.2-1
- Update to git tag 0.1.2
- Create OpenCV wrapper sub-package
- Create fakenect library sub-package

* Thu Mar 24 2011 Rich Mattes <richmattes@gmail.com> - 0-0.3.4a159fgit
- Force cmake to honor rpm optflags
- Change to out-of-tree build

* Thu Mar 24 2011 Rich Mattes <richmattes@gmail.com> - 0-0.2.4a159fgit
- Update to latest snapshot

* Mon Jan 31 2011 Rich Mattes <richmattes@gmail.com> - 0-0.1.687b2da5git
- Initial package

