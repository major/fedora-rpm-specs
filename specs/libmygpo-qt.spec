
# TODO: upstream qt4 support is deprecated, conditionalize qt4 support
# in hopes of removing in soonish
%global qt4 1

Name:    libmygpo-qt
Summary: Qt4 Library that wraps the gpodder.net Web API
Version: 1.1.0
Release: 19%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
#Url:     http://wiki.gpodder.org/wiki/Libmygpo-qt
URL:     https://github.com/gpodder/libmygpo-qt/
Source0: https://github.com/gpodder/libmygpo-qt/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: cmake
BuildRequires: doxygen

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Network)

%if 0%{?qt4}
BuildRequires: automoc4
BuildRequires: pkgconfig(QJson)
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtNetwork)
BuildRequires: pkgconfig(QtTest)
%endif

%description
libmygpo-qt is a Qt4 Library that wraps the gpodder.net Web API,
http://wiki.gpodder.org/wiki/Web_Services/API_2
 
%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package -n libmygpo-qt5
Summary: Qt5 Library that wraps the gpodder.net Web API
%description -n libmygpo-qt5
libmygpo-qt5 is a Qt5 Library that wraps the gpodder.net Web API,
http://wiki.gpodder.org/wiki/Web_Services/API_2

%package -n libmygpo-qt5-devel
Summary: Development files for libmygpo-qt5
Requires: libmygpo-qt5%{?_isa} = %{version}-%{release}
%description -n libmygpo-qt5-devel
%{summary}.

 
%prep
%autosetup -p1


%build
%if 0%{?qt4}
%global _vpath_builddir %{_target_platform}
%cmake .. \
  -DBUILD_WITH_QT4:BOOL=ON \
  -DINCLUDE_INSTALL_DIR:PATH=%{_qt4_headerdir}/mygpo-qt \
  -DLIB_INSTALL_DIR:PATH=%{_qt4_libdir}/mygpo-qt

%cmake_build
%endif

%global _vpath_builddir %{_target_platform}-qt5
%cmake .. \
  -DBUILD_WITH_QT4:BOOL=OFF \
  -DINCLUDE_INSTALL_DIR:PATH=%{_qt5_headerdir}/mygpo-qt \
  -DLIB_INSTALL_DIR:PATH=%{_qt5_libdir}/mygpo-qt

%cmake_build


%install
%if 0%{?qt4}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%endif

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5


%check
%if 0%{?qt4}
export PKG_CONFIG_PATH=%{buildroot}%{_qt4_libdir}/pkgconfig
test "$(pkg-config --modversion libmygpo-qt)" = "%{version}"
export CTEST_OUTPUT_ON_FAILURE=1
# test 2 currently fails on i686, poke upstream -- rex
make test -C %{_target_platform} ||:
%endif
export PKG_CONFIG_PATH=%{buildroot}%{_qt5_libdir}/pkgconfig
test "$(pkg-config --modversion libmygpo-qt5)" = "%{version}"
export CTEST_OUTPUT_ON_FAILURE=1
# test 2 currently fails on i686, poke upstream -- rex
make test -C %{_target_platform}-qt5 ||:

 
%if 0%{?qt4}
%ldconfig_scriptlets

%files
%doc AUTHORS LICENSE README 
%{_qt4_libdir}/libmygpo-qt.so.1*
 
%files devel
%{_qt4_headerdir}/mygpo-qt/
%{_qt4_libdir}/libmygpo-qt.so
%{_qt4_libdir}/pkgconfig/libmygpo-qt.pc
%{_qt4_libdir}/cmake/mygpo-qt/
%endif

%ldconfig_scriptlets -n libmygpo-qt5

%files -n libmygpo-qt5
%doc AUTHORS LICENSE README
%{_qt5_libdir}/libmygpo-qt5.so.1*

%files -n libmygpo-qt5-devel
%{_qt5_headerdir}/mygpo-qt/
%{_qt5_libdir}/libmygpo-qt5.so
%{_qt5_libdir}/pkgconfig/libmygpo-qt5.pc
%{_qt5_libdir}/cmake/mygpo-qt5/

 
%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.0-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Than Ngo <than@redhat.com> - 1.1.0-7
- Fixed FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-1
- 1.1.0
- use %%make_build %%ldconfig_scriptlets
- make qt5 unconditional
- conditionalize qt4 support (which is deprecated upstream)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.8-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Oct 09 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.8-2
- qt5-devel: fix typo in base pkg dependency

* Wed Oct 01 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.8-1
- 1.0.8
- include path for cmake and chkconfig are wrong for libmygpo-qt (#1148246)
- use github-hosted sources
- Qt5 support: libmygpo-qt5,libmy-qt5-devel subpkgs

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 13 2013 Rex Dieter <rdieter@fedoraproject.org> 1.0.7-1
- 1.0.7

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.6-3
- rebuild (qjson)

* Fri Nov 23 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.6-2
- rebuild (qjson)

* Sat Oct 13 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.6-1
- 1.0.6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.5-1
- 1.0.5

* Wed Sep 14 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.4-1
- 1.0.4

* Mon May 23 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-1
- 1.0.3

* Fri May 20 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.2-2
- drop kde deps/macros, this is a qt-only library

* Tue May 10 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.2-1
- 1.0.2 first try


