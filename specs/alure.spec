# Force out of source build
%undefine __cmake_in_source_build

Name:           alure
Version:        1.2
Release:        33%{?dist}
Summary:        Audio Library Tools REloaded
# ALURE code is LGPLv2+; note -devel subpackage has its own license tag
License:        LGPL-2.1-or-later
URL:            http://kcat.strangesoft.net/alure.html
Source0:        http://kcat.strangesoft.net/%{name}-releases/%{name}-%{version}.tar.bz2
Patch0:         alure-gcc47.patch
Patch1:         alure-1.2-fluidsynth-cflags-fix.patch
Patch2:		alure-1.2-use-unique_ptr.patch
Patch3:		alure-1.2-sndfile-cflags-fix.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake, libvorbis-devel, libsndfile-devel, openal-soft-devel, flac-devel, dumb-devel, fluidsynth-devel

%description
ALURE is a utility library to help manage common tasks with OpenAL
applications. This includes device enumeration and initialization,
file loading, and streaming.

%package        devel
Summary:        Development files for %{name}
# Devel doc includes some files under GPLv2+ from NaturalDocs
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch -P0
%patch -P1 -p1 -b .fluidsynth-cflags-fix
%patch -P2 -p1 -b .unique_ptr
%patch -P3 -p1 -b .sndfile-cflags-fix

%build
%cmake -DBUILD_STATIC:BOOL=OFF
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
# strip installed html doc
rm -rf %{buildroot}%{_docdir}/alure/html

%ldconfig_scriptlets

%files
%doc COPYING
%{_libdir}/*.so.*
%{_bindir}/alure*

%files devel
%doc docs/html examples
%{_includedir}/AL/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Tom Callaway <spot@fedoraproject.org> - 1.2-32
- fix FTBFS, apply a minor C++ cleanup

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Tom Callaway <spot@fedoraproject.org> - 1.2-26
- fix FTBFS

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2-9
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 30 2012 Bruno Wolff III <bruno@wolff.to> - 1.2-3
- Fix for gcc 4.7

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 29 2011 Julian Aloofi <julian@fedoraproject.org> - 1.2-1
- update to latest upstream release

* Sat May 28 2011 Julian Aloofi <julian@fedoraproject.org> - 1.1-1
- update to latest upstream release
- enabled FLAC, DUMB and fluidsynth support

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 01 2009 Guido Grazioli <guido.grazioli@gmail.com> - 1.0-4
- Fixed license for -devel subpackage
- Included sample code in -devel subpackage
- Sanitized %%files

* Tue Sep 29 2009 Guido Grazioli <guido.grazioli@gmail.com> - 1.0-3
- Renamed from libalure to alure
- Fixed license

* Mon Sep 28 2009 Guido Grazioli <guido.grazioli@gmail.com> - 1.0-2
- Fix multilib pkgconfig path

* Sat Sep 26 2009 Guido Grazioli <guido.grazioli@gmail.com> - 1.0-1
- Initial packaging 
