%global _hardened_build 1

Name:           freeDiameter
Version:        1.5.0
Release:        6%{?dist}
Summary:        A Diameter protocol open implementation

License:        BSD
URL:            http://www.freediameter.net/
Source0:        http://www.freediameter.net/hg/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  libidn-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  lksctp-tools-devel

%description
freeDiameter is an open source Diameter protocol implementation. It provides 
an extensible platform for deploying a Diameter network for your 
Authentication, Authorization and Accounting needs.

%package devel
Summary:        Library for freeDiameter package
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the shared library
for %{name} package.

%prep
%autosetup

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DDISABLE_SCTP=ON . -Wno-dev
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc doc
%{_bindir}/freeDiameterd
%{_bindir}/%{name}d-%{version}
%{_libdir}/libfdcore.so.6
%{_libdir}/libfdproto.so.6
%{_libdir}/libfdcore.so.%{version}
%{_libdir}/libfdproto.so.%{version}

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}/
%{_libdir}/libfdcore.so
%{_libdir}/libfdproto.so

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Filipe Rosset <rosset.filipe@gmail.com> - 1.5.0-1
- Update to 1.5.0 fixes rhbz#1861989 - CVE-2020-6098

* Mon Aug 24 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.4.0-4
- Fix FTBFS rhbz#1863579

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 05 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.4.0-1
- Update to 1.4.0 fixes rhbz#1596273 and rhbz#1799370

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.0-13
- Spec cleanup / modernization

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 31 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.0-6
- spec cleanup

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Tomáš Mráz <tmraz@redhat.com> - 1.2.0-3
- Rebuild for new libgcrypt

* Thu Feb 20 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.0-2
- new upstream version 1.2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 1.1.6-1
- new upstream version 1.1.6

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec  7 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 1.1.5-1
- Updated to new upstream 1.1.5

* Sat Sep 29 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 1.1.4-1
- Updated to 1.1.4

* Sat Aug 25 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 1.1.3-1
- Updated to 1.1.3.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 16 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 1.1.2-1
- Updated to 1.1.2.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 29 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 1.1.1-1
- Updated to 1.1.1.

* Mon Jun 06 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 1.1.0-1
- Updated to 1.1.0.

* Mon Dec 27 2010 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 1.0.3-1
- Initial package.

