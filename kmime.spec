Name:    kmime
Version: 24.01.85
Release: 1%{?dist}
Summary: The KMime Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# https://invent.kde.org/pim/kmime/-/merge_requests/54
Patch0:  move-translations.patch

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kcodecs-devel

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libkmime5.po -execdir mv {} libkmime6.po \;


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/%{name}.*
%{_kf6_libdir}/libKPim6Mime.so.*

%files devel
%{_includedir}/KPim6/KMime/
%{_kf6_libdir}/libKPim6Mime.so
%{_kf6_libdir}/cmake/KPim6Mime/

%changelog
* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-2
- Backport rename translation files

* Tue Dec 5 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
