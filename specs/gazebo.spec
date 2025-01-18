%undefine __cmake_in_source_build
%global abiversion 10

Name:           gazebo
Version:        10.2.0
Release:        12%{?dist}
Summary:        3D multi-robot simulator with dynamics

# gazebo/gui/qgv is LGPLv3+
# gazebo/gui/qtpropertybrowser/ is BSD
# test/gtest is BSD
# Automatically converted from old format: ASL 2.0 and BSD and LGPLv3+ - review is highly recommended.
License:        Apache-2.0 AND LicenseRef-Callaway-BSD AND LGPL-3.0-or-later
URL:            http://www.gazebosim.org
Source0:        http://osrf-distributions.s3.amazonaws.com/%{name}/releases/%{name}-%{version}.tar.bz2
Source1:        gazebo.desktop
# This patch unbundles skyx and removes boost::signals
# https://bitbucket.org/osrf/gazebo/pull-requests/3050/dont-search-for-boost-signals-component/activity#
Patch0:         %{name}-9.5.0-fedora.patch
# Remove rpath in pkgconfig files
# Not submitted upstream
Patch2:         %{name}-7.3.1-rpath.patch
# Fix an exception that differs in behaviour because of boost differences
# Not submitted upstream
Patch3:         %{name}-2.2.2-connection.patch
# Fix an error due to __linux not being defined on ppc64
# Addresses rhbz#1396676
# Not submitted upstream
Patch5:         %{name}-7.4.0-fixtest.patch
Patch6:         %{name}-gaussian-noise-model-with-0-bias-stddev.patch
Patch9:         %{name}-9.5.0-python3.patch
# Set a default CMake policy to disable warnings about the automoc behavior
# Disable default hidden symbol visibility (rhbz#1871291)
Patch10:        %{name}-10.1.0-automoc.patch
Patch11:        %{name}-10.1.0-singleton.patch
Patch12:        %{name}-9.5.0-wayland.patch
Patch13:        %{name}-10.1.0-tbb.patch
Patch14:        %{name}-10.1.0-boost173.patch
# https://github.com/osrf/gazebo/commit/b4429a242c43e01c367bc02afa2c4a0e6b59dddd
# https://github.com/kcat/openal-soft/commit/399dfca1e3352050a5289be6bcd7b7dce353ccf8
Patch15:        %{name}-10.1.0-openal121.patch
# Fix build against qwt-6.2
Patch16:        %{name}-10.1.0-qwt.patch
# https://github.com/gazebosim/gazebo-classic/pull/3290
Patch17:        %{name}-pr3290-gcc13-array-include.patch
# https://github.com/gazebosim/gazebo-classic/pull/3345
Patch18:        %{name}-pr3345-fix-build-with-graphviz-9.patch
# https://github.com/gazebosim/gazebo-classic/pull/2862
Patch19:        %{name}-pr2862-simpletrackedvehicle-fix-for-boost-1.74.patch
# https://github.com/gazebosim/gazebo-classic/commit/3a9efee7ccdf552cbf22188131782f242f6c0542
Patch20:        %{name}-10.2.0-graphviz-10.patch

BuildRequires:  python3-pyopengl
BuildRequires:  boost-devel
BuildRequires:  bullet-devel
BuildRequires:  cmake
BuildRequires:  console-bridge-devel
BuildRequires:  cppzmq-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  freeimage-devel
BuildRequires:  gdal-devel
BuildRequires:  gperftools-devel
BuildRequires:  graphviz-devel
BuildRequires:  gtest-devel
BuildRequires:  gts-devel
BuildRequires:  hdf5-devel
BuildRequires:  libccd-devel
BuildRequires:  libcurl-devel
BuildRequires:  libtar-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libusb1-devel
BuildRequires:  libXext-devel
BuildRequires:  libxml2-devel
BuildRequires:  ignition-cmake-devel
BuildRequires:  ignition-math-devel >= 4
BuildRequires:  ignition-msgs-devel >= 1
BuildRequires:  ignition-transport-devel >= 4
BuildRequires:  ogre-devel
BuildRequires:  openal-soft-devel
BuildRequires:  protobuf-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qwt-qt5-devel
BuildRequires:  rubygem-ronn
BuildRequires:  sdformat-devel >= 6
BuildRequires:  SkyX-devel
BuildRequires:  tbb2020.3-devel
BuildRequires:  tinyxml-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  urdfdom-headers-devel
BuildRequires:  urdfdom-devel
BuildRequires:  pkgconfig(uuid)

Requires: %{name}-media = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Gazebo is a multi-robot simulator for outdoor environments. It is capable of 
simulating a population of robots, sensors and objects in a three-dimensional 
world. It generates both realistic sensor feedback and physically plausible 
interactions between objects.  It includes an accurate simulation of rigid-body 
physics.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-ode-devel%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       bullet-devel
Requires:       freeimage-devel
Requires:       gdal-devel
Requires:       ogre-devel
Requires:       protobuf-devel
Requires:       qt5-qtbase-devel
Requires:       sdformat-devel
Requires:       tbb-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package common
Summary:       Common directories for %{name}
BuildArch:     noarch

%description common
The %{name}-common package provides common directories for the %{name}
subpackages.

%package libs
Summary:      Shared libraries and plugins for %{name}
Requires:     %{name}-common

%description libs
The %{name}-libs package provides shared libraries and plugins required
at runtime for %{name} and other clients linked against %{name}

%package media
Summary:       Media files for %{name}
Requires:      %{name}-common = %{version}-%{release}
Requires:      %{name} = %{version}-%{release}
Requires:      SkyX
BuildArch:     noarch

%description media
Assets and media files for %{name}

%package ode
Summary:       Gazebo fork of the Open Dynamics Engine

%description ode
Gazebo fork of the Open Dynamics Engine physics library

%package ode-devel
Summary:      Development headers and libraries for gazebo-ode
Requires:     %{name}-ode%{?_isa} = %{version}-%{release}

%description ode-devel
The %{name}-ode-devel package contains libraries and header files for
developing applications that use %{name}-ode.

%package -n player-%{name}
Summary:       Gazebo plugin driver for the Player robot server.
Requires:      %{name}-common = %{version}-%{release}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: player-devel >= 3.1.0

%description -n player-%{name}
Plugin driver for the Player robot server.  Translates gazebo interfaces
to be accessible through the Player server interfaces.

%package doc
Summary:       Development documentation for %{name}
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch

%description doc
Development documentation for %{name}

%prep
%setup -q
%patch 0 -p0 -b .fedora
%patch 2 -p0 -b .rpath
%patch 3 -p0 -b .connection
%patch 5 -p0 -b .fixtest
%patch 6 -p1 -b .gaussianstddev
%patch 9 -p1 -b .py3
%patch 10 -p1 -b .automoc
%patch 11 -p1 -b .singleton
%patch 12 -p1 -b .wayland
%patch 13 -p1 -b .tbb
# Fix boost::placeholders namespace for boost-1.73 (rhbz#1843110)
%patch 14 -p1 -b .boost173
%patch 15 -p1 -b .openal121
%patch 16 -p1 -b .qwt
%patch 17 -p1 -b .gcc13
%patch 18 -p1 -b .graphviz9
%patch 19 -p1 -b .boost174
%patch 20 -p1 -b .graphviz10
# These are either unused, or replaced by system versions
rm -rf deps/ann
rm -rf deps/fcl
rm -rf deps/parallel_quickstep
rm -rf deps/libccd

%build
%cmake  \
 -DCMAKE_VERBOSE_MAKEFILE=ON \
 -DLIB_INSTALL_DIR:STRING="%{_lib}" \
%ifnarch x86_64
 -DSSE2_FOUND=OFF \
%else
 -DSSE2_FOUND=ON \
%endif
 -DSSE3_FOUND=OFF \
 -DSSSE3_FOUND=OFF \
 -DSSE4_1_FOUND=OFF \
 -DSSE4_2_FOUND=OFF \
 -Dogre_library_dirs=%{_libdir} \
 -DCMAKE_BUILD_TYPE=Release \
 -DUSE_UPSTREAM_CFLAGS=OFF \
 -DUSE_HOST_CFLAGS=ON \
 -DCMAKE_INSTALL_DATAROOTDIR=share 

%cmake_build
%cmake_build --target tests
%cmake_build --target doc || exit 0;
%cmake_build --target man || exit 0;
mv %{_vpath_builddir}/doxygen_msgs/html{,_msgs}

%install
%cmake_install

# Get rid of SkyX media files; symlink to the files that SkyX provides
rm -fr %{buildroot}%{_datadir}/%{name}-%{abiversion}/media/skyx
ln -s %{_datadir}/SKYX/Media/SkyX/ %{buildroot}%{_datadir}/%{name}-%{abiversion}/media/skyx

# Get rid of bundled fonts
rm -fr %{buildroot}%{_datadir}/%{name}-%{abiversion}/media/fonts/*.ttf

# Install the example files in the datadir.
cp -pr examples/ %{buildroot}%{_datadir}/%{name}-%{abiversion}

# Install the icon.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
# The icon needs to be square to display properly on some systems.
# Edit the shape of the svg and change the viewport so it looks the same.
sed 'N; s/width="\([0-9\.]*\)"\n\([ ]*\)height="\([0-9\.]*\)"/width="\3"\n\2height="\3"\n\2viewBox="0 0 \1 \3"/' \
    gazebo/gui/images/gazebo.svg > %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Install uncompressed manpages
rm -f %{buildroot}/%{_mandir}/man1/*.gz
install -p -m 0644 %{_vpath_builddir}/tools/*[a-z].1 %{buildroot}%{_mandir}/man1/
install -p -m 0644 %{_vpath_builddir}/gazebo/*[a-z].1 %{buildroot}%{_mandir}/man1/
install -p -m 0644 %{_vpath_builddir}/gazebo/gui/*[a-z].1 %{buildroot}%{_mandir}/man1/

# Install the desktop file.
desktop-file-install  \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}

# Private plugin library: get rid of versioned symlinks,
# move into private subdirectory of libdir
mkdir -p %{buildroot}%{_libdir}/player-3.1
rm -f %{buildroot}/%{_libdir}/libgazebo_player.so
rm -f %{buildroot}/%{_libdir}/libgazebo_player.so.?
mv %{buildroot}/%{_libdir}/libgazebo_player.so.%{version} %{buildroot}%{_libdir}/player-3.1/libgazebo_player.so

rm -f %{buildroot}/%{_libdir}/*.a

%check
# Tests run for informational purposes only
# IGN_IP needs to be set on builders: https://answers.gazebosim.org/question/21103/exception-sending-a-message/
export IGN_IP=127.0.0.1
export GAZEBO_IP=127.0.0.1
%ctest --verbose --parallel 1 --exclude-regex ".*OpenAL.*" || exit 0

%files
%license COPYING LICENSE
%doc AUTHORS
%{_bindir}/*
%{_datadir}/%{name}-%{abiversion}/setup.sh
%{_datadir}/%{name}/setup.sh
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/*.1.*

%files common
%dir %{_datadir}/%{name}-%{abiversion}
%dir %{_datadir}/%{name}-%{abiversion}/examples

%files libs
%exclude %{_libdir}/libgazebo_ode.so.*
%{_libdir}/*.so.*
%{_libdir}/%{name}-%{abiversion}
%{_datadir}/%{name}-%{abiversion}/worlds

%files -n player-%{name}
%{_libdir}/player-3.1/libgazebo_player.so
%{_datadir}/%{name}-%{abiversion}/examples/player

%files media
%{_datadir}/%{name}-%{abiversion}/media
%{_datadir}/%{name}-%{abiversion}/models

%files ode
%license deps/opende/LICENSE-BSD.TXT
%{_libdir}/libgazebo_ode.so.*

%files ode-devel
%{_libdir}/libgazebo_ode.so
%{_libdir}/pkgconfig/gazebo_ode.pc
%dir %{_includedir}/%{name}-%{abiversion}/%{name}
%dir %{_includedir}/%{name}-%{abiversion}
%{_includedir}/%{name}-%{abiversion}/%{name}/ode

%files doc
%license COPYING LICENSE
%doc %{_vpath_builddir}/doxygen/html
%doc %{_vpath_builddir}/doxygen_msgs/html_msgs

%files devel
%{_datadir}/%{name}-%{abiversion}/examples/plugins
%{_datadir}/%{name}-%{abiversion}/examples/ignition
%{_datadir}/%{name}-%{abiversion}/examples/stand_alone
%{_libdir}/*.so
%exclude %{_includedir}/%{name}-%{abiversion}/%{name}/ode
%{_includedir}/%{name}-%{abiversion}
%{_libdir}/pkgconfig/gazebo.pc
%{_libdir}/pkgconfig/gazebo_transport.pc
%{_libdir}/cmake/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 10.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 10.2.0-11
- rebuild for tinyxml2

* Sat Nov 09 2024 Sandro Mani <manisandro@gmail.com> - 10.2.0-10
- Rebuild (GDAL)

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 10.2.0-9
- Rebuild for hdf5 1.14.5

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 10.2.0-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 14 2024 Sandro Mani <manisandro@gmail.com> - 10.2.0-6
- Rebuild (gdal)

* Thu Apr 04 2024 Rich Mattes <richmattes@gmail.com> - 10.2.0-5
- Rebuild for urdfdom-4.0.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 10.2.0-2
- Rebuilt for Boost 1.83
- Build against tbb2020.3 instead of tbb (#2036372)

* Fri Nov 24 2023 Rich Mattes <richmattes@gmail.com> - 10.2.0-1
- Update to release 10.2.0
- Add upstream patch to support Graphviz 9
- Resolves: rhbz#2250639

* Thu Nov 16 2023 Sandro Mani <manisandro@gmail.com> - 10.1.0-40
- Rebuild (gdal)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 12 2023 Sandro Mani <manisandro@gmail.com> - 10.1.0-38
- Rebuild (gdal)

* Sun Feb 26 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.1.0-37
- Backport upstream patch for additional include needed for g++13

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 10.1.0-36
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Sandro Mani <manisandro@gmail.com> - 10.1.0-34
- Rebuild (qwt)

* Sun Nov 13 2022 Sandro Mani <manisandro@gmail.com> - 10.1.0-33
- Rebuild (gdal)

* Sun Sep 25 2022 Rich Mattes <richmattes@gmail.com> - 10.1.0-32
- Rebuild for tinyxml2-9.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.1.0-30
- Patch for openal 1.21

* Sat May 21 2022 Sandro Mani <manisandro@gmail.com> - 10.1.0-29
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 10.1.0-28
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 22 2021 Orion Poplawski <orion@nwra.com> - 10.1.0-26
- Rebuild for hdf5 1.12.1

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 10.1.0-25
- Rebuild (gdal)

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 10.1.0-24
- Rebuilt for protobuf 3.19.0

* Mon Oct 25 2021 Adrian Reber <adrian@lisas.de> - 10.1.0-23
- Rebuilt for protobuf 3.18.1

* Mon Oct 25 2021 Adrian Reber <adrian@lisas.de> - 10.1.0-22
- Rebuilt for protobuf 3.18.1

* Fri Aug 13 2021 Adam Williamson <awilliam@redhat.com> - 10.1.0-21
- Rebuild for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Sandro Mani <manisandro@gmail.com> - 10.1.0-19
- Rebuild (gdal)

* Mon May 10 2021 Jonathan Wakely <jwakely@redhat.com> - 10.1.0-18
- Rebuilt for removed libstdc++ symbols (#1937698)

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 10.1.0-17
- Rebuild (gdal)

* Fri Feb 12 2021 Tom Callaway <spot@fedoraproject.org> - 10.1.0-16
- rebuild for new bullet

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 10.1.0-14
- Rebuilt for Boost 1.75

* Tue Jan 12 16:52:53 CET 2021 Adrian Reber <adrian@lisas.de> - 10.1.0-13
- Rebuilt for protobuf 3.14

* Fri Nov  6 22:42:28 CET 2020 Sandro Mani <manisandro@gmail.com> - 10.1.0-12
- Rebuild (proj, gdal)

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 10.1.0-11
- Rebuilt for protobuf 3.13

* Sat Aug 22 2020 Rich Mattes <richmattes@gmail.com> - 10.1.0-10
- Disable hidden symbols by default to work around run-time errors (rhbz#1871291)
- Explicitly build tests, and only run one test at a time in ctest

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Adrian Reber <adrian@lisas.de> - 10.1.0-7
- Rebuilt for protobuf 3.12

* Fri Jun 05 2020 Björn Esser <besser82@fedoraproject.org> - 10.1.0-6
- Rebuild (boost)

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 10.1.0-5
- Rebuild (gdal)

* Sun Apr 19 2020 Rich Mattes <richmattes@gmail.com> - 10.1.0-4
- Add wayland work-around (rhbz#1816487)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 10.1.0-3
- Rebuild (gdal)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Rich Mattes <richmattes@gmail.com> - 10.1.0-1
- Update to release 10.1.0 (rhbz#1694168)

* Wed Jan 01 2020 Nicolas Chauvet <kwizart@gmail.com> - 9.5.0-11
- Bump for infra

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 9.5.0-10
- Rebuild for protobuf 3.11

* Tue Nov 12 2019 Scott Talbert <swt@techie.net> - 9.5.0-9
- Switch scripts to use Python 3 and BR python3-pyopengl (#1771216)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Scott K Logan <logans@cottsay.net> - 9.5.0-7
- Devel package requires bullet-devel

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 9.5.0-6
- Rebuild for hdf5 1.10.5

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 9.5.0-5
- Rebuild for hdf5 1.10.5

* Sat Feb 23 2019 Rich Mattes <richmattes@gmail.com> - 9.5.0-4
- Fix pkgconfig generation (#1680265)

* Wed Feb 06 2019 Rich Mattes <richmattes@gmail.com> - 9.5.0-3
- Add upstream patch to remove boost::signals

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 9.5.0-2
- Rebuild for tinyxml2 7.x

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 9.5.0-1
- Update to 9.5.0

* Fri Nov 23 2018 Till Hofmann <thofmann@fedoraproject.org> - 8.3.0-5
- Add patch to fix missing include of boost/scoped_ptr

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8.3.0-4
- Rebuild for protobuf 3.6

* Wed Aug 15 2018 Till Hofmann <thofmann@fedoraproject.org> - 8.3.0-3
- Add patch to fix gaussian noise model with stddev == 0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Adam Williamson <awilliam@redhat.com> - 8.3.0-1
- Update to 8.3.0, rebuild for Boost 1.66

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Rich Mattes <richmattes@gmail.com> - 8.1.1-4
- Rebuild for bullet-2.87

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 8.1.1-3
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8.1.1-2
- Rebuild for protobuf 3.4

* Sun Aug 20 2017 Rich Mattes <richmattes@gmail.com> - 8.1.1-1
- Update to release 8.1.1

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 8.0.0-8
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 8.0.0-5
- Rebuilt for Boost 1.64

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 8.0.0-4
- Rebuild for protobuf 3.3.1

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Apr 09 2017 Rich Mattes <richmattes@gmail.com> - 8.0.0-2
- Rebuild for player-3.1.0

* Mon Apr 03 2017 Rich Mattes <richmattes@gmail.com> - 8.0.0-1
- Update to release 8.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Orion Poplawski <orion@cora.nwra.com> - 7.4.0-5
- Rebuild for protobuf 3.2.0

* Wed Nov 23 2016 Rich Mattes <richmattes@gmail.com> - 7.4.0-4
- Add fixes for ftbfs (rhbz#1396676)

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 7.4.0-3
- Rebuild for protobuf 3.1.0

* Wed Oct 26 2016 Rich Mattes <richmattes@gmail.com> - 7.4.0-2
- Add missing ldconfig scriptlets to libs subpackage

* Sun Oct 16 2016 Rich Mattes <richmattes@gmail.com> - 7.4.0-1
- Update to release 7.4.0 (rhbz#1383853)

* Thu Sep 22 2016 Jerry James <loganjerry@gmail.com> - 7.3.1-2
- Rebuild for tbb 2017
- tbb is now available on s390(x)

* Mon Jul 18 2016 Rich Mattes <richmattes@gmail.com> - 7.3.1-1
- Update to release 7.3.1 (rhbz#1247414)

* Tue Jul 05 2016 Rich Mattes <richmattes@gmail.com> - 6.5.1-5
- Remove gazebo_player from gazebo-config.cmake (rhbz#1352931)

* Tue Feb 09 2016 Rich Mattes <richmattes@gmail.com> - 6.5.1-4
- Rebuild for bullet 2.83

* Tue Feb 02 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 6.5.1-3
- Rebuilt for Boost 1.60.

* Fri Jan 15 2016 Jerry James <loganjerry@gmail.com> - 6.5.1-2
- Rebuild for tbb 4.4u2

* Mon Jan 04 2016 Rich Mattes <richmattes@gmail.com> - 6.5.1-1
- Update to release 6.5.1 (rhbz#1247414)

* Sat Oct 17 2015 Kalev Lember <klember@redhat.com> - 5.1.0-8
- Rebuilt for libgeos soname bump

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 5.1.0-7
- Rebuilt for Boost 1.59

* Sun Aug 09 2015 Jonathan Wakely <jwakely@redhat.com> 5.1.0-6
- Patch to fix build with Boost 1.58 (bug #1251699)

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 29 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.1.0-4
- Rebuilt for libgdal 2.0.0

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 5.1.0-3
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Rich Mattes <richmattes@gmail.com> - 5.1.0-1
- Update to release 5.1.0

* Fri May 22 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.2-3
- Use CXXFLAGS in build (bug #1223611)

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 4.0.2-3
- Rebuilt for protobuf soname bump

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 4.0.2-2
- Rebuild for boost 1.57.0

* Sun Nov 02 2014 Rich Mattes <richmattes@gmail.com> - 4.0.2-1
- Update to release 4.0.2

* Mon Oct 20 2014 Rich Mattes <richmattes@gmail.com> - 3.1.0-2
- Devel package requires ogre-devel (rhbz#1154450)

* Sun Sep 28 2014 Rich Mattes <richmattes@gmail.com> - 3.1.0-1
- Update to release 3.1.0

* Fri Sep 12 2014 Rich Mattes <richmattes@gmail.com> - 3.0.0-7
- Add gazebo library path to pkgconfig

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Rich Mattes <richmattes@gmail.com> - 3.0.0-5
- Add arch specific requirements

* Mon Jun 23 2014 Rich Mattes <richmattes@gmail.com> - 3.0.0-4
- Create a gazebo-common subpackage to own directories in datadir
- Have gazebo and gazebo-media depend on each other
- Remove rpath and other brokenness from pkgconfig and cmake scripts

* Mon Jun 09 2014 Rich Mattes <richmattes@gmail.com> - 3.0.0-3
- Update to address review comments, including:
- Remove libgazebo_player from link library list
- Add patch to gazebo transport to fix boost
- Add gdal-devel to -devel Requires
- Export path and library path before running tests
- Disable tests that don't have the proper build deps
- Dump test logs on test failure

* Wed May 21 2014 Rich Mattes <richmattes@gmail.com> - 3.0.0-2
- Remove fonts from media package

* Mon May 19 2014 Rich Mattes <richmattes@gmail.com> - 3.0.0-1
- Update to release 3.0.0
- Add ODE subpackage

* Mon Mar 03 2014 Rich Mattes <richmattes@gmail.com> - 2.2.1-3
- Fix issues with conflicting ownership of directories in datadir

* Mon Feb 10 2014 Rich Mattes <richmattes@gmail.com> - 2.2.1-2
- Remove libgazebo_player from link list

* Mon Jan 20 2014 Rich Mattes <richmattes@gmail.com> - 2.2.1-1
- Update to release 2.2.1
- Install desktop and icon files using Scott Logan's patch
- Fix gazebo-config.cmake so other CMake projects can build against Gazebo
- Add missing runtime dependencies to the -devel file

* Thu Jan 16 2014 Rich Mattes <richmattes@gmail.com> - 2.1.0-2
- Add patch to fix qreal usage on ARM (upstream issue 1007)

* Sun Jan 05 2014 Rich Mattes <richmattes@gmail.com> - 2.1.0-1
- Update to release 2.1.0

* Sun Oct 06 2013 Rich Mattes <richmattes@gmail.com> - 2.0.0-1
- Update to release 2.0.0

* Sat May 25 2013 Rich Mattes <richmattes@gmail.com> - 1.8.1-1
- Update to release 1.8.1

* Sat Apr 20 2013 Rich Mattes <richmattes@gmail.com> - 1.7.1-1
- Update to release 1.7.1

* Fri Apr 19 2013 Rich Mattes <richmattes@gmail.com> - 1.6.3-1
- Update to release 1.6.3

* Tue Mar 12 2013 Rich Mattes <richmattes@gmail.com> - 1.5.0-1
- Update to release 1.5.0

* Wed Jan 16 2013 Rich Mattes <richmattes@gmail.com> - 1.3.1-1
- Update to release 1.3.1

* Fri Nov 09 2012 Rich Mattes <richmattes@gmail.com> - 1.2.6-1
- Update to release 1.2.6

* Mon Oct 29 2012 Rich Mattes <richmattes@gmail.com> - 1.2.5-1
- Update to release 1.2.5

* Tue Oct 16 2012 Rich Mattes <richmattes@gmail.com> - 1.2.2-1
- Update to release 1.2.2

* Tue May 29 2012 Rich Mattes <richmattes@gmail.com> - 1.0.1-2
- Clean up patches, incorperate build system fixes to patches
- Add player subpackage

* Fri May 25 2012 Rich Mattes <richmattes@gmail.com> - 1.0.1-1
- Update to version 1.0.1

* Thu Apr 26 2012 Rich Mattes <richmattes@gmail.com> - 1.0.0-1
- Initial package
