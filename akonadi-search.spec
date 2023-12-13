Name:    akonadi-search
Version: 24.01.80
Release: 1%{?dist}
Summary: The Akonadi Search library and indexing agent

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL
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

%changelog
* Sat Dec 9 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
