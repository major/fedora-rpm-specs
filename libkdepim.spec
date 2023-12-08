Name:    libkdepim
Version: 24.01.80
Release: 1%{?dist}
Summary: Library for common kdepim apps

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)

BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


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
%{_kf6_libdir}/libKPim6Libkdepim.so.5*
%{_kf6_libdir}/libKPim6Libkdepim.so.6*

%files devel
%{_includedir}/KPim6/Libkdepim/
%{_kf6_libdir}/cmake/KPim6Libkdepim/
%{_kf6_libdir}/cmake/KPim6MailTransportDBusService/
%{_kf6_libdir}/libKPim6Libkdepim.so
%{_kf6_datadir}/dbus-1/interfaces/org.kde.addressbook.service.xml
%{_kf6_datadir}/dbus-1/interfaces/org.kde.mailtransport.service.xml
%{_kf6_qtplugindir}/designer/kdepim6widgets.so


%changelog
* Wed Dec 6 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
