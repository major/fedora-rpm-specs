# missing test dependencies
%bcond tests 0

%global pkgname moonscript

Name:           lua-%{pkgname}
Version:        0.6.0
Release:        %autorelease
Summary:        A little language that compiles to Lua

# license text part of README.md
License:        MIT
URL:            http://moonscript.org/
Source:         https://github.com/leafo/moonscript/archive/v%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  lua-devel >= 5.1
BuildRequires:  lua-argparse >= 0.7
BuildRequires:  lua-filesystem >= 1.5
# avoid lpeg 0.11 per upstream rockspec
BuildRequires:  lua-lpeg >= 0.12
%if %{with tests}
BuildRequires:  make
%endif
Requires:       /usr/bin/lua
Requires:       lua-argparse >= 0.7
Requires:       lua-filesystem >= 1.5
Requires:       lua-lpeg >= 0.12
# lua-inotify is a soft requirement;
# needed for the directory watching feature
Recommends:     lua-inotify


%description
MoonScript is a dynamic scripting language that compiles into Lua. It
gives you the power of Lua combined with a rich set of features.

MoonScript can either be compiled into Lua and run at a later time, or
it can be dynamically compiled and run using the moonloader. It’s as
simple as require "moonscript" in order to have Lua understand how to
load and run any MoonScript file.

Because it compiles right into Lua code, it is completely compatible
with alternative Lua implementations like LuaJIT, and it is also
compatible with all existing Lua code and libraries.

The command line tools also let you run MoonScript directly from the
command line, like any first-class scripting language.


%prep
%autosetup -n %{pkgname}-%{version}
chmod +x bin/moonc


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p bin/moon{,c,-tags} $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{lua_pkgdir}
cp -pr moon moonscript $RPM_BUILD_ROOT%{lua_pkgdir}/


%check
%if %{with tests}
make test
%endif


%files
%doc CHANGELOG.md README.md docs/*
%{_bindir}/moon
%{_bindir}/moonc
%{_bindir}/moon-tags
%{lua_pkgdir}/moon
%{lua_pkgdir}/moonscript


%changelog
%autochangelog
