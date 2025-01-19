%global forgeurl https://github.com/alerque/fluent-lua
%global tag v%{version}

Name:      lua-fluent
Version:   0.2.0
Release:   6%{?dist}
Summary:   Lua implementation of Project Fluent
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
BuildRequires: lua-devel
Requires:      lua-cldr
Requires:      lua-epnf
Requires:      lua-penlight

# Tests
BuildRequires: lua-cldr
BuildRequires: lua-epnf
BuildRequires: lua-penlight

%description
A Lua implementation of Project Fluent, a localization paradigm designed to
unleash the entire expressive power of natural language translations.
Fluent is a family of localization specifications, implementations and good
practices developed by Mozilla who extracted parts of their 'l20n' solution
(used in Firefox and other apps) into a re-usable specification.


%prep
%forgesetup


%build
# Nothing to do here


%install
install -dD %{buildroot}%{lua_pkgdir}
cp -av fluent/ %{buildroot}%{lua_pkgdir}


%check
# Smoke test for now, missing dependency busted for test suite
LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua;;" \
lua -e '
local FluentBundle = require("fluent")
local bundle = FluentBundle()

bundle:add_messages([[
hello = Hello { $name }!
foo = bar
    .attr = baz
]])

print(bundle:format("foo"))
print(bundle:format("foo.attr"))
print(bundle:format("hello", { name = "World" }))
'


%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{lua_pkgdir}/fluent/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Nov 15 2022 Jonny Heggheim <hegjon@gmail.com> - 0.2.0-1
- Initial package
