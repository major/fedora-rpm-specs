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
Release:        %autorelease

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

%check
lua %{SOURCE2}

%files
%doc README.md
%{lua_libdir}/mpack.so

%files -n lua5.1-mpack
%{lua_compat_libdir}/mpack.so

%changelog
%autochangelog
