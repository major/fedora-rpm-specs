%global lua_version 5.4
%global lua_libdir %{_libdir}/lua/%{lua_version}
%global lua_pkgdir %{_datadir}/lua/%{lua_version}

%global lua_compat_version 5.1
%global lua_compat_libdir %{_libdir}/lua/%{lua_compat_version}
%global lua_compat_pkgdir %{_datadir}/lua/%{lua_compat_version}
%global lua_compat_builddir %{_builddir}/compat-lua-%{name}-%{version}-%{release}

%global libmpack_version 1.0.5

BuildRequires:  libtool
BuildRequires:  lua >= %{lua_version}
BuildRequires:  lua-devel >= %{lua_version}

Name:           lua-mpack
Version:        1.0.12
Release:        2%{?dist}

License:        MIT
Summary:        Implementation of MessagePack for Lua
Url:            https://github.com/libmpack/libmpack-lua

Requires:       lua(abi) = %{lua_version}

Source0:        https://github.com/libmpack/libmpack-lua/archive/%{version}/libmpack-lua-%{version}.tar.gz
Source1:        https://github.com/libmpack/libmpack/archive/%{libmpack_version}/libmpack-%{libmpack_version}.tar.gz
Source2:        test_mpack.lua

%description
mpack is a small binary serialization/RPC library that implements
both the msgpack and msgpack-rpc specifications.

%package -n lua5.1-mpack
Summary:        Implementation of MessagePack for Lua %{lua_compat_version}
BuildRequires:  compat-lua >= %{lua_compat_version}
BuildRequires:  compat-lua-devel >= %{lua_compat_version}
BuildRequires: make
Requires:       lua(abi) = %{lua_compat_version}
Obsoletes:      compat-%{name} < %{version}
Provides:       compat-%{name} = %{version}

%description -n lua5.1-mpack
mpack is a small binary serialization/RPC library that implements
both the msgpack and msgpack-rpc specifications for Lua %{lua_compat_version}.

%prep
%autosetup -p1 -n libmpack-lua-%{version}

mkdir mpack-src
pushd mpack-src
tar xfz %{SOURCE1} --strip-components=1
popd

# hack to export flags
echo '#!/bin/sh' > ./configure
chmod +x ./configure

rm -rf %{lua_compat_builddir}
cp -a . %{lua_compat_builddir}

%build

%configure
make %{?_smp_mflags} \
     USE_SYSTEM_MPACK=no \
     USE_SYSTEM_LUA=yes \
     MPACK_LUA_VERSION=%{lua_version}.x \
     LUA_INCLUDE="$(pkg-config --cflags lua)"

pushd %{lua_compat_builddir}
%configure
make %{?_smp_mflags} \
     USE_SYSTEM_MPACK=no \
     USE_SYSTEM_LUA=yes \
     MPACK_LUA_VERSION=%{lua_compat_version}.x \
     LUA_INCLUDE="$(pkg-config --cflags lua-%{lua_compat_version})"
popd

%install
make \
     USE_SYSTEM_MPACK=no \
     USE_SYSTEM_LUA=yes \
     LUA_CMOD_INSTALLDIR=%{lua_libdir} \
     DESTDIR=%{buildroot} \
     install

pushd %{lua_compat_builddir}
make \
     USE_SYSTEM_MPACK=no \
     USE_SYSTEM_LUA=yes \
     LUA_CMOD_INSTALLDIR=%{lua_compat_libdir} \
     DESTDIR=%{buildroot} \
     install
popd

# This segfaults on i686 platforms
# https://github.com/libmpack/libmpack-lua/issues/14
%ifarch x86_64 ppc64lc aarch64 s390x
%check
lua %{SOURCE2}
%endif

%files
%doc README.md
%{lua_libdir}/mpack.so

%files -n lua5.1-mpack
%{lua_compat_libdir}/mpack.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 30 2024 Michel Lind <salimma@fedoraproject.org> - 1.0.12-1
- Update to version 1.0.12; Fixes: RHBZ#2263242

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 20 2023 Andreas Schneider <asn@redhat.com> - 1.0.11-1
- Update to version 1.0.11
- resolves: rhbz#2243078

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 18 2023 Andreas Schneider <asn@redhat.com> - 1.0.10-1
- resolves: rhbz#2179479 - Update to version 1.0.10

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Andreas Schneider <asn@redhat.com> - 1.0.9-1
- Update to version 1.0.8

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.8-4
- Rebuilt for Lua 5.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Andreas Schneider <asn@redhat.com> - 1.0.8-1
- Update to version 1.0.8
- Changed name of compat-lua to lua-5.1

* Mon Mar 11 2019 Andreas Schneider <asn@redhat.com> - 1.0.7-6
- Fix build issue with assert()

* Tue Mar 05 2019 Aron Griffis <aron@scampersand.com> - 1.0.7-5
- Add compat 5.1 build for neovim

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Andreas Schneider <asn@redhat.com> - 1.0.7-1
- Update to version 1.0.7
- Fix Building on 32bit platforms

* Wed Nov 08 2017 Andreas Schneider <asn@redhat.com> - 1.0.6-5
- Add a simple test for mpack

* Wed Nov 08 2017 Andreas Schneider <asn@redhat.com> - 1.0.6-4
- Update patch to compile with newer lua versions

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 08 2017 Andreas Schneider <asn@redhat.com> - 1.0.6-1
- Update to 1.0.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Andreas Schneider <asn@redhat.com> - 1.0.4-1
- resolves: #1417325 - Update to version 1.0.4

* Fri Nov 25 2016 Andreas Schneider <asn@redhat.com> - 1.0.3-5
- Add requirement on ABI version and do not package lua directory

* Thu Nov 24 2016 Andreas Schneider <asn@redhat.com> - 1.0.3-4
- Add the license correctly in the files section

* Tue Nov 15 2016 Andreas Schneider <asn@redhat.com> - 1.0.3-3
- Create a configure script so we export all flags

* Tue Nov 15 2016 Andreas Schneider <asn@redhat.com> - 1.0.3-2
- Removed Group:
- Removed BuildRoot:

* Mon Nov 14 2016 Andreas Schneider <asn@redhat.com> - 1.0.3-1
- Initial version 1.0.3
