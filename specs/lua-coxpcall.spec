%global         gittag %(v=%{version}; echo ${v//./_})
%global         forgeurl https://github.com/keplerproject/coxpcall
Summary:        Coroutine safe xpcall and pcall versions for Lua
Name:           lua-coxpcall
License:        MIT

Version:        1.17.0
Release:        9%{?dist}

URL:            http://keplerproject.github.io/coxpcall/ 
Source0:        %{forgeurl}/archive/v%{gittag}/coxpcall-v%{gittag}.tar.gz

BuildArch:      noarch
BuildRequires:  lua-devel

%description
Coxpcall encapsulates the protected calls with a coroutine based loop,
so errors can be handled without the usual pcall/xpcall issues with 
coroutines for Lua 5.1.

Using Coxpcall usually consists in simply loading the module and then 
replacing Lua pcall and xpcall by copcall and coxpcall.

Coxpcall is free software and uses the same license as Lua 5.1.

Lua 5.2 was extended with the Coxpcall functionality and hence it 
is no longer required. The 5.2+ compatibility by coxpcall means 
that it maintains backward compatibility while using the built-in 
Lua implementation.

%prep
%autosetup -n coxpcall-%{gittag} 

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{lua_pkgdir}/
cp -p src/coxpcall.lua %{buildroot}%{lua_pkgdir}/


%check
lua tests/test.lua

%files
%doc README.md
%doc doc/coxpcall.png
%doc doc/doc.css
%doc doc/index.html  
%license doc/license.html
%{lua_pkgdir}/coxpcall.lua

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 19 2022 Benson Muite <benson_muite@emailplus.org> - 1.17.0-3
- Fix source url

* Thu Nov 17 2022 Benson Muite <benson_muite@emailplus.org> - 1.17.0-2
- Add changelog history
- Add macro gittag
- Update url

* Thu Nov 17 2022 Benson Muite <benson_muite@emailplus.org> - 1.17.0-1
- Initial packaging for unretirement

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
 
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
 
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
 
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
 
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
 
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
 
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
 
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
 
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
 
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
 
* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 1.15.0-1
- update to 1.15.0
- rebuild for lua 5.3
 
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
 
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
 
* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 1.14.0-1
- update to 1.14.0
 
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
	
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
	
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
	
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 20 2010 Tim Niemueller <tim@niemueller.de> - 1.13.0-1
- Initial package
