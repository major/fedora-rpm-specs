Name:    libgravatar
Version: 24.01.85
Release: 1%{?dist}
Summary: Gravatar support library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)

BuildRequires:  cmake(KPim6PimCommon)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.


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
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6Gravatar.so.*

%files devel
%{_kf6_libdir}/libKPim6Gravatar.so
%{_kf6_libdir}/cmake/KPim6Gravatar/
%{_includedir}/KPim6/Gravatar/

%changelog
* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Tue Dec 12 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
