%global ver		13.0.50
%global snap		20220502
%global gnulibsnap	20220627

#	Turn off the brp-python-bytecompile automagic
%global	_python_bytecompile_extra	0


#	Git snapshots are produced as follows:
#
#	git clone --recursive git://sourceware.org/git/insight.git
#	cd insight
#	autoconf
#	configure
#	(cd bundle; ./src-release.sh -x insight)
#
#	Tarball is then found at bundle/insight-%<ver>.%<snap>.tar.xz

Name:		insight
Version:	%(echo %{ver} | tr - .)%{?snap:.%{snap}}
Release:	21%{?dist}
Summary:	Graphical debugger based on GDB
# Automatically converted from old format: GPLv3+ and GPLv3+ with exceptions and GPLv2+ and GPLv2+ with exceptions and GPL+ and LGPLv2+ and BSD and Public Domain and GFDL - review is highly recommended.
License:	GPL-3.0-or-later AND LicenseRef-Callaway-GPLv3+-with-exceptions AND GPL-2.0-or-later AND LicenseRef-Callaway-GPLv2+-with-exceptions AND GPL-1.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-GFDL
Url:		https://www.sourceware.org/insight/
# Source0:	ftp://sourceware.org/pub/insight/releases/insight-%<ver>.tar.bz2
Source0:	insight-%{version}.tar.xz
Source1:	insight.1
Requires:	iwidgets
Requires:	xterm
Provides:	bundled(binutils) = %{snap}
Provides:	bundled(gnulib) = %{gnulibsnap}
Provides:	bundled(libiberty) = %{snap}
Provides:	bundled(md5-gcc) = %{snap}
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	iwidgets
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel >= 6.0
BuildRequires:	expat-devel
BuildRequires:	gmp-devel
BuildRequires:	python3-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	autogen
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	texinfo-tex
BuildRequires:	perl-podlators
BuildRequires:	libbabeltrace-devel
#	For C++ pretty printers.
BuildRequires:	libstdc++

BuildRequires:	itcl-devel >= 3.3
BuildRequires:	itk-devel >= 3.3

%ifarch %{ix86} x86_64
%global have_libipt	1
BuildRequires:	libipt-devel
%endif
BuildRequires: make

#	Insight patches.

Patch1:		insight-11.0.50-relocate.patch

#	Some patches from gdb. See gdb spec file for info.

Patch101:	insight-13.0-gdb-6.3-gstack-20050411.patch
Patch102:	gdb-6.5-bz185337-resolve-tls-without-debuginfo-v2.patch
Patch103:	insight-13.0-gdb-6.6-buildid-locate.patch
Patch104:	gdb-6.6-buildid-locate-solib-missing-ids.patch
Patch105:	insight-13.0-gdb-6.6-buildid-locate-rpm.patch
Patch106:	gdb-6.6-buildid-locate-rpm-librpm-workaround.patch
Patch107:	gdb-6.6-buildid-locate-misleading-warning-missing-debuginfo-rhbz981154.patch
Patch108:	gdb-fedora-libncursesw.patch
Patch109:	gdb-6.6-buildid-locate-rpm-scl.patch
Patch110:	gdb-container-rh-pkg.patch
Patch111:	gdb-linux_perf-bundle.patch
Patch112:	gdb-libexec-add-index.patch

#	Additional patches.

Patch201:	insight-13.0-symtab_no_format_overflow.patch
Patch202:	insight-13.0-bfd-CVE-2022-4285,patch
Patch203:	insight-13.0-print-check-value.patch
Patch204:	insight-13.0-distutils.patch
Patch205:	insight-13.0-noselfmove.patch
Patch206:	insight-configure-c99.patch
Patch207:	insight-13.0-bfd-CVE-2023-1972.patch
Patch208:	insight-13.0-gdb-python313.patch
Patch209:	insight-13.0.50-calloc.patch
Patch210:	insight-13.0.50-C++20.patch
Patch211:	insight-13.0.50-bool.patch


%description
 Insight is a tight graphical user interface to GDB written in Tcl/Tk.
It provides a comprehensive interface that enables users to harness
most of GDB's power. It's also probably the only up-to-date UI for
the latest GDB version.


#-------------------------------------------------------------------------------
%prep 
#-------------------------------------------------------------------------------

%setup -q -n insight-%{version}

%patch 1 -p1 -b .relocate

%patch 101 -p1
%patch 102 -p1
%patch 103 -p1
%patch 104 -p1
%patch 105 -p1
%patch 106 -p1
%patch 107 -p1
%patch 108 -p1
%patch 109 -p1
%patch 110 -p1
%patch 111 -p1
%patch 112 -p1

%patch 201 -p1
%patch 202 -p1
%patch 203 -p1
%patch 204 -p1
%patch 205 -p1
%patch 206 -p1
%patch 207 -p1
%patch 208 -p1
%patch 209 -p1
%patch 210 -p1
%patch 211 -p1


#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

TOPDIR=`pwd`

#	Need a complete reconfiguration after unbundling.

autogen Makefile.def
autoreconf

#	Patches require some autotools rebuilds.

for location in gdb/gdbtk/plugins libgui
do	(
		cd $location
		aclocal -I "${TOPDIR}/config"
		automake
		autoconf
	)
done

#	Force documentation reconfiguration.
touch gdb/doc/version.subst

#	Get inclusion paths.

. "%{_libdir}/tclConfig.sh"
. "%{_libdir}/tkConfig.sh"

# We call configure directly rather than via macros, thus if
# we are using LTO, we have to manually fix the broken configure
# scripts
[ '%{_lto_cflags}' != '' ] && %{_fix_broken_configure_for_lto}

#	Do not use configure macro: let config.guess determine host,
#	build and target. This is the best way to get compatible values and
#	avoid building a cross tool.
CFLAGS="${RPM_OPT_FLAGS} -DDNF_DEBUGINFO_INSTALL"; export CFLAGS
CXXFLAGS="${RPM_OPT_FLAGS} -DDNF_DEBUGINFO_INSTALL"; export CXXFLAGS
LDFLAGS="${LDFLAGS:-%{?build_ldflags}}" ; export LDFLAGS
./configure	--prefix="%{_prefix}"					\
		--libdir="%{_libdir}"					\
		--enable-gdbtk						\
		--disable-binutils					\
		--disable-gdbserver					\
		--disable-elfcpp					\
		--disable-gas						\
		--disable-gold						\
		--disable-gprof						\
		--disable-ld						\
		--disable-rpath						\
		--disable-sim						\
		--disable-zlib						\
		--enable-gdb-build-warnings=,-Wno-unused,-Wno-deprecated-declarations,-Wno-nonnull-compare,-Wno-address,-Wno-stringop-overflow \
		--with-gdb-datadir='%{_datadir}/insight'		\
		--with-jit-reader-dir='%{_libdir}/insight'		\
		--with-separate-debug-dir='/usr/lib/debug'		\
		--with-system-readline					\
		--with-system-zlib					\
		--with-expat						\
		--with-python=%{__python3}				\
		--with-tclinclude="${TCL_SRC_DIR}"			\
		--with-tkinclude="${TK_SRC_DIR}"			\
		--without-libunwind					\
		--enable-64-bit-bfd					\
		--with-babeltrace					\
		--without-guile						\
		--with-lzma						\
%if 0%{?have_libipt}
		--with-intel-pt						\
%else
		--without-intel-pt					\
%endif
%ifarch sparc sparcv9 sparc64
		--without-mmap						\
%endif
%ifarch %{arm}
		--disable-inprocess-agent				\
%else
		--enable-inprocess-agent				\
%endif
		--with-auto-load-dir='$debugdir:$datadir/auto-load'	\
		--with-auto-load-safe-path='$debugdir:$datadir/auto-load' \
		--enable-targets=s390-linux-gnu,powerpc-linux-gnu,arm-linux-gnu,aarch64-linux-gnu \
		%{_target_platform}

make %{?_smp_mflags}


#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

INSTALL="install -p"

make DESTDIR="${RPM_BUILD_ROOT}" INSTALL="${INSTALL}" install

#	Removes unnecessary stuff.

(
	cd	"${RPM_BUILD_ROOT}"

	rm -f .%{_bindir}/gcore
	rm -f .%{_bindir}/gdb-add-index
	rm -f .%{_bindir}/gdb
	rm -f .%{_bindir}/gdbtui
	rm -f .%{_bindir}/gstack

	rm -rf .%{_includedir}

	rm -f .%{_libdir}/*.a
	rm -f .%{_libdir}/*.la
	rm -f .%{_libdir}/*.sh
	rm -f .%{_libdir}/libinproctrace.so

	rm -rf .%{_prefix}/man
	rm -rf .%{_datadir}/man

	rm -rf .%{_datadir}/info
	rm -rf .%{_datadir}/locale

	rm -rf .%{_datadir}/insight/system-gdbinit

	# /usr/share/insight/guile/ gets installed even --without-guile
	rm -rf .%{_datadir}/insight/guile
)

#	Regenerate the libgui pkgIndex.tcl file.

echo "pkg_mkIndex \"${RPM_BUILD_ROOT}%{_datadir}/insight/gui\"" | tclsh

#	Populate the auto-load directory from the libstdc++ gdb-specific
#		directory.

mkdir -p "${RPM_BUILD_ROOT}%{_datadir}/insight/auto-load"
rpm -ql libstdc++ | grep "^%{_datadir}/gdb/auto-load" | while read T
do	F="${RPM_BUILD_ROOT}%{_datadir}/insight/${T#%{_datadir}/gdb/}"
	if [[ "${F}/" =~ '/__pycache__/' ]]
	then	: # Do not copy cache.
	elif [ -e "${F}" ]
	then	: # Already exists: ignore.
	elif [ -d "${T}" ]
	then	mkdir -p "${F}"
	else	if [ -h "${T}" ]
		then	D=`dirname "${T}"`
			LINK=`realpath --relative-base="${D}" "${T}"`
			if [[ "${LINK}" =~ '^/' ]]
			then	T="${LINK}"
			else	T=`realpath --relative-base="${D}" "${T}"`
			fi
		fi
		ln -s "${T}" "${F}"
	fi
done

#	Install man file.

${INSTALL} -m 755 -d "${RPM_BUILD_ROOT}%{_mandir}/man1"
${INSTALL} -m 644 -p "%{SOURCE1}" "${RPM_BUILD_ROOT}%{_mandir}/man1/"

#	Create the menu entry.

${INSTALL} -m 755 -d "${RPM_BUILD_ROOT}%{_datadir}/applications"
desktop-file-install							\
	--dir		"${RPM_BUILD_ROOT}%{_datadir}/applications"	\
	gdb/gdbtk/insight.desktop

#	Install icon.

${INSTALL} -m 755 -d "${RPM_BUILD_ROOT}%{_datadir}/pixmaps"
${INSTALL} -m 644 gdb/gdbtk/insight_icon.svg				\
	"${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.svg"

#	Python byte compile, but not in auto-load.

%py_byte_compile %{__python3} %{buildroot}%{_datadir}/insight/python/gdb

#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------

%defattr(-, root, root, -)
%doc gdb/NEWS gdb/gdbtk/README gdb/gdbtk/plugins/HOW-TO COPYING COPYING3
%{_bindir}/*
%{_datadir}/insight
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man*/*


#-------------------------------------------------------------------------------
%changelog
#-------------------------------------------------------------------------------

* Tue Jan 21 2025 Patrick Monnerat <patrick@monnerat.net> 13.0.50.20220502-21
- Patch "bool" to rename a variable conflicting with a reserved word.

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.50.20220502-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 13.0.50.20220502-19
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.50.20220502-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 13.0.50.20220502-17
- Rebuilt for Python 3.13

* Wed Apr  3 2024 Patrick Monnerat <patrick@monnerat.net> 13.0.50.20220502-16
- Patch "C++20" to fix a language deprecation (FTBFS).
  https://bugzilla.redhat.com/show_bug.cgi?id=2272908

* Mon Jan 29 2024 Patrick Monnerat <patrick@monnerat.net> 13.0.50.20220502-15
- Patch "calloc" to respect count/size parameter order.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.50.20220502-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.50.20220502-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Patrick Monnerat <patrick@monnerat.net> 13.0.50.20220502-12
- Patch "python313" for Python 3.13 compatibility.
  https://bugzilla.redhat.com/show_bug.cgi?id=2245835

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.50.20220502-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 13.0.50.20220502-10
- Rebuilt for Python 3.12

* Fri Apr 14 2023 Patrick Monnerat <patrick@monnerat.net> 13.0.50.20220502-9
- Disable stringop-overflow warnings.
- Patch "bfd-CVE-2023-1972" fixes a security issue in bfd library.
  https://bugzilla.redhat.com/show_bug.cgi?id=2185646

* Wed Jan 25 2023 Florian Weimer <fweimer@redhat.com> - 13.0.50.20220502-8
- Apply binutils-gdb upstream patch to fix C99 issue in configure script

* Tue Jan 24 2023 Patrick Monnerat <patrick@monnerat.net> 13.0.50.20220502-7
- Patch "noselfmove" removes the move to self tests.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.50.20220502-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 23 2022 Patrick Monnerat <patrick@monnerat.net> 13.0.50.20220502-5
- Patch "distutils" removes deprecated python 3.12 module use.
  https://bugzilla.redhat.com/show_bug.cgi?id=2155038

* Wed Dec 14 2022 Patrick Monnerat <patrick@monnerat.net> 13.0.50.20220502-4
- Patch "print-check-value" avoids segfault when printing ghost variable.
- Patch "bfd-CVE-2022-4285" fixes CVE-2022-4285.
  https://bugzilla.redhat.com/show_bug.cgi?id=2152948

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.50.20220502-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 13.0.50.20220502-2
- Rebuilt for Python 3.11

* Mon May  2 2022 Patrick Monnerat <patrick@monnerat.net> 13.0.50.20220502-1
- New upstream snapshot.
- Disable deprecated declaration warnings/errors.
- Disable nonnull-compare warnings.
- Patch "symtab_no_format_overflow" to avoid a false positive format overflow
  detection.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.50.20201215-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.50.20201215-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 11.0.50.20201215-5
- Rebuilt for Python 3.10

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 11.0.50.20201215-4
- Rebuilt for removed libstdc++ symbols (#1937698)

* Tue Mar 23 2021 Patrick Monnerat <patrick@monnerat.net> 11.0.50.20201215-3
- Fix lto_cflags test.
- Disable guile.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.50.20201215-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec  5 2020 Patrick Monnerat <patrick@monnerat.net> 11.0.50.20201215-1
- New upstream snapshot.
- Fixes FTBFS.
  https://bugzilla.redhat.com/show_bug.cgi?id=1906699
- Uses guile 2.2
  https://bugzilla.redhat.com/show_bug.cgi?id=1901360

* Sat Aug  8 2020 Patrick Monnerat <patrick@monnerat.net> 10.0.50.20200210-10
- Patch "python39-2" removes another Python 3.9 deprecated function call.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.50.20200110-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.50.20200110-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Jeff Law <law@redhat.com> 10.0.50.20200110-7
- Fix broken configure tests compromised by LTO

* Wed Jul  1 2020 Patrick Monnerat <patrick@monnerat.net> 10.0.50.20200110-6
- Rebuild for guile 2.2.
  https://bugzilla.redhat.com/show_bug.cgi?id=1852708
- Turn off the brp-python-bytecompile automagic.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 10.0.50.20200110-5
- Rebuilt for Python 3.9

* Tue May  5 2020 Patrick Monnerat <patrick@monnerat.net> 10.0.50.20200210-4
- Patch "python39" removes a Python 3.9 deprecated function call.
  https://bugzilla.redhat.com/show_bug.cgi?id=1831213
  https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=97ed802

* Mon Apr  6 2020 Patrick Monnerat <patrick@monnerat.net> 10.0.50.20200210-3
- Patch "gcc10" for gnu C version 10 compatibility.
  https://bugzilla.redhat.com/show_bug.cgi?id=1818009
  https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=cda7e56

* Tue Mar 10 2020 Patrick Monnerat <patrick@monnerat.net> 10.0.50.20200210-2
- Let config.guess determine host, build and target. This will avoid building
  a cross tool.

* Fri Feb  7 2020 Patrick Monnerat <patrick@monnerat.net> 10.0.50.20200210-1
- New upstream snapshot (commit 26d2110bcaaf387e3e3f4d6950ca0536a9f10a5a).

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.50.20190118-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 8.2.50.20190118-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 8.2.50.20190118-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.50.20190118-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8.2.50.20190118-3
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.50.20190118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Patrick Monnerat <patrick@monnerat.net> 8.2.50.20190118-1
- New upstream snapshot (commit b0e5b9996dcb1b8079eaaa26c6c7d04b391324a0).
- Patch "bfd-absolute-value" to get rid of a non portable labs() call in bfd.

* Sat Aug 11 2018 Patrick Monnerat <patrick@monnerat.net> 8.1.50.20180216-6
- Install guile files.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.50.20180216-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Patrick Monnerat <patrick@monnerat.net> 8.1.50.20180216-4
- Patch "python37" for Python version 3.7 compatibility.
  https://sourceware.org/bugzilla/show_bug.cgi?id=23252

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 8.1.50.20180216-3
- Rebuilt for Python 3.7

* Wed Mar  7 2018 Patrick Monnerat <patrick@monnerat.net> 8.1.50.20180216-2
- Patch "serialbaud" change set/show baud rate command.
  https://sourceware.org/git/?p=insight.git;a=commit;h=a2b5b98
- Patch "globalpref" uses global name prefix for preference array.
  https://sourceware.org/git/?p=insight.git;a=commit;h=19d337f

* Fri Feb 16 2018 Patrick Monnerat <patrick@monnerat.net> 8.1.50.20180216-1
- New upstream release.
- Modernize spec file (BZ #1545189).

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.12.50.20170416-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.12.50.20170416-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.12.50.20170416-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.12.50.20170416-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Apr 16 2017 Patrick Monnerat <patrick@monnerat.net> 7.12.50.20170416-1
- New upstream release.
- Fixes BZ #1409768.
- Fixes BZ #1423741.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.10.50.20160208-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 7.10.50.20160208-3
- Rebuild for readline 7.x

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 7.10.50.20160208-2
- Rebuild for Python 3.6

* Mon Feb  8 2016 Patrick Monnerat <patrick.monnerat@dh.com> 7.10.50.20160208-1
- New snapshot.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.8.50-7.20140827git
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jun 23 2015 Patrick Monnerat <pm@datasphere.ch> 7.8.50-6.20140827git
- Patch "vla-intel-2" to fix a subexpression operator precedence.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.8.50-5.20140827git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 21 2015 Patrick Monnerat <pm@datasphere.ch> 7.8.50-4.20140827git
- Conditionally backport to F20.
  https://bugzilla.redhat.com/show_bug.cgi?id=1184080
- Patch "locvars" to populate local variables window.
  https://github.com/monnerat/insight/commit/a8b05335
- Fix libstdc++ pretty printers implementation (for console window only).

* Tue Jan 13 2015 Patrick Monnerat <pm@datasphere.ch> 7.8.50-3.20140827git
- URL change.
- Do not install /usr/bin/gcore: now provided by the gdb package.
  https://bugzilla.redhat.com/show_bug.cgi?id=1180627

* Mon Oct 27 2014 Patrick Monnerat <pm@datasphere.ch> 7.8.50-2.20140827git
- Enlarge icon by resizing.
  https://bugzilla.redhat.com/show_bug.cgi?id=1157545

* Wed Aug 27 2014 Patrick Monnerat <pm@datasphere.ch> 7.8.50-1.20140827git
- New snapshot.
- Patch "iwidgetsname" for package name case spelling.
- Limited pretty printers support (from console window).

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.50-16.20120403cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Patrick Monnerat <pm@datasphere.ch> 7.4.50-15.20120403cvs
- Patch "tcl86" for tcl/tk version 8.6 and itcl/itk/iwidgets 4.0 compatibility.
- Patch "bfdarm" to fix bfd compilation on arm.
- Requires xterm for Fedora 21.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.50-14.20120403cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Dan Horák <dan[at]danny.cz> - 7.4.50-13.20120403cvs
- fix build on s390(x) with a patch from binutils
- fix FTBFS due GCC 4.9

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 7.4.50-12.20120403cvs
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Mon Mar  3 2014 Patrick Monnerat <pm@datasphere.ch> 7.4.50-11.20120403cvs
- Use our own python and syscalls scripts rather than gdb's.
  https://bugzilla.redhat.com/show_bug.cgi?id=1067668

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.50-10.20120403cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul  3 2013 Patrick Monnerat <pm@datasphere.ch> 7.4.50-9.20120403cvs
- Patch "texinfo5" to adapt doc to texinfo version 5.

* Wed Jul  3 2013 Patrick Monnerat <pm@datasphere.ch> 7.4.50-8.20120403cvs
- Compress snapshot tar archive with xz.
  https://bugzilla.redhat.com/show_bug.cgi?id=980597

* Fri Feb 15 2013 Patrick Monnerat <pm@datasphere.ch> 7.4.50-7.20120403cvs
- Patch "nocygnus" to replace automake option "cygnus" by "foreign no-dist".

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.50-6.20120403cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec  5 2012 Patrick Monnerat <pm@datasphere.ch> 7.4.50-5.20120403cvs
- Patch "bz883591" to fix a segmentation fault.
  https://bugzilla.redhat.com/show_bug.cgi?id=883591

* Thu Nov 15 2012 Patrick Monnerat <pm@datasphere.ch> 7.4.50-4.20120403cvs
- Path "objalloc" to fix libiberty security bug CVE-2012-3509.
  https://bugzilla.redhat.com/show_bug.cgi?id=877014
- Enable Python to support STL extensions.
  https://bugzilla.redhat.com/show_bug.cgi?id=865554

* Fri Jul 20 2012 Patrick Monnerat <pm@datasphere.ch> 7.4.50-3.20120403cvs
- Patch "structsiginfo" to replace occurrences of "struct siginfo" by
  "siginfo_t".

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.50-2.20120403cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr  3 2012 Patrick Monnerat <pm@datasphere.ch> 7.4.50-1.20120403cvs
- New cvs snapshot.
- Patches imported or adapted from gdb package.
- Patch "sig2dead" to avoid a segfault while notifying a signal to a dead
  process.
  http://sourceware.org/ml/insight/2012-q2/msg00002.html
- Patch "sizesizet" to fix a type mismatch between print format descriptors and
  corresponding argument.
  http://sourceware.org/ml/insight/2012-q2/msg00003.html

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb  9 2011 Patrick Monnerat <pm@datasphere.ch> 6.8.1-4
- Patch "unused" to suppress "variable set but not used" errors.
- Patch "gcc45" to fix gcc 4.5 errors on incompatible enums.
  https://bugzilla.redhat.com/show_bug.cgi?id=631116

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 13 2010 Patrick Monnerat <pm@datasphere.ch> 6.8.1-2
- Patch "sbrk" to enable sbrk() prototype on F13.

* Wed Jan 13 2010 Patrick Monnerat <pm@datasphere.ch> 6.8.1-1
- New version.
- Patch "baseclassfield" to fix bug BZ 551126.
- Start a terminal for standard IO when invoked through desktop file.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Patrick Monnerat <pm@datasphere.ch> 6.8-8
- Fix bug #511501: combobox.tcl installed twice causes build failure.
- Patch "readline6" to use system readline version 6.

* Mon Mar  2 2009 Patrick Monnerat <pm@datasphere.ch> 6.8-7
- Removed libXft-devel build requirement.
- .desktop file categories fixed.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Patrick Monnerat <pm@datasphere.ch> 6.8-5
- Patch "gcc44" to make it compilable with gcc 4.4.
- Build converts image format using ImageMagick instead of gif2png.
- Add build requirement of libXft-devel as a temporary workaround for missing
  dependence of tk-devel on it.

* Mon Oct 13 2008 Patrick Monnerat <pm@datasphere.ch> 6.8-4
- X-Fedora application category removed.
- Force option -p of install.

* Thu Oct  9 2008 Patrick Monnerat <pm@datasphere.ch> 6.8-3
- Patch "lib64" to enable tcl/tk/itcl/itk searches also in */lib64.

* Wed Oct  8 2008 Patrick Monnerat <pm@datasphere.ch> 6.8-2
- Patch "tclm4" to define tcl/tk autoconf macros in gdbtk/plugins directory.
- Use system readline.
- Force expat use.

* Thu Aug 14 2008 Patrick Monnerat <pm@datasphere.ch> 6.8-1
- Initial package.
- Patch "warnings" to suppress compilation warnings, since these abort rpmbuild.
- Patch "destdir" to properly install files when DESTDIR is defined.
- Patch "derefbug" to fix an address/value confusion bug.
- Patch "gcc43" to satisfy extra checks of gcc compiler version 4.3.
- Patch "ia64bound" to fix an array index out-of-bound bug in IA64
  specific code.
- Patch "itcl33" to migrate all code to itcl/itk version 3.3.
- Patch "syspackages" to use system-installed packages tck, tk, itcl, itk and
  iwidgets.
- Patch "relocate" to move all datadir/subdir stuff into datadir/insight (incl.
  libgui, that ought to be an external package). Non-binary libdir/* is also
  moved.
