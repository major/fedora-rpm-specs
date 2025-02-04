%undefine __cmake_in_source_build
%global abiversion 3.1
%global releasetag release-3-1-0

Name:           player
Version:        3.1.0
Release:        62%{?dist}
Summary:        Cross-platform robot device interface and server

License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://playerproject.github.io
Source0:        https://github.com/playerproject/%{name}/archive/%{releasetag}/%{name}-%{version}.tar.gz
Source1:        playernav.desktop
Source2:        playercam.desktop
Source3:        playerv.desktop

Patch0:         %{name}-3.1.0-cmake3.patch
# Upstream PR: https://github.com/playerproject/player/pull/12
Patch1:         %{name}-3.1.0-cmake-find-python-version.patch
Patch2:         %{name}-3.1.0-cpp11.patch
Patch3:         %{name}-3.1.0-tirpc.patch
Patch4:         %{name}-3.1.0-python3.patch
Patch5:         %{name}-3.1.0-opencv3.patch
Patch6:         %{name}-opencv4.patch
# Upstream PR: https://github.com/playerproject/player/pull/27
Patch7:         %{name}-3.1.0-pr27-struct-forward-for-swig-parse.patch
# Sort order: build tools, feature libs, within alphabetically, group related
# entries on single line (most dominant lib first or alphabetically)

# Build tools
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen, texlive-latex, texlive, texlive-dvips, latex2html, graphviz
BuildRequires:  libtool, libtool-ltdl-devel, texlive-newunicodechar
# Libs to enable Player features
BuildRequires:  alsa-lib-devel
BuildRequires:  avahi-compat-howl-devel
BuildRequires:  boost-devel boost-thread
BuildRequires:  eigen3-devel
BuildRequires:  flexiport-devel
BuildRequires:  freeglut-devel
BuildRequires:  gearbox-devel
BuildRequires:  hokuyoaist-devel
BuildRequires:  geos-devel
BuildRequires:  gsl-devel
BuildRequires:  gtk2-devel, libgnomecanvas-devel
BuildRequires:  guile22-devel
%ifnarch s390 s390x
BuildRequires:  libdc1394-devel, libraw1394-devel
%endif
BuildRequires:  libfreenect-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libphidget22-devel
BuildRequires:  libpq-devel
BuildRequires:  libstatgrab-devel
BuildRequires:  libtirpc-devel
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  libv4l-devel
BuildRequires:  libXext-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libGL-devel, mesa-libGLU-devel
BuildRequires:  opencv-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  python3
BuildRequires:  swig
BuildRequires:  ruby, ruby-devel
BuildRequires:  zlib-devel

# There is no support for Python 3 yet, see:
# https://github.com/playerproject/player/issues/17
Obsoletes: python3-player < 3.1.0-48

%description
Player is a network server for robot control. Running on your robot, Player
provides a clean and simple interface to the robot's sensors and actuators
over the IP network. Your client program talks to Player over a TCP socket,
reading data from sensors, writing commmands to actuators, and configuring
devices on the fly. Player supports a variety of robot hardware.


%package devel
Summary: Header files and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig cmake
Requires: boost-devel
Requires: geos-devel
Requires: libtool-ltdl-devel
Requires: libtirpc-devel
Requires: zlib-devel

%description devel
This package contains the header files and libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary: Development documentation for Player
BuildArch: noarch

%description doc
This package contains the development documentation for Player.

%package examples
Summary:  Examples and templates for Player
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description examples
This package contains example code for %{name} development.
Included are sample plugin drivers, and examples.

%package -n ruby-%{name}
Summary: Ruby bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
#Until f28
Obsoletes: %{name}-ruby < 3.0.2-56
Requires: ruby(release) >= 1.8

%description -n ruby-%{name}
This package contains the Ruby client-side bindings for %{name}.
If you would like to build %{name} clients using Ruby you
will need to install this package.  Includes bindings built
against the C and C++ client libraries. Ruby bindings
are experimental.


%prep
%setup -q -n %{name}-%{releasetag}
%patch -P 0 -p1 -b .cmake3
%patch -P 1 -p1 -b .cmake-find-python-version
%patch -P 2 -p1 -b .cpp11
%patch -P 3 -p1 -b .tirpc
%patch -P 4 -p1 -b .python3
%patch -P 5 -p1 -b .opencv3
%patch -P 6 -p1 -b .opencv4
%patch -P 7 -p1 -b .swig_forward

# Filter out the 'build' folder from doxygen generation
sed -i 's|EXCLUDE                =|EXCLUDE                = ../%{_vpath_builddir}|' doc/player.dox.in

%build
export CXXFLAGS="-std=c++14 %{optflags}"
export LDFLAGS="%{?__global_ldflags} -lpthread"
# python3 binding fails to build, now explicitly disabing it (#2161923)
%cmake %{?_cmake_skip_rpath} \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_DOCUMENTATION=ON \
  -DBUILD_PLAYERCC=ON \
  -DSWIG_EXECUTABLE=/usr/bin/swig \
  -DBUILD_PLAYERCC_BOOST=ON \
  -DBUILD_PYTHONC_BINDINGS=OFF \
  -DBUILD_PYTHONCPP_BINDINGS=OFF \
  -DBUILD_EXAMPLES=ON \
  -DBUILD_RUBYCPP_BINDINGS=ON \
  -DUNICAP_DIR=/usr \
%if 0%{?fedora} >= 32
  -DENABLE_DRIVER_SHAPETRACKER=OFF \
  -DENABLE_DRIVER_SIMPLESHAPE=OFF \
  -DENABLE_DRIVER_IMAGESEQ=OFF \
%endif
%if 0%{?fedora} >= 34
  -DENABLE_DRIVER_EPUCK=OFF \
%endif
  -DLARGE_FILE_SUPPORT=ON \
  -DRUBY_BINDINGS_INSTALL_DIR=%{ruby_vendorarchdir}

%cmake_build
%cmake_build --target doc

%install
%cmake_install
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
mkdir -p %{buildroot}/%{_libdir}/%{name}-%{abiversion}
mv %{buildroot}/%{_datadir}/%{name}/config %{buildroot}/%{_sysconfdir}/%{name}
find %{buildroot} -name '*.la' -exec rm {} \;
rm -rf %{buildroot}/%{_docdir}/*

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
--vendor="fedora"               \
%endif
--dir=%{buildroot}%{_datadir}/applications         \
%{SOURCE1}

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
--vendor="fedora"               \
%endif
--dir=%{buildroot}%{_datadir}/applications         \
%{SOURCE2}

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
--vendor="fedora"               \
%endif
--dir=%{buildroot}%{_datadir}/applications         \
%{SOURCE3}

%ldconfig_scriptlets

%files
%license COPYING COPYING.lib
%doc README.md AUTHORS
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config/*
%{_bindir}/player*
%{_bindir}/pmaptest
%{_libdir}/*.so.*
%dir %{_datadir}/player
%{_datadir}/applications/*.desktop
%dir %{_libdir}/player-%{abiversion}

%files devel
%{_includedir}/player-%{abiversion}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/Modules/*

%files examples
%{_datadir}/player/examples

%files doc
%license COPYING COPYING.lib
%doc doc/*.txt
%doc doc/*.html
%doc %{_vpath_builddir}/doc/player-docs

%files -n ruby-%{name}
%{ruby_vendorarchdir}/*.so

%changelog
* Sun Feb 02 2025 Orion Poplawski <orion@nwra.com> - 3.1.0-62
- Rebuild with gsl 2.8

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-60
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Sun Dec 22 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-59
- Explicltiy disable python bindings (ref: #2161923)

* Thu Jul 25 2024 Sérgio Basto <sergio@serjux.com> - 3.1.0-58
- Rebuild for opencv 4.10.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 12 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-56
- Fix FTBFS with -Werror=incompatible-pointer-types
  on swig ruby binding using struct forward decl

* Thu Jan 25 2024 Tomas Korbar <tkorbar@redhat.com> - 3.1.0-55
- Changed required guile version to 2.2
  https://src.fedoraproject.org/rpms/player/pull-request/6

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-53
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Mon Aug 07 2023 Sérgio Basto <sergio@serjux.com> - 3.1.0-52
- Rebuild for opencv 4.8.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Till Hofmann <thofmann@fedoraproject.org> - 3.1.0-50
- Rebuild for libdc1394-2.2.7

* Sun Mar 12 2023 Tim Orling <ticotimo@gmail.com> - 3.1.0-49
- migrated to SPDX license

* Thu Feb  2 2023 Florian Weimer <fweimer@redhat.com> - 3.1.0-48
- Remove non-working Python 3 module (#2161923)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sérgio Basto <sergio@serjux.com> - 3.1.0-46
- Rebuild for opencv 4.7.0

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-45
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Oct 29 2022 Rich Mattes <richmattes@gmail.com> - 3.1.0-44
- Remove libunicap buildrequires (Fixes: #2130273)

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-43
- Change to BR: libphidget22-devel

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-42
- Rebuild for gsl-2.7.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Sérgio Basto <sergio@serjux.com> - 3.1.0-40
- Rebuilt for opencv 4.6.0

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-39
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Sandro Mani <manisandro@gmail.com> - 3.1.0-37
- Rebuild (geos)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-36
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.0-35
- Rebuilt for Python 3.10

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 3.1.0-34
- Rebuild (geos)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Vít Ondruch <vondruch@redhat.com> - 3.1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Thu Oct 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.1.0-31
- Rebuilt for OpenCV

* Tue Oct 20 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.1.0-30
- Fix FTBFS by dropping DRIVER_EPUCK

* Fri Aug 14 2020 Jeff Law <law@redhat.com> - 3.1.0-29
- Force C++14 as this code is not C++17 ready

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-28
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.1.0-26
- Rebuilt for OpenCV 4.3

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 3.1.0-25
- Rebuilt for Boost 1.73 and Python 3.9 together

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 3.1.0-24
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-23
- Rebuilt for Python 3.9

* Tue Mar 03 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.1.0-22
- Rebuilt for libfreenect

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.1.0-20
- Rebuild for OpenCV 4.2

* Mon Dec 30 2019 Nicolas Chauvet <kwizart@gmail.com> - 3.1.0-19
- Rebuilt for opencv4
- Disable few drivers not ported to opencv2 API
- Enable LARGE_FILE_SUPPORT and libv4l

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.1.0-18
- Rebuilt for new freeglut

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.1.0-17
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 3.1.0-13
- Rebuilt for Boost 1.69

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 3.1.0-12
- Fix rawhide FTBFS (rhbz#1605475)
- Replace python 2 subpackage with python3 subpackage (rhbz#1634371)

* Sun Oct 07 2018 Till Hofmann <thofmann@fedoraproject.org> - 3.1.0-11
- Add patch to fix python version determination in cmake
- Add missing BR graphviz

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-10
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Adam Williamson <awilliam@redhat.com> - 3.1.0-8
- Add tirpc-devel to -devel requires and pkgconfig file

* Mon Mar 05 2018 Adam Williamson <awilliam@redhat.com> - 3.1.0-7
- Rebuild for another opencv soname bump

* Sat Feb 24 2018 Rich Mattes <richmattes@gmail.com> - 3.1.0-6
- Add patch to build against tirpc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Sérgio Basto <sergio@serjux.com> - 3.1.0-5
- Rebuild (opencv-3.3.1)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 3.1.0-2
- Rebuilt for Boost 1.64

* Sun Apr 09 2017 Rich Mattes <richmattes@gmail.com> - 3.1.0-1
- Update to release 3.1.0
- Remove upstream patches
- Add BuildRequires to enable more features

* Tue Apr 04 2017 Rich Mattes <richmattes@gmail.com> - 3.0.2-59
- Rebuild for gazebo-8.0.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Vít Ondruch <vondruch@redhat.com> - 3.0.2-57
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Sun Jan 01 2017 Rich Mattes <richmattes@gmail.com> - 3.0.2-56
- Rebuild for new geos
- Clean up naming of python and ruby subpackages

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-55
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Rich Mattes <richmattes@gmail.com> - 3.0.2-54
- Rebuild for opencv-3.1 changes

* Tue May 03 2016 Rich Mattes <richmattes@gmail.com> - 3.0.2-53
- Rebuild for opencv-3.1.0

* Tue Feb 23 2016 Rich Mattes <richmattes@gmail.com> - 3.0.2-52
- Fix rawhide FTBFS (rhbz#1307867)

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 3.0.2-52
- Rebuild for gsl 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-50
- Rebuilt for Boost 1.60

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 3.0.2-49
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Sat Oct 17 2015 Kalev Lember <klember@redhat.com> - 3.0.2-48
- Rebuilt for libgeos soname bump

* Mon Sep 21 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.0.2-47
- Fix the build against libstatgrab 0.91

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-46
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-45
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.0.2-44
- rebuild for Boost 1.58

* Wed Jul 01 2015 Jozef Mlich <jmlich@redhat.com> - 3.0.2-43
- replacing deprecated opencv functions calls

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 3.0.2-41
- Fix the build

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 3.0.2-40
- Rebuild for boost 1.57.0

* Thu Sep 25 2014 Karsten Hopp <karsten@redhat.com> 3.0.2-39
- fix libdir on new 64bit archs, aarch64 and ppc64le

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 Rex Dieter <rdieter@fedoraproject.org> 3.0.2-37
- rebuild (libpqxx)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Petr Machata <pmachata@redhat.com> - 3.0.2-35
- Don't add -mt to boost DSO names (player-3.0.2.boost155.patch)

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 3.0.2-35
- rebuild for boost 1.55.0

* Sun Oct 06 2013 Rich Mattes <richmattes@gmail.com> - 3.0.2-34
- Rebuild for libstatgrab reversion

* Sat Sep 14 2013 Rich Mattes <richmattes@gmail.com> - 3.0.2-33
- Rebuild for new geos

* Sat Aug 17 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.2-32
- Add player-3.0.2.libstatgrab-0.90.patch
  (Fix FTBFS caused by upgrading libstatgrab to 0.90).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 3.0.2-30
- Rebuild for boost 1.54.0

* Mon Mar 25 2013 Vít Ondruch <vondruch@redhat.com> - 3.0.2-29
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.0.2-28
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077
- Add libpthread to be linked explicitly so that build succeeds

* Wed Mar 06 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 3.0.2-27
- Rebuild with new geos.

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.0.2-26
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.0.2-25
- Rebuild for Boost-1.53.0

* Sat Jan 26 2013 Rich Mattes <richmattes@gmain.com> - 3.0.2-24
- Update for new phidget RFID API

* Fri Jan 25 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 3.0.2-24
- Rebuild against geos 3.3.7.

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 3.0.2-23
- rebuild due to "jpeg8-ABI" feature drop

* Mon Nov 19 2012 Devrim GÜNDÜZ <devrim@gunduz.org> - 3.0.2-22
- Rebuild with new geos.

* Sat Nov 10 2012 Rich Mattes <richmattes@gmail.com> - 3.0.2-21
- Rebuild for new OpenCV

* Mon Jul 30 2012 Rich Mattes <richmattes@gmail.com> - 3.0.2-20
- Added dependency on hokuyoaist library
- Added dependency on flexiport library
- Fixed hokuyoaist driver to work with hokuyoaist library
- Removed gearbox dependency
- Updated for boost-1.5.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Rich Mattes <richmattes@gmail.com> - 3.0.2-18
- boost::TIME_UTC no longer defined, use glibc's instead
- cast FILE* to gzFile for gzip functions
- Fix bug where docs were being included in both base and -doc subpackages

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-17
- Rebuilt for c++ ABI breakage

* Wed Jan 11 2012 Rich Mattes <richmattes@gmail.com> - 3.0.2-16
- Rebuild for new gcc and geos

* Sat Nov 26 2011 Rich Mattes <richmattes@gmail.com> - 3.0.2-15
- Rebuilt for new boost

* Sun Oct 09 2011 Rich Mattes <richmattes@gmail.com> - 3.0.2-14
- Rebuild for geos update

* Wed Aug 31 2011 Rex Dieter <rdieter@fedoraproject.org> 3.0.2-13
- rebuild (opencv)

* Tue Aug 02 2011 Rich Mattes <richmattes@gmail.com> - 3.0.2-12
- Rebuild for new boost

* Fri Jul 01 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 3.0.2-11
- bump for libpqxx
- disable rapth

* Sun Jun 19 2011 Rich Mattes <richmattes@gmail.com> - 3.0.2-10
- Rebuild for geos update

* Wed May 04 2011 Dan Horák <dan[at]danny.cz> - 3.0.2-9
- Add s390x as 64-bit arch

* Sun Apr 10 2011 Rich Mattes <richmattes@gmail.com> - 3.0.2-8
- Rebuild for boost soname change

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Thomas Spura <tomspur@fedoraproject.org> - 3.0.2-6
- rebuild for new boost

* Sat Jan 08 2011 Rich Mattes <richmattes@gmail.com> - 3.0.2-5
- Rebuild for OpenCV 2.2
- Fix assertion error in PlayerCam
- Enable libphidget support

* Fri Jul 30 2010 Rich Mattes <richmattes@gmail.com> - 3.0.2-4
- Rebuilt for boost 1.44

* Mon Jul 26 2010 Rich Mattes <richmattes@gmail.com> - 3.0.2-3
- Rebuilt for Python 2.7 mass rebuild
- Restore pmaptest
- Add copyright files to player-doc subpackage

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 29 2010 Rich Mattes <richmattes@gmail.com> - 3.0.2-1
- Upgrade to release 3.0.2
- Remove more supurious BuildRequires
- Add BuildRequires to enable more features

* Sat Jun 26 2010 Rich Mattes <richmattes@gmail.com> - 3.0.1-7
- Rebuild for OpenCV soname change
- Remove unnecessary BuildRequires

* Thu Apr 1 2010 Rich Mattes <richmattes@gmail.com> - 3.0.1-6
- Rebuild for GEOS soname change

* Wed Mar 24 2010 Rich Mattes <richmattes@gmail.com> - 3.0.1-5
- Rebuild for Gearbox drivers
- Added missing Requires for devel package

* Mon Mar 01 2010 Tim Niemueller <tim@niemueller.de> - 3.0.1-4
- Bump EVR for proper F-12 to F-13 upgrade path

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 3.0.1-2
- Rebuild for Boost soname bump

* Sun Jan 10 2010 Rich Mattes <richmattes@gmail.com> - 3.0.1-1
- Updated to release 3.0.1
- Fixed ruby bindings install path
- Fixed documentation build process
- Added libdir/player to plugin search path
- Fix Rawhide compilation issue by adding -DBoost_USE_MULTITHREAD=ON to cmake

* Sun Nov 08 2009 Tim Niemueller <tim@niemueller.de> - 3.0.0-4
- devel sub-package obsoletes no longer available static sub-package

* Sun Oct 18 2009 Tim Niemueller <tim@niemueller.de> - 3.0.0-3
- Merge Rich's changes with Fedora spec file

* Sat Oct 10 2009 Rich Mattes <richmattes@gmail.com> - 3.0.0-2
- Fixed x86_64 build issues
- Fixed x86_64 library install path
- Fixed mock i586 and x86_64 dep issues
- Enabled Python C++ and Ruby C++ bindings
- Made doc and examples packages .noarch

* Wed Oct 7 2009 Rich Mattes <richmattes@gmail.com> - 3.0.0-1
- Upgrade package to Player 3.0.0

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.1.1-13
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.1-11
- Exclude -examples subpackage files in main package (#489184).

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 2.1.1-9
- rebuild with new openssl

* Sun Dec 21 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-8
- Add patch for broken linux/serial.h (thanks to Caolán McNamara)
- Add patch for GCC 4.4 (thanks to Caolán McNamara)
- Rebuild for Python 2.6

* Sat Dec  6 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.1.1-7
- Fix libtool issue

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.1.1-6
- Rebuild for Python 2.6

* Tue Sep 02 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-5
- Added plugindir patch

* Fri Aug 15 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-4
- Changed norpath patch, fixes build problem on Fedora 8
- Added libtool BR
- Added autotools BR, needed because for patches of .am files

* Fri Aug 08 2008 Jef Spaleta <jspaleta at fedoraproject dot org> - 2.1.1-3
- Review clean-ups

* Tue Aug 05 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-2
- Only BR geos-devel on Fedora 9

* Fri Aug 01 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-1
- Upgrade to 2.1.1

* Mon Jun 23 2008 Jef Spaleta <jspaleta at fedoraproject dot org> - 2.1.0-0.3.rc2.fc9
- Review clean-ups

* Thu May 22 2008 Tim Niemueller <tim@niemueller.de> - 2.1.0-0.2.rc2.fc9
- Added subpackages for doc and examples
- Remove *.la files
- Fix BuildRequires

* Thu May 08 2008 Tim Niemueller <tim@niemueller.de> - 2.1.0-0.1.rc2.fc9
- Initial spec file

