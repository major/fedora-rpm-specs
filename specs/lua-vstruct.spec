%global forgeurl https://github.com/ToxicFrog/vstruct
%global tag v%{version}

Name:      lua-vstruct
Version:   2.1.1
Release:   7%{?dist}
Summary:   Lua library to manipulate binary data
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
BuildRequires: lua-devel

%description
%{summary}.

%prep
%forgesetup

%build
# Nothing to do here

%install
install -dD %{buildroot}%{lua_pkgdir}/vstruct

install -p -m 644 api.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 ast.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 compat1x.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 cursor.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 frexp.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 init.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 io.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 lexer.lua %{buildroot}%{lua_pkgdir}/vstruct/
cp -av ast/ %{buildroot}%{lua_pkgdir}/vstruct/
cp -av io/ %{buildroot}%{lua_pkgdir}/vstruct/

%check
# Fails due to package.path magic in the test file depends on
# the parent folder name
# lua test.lua

LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua" \
lua -e 'local vstruct = require "vstruct"
print(vstruct._VERSION)'

%files
%license COPYING
%doc README.md
%doc CHANGES
%{lua_pkgdir}/vstruct/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Jonny Heggheim <hegjon@gmail.com> - 2.1.1-1
- Initial package
