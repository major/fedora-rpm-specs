Name:    akonadi-notes
Version: 24.01.85
Release: 1%{?dist}
Summary: The Akonadi Notes Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# https://invent.kde.org/pim/akonadi-notes/-/merge_requests/8.patch
Patch0:         move-translations.patch

BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(Qt6Xml)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6Mime)

%description
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  cmake(KPim6Mime)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name akonadinotes5.po -execdir mv {} akonadinotes6.po \;


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_libdir}/libKPim6AkonadiNotes.so.*

%files devel
%{_includedir}/KPim6/AkonadiNotes/
%{_kf6_libdir}/cmake/KPim6AkonadiNotes/
%{_kf6_libdir}/libKPim6AkonadiNotes.so


%changelog
* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-4
- Backport rename translation files

* Tue Dec 19 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-3
- Don't obsolete kf5-akonadi-notes, this is coinstallable

* Sat Dec 16 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-2
- Obsoletes the old version

* Sat Dec 9 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
