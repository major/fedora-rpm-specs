Name:    telepathy-logger-qt
Version: 17.09.0
Release: 9%{?dist}
Summary: Telepathy Logging for Qt 5

License: LGPLv2+
URL:     https://cgit.kde.org/%{name}.git

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{name}/%{versiondir}/src/%{name}-%{version}.tar.xz

BuildRequires: bison
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: flex
BuildRequires: python3
BuildRequires: python3-dbus
BuildRequires: python3-devel
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(telepathy-logger-0.2)
BuildRequires: pkgconfig(TelepathyQt5)
BuildRequires: pkgconfig(libxml-2.0)

%description
%{summary}

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# for parent include dir ownership (mostly)
Requires: telepathy-logger-devel%{?_isa}
%description devel
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%{cmake} \
  -DPYTHON_EXECUTABLE:PATH=%{__python3}

%cmake_build

%install
%cmake_install


%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING
%{_libdir}/libtelepathy-logger-qt.so.5*
%{_libdir}/libtelepathy-logger-qt.so.0.9*

%files devel
%{_includedir}/TelepathyLoggerQt/
%{_libdir}/libtelepathy-logger-qt.so
%{_libdir}/cmake/TelepathyLoggerQt/


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 17.09.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 17.09.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 17.09.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 17.09.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 17.09.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Than Ngo <than@redhat.com> - 17.09.0-4
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.09.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.09.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Rex Dieter <rdieter@fedoraproject.org> - 17.09.0-1
- 19.09.0

* Tue Feb 18 2020 Than Ngo <than@redhat.com> - 17.08.0-9
- support Python3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.08.0-5
- %%build: -DPYTHON_EXECUTABLE:PATH=%%{__python2} (#1606505)
- use %%make_build %%ldconfig_scriptlets

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 17.08.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.0-1
- 17.08.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.04.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.04.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.04.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.04.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.04.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Daniel Vrátil <dvratil@redhat.com> - 15.04.0-1
- Update to 15.04.0 (Qt 5 release)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Jan Grulich <jgrulich@redhat.com> - 0.8.0-1
- 0.8.0

* Mon May 20 2013 Jan Grulich <jgrulich@redhat.com> - 0.6.2-1
- 0.6.2 (set version according to KTp)

* Wed Apr 17 2013 Jan Grulich <jgrulich@redhat.com> - 0.6.1-1
- 0.6.1

* Tue Apr 02 2013 Jan Grulich <jgrulich@redhat.com> - 0.6.0-1
- 0.6.0

* Thu Mar 07 2013 Rex Dieter <rdieter@fedoraproject.org> - 0.5.80-1
- 0.5.80

* Sun Feb 17 2013 Jan Grulich <jgrulich@redhat.com> - 0.5.3-1
- 0.5.3

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Jan Grulich <jgrulich@redhat.com> 0.5.2-1
- 0.5.2

* Wed Oct 31 2012 Rex Dieter <rdieter@fedoraproject.org> 0.5.1-2
- rebuild (telepathy-logger)

* Fri Oct 05 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.5.1-1
- 0.5.1

* Mon Aug 27 2012 Rex Dieter <rdieter@fedoraproject.org> 0.5.0-1
- 0.5.0

* Sat Jul 28 2012 Jan Grulich <jgrulich@redhat.com> - 0.4.1-2
- Fix libraries in %%files

* Thu Jul 26 2012 Jan Grulich <jgrulich@redhat.com> - 0.4.1-1
- 0.4.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-2
- QtGLib pkgconfig patch

* Mon Jun 11 2012 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-1
- first try

