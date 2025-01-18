Summary:	Execution analysis and debugging tool-suite
Name:		frysk
Version:	0.4
Release:	96%{?dist}

# Fedora 17+ is still waiting for vte et.al. bindings.
%define enable_gnome %{fedora}0 < 170
%define enable_devel %{fedora}0 < 170

# https://docs.fedoraproject.org/en-US/legal/allowed-licenses/
# https://docs.fedoraproject.org/en-US/legal/license-review-process/
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/new
# origin: Legacy Abbreviation -> SPDX
#
# getopt GPLv2+ with exception -> GPL-2.0-or-later WITH Classpath-exception-2.0
# frysk: GPLv2 with 398-exception -> GPL-2.0 WITH ???redhat??? exception
# libunwind: MIT Modern Style with sublicense -> MIT

License:	GPL-2.0-only WITH 389-exception AND GPL-2.0-or-later WITH Classpath-exception-2.0 AND MIT

URL:		http://sourceware.org/frysk
Source:		ftp://sourceware.org/pub/frysk/%{name}-%{version}.tar.bz2

# Import unreleased fixes
Patch0:		frysk-0.4-head.patch

# Local fixes.
Patch1:		frysk-0.4-bash-dollar-star.patch
Patch2:		frysk-0.4-strayelsif.patch
Patch3:		frysk-0.4-fdebugrpm.patch
Patch4:		frysk-0.4-mktlwidgetdir.patch
Patch5:		frysk-0.4-gcc-warnings.patch
Patch6:		frysk-0.4-funitexitman.patch
Patch7:		frysk-0.4-mvtesttomain.patch
Patch8:		frysk-0.4-taskstoputil.patch
Patch9:		frysk-0.4-publictestbedsymtab.patch
Patch10:	frysk-0.4-noelfmem.patch
Patch11:	frysk-0.4-gccjint.patch
Patch12:	frysk-0.4-taskstoperr.patch
Patch13:	frysk-0.4-lostfork.patch
Patch14:	frysk-0.4-nooptimize.patch
Patch15:	frysk-0.4-skipdecl.patch
Patch16:	frysk-0.4-flushstat.patch
Patch17:	frysk-0.4-ftrace.patch
Patch18:	frysk-0.4-usererrno.patch
Patch19:	frysk-0.4-configure-enable-gnome.patch
Patch20:	frysk-0.4-bin-antlr.patch
Patch21:	frysk-0.4-nopkglibdir.patch
Patch22:	frysk-0.4-no-jdom.patch
Patch23:	frysk-0.4-missing-javah-cni-built.patch
Patch24:	frysk-0.4-jni.patch
Patch25:	frysk-0.4-awk-gensub.patch
Patch26:	frysk-0.4-pic-asm.patch
Patch27:	frysk-0.4-per-thread-java-id.patch
Patch28:	frysk-0.4-unwind-global-id.patch
Patch29:	frysk-0.4-use-installed-antlr.patch
Patch30:	frysk-0.4-use-installed-junit.patch
Patch31:	frysk-0.4-jni-issameobject.patch
Patch32:	frysk-0.4-switch-ecj-to-javac.patch
Patch33:	frysk-0.4-use-installed-jline.patch
Patch34:	frysk-0.4-libunwind-fstack.patch
Patch35:	frysk-0.4-clone-cursor.patch
Patch36:	frysk-0.4-fedpkg-lint-licence.patch
Patch37:	frysk-0.4-fedpkg-lint-solib.patch
Patch38:	frysk-0.4-gelf-newphdr.patch
Patch39:	frysk-0.4-jnixx-signed-unsigned.patch
Patch40:	frysk-0.4-check-p-not-status.patch
Patch41:	frysk-0.4-python3.patch
Patch42:	frysk-0.4-jline1-to-jline.patch
Patch43:	frysk-0.4-disable-arch32-tests.patch
Patch44:	frysk-0.4-steptester-indentation.patch
Patch45:	frysk-0.4-gcc-fcommon.patch
Patch46:	frysk-0.4-javac.patch
Patch47:	frysk-0.4-jnixx-union-as-reserved-word.patch
Patch48:	frysk-0.4-jnixx-dont-emit-nested-classes.patch
Patch49:	frysk-0.4-49-elf-newehdr-null.patch
Patch50:	frysk-0.4-50-autoconf-2-70-fixes.patch
Patch51:	frysk-0.4-51-debugedit-path.patch
Patch52:	frysk-0.4-52-libunwind-tests.patch

Patch100:	frysk-0.4-aclocaljavac.patch
Patch101:	frysk-0.4-cxx-scope.patch

# Do not push these upstream
Patch1003:	frysk-0.4-nogtkwerror.patch

# Use installed elfutils
Patch666:	frysk-0.4-sodwfl.patch

BuildRequires:	gcc-c++
BuildRequires:	java-devel
BuildRequires:	junit >= 3.8.1
BuildRequires:	antlr-tool >= 2.7.4
BuildRequires:	xmlto
BuildRequires:	sharutils
BuildRequires:	transfig >= 3.2.0
BuildRequires:	audit-libs-devel
BuildRequires:	autoconf automake libtool
# Some scripts run during the build use python
BuildRequires:	python3
BuildRequires:	elfutils-devel >= 0.151
BuildRequires:	jline2
BuildRequires:	debugedit

# it seems java requires explict runtime requires!?!?
Requires: junit
Requires: antlr-tool
Requires: jline2

%if %{enable_gnome}
BuildRequires:	jdom >= 1.0
BuildRequires:	glib-java >= 0.2.6
BuildRequires:	cairo-java-devel >= 1.0.3
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	gtk2-devel >= 2.8.0
BuildRequires:	libgtk-java-devel >= 2.8.7-6
BuildRequires:	libvte-java-devel >= 0.12.0
BuildRequires:	libglade-java-devel >= 2.12.3
BuildRequires:	libglade2-devel >= 2.5.1
BuildRequires:	vte-devel >= 0.12.1
BuildRequires:	gnome-python2-gconf
%endif
BuildRequires: make


# Bug #305611: PPC Build problems with libunwind
# Bug #416961: ALPHA not supported by frysk and libunwind.
# Bug #467970: SPARC/SPARC64 not supported by frysk and libunwind.
# Bug #467971: ARM not supported by frysk.
# Bug #506961: S390(X) not supported by frysk and libunwind.
# Bug #2104040: native frysk depends on to be removed i686 java-openjdk packages
ExclusiveArch: x86_64 ppc64

# We do not want to build a ``cross-debugging version'' i686->i386;
# libunwind build would get confused by this.  Override the cmd-line
# --target option:
%ifarch %{ix86}
%define _target_cpu %{_host_cpu}
%endif

%description
Frysk is an execution-analysis technology implemented using native
Java and C++.  It is aimed at providing developers and sysadmins with
the ability to both examine and analyze running multi-host,
multi-process, multi-threaded systems.  Frysk allows the monitoring of
running processes and threads, of locking primitives and will also
expose deadlocks, gather data and debug any given process in the
system.

%if %{enable_devel}
%package devel
Summary:	The development part of Frysk
Requires:	%{name} = %{version}-%{release}
%endif
%if %{enable_gnome}
Requires:	python2-dogtail >= 0.5.2
# Needed by "dogtail-run-headless -n":
Requires:	metacity
Requires:	python2
%endif

%if %{enable_devel}
%description devel
Frysk is an execution-analysis technology implemented using native
Java and C++.  It is aimed at providing developers and sysadmins with
the ability to both examine and analyze running multi-host,
multi-process, multi-threaded systems.  Frysk allows the monitoring of
running processes and threads, of locking primitives and will also
expose deadlocks, gather data and debug any given process in the
system.

This package contains the development components of Frysk.
%endif

%if %{enable_gnome}
%package gnome
Summary:	The GNOME front-end of Frysk
Requires:	%{name} = %{version}-%{release}
Requires:	libgconf-java
Requires:	libglade-java >= 2.12.5
Requires:	libvte-java >= 0.12.0

%description gnome
Frysk is an execution-analysis technology implemented using native
Java and C++.  It is aimed at providing developers and sysadmins with
the ability to both examine and analyze running multi-host,
multi-process, multi-threaded systems.  Frysk allows the monitoring of
running processes and threads, of locking primitives and will also
expose deadlocks, gather data and debug any given process in the
system.

This package contains the GNOME front end for Frysk.
%endif

%prep

%setup -q -n %{name}-%{version}
pwd

%patch -P0 -p1 -z .head

%patch -P1 -p1 -z .bash-dollar-star
%patch -P2 -p1 -z .strayelsif
%patch -P3 -p1 -z .fdebugrpm
%patch -P4 -p1 -z .mktlwidgetdir
%patch -P5 -p1 -z .gcc-warnings
%patch -P6 -p1 -z .funitexitman
mv frysk-core/frysk/pkglibdir/FunitSimpleInterfaceTest.java frysk-core/frysk/pkglibdir/FunitSimpleInterfaceMain.java
%patch -P7 -p1 -z .mvtesttomain -F 1
mv frysk-core/frysk/util/ProcStopUtil.java frysk-core/frysk/util/TaskStopUtil.java
%patch -P8 -p1 -z .taskstoputil -F 3
%patch -P9 -p1 -z .publictestbedsymtab
%patch -P10 -p1 -z .noelfmem
%patch -P11 -p1 -z .gccjint
%patch -P12 -p1 -z .taskstoperr
%patch -P13 -p1 -z .lostfork
%patch -P14 -p1 -z .nooptimize
%patch -P15 -p1 -z .skipdecl
%patch -P16 -p1 -z .flushstat
%patch -P17 -p1 -z .ftrace
%patch -P18 -p1 -z .usererrno
%patch -P19 -p1 -z .configure-enable-gnome
%patch -P20 -p1 -z .bin-antlr

%if %{fedora}0 >= 130
%patch -P100 -p1 -z .aclocaljavac
%endif

%if %{enable_gnome}
# don't apply - leaves default as build gnome
%else
%patch -P101 -p1 -z .configure-enable-gnome
%endif

%if %{enable_devel}
# don't apply - leaves devel package installed
%else
%patch -P21 -p1 -z .nopkglibdir
%endif

%patch -P1003 -p1 -z .nogtkwerror

%patch -P666 -p1 -z .sodwfl
rm -rf frysk-imports/elfutils

%if %{enable_gnome}
# don't apply, leave jdom around
%else
%patch -P22 -p1 -z .no-jdom
rm -rf frysk-core/frysk/dom
rm -rf frysk-core/frysk/rt/LineXXX.java
%endif

%patch -P23 -p1 -z .missing-javah-cni-built
%patch -P24 -p1 -z .jni
%patch -P25 -p1 -z .awk-gensub
%patch -P26 -p1 -z .pic-asm
%patch -P27 -p1 -z .per-thread-java-id
%patch -P28 -p1 -z .unwind-global-id
%patch -P29 -p1 -z .use-installed-antlr
rm -rf frysk-imports/antlr
%patch -P30 -p1 -z .use-installed-junit
rm -rf frysk-imports/junit
%patch -P31 -p1 -z .jni-issameobject
%patch -P32 -p1 -z .switch-ecj-to-javac
%patch -P33 -p1 -z .use-installed-jline
rm -rf frysk-imports/jline
# automake doesn't like old names
mv frysk-imports/libunwind/configure.{in,ac}
%patch -P34 -p1 -z .libunwind-fstack
%patch -P35 -p1 -z .clone-cursor
%patch -P36 -p1 -z .fedpkg-lint-licence
%patch -P37 -p1 -z .fedpkg-lint-solib
%patch -P38 -p1 -z .gelf-newphdr
%patch -P39 -p1 -z .jnixx-signed-unsigned
%patch -P40 -p1 -z .check-p-not-status
%patch -P41 -p1 -z .python3
%patch -P42 -p1 -z .jline1-to-jline
%patch -P43 -p1 -z .disable-arch32-tests
%patch -P44 -p1 -z .steptester-indentation
%patch -P45 -p1 -z .gcc-fcommon
%patch -P46 -p1 -z .javac
%patch -P47 -p1 -z .jnixx-union-as-reserved-word
%patch -P48 -p1 -z .jnixx-dont-emit-nested-classes
%patch -P49 -p1 -z .49-elf-newehdr-null
%patch -P50 -p1 -z .50-autoconf-2-70-fixes
%patch -P51 -p1 -z .51-debugedit-path
%patch -P52 -p1 -z .52-libunwind-tests.patch

echo "%{version}-%{release}" > frysk-common/version.in

# don't try to build assembler test files
rm frysk-core/frysk/pkglibdir/*.S

./bootstrap.sh

%build 

uname -a
gcc --version
pwd
mkdir -p build
cd build

# double check xmlto
rpm -ql xmlto || :
ls -l /usr/bin/xmlto || :
# Capture the configure line
rm -f configure
echo '#!/bin/sh -x'			>> configure
echo 'exec ../$(basename $0) "$@"'	>> configure
chmod a+x configure

%configure \
	CFLAGS="$RPM_OPT_FLAGS" \
	CXXFLAGS="$RPM_OPT_FLAGS"

make %{?_smp_mflags}

%install

rm -rf %{buildroot}

# Workaround for bug #??:
mkdir -p $RPM_BUILD_ROOT/usr/share/frysk

pwd
cd build
make DESTDIR=$RPM_BUILD_ROOT install %{?_smp_mflags}

find $RPM_BUILD_ROOT

%if %{enable_gnome}
# Fix timestamp of a generated script:
touch -r \
  ../frysk-gui/frysk/gui/FryskGui.java-in \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/dogtail_scripts/frysk_suite.py
# ...and a few other ones:
for f in test2866.py test2985.py test3380.py; do
  touch -r \
    ../frysk-gui/frysk/gui/test/dogtail_scripts/$f \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/dogtail_scripts/$f
done
%endif

# some stray files.
%if %{enable_devel}
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/gen-type-funit-tests
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/ChangeLog
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/test-exe-x86.c.source
%else
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/test-sysroot
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}
# do not document uninstalled devel commands
rm -rf $RPM_BUILD_ROOT%{_mandir}/man8
%endif

# We are not yet ready to be in the menu:
%if %{enable_gnome}
echo "Hidden=true" >> $RPM_BUILD_ROOT%{_datadir}/applications/frysk.desktop
%endif

%if %{enable_devel}
# Remove duplicates; causes tools to complain.
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/funit-exec-alias
# Remove debuginfo; confuses elfutils.
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/funit-*-nodebug
%endif

%files

%defattr(-,root,root)

%doc frysk-common/COPYING frysk-common/EXCEPTION

%{_bindir}/fauxv
%{_bindir}/fcatch
%{_bindir}/fcore
%{_bindir}/fdebugdump
%{_bindir}/fdebuginfo
%{_bindir}/fdebugrpm
%{_bindir}/ferror
%{_bindir}/fexe
%{_bindir}/fhpd
%{_bindir}/fmaps
%{_bindir}/fstack
%{_bindir}/fstep
%{_bindir}/ftrace

%{_libdir}/%{name}/libfrysk-sys-jni.so
# See bug 211824 for why these are in lib and not /usr/share/java/*
%{_libdir}/%{name}/java/*.jar

%{_mandir}/man1/fauxv.1.gz
%{_mandir}/man1/fcatch.1.gz
%{_mandir}/man1/fcore.1.gz
%{_mandir}/man1/fdebugdump.1.gz
%{_mandir}/man1/fdebuginfo.1.gz
%{_mandir}/man1/fdebugrpm.1.gz
%{_mandir}/man1/ferror.1.gz
%{_mandir}/man1/fexe.1.gz
%{_mandir}/man1/fhpd.1.gz
%{_mandir}/man1/fmaps.1.gz
%{_mandir}/man1/fstack.1.gz
%{_mandir}/man1/fstep.1.gz
%{_mandir}/man1/ftrace.1.gz
%{_mandir}/man7/frysk.7.gz

%if %{enable_devel}
%files devel

%defattr(-,root,root)

%{_libdir}/libfrysk-junit.so

%dir %{_libdir}/%{name}
%{_libdir}/%{name}/FunitSimpleInterfaceMain
%{_libdir}/%{name}/fsystest
%{_libdir}/%{name}/funit*
%{_libdir}/%{name}/hpd-c
%{_libdir}/%{name}/sys-tests
%{_libdir}/%{name}/test-sysroot
%{_libdir}/%{name}/test1
%{_datadir}/%{name}/helloworld.o
%{_datadir}/%{name}/test_looper.xml
%{_datadir}/%{name}/test-core-x86
%{_datadir}/%{name}/test-core-x8664
%{_datadir}/%{name}/test-exe-x86
%{_datadir}/%{name}/libtest.so

%{_mandir}/man8/*
%endif

%if %{enable_gnome}
%{_libdir}/libfrysk-jdom.so
%{_libdir}/%{name}/ftail
%{_datadir}/%{name}/dogtail_scripts
%endif

%if %{enable_gnome}
%files gnome

%defattr(-,root,root)

%{_bindir}/frysk

%{_libdir}/libEggTrayIcon.so
%{_libdir}/libfrysk-ftk.so
%{_libdir}/libfrysk-gtk.so
%{_libdir}/libfrysk-gui.so
%{_libdir}/libftk*.so

%{_datadir}/%{name}/glade
%{_datadir}/%{name}/images

%{_datadir}/%{name}/messages.properties
%{_datadir}/applications/frysk.desktop
%{_datadir}/pixmaps/fryskTrayIcon48.png

%dir %{_datadir}/gnome/help/%{name}
%{_datadir}/gnome/help/%{name}/*

%{_mandir}/man1/frysk.1.gz

%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-96
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-95
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0.4-94
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-93
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-92
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-91
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 15 2023 Andrew Cagney <cagney@fedoraproject.org> - 0.4-90
- drop hack mangling _FORTIFY_SOURCE; fix 2161322

* Mon Apr 3 2023 Andrew Cagney <cagney@fedoraproject.org> - 0.4-89
- update frysk licence

* Thu Mar 9 2023 Andrew Cagney <cagney@fedoraproject.org> - 0.4-88
- update getopt and libunwind sub licences

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-87
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 29 2022 Andrew Cagney <cagney@fedoraproject.org> - 0.4-86
- don't build libunwind tests; frysk-0.4-52-libunwind-tests.patch

* Thu Jul 21 2022 Andrew Cagney <cagney@fedoraproject.org> - 0.4-85
- ding dong the 32-bit Java is dead; #2104040

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-84
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.4-83
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-82
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 4 2021 Andrew Cagney <cagney@fedoraproject.org> - 0.4-81
- require debugedit; fix hardwired path

* Wed Aug 4 2021 Andrew Cagney <cagney@fedoraproject.org> - 0.4-80
- Allow autoconf 2.69

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 12 2021 Andrew Cagney <cagney@fedoraproject.org> - 0.4-78
- autoconf 2.70

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Jerry James <loganjerry@gmail.com> - 0.4-76
- Depend on jline2, not jline

* Fri Dec 11 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-75
- fix check of elf_newehdr()'s return value

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Andrew Cagney <cagney@fedoraproject.org> - 0.4-73
- 'union' onto 'union$' - frysk-0.4-jnixx-union-as-reserved-word.patch
- omit nested local classes - frysk-0.4-jnixx-dont-emit-nested-classes.patch

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.4-72
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jun 9 2020 Andrew Cagney <cagney@fedoraproject.org> - 0.4-71
- drop -source 1.4 -- frysk-0.4-javac.patch

* Tue Jan 28 2020 Andrew Cagney <cagney@fedoraproject.org> - 0.4-70
- pacify gcc -fcommon

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Andrew Cagney <cagney@fedoraproject.org> - 0.4-68
- make runtime java dependencies explicit - found by Magnus Glantz
- depend on antlr-tool instead of antlr

* Thu Sep 5 2019 Andrew Cagney <cagney@fedoraproject.org> - 0.4-67
- Updates for jline(2)
- Pacify GCC - fix some indentation
- Default to no 32-bit tests (drop config's --disable-arch32-tests)

* Thu Sep 5 2019 Andrew Cagney <cagney@fedoraproject.org> - 0.4-66
- Depend on jline, not jline1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Andrew Cagney <cagney@fedoraproject.org> - 0.4-64
- Update README cribsheet

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Andrew Cagney <cagney@fedoaproject.org> - 0.4-62
- Deal with python 3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4-60
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Andrew Cagney <cagney@fedoraproject.org> - 0.4-56
- fix warnings/errors from latest compilers

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 6 2017 Andrew Cagney <cagney@fedoraproject.org> - 0.4-54
- work around evolving gelf_newphdr() interface

* Tue Apr 19 2016 Andrew Cagney <cagney@fedoraproject.org> - 0.4-53
- fix some fedpkg lint problems
- add frysk-0.4-fedpkg-lint-licence.patch
- add frysk-0.4-fedpkg-lint-solib.patch
- use Fedora approved name for libunwind licence

* Tue Apr 19 2016 Andrew Cagney <cagney@fedoraproject.org> - 0.4-52
- clone the jobject when cloning the cursor - frysk-0.4-clone-cursor.patch

* Mon Apr 18 2016 Andrew Cagney <cagney@fedoraproject.org> - 0.4-51
- better handle prelink - frysk-0.4-libunwind-fstack.patch

* Tue Apr 12 2016 Andrew Cagney <cagney@fedoraproject.org> - 0.4-50
- do not ship a local copy of junit.jar - frysk-0.4-use-installed-junit.patch
- do not ship a local copy of jline.jar - frysk-0.4-use-installed-jline.patch
- update licence list - drop unbundled code
- remove long dead configurations
- in JNIXX operator== use IsSameObject - frysk-0.4-jni-issameobject.patch
- use javac - frysk-0.4-switch-ecj-to-javac.patch

* Tue Apr 12 2016 Andrew Cagney <cagney@fedoraproject.org> - 0.4-49
- do not ship a local copy of antlr.jar - frysk-0.4-use-installed-antlr.patch

* Tue Apr 12 2016 Andrew Cagney <cagney@fedoraproject.org> - 0.4-48
- Use a global java ID in libunwind - frysk-0.4-unwind-global-id.patch

* Wed Apr 06 2016 Andrew Cagney <cagney@fedoraproject.org> - 0.4-47
- Use java ID for local thread - frysk-0.4-per-thread-java-id.patch

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Andrew Cagney <cagney@fedoraproject.org> - 0.4.45
- Fix AWK gensub parameter 3; new warning about it is being printed to
  STDOUT instead of STDERR and, hence, ends up in generated Java files
- Don't build assembler test files as conflicts with building PIC.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 21 2014 Andrew Cagney <cagney@fedoraproject.org> - 0.4-42
- Switch from the CNI to the JNI native bindings
- Build using Java/ECJ removing dependency on gcc-java
- Added patch frysk-0.4-jni.patch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Andrew Cagney <cagney@fedoraproject.org> - 0.4-39
- Don't build jdom, no longer needed
- Force the generation of some cni headers
- Pacify automake by giving config files names it likes

* Sat Jan 26 2013 Andrew Cagney <cagney@fedoraproject.org> - 0.4-38
- Rebuild unchanged against new gcj so it picks up libgcj.so.14.

* Tue Aug 7 2012 Andrew Cagney <cagney@fedoraproject.org> - 0.4-37
- Add java-1.5.0-gcj to BuildRequires list.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 11 2012 Andrew Cagney <cagney@fedoraproject.org> - 0.4-35
- Clean up pkglibdir and pkglibdata dir, devel package not needed.

* Sat Jan 21 2012 Andrew Cagney <cagney@fedoraproject.org> - 0.4-34
- Add frysk-0.4-configure-enable-gnome.patch as no vte/java bindings.
- Use installed antlr - frysk-0.4-bin-antlr.patch
- Fix scope warning from latest c++ - frysk-04-cxx-scope.patch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4-32
- Rebuild for new libpng

* Fri Mar 11 2011 Dan Horák <dan[at]danny.cz> - 0.4-31
- switch to ExclusiveArch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 6 2011 Andrew Cagney <cagney [at] fedoraproject [dot] org> - 0.4-29
- enable use of host's elfutils when f15; final bug appears fixed
- fix unused rerrno variable; frysk-04-usererrno.patch

* Tue Sep 28 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4-28
- rebuild, fix lzma linking

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.4-27
- recompiling .py files against Python 2.7 (rhbz#623298)

* Tue Mar 30 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-26
- during an exec, flush the cached "stat", don't re-read it -
  frysk-0.4-flushstat.patch
- document ftrace's -f/-follow option, update tests -
  frysk-0.4-ftrace.patch

* Tue Mar 30 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-25
- for stack tests use a pragma to reduce optimization level -
  frysk-0.4-nooptimize
- prefer a variable definition over its declaration -
  frysk-0.4-skipdecl

* Tue Mar 30 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-24
- for fcatch et.al. don't exit when outstanding child events -
  frysk-0.4-lostfork.patch

* Mon Mar 29 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-23
- for fexe et.al., exit cleanly when an error -
  frysk-0.4-taskstoperr.patch

* Mon Mar 29 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-22
- work around gcc bug where MAX_INT+1 isn't -ve -
  frsyk-0.4-gccjint.patch

* Thu Mar 25 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-21
- Merge 0.145 elfutils and local fixes.  This is Plan B, Plan A was to
  use the installed elfutils.

* Thu Mar 25 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-20
- Don't use elf_from_remote_memory - frysk-0.4-noelfmem.patch.

* Thu Mar 25 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-19
- Make TestbedSymTab public - frysk-0.4-publictestbedsymtab.patch.

* Wed Mar 24 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-18
- Update fhpd's watchpoints, ftrace, etc from head - frysk-0.4-head.patch

* Wed Mar 24 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-17
- In fstack et.al., don't exit until all processes have been detached
  - frysk-0.4-taskstoputil.patch.

* Wed Mar 24 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-16
- Re-organize local patches, blat the version.

* Wed Mar 17 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-15
- Fix manpage typos - frysk-0.4-manpages.patch

* Wed Mar 17 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-14
- Update to latest autotools - frysk-0.4-aclocaljavac.patch,
  frysk-0.4-elfutilsdeps.patch
- Add missing include sys/stat.h - frysk-0.4-elfutilsfstat.patch
- Create missing dir - frysk-0.4-mktlwidgetdir.patch

* Mon Mar 15 2010 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-13
- Fix debuginforpm's sed line (from  Stephen Tweedie).

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.4-12
- rebuilt with new audit

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-10
- Add frysk-0.4-fix-duplicates.patch to address duplicated install
  problems.

* Fri Jun 19 2009 Andrew Cagney <cagney [at] fedoraproject.org> - 0.4-9
- Add sparc64 and s390x to ExcludeArch.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 9 2009 Andrew Cagney <cagney [at] fedoraproject org> - 0.4-7
- Add frysk-0.4-gcc-warnings.patch; fix warnings from newer gcc.
- Delete funit-stacks-nodebug and funit-exec-alias; confuses install.

* Sun Feb 08 2009 Andrew Cagney <cagney [at] fedoraproject org> - 0.4-6
- Add frysk-0.4-batch-dollar-star.patch; avoid empty "$*" and "$@" in
  shell scripts (bash bug?).

* Sun Feb 08 2009 Alex Lancaster <alexlan[AT] fedoraproject org> - 0.4-5
- Rebuild for new GCC 4.4 to fix broken deps

* Tue Dec 23 2008 Andrew Cagney <andrew.cagney@gmail.com> - 0.4-4
- Improve summaries.

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.4-3
- Rebuild for Python 2.6

* Mon Oct 27 2008 Andrew Cagney <andrew.cagney@gmail.com> - 0.4-2
- drop EPL from licence list; cdtparser deleted
- re-enable SMP make
- disable -Werror flag to gcj

* Mon Oct 20 2008 Andrew Cagney <andrew.cagney@gmail.com> - 0.4-1
- add sparc and arm to ExcludeArch.

* Mon Jun 9 2008 Sami Wagiaalla <swagiaal@rdhat.com> - 0.4-0
- import frysk-0.4.tar.bz2
- removed Patch7: frysk-0.0.1.2008.02.29.rh1-jboolean-array.patch
- removed Patch8: frysk-0.0.1.2008.02.29.rh1-asm-includes.patch
- removed Patch10: frysk-0.0.1.2008.03.19.rh1-fparser8.patch
- removed Patch11: frysk-0.2.1-ppc-build.patch
- Added fdebugdump files to files list
- Added libfrysk-sys-jni.so to file list.
- remove fparser from executable list.
- remove test_main_looper from file list.
- remove libfrysk-cdtparser from file list.

* Fri Apr 4 2008 Andrew Cagney <cagney@rdhat.com> - 0.2.1-2
- add patch11, frysk-0.2.1-ppc-build.patch.

* Fri Apr 4 2008 Andrew Cagney <cagney@rdhat.com> - 0.2.1-1
- re-instate patch10, install fparser's manpage in man8
- drop patch6, frysk-0.0.1.2008.01.18.rh1-elfutils-werror.patch.

* Fri Apr 4 2008 Andrew Cagney <cagney@rdhat.com> - 0.2.1-0
- import frysk-0.2.1.tar.bz2
- drop patch9, frysk-elfutils-src.patch.
- drop patch10, install fparser's manpage in man8

* Tue Mar 25 2008 Andrew Cagney <cagney@rdhat.com> - 0.0.1.2008.03.19.rh1-1
- import 0.0.1.2008.03.19.rh1 (35c076f3436b95a116cba33f52e0c9a592607dfa)
- move fparser to pkglibdir.
- add ferror to frysk's file list.
- add FunitSimpleInterfaceTest to frysk-devel's file list.
- add frysk.7 to frysk's file list.
- move frysk.1 to frysk-gnome's file list
- add Patch9 frysk-elfutils-crc.patch, work-around broken CRC check.
- add Patch10, install fparser's manpage in man8

* Tue Mar 11 2008 Sami Wagiaalla <swagiaal@rdhat.com> - 0.0.1.2008.03.11-2
- Added statements to check for xmlto.

* Tue Mar 11 2008 Sami Wagiaalla <swagiaal@rdhat.com> - 0.0.1.2008.03.11-1
- Import 0.0.1.2008.03.11 (84bcf09e5a329252d81e853e49f0cf1449f937c2)

* Tue Mar 11 2008 Sami Wagiaalla <swagiaal@rdhat.com> - 0.0.1.2008.02.29.rh1-2
- Update releease number
- added frysk-0.0.1.2008.02.29.rh1-asm-includes.patch
- added frysk-0.0.1.2008.02.29.rh1-jboolean-array.patch

* Fri Feb 29 2008 Sami Wagiaalla <swagiaal@rdhat.com> - 0.0.1.2008.02.29.rh1-1
- Import frysk-0.0.1.2008.02.29.rh1 (148d1359cf791171d7f346d4fca35c1fc36aca8c)
- Remove BuildRequires: libgconf-java-devel
- Remove Patch4 (frysk-0.0.1.2008.01.18.rh1-no-sysroot.patch)
- Remove Patch5 (frysk-0.0.1.2008.01.18.rh1-line-npe.patch)

* Tue Feb 5 2008 Andrew Cagney <cagney@redhat.com> - 0.0.1.2008.01.18.rh1-3
- Add frysk-0.0.1.2008.01.18.rh1-elfutils-werror.patch to fix elfutils
  errors.

* Mon Feb  4 2008 Stepan Kasal <skasal@redhat.com> - 0.0.1.2008.01.18.rh1-2
- rebuild against rebuilt java-gnome

* Sun Jan 20 2008 Andrew Cagney <cagney@redhat.com> - 0.0.1.2008.01.18.rh1-1
- Import frysk-0.0.1.2008.01.18.rh1 (4cff0daa2996b28274985fa4674160f15e5fd9e2)
- Delete run_make_check code.
- Add patch4, frysk-0.0.1.2008.01.18.rh1-no-sysroot.patch to not build
  sysroot tests.
- Add patch5, frysk-0.0.1.2008.01.18.rh1-line-npe.patch to prevent NPE
  in source window.
- Enable ppc64 build; disable alpha build (bug 416961).
- Move dogtail testing requirements to devel package.
- Delete stray ChangeLog, gen-type-funit-tests, and
  test-exe-x86.c.source files.

* Wed Oct 17 2007 Andrew Cagney <cagney@redhat.com> - 0.0.1.2007.10.17-1
- Import frysk-0.0.1.2007.10.17.
- Remove hack disabling glade check.

* Mon Sep 24 2007 Andrew Cagney <cagney@redhat.com> - 0.0.1.2007.09.24-2
- Install frysk.desktop; but with Hidden=true.
- Sort files list.
- Remove trailing period from summaries.
- Replace ExclusiveArch with ExcludeArch of ppc and ppc64; bug 305611.

* Mon Sep 24 2007 Andrew Cagney <cagney@redhat.com> - 0.0.1.2007.09.24-1
- Update files list.
- Fix path to dogtail_scripts.
- Fix touch paths to allow for build sub-directory.
- Import frysk-0.0.1.2007.09.24.tar.bz2.
- Remove frysk-20060922-a-cast.patch
- Remove frysk-xfail-2130.patch.
- Run bootstrap.sh over source tree.
- Add autoconf, automake, and libtool to BuildRequires.
- Remove binutils-devel from BuildRequires.
- Build in separate sub-directory.
- Do not force JV_SCAN into the build environment.
- Update Licence.
- Change BuildRoot to prefered fedora format.
- Expand Summary to mention debugging.

* Tue Mar 13 2007 Stepan Kasal <skasal@redhat.com> - 0.0.1.2007.03.13.rh1-1
- New upstream version, adapt the file list.
- Remove frysk-no-dejagnu.patch.
- configure --disable-werror

* Tue Feb  6 2007 Stepan Kasal <skasal@redhat.com> - 0.0.1.2007.02.07.rh1-1
- New upstream version.
- Add Gnome help files, test_looper.xml, and test_main_looper to the file
  lists.
- Temporarily:
  switch off /usr/share/frysk/test, current tarball does not install it;
  switch off ppc64 build, frysk-imports/include/frysk-asm.h ain't ready.

* Tue Feb  6 2007 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.22.rh1-8
- Do not delete the .desktop file, nove it to docdir.
- Related: #211200

* Tue Jan 30 2007 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.22.rh1-7
- Move the requirement for libgconf-java to subpackage frysk-gnome.
- Resolves: #225401.

* Thu Jan 25 2007 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.22.rh1-6
- Fix the mistake which I made while backporting the TestFStack patch.
- Related: #224248

* Wed Jan 24 2007 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.22.rh1-5
- Add frysk-20070106-TestFStack.patch frysk-20070124-libunwind.patch .
- Resolves: #224248

* Wed Jan 17 2007 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.22.rh1-4
- Second iteration to make section 8 man pages platform-independent.
- Resolves: #222468

* Wed Jan 17 2007 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.22.rh1-3
- Make the contents of section 8 man pages platform-independent.
- Resolves: #222468
- Move section 8 man pages to frysk-devel, where the corresponding utilities
  reside.

* Wed Jan 17 2007 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.22.rh1-2
- Fix time stamps of installed *.py files, which ...
- Resolves: #222468

* Tue Dec 19 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.22.rh1-1
- New upstream version.
- libexecdir -> libdir and other file list updates
- Remove frysk-arch32-disable.patch, use --disable-arch32-tests instead.
- Add frysk-no-dejagnu.patch and create $RPM_BUILD_ROOT${pkgdatadir},
  to work around a bug in install-dejagnu-testsuite-local rule.
- Resolves: #218819

* Tue Dec 19 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.01.rh1-4
- Add frysk-20061201-i386_is_not_64bit.patch
- Related: #218835

* Tue Dec 19 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.01.rh1-3
- Use libexecdir with the old version.
- Related: #218835

* Mon Dec 18 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.01.rh1-2
- Fix typo in the previous chlog entry.
- Resolves: #211200

* Mon Dec 18 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.01.rh1-2
- Do not install the .desktop file.
- Resolves: #211200
- Split to frysk, frysk-devel, and frysk-gnome; move the requires for gui
  java-gnome libraries to frysk-gnome.
- Resolves: #218835

* Fri Dec  1 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.01.rh1-2
- Related: #211775
- The ppc64 build works again.

* Fri Dec  1 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.12.01.rh1-1
- New upstream version.
- Resolves: #211288.

* Thu Nov 30 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.11.30.rh1-1
- New upstream version.
- The stamp file for glade files has been renamed.
- Disable ppc64 build.

* Mon Oct 30 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.10.30.rh1-1
- New upstream version.
- Do not apply frysk-xfail-2130.patch, we do not run make check anyway.
- Do not list the binaries in the file list; use `f*'.

* Mon Oct 23 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.10.23.rh1-1
- New upstream version.
- Do not pack the jars; they cause multilib conflicts.
- Add /usr/bin/fcrash to the file list.

* Tue Oct 17 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.10.17.rh1-1
- New upstream version.

* Fri Oct 13 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.10.13.rh1-1 
- New upstream version.

* Wed Oct 11 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.10.11.rh1-1
- New upstream version.

* Mon Oct  2 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.10.02.rh1-1
- New upstream version.

* Tue Sep 26 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.09.22.rh1-1
- New upstream version.
- Refresh frysk-xfail-2130.patch.
- Add frysk-20060922-a-cast.patch to fix a warning.
- Add fstack to the file list.

* Fri Sep 15 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.09.15.rh1-2
- BuildRequire binutils-devel.

* Fri Sep 15 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.09.15.rh1-1
- New upstream version.
- Make sure we are not building a ``cross-debugging'' libunwind on i686.

* Tue Sep 12 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.09.08.rh1-2
- Do not require dogtail on FC-5; it's not available there.

* Mon Sep 11 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.09.08.rh1-1
- New upstream version.

* Sat Sep  2 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.08.30.rh1-2
- Tried to build on 32bit ppc, but it does not work yet.

* Tue Aug 29 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.08.30.rh1-1
- New upstream version.
- Removed xorg-x11-xinit from BuildRequires, dogtail was fixed to require it.
- Build also on ppc64.

* Mon Aug 28 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.08.28.rh1-1
- New upstream version.
- Remove Patch1, the code now contains a real fix for bug #203902.

* Fri Aug 25 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.08.24.rh1-3
- Patch1 for bug #203902.

* Fri Aug 25 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.08.24.rh1-2
- Comment out the %%check section temporarily.

* Thu Aug 24 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.08.24.rh1-1
- New upstream version.
- Add Requires: libgconf-java

* Tue Aug 22 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.08.22.rh1-1
- New upstream version.
- Add BuildRequires: gnome-python2-gconf, remove BuildRequires: ghostscript.
- Add `uname -a' to %%check.

* Wed Aug 16 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.08.16.rh1-1
- New upstream version.

* Tue Aug 15 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.08.15.rh1-1
- New upstream version.
- Require latest java-gnome.
- frysk-xfail-2130.patch: fails if building on an old kernel.

* Wed Aug  9 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.08.09.rh1-1
- New upstream version, incorporates both the patches.

* Wed Aug  2 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.07.25.rh1-4
- Add make check to %%check
- Add patches to disable failing tests.

* Wed Aug  2 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.07.25.rh1-3
- BuildRequires latest dogtail

* Fri Jul 28 2006 Phil Muldoon <pmuldoon@redhat.com> - 0.0.1.2006.07.25.rh1-3
- Add dogtail to BuildRequires 

* Tue Jul 25 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.07.25.rh1-2
- Add ftrace to the file list.

* Tue Jul 25 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.07.25.rh1-1
- New upstream version.

* Sat Jul 22 2006 Thomas Fitzsimmons <fitzsim@redhat.com> - 0.0.1.2006.07.18.rh1-2
- Bump release number. (dist-fc6-java)

* Tue Jul 18 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.07.18.rh1-1
- New upstream version, incorporates the previous two patches.

* Tue Jul 18 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.07.14.rh1-2
- Add two patches from Phil Muldoon:
  frysk-20060714-observer.patch -- continue even though an observer cannot be load
  frysk-20060714-timer.patch -- fix incorrect usage of a core timer

* Fri Jul 14 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.07.14.rh1-1
- New upstream version.

* Thu Jul 13 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.07.13.rh1-1
- New upstream version.

* Wed Jul 12 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.07.12.rh2-1
- New upstream version.

* Wed Jul 12 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.07.12.rh1-1
- New upstream version.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.0.1.2006.06.28.rh1-0.1
- rebuild

* Wed Jun 28 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.06.28.rh1-1
- Remove  BuildRequires:  autoconf automake

* Tue Jun 27 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.06.28.rh1-0
- Refresh the tarball.
- Remove the patches, they are all upstream now.
- BuildRequires: sharutils, instead of gmime.
- Do not remove the unwanted files, they should not be installed anymore.
- Do not hide the menu entry.
- Do not call ./bootstrap.sh.

* Fri Jun 16 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.06.15-3
- Add the non-intermediate hack.
- Remove more unwanted files.
- Add patch to link statically with libelf; remove elfutils libraries.

* Fri Jun 16 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.06.15-2
- Suppress warnings caused by _FORTIFY_SOURCE=2
- Remove unwanted files.

* Fri Jun 16 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.06.15-1
- Add BuildRequires: libgconf-java-devel
- Update frysk-unistd.patch

* Thu Jun 15 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.06.15-0
- Refresh the tarball.
- Patch to fix Elf.cxx on 64bit.
- Anoter patch required by new linux/unistd.h.
- Add BuildRequires: ghostscript

* Thu Jun 15 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.06.14-1
- Patch for new linux/unistd.h.
- Patch to avoid scanf("%%a[..]").

* Wed Jun 14 2006 Stepan Kasal <skasal@redhat.com> - 0.0.1.2006.06.14-0
- New upstream version.
- Add BuildRequires: libglade2-devel >= 2.5.1
- Refresh other BuildRequires.
- Replace the noxmltest.patch patch by two touch commands.
- Add BuildRequires: autoconf automake, BuildRequires: gcc-java >= 4.1.1

* Thu May 18 2006 Stepan Kasal <skasal@redhat.com>    - 0.0.1.2006.02.19.rh2-0.FC5.3
- Add gmime to BuildRequires.

* Fri Mar 03 2006 Andrew Cagney <cagney@redhat.de> 0.0.1.2006.02.19.rh2-0.FC5.2
- Add Hidden=true to frysk.desktop file; from halfline; with fixes.
- Disable xml check in frysk-gui/.

* Wed Mar 01 2006 Andrew Cagney <cagney@redhat.de> 0.0.1.2006.02.19.rh2-0.FC5.1
- Add dependencies on latest Java-GNOME bindings.

* Wed Mar 01 2006 Andrew Cagney <cagney@redhat.de> 0.0.1.2006.02.19.rh2-0.FC5.0
- Import frysk 0.0.1.2006.02.19.rh2; works around bug #180637.
- Enable x86_64, update *-java BuildRequires; fix bug #183538.

* Tue Feb 21 2006 Karsten Hopp <karsten@redhat.de> 0.0.1.2006.02.19.rh1-0.FC5.1
- BuildRequires: xmlto

* Mon Feb 20 2006 Andrew Cagney <cagney@redhat.com> 0.0.1.2006.02.19.rh1-0.FC5.0
- Import frysk 0.0.1.2006.02.19.rh1 -- snapshot from middle of that day.

* Sat Feb 18 2006 Andrew Cagney <cagney@redhat.com> 0.0.1.2006.02.12-0.FC5.1
- Remove eclipse-cdt >= 3.0.0 from BuildRequires.  From Wu Zhou
  woodzltc@ibm.

* Sun Feb 12 2006 Andrew Cagney <cagney@redhat.com> 0.0.1.2006.02.12-0.FC5.0
- Import frysk 0.0.1.2006.02.12.

* Thu Feb 09 2006 Adam Jocksch <ajocksch@redhat.com> 0.0.1.2006.02.09-0.FC5.0
- Removed ftrace from %%files and added libexedir files and man pages.
- Imported new frysk tarball, 

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.0.1.2006.01.22-0.FC5.1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Feb 06 2006 Adam Jocksch <ajocksch@redhat.com> 0.0.1.2006.01.22-0.FC5.1
- Bumped version, rebuilt.

* Mon Jan 23 2006 Andrew Cagney <cagney@redhat.com> 0.0.1.2006.01.22-0.FC4.0
- Simplify .spec file (remove unused macro definitions).
- Import frysk 0.0.1.2006.01.22.
- Update -files; adding frysk.desktop and fryskTrayIcon48.png.

* Thu Dec 22 2005 Andrew Cagney <cagney@redhat.com> 0.0.1.2005.12.14.15.12-0.FC4.1
- Import frysk-0.0.1.2005.12.14.15.12 rpm.
- Drop build dependency java-1.4.2-gcj-compat-devel
- Apply Patch003, frysk-makefileam.patch.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 16  2005 Igor Foox <ifoox@redhat.com> 0.0.0.20051116-0.3
- Added jars under /usr/share/java to distribution.

* Wed Nov 16  2005 Igor Foox <ifoox@redhat.com> 0.0.0.20051116-0.1
- Update source.

* Wed Nov 16  2005 Igor Foox <ifoox@redhat.com> 0.0.0.20051114-0.3
- Removed runtime dependency for eclipse-cdt, changed buildtime eclipse-cdt dependency to 3.0.0.

* Wed Nov 16  2005 Igor Foox <ifoox@redhat.com> 0.0.0.20051114-0.2
- Changed dependency on frysk-cdtparser to eclipse-cdt (it was somehow magically reversed).

* Mon Nov 14  2005 Igor Foox <ifoox@redhat.com> 0.0.0.20051114-0.1
- Removed smp flags.

* Thu Nov 10  2005 Igor Foox <ifoox@redhat.com> 0.0.0.20051109-0.3
- Update source.

* Thu Nov 10  2005 Igor Foox <ifoox@redhat.com> 0.0.0.20051109-0.2
- Added ExclusiveArch for i386.

* Thu Nov 10  2005 Igor Foox <ifoox@redhat.com> 0.0.0.20051109-0.1
- Updated source, changed cdtparser dependency to eclipse-cdt. Added build
restriction to i386. Added %%{?_smp_flags} to make command.

* Fri Oct 28  2005 Igor Foox <ifoox@redhat.com> 0.0-2
- Validated all Requires and BuildRequires clauses, fixed some of them.
- Fixed bug with libdir detection based on architecture.

* Wed Oct 26  2005 Igor Foox <ifoox@redhat.com> 0.0-1
- Birth.
