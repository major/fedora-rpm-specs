Name:    akonadi-search
Version: 24.12.1
Release: 2%{?dist}
Summary: The Akonadi Search library and indexing agent

# Rust crate licensing:
# MIT
# MIT OR Apache-2.0
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND (MIT OR Apache-2.0) AND MIT
URL:     https://invent.kde.org/frameworks/%{name}

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  xapian-core-devel
BuildRequires:  corrosion
BuildRequires:  rust
BuildRequires:  cargo

Obsoletes:      kf5-akonadi-search < 24.01.80-1

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KPim6Akonadi)
Requires:       cmake(KPim6AkonadiMime)
Requires:       cmake(KF6Contacts)
Requires:       cmake(KPim6Mime)
Requires:       cmake(KF6CalendarCore)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%generate_buildrequires
cd agent/rs/htmlparser
%cargo_generate_buildrequires
cd ../../..

%prep
%autosetup -n %{name}-%{version} -p1
%cargo_prep

# Delete the Cargo.lock (So it doesn't fail building)
find -name "Cargo.lock" -print -delete

%build
cd agent/rs/htmlparser
%cargo_license_summary
%cargo_license
cd ../../..
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/akonadi_html_to_text
%{_kf6_bindir}/akonadi_indexing_agent
%{_kf6_datadir}/akonadi/agents/akonadiindexingagent.desktop
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6AkonadiSearchCore.so.*
%{_kf6_libdir}/libKPim6AkonadiSearchDebug.so.*
%{_kf6_libdir}/libKPim6AkonadiSearchPIM.so.*
%{_kf6_libdir}/libKPim6AkonadiSearchXapian.so.*
%{_kf6_plugindir}/krunner/kcms/kcm_krunner_pimcontacts.so
%{_kf6_plugindir}/krunner/krunner_pimcontacts.so
%{_kf6_qtplugindir}/pim6/akonadi/

%files devel
%{_includedir}/KPim6/AkonadiSearch/
%{_kf6_libdir}/cmake/KPim6AkonadiSearch/
%{_kf6_libdir}/libKPim6AkonadiSearchCore.so
%{_kf6_libdir}/libKPim6AkonadiSearchDebug.so
%{_kf6_libdir}/libKPim6AkonadiSearchPIM.so
%{_kf6_libdir}/libKPim6AkonadiSearchXapian.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Sat Mar 09 2024 Marie Loise Nolden <loise@kde.org> - 24.02.0-2
- add missing BuildArch: noarch to -doc package

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90
- Add doc package for KF6 API

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Sat Dec 16 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-2
- Obsoletes the old plasma5 package

* Sat Dec 9 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
