%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%{tcl_version}}

Summary: Widget extension to the Tcl/Tk scripting language
Name: blt
Version: 2.4
Release: 71.z%{?dist}

License: MIT
URL: http://sourceforge.net/projects/blt/
Source0: http://downloads.sourceforge.net/blt/BLT2.4z.tar.gz
#Source0: http://downloads.sourceforge.net/blt/blt-20050731cvs.tgz
Patch0: http://downloads.sourceforge.net/blt/blt2.4z-patch-2
Patch1: http://jfontain.free.fr/blt2.4z-patch-64
Patch2: blt2.4-tk8.5.patch
Patch3: blt2.4z-destdir.patch
Patch4: blt2.4z-norpath.patch
Patch5: blt2.4z-noexactversion.patch
Patch6: blt2.4z-zoomstack.patch
Patch7: blt2.4z-tk8.5.6-patch
Patch8: blt2.4z-tcl8.6.patch
Patch9: blt2.4z-tk8.6.patch
Patch10: blt-configure-c99.patch


Provides: tk-blt = %{version}-%{release}
BuildRequires: tk-devel >= 8.4.7 gcc
BuildRequires: make

Requires: tk >= 8.4.7
Requires: itcl
Requires: tcl(abi) = 8.6


%description
BLT is a very powerful extension to Tk. It adds plotting widgets
(graph, barchart and stripchart), hierarchy tree and table, tab
notebook, table geometry manager, vector, background program
execution, busy utility, eps canvas item, drag and drop facility,
bitmap command and miscellaneous commands.
Note: this version is stubs enabled and therefore should be compatible
with Tcl/Tk versions after and including 8.3.1.


%package devel
Summary:        Development files for BLT
Requires:       tcl-devel
Requires:       %{name} = %{version}-%{release}

%description devel
BLT is an extension to the Tk toolkit. BLT's most useful feature is the
provision of more widgets for Tk, but it also provides more geometry managers
and miscellaneous other commands. Note that you won't need to any patching
of the Tcl or Tk source file to use BLT, but you will need to have Tcl/Tk
installed in order to use BLT.

This package provides headers needed to build packages based on BLT.

%package doc
Summary:        HTML documentation for BLT
BuildArch:      noarch

%description doc
This package provides the html documentation for BLT

%prep
%setup -q -n %{name}%{version}z
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p0
%patch -P6 -p0
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1

# Fix bad interpreter path
sed -i -e 's#/usr/local/bin/tclsh#/usr/bin/tclsh#' demos/scripts/page.tcl

# Rename a couple of files that conflict with other packages
mv man/graph.mann man/bltgraph.mann
mv man/bitmap.mann man/bltbitmap.mann

%build
# fix RHBZ 1105266
sed -i -e "s|SHLIB_LD_FLAGS='-rdynamic -shared -Wl,-E -Wl,-soname,\$@'|SHLIB_LD_FLAGS='-rdynamic -shared -Wl,-E -Wl,-soname,\$@ -ltk -ltcl'|" configure
%configure --with-tcl=%{_libdir} --with-tk=%{_libdir} --with-blt=%{tcl_sitelib} --includedir=%{_includedir}/%{name}
pushd src/shared
# no _smp_mflags; race conditions.
make
popd

for file in demos/*.tcl ; do
    sed -i -e 's#../src/bltwish#/usr/bin/wish#' $file
done
sed -i -e 's#../bltwish#/usr/bin/wish#' demos/scripts/xcolors.tcl

%install
make install INSTALL_ROOT=%{buildroot}
# Fedora policy is not to generate new shells for Tcl extensions
rm -f %{buildroot}%{_bindir}/bltsh*
rm -f %{buildroot}%{_bindir}/bltwish*
# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a
# Remove some doc files from the script area
rm -f %{buildroot}%{tcl_sitelib}/%{name}%{version}/{README,NEWS,PROBLEMS}
# Remove man pages.  HTML documentation is already available.
rm -rf %{buildroot}%{_mandir}/

%ldconfig_scriptlets

%files
%doc README INSTALL PROBLEMS
%{_libdir}/*.so
%{tcl_sitelib}/%{name}%{version}
%{tcl_sitearch}/%{name}%{version}
# Man pages conflict with iwidgets.  This is a common problem among
# Tk widget extensions.
#%{_mandir}/man3/*
#%{_mandir}/mann/*

%files doc
%doc html/

%files devel
%{_includedir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-71.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 15 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.4-70.z
- Apply debian patch for tk8.6 build failure with
  -Werror=incompatible-pointer-types

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-69.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-68.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-67.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-66.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-65.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Florian Weimer <fweimer@redhat.com> - 2.4-64.z
- Port configure script to C99

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-63.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 09 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.4-62.z
- Fix build error on el9.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-61.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-60.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-59.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-58.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-57.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-56.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-55.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.4-54.z
- Add gcc to BR.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-53.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-52.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-51.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-50.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-49.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-48.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.4-47.z
- Make -doc noarch and not to require the main package.
- Add Require to -devel: tcl-devel.
- "define" -> "global".

* Fri Jul 03 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 2.4-46.z
- Fix requiers for EPEL (RHBZ #1238627).
- Clean spec (buildroot tag, clean section, rm buildroot).

* Tue Jun 30 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 2.4-45.z
- Fix for RHBZ #1105266.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-44.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-43.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-42.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 2.4-41.z
- Fix for tk-8.6.

* Fri May 30 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 2.4-40.z
- Fix for tcl-8.6.

* Fri May 30 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 2.4-39.z
- Changed requires to require tcl-8.6.

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4-38.z
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-37.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-36.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-35.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-34.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-33.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 9 2010 Wart <wart at kobold.org> 2.4-32.z
- Fix segfault caused by use of uninitialized array
- Add upstream patch for drawing text on a bitmap (bz #486165, bz #530277,
  bz #504388)
- Add ZoomStack widget (bz #503483)
- Split doc into subpackage (bz #492453)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-31.z
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Jesse Keating <jkeating@redhat.com> - 2.4-30.z
- Rebuild for F11 mass rebuild
- Remove package name from Summary

* Thu May 29 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.4-28.z
- Patched to recover blt::graph (bz #446862)

* Thu Apr 3 2008 Wart <wart at kobold.org> 2.4-27
- Remove man pages due to conflict with iwidgets.  This is a common problem
  among Tk widget extensions. (BZ #439769)
- Trivial cleanup to source URLs.

* Mon Mar 17 2008 Wart <wart at kobold.org> 2.4-26
- Add patch to prevent BLT from puking every time there is a minor
  version bump for Tcl. (BZ #437780)

* Sat Feb 9 2008 Wart <wart at kobold.org> 2.4-25
- Rebuild for gcc 4.3
- Add patch to add soname and remove rpath

* Mon Jan 07 2008 Wart <wart at kobold.org> 2.4-24
- Move pkgIndex.tcl file to %%{_libdir} as it contains arch-specific
  components

* Mon Jan 07 2008 Wart <wart at kobold.org> 2.4-23
- Clean up spec file by creating patch for broken Makefile stanzas

* Mon Jan 07 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.4-22
- Debug files in debug package (bug #427681)

* Sat Jan 05 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.4-21
- Libraries moved to %%libdir, file in ld.so.conf.d not needed
- Tcl files moved to %%tcl_sitelib

* Fri Jan 04 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.4-20
- Rebuilt for tk 8.5 (added patch)
- Following PackagingDrafts/Tcl

* Thu Nov 15 2007 Sergio Pascual <sergiopr at fedoraproject.org> 2.4-19
- Renaming the file in /etc/ld.so.conf.d to %%name

* Mon Nov 05 2007 Sergio Pascual <sergiopr at fedoraproject.org> 2.4-18
- Providing file in /etc/ld.so.conf.d (bug #333081)

* Mon Oct 22 2007 Marek Mahut <mmahut fedoraproject.org> 2.4-17
- Providing devel package as per request in BZ#249812

* Thu Feb 8 2007 Jean-Luc Fontaine <jfontain@free.fr> 2.4-15.z
- require tk < 8.5

* Mon Aug 28 2006 Jean-Luc Fontaine <jfontain@free.fr> 2.4-14.z
- added dist tag
- rebuild for Fedora Extras 6

* Tue Feb 28 2006 Jean-Luc Fontaine <jfontain@free.fr> 2.4-13.z
- rebuild for Fedora Extras 5

* Thu Nov 10 2005 Jean-Luc Fontaine <jfontain@free.fr> 2.4-12.z
- only require tk and tk-devel for building

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Nov 5 2004 Jean-Luc Fontaine <jfontain@free.fr> 0:2.4-10.z
- added patch to allow building on 64 bit architectures
- use %%libdir instead of %%prefix in configure for the same reason

* Tue Nov 16 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.4-0.fdr.9.z
- in build requirements, work around tcl-devel and tk-devel packages non
  existence in RH 8.0 and 9

* Wed Nov 7 2003 Ville Skyttä <ville.skytta at iki.fi> 0:2.4-0.fdr.8.z
- disabled %%_smp_mflags in make stage
- escaped percent characters in change log

* Tue Nov 5 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.4-0.fdr.7.z
- in installation stage, removed some leftover copies in parent
  directory which left dirt in BUILD directory

* Tue Nov 4 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.4-0.fdr.6.z
- changed release tag from 0.fdr.0.X.z to 0.fdr.X.z as this is a post
  release
- use "download.sourceforge.net/..." instead of
  "prdownloads.sourceforge.net/..." to make URLs directly downloadable
- removed AutoReqProv
- used "%%setup -q -n ..." to remove unnecessary cd's.
- no longer override $RPM_OPT_FLAGS
- used %%_prefix instead of %%_usr
- added -p argument to install and cp to preserve timestamps
- replaced %%__cp and %%__install by cp and install
- fixed URL to point to sourceforge project page as homepage is empty
- no longer use RPM_OPT_FLAGS in CFLAGS as make argument as %%configure
  already handles it

* Tue Nov 1 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.4-0.fdr.5.z
- removed RCS line
- set Epoch to 0 and removed it from Release
- used a full macroless URL to the source tarball and patches
- removed Packager (not used in Fedora)
- used rm instead of %%__rm macro
- used SMP flags in make stage

* Tue Oct 22 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.4-0.fdr.4.z
- checked with rpmlint and improved accordingly.
