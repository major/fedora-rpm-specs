%global forgeurl https://github.com/luarocks/argparse
%global tag %{version}
%global extractdir argparse-412e6aca393e365f92c0315dfe50181b193f1ace
%global archivename lua-argparse-%{version}

Name:           lua-argparse
Version:        0.7.1
Release:        5%{?dist}
Summary:        Feature-rich command line parser for Lua

License:        MIT
URL:            %{forgeurl}

%forgemeta
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  lua-devel

%description
Argparse is a feature-rich command line parser for Lua inspired by argparse
for Python.

Argparse supports positional arguments, options, flags, optional arguments,
subcommands and more. Argparse automatically generates usage, help and error
messages.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
Requires:       python3-sphinx_rtd_theme

%description    doc
This package contains documentation for %{name}.

%prep
%forgesetup

%build
sphinx-build-3 -b html docsrc doc

%install
install -m 644 -D -p src/argparse.lua %{buildroot}%{lua_pkgdir}/argparse.lua

%check
# Smoke test for now
LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua" \
lua -e 'local argparse = require "argparse"
local parser = argparse()
assert(#parser == 0)'

%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{lua_pkgdir}/argparse.lua

%files doc
%license LICENSE
%doc doc/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 18 2023 Jonny Heggheim <hegjon@gmail.com> - 0.7.1-1
- Updated to version 0.7.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Tom Callaway <spot@fedoraproject.org> - 0.6.0-1
- update to 0.6.0
- rebuild for lua 5.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Hard-coded Lua version to address build issues

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 9 2015 Jeff Backus <jeff.backus@gmail.com> - 0.5.0-1
- Updated to latest version / address bug #1289954

* Thu Sep 10 2015 Jeff Backus <jeff.backus@gmail.com> - 0.4.1-2
- Fixed build issue on EPEL

* Tue Aug 4 2015 Jeff Backus <jeff.backus@gmail.com> - 0.4.1-1
- Updated to latest version
- Removed extraneous patch

* Tue Aug 4 2015 Jeff Backus <jeff.backus@gmail.com> - 0.4.0-3
- Changed license handling to more readable form
- Modified to rebuild sphinx documentation and remove fonts
- Added patch to put license at head of argparse.lua

* Mon Jul 27 2015 Jeff Backus <jeff.backus@gmail.com> - 0.4.0-2
- Fixed permissions on argparse.lua
- Added proper handling of license for EPEL6
- Removed commented-out macros

* Wed Jul 22 2015 Jeff Backus <jeff.backus@gmail.com> - 0.4.0-1
- Initial release
