%define __cmake_in_source_build 1

Name:		stratagus
Summary:	Real-time strategy gaming engine
Version:	3.3.2
Release:	3%{?dist}
License:	GPLv2
URL:		https://github.com/Wargus/Stratagus
Source0:	https://github.com/Wargus/Stratagus/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		stratagus-0001-Fix-binaries-path.patch
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_image-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	compat-lua-devel
BuildRequires:	compat-tolua++-devel
BuildRequires:	dos2unix
BuildRequires:	gcc-c++
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	make
BuildRequires:	sqlite-devel
BuildRequires:	zlib-devel
Provides:	bundled(guichan)


%description
Stratagus is a free cross-platform real-time strategy gaming engine. It
includes support for playing over the internet/LAN, or playing a
computer opponent. The engine is configurable and can be used to create
games with a wide-range of features specific to your needs.


%package devel
Summary:       Development files for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description devel
This package contains development files for %{name}.


%prep
%autosetup -p1
iconv -f iso8859-1 -t utf8 doc/guichan-copyright.txt > doc/guichan-copyright.utf8 && mv -f doc/guichan-copyright.{utf8,txt}

%build
mkdir build
pushd build
%cmake .. -DENABLE_DEV=ON -DLUA_INCLUDE_DIR=%{_includedir}/lua-5.1
make %{?_smp_mflags}
popd


%install
make install -C build DESTDIR=%{buildroot}


%files
%license COPYING
%doc README.md doc/
%{_bindir}/%{name}
%{_bindir}/png2%{name}


%files devel
%{_includedir}/%{name}*

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 11 2022 Peter Lemenkov <lemenkov@gmail.com> - 3.3.2-1
- Update to ver. 3.3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 22 2020 Jeff Law <law@redhat.com> - 2.4.2-6
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.4.2-1
- Update to ver. 2.4.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.7-6
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 26 2015 Hans de Goede <hdegoede@redhat.com> - 2.2.7-5
- Rebuilt against compat-tolua++ / fix FTBFS

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Filipe Rosset <rosset.filipe@gmail.com> - 2.2.7-3
- Fix FTBFS build in rawhide, spec cleanup, dependencies fixes
- Added patch to fix binaries path, provide -devel package
- Fixes rhbz #993385 and #1107379

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 01 2013 Bruno Wolff III <bruno@wolff.to> - 2.2.7-1
- Update to upstream 2.2.7
- Project has moved from sourceforge to launchpad
- Changelog: https://launchpad.net/stratagus/+milestone/2.2.7
- Update supports lua 5.1
- Update supports libpng 1.6
- Stratagus has switched to cmake

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Bruno Wolff III <bruno@wolff.to> 2.2.4-14
- Fix for libpng 1.5 so it will build in rawhide

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-12
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.2.4-10
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 03 2009 Caolán McNamara <caolanm@redhat.com> - 2.2.4-7
- add stdio.h for stderr

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Peter Lemenkov <lemenkov@gmail.com> 2.2.4-5
- Fixed links
- Cosmetic cleanups

* Tue Feb 26 2008 Jindrich Novy <jnovy@redhat.com> 2.2.4-4
- fix build in gcc-4.3 (#434370)
- rebuild against new libmikmod (#434783)

* Sat Feb 23 2008 Peter Lemenkov <lemenkov@gmail.com> 2.2.4-3
- rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.4-2
- Autorebuild for GCC 4.3

* Sat Aug  4 2007 Peter Lemenkov <lemenkov@gmail.com> 2.2.4-1
- Version 2.2.4

* Thu Apr 19 2007 Peter Lemenkov <lemenkov@gmail.com> 2.2.3-2
- rebuild

* Mon Mar  5 2007 Peter Lemenkov <lemenkov@gmail.com> 2.2.3-1
- Ver. 2.2.3
- dropped stratagus--use-lua51.diff

* Wed Jan 24 2007  Peter Lemenkov <lemenkov@gmail.com> 2.2.2-0
- Version 2.2.2

* Sun Dec 24 2006 Peter Lemenkov <lemenkov@gmail.com> 2.2.1-0
- Version 2.2.1
- Using externally shipping tolua++ nstead of internal one.
- No more using of MAD and FLAC

* Sat Nov 18 2006 Peter Lemenkov <lemenkov@gmail.com> 2.1-11
- fix for bug #216166 suggested by Hans de Goede

* Thu Nov 16 2006 Peter Lemenkov <lemenkov@gmail.com> 2.1-10
- Applied patches from Hans de Goede

* Sat Sep 16 2006 Peter Lemenkov <lemenkov@gmail.com> 2.1-9%{?dist}
- Added necessary BuildRequires

* Sat Sep 16 2006 Peter Lemenkov <lemenkov@gmail.com> 2.1-8%{?dist}
- Fixed library paths

* Sat Sep 16 2006  Peter Lemenkov <lemenkov@gmail.com> 2.1-7%{?dist}
- Fix building with Lua 5.1

* Sat May 06 2006 Peter Lemenkov <lemenkov@newmail.ru> 2.1-6%{?dist}
- Added link to page with datasets

* Thu Mar 30 2006 Peter Lemenkov <lemenkov@newmail.ru> 2.1-5%{?dist}
- addition of new patch

* Thu Mar 30 2006 Peter Lemenkov <lemenkov@newmail.ru> 2.1-4%{?dist}
- patch for removal /usr/local/-directories from Rules.make.in
- temporarily disabled parallel make

* Thu Mar 30 2006 Peter Lemenkov <lemenkov@newmail.ru> 2.1-2%{?dist}
- added dist-tag

* Thu Mar 30 2006 Peter Lemenkov <lemenkov@newmail.ru> 2.1-2
- rebuild

* Sat Nov 19 2005 Peter Lemenkov <lemenkov@newmail.ru> 2.1-1
- Initial build for FC-Extras
