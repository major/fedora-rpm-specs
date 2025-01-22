Name:		libsysstat
Version:	1.1.0
Release:	2%{?dist}
License:	GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:	Library used to query system info and statistics
Url:		http://www.lxde.org
Source0:	https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  lxqt-build-tools >= 0.6.0

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
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS COPYING
%{_libdir}/libsysstat-qt6.so.1
%{_libdir}/libsysstat-qt6.so.%{version}

%files devel
%dir %{_includedir}/sysstat-qt6/
%dir %{_datadir}/cmake/sysstat-qt6/
%{_includedir}/sysstat-qt6/*
%{_datadir}/cmake/sysstat-qt6/*
%{_libdir}/pkgconfig/sysstat-qt6.pc
%{_libdir}/libsysstat-qt6.so


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Steve Cossette <farchord@gmail.com> - 1.1.0-1
- 1.1.0

* Wed Apr 17 2024 Steve Cossette <farchord@gmail.com> - 1.0.0-1
- 1.0.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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
