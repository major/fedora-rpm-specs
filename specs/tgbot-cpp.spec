Name: tgbot-cpp
Version: 1.6
Release: 6%{?dist}

Summary: C++ library for Telegram bot API
License: MIT
URL: https://github.com/reo7sp/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: openssl-devel
BuildRequires: ninja-build
BuildRequires: boost-devel
BuildRequires: curl-devel
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
C++ library for Telegram bot API.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_TESTS=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/libTgBot.so.1*

%files devel
%{_includedir}/tgbot
%{_libdir}/libTgBot.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild
