Name: tgbot-cpp
Version: 1.3
Release: 3%{?dist}

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
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 09 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3-1
- Updated to version 1.3.

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.2.1-5
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.1-1
- Updated to version 1.2.1.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2-1
- Updated to version 1.2.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-1
- Initial SPEC release.
