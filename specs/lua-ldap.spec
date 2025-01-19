# fallback for EPEL
%{!?lua_version: %global lua_version %{lua: print(string.sub(_VERSION, 5))}}
%{!?lua_libdir: %global lua_libdir %{_libdir}/lua/%{lua_version}}
Name:           lua-ldap
Version:        1.3.1
Release:        7%{?dist}
Summary:        LDAP client library for Lua, using OpenLDAP
License:        MIT
URL:            https://lualdap.github.io/lualdap/
Source0:        https://github.com/lualdap/lualdap/archive/v%{version}/lualdap-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua-devel >= %{lua_version}
BuildRequires:  openldap-devel
BuildRequires:  lua >= %{lua_version}
%if 0%{?rhel} && 0%{?rhel} < 9
Requires:       lua(abi) = %{lua_version}
%endif
%if 0%{?rhel} == 7
BuildRequires:  lua-rpm-macros
%endif

%description
LuaLDAP is a simple interface from Lua to an LDAP client. It enables a Lua 
program to:
* Connect to an LDAP server;
* Execute any operation (search, add, compare, delete, modify and rename);
* Retrieve entries and references of the search result.

%prep
%setup -q -n lualdap-%{version}
sed -i -e 's/-DLUA_USE_C89//' -e 's/-std=c89//' Makefile

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags} -fPIC" LUA_LIBDIR=%{_libdir} LUA_INCDIR=%{_includedir}

%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   local lualdap = require("lualdap"); print("Hello from "..lualdap._VERSION.."!");'

%install
%make_install INST_LIBDIR=%{lua_libdir}

%files
%doc README.md docs/[cmn]*.md
%license docs/license.md
%{lua_libdir}/lualdap.so*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 09 2023 Christian Krause <chkr@fedoraproject.org> - 1.3.1-3
- Disable C89 support to match the lua runtime (required on i686)

* Thu Aug 03 2023 Christian Krause <chkr@fedoraproject.org> - 1.3.1-2
- Cleanup spec file according to review comments

* Sun Jun 25 2023 Christian Krause <chkr@fedoraproject.org> - 1.3.1-1
- Unretire lua-ldap (#2217273)
- Cleanup spec file
- Update to latest upstream
- Remove obsolete patches

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.0-17
- fix for lua 5.4

* Tue Jun 30 2020 Björn Esser <besser82@fedoraproject.org> - 1.1.0-16
- Rebuilt for Lua 5.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Tom Callaway <spot@fedoraproject.org> - 1.1.0-5
- update for lua 5.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 13 2014 Dan Callaghan <dcallagh@redhat.com> - 1.1.0-3
- fix perms on lualdap.c and lualdap.so

* Mon Jun 30 2014 Dan Callaghan <dcallagh@redhat.com> - 1.1.0-2
- cp -p, run tests in %%check

* Thu Jun 05 2014 Dan Callaghan <dcallagh@redhat.com> - 1.1.0-1
- initial version
