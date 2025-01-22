%global date          20210115
%global commit0       3bdb0b13e5ceb6b686f4e7f9424179b5bcb71ab8
%global shortcommit0  %(c=%{commit0}; echo ${c:0:7})
%global the_owner     srdgame

Name:           librs232
Version:        1.0.4
Release:        15.%{date}git%{shortcommit0}%{?dist}
Summary:        Library for serial communications over RS-232 with Lua bindings
License:        MIT
Url:            https://github.com/%{the_owner}/%{name}/
Source:         https://github.com/%{the_owner}/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{date}git%{shortcommit0}.tar.gz
# Fix FTBFS on gcc 13:
# Upstrem reference: https://patch-diff.githubusercontent.com/raw/srdgame/librs232/pull/10.patch
Patch0:         https://patch-diff.githubusercontent.com/raw/%{the_owner}/%{name}/pull/10.patch#/%{name}-%{version}-Fix-rs232_set_-prototypes-mismatch.patch


BuildRequires:  /usr/bin/git
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  lua >= 5.1
BuildRequires:  lua-devel >= 5.1
BuildRequires:  make


%description
%{name} is a multi-platform library that provides support for communicating
over serial ports (e.g. RS-232). It also provides Lua bindings.


%package devel
Summary: Development files for %{name}
License: MIT
Requires: %{name}%{?_isa} = %{version}-%{release}


%description devel
The %{name}-devel package contains C header files for developing
applications that use %{name} library.


%package -n lua-%{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Lua bindings for %{name}
License: MIT
Requires: lua(abi) = %{lua_version}


%description -n lua-%{name}
The lua-%{name} package provides Lua binding for %{name} library.
It allows Lua programs to communicate over serial ports.


%prep
%autosetup -S git -n %{name}-%{commit0}
export LUA_INCLUDE=

%build
./autogen.sh
%configure --disable-static

%make_build


%install
%make_install
# Remove unneeded .la files
find %{buildroot} -name '*.la' -exec rm {} \;


%files
%license COPYING
%doc AUTHORS doc/example.lua
%{_libdir}/*.so.*


%ldconfig_scriptlets


%files devel
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}*.pc


%files -n lua-%{name}
%{lua_libdir}/*.so


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-15.20210115git3bdb0b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-14.20210115git3bdb0b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-13.20210115git3bdb0b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-12.20210115git3bdb0b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-11.20210115git3bdb0b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.4-10.20210115git3bdb0b1
- Add missing patch to repository

* Tue Jan 24 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.4-9.20210115git3bdb0b1
- Remove patch upstream merged
- Add patch to fix FTBFS on gcc 13 (f38)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8.20191120gitc106c94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7.20191120gitc106c94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6.20191120gitc106c94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5.20191120gitc106c94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4.20191120gitc106c94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3.20191120gitc106c94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.4-2.20191120gitc106c94
- Upload new-sources

* Tue Jun 30 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.4-1.20191120gitc106c94
- Drop patch upstream merged
- Update to the latest available version
- Add patch to support lua >=5.4 (#rhbz 1852144)

* Tue Jun 30 2020 Björn Esser <besser82@fedoraproject.org> - 1.0.3-11.20190917git1c29a27
- Rebuilt for Lua 5.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10.20190917git1c29a27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.3-9.20190917git1c29a27
- Drop patch upstream merged
- Update to the latest available version
- Add patch to fix compilation error

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7.20171229git21ecc3c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6.20171229git21ecc3c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5.20171229git21ecc3c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4.20171229git21ecc3c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.3-3.20171229git21ecc3c
- Drop patch upstream merged
- Configure warning patch added

* Thu Dec 21 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.3-2.20171219gitc0a3c75
- Drop patch upstream merged

* Tue Sep 26 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.3-1.20160327git4de45dd
- Initial RPM release.
