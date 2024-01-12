Name:    libkleo
Version: 24.01.85
Release: 2%{?dist}
Summary: KDE PIM cryptographic library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later WITH GCC-exception-3.1
URL:     https://invent.kde.org/frameworks/%{name}/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


BuildRequires:  boost-devel

BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  gpgmepp-devel >= 1.7.1
BuildRequires:  cmake(QGpgmeQt6)
# workaround gpgmepp-devel missing Requires: libassuan-devel for now
BuildRequires:  libassuan-devel
# kf6
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)

# gpg support ui
Recommends:     pinentry-gui

Obsoletes:      kf5-libkleo < 24.01.80

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# INTERFACE_LINK_LIBRARIES "QGpgme;Gpgmepp"
Requires:       cmake(Gpgmepp)
Requires:       cmake(QGpgme)
Requires:       cmake(QGpgmeQt6)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

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
%{_kf6_sysconfdir}/xdg/libkleopatrarc
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6Libkleo.so.*
%{_kf6_datadir}/libkleopatra/

%files devel
%{_kf6_libdir}/libKPim6Libkleo.so
%{_kf6_libdir}/cmake/KPim6Libkleo/
%{_includedir}/KPim6/Libkleo/
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 24.01.85-2
- add doc package for KF6 API

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Wed Dec 20 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-2
- Obsolete kf5-libkleo

* Wed Dec 6 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
