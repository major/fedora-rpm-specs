%bcond_without test

%ifarch %{arm} %{ix86} x86_64 %{mips} aarch64 s390x
%bcond_without luajit
%else
%bcond_with luajit
%endif

%global lua_incdir %{_includedir}/lua-%{lua_version}
%global lua_builddir obj-lua%{lua_version}

%global lua_51_version 5.1
%global lua_51_incdir %{_includedir}/lua-%{lua_51_version}
%global lua_51_libdir %{_libdir}/lua/%{lua_51_version}
%global lua_51_pkgdir %{_datadir}/lua/%{lua_51_version}
%global lua_51_builddir obj-lua%{lua_51_version}

%global luajit_version 2.1
%global luajit_incdir %{_includedir}/luajit-%{luajit_version}
%global luajit_libdir %{_libdir}/luajit/%{luajit_version}
%global luajit_builddir obj-luajit

%global real_version 1.50.0
%global extra_version 0

%if 0%{?rhel} && 0%{?rhel} < 9
# EPEL8's cmake macros have _vpath_builddir defined
# ... but its cmake does not support -B
# see https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds
%global _vpath_builddir .
%endif

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libuv-devel >= 1.50.0
BuildRequires:  lua-devel
BuildRequires:  compat-lua >= %{lua_51_version}
BuildRequires:  compat-lua-devel >= %{lua_51_version}
%if %{with luajit}
BuildRequires:  luajit-devel
# /with luajit
%endif
BuildRequires:  lua5.1-compat53

Name:           lua-luv
Version:        %{real_version}.%{extra_version}
Release:        %autorelease

License:        Apache-2.0
Summary:        Bare libuv bindings for lua
Url:            https://github.com/luvit/luv

%if 0%{?fedora} < 33 && 0%{?rhel} < 9
Requires:       lua(abi) = %{lua_version}
%endif

Source0:        https://github.com/luvit/luv/archive/v%{real_version}-%{extra_version}/luv-%{version}.tar.gz

Patch0:         luv-module-install.patch
# Disable multicast tests as they don't work with firewalld
Patch1:         lua-luv-disable-udp-test.patch


%description
%global _description %{expand:
This library makes libuv available to lua scripts. It was made
for the luvit project but should usable from nearly any lua
project.

The library can be used by multiple threads at once. Each thread
is assumed to load the library from a different lua_State. Luv
will create a unique uv_loop_t for each state. You can't share uv
handles between states/loops.

The best docs currently are the libuv docs themselves. Hopefully
soon we'll have a copy locally tailored for lua.}

%package -n libluv
Summary:        Lua bindings for libluv as a library

%description -n libluv
%{_description}

%package -n libluv-devel
Summary:        Development files for lua-luv
Requires:       libluv%{?_isa} = %{version}-%{release}

%description -n libluv-devel
Files required for lua-luv development

%package -n lua5.1-luv
Summary:        Bare libuv bindings for lua 5.1
Requires:       lua(abi) = %{lua_51_version}

%description -n lua5.1-luv
%{_description}

%if %{with luajit}
%package -n luajit%{luajit_version}-luv
Summary:        Bare libuv bindings for lua 5.1
Requires:       lua(abi) = %{lua_51_version}

%description -n luajit%{luajit_version}-luv
%{_description}
#/ with luajit
%endif

%prep
%autosetup -n luv-%{real_version}-%{extra_version} -p1

# Remove bundled dependencies
rm -rf deps

# Remove network sensitive tests gh#luvit/luv#340
rm -f tests/test-dns.lua

%build
# lua
mkdir %{lua_builddir}
%global __cmake_builddir  %{lua_builddir}

%cmake \
    -DWITH_SHARED_LIBUV=ON \
    -DWITH_LUA_ENGINE=Lua \
    -DLUA_BUILD_TYPE=System \
    -DMODULE_INSTALL_LIB_DIR=%{lua_libdir} \
    -DLUA_INCLUDE_DIR=%{lua_incdir} \
    -DBUILD_SHARED_LIBS=OFF

%cmake_build

# lua-compat
mkdir %{lua_51_builddir}
%global __cmake_builddir %{lua_51_builddir}

%cmake \
    -DWITH_SHARED_LIBUV=ON \
    -DWITH_LUA_ENGINE=Lua \
    -DLUA_BUILD_TYPE=System \
    -DSHAREDLIBS_INSTALL_LIB_DIR=%{_libdir} \
    -DMODULE_INSTALL_LIB_DIR=%{lua_51_libdir} \
    -DLUA_COMPAT53_DIR=%{lua_51_incdir} \
    -DLUA_INCLUDE_DIR=%{lua_51_incdir} \
    -DLUA_LIBRARY=%{_libdir}/liblua-%{lua_51_version}.so \
    -DBUILD_SHARED_LIBS=ON

%cmake_build

%if %{with luajit}
# luajit
mkdir %{luajit_builddir}
%global __cmake_builddir %{luajit_builddir}

%cmake \
    -DWITH_SHARED_LIBUV=ON \
    -DWITH_LUA_ENGINE=LuaJit \
    -DLUA_BUILD_TYPE=System \
    -DMODULE_INSTALL_LIB_DIR=%{luajit_libdir} \
    -DLUA_COMPAT53_DIR=%{lua_51_incdir} \
    -DBUILD_SHARED_LIBS=OFF

%cmake_build
# /with luajit
%endif

%install
# lua
%global __cmake_builddir  %{lua_builddir}
%cmake_install

# lua-5.1
%global __cmake_builddir  %{lua_51_builddir}
%cmake_install

%if %{with luajit}
# luajit
%global __cmake_builddir  %{luajit_builddir}
%cmake_install
# /with luajit
%endif

%if %{with test}
%check
# `test normal` fails, because the handle is a file not a tty,
# see https://github.com/luvit/luv/issues/687
rm tests/test-tty.lua

# lua-5.1
ln -sf %{lua_51_builddir}/luv.so luv.so
lua-5.1 tests/run.lua
rm luv.so
# lua
ln -sf %{lua_builddir}/luv.so luv.so
lua tests/run.lua
rm luv.so

%if %{with luajit}
# luajit
ln -sf %{luajit_builddir}/luv.so luv.so
%if 0%{?el8}
%ifarch aarch64
# luajit test consistently failing with:
# ok 105 udp - udp recvmmsg
# PANIC: unprotected error in call to Lua API (bad light userdata pointer)
# /var/tmp/rpm-tmp.8I3N1v: line 45:   553 Aborted                 (core dumped) luajit tests/run.lua
rm tests/test-work.lua
%endif
%endif
luajit tests/run.lua
rm luv.so
# /with luajit
%endif

# /with test
%endif

%files -n libluv
%doc README.md
%license LICENSE.txt
%{_libdir}/libluv.so.*

%files -n libluv-devel
%{_libdir}/libluv.so
%{_libdir}/pkgconfig/*.pc

%dir %{_includedir}/luv/
%{_includedir}/luv/lhandle.h
%{_includedir}/luv/lreq.h
%{_includedir}/luv/luv.h
%{_includedir}/luv/util.h

%files
%{lua_libdir}/luv.so

%files -n lua5.1-luv
%{lua_51_libdir}/luv.so

%if %{with luajit}
%files -n luajit%{luajit_version}-luv
%{luajit_libdir}/luv.so
#/ with luajit
%endif

%changelog
%autochangelog
