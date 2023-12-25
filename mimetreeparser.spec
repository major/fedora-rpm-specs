Name:    mimetreeparser
Version: 24.01.85
Release: 1%{?dist}
Summary: Parser for MIME trees

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND FSFULLR AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/pim/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules

BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)

# Qt6 Missing dirs build errors
BuildRequires:  qt6-qtbase-private-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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
%license LICENSES/*
%{_kf6_libdir}/libKPim6MimeTreeParser*.so.*
%{_kf6_libdir}/qt6/mkspecs/modules/qt_MimeTreeParser*.pri
%{_kf6_qmldir}/org/kde/pim/mimetreeparser/
%{_datadir}/qlogging-categories6/mimetreeparser2.categories

%files devel
%{_kf6_libdir}/libKPim6MimeTreeParser*.so
%{_includedir}/KPim6/MimeTreeParser*/
%{_kf6_libdir}/cmake/KPim6MimeTreeParser*/


%changelog
* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Sat Dec 9 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
