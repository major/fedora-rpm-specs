%global gitdate 20230906.181324
%global cmakever 5.27.80
%global commit0 683acbbec9b3b14aeac146a4be7be20a02dae312
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20230706
%global kf6ver 5.240.0
 
Name:           ocean-sound-theme
Summary:        Ocean Sound Theme for Plasma
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}
BuildArch: noarch
 
License:        CC0-1.0 AND BSD-2-Clause AND CC-BY-SA-4.0
URL:            https://invent.kde.org/plasma/%{name}
 
%global versiondir %(echo %{version} | cut -d. -f1-2)
Source0:        https://invent.kde.org/plasma/%{name}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
 
BuildRequires:  extra-cmake-modules >= %{kf6ver}
BuildRequires:  kf6-rpm-macros >= %{kf6ver}
BuildRequires:	gcc-c++
BuildRequires:  cmake
 
Requires:       kf6-filesystem >= %{kf6ver}
 
%description
%{summary}.
 
%prep
%autosetup -n %{name}-%{commit0}
 
 
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
* Fri Sep 22 2023 Steve Cossette <farchord@gmail.com> - 5.27.80^20230706.180800.683acbb-1
- Initial build
