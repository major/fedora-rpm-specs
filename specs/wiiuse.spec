%undefine __cmake_in_source_build
%global commit dfbe3d2cd21d3d88d7ba9de39cfc8aa901a6041b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wiiuse
Version:        0.15.5
Release:        14%{?dist}
Summary:        The wiiuse library is used to access and control multiple Nintendo Wiimotes
License:        GPL-3.0-or-later
URL:            https://github.com/rpavlik/wiiuse
Source0:        https://github.com/rpavlik/wiiuse/archive/%{version}/%{name}-%{version}.tar.gz
#Patch0:         wiiuse-freeglut.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  bluez-libs-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  freeglut-devel
BuildRequires:  SDL-devel
BuildRequires:  dos2unix
BuildRequires:  cmake
BuildRequires:  /usr/bin/chrpath

%description
A library that implements access to wiiremote controllers via bluetooth.

%package devel
Summary: Developer tools for the wiiuse library
Requires: bluez-libs-devel
Requires: wiiuse = %{version}-%{release}

%description devel
Header files needed to develop programs that link against the wiiuse library.

%package examples
Summary: Example programs for the wiiuse library
Requires: wiiuse = %{version}-%{release}

%description examples
Example programs to test accessing wiiremote controllers

%prep
%autosetup -p0

#Convert all relevant files to unix charset
for i in CHANGELOG.mkd README.mkd; do dos2unix $i; done
for i in example*/*; do dos2unix $i; done
for i in src/*; do dos2unix $i; done

%build
%cmake
%cmake_build

%install
# Can't use make install as it is a pathetic copy into fixed paths and won't
# work on x86_64
install -Dpm 0755 %{_vpath_builddir}/src/libwiiuse.so %{buildroot}%{_libdir}/libwiiuse.so.0
ln -s libwiiuse.so.0 %{buildroot}%{_libdir}/libwiiuse.so
install -Dpm 0644 src/wiiuse.h %{buildroot}%{_includedir}/wiiuse.h
install -Dpm 0755 %{_vpath_builddir}/example/wiiuseexample %{buildroot}%{_bindir}/wiiuseexample
install -Dpm 0755 %{_vpath_builddir}/example-sdl/wiiuseexample-sdl %{buildroot}%{_bindir}/wiiuseexample-sdl
chrpath -d %{buildroot}%{_bindir}/wiiuseexample*

%files
%{_libdir}/libwiiuse.so.0
%license LICENSE
%doc CHANGELOG.mkd README.mkd

%files devel
%{_includedir}/wiiuse.h
%{_libdir}/libwiiuse.so

%files examples
%doc example/example.c example-sdl/sdl.c
%{_bindir}/wiiuseexample
%{_bindir}/wiiuseexample-sdl

%ldconfig_scriptlets

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.15.5-10
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.15.5-1
- 0.15.5

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.15.4-4
- Rebuilt for new freeglut

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.15.4-1
- Latest upstream.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-0.8.gite7fcdf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-0.7.gite7fcdf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.0-0.6.gite7fcdf8
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-0.5.gite7fcdf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-0.4.gite7fcdf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-0.3.gite7fcdf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-0.2.gite7fcdf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.15.0-0.1.gite7fcdf8
- Update to latest snapshot because current (latest) release is totally broken

* Fri Dec 18 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.14.0-2
- Build with $RPM_OPT_FLAGS
- Ship LICENSE as %%license where available

* Mon Dec 14 2015 Jon Ciesla <limburgher@gmail.com> - 0.14.0-1
- New upstream.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 16 2014 Simo Sorce <simo@fedoraproject.org> - 0.12-12
- Add devel dependency on bluez-libs-devel
- Fixes: #1142457

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Simo Sorce <simo@fedoraproject.org> - 0.12-4
Import and first build

* Sun Jan 16 2011 Simo Sorce <simo@fedoraproject.org> - 0.12-3
Fix dependencies and summary.

* Sun Dec 12 2010 Simo Sorce <simo@fedoraproject.org> - 0.12-2
Rename to wiiuse following Fedora Packages guidelines
Fix License definition
Expand summary.

* Fri Nov 26 2010 Simo Sorce <simo@fedoraproject.org> - 0.12-1
Initial release
