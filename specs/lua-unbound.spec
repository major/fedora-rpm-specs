Summary:        Binding to libunbound for Lua
Name:           lua-unbound
Version:        1.0.0
Release:        10%{?dist}
License:        MIT
URL:            https://www.zash.se/luaunbound.html
Source0:        https://code.zash.se/dl/luaunbound/luaunbound-%{version}.tar.gz
Source1:        https://code.zash.se/dl/luaunbound/luaunbound-%{version}.tar.gz.asc
Source2:        gpgkey-3E52119EF853C59678DBBF6BADED9A77B67AD329.gpg
Requires:       lua(abi) = %{lua_version}
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua >= %{lua_version}
BuildRequires:  lua-devel >= %{lua_version}
BuildRequires:  unbound-devel

%description
Lua bindings for the Unbound APIs.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n luaunbound-%{version}

%build
%make_build \
  LUA_VERSION=%{lua_version} \
  MYCFLAGS="$RPM_OPT_FLAGS" \
  MYLDFLAGS="$RPM_LD_FLAGS" \
  LD=%{__cc}

%install
%make_install LUA_LIBDIR=%{lua_libdir}

# Correct strange upstream file permission
chmod 755 %{buildroot}%{lua_libdir}/lunbound.so

%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   local lunbound = require("lunbound");
   print("Hello from "..lunbound._LIBVER.."!");'

%files
%license LICENSE
%doc README.markdown
%{lua_libdir}/lunbound.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Robert Scheck <robert@fedoraproject.org> 1.0.0-1
- Upgrade to 1.0.0 (#1982222)

* Sun Jan 10 2021 Robert Scheck <robert@fedoraproject.org> 0.5-1
- Upgrade to 0.5 (#1914678)
- Initial spec file for Fedora and Red Hat Enterprise Linux
