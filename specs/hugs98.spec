%define hugs_ver plus-Sep2006

Name:		hugs98
Version:	2006.09
Release:	53%{?dist}
Summary:	Haskell Interpreter

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.haskell.org/hugs
Source0:	http://cvs.haskell.org/Hugs/downloads/2006-09/%{name}-%{hugs_ver}.tar.gz
Patch0:         hugs98-gnu.patch
Patch1:		hugs98-config.patch
Patch2: hugs98-machdep-bufsize.patch

BuildRequires:	docbook-utils
BuildRequires:	freeglut-devel
BuildRequires:	gcc
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	libICE-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	libXi-devel
BuildRequires:	libXmu-devel
BuildRequires:	libXt-devel
BuildRequires:	readline-devel
BuildRequires:	xorg-x11-proto-devel
BuildRequires:	openal-soft-devel
BuildRequires:	freealut-devel
%ifnarch aarch64 ppc64le x86_64
BuildRequires:	/usr/bin/execstack
%endif
BuildRequires: make

%description
Hugs 98 is a functional programming system based on Haskell 98,
the de facto standard for non-strict functional programming languages.
Hugs 98 provides an almost complete implementation of Haskell 98.


%package openal
Summary:	OpenAL package for Hugs98
Requires:	%{name} = %{version}-%{release}

%description openal
OpenAL package for Hugs98.


%package alut
Summary:	ALUT package for Hugs98
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-openal = %{version}-%{release}

%description alut
ALUT package for Hugs98.


%package x11
Summary:	X11 package for Hugs98
Requires:	%{name} = %{version}-%{release}

%description x11
X11 package for Hugs98.


%package opengl
Summary:	OpenGL package for Hugs98
Requires:	%{name} = %{version}-%{release}

%description opengl
OpenGL package for Hugs98.


%package glut
Summary:	GLUT package for Hugs98
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-opengl = %{version}-%{release}

%description glut
GLUT package for Hugs98.


%package hgl
Summary:	Haskell Graphics Library for Hugs98
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-x11 = %{version}-%{release}

%description hgl
Haskell Graphics Library for Hugs98.


%package demos
Summary:	Demo files for Hugs98
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-glut = %{version}-%{release}
Requires:	%{name}-hgl = %{version}-%{release}

%description demos
Demo files for Hugs98.


%prep
%setup -q -n %{name}-%{hugs_ver}
# add undefined struct
%patch -P0 -p1 -b .gnu
%patch -P1 -p1 -b .config
%patch -P 2 -p1
# use inline keyword
sed -i 's|extern inline|inline|' packages/base/include/HsBase.h packages/network/include/HsNet.h packages/unix/include/HsUnix.h hsc2hs/Main.hs
# libalut needs libopenal
sed -i 's|ALUT_LIBS="$ac_cv_search_alutExit"|ALUT_LIBS="$ac_cv_search_alutExit -lopenal"|' packages/ALUT/configure
# this is to avoid network lookup of the DTD
sed -i 's|\"http://www.oasis-open.org.*\"||' docs/users_guide/users_guide.xml
# Update config.guess/sub to fix builds on new architectures (aarch64/ppc64le)
cp /usr/lib/rpm/redhat/config.* .


%build
# Work around C99 compatibility issues (bug 2160645).
%global build_type_safety_c 0
# Some configure probes do not use CFLAGS.
export CC="gcc -fpermissive"
%define __global_ldflags ""
%configure --with-pthreads --enable-char-encoding=locale
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install_all_but_docs
make -C docs DESTDIR=%{buildroot} install_man

%ifnarch aarch64 ppc64le x86_64
execstack -s %{buildroot}%{_bindir}/{hugs,runhugs,ffihugs}
%endif

find %{buildroot} -name '*.so' -exec chmod 0755 '{}' ';'

rm %{buildroot}%{_libdir}/hugs/demos/Makefile.in

mv %{buildroot}%{_datadir}/hsc2hs-*/* %{buildroot}%{_libdir}/hugs/programs/hsc2hs

sed -i "s|^bindir.*|bindir=\"%{_bindir}\"|
        s|^libdir.*|libdir=\"%{_libdir}/hugs/programs/hsc2hs|
        s|^datadir.*|datadir=\"%{_libdir}/hugs/programs/hsc2hs\"|" \
    %{buildroot}%{_libdir}/hugs/programs/hsc2hs/Paths_hsc2hs.hs



%files
%license License
%doc Readme
%doc Credits
%doc docs/ffi-notes.txt
%doc docs/server.html
%doc docs/libraries-notes.txt
%doc docs/users_guide/users_guide
%{_bindir}/cpphs-hugs
%{_bindir}/ffihugs
%{_bindir}/hugs
%{_bindir}/hsc2hs-hugs
%{_bindir}/runhugs
%{_libdir}/hugs
%exclude %{_libdir}/hugs/packages/OpenAL
%exclude %{_libdir}/hugs/packages/ALUT
%exclude %{_libdir}/hugs/packages/X11
%exclude %{_libdir}/hugs/packages/OpenGL
%exclude %{_libdir}/hugs/packages/GLUT
%exclude %{_libdir}/hugs/packages/HGL
%{_mandir}/man1/hugs.1*


%files demos
%{_libdir}/hugs/demos


%files openal
%{_libdir}/hugs/packages/OpenAL


%files alut
%{_libdir}/hugs/packages/ALUT


%files x11
%{_libdir}/hugs/packages/X11


%files opengl
%{_libdir}/hugs/packages/OpenGL


%files glut
%{_libdir}/hugs/packages/GLUT


%files hgl
%{_libdir}/hugs/packages/HGL


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2006.09-52
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Florian Weimer <fweimer@redhat.com> - 2006.09-49
- Build with CC="gcc -fpermissive", increase command line buffer size

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 29 2023 Florian Weimer <fweimer@redhat.com> - 2006.09-47
- Set build_type_safety_c to 0 (#2160645)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-40
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Jeff Law <law@redhat.com> - 2006.09-38
- Fix configure test compromised by LTO.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Jens Petersen <petersen@redhat.com> - 2006.09-35
- drop alternatives
- more explicit filelists

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2006.09-34
- Rebuild for readline 8.0

* Sun Feb  3 2019 Jens Petersen <petersen@redhat.com> - 2006.09-33
- drop use of execstack on x86_64

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Jens Petersen <petersen@redhat.com> - 2006.09-30
- BR gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2006.09-25
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2006.09-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 04 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2006.09-23
- Use new execstack (#1247795)

* Fri Jul 10 2015 Gérard Milmeister <gemi@bluewin.ch> - 2006.09-22
- Build fixes

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2006.09-19
- Fix build for aarch/ppc64le

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 29 2013 Jens Petersen <petersen@redhat.com> - 2006.09-17
- buildroot spec file cleanup

* Wed Aug 21 2013 Jens Petersen <petersen@redhat.com> - 2006.09-16
- BR autoconf for aarch64

* Tue Aug 20 2013 Jens Petersen <petersen@redhat.com> - 2006.09-15
- regenerate autoconf files on aarch64 (#925561)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 19 2010 Jens Petersen <petersen@redhat.com> - 2006.09-9
- rebuild

* Sun Aug 16 2009 Gerard Milmeister <gemi@bluewin.ch> - 2006.09-8
- rebuild against openal-soft

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul  3 2009 Gerard Milmeister <gemi@bluewin.ch> - 2006.09-6
- added alternatives setup for runhaskell and friends

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2006.09-4
- Autorebuild for GCC 4.3

* Sun Feb 11 2007 Gerard Milmeister <gemi@bluewin.ch> - 2006.09-2
- rebuild to use ncurses

* Mon Oct 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 2006.09-1
- new version Sep2006

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 2006.05-6
- Rebuild for FE6

* Fri Jun 23 2006 Gerard Milmeister <gemi@bluewin.ch> - 2006.05-5
- switch char encoding from utf-8 to locale

* Wed Jun 21 2006 Gerard Milmeister <gemi@bluewin.ch> - 2006.05-4
- added execstack for the hugs binary

* Tue Jun 20 2006 Gerard Milmeister <gemi@bluewin.ch> - 2006.05-1
- new version 2006.05 with libraries

* Mon Apr 24 2006 Gerard Milmeister <gemi@bluewin.ch> - 2005.03-3
- added patch provided by Jens Petersen to build OpenAL package

* Tue Apr 18 2006 Gerard Milmeister <gemi@bluewin.ch> - 2005.03-1
- changed version numbering scheme
- split off demos package
- split of some packages
- do not build openal support (compile errors)
- enable pthreads

* Wed Mar 30 2005 Gerard Milmeister <gemi@bluewin.ch> - 200503-1
- New Version Mar2005

* Sun Feb 13 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:200311-1
- Changed version scheme

* Mon Jan  5 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.0-0.fdr.1.200311
- New Version Nov2003

* Mon Oct 20 2003 Gerard Milmeister <gemi@bluewin.ch> - Nov2002-0.fdr.1
- First Fedora release
