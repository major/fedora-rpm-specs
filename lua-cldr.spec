%global forgeurl https://github.com/alerque/cldr-lua
%global tag v%{version}

Name:      lua-cldr
Version:   0.3.0
Release:   1%{?dist}
Summary:   Lua interface to Unicode CLDR data

# The Lua interfaces and code is MIT License
# All data provided by the Unicode Consortium is licensed under ICU License
License:   MIT AND ICU
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
Requires:      lua-penlight
BuildRequires: lua-devel

# Tests
BuildRequires: lua-penlight

%description
Unicode CLDR (Common Locale Data Repository) data and Lua interface.

%prep
%forgesetup

%build
# Nothing to do here

%install
install -dD %{buildroot}%{lua_pkgdir}
cp -av cldr/ %{buildroot}%{lua_pkgdir}

%check
# Smoke test for now, missing dependency busted for test suite
LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua;;" \
lua -e 'local CLDR = require("cldr")
print(#CLDR.locales)
assert(#CLDR.locales > 100)'


%files
%license LICENSE
%license LICENSE-Unicode
%doc README.md
%doc CHANGELOG.md
%{lua_pkgdir}/cldr/

%changelog
* Tue Dec 06 2022 Jonny Heggheim <hegjon@gmail.com> - 0.3.0-1
- Updated to version 0.3.0

* Sun Nov 13 2022 Jonny Heggheim <hegjon@gmail.com> - 0.2.0-1
- Initial package
