# Try opting-out of LTO, due to test failures
%define _lto_cflags %{nil}

%global soversion 26

Name:           libopenshot
Version:        0.3.3
Release:        7%{?dist}
Summary:        Library for creating and editing videos

# See .reuse/dep5 for details
License:        LGPL-3.0-or-later and BSD-3-Clause
URL:            http://www.openshot.org/
Source0:        https://github.com/OpenShot/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# libopenshot is completely broken on ppc64le, see rfbz #5528
ExcludeArch:    ppc64le

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  alsa-lib-devel
BuildRequires:  babl-devel
BuildRequires:  ImageMagick-c++-devel
# EPEL 8 don't have ffmpeg-free so we can't build it on EPEL 8
BuildRequires:  ffmpeg-free-devel
BuildRequires:  opencv-devel
BuildRequires:  protobuf-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  unittest-cpp-devel
BuildRequires:  cppzmq-devel
BuildRequires:  zeromq-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libopenshot-audio-devel >= 0.3.2
BuildRequires:  catch-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-setuptools


%description
OpenShot Library (libopenshot) is an open-source project
dedicated to delivering high quality video editing, animation,
and playback solutions to the world.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n     python%{python3_pkgversion}-%{name}
Summary:        Python bindings for %{name}
BuildRequires:  swig >= 3.0
BuildRequires:  python%{python3_pkgversion}-libs
BuildRequires:  python%{python3_pkgversion}-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      python-%{name} < 0.1.1-2
Provides:       python-%{name} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}
The python-%{name} package contains python bindings for
applications that use %{name}.


%package -n     ruby-%{name}
Summary:        Ruby bindings for %{name}
BuildRequires:  ruby-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ruby-%{name}
The ruby-%{name} package contains ruby bindings for
applications that use %{name}.


%prep
%autosetup -p1

rm -rf third_party/jsoncpp

%build
%cmake -Wno-dev -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%check
# Some tests soft-fail because of missing OpenH264
%cmake_build --target test || :

%install
%cmake_install

%files
%doc AUTHORS README.md
%license LICENSES/* .reuse/dep5
%{_libdir}/%{name}.so.%{soversion}
%{_libdir}/%{name}.so.%{version}

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so

%files -n python%{python3_pkgversion}-libopenshot
%pycached %{python3_sitearch}/openshot.py
%{python3_sitearch}/_openshot.so

%files -n ruby-libopenshot
%{ruby_vendorarchdir}/openshot.so

%changelog
* Tue Feb 04 2025 Sérgio Basto <sergio@serjux.com> - 0.3.3-7
- Rebuild for opencv-4.11.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.3-5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Mon Sep 23 2024 Fabio Valentini <decathorpe@gmail.com> - 0.3.3-4
- Rebuild for ffmpeg 7

* Thu Jul 25 2024 Sérgio Basto <sergio@serjux.com> - 0.3.3-3
- Rebuild for opencv 4.10.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 13 2024 Sérgio Basto <sergio@serjux.com> - 0.3.3-1
- Update libopenshot to 0.3.3 (#2294047)

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.3.2-6
- Rebuilt for Python 3.13

* Mon Feb 05 2024 Sérgio Basto <sergio@serjux.com> - 0.3.2-5
- Rebuild for opencv 4.9.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild
- BR: python3-setuptools to fix ModuleNotFoundError: No module named 'distutils'

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.2-2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Aug 11 2023 Sérgio Basto <sergio@serjux.com> - 0.3.2-1
- Update libopenshot to 0.3.2

* Mon Aug 07 2023 Sérgio Basto <sergio@serjux.com> - 0.3.0-5
- Rebuild for opencv 4.8.0

* Fri Aug 04 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.3.0-4
- Add check section and run tests

* Sun Jan 15 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.3.0-3
- Import to Fedora

* Fri Jan 13 2023 Sérgio Basto <sergio@serjux.com> - 0.3.0-2
- Rebuild for ImageMagick 7.1

* Fri Dec 02 2022 Leigh Scott <leigh123linux@gmail.com> - 0.3.0-1
- New upstream release

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Sat Jun 25 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.7-7
- Rebuilt for Python 3.11

* Thu Jun 23 2022 Sérgio Basto <sergio@serjux.com> - 0.2.7-6
- Rebuilt for opencv 4.6.0
- Fix cmake build

* Sun Feb 06 2022 Leigh Scott <leigh123linux@gmail.com> - 0.2.7-5
- Rebuilt for ffmpeg

* Fri Nov 12 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.2.7-4
- rebuilt

* Tue Nov 09 2021 Leigh Scott <leigh123linux@gmail.com> - 0.2.7-3
- Rebuilt for new ffmpeg snapshot

* Mon Nov 08 2021 Leigh Scott <leigh123linux@gmail.com> - 0.2.7-2
- rebuilt

* Tue Sep 07 2021 Leigh Scott <leigh123linux@gmail.com> - 0.2.7-1
- New upstream release

* Thu Aug 26 2021 Leigh Scott <leigh123linux@gmail.com> - 0.2.6-1
- New upstream release

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Leigh Scott <leigh123linux@gmail.com> - 0.2.5-9
- Rebuild for python-3.10

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Leigh Scott <leigh123linux@gmail.com> - 0.2.5-7
- Rebuilt for new ffmpeg snapshot

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Add patch from upstream to fix unit test failures

* Tue Aug 04 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.2.5-5
- Updates for Fedora 33 build changes

* Tue Jun 02 2020 Leigh Scott <leigh123linux@gmail.com> - 0.2.5-4
- Fix gcc-10 -fno-common issue

* Sat May 30 2020 Leigh Scott <leigh123linux@gmail.com> - 0.2.5-3
- Rebuild for python-3.9

* Wed May 20 2020 Sérgio Basto <sergio@serjux.com> - 0.2.5-2
- Rebuild for ImageMagick on el7

* Sat Mar 07 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.2.5-1
- New upstream release

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.2.4-2
- Rebuild for ffmpeg-4.3 git

* Thu Feb 13 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.2.4-1
- New upstream release
- Drop upstreamed patches / fixes, relax libopenshot-audio dependency
- Disable building Ruby bindings on ppc64le due to compilation failures

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.3-5.20190912gitc685571
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.2.3-4
- Update to git HEAD for compatibility with OpenShot update
- Remove CMAKE_SKIP_RPATH per current packaging guidelines
- Delete outdated copy of standard CMake module, causes python3.8 failures

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 0.2.3-3.20190406git101f25a
- Rebuild for new ffmpeg version

* Sun Jun 23 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.2.3-3
- Add explicit Requires: zeromq, to work around other EL7
  packages which provide the required libzmq.so.5

* Tue Apr 09 2019 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.2.3-2
- Upgrade to latest git revision, to fix FTBFS with GCC9 on Fedora 30
- Requires libopenshot-audio also built from same or later gitrev
- Drop upstreamed patches

* Fri Mar 22 2019 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.2.3-1
- New upstream release
- Drop upstreamed patches

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-2
- Rebuild for ffmpeg-3.4.5 on el7
- Use ldconfig_scriptlets macros
- Use default compiler flags
- Use CMake3
- Patched for using CMake3's Swig variable
- Remove obsolete Group tags

* Mon Sep 24 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.2.2-1
- New upstream release
- Unbundle jsoncpp
- Drop ffmpeg patch (upstreamed), add patch to fix tests env

* Wed Aug 29 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.2.0-2
- Rebuilt for new ImageMagick 6.9.10.10

* Tue Jul 31 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.2.0-1
- New upstream release

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-6
- Rebuilt for Python 3.7

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.9-5
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 17 2018 Sérgio Basto <sergio@serjux.com> - 0.1.9-3
- require libopenshot-audio 0.1.5

* Wed Jan 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.1.9-2.1
- Rebuilt for ffmpeg-3.5 git

* Sat Jan 13 2018 Richard Shaw <hobbes1069@gmail.com> - 0.1.9-1.1
- Build against correct libopenshot-audio.

* Sat Jan 13 2018 Richard Shaw <hobbes1069@gmail.com> - 0.1.9-1
- Update to latest upstream release.

* Wed Nov 22 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.1.8-3
- Adjust python for el7

* Tue Oct 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.1.8-2
- Rebuild for ffmpeg update

* Thu Sep 07 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.1.8-1
- Update libopenshot to 0.1.8

* Sat Sep 02 2017 Sérgio Basto <sergio@serjux.com> - 0.1.7-1
- Update libopenshot to 0.1.7
- Fix compilation with GCC 7 by adding -Wno-error, reference
  https://github.com/monocasual/giada/issues/139

* Sun Aug 27 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.1.6-2
- Rebuilt for ImageMagick

* Fri May 19 2017 Richard Shaw <hobbes1069@gmail.com> - 0.1.6-1
- Update to latest upstream release.

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.1.4-2
- Rebuild for ffmpeg update

* Thu Apr 06 2017 Sérgio Basto <sergio@serjux.com> - 0.1.4-1
- Update to 0.1.4

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 14 2017 Richard Shaw <hobbes1069@gmail.com> - 0.1.3-1
- Update to latest upstream release.

* Mon Oct 17 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.2-1
- Update to latest upstream release.

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.1.1-3
- Rebuilt for ffmpeg-3.1.1

* Mon Apr 18 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.1-2
- Rename python-libopenshot to python3-libopenshot.

* Fri Apr  8 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.1-1
- Update to latest upstream release.

* Tue Feb  9 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.0-1
- Update to latest upstream release.

* Mon Nov 16 2015 Richard Shaw <hobbes1069@gmail.com> - 0.0.6-1
- Update to latest upstream release.

* Wed Jun 24 2015 Sérgio Basto <sergio@serjux.com> - 0.0.4-2
- Fixed unused-direct-shlib-dependency in cmake with global optflags,
  instead use "export CXXFLAGS" that was override all flags .

* Mon May 18 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 0.0.4-1
- New upstream release 0.0.4
- Fix FTBFS (rf#3624)

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 0.0.3-4
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.0.3-3
- Rebuilt for FFmpeg 2.4.x

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.0.3-2
- Rebuilt for FFmpeg 2.4.x

* Tue Jul 15 2014 Richard Shaw <hobbes1069@gmail.com> - 0.0.3-1
- Initial packaging.
