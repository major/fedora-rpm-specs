
# uncomment to enable bootstrap mode
#global bootstrap 1

%if ! 0%{?bootstrap}
#global docs 1
%global tests 1
%endif

Name:    libalkimia
Summary: Financial library
Version: 8.2.1
Release: 2%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://kmymoney.org/
Source0: https://download.kde.org/stable/alkimia/%{version}/alkimia-%{version}.tar.xz

## upstream patches
# https://invent.kde.org/office/alkimia/-/commit/089794942385e4d3fc02e028eab2039bbcaab508
Patch0: alkimia-8.2.1-install-financequote.patch

## upstreamable patches
# https://invent.kde.org/office/alkimia/-/merge_requests/61
Patch100: alkimia-8.2.1-install-python.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkg-config
# KF6
BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(Plasma)
# Qt6
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Test)
%ifarch %{qt6_qtwebengine_arches}
%global webengine 1
BuildRequires: cmake(Qt6WebEngineWidgets)
%endif

# While upstream prefers MPIR over GMP (“MPIR is preferred over GMP” in
# CMakeLists.txt), MPIR is no longer maintained upstream
# (https://groups.google.com/g/mpir-devel/c/qTOaOBuS2E4?hl=en), so we
# unconditionally use GMP instead.
BuildRequires: pkgconfig(gmp)

# financequote.pl
BuildRequires: perl-generators

# gdb.py
BuildRequires: python3-devel

# %%check
%if 0%{?tests}
BuildRequires: xwayland-run
BuildRequires: libEGL
%endif

%if 0%{?docs}
BuildRequires: doxygen
%endif

%description
%{summary}

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gmp-devel
%description devel
%{summary}.

%package        qt6
Summary:        Accounts framework Qt6 bindings
Obsoletes:      %{name}-qt5 < 8.2.1
# financequote.pl
Recommends:     perl(Date::Manip)
Recommends:     perl(Finance::Quote)
Recommends:     perl(LWP)
Recommends:     perl(XML::Parser)
Recommends:     perl(XML::Writer)
%description    qt6
%{summary}.

%package        qt6-devel
Summary:        Development files for %{name}-qt6
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
Requires:       gmp-devel
%if 0%{?webengine}
Requires:       cmake(Qt6WebEngineWidgets)
%endif
Obsoletes:      %{name}-qt5-devel < 8.2.1
%description    qt6-devel
%{summary}.

%package        doc
Summary:        API Documentation for %{name}
BuildArch:      noarch
%description    doc
%{summary}.


%prep
%autosetup -n alkimia-%{version} -p1


%build
%cmake_kf6 \
  %{!?plasma:-DBUILD_APPLETS:BOOL=OFF} \
  -DBUILD_WITH_QT6=ON \
  -DBUILD_WITH_WEBENGINE:BOOL=%{?webengine:ON}%{!?webengine:OFF} \
  -DBUILD_WITH_WEBKIT:BOOL=OFF \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
  -DENABLE_FINANCEQUOTE:BOOL=ON

%cmake_build

## docs
%if 0%{?docs}
# auto-update doxygen configuration
doxygen -u %{_target_platform}-qt6/src/libalkimia.doxygen
make libalkimia_apidoc -C %{_target_platform}-qt6
%endif

%install
%cmake_install

%if 0%{?docs}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a %{_target_platform}-qt6/src/apidocs/html/ %{buildroot}%{_pkgdocdir}/
%endif

## unpackaged files
%if ! 0%{?plasma}
rm -fv  %{buildroot}%{_kf6_datadir}/locale/*/LC_MESSAGES/plasma*
%endif

# Perform byte compilation manually on paths outside the usual locations
%py_byte_compile %{python3} %{buildroot}%{_datadir}/gdb

%find_lang %{name} --all-name


%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libalkimia6)" = "%{version}"
%if 0%{?tests}
# some tests require online access, not available in mock builds
# alkonlinequotestest requires a JS-enabled browser backend
%global __ctest xwfb-run -- %{__ctest}
time \
%ctest -E '(download|newstuff|web)engine%{!?webengine:|onlinequotes}'
%endif


%files qt6 -f %{name}.lang
%doc README.md
%license COPYING*
%{_kf6_bindir}/onlinequoteseditor6
%{_kf6_libdir}/libalkimia6.so.8{,.*}
%{_kf6_qmldir}/org/kde/alkimia6/
%{_kf6_datadir}/alkimia6/
%{_kf6_datadir}/applications/org.kde.onlinequoteseditor6.desktop
%{_kf6_datadir}/icons/*/*/apps/onlinequoteseditor6.*
%{_kf6_datadir}/knsrcfiles/*-quotes.knsrc
%{_kf6_metainfodir}/org.kde.onlinequoteseditor6.appdata.xml

%files qt6-devel
%dir %{_includedir}/alkimia/
%{_includedir}/alkimia/Qt6/
%{_kf6_libdir}/libalkimia6.so
%{_kf6_libdir}/pkgconfig/libalkimia6.pc
%{_kf6_libdir}/cmake/LibAlkimia6-*/
%{_kf6_datadir}/gdb/

%if 0%{?docs}
%files doc
%dir %{_pkgdocdir}/
%doc %{_pkgdocdir}/html
%endif


%changelog
* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 8.2.1-2
- Rebuilt for Python 3.14.0rc3 bytecode

* Tue Aug 05 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 8.2.1-1
- 8.2.1
- Build for Qt6

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 8.1.2-2
- convert license to SPDX

* Fri Jul 19 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 8.1.2-1
- 8.1.2
- Use QtWebEngine on applicable arches
- Add financequote dependencies

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 02 2022 Rex Dieter <rdieter@fedoraproject.org> - 8.0.3-8
- drop deprecations (qt4), use modern cmake macros
- disable docs (temporary, workaround FTBFS issues)

* Wed Feb 02 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 8.0.3-8
- Use gmp unconditionally, since mpir is unmaintained upstream

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 8.0.3-4
- FTBFS, adjust to new cmake macros (#1863974)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 8.0.3-1
- 8.0.3

* Mon May 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 8.0.2-3
- -doc: drop dep on main pkg (#1833984)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Rex Dieter <rdieter@fedoraproject.org> - 8.0.2-1
- 8.0.2
- drop qt4 support f31+

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 7.0.2-1
- 7.0.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 31 2018 Rex Dieter <rdieter@fedoraproject.org> - 7.0.1-4
- pull in upstream(ed) patches

* Thu Mar 29 2018 Rex Dieter <rdieter@fedoraproject.org> - 7.0.1-3
- -qt4: make kde4 kmymoney buildable again
- -qt4: use gmp unconditionally (as previous alkimia v5 used gmp)

* Mon Mar 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 7.0.1-2
- -devel: Requires: (gmp,mpir)-devel

* Sun Mar 18 2018 Rex Dieter <rdieter@fedoraproject.org> -  7.0.1-1
- 7.0.1
- -qt5 support

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-1
- libalkimia-5.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.3.2-7
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.3.2-1
- 4.3.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 02 2011 Rex Dieter <rdieter@fedoraproject.org> 4.3.1-4
- rebuild (gmp)

* Mon Aug 22 2011 Rex Dieter <rdieter@fedoraproject.org> 4.3.1-3
- .spec cosmetics

* Sat Aug 20 2011 Rex Dieter <rdieter@fedoraproject.org> 4.3.1-2
- BR: gmp-devel
- %%check : don't ignore errors

* Sat Aug 06 2011 Rex Dieter <rdieter@fedoraproject.org> 4.3.1-1
- 4.3.1

* Tue Jun 21 2011 Rex Dieter <rdieter@fedoraproject.org> 4.3.0-1
- first try


