%global majorrel 4.3.0
%global commit e99ab4a000411dace7d3423ec37bdb7772998b1c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20200221

%ifarch %{java_arches}
%bcond_without java
%endif

# probably never coming back. sorry.
%bcond_with plugin

Name:		freewrl
Version:	%{majorrel}
Release:	23.%{commitdate}git%{shortcommit}%{?dist}
Summary:	X3D / VRML visualization program
License:	LGPL-3.0-or-later
URL:		http://freewrl.sourceforge.net
# Source0:	http://sourceforge.net/projects/freewrl/files/freewrl-linux/3.0/%%{name}-%%{version}.tar.bz2
# git clone https://git.code.sf.net/p/freewrl/git freewrl-git
# cd freewrl-git
# cp -a freex3d/ ../freewrl-%%{version}-%%{commitdate}git%%{shortcommit}
# cd ..
# tar --exclude-vcs -cjf %%{name}-%%{version}-%%{commitdate}git%%{shortcommit}.tar.bz2 freewrl-%%{version}-%%{commitdate}git%%{shortcommit}
Source0:	%{name}-%{version}-%{commitdate}git%{shortcommit}.tar.bz2
Source1:	README.FreeWRL.java
# gcc says:
# main/ProdCon.c:427:19: error: too few arguments to function 'cParse'
Patch3:		freewrl-3.0.0-20170208git621ae4e-cparse-stl-fix.patch
# warning: '__builtin_strncpy' output truncated before terminating nul copying 54 bytes from a string of the same length [-Wstringop-truncation]
Patch4:		freewrl-4.3.0-use-memcpy-instead-of-strncpy.patch
# main/ProdCon.c:414:29: warning: implicit declaration of function 'convertAsciiSTL' [-Wimplicit-function-declaration]
# main/ProdCon.c:424:29: warning: implicit declaration of function 'convertBinarySTL' [-Wimplicit-function-declaration]
Patch5:		freewrl-4.3.0-missing-functions.patch
# lots of indent issues caught by -Wmisleading-indentation
Patch6:		freewrl-4.3.0-fix-indent-issues.patch
# lots of signedness fixes like
# io_files.c:627:17: warning: pointer targets in passing argument 1 of 'stlDTFT' differ in signedness [-Wpointer-sign]
Patch7:		freewrl-4.3.0-sign-fixes.patch
Patch8: freewrl-c99.patch
# Fix issue with incompatible pointer type
Patch9:		freewrl-4.3.0-fix-cast.patch
BuildRequires:	gcc-c++
BuildRequires:	zlib-devel, freetype-devel, fontconfig-devel
BuildRequires:	imlib2-devel, nspr-devel
BuildRequires:	expat-devel, libXxf86vm-devel, libX11-devel, libXext-devel
BuildRequires:	mesa-libGL-devel, mesa-libGLU-devel, glew-devel, libxml2-devel
BuildRequires:	libjpeg-devel, libpng-devel, unzip, wget
BuildRequires:	ImageMagick, desktop-file-utils, chrpath
BuildRequires:	libXaw-devel, libXmu-devel, freealut-devel
BuildRequires:	liblo-devel, libcurl-devel, openal-soft-devel
%if %{with java}
BuildRequires:	java-devel
%endif
%if %{with plugin}
%ifnarch armv7hl s390x i686
BuildRequires:	firefox
%endif
%endif
BuildRequires:	sox, doxygen
BuildRequires:	ode-devel
BuildRequires:	autoconf, automake, libtool
BuildRequires:	make

Requires:	sox, unzip, wget, ImageMagick

%description
FreeWRL is an X3D / VRML visualization program. This package contains the
standalone commandline tool.

%package devel
Summary:	Development files for FreeWRL
Requires:	freewrl%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Development libraries and headers for FreeWRL.

%if %{with java}
%package java
Summary:	Java support for FreeWRL
Requires:	java-headless
Requires:	freewrl%{?_isa} = %{version}-%{release}

%description java
Java support for FreeWRL.
%endif

%package -n libEAI
Summary:	FreeWRL EAI C support library

%description -n libEAI
FreeWRL EAI C support library.

%package -n libEAI-devel
Summary:	Development files for libEAI
Requires:	libEAI%{?_isa} = %{version}-%{release}

%description -n libEAI-devel
Development libraries and headers for libEAI.

%if %{with plugin}
%ifnarch armv7hl s390x
%package plugin
Summary:	Browser plugin for FreeWRL
Requires:	freewrl%{?_isa} = %{version}-%{release}
Requires:	firefox

%description plugin
FreeWRL is an X3D / VRML visualization program. This package contains the
browser plugin for Firefox (and other xulrunner compatible browsers).
%endif
%endif

%prep
%setup -q -n %{name}-%{majorrel}-%{commitdate}git%{shortcommit}
%if %{with java}
cp %{SOURCE1} .
%endif
# Don't need it.
rm -rf appleOSX/
%patch -P3 -p1 -b .cparsestlfix
%patch -P4 -p1 -b .memcpy
%patch -P5 -p1 -b .missing-functions
%patch -P6 -p1 -b .fixindent
%patch -P7 -p1 -b .signfix
%patch -P8 -p1
%patch -P9 -p1 -b .fix-cast
autoreconf --force --install

# hardcoding /usr/local/lib is a no-no
sed -i 's|libpath = "/usr/local/lib"|libpath = "%{_libdir}"|g' src/bin/main.c

%build
%global optflags %{optflags} -Wno-comment -Wno-unused-variable
export LDFLAGS="-Wl,--as-needed"
%configure --with-target=x11 \
	   --enable-fontconfig \
	   %{?with_java:--enable-java} \
	   --enable-libeai \
	   --disable-osc \
	   --enable-libcurl \
	   --enable-rbp \
	   --enable-twodee \
	   --enable-STL \
	   --disable-static \
	   --with-javadir=/usr/lib/jvm/java-openjdk/jre/lib/ext \
	   --with-javascript=duk \
	   --with-statusbar=hud
make %{?_smp_mflags}
pushd doc
make html/index.html
popd

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}/
%if %{with java}
install -p src/java/java.policy %{buildroot}%{_datadir}/%{name}/
%endif

%if %{with plugin}
# no firefox on armv7hl | s390x | i686
%ifarch armv7hl s390x i686
rm -rf %{buildroot}%{_libdir}/mozilla/plugins/libFreeWRLplugin.so
%endif
%endif

rm -rf %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/mozilla/plugins/*.la

desktop-file-validate %{buildroot}%{_datadir}/applications/freewrl.desktop
chmod -x %{buildroot}%{_datadir}/applications/freewrl.desktop
%if %{with java}
chmod -x %{buildroot}%{_datadir}/%{name}/java.policy
%endif

chrpath --delete %{buildroot}%{_bindir}/freewrl
# chrpath --delete %%{buildroot}%%{_bindir}/freewrl_snd
chrpath --delete %{buildroot}%{_libdir}/libFreeWRLEAI.so.*

%ldconfig_scriptlets

%ldconfig_scriptlets -n libEAI

%files
%doc AUTHORS README TODO
%license COPYING COPYING.LESSER
%{_bindir}/%{name}
%{_bindir}/%{name}_msg
# %%{_bindir}/%%{name}_snd
%{_libdir}/libFreeWRL.so.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}*

%files devel
%doc doc/html
%{_includedir}/libFreeWRL.h
%{_libdir}/libFreeWRL.so
%{_libdir}/pkgconfig/libFreeWRL.pc

%if %{with java}
%files java
%doc README.FreeWRL.java
%{_datadir}/%{name}/
/usr/lib/jvm/java-openjdk/jre/lib/ext/vrml.jar
%endif

%files -n libEAI
%license COPYING COPYING.LESSER
%{_libdir}/libFreeWRLEAI.so.*

%files -n libEAI-devel
%{_includedir}/FreeWRLEAI/
%{_libdir}/libFreeWRLEAI.so
%{_libdir}/pkgconfig/libFreeWRLEAI.pc

# Plugin is dead and gone, thanks to Mozilla.
%if %{with plugin}
%ifnarch armv7hl s390x i686
%files plugin
%{_libdir}/mozilla/plugins/libFreeWRLplugin.so
%endif
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-23.20200221gite99ab4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-22.20200221gite99ab4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Tom Callaway <spot@fedoraproject.org> - 4.3.0-21.20200221gite99ab4a
- fix FTBFS

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-20.20200221gite99ab4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-19.20200221gite99ab4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-18.20200221gite99ab4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Leigh Scott <leigh123linux@gmail.com> - 4.3.0-17.20200221gite99ab4a
- Rebuild fo new imlib2

* Tue Feb 21 2023 Florian Weimer <fweimer@redhat.com> - 4.3.0-16.20200221gite99ab4a
- Port to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-15.20200221gite99ab4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Tom Callaway <spot@fedoraproject.org> - 4.3.0-14.20200221gite99ab4a
- disable plugin more completely with a conditional

* Sun Jul 24 2022 Robert-André Mauchin <zebob.m@gmail.com> - 4.3.0-13.20200221gite99ab4a
- Rebuilt for Ode soname bump

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-12.20200221gite99ab4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 4.3.0-11.20200221gite99ab4a
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-10.20200221gite99ab4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 30 2021 Tom Callaway <spot@fedoraproject.org> - 4.3.0-9.20200221gite99ab4a
- drop obsolete BR: texlive-updmap-map
- update to latest git code

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-8.20190827git36b721c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb  1 2021 Tom Callaway <spot@fedoraproject.org> - 4.3.0-7.20190827git36b721c
- fix tex BR

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-6.20190827git36b721c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-5.20190827git36b721c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 4.3.0-4.20190827git36b721c
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 18 2020 Tom Callaway <spot@fedoraproject.org> - 4.3.0-3.20190827git36b721c
- fix tex dependencies

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2.20190827git36b721c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Tom Callaway <spot@fedoraproject.org> - 4.3.0-1.20190827git36b721c
- update to latest git master
- apply some code cleanups to make compile quieter

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11.20170729git4f920cb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Tom Callaway <spot@fedoraproject.org> - 3.0.0-10.20170729git4f920cb
- add lots of missing tex BRs

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9.20170729git4f920cb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8.20170729git4f920cb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun  1 2018 Tom Callaway <spot@fedoraproject.org> - 3.0.0-7.20170729git4f920cb
- add missing texlive BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6.20170729git4f920cb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Tom Callaway <spot@fedoraproject.org> - 3.0.0-5.20170729git4f920cb
- update again, git master is now proper branch
- reapply curl res fix

* Fri Jul 28 2017 Tom Callaway <spot@fedoraproject.org> - 3.0.0-4.20170708git7a28224
- update to git devel tree
- do not bother with mozilla plugin
- fix code to not immediately and always SEGV

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3.20170208git621ae4e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb  8 2017 Tom Callaway <spot@fedoraproject.org> - 3.0.0-2.20170208git621ae4e
- update to git develop tree
- disable osc
- fix armv7hl weirdness

* Fri May 27 2016 Tom Callaway <spot@fedoraproject.org> - 3.0.0-1
- update to 3.0.0

* Fri Feb 05 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.3.3.1-7
- Add BR: tex(tabu.sty) (Fix F24FTBFS).
- Add %%license.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Tom Callaway <spot@fedoraproject.org> - 2.3.3.1-6
- add missing tex BR

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Tom Callaway <spot@fedoraproject.org> - 2.3.3.1-3
- add missing tex BR

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Tom Callaway <spot@fedoraproject.org> - 2.3.3.1-1
- update to 2.3.3.1

* Tue Apr 22 2014 Tom Callaway <spot@fedoraproject.org> - 2.3.3-1
- update to 2.3.3

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.22.13.1-13
- Use Requires: java-headless rebuild (#1067528)

* Sun Feb  9 2014 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-12
- fix the fontconfig font matching code to actually work (bz 1062829)

* Tue Dec  3 2013 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-11
- fix error with -Werror=format-security 

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 1.22.13.1-10
- rebuilt for GLEW 1.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.13.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr  9 2013 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-8
- use js-devel (xulrunner's jsapi.h is now C++ only)

* Fri Feb  1 2013 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-7
- three args for JS_GetPrototype today
- fix more abandoned API

* Wed Jan  9 2013 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-6
- use JS_NewGlobalObject instead of JS_NewCompartmentAndGlobalObject

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.22.13.1-5
- rebuild against new libjpeg

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 1.22.13.1-4
- Rebuild for glew 1.9.0

* Tue Jul 31 2012 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-3
- fix build, patch out deprecated JS_FinalizeStub, JS_DestroyContextMaybeGC

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-1
- update to 1.22.13.1

* Tue Jan 17 2012 Tom Callaway <spot@fedoraproject.org> - 1.22.12-0.7.pre2
- fix compile with gcc 4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.12-0.6.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec  6 2011 Tom Callaway <spot@fedoraproject.org> - 1.22.12-0.5.pre2
- fix build against firefox8 

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.22.12-0.4.pre2
- Rebuild for new libpng

* Tue Aug  9 2011 Tom Callaway <spot@fedoraproject.org> - 1.22.12-0.3.pre2
- move browser plugin to independent subpackage to minimize deps on main package

* Tue Aug  9 2011 Tom Callaway <spot@fedoraproject.org> - 1.22.12-0.2.pre2
- drop Requires: pkgconfig
- delete appleOSX/ dir 

* Wed Jul 27 2011 Tom Callaway <spot@fedoraproject.org> - 1.22.12-0.1.pre2
- pre2

* Tue Jul 19 2011 Tom Callaway <spot@fedoraproject.org> - 1.22.12-0.1.pre1
- initial package
