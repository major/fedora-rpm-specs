%global __cmake_in_source_build 1
Name: Box2D
Version:  2.4.2
Release:  2%{?dist}
Summary: A 2D Physics Engine for Games

License: Zlib
URL: http://box2d.org/
Source0: https://github.com/erincatto/box2d/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake
BuildRequires: make

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description
Box2D is an open source C++ engine for simulating rigid bodies in 2D. 
Box2D is developed by Erin Catto and has the zlib license. 
While the zlib license does not require acknowledgement, 
we encourage you to give credit to Box2D in your product. 

%description devel
Box2D is an open source C++ engine for simulating rigid bodies in 2D. 
Box2D is developed by Erin Catto and has the zlib license. 
While the zlib license does not require acknowledgement, 
we encourage you to give credit to Box2D in your product. 

These are the development files.

%prep
%setup -qn box2d-%{version}
rm -r extern

%build
%cmake -DBOX2D_INSTALL=ON -DBOX2D_BUILD_SHARED=ON -DBOX2D_BUILD_TESTBED=OFF -DBOX2D_BUILD_UNIT_TESTS=OFF .
%cmake_build

%install
%make_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/*.so.2*

%files devel
%doc README.md docs/
%{_libdir}/*.so
%{_includedir}/box2d
%{_libdir}/cmake/box2d/*.cmake

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.4.2-1
- 2.4.2

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.4.1-10
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 17 2021 Caolán McNamara <caolanm@redhat.com> - 2.4.1-5
- disable building BOX2D_BUILD_UNIT_TESTS due to "SIGSTKSZ ... no
  longer constant on Linux ... redefined to sysconf(_SC_SIGSTKSZ)"
  https://github.com/bminor/glibc/blob/master/NEWS causing build failure

* Wed Feb 17 2021 Caolán McNamara <caolanm@redhat.com> - 2.4.1-4
- reduce unnecessary dependencies

* Wed Feb 10 2021 Timm Bäder <tbaeder@redhat.com> - 2.4.1-3
- Use make macros

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.4.1-1
- 2.4.1

* Mon Aug 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.4.0-1
- 2.4.0 with patch for cmake shared libs.

* Tue Aug 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.3.1-15
- Fix FTBFS.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 20 2015 Lubomir Rintel <lkundrak@v3.sk> - 2.3.1-1
- Update

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 06 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.1-3
- Review fixes from BZ 844090 comment 6.

* Thu Aug 02 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.1-2
- Unbundle freeglut and glui.

* Sat Jul 28 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.1-1
- create.
