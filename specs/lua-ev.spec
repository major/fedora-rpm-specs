Summary:        Lua integration with libev
Name:           lua-ev
License:        MIT

Version:        1.5
Release:        9%{?dist}

URL:            https://github.com/brimworks/lua-ev
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libev-devel
BuildRequires:  lua-devel

%description
Event loop programming with Lua.

%prep
%autosetup -n %{name}-%{version} 

%build
%cmake -DINSTALL_CMOD=%{lua_libdir}
%cmake_build

%install
%cmake_install 
ln -s README README.copy

%check
#packaged tests do not work directly
#Use example program as a smoke test
LUA_CPATH=%{buildroot}%{lua_libdir}/?.so \
lua example.lua
LUA_CPATH=%{buildroot}%{lua_libdir}/?.so \
lua -e 'ev = require "ev"; print(ev.version())'

%files
%license README
%doc example.lua
%doc README.copy
%{lua_libdir}/ev.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Benson Muite <benson_muite@emailplus.org> - 1.5-3
- Use README as license

* Sat Nov 19 2022 Benson Muite <benson_muite@emailplus.org> - 1.5-2
- Fix install location based on review
- Add further smoke test

* Wed Nov 16 2022 Benson Muite <benson_muite@emailplus.org> - 1.5-1
- Initial release
