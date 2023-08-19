%global forgeurl https://github.com/leafo/loadkit
%global tag v%{version}

Name:      lua-loadkit
Version:   1.1.0
Release:   %autorelease
Summary:   Loadkit allows you to load arbitrary files within the Lua package path
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source0:    %{forgesource}

# https://github.com/leafo/loadkit/issues/3
Source1:   https://github.com/leafo/loadkit/raw/95b13a36442f59b41ab52df96d52233c4a725dfd/LICENSE

BuildArch:     noarch
BuildRequires: lua-devel

%description
Loadkit lets you register new file extension handlers that can be opened
with require, or you can just search for files of any extension using the
current search path.

%prep
%forgesetup

cp %{SOURCE1} .

%build
# Nothing to do here

%install
install -dD %{buildroot}%{lua_pkgdir}
install -p -m 644 loadkit.lua %{buildroot}%{lua_pkgdir}

%check
LUA_PATH=%{buildroot}%{lua_pkgdir}/loadkit.lua \
lua -e 'local loadkit = require "loadkit"; assert(not loadkit.is_registered("test"))'

%files
%license LICENSE
%doc README.md
%{lua_pkgdir}/loadkit.lua

%changelog
%autochangelog
