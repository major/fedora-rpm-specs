# Commit corresponding to release 2.14.1
%global commit c9dc01f16be159a809d73ea54c8f6cf31a735812
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           cppmyth
Version:        2.17.4
Release:        3%{?dist}
Summary:        Client interface for the MythTV backend

License:        GPL-2.0-or-later
URL:            https://github.com/janbar/%{name}/
Source0:        %{url}/archive/%{shortcommit}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)

%description
This project is intended to create a easy client interface for the MythTV
backend. Its development started from January 2014 and today the API supports
the protocol version of MythTV 0.26 to 0.29.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit}


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build


%install
%cmake_install


%files
%doc README
%{_libdir}/*.so.*


%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 10 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.17.4-1
- Update to 2.17.4

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 24 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.15.1-1
- Update to 2.15.1
- Switch license tag to SPDX

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 05 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.14.7-1
- Update to 2.14.7

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.14.1-1
- Update to 2.14.1

* Thu Aug 06 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.13.0-5
- Use new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.13.0-1
- Update to 2.13.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.12.1-1
- Update to 2.12.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 24 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.9.4-1
- Update to 2.9.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 01 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.1.10-3
- Do not treat AArch64 (__ARM_ARCH = 8) as ARM (from upstream) - rhbz#1217098
-
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.10-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr 08 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.1.10-1
- Update to 1.1.10

* Tue Dec 30 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.1.0.2-2
- Fix License tag
- Fix misspelling in Description

* Wed Dec 24 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.1.0.2-1
- Initial RPM release
