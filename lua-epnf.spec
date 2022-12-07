%global forgeurl https://github.com/siffiejoe/lua-luaepnf
%global tag v%{version}

Name:      lua-epnf
Version:   0.3
Release:   1%{?dist}
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
* Tue Nov 15 2022 Jonny Heggheim <hegjon@gmail.com> - 0.3-1
- Initial package
