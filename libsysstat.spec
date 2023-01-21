%define __cmake_in_source_build 1

Name:		libsysstat
Version:	0.4.6
Release:	5%{?dist}
License:	GPLv2 and LGPLv2+
Summary:	Library used to query system info and statistics
Url:		http://www.lxde.org
Source0:	https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	%{?fedora:cmake >= 3.1.0}%{!?fedora:cmake3 >= 3.3}
BuildRequires: pkgconfig(Qt5Core)
#BuildRequires: pkgconfig(Qt5Help)
BuildRequires: lxqt-build-tools >= 0.6.0
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

%description
Library used to query system info and statistics

%package devel
Summary:	Devel files for libsysstat
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Sysstat libraries for development.


%prep
%autosetup


%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif

mkdir build
cd build
%cmake ..
%{cmake_build}
%if 0%{?el7}
EOF
%endif


%install
cd build
%cmake_install


%ldconfig_scriptlets


%files
%doc AUTHORS COPYING
%{_libdir}/libsysstat-qt5.so.0
%{_libdir}/libsysstat-qt5.so.0.4.6

%files devel
%dir %{_includedir}/sysstat-qt5/
%dir %{_datadir}/cmake/sysstat-qt5/
%{_includedir}/sysstat-qt5/*
%{_datadir}/cmake/sysstat-qt5/*
%{_libdir}/pkgconfig/sysstat-qt5.pc
%{_libdir}/libsysstat-qt5.so


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Zamir SUN <sztsian@gmail.com> - 0.4.6-3
- Fix cmake macro issue.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 25 2021 zsun <sztsian@gmail.com> - 0.4.6-1
- Update to 0.4.6

* Thu Aug 05 2021 Zamir SUN <sztsian@gmail.com> - 0.4.5-1
- Update to 0.4.5

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 0.4.4-1
- Update to 0.4.4

* Fri Aug 07 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-4
- Spec fixes against F33

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.4.3-1
- Update to 0.4.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Zamir SUN <sztsian@gmail.com> - 0.4.2-3
- Improve compatibility with epel7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Zamir SUN <sztsian@gmail.com>  - 0.4.2-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 04 2018 Zamir SUN <zsun@fedoraproject.org> - 0.4.1-1
- Update to version 0.4.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - 0.3.2-1
- New upstream release tied to lxqt 0.11

* Mon May 30 2016 Than Ngo <than@redhat.com> - 0.3.1-4
- cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.3.1-2
- Prepare for lxqt epel7

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.3.1-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.3.0-2
- Rebuild (gcc5)

* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.3.0-1
- New upstream version 0.3.0

* Fri Oct 24 2014 TI_Eugene <ti.eugene@gmail.com> - 0.2.0-1
- Version bump
- qt5 only

* Fri Sep 26 2014 TI_Eugene <ti.eugene@gmail.com> - 0.1.0-1
- Initial packaging
