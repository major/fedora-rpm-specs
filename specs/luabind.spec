Name:		luabind
Version:	0.9.1
Release:	48%{?dist}
Summary:	A library that helps create bindings between C++ and Lua
License:	MIT
URL:		http://www.rasterbar.com/products/luabind.html
Source0:	http://download.sourceforge.net/luabind/%{name}-%{version}.tar.gz
BuildRequires:	boost-devel, boost-build, lua-devel >= 5.1
BuildRequires:	gcc-c++
# https://github.com/devurandom/luabind/commit/78509cc0242161116c989a08439ea28386deeca2
Patch0:		luabind-0.9.1-boost149fix.patch
# Lua 5.2 support
# https://github.com/luabind/luabind/commits/0.9
Patch1:		001-luabind-use-lua_compare.patch
Patch2:		002-luabind-deprecated-LUA_GLOBALSINDEX.patch
Patch3:		003-luabind-use-lua_rawlen.patch
Patch4:		004-luabind-getsetuservalue.patch
Patch5:		005-luabind-lua_resume_extra_param.patch
Patch6:		006-luabind-luaL_newstate.patch
Patch7:		007-luabind-lua-52-fix-test.patch
Patch8:		008-luabind-lua_pushglobaltable.patch
Patch9:		luabind-0.9.1-boost157fix.patch
Patch10:	luabind-0.9.1-lua-5.4.patch
# https://github.com/luabind/luabind/pull/34
Patch11:	luabind-0.9.1-orderfix.patch

%description
Luabind is a library that helps you create bindings between C++ and Lua. It 
has the ability to expose functions and classes, written in C++, to Lua. It 
will also supply the functionality to define classes in Lua and let them derive 
from other Lua classes or C++ classes. Lua classes can override virtual 
functions from their C++ base classes. It is written towards Lua 5.0, and does 
not work with Lua 4.

%package devel
Summary:	Development libraries and headers for luabind
Requires:	%{name} = %{version}-%{release}
Requires:	boost-devel

%description devel
This package contains the development libraries and headers for luabind.

%prep
%setup -q
%patch -P0 -p1 -b .boost
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1 -b .lua54
%patch -P11 -p1 -b .orderfix
sed -i 's|$(prefix)/lib|$(prefix)/%{_lib}|g' Jamroot

# Perms cleanup
chmod -x doc/*.rst doc/*.png src/*.cpp luabind/*.hpp luabind/detail/*.hpp

%build
export BOOST_BUILD_PATH=%{_datadir}/boost-build/src/kernel
b2 %{?jobs:-j%{jobs}} -d+2 "cxxflags=%{optflags}" release

%install
export BOOST_BUILD_PATH=%{_datadir}/boost-build/src/kernel
b2 -d2 --prefix=%{buildroot}%{_prefix} --libdir=%{buildroot}%{_libdir} release install

%ldconfig_scriptlets

%files
%doc LICENSE
%{_libdir}/*.so.*

%files devel
%doc doc/*
%{_includedir}/luabind/
%{_libdir}/*.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug  2 2023 Tom Callaway <spot@fedoraproject.org> - 0.9.1-44
- apply fix for non-functioning inheritance

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb  2 2021 Tom Callaway <spot@fedoraproject.org> - 0.9.1-38
- use BOOST_BUILD_PATH to help b2 always find the boost-build.jam file

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Tom Callaway <spot@fedoraproject.org> - 0.9.1-36
- fix FTBFS, fix build against lua 5.4

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-35
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 0.9.1-30
- add BuildRequires: gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-25
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-23
- Rebuilt for Boost 1.63

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-21
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-20
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.9.1-18
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.1-16
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb  4 2015 Petr Machata <pmachata@redhat.com> - 0.9.1-15
- Rebuild for boost 1.57.0
- Fix an ADL workaround in object.hpp to adapt to the new Boost
  version (luabind-0.9.1-boost157fix.patch)

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 0.9.1-14
- rebuild for lua 5.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.9.1-11
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.9.1-9
- Rebuild for boost 1.54.0

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 0.9.1-8
- fix for lua 5.2

* Thu May  9 2013 Tom Callaway <spot@fedoraproject.org> - 0.9.1-7
- add missing Requires: boost-devel on -devel subpackage

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Tom Callaway <spot@fedoraproject.org> - 0.9.1-5
- apply fix for FTBFS with boost 1.49.0 (bz 893887)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Tom "spot" Callaway <spot@fedoraproject.org> - 0.9.1-1
- initial build for Fedora
