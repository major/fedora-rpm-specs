%global app_id org.kde.kexi

# koffice version to Obsolete
%global koffice_ver 3:2.3.70

%bcond_with bootstrap

%if %{without bootstrap}
# some known failures, ping upstream
%global tests 1
%endif

Name:    kexi
Summary: An integrated environment for managing data
Version: 3.2.0
Release: 13%{?dist}
License: LGPL-2.0-or-later AND GFDL-1.2-or-later
Url:     https://kexi-project.org/
Source0: https://download.kde.org/%{stable_kf5}/%{name}/src/%{name}-%{version}.tar.xz

## upstream patches (lookaside cache)
Patch8: 0008-cmake-find-PostgreSQL-12.patch
Patch13: 0013-Fix-build-with-Qt-5.13.patch
Patch31: 0031-add-override-where-needed.patch
Patch36: 0036-TRIVIAL-Move-Q_REQUIRED_RESULT-to-correct-place.patch
Patch50: 0050-cmake-find-PostgreSQL-13.patch
Patch80: 0080-cmake-find-PostgreSQL-14.patch
Patch504: 0504-Fix-glib-include-position.patch
Patch543: 0543-Fix-build-with-GCC-12-standard-attributes-in-middle-.patch

BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Qml)

BuildRequires: cmake(Qt5UiTools)
#BuildRequires: cmake(Qt5WebKit)
#BuildRequires: cmake(Qt5WebKitWidgets)

BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5TextEditor)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)

BuildRequires: cmake(KF5DocTools)
#BuildRequires: doxygen

BuildRequires: breeze-icon-theme-rcc
# needed at runtime too, apparently -- rex
Requires: breeze-icon-theme-rcc

# kdb/kproperty/kreport and kexi are all tied together
BuildRequires: cmake(KDb) >= %{version}
BuildRequires: cmake(KPropertyWidgets) >= %{version}
BuildRequires: cmake(KReport) >= %{version}

Requires: kdb%{?_isa} >= %{version}
Requires: kproperty%{?_isa} >= %{version}
Requires: kreport%{?_isa} >= %{version}

## mapbrowser currently disabled in sources
#BuildRequires: cmake(Marble)

## DB engines
BuildRequires: glib2-devel
BuildRequires: mariadb-connector-c-devel
# this shouldn't be needed, but the build system configuration seems to
# mistakenly detect server-related headers
BuildRequires: postgresql-server-devel

%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

Obsoletes: koffice-kexi < %{koffice_ver}
Obsoletes: koffice-kexi-libs < %{koffice_ver}

Obsoletes: calligra-kexi < 3.0.0
Provides:  calligra-kexi = %{version}-%{release}

Obsoletes: calligra-kexi-map-form-widget < 3.0.0
#Provides:  calligra-kexi-map-form-widget = %{version}-%{release}

%description
Kexi is an integrated data management application.  It can be used for
creating database schemas, inserting data, performing queries, and
processing data. Forms can be created to provide a custom interface to
your data. All database objects – tables, queries and forms – are
stored in the database, making it easy to share data and design.

For additional database drivers take a look at kexi-driver-*

%package  libs
Summary:  Runtime libraries for %{name}
Obsoletes: calligra-kexi-libs < 3.0.0
Provides:  calligra-kexi-libs = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package spreadsheet-import
Summary: Spreadsheet-to-Kexi-table import plugin
Obsoletes: calligra-kexi-spreadsheet-import < 3.0.0
Provides:  calligra-kexi-spreadsheet-import = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%description spreadsheet-import
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{?!tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html

## versioning silliness
# compat symlink
ln -s kexi-%{majmin_ver_kf5} %{buildroot}%{_bindir}/kexi
# rename appdata/.desktop
mv %{buildroot}%{_metainfodir}/%{app_id}-%{majmin_ver_kf5}.appdata.xml \
   %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml
mv %{buildroot}%{_datadir}/applications/%{app_id}-%{majmin_ver_kf5}.desktop \
   %{buildroot}%{_datadir}/applications/%{app_id}.desktop


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
## tests have known failures, TODO: consult upstream
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
#xvfb-run -a \
%make_build ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif


%files -f %{name}.lang
%license COPYING.LIB COPYING.DOC
%doc AUTHORS README.md
%{_bindir}/kexi
%{_bindir}/kexi-%{majmin_ver_kf5}
%{_metainfodir}/%{app_id}.appdata.xml
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/kexi/
%{_datadir}/icons/hicolor/*/*/kexi-%{majmin_ver_kf5}.*

%ldconfig_scriptlets libs

%files libs
%license COPYING.LIB
%{_libdir}/libkexi*
%{_libdir}/libkformdesigner*
%{_qt5_plugindir}/kexi/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 3.2.0-12
- Disable webbrowser support
- Use KF5 macros

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Ondřej Sloup <osloup@redhat.com> - 3.2.0-6
- Rebuild for new PostgreSQL 15 

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 3.2.0-3
- Fix FTBFS (#1987621)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 18 2021 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Than Ngo <than@redhat.com> - 3.1.0-7
- Fixed FTBFS

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-3
- upstream buildfix (#1604485)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.94-1
- 3.0.94
- undo some of the versioning/parallel-install silliness

* Fri Oct 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-3
- Requires: breeze-icon-theme-rcc (#1492881)

* Fri Aug 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-2
- typo in kreport dependency

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-1
- 3.0.2, bump kdb dep

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1.1-1
- 3.0.1.1 (fix translations)

* Wed Jun 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-2
- License: GPLv2+
- BR: breeze-icon-theme-rcc
- appdata/desktop file validation

* Wed Apr 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-1
- first try
