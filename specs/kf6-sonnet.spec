%global		framework sonnet

Name:		kf6-%{framework}
Version:	6.10.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 solution for spell checking
License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:		https://invent.kde.org/frameworks/%{framework}

Source0:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
# patch out default excluded file list to have it empty
# https://bugs.kde.org/show_bug.cgi?id=482376
Patch0:		sonnet6-default-list.patch

BuildRequires:	appstream
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtdeclarative-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	zlib-devel
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(aspell)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	hspell-devel
BuildRequires:	pkgconfig(libvoikko)


Requires:	kf6-filesystem
Recommends:	%{name}-hunspell

%description
KDE Frameworks 6 Tier 1 solution for spell checking.


%package	aspell
Summary:	aspell plugin for %{name}
Requires:	%{name} = %{version}-%{release}
%description	aspell
The %{name}-aspell package contains the aspell spellchecking
plugin for %{name}.

%package	hunspell
Summary:	hunspell plugin for %{name}
Requires:	%{name} = %{version}-%{release}
%description	hunspell
The %{name}-hunspell package contains the hunspell spellchecking
plugin for %{name}.

%package	hspell
Summary:	hspell plugin for %{name}
Supplements:	(%{name} and langpacks-he)
Requires:	%{name} = %{version}-%{release}
Requires:	hunspell-he

%description	hspell
The %{name}-hspell package contains the Hebrew hspell spellchecking
plugin for %{name}.

%package	voikko
Summary:	voikko plugin for %{name}
Supplements:	(%{name} and langpacks-fi)
Requires:	%{name} = %{version}-%{release}
%description	voikko
The %{name}-voikko package contains the Finnish voikko spellchecking
plugin for %{name}.


%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
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
%find_lang_kf6 sonnet6_qt

%files -f sonnet6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6SonnetCore.so.*
%{_kf6_bindir}/parsetrigrams6
%{_kf6_qmldir}/org/kde/sonnet/
%{_kf6_libdir}/libKF6SonnetUi.so.*

%files aspell
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_aspell.so

%files hunspell
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_hunspell.so

%files hspell
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_hspell.so

%files voikko
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_voikko.so


%files devel
%doc README.md
%license LICENSES/*.txt
%{_kf6_includedir}/Sonnet/
%{_kf6_includedir}/SonnetCore/
%{_kf6_includedir}/SonnetUi/
%{_kf6_libdir}/cmake/KF6Sonnet/
%{_kf6_libdir}/libKF6SonnetCore.so
%{_kf6_libdir}/libKF6SonnetUi.so
%{_kf6_qtplugindir}/designer/sonnet6widgets.so
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

* Mon Mar 4 2024 Marie Loise Nolden <loise@kde.org> - 6.0.0-3
- patch out default exclude list with KDE names, it can't be resetted

* Thu Feb 29 2024 Marie Loise Nolden <loise@kde.org> - 6.0.0-2
- add aspell, hspell, voikko (finnish)
- make spellchecking engine plugins separate packages as they link
  to the library of that engine
- recommend hunspell plugin as a default install

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

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

* Sun Sep 24 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230920.235103.01f7019-1
- Initial release
