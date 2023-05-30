%global srcname readline

# Tests currently fail
# Testing readline.lua 2.9, 27jan2021 on Linux
# ok 1 - type of RL is table
# About to test the Alternative Interface ...
# Tab-completion should work: readline: readline_callback_read_char() called with no handler!
%bcond_with tests

Name:           lua-%{srcname}
Version:        3.3
Release:        %autorelease
Summary:        Lua interface to the readline and history libraries

License:        MIT
URL:            https://pjb.com.au/comp/lua/%{srcname}.html
Source0:        https://pjb.com.au/comp/lua/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  lua-devel >= 5.1
%if %{with tests}
BuildRequires:  lua-posix
%endif
BuildRequires:  readline-devel
Requires:       lua-posix
%if 0%{?el7}
BuildRequires:  lua-rpm-macros
%endif
%if 0%{?fedora} < 33 && 0%{?rhel} < 9
Requires:       lua(abi) = %{lua_version}
%endif

%description
This Lua module offers a simple calling interface to the GNU Readline/History
Library.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%{__cc} %{optflags} %{?__global_ldflags} -fPIC \
  $(pkgconf --cflags --libs lua) $(pkgconf --cflags --libs readline) \
  -c C-%{srcname}.c
%{__cc} %{?__global_ldflags} -shared -o C-%{srcname}.so C-%{srcname}.o

%install
mkdir -p %{buildroot}%{lua_libdir}
mkdir -p %{buildroot}%{lua_pkgdir}
cp -p C-%{srcname}.so %{buildroot}%{lua_libdir}/
cp -p %{srcname}.lua %{buildroot}%{lua_pkgdir}/


%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   local RL = require("readline"); print("Hello from "..RL.Version.."!");'

%if %{with tests}
lua test/test_rl.lua
%endif


%files
%doc doc/%{srcname}.html
%{lua_libdir}/C-%{srcname}.so
%{lua_pkgdir}/%{srcname}.lua


%changelog
%autochangelog
