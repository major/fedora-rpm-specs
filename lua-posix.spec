# Tests require specl which is not yet packaged
%bcond_with check

Name:           lua-posix
Version:        36.2.1
Release:        %autorelease
Summary:        POSIX library for Lua
License:        MIT
URL:            http://luaforge.net/projects/luaposix/
Source0:        https://github.com/luaposix/luaposix/archive/v%{version}/lua-posix-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  lua-devel
%{?lua_requires}

%description
This is a POSIX library for Lua which provides access to many POSIX features
to Lua programs.


%prep
%autosetup -p1 -n luaposix-%{version}


%build
build-aux/luke CFLAGS="%build_cflags" LDFLAGS="%build_ldflags"


%install
build-aux/luke install PREFIX=%{buildroot}%{_prefix} INST_LIBDIR=%{buildroot}%{lua_libdir}


%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   local posix = require("posix.errno"); print("Hello from "..posix.version.."!");'

%if %{with check}
lua ./spec/spec_helper.lua
%endif


%files
%license LICENSE
%doc AUTHORS NEWS.md README.md
%{lua_libdir}/*
%{lua_pkgdir}/posix/


%changelog
%autochangelog
