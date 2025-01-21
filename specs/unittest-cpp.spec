%global         _hardened_build 1
%global         oldname     UnitTest++

Name:           unittest-cpp
Version:        2.0.0
Release:        20%{?dist}
Summary:        Lightweight unit testing framework for C++
License:        MIT

URL:            https://github.com/%{name}/%{name}
Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz
# documentation from 1.4 tarball: docs/UnitTest++.html
Source1:        %{name}.html
# Fix configure.ac version test
Patch0:         fix_version_2.0.0.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  libtool

%description
%{name} is a lightweight unit testing framework for C++.
Simplicity, portability, speed, and small footprint are all
very important aspects of %{name}.

%package devel
Summary:        Object files for development using %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the object files
necessary for developing test programs.

%package static
Summary:        Static library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains the object files
necessary for statically linking test programs.

%prep
%autosetup -p1
cp -p %SOURCE1 .
# autoreconf will complain about missing NEWS and README files
touch NEWS
ln README.md README
# autoreconf will add a GPLv3 license text in COPYING
ln LICENSE COPYING
autoreconf -i

%build
%configure
# rpmlint unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%check
make check

%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{oldname}.la

%files
%doc AUTHORS README.md
%license LICENSE
%{_libdir}/lib%{oldname}.so.2*

%files devel
%doc %{name}.html
%{_includedir}/%{oldname}
%{_libdir}/lib%{oldname}.so
%{_libdir}/pkgconfig/UnitTest++.pc

%files static
%{_libdir}/lib%{oldname}.a

%ldconfig_scriptlets

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Leigh Scott <leigh123linux@gmail.com> - 2.0.0-9
- Update to 2.0.0 release 

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Raphael Groner <projects.rg@smart.ms> - 2.0.0-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 07 2016 Raphael Groner <projects.rg@smart.ms> - 1.6.1-1
- bump to v1.6.1, rhbz#1333400

* Mon Mar 28 2016 François Cami <fcami@fedoraproject.org> - 1.6.0-1.20160301gitb69b63a
- Update to 1.6.0 + drop our .pc file (ship upstream's instead).

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-19.20130823gite76d25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-18.20130823gite76d25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4-17.20130823gite76d25a
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-16.20130823gite76d25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-15.20130823gite76d25a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 22 2013 Luke Benstead <kazade@fedoraproject.org> - 1.4-14.20130823gite76d25a
- Fix .spec file after previous change

* Fri Nov 22 2013 Luke Benstead <kazade@fedoraproject.org> - 1.4-13.20130823gite76d25a
- Rename the .pc file to be consistent with other platforms

* Fri Nov 22 2013 François Cami <fcami@fedoraproject.org> - 1.4-12.20130823gite76d25a
- Misc. spec fixes.

* Thu Nov 21 2013 Luke Benstead <kazade@fedoraproject.org> - 1.4-11.20130823gite76d25a
- Bump to latest upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11.20130509gitc42e68b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 06 2013 François Cami <fcami@fedoraproject.org> - 1.4-10.20130509gitc42e68b
- Make -static depend on -devel. Suggested by Michael Schwendt.

* Fri May 31 2013 François Cami <fcami@fedoraproject.org> - 1.4-9.20130509gitc42e68b
- Use github directly for git tarball generation.
- Move autoreconf to %%build.
- Add %%check.
- Removed duplicate files.
- All changes suggested by Björn Esser.

* Thu May 30 2013 François Cami <fcami@fedoraproject.org> - 1.4-8.20130509gitc42e68bb
- Switch upstream from http://sf.net/projects/unittest-cpp
  to https://github.com/unittest-cpp/unittest-cpp
- Rebase sources to c42e68bb999d01da9ec71b67ff1a2cbd6ec1b6a6
- Use consistent naming as much as possible.
- Use autotools to build both shared and static libraries.
- Most changes suggested by Michael Schwendt.

* Wed Mar 13 2013 François Cami <fcami@fedoraproject.org> - 1.4-7
- Fix linker flags breakage.

* Tue Mar 12 2013 François Cami <fcami@fedoraproject.org> - 1.4-6
- Replace %%define with %%global.

* Wed Mar 6 2013 François Cami <fcami@fedoraproject.org> - 1.4-5
- Remove unneeded space in sed expression. 

* Wed Mar 6 2013 François Cami <fcami@fedoraproject.org> - 1.4-4
- Use consistent naming in .pc file (fix by Luke Benstead).

* Wed Feb 27 2013 François Cami <fcami@fedoraproject.org> - 1.4-3
- Use multi-line, single-instance sed, courtesy of Dennis Johnson.

* Sat Feb 23 2013 François Cami <fcami@fedoraproject.org> - 1.4-2
- Change package name. Add .pc file courtesy of Luke Benstead.

* Sat Feb 02 2013 François Cami <fcami@fedoraproject.org> - 1.4-1
- Initial Fedora RPM.

