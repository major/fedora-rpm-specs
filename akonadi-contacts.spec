Name:    akonadi-contacts
Version: 24.01.80
Release: 2%{?dist}
Summary: The Akonadi Contacts Library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Prison)

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextUtils)

BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6GrantleeTheme)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6IconThemes)

Obsoletes:      kf5-akonadi-contacts < 24.01.80-1

%description
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  cmake(KPim6Akonadi)
Requires:  cmake(KF6Contacts)
Requires:  cmake(KPim6GrantleeTheme)
Recommends:  cmake(KF6CalendarCore)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%{_kf6_datadir}/akonadi/plugins/serializer/
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6AkonadiContactCore.so.*
%{_kf6_libdir}/libKPim6AkonadiContactWidgets.so.*
%{_kf6_qtplugindir}/akonadi_serializer_*.so
%{_datadir}/kf6/akonadi/contact/data/zone.tab
%{_datadir}/kf6/akonadi/contact/pics/world.jpg

%files devel
%{_includedir}/KPim6/AkonadiContactCore/
%{_includedir}/KPim6/AkonadiContactWidgets/
%{_kf6_libdir}/cmake/KPim6AkonadiContactCore/
%{_kf6_libdir}/cmake/KPim6AkonadiContactWidgets/
%{_kf6_libdir}/libKPim6AkonadiContactCore.so
%{_kf6_libdir}/libKPim6AkonadiContactWidgets.so

%changelog
* Sat Dec 16 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-2
- Obsoletes the old version

* Sat Dec 9 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
