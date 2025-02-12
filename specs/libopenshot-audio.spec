%global soversion 10

Name:           libopenshot-audio
Version:        0.4.0
Release:        1%{?dist}
Summary:        Audio library used by OpenShot

License:        GPL-3.0-or-later
URL:            http://openshot.org/
Source0:        https://github.com/OpenShot/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# Disabling libopenshot-audio due to libopenshot exclusion, see rfbz #5528
ExcludeArch:    ppc64le

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  alsa-lib-devel
BuildRequires:  zlib-devel

# This is a modified version of JUCE
Provides:       bundled(JUCE) = 5.4.3
# JUCE has modified versions of these
Provides:       bundled(flac) = 1.3.1
Provides:       bundled(libvorbis) = 1.3.2

%description
OpenShot Audio Library (libopenshot-audio) is an open-source
project based on JUCE, and enables high-quality audio editing
and playback for libopenshot.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        demo
Summary:        Program for demonstrating %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    demo
%{summary}.


%prep
%autosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license COPYING
%doc AUTHORS README.md
%{_libdir}/%{name}.so.%{soversion}
%{_libdir}/%{name}.so.%{version}

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/cmake/OpenShotAudio/

%files demo
%{_bindir}/openshot-audio-demo
%{_mandir}/man1/openshot-audio-demo.1*


%changelog
* Mon Feb 10 2025 Sérgio Basto <sergio@serjux.com> - 0.4.0-1
- Update libopenshot-audio to 0.4.0

* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 13 2024 Sérgio Basto <sergio@serjux.com> - 0.3.3-1
- Update libopenshot-audio to 0.3.3 (#2294047)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 11 2023 Sérgio Basto <sergio@serjux.com> - 0.3.2-1
- Update libopenshot-audio to 0.3.2 (#2185294)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 15 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.3.0-2
- Adapt for Fedora

* Fri Dec 02 2022 Leigh Scott <leigh123linux@gmail.com> - 0.3.0-1
- New upstream release

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 07 2021 Leigh Scott <leigh123linux@gmail.com> - 0.2.2-1
- New upstream release

* Thu Aug 26 2021 Leigh Scott <leigh123linux@gmail.com> - 0.2.1-1
- New upstream release

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Aug 04 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.2.0-2
- Update build configs for Fedora 33

* Sat Mar 07 2020 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.2.0-1
- New upstream release

* Thu Feb 13 2020 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.9-1
- New upstream release

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.8-4.20190405git7001b68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.8-3.20190405git7001b68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.8-2
- Upgrade to latest git revision, to fix FTBFS with GCC9 on Fedora 30
- libopenshot-audio upgraded to JUCE 5.4.3 internally
- Drop patches upstreamed or made unnecessary by JUCE update

* Fri Mar 22 2019 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.8-1
- New upstream release

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.7-2
- Update patch to completely remove Xinerama dependency

* Mon Sep 24 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.7-1
- New upstream release

* Tue Jul 31 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.6-1
- New upstream release

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Richard Shaw <hobbes1069@gmail.com> - 0.1.5-1
- Update to latest upstream release.

* Sat Sep 02 2017 Sérgio Basto <sergio@serjux.com> - 0.1.4-1
- Update libopenshot-audio to 0.1.4

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.2-1
- Update to latest upstream release.

* Fri Apr  8 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.1-1
- Update to latest upstream release.

* Mon Nov 16 2015 Richard Shaw <hobbes1069@gmail.com> - 0.0.6-1
- Update to latest upstream release.

* Thu Jun 25 2015 Sérgio Basto <sergio@serjux.com> - 0.0.4-2
- Fixed unused-direct-shlib-dependency in cmake with global optflags.

* Mon May 18 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 0.0.4-1
- New upstream release 0.0.4

* Tue Jul 15 2014 Richard Shaw <hobbes1069@gmail.com> - 0.0.3-1
- Initial packaging.
