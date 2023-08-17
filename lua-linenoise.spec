%global forgeurl https://github.com/hoelzro/lua-linenoise
%global tag %{version}
%forgemeta

Name:      lua-linenoise
Version:   0.9
Release:   %autorelease
Summary:   A binding for the linenoise command line library
# Binding is MIT license and bundled linenoise is BSD
License:   MIT AND BSD-2-Clause
URL:       %{forgeurl}

Source:    %{forgesource}

BuildRequires: lua-devel
BuildRequires: gcc

Provides: bundled(linenoise)
Provides: bundled(linenoise-utf8)

%description
Linenoise (https://github.com/antirez/linenoise) is a delightfully simple
command line library. This Lua module is simply a binding for it.

The main Linenoise upstream has stagnated a bit, so this binding tracks
https://github.com/yhirose/linenoise/tree/utf8-support, which includes things
like UTF-8 support and ANSI terminal escape sequence detection.


%prep
%forgesetup


%build
%{__cc} %{optflags} %{?__global_ldflags} -fPIC -c -o linenoise.o linenoise.c
%{__cc} %{optflags} %{?__global_ldflags} -fPIC -c -o encodings/utf8.o encodings/utf8.c
%{__cc} %{optflags} %{?__global_ldflags} -fPIC -c -o linenoiselib.o linenoiselib.c

%{__cc} %{?__global_ldflags} -shared -o linenoise.so linenoise.o encodings/utf8.o linenoiselib.o


%install
install -dD %{buildroot}%{lua_libdir}
install -p -m 755 linenoise.so %{buildroot}%{lua_libdir}/


%check
LUA_CPATH=%{buildroot}%{lua_libdir}/linenoise.so \
lua -e 'local L = require "linenoise"; L.enableutf8();'


%files
%license COPYING
%doc README.md
%doc Changes
%doc readline-readme.md
%doc example.lua
%{lua_libdir}/linenoise.so


%changelog
%autochangelog
