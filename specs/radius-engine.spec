Name:		radius-engine
Version:	1.1
Release:	27%{?dist}
Summary:	A Lua based real-time 2D graphics game engine
License:	MIT
URL:		http://radius-engine.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz
Patch0:		radius-engine-0.6-configure-lua.patch
Patch1:		radius-engine-1.1-shared-libs.patch
# Latest autoconf enables "extra-portability" along with "Wall", which causes
# warnings (treated as errors because of Wall) to be thrown. We just need to 
# pass "-Wno-extra-portability" to fix this.
Patch2:		radius-engine-1.1-disable-extra-portability.patch
# Use compat-lua
Patch3:		radius-engine-1.1-compat-lua.patch
BuildRequires: make
BuildRequires:	compat-lua-devel, SDL-devel, mesa-libGL-devel, mesa-libGLU-devel
BuildRequires:	physfs-devel, libpng-devel, zlib-devel, SDL_sound-devel
# I could not figure out a way to generate a patch to enable shared libraries 
# that worked right. All my attempts resulted in an environment where make, 
# when invoked, would re-run aclocal and automake. :P
# So, I'm just running autoreconf in the spec file. :P :P
BuildRequires:	autoconf, libtool

%description
Radius Engine is a Lua script-based real-time 2D graphics engine designed for 
rapidly prototyping games. Built on top of SDL and OpenGL, games made with 
Radius Engine are portable to both Windows and Linux.

%package devel
Summary:	Development libraries and headers for Radius Engine
Requires:	compat-lua-devel, SDL-devel, mesa-libGL-devel, mesa-libGLU-devel
Requires:	physfs-devel, libpng-devel, zlib-devel, SDL_sound-devel
Requires:	%{name} = %{version}-%{release}

%description devel
Development libraries and headers for Radius Engine.

%prep
%setup -q
%patch -P0 -p1 -b .lua
%patch -P1 -p1 -b .shared
%patch -P2 -p1 -b .disable-extra-portability
%patch -P3 -p1 -b .compat-lua
# autoconf is being anal now.
mv configure.in configure.ac
autoreconf -if
chmod -x *.c *.h ChangeLog

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc ChangeLog
%{_libdir}/libradius-engine.so.*

%files devel
%{_includedir}/radius.h
%{_libdir}/libradius-engine.so
%{_libdir}/pkgconfig/radius-engine.pc

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 10 2013 Tom Callaway <spot@fedoraproject.org> - 1.1-4
- use compat-lua

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep  4 2012 Tom Callaway <spot@fedoraproject.org> - 1.1-1
- update to 1.1

* Fri Aug  3 2012 Tom Callaway <spot@fedoraproject.org> - 0.7-5
- fix ftbfs because of autoconf changes

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 15 2011 Tom Callaway <spot@fedoraproject.org> - 0.7-2
- rebuild

* Fri Dec  9 2011 Tom Callaway <spot@fedoraproject.org> - 0.7-1
- update to 0.7

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 3 2011 Tom Callaway <spot@fedoraproject.org> 0.6-1
- Initial package
