%global __cmake_in_source_build 1
Name:           chipmunk
Version:        7.0.3
Release:        16%{?dist}
Summary:        Physics engine for 2D games

License:        MIT
URL:            https://github.com/slembcke/Chipmunk2D/
Source0:        https://github.com/slembcke/Chipmunk2D/archive/Chipmunk-%{version}.tar.gz
Patch0:         sysctl.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: freeglut-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel
BuildRequires: make

%description
Chipmunk is a 2D rigid body physics library distributed under the MIT license.
Though not yet complete, it is intended to be fast, numerically stable, and 
easy to use.


%package        devel
Summary:        Development tools for programs which will use the chipmunk library
Requires:       %{name} = %{version}-%{release}

%description    devel
Chipmunk is a 2D rigid body physics library distributed under the MIT license.
Though not yet complete, it is intended to be fast, numerically stable, and 
easy to use.

This package contains the header files and  static libraries to develop
programs that will use the chipmunk library.  You should
install this package if you need to develop programs which will use the 
chipmunk library functions.  You'll also need to install the chipmunk package.

%prep
%setup -qn Chipmunk2D-Chipmunk-%{version}
%patch -P0 -p0

%build
%{cmake}
%{__make} VERBOSE=1 %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
%make_install

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc README.textile
%{_libdir}/*.so.*
%exclude %{_libdir}/*.a

%files devel
%doc doc/ demo/
%{_includedir}/chipmunk
%{_libdir}/*.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 7.0.3-11
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 7.0.3-5
- Fix FTBFS.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 7.0.3-1
- 7.0.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Jon Ciesla <limburgher@gmail.com> - 5.3.4-13
- ExcludeArch ppc64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Jon Ciesla <limburgher@gmail.com> - 5.3.4-7
- Clean out ruby bits for good, BZ 1089260.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Jon Ciesla <limb@jcomserv.net> - 5.3.4-1
- latest upstream.

* Fri Aug 20 2010 Jon Ciesla <limb@jcomserv.net> - 5.3.1-1
- latest upstream.

* Thu Jul 15 2010 Jon Ciesla <limb@jcomserv.net> - 5.2.0-1
- Latest upstream, BZ 545475.
- Dropped cmake patch, updated dsolink patch.
- Dropped ruby extension for now, not up to date per upstream.

* Mon Jun 28 2010 Jon Ciesla <limb@jcomserv.net> - 4.1.0-9
- Fix FTBFS, BZ 599950.

* Thu Oct  1 2009 Hans de Goede <hdegoede@redhat.com> - 4.1.0-8
- Fix FTBFS

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Jon Ciesla <limb@jcomserv.net> - 4.1.0-6
- ruby extension fix, BZ 489187.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 08 2009 Jon Ciesla <limb@jcomserv.net> - 4.1.0-4
- Attempted 64-bit fix.

* Wed Jan 07 2009 Jon Ciesla <limb@jcomserv.net> - 4.1.0-3
- Review fixes.

* Wed Jan 07 2009 Jon Ciesla <limb@jcomserv.net> - 4.1.0-2
- Review fixes.

* Mon Dec 01 2008 Jon Ciesla <limb@jcomserv.net> - 4.1.0-1
- New version.

* Mon Sep 15 2008 Jon Ciesla <limb@jcomserv.net> - 4.0.2-1
- Created package.
