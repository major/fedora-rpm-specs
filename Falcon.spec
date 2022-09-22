%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global host     www.falconpl.org
# latest bugfix release does not come with updated docs
# remove once the releases are synced again
%global docver   %{version}

Name:            Falcon
Version:         0.9.6.8
Release:         25%{?dist}
Summary:         The Falcon Programming Language
Summary(it):     Il linguaggio di programmazione Falcon

License:        GPLv2+
URL:            http://%{host}/
Source0:        http://%{host}/project_dl/_official_rel/%{name}-%{version}.tgz
Source1:        http://%{host}/project_dl/_official_rel/%{name}-docs-%{docver}.tgz
# Patches from Git for Falcon's mongo modules
Patch0:         Falcon-0.9.6.8-mongo-cmake-linux-x64.patch
Patch1:         Falcon-0.9.6.8-mongo-stdint.patch
Patch2:         Falcon-0.9.6.8-gcc10.patch

%if 0%{?rhel} <= 5
%endif

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)

%description
The Falcon Programming Language is an embeddable scripting language
aiming to empower even simple applications with a powerful,
flexible, extensible and highly configurable scripting engine.

Falcon is also a standalone multiplatform scripting language that
aims to be both simple and powerful.

%description -l it
Il Falcon è un linguaggio di programmazione embeddabile che intende
fornire nuove potenzialità anche a semplici applicazioni, fornendo
loro un potente, flessibie, estendibile e configurabile motore
di scripting.

Falcon è anche uno scripting languge completo e multipiattaforma,
semplice e potente.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name} = %{version}-%{release}
Requires:  cmake

%description devel
The Falcon Programming Language is an embeddable scripting language
aiming to empower even simple applications with a powerful,
flexible, extensible and highly configurable scripting engine.

Falcon is also a standalone multiplatform scripting language that
aims to be both simple and powerful.

This package contains development files for %{name}. This is not
necessary for using the %{name} interpreter.

%package   doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
The Falcon Programming Language is an embeddable scripting language
aiming to empower even simple applications with a powerful,
flexible, extensible and highly configurable scripting engine.

Falcon is also a standalone multiplatform scripting language that
aims to be both simple and powerful.

This package contains HTML documentation for %{name}.


%prep
%setup -q -a1
%patch0 -p1 -b .mongo-cmake-linux-x64
%patch1 -p1 -b .mongo-stdint
%patch2 -p1 -b .gcc10


%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
reldocdir=$(echo %{_pkgdocdir} | sed -e 's|^%{_prefix}/||')
%cmake . \
       -DFALCON_SHARE_DIR=$reldocdir
#-DFALCON_LIB_DIR=%{_lib} \
#       -DFALCON_CMAKE_DIR=%{_lib}/falcon/cmake \

%cmake_build


%install
%cmake_install
cp -pR %{docver}-html $RPM_BUILD_ROOT%{_pkgdocdir}


%ldconfig_scriptlets


%files
%doc %{_pkgdocdir}
%exclude %{_pkgdocdir}/%{docver}-html
%exclude %{_bindir}/falcon-conf
%exclude %{_bindir}/falconeer.fal
%exclude %{_bindir}/faltest
%{_bindir}/*
%exclude %{_mandir}/man1/falcon-conf*
%exclude %{_mandir}/man1/falconeer.fal*
%exclude %{_mandir}/man1/faltest*
%{_libdir}/falcon
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%{_bindir}/falcon-conf
%{_bindir}/falconeer.fal
%{_bindir}/faltest
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/cmake/faldoc
%{_mandir}/man1/falcon-conf*
%{_mandir}/man1/falconeer.fal*
%{_mandir}/man1/faltest*

%files doc
%doc %{_pkgdocdir}/%{docver}-html


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Jeff Law <law@redhat.com> - 0.9.6.8-21
- Force C++14 as this code is not C++17 ready

* Tue Aug 25 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.6.8-20
- Fix for CMake macro changes
- Consistently use pkgconfig for build requirements
- Add optional dependencies (curl, SDL)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 0.9.6.8-18
- Fix narrowing conversion problem caught by gcc-10

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.6.8-8
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 11 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.9.6.8-5
- Install docs to %%{_pkgdocdir} where available (#993747).

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar  6 2012 Michel Salim <salimma@fedoraproject.org> - 0.9.6.8-1
- Update to 0.9.6.8

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.6-4
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov  5 2010 Michel Salim <salimma@fedoraproject.org> - 0.9.6.6-1
- Update to 0.9.6.6

* Wed Sep 23 2009 Michel Salim <salimma@fedoraproject.org> - 0.9.4.2-1
- Update to 0.9.4.2
- Package documentation files

* Tue Aug 25 2009 Michel Salim <salimma@fedoraproject.org> - 0.9.4-1
- Update to 0.9.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  6 2009 Michel Salim <salimma@fedoraproject.org> - 0.8.14.2-1
- Update to 0.8.14.2

* Mon Jun  9 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.8.10-3
- Revert r401 patch; does not fix cmake-2.6 problem on Rawhide
  Reverting to manually using 'make install' in individual subdirectories

* Mon Jun  9 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.8.10-2
- Merge in cmake fixes from core/trunk r401
- Patch core/CMakeLists.txt to default to /usr, as it appears that the
  requested prefix is not properly used
- Fix incorrect #! interpreter in falconeer.fal

* Sat Jun  7 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.8.10-1
- Update to 0.8.10

* Wed May 21 2008 Michel Salim <salimma@fedoraproject.org> - 0.8.8-3
- Use correct libdir for module path

* Thu Apr 24 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.8.8-2
- Updated license
- Changed source URL to one that includes license grant

* Fri Jan 25 2008 Michel Salim <michel.sylvan@gmail.com> - 0.8.8-1
- Initial Fedora package
  Based on initial spec by Giancarlo Niccolai <gc@falconpl.org>
