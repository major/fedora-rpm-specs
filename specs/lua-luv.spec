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

%global real_version 1.48.0
%global extra_version 2

%if 0%{?rhel} && 0%{?rhel} < 9
# EPEL8's cmake macros have _vpath_builddir defined
# ... but its cmake does not support -B
# see https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds
%global _vpath_builddir .
%endif

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libuv-devel >= 1.44.0
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
Release:        3%{?dist}

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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 02 2024 Andreas Schneider <asn@redhat.com> - 1.48.0.2-1
- Update to version 1.48.0-2
  * https://github.com/luvit/luv/releases/tag/v1.48.0-2
- Build with luajit on s390x

* Thu Feb 22 2024 Andreas Schneider <asn@redhat.com> - 1.48.0.0-1
- Update to version 1.48.0-0
  * https://github.com/luvit/luv/releases/tag/v1.48.0-0

* Thu Jan 25 2024 Andreas Schneider <asn@redhat.com> - 1.47.0.0-4
- Update patches to upstream version

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.47.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.47.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Andreas Schneider <asn@redhat.com> - 1.47.0.0-1
- Update to version 1.47.0-0
  * https://github.com/luvit/luv/releases/tag/1.47.0-0
 
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 06 2023 Andreas Schneider <asn@redhat.com> - 1.44.2.1-3
- resolves: #2212583 - Create a common libluv and libluv-devel package

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 09 2022 Andreas Schneider <asn@redhat.com> - 1.44.2.1-1
- Update to version 1.44.2.1
  * https://github.com/luvit/luv/releases/tag/1.44.2-1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.43.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 16 2022 Andreas Schneider <asn@redhat.com> - 1.43.0.0-1
- Update to version 1.43.0.0
  * https://github.com/luvit/luv/releases/tag/1.43.0-0

* Fri Mar 11 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.42.0.1-3
- Adjust for cmake 3.23.0, where -S (passed by %%cmake) overrides the positional argument
- Disable UDP multicast tests unconditionally, seems flaky
- Disable luajit threadpool tests on EPEL 8 aarch64

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Andreas Schneider <asn@redhat.com> - 1.42.0.0-1
- Update to version 1.42.0.1
  * https://github.com/luvit/luv/releases/tag/1.42.0-1
  * https://github.com/luvit/luv/releases/tag/1.42.0-0
- Do not build luajit on s390x and ppc64

* Fri Jul 23 2021 Andreas Schneider <asn@redhat.com> - 1.41.1.0-3
- Build a luajit2.1 flavor

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.41.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Andreas Schneider <asn@redhat.com> - 1.41.1.0-1
- Update to version 1.41.1
  * https://github.com/luvit/luv/releases/tag/1.41.1-0

* Mon Jul 12 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.41.0.0-3
- use macros from lua-{s,}rpm-macros; spec now portable across Lua versions
- reenable s390x build on epel8 (#1829151)

* Sat Jul 03 2021 Andreas Schneider <asn@redhat.com> - 1.41.0.0-2
- Fixed tests with lua >= 5.4.3

* Mon Apr 19 2021 Andreas Schneider <asn@redhat.com> - 1.41.0.0-1
- Update to version 1.41.0
  * https://github.com/luvit/luv/releases/tag/1.41.0-0
  * https://github.com/luvit/luv/releases/tag/1.40.0-0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Tom Callaway <spot@fedoraproject.org> - 1.36.0.0-3
- fix for lua 5.4
- adjust logic for new cmake weirdness (f33+)

* Tue Jun 30 2020 Björn Esser <besser82@fedoraproject.org> - 1.36.0.0-2
- Rebuilt for Lua 5.4

* Tue Apr 28 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.36.0.0-1
- Update to version 1.36.0-0
- Support building on EPEL 8

* Sat Feb 29 2020 Andreas Schneider <asn@redhat.com> - 1.34.2.1-1
-  Update to version 1.34.2-1
  - https://github.com/luvit/luv/releases/tag/1.34.2-0
  - https://github.com/luvit/luv/releases/tag/1.34.2-1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.1.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Andreas Schneider <asn@redhat.com> - 1.34.1.1-0
- Update to version 1.34.1-1

* Tue Oct 29 2019 Andreas Schneider <asn@redhat.com> - 1.32.0.0-0
- Update to version 1.32.0-0

* Tue Oct 01 2019 Andreas Schneider <asn@redhat.com> - 1.30.1.1-5
- Fixed versioning

* Tue Oct 01 2019 Andreas Schneider <asn@redhat.com> - 1.30.1-4.1
- Update to version 1.30.1-1
- Removed luv-1.30-include_lua_header.patch
- Added missing Requires for devel packages
- Fixed source URL
- Fixed license
- Preserved timestamps

* Mon Sep 30 2019 Andreas Schneider <asn@redhat.com> - 1.30.1-3
- Fixed BR for lua 5.3

* Mon Sep 30 2019 Andreas Schneider <asn@redhat.com> - 1.30.1-2
- Added BR for gcc
- Renamed lua globals

* Tue Sep 24 2019 Andreas Schneider <asn@redhat.com> - 1.30.1-1
- Initial version 1.30.1-0
