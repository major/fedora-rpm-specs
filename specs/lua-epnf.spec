%global forgeurl https://github.com/siffiejoe/lua-luaepnf
%global tag v%{version}

Name:      lua-epnf
Version:   0.3
Release:   7%{?dist}
Summary:   Extended PEG Notation Format (easy grammars for LPeg)
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
Requires:      lua-lpeg
BuildRequires: lua-devel

#Tests
BuildRequires: lua-lpeg

%description
This Lua module provides sugar for writing grammars/parsers using
the LPeg library. It simplifies error reporting and AST building.


%prep
%forgesetup


%build
# Nothing to do here


%install
install -dD %{buildroot}%{lua_pkgdir}
install -p -m 644 src/epnf.lua %{buildroot}%{lua_pkgdir}/epnf.lua


%check
cd tests
for test in *.lua; do
  lua $test
done


%files
%license README.md
%doc doc/readme.txt
%{lua_pkgdir}/epnf.lua


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Jonny Heggheim <hegjon@gmail.com> - 0.3-1
- Initial package
