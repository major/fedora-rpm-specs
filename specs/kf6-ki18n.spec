%global		framework ki18n

Name:		kf6-%{framework}
Version:	6.10.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon for localization
License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND ODbl-1.0
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	gettext
BuildRequires:	kf6-rpm-macros
BuildRequires:	perl-interpreter
BuildRequires:	python3
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtdeclarative-devel
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	pkgconfig(iso-codes)

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon for localization.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	gettext
Requires:	python3
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6I18n.so.6
%{_kf6_libdir}/libKF6I18n.so.%{version}
%{_kf6_libdir}/libKF6I18nQml.so.6
%{_kf6_libdir}/libKF6I18nQml.so.%{version}
%{_kf6_libdir}/libKF6I18nLocaleData.so.6
%{_kf6_libdir}/libKF6I18nLocaleData.so.%{version}
%{_kf6_datadir}/qlogging-categories6/*%{framework}*
%{_kf6_qmldir}/org/kde/i18n/localeData/
%{_kf6_qtplugindir}/kf6/ktranscript.so
%lang(ca) %{_datadir}/locale/ca/LC_SCRIPTS/ki18n6/
%lang(ca@valencia) %{_datadir}/locale/ca@valencia/LC_SCRIPTS/ki18n6/
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/ki18n6/
%lang(gd) %{_datadir}/locale/gd/LC_SCRIPTS/ki18n6/
%lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS/ki18n6/
%lang(ko) %{_datadir}/locale/ko/LC_SCRIPTS/ki18n6/
%lang(ru) %{_datadir}/locale/ru/LC_SCRIPTS/ki18n6/
%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS/ki18n6/
%lang(nb) %{_datadir}/locale/nb/LC_SCRIPTS/ki18n6/
%lang(nn) %{_datadir}/locale/nn/LC_SCRIPTS/ki18n6/
%lang(sr@ijekavian) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/ki18n6/
%lang(sr@ijekavianlatin) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n6/
%lang(sr@latin) %{_datadir}/locale/sr@latin/LC_SCRIPTS/ki18n6/
%lang(sr) %{_datadir}/locale/uk/LC_SCRIPTS/ki18n6/

%files devel
%{_kf6_includedir}/KI18n/
%{_kf6_includedir}/KI18nLocaleData/
%{_kf6_libdir}/libKF6I18n.so
%{_kf6_libdir}/libKF6I18nQml.so
%{_kf6_libdir}/libKF6I18nLocaleData.so
%{_kf6_libdir}/cmake/KF6I18n/
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Fri Jan 03 2025 Steve Cossette <farchord@gmail.com> - 6.10.0-1
- 6.10.0

* Sat Dec 14 2024 Steve Cossette <farchord@gmail.com> - 6.9.0-1
- 6.9.0

* Sat Nov 02 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.8.0-1
- 6.8.0

* Fri Oct 04 2024 Steve Cossette <farchord@gmail.com> - 6.7.0-1
- 6.7.0

* Mon Sep 16 2024 Steve Cossette <farchord@gmail.com> - 6.6.0-1
- 6.6.0

* Sat Aug 10 2024 Steve Cossette <farchord@gmail.com> - 6.5.0-1
- 6.5.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 06 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.4.0-1
- 6.4.0

* Sat Jun 01 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.0-1
- 6.3.0

* Sat May 04 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.0-1
- 6.2.0

* Wed Apr 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.0-1
- 6.1.0

* Sat Mar 09 2024 Marie Loise Nolden <loise@kde.org> - 6.0.0-2
- add missing BuildArch: noarch to -doc package

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

* Mon Feb 12 2024 Benson Muite <benson_muite@emailplus.org> - 5.249.0-2
- Fix typo in license name
- Add sonames to libraries

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.249.0-1
- 5.249.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.248.0-1
- 5.248.0

* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 5.247.0-2
- add doc package for KF6 API

* Wed Dec 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.247.0-1
- 5.247.0

* Sat Dec 02 2023 Justin Zobel <justin.zobel@gmail.com> - 5.246.0-1
- Update to 5.246.0

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230829.233059.7042d58-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233059.7042d58-2
- Rebuild for Qt Private API

* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.233059.7042d58-1
- Initial Release
