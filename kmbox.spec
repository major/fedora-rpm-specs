Name:    kmbox
Version: 24.01.85
Release: 1%{?dist}
Summary: The KMbox Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(KF6Codecs)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6Mime)
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

%files
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6Mbox.so.*

%files devel
%{_includedir}/KPim6/KMbox
%{_kf6_libdir}/cmake/KPim6Mbox/
%{_kf6_libdir}/libKPim6Mbox.so


%changelog
* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Fri Dec 8 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
