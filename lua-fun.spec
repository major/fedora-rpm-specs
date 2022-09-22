%define luaver 5.4
%define luapkgdir %{_datadir}/lua/%{luaver}
# LuaJIT is compatible with Lua 5.1 and uses the same directory for modules
%global ljpkgdir %{_datadir}/lua/5.1

# LuaJIT has limited support for architectures
%ifarch %{arm} %{ix86} x86_64 %{mips} aarch64
%bcond_without luajit
%else
%bcond_with luajit
%endif

Name: lua-fun
Version: 0.1.3
Release: 18%{?dist}
Summary: Functional programming library for Lua
License: MIT
URL: https://github.com/rtsisyk/luafun
Source0: https://github.com/rtsisyk/luafun/archive/%{version}/luafun-%{version}.tar.gz
BuildArch: noarch
BuildRequires: make
BuildRequires: lua >= %{luaver}
%if %{with luajit}
BuildRequires: luajit >= 2.0
%endif
%if 0%{?el6}
Requires: lua >= %{luaver}
%else
Requires: lua(abi) = %{luaver}
%endif

%description -n lua-fun
Lua Fun is a high-performance functional programming library for Lua
designed with LuaJIT's trace compiler in mind.

Lua Fun provides a set of more than 50 programming primitives typically
found in languages like Standard ML, Haskell, Erlang, JavaScript, Python and
even Lisp. High-order functions such as map, filter, reduce, zip, etc.,
make it easy to write simple and efficient functional code.

This package provides a module for Lua %{luaver}.

%if %{with luajit}
%package -n luajit-fun
Summary: Functional programming library for LuaJIT
Requires: luajit >= 2.0

%description -n luajit-fun
Lua Fun is a high-performance functional programming library for Lua
designed with LuaJIT's trace compiler in mind.

Lua Fun provides a set of more than 50 programming primitives typically
found in languages like Standard ML, Haskell, Erlang, JavaScript, Python and
even Lisp. High-order functions such as map, filter, reduce, zip, etc.,
make it easy to write simple and efficient functional code.

This package provides a module for LuaJIT.
%endif # with luajit

%prep
%setup -q -n luafun-%{version}

%build
# nothing to do

%install
# Install for Lua
mkdir -p %{buildroot}%{luapkgdir}
cp -av fun.lua %{buildroot}%{luapkgdir}/fun.lua
%if %{with luajit}
# Install for LuaJIT
mkdir -p %{buildroot}%{ljpkgdir}
cp -av fun.lua %{buildroot}%{ljpkgdir}/fun.lua
%endif # with luajit

%check
cd tests
/usr/bin/lua ./runtest *.lua
%if %{with luajit}
/usr/bin/luajit ./runtest *.lua
%endif # with luajit

%files -n lua-fun
%{luapkgdir}/fun.lua
%doc README.md CONTRIBUTING.md
%license COPYING.md

%if %{with luajit}
%files -n luajit-fun
%{ljpkgdir}/fun.lua
%doc README.md CONTRIBUTING.md
%license COPYING.md
%endif # with luajit

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-13
- Rebuilt for Lua 5.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 7 2016 Roman Tsisyk <roman@tarantool.org> - 0.1.3-5
- Fix #1371238: "lua: command not found" during tests

* Mon Nov 7 2016 Roman Tsisyk <roman@tarantool.org> - 0.1.3-4
- Disable luajit-fun on architectures where LuaJIT is not supported

* Mon Aug 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.1.3-3
- Rebuild for LuaJIT 2.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Roman Tsisyk <roman@tarantool.org> - 0.1.3-1
- Initial version.
