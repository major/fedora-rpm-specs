%global debug_package %{nil}

Name:           plasma-mobile-sounds
Version:        0.1
Release:        2%{?dist}
License:        CC-BY-SA and CC0 and CC-BY
Summary:        Plasma Mobile Sound Theme
Url:            https://invent.kde.org/plasma-mobile/plasma-mobile-sounds
Source:         https://download.kde.org/stable/plasma-mobile-sounds/0.1/plasma-mobile-sounds-0.1.tar.xz

BuildArch: noarch

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros

BuildRequires: pkgconfig(Qt5Core)

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%files
%{_kf5_datadir}/sounds/plasma-mobile

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 11 2022 Justin Zobel <justin@1707.io> - 0.1-1
- Initial version of package
