# Forked from https://sourceforge.net/projects/qwt/files/qwt/5.2.3/
# This was the last, almost unannounced maintenance release of the 5.x branch,
# see: https://sourceforge.net/p/qwt/mailman/message/30128542/
# This fork contains several bugfixes and configuration file patches, to comply
# with distribution-specific system paths.

# Force out of source build
%undefine __cmake_in_source_build

%global commit0 a2b11e3f7c83dcba30a9bfac86a54ccb8305691d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate 20210522
%global owner gbm19

Name:    qwt5-qt5
Version: 5.2.3a
Release: 21.%{commitdate}git%{shortcommit0}%{?dist}
Summary: Qt Widgets for Technical Applications adapted to Qt5

License: LGPL-2.1-or-later WITH Qwt-exception-1.0
URL:     https://github.com/gbm19/qwt5-qt5
Source:  https://github.com/%{owner}/%{name}/archive/master/%{name}-master.tar.gz

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets) pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Svg) pkgconfig(Qt5Designer)

%description
The Qwt library contains GUI Components and utility classes which are primarily
useful for programs with a technical background.
Besides a 2D plot widget it provides scales, sliders, dials, compasses,
thermometers, wheels and knobs to control or display values, arrays
or ranges of type double.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains qt5 libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Extra Developer documentation for %{name}
Requires: qt5-qtbase
BuildArch: noarch

%description doc
%{summary} in HTML format.


%prep
%setup -qc -n %{name}-master

pushd %{name}-master
# avoid conflicts with qwt5-qt4 man files
for f in doc/man/man3/*.3; do mv $f ${f/%.3/.qt5.3}; done


%build
pushd %{name}-master
%cmake
%cmake_build


%install
pushd %{name}-master
%cmake_install

%ldconfig_scriptlets


%files
%license %{name}-master/COPYING
%doc %{name}-master/CHANGES
%doc %{name}-master/README
%{_qt5_libdir}/lib%{name}.so
%{?_qt5_plugindir}/designer/libqwt5_designer_plugin.so

%files devel
%{_mandir}/man3/*
%{_qt5_headerdir}/%{name}/
%{_qt5_libdir}/lib%{name}.so
%{_qt5_libdir}/pkgconfig/%{name}.pc

%files doc
%dir %{_qt5_docdir}/html/
%{_qt5_docdir}/html/%{name}/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3a-21.20210522gita2b11e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3a-20.20210522gita2b11e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3a-19.20210522gita2b11e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3a-18.20210522gita2b11e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3a-17.20210522gita2b11e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3a-16.20210522gita2b11e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.2.3a-15.20210522gita2b11e3
- Really remove the path

* Sat Jul 23 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.2.3a-14.20210522gita2b11e3
- Remove source path after cmake macro

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3a-13.20210522gita2b11e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3a-12.20210522gita2b11e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3a-11.20210522gita2b11e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.2.3a-10.20210522gita2b11e3
- Update to snapshot a2b11e3

* Fri May 07 2021 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.2.3a-9.20210114gitacd8dbb
- Update to snapshot acd8dbb
- Switch to cmake

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3a-8.20200902git0052f96
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.2.3a-7.20200902git0052f96
- Update to latest snapshot

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3a-6.20190819giteeacc44
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3a-5.20190819giteeacc44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.2.3a-4.20190819giteeacc44
- fixes based on RHBZ#1844643

* Fri Jun 05 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.2.3a-3.20190819giteeacc44
- Spec file cleanup

* Sat Feb 15 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 5.2.3a-2.20190819giteeacc44
- Minor bugfixes

* Sat Sep 15 2018 Miquel Garriga https://github.com/gbm19 - 5.2.3a-1.20180916gitd071002
- First version using Qt5
