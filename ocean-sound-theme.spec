Name:           ocean-sound-theme
Summary:        Ocean Sound Theme for Plasma
Version: 5.92.0
Release: 1%{?dist}
BuildArch: noarch

License:        CC0-1.0 AND BSD-2-Clause AND CC-BY-SA-4.0
URL:            https://invent.kde.org/plasma/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  cmake

Requires:       kf6-filesystem

%description
%{summary}.

%prep
%autosetup


%build
%{cmake_kf6}
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt 
%{_datadir}/sounds/ocean/
 
%changelog
* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.92.0-1
- 5.92.0

* Thu Dec 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.91.0-1
- 5.91.0

* Sun Dec 03 2023 Justin Zobel <justin.zobel@gmail.com> - 5.90.0-1
- Update to 5.90.0

* Fri Nov 10 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- 5.27.80

* Fri Sep 22 2023 Steve Cossette <farchord@gmail.com> - 5.27.80^20230706.180800.683acbb-1
- Initial build
