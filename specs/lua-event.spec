%global enable_docs 1

# ikiwiki is not available on EPEL
%{?rhel:%global enable_docs 0}

Summary:        Bindings of libevent to Lua
Name:           lua-event
Version:        0.4.6
Release:        16%{?dist}
License:        MIT
URL:            https://github.com/harningt/luaevent/
Source0:        https://github.com/harningt/luaevent/archive/v%{version}/luaevent-%{version}.tar.gz

# Make sure CFLAGS/LDFLAGS are respected.
Patch0:         %{name}-0.4.3-respect-cflags.patch
# Conditionalize env calls which are gone in modern lua
Patch1:         luaevent-0.4.3-envfix.patch

Requires:       lua(abi) = %{lua_version}
Requires:       lua-socket
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua >= %{lua_version}
BuildRequires:  lua-devel >= %{lua_version}
BuildRequires:  libevent-devel >= 1.4

%description
Lua bindings for libevent, an asynchronous event notification library
that provides a mechanism to execute a callback function when a specific
event occurs on a file descriptor or after a timeout has been reached.

%if 0%{?enable_docs}
%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
BuildRequires:  ikiwiki

%description doc
This package contains documentation for developing applications that
use Lua bindings for libevent, an asynchronous event notification library
that provides a mechanism to execute a callback function when a specific
event occurs on a file descriptor or after a timeout has been reached.
%endif

%prep
%setup -q -n luaevent-%{version}
%patch -P0 -p1
%patch -P1 -p1 -b .envfix
# Remove 0-byte file.
rm -f doc/modules/luaevent.mdwn

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export LDFLAGS="$RPM_LD_FLAGS -shared"
%make_build

%if 0%{?enable_docs}
/bin/sh makeDocs.sh
%endif

%install
%make_install \
  INSTALL_DIR_LUA=%{lua_pkgdir} \
  INSTALL_DIR_BIN=%{lua_libdir}

%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   dofile("test/basic.lua");'

%files
%license doc/COPYING
%doc CHANGELOG README doc/COROUTINE_MANAGEMENT doc/PLAN
%dir %{lua_libdir}/luaevent/
%{lua_libdir}/luaevent/core.so
%{lua_pkgdir}/luaevent.lua

%if 0%{?enable_docs}
%files doc
%doc html/*
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Björn Esser <besser82@fedoraproject.org> - 0.4.6-5
- Rebuilt for Lua 5.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Robert Scheck <robert@fedoraproject.org> - 0.4.6-3
- Correct GitHub source URL
- Ensure linker flag injection

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Robert Scheck <robert@fedoraproject.org> - 0.4.6-1
- Upgrade to 0.4.6

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Tom Callaway <spot@fedoraproject.org> - 0.4.3-9
- rebuild for lua 5.3
- conditionalize env calls that are no longer in modern lua

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.3-6
- fix conditional logic

* Sat Aug 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.3-5
- temporarily disable docs for f20 due as ikiwiki has dependency problems

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 0.4.3-3
- rebuild for lua 5.2

* Wed Apr 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.3-2
- amend directory ownership
- include markdown documentation
- change from %%define to %%global

* Tue Apr 16 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.3-1
- update to upstream release 0.4.3
- fix typo in %%description
- fix license tag
- make sure CFLAGS/LDFLAGS are respected
- put documentation in -doc subpackage, and only build for Fedora as ikiwiki
  is not available on EPEL

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.1-1
- initial package
