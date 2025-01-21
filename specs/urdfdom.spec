%global libversion 4.0

Name:       urdfdom
Version:    4.0.0
Release:    4%{?dist}
Summary:    U-Robot Description Format Document Object Model

License:    BSD-3-Clause
URL:        http://ros.org/wiki/urdf
Source0:    https://github.com/ros/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  console-bridge-devel
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  tinyxml2-devel
BuildRequires:  urdfdom-headers-static

%description
The URDF (U-Robot Description Format) library
provides core data structures and a simple XML parser
for populating the class data structures from an URDF file

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   tinyxml2-devel
Requires:   urdfdom-headers-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_bindir}/urdf_mem_test


%files
%license LICENSE
%{_bindir}/*
%{_libdir}/*.so.%{libversion}
%{_datadir}/%{name}

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}
%{_includedir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 4.0.0-3
- rebuild for tinyxml2

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 02 2024 Rich Mattes <richmattes@gmail.com> - 4.0.0-1
- Update to release 4.0.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Rich Mattes <richmattes@gmail.com> - 1.0.4-1
- Update to release 1.0.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-2
- Rebuilt for Boost 1.69

* Fri Nov 23 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.0.0-1
- Update to release 1.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.4.2-7
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.4.2-4
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 0.4.2-3
- Rebuilt for Boost 1.64

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 0.4.2-2
- Rebuilt for Boost 1.63

* Sun Jul 17 2016 Rich Mattes <richmattes@gmail.com> - 0.4.2-1
- Update to release 0.4.2

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 0.3.0-12
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.3.0-11
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.3.0-9
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.0-7
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 0.3.0-6
- Rebuild for boost 1.57.0

* Sat Aug 23 2014 Rich Mattes <richmattes@gmail.com> - 0.3.0-5
- Rebuild for console-bridge

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.3.0-2
- rebuild for boost 1.55.0

* Wed Apr 16 2014 Rich Mattes <richmattes@gmail.com> - 0.3.0-1
- Update to release 0.3.0

* Sun Feb 09 2014 Rich Mattes <richmattes@gmail.com> - 0.2.9-2
- Rebuild for console-bridge 0.2.5

* Sat Oct 19 2013 Rich Mattes <richmattes@gmail.com> - 0.2.9-1
- Update to release 0.2.9
- Remove upstreamed patches

* Wed Aug 21 2013 Rich Mattes <richmattes@gmail.com> - 0.2.8-2
- Backport upstream SONAME patch
- Add ldconfig post and postun

* Mon Aug 19 2013 Rich Mattes <richmattes@gmail.com> - 0.2.8-1
- Update to release 0.2.8
- Change upstream to github

* Tue Mar 12 2013 Rich Mattes <richmattes@gmail.com> - 0.2.7-1
- Update to release 0.2.7

* Tue Oct 16 2012 Rich Mattes <richmattes@gmail.com> - 0.2.3-1
- Initial package
