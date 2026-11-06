Name:           kio-gopher
Version:        2.0.0
Release:        1%{?dist}
Summary:        Gopher KIO Slave for KDE apps

License:        CC0-1.0 AND GPL-2.0-or-later
URL:            https://invent.kde.org/network/kio-gopher
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt6Core)

BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang gopher --with-html --all-name

%files -f gopher.lang
%license LICENSES/*
%doc ChangeLog README
%{_kf6_qtplugindir}/kf6/kio/gopher.so

%changelog
* Sat Apr 18 2026 Steve Cossette <farchord@gmail.com> - 2.0.0-1
- Initial Release
