%global forgeurl https://github.com/starwing/luautf8
%global tag %{version}

Name:      lua-luautf8
Version:   0.1.5
Release:   6%{?dist}
Summary:   A UTF-8 support module for Lua
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildRequires: lua-devel
BuildRequires: gcc

%description
This module adds UTF-8 support to Lua.

It uses data extracted from the
[Unicode Character Database](http://www.unicode.org/reports/tr44/),
and is tested on Lua 5.2.3, Lua 5.3.0 and LuaJIT.

parseucd.lua is a pure Lua script to generate unidata.h, to support conversion
of characters and to check the category of a characters.

It is compatible with Lua's own string module, and it passes all
string and pattern matching tests in the lua test suite.

It also add some useful routines for UTF-8 features, including:
- a convenient interface to escape Unicode sequences in string.
- string insert/remove, since UTF-8 substring extract may expensive.
- calculating the Unicode width, which can be useful when implementing a
  console emulator.
- an interface to translate Unicode offset and byte offset.


%prep
%forgesetup


%build
%{__cc} %{optflags} %{?__global_ldflags} -fPIC -c -o lutf8lib.o lutf8lib.c

%{__cc} %{?__global_ldflags} -shared -o lua-utf8.so lutf8lib.o


%install
install -dD %{buildroot}%{lua_libdir}
install -p -m 755 lua-utf8.so %{buildroot}%{lua_libdir}/


%check
LUA_CPATH="%{buildroot}%{lua_libdir}/?.so" \
lua -e 'local utf8 = require "lua-utf8"; assert(4 == utf8.len("test"));'

LUA_CPATH="%{buildroot}%{lua_libdir}/?.so" \
lua test.lua

%files
%license LICENSE
%doc README.md
%{lua_libdir}/lua-utf8.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Dec 08 2022 Jonny Heggheim <hegjon@gmail.com> - 0.1.5-1
- Updated to version 0.1.5

* Wed Nov 16 2022 Jonny Heggheim <hegjon@gmail.com> - 0.1.4-1
- Initial package
