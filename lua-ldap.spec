%if 0%{?fedora} >= 22
%global luaver 5.4
%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}
%global compatbuilddir %{_builddir}/lua51-%{name}-%{version}-%{release}
%else
%if 0%{?fedora} >= 20 || 0%{?rhel} > 7
%global luaver 5.2
%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}
%global compatbuilddir %{_builddir}/lua51-%{name}-%{version}-%{release}
%else
%global luaver 5.1
%endif
%endif

%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-ldap
Version:        1.1.0
Release:        21%{?dist}
Summary:        LDAP client library for Lua, using OpenLDAP
License:        MIT
URL:            http://www.keplerproject.org/lualdap/
Source0:        http://files.luaforge.net/releases/lualdap/lualdap/LuaLDAP%{version}/lualdap-%{version}.tar.gz
# obey DESTDIR in the Makefile
Patch0:         destdir.patch
# fixes for Lua 5.2 compatibility
Patch1:         lua52.patch
# https://github.com/luaforge/lualdap/commit/0d2e40bb182d8e417a5dac9000e5a5bb17422adf
Patch2:         fix-attempt-to-concatenate-a-nil-value.patch
# fix tests for Lua 5.2, make them runnable in the build
# https://github.com/luaforge/lualdap/pull/2
Patch3:         0001-update-test.lua-for-5.2.patch
Patch4:         0002-script-to-run-test.lua-against-a-dummy-slapd.patch
# Fixup for Lua 5.4
Patch5:         lualdap-1.1.0-lua54.patch
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
Requires:       lua(abi) = %{luaver}
%else
Requires:       lua >= %{luaver}
%endif
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  openldap-devel
# for tests
BuildRequires:  lua
BuildRequires:  openldap-servers

%description
LuaLDAP is a simple interface from Lua to an LDAP client. It enables a Lua 
program to:
* Connect to an LDAP server;
* Execute any operation (search, add, compare, delete, modify and rename);
* Retrieve entries and references of the search result.

%if "%{?luacompatver}"
%package compat
Summary:        LDAP client library for Lua 5.1, using OpenLDAP
BuildRequires:  compat-lua-devel >= %{luacompatver}
BuildRequires: make
Requires:       lua(abi) = %{luacompatver}

%description compat
LuaLDAP is a simple interface from Lua to an LDAP client. It enables a Lua 5.1 
program to:
* Connect to an LDAP server;
* Execute any operation (search, add, compare, delete, modify and rename);
* Retrieve entries and references of the search result.
%endif

%prep
%setup -q -n lualdap-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p2
%patch5 -p1
chmod a+x tests/run-tests.sh
# LUA_VERSION_NUM is defined in lua.h, it shouldn't be set in config
echo "LUA_VERSION_NUM = " >>config
%if "%{?luacompatver}"
rm -rf %{compatbuilddir}
cp -a . %{compatbuilddir}
%endif

echo "CFLAGS = $RPM_OPT_FLAGS -fPIC -I%{_includedir} -DLDAP_DEPRECATED" >>config
echo "LUA_LIBDIR = %{lualibdir}" >>config

%if "%{?luacompatver}"
echo "CFLAGS = $RPM_OPT_FLAGS -fPIC -I%{_includedir}/lua-%{luacompatver} -DLDAP_DEPRECATED" >>%{compatbuilddir}/config
echo "LUA_LIBDIR = %{luacompatlibdir}" >>%{compatbuilddir}/config
%endif

%build
make %{?_smp_mflags}

%if "%{?luacompatver}"
pushd %{compatbuilddir}
make %{?_smp_mflags}
popd
%endif

%check
make check

%install
make install DESTDIR=%{buildroot}

%if "%{?luacompatver}"
pushd %{compatbuilddir}
make install DESTDIR=%{buildroot}
popd
%endif

%files
%doc README doc/
%{lualibdir}/lualdap.so*

%if "%{?luacompatver}"
%files compat
%doc README doc/
%{luacompatlibdir}/lualdap.so*
%endif

%changelog
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
