Name:    libksieve
Version: 24.01.95
Release: 1%{?dist}
Summary: Sieve support library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(KF6TextEditTextToSpeech)

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KPim6PimCommon)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6IMAP)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KF6DocTools)

Obsoletes:      kf5-libksieve < 24.01.80

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6SyntaxHighlighting)
%description    devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/knsrcfiles/ksieve_script.knsrc
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_datadir}/sieve/
%{_kf6_libdir}/libKPim6KManageSieve.so.*
%{_kf6_libdir}/libKPim6KSieve.so.*
%{_kf6_libdir}/libKPim6KSieveUi.so.*
%{_kf6_libdir}/libKPim6KSieveCore.so.*

%files devel
%{_includedir}/KPim6/KManageSieve/
%{_includedir}/KPim6/KSieve/
%{_includedir}/KPim6/KSieveCore/
%{_includedir}/KPim6/KSieveUi/
%{_kf6_libdir}/cmake/KPim6KManageSieve/
%{_kf6_libdir}/cmake/KPim6KSieve/
%{_kf6_libdir}/cmake/KPim6KSieveCore/
%{_kf6_libdir}/cmake/KPim6KSieveUi/
%{_kf6_libdir}/libKPim6KManageSieve.so
%{_kf6_libdir}/libKPim6KSieve.so
%{_kf6_libdir}/libKPim6KSieveUi.so
%{_kf6_libdir}/libKPim6KSieveCore.so
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 24.01.85-2
- add doc package for KF6 API

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Wed Dec 20 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-2
- Obsolete kf5-libksieve

* Tue Dec 12 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
