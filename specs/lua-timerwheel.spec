Summary:        Pure Lua timerwheel implementation 
Name:           lua-timerwheel
License:        MIT

Version:        1.0.2
Release:        10%{?dist}

URL:            https://github.com/Tieske/timerwheel.lua
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
Requires:       lua-coxpcall
BuildRequires:  lua-devel
BuildRequires:  lua-coxpcall
#Needed for tests
BuildRequires:  lua-socket
#BuildRequires:  lua-busted

%description
Efficient timer for timeout related timers: fast insertion, deletion, 
and execution (all as O(1) implemented), but with lesser precision.
This module will not provide the timer/runloop itself. Use your own 
runloop and call wheel:step to check and execute timers.

%prep
%autosetup -n timerwheel.lua-%{version} 

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{lua_pkgdir}/timerwheel
cp -p src/timerwheel/init.lua %{buildroot}%{lua_pkgdir}/timerwheel/init.lua
 

%check
#Uses lua-busted which is not available yet.
#Smoke test
LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua;;
" \
lua -e ' 
   local tw = require"timerwheel"
   local set_time, now
   do
     local _time
     _time = 0
     set_time = function(t)
       _time = t
     end
     now = function()
       return _time
     end
   end

   local wheel = tw.new()

   local wheel = tw.new {
     precision = 0.5,
     ringsize = 10,
     now = function() end,
     err_handler = function() end,
   }'


%files
%license LICENSE
%doc README.md
%doc docs/ldoc.css
%doc docs/index.html  
%doc docs/topics/readme.md.html
%dir %{lua_pkgdir}/timerwheel
%{lua_pkgdir}/timerwheel/init.lua

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 08 2023 Benson Muite <benson_muite@emailplus.org> - 1.0.2-4
- Update smoke test

* Sat Nov 19 2022 Benson Muite <benson_muite@emailplus.org> - 1.0.2-3
- Update test, only needed for older versions of lua

* Thu Nov 17 2022 Benson Muite <benson_muite@emailplus.org> - 1.0.2-2
- Add smoke test
- Fix directory ownership
- Include coxpcall as a dependency

* Thu Nov 17 2022 Benson Muite <benson_muite@emailplus.org> - 1.0.2-1
- Initial release
