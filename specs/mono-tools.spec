%global debug_package %{nil}

Name:    mono-tools
Summary: A collection of tools for mono applications
Version: 4.2
Release: 32%{?dist}
License: MIT
URL:     http://www.mono-project.com/Main_Page
Source0: http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
Patch1:  mono-tools-4.2-sharpziplib.patch
Patch2:  mono-tools-4.2-fix-xml-wellformed-comment.patch
Patch3:  mono-tools-4.2-fix-cecil.patch

BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gettext-devel
BuildRequires: gnome-desktop-sharp-devel
BuildRequires: gnome-sharp-devel
BuildRequires: gtk-sharp2-devel
BuildRequires: gtk-sharp2-gapi
BuildRequires: sharpziplib-devel
BuildRequires: hunspell-devel
BuildRequires: libgdiplus-devel
BuildRequires: mono-data
BuildRequires: mono-data-oracle
BuildRequires: mono-devel >= 4.0
BuildRequires: nunit
BuildRequires: nunit-devel
BuildRequires: mono-cecil
BuildRequires: mono-cecil-devel
BuildRequires: monodoc-devel
BuildRequires: mono-web-devel
BuildRequires: pkgconfig
BuildRequires: autoconf automake libtool
Requires: mono-core >= 4.0 links monodoc
Requires: mono-cecil
Requires: sharpziplib

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
Monotools are a number of tools for mono such as allowing monodoc to be run
independantly of monodevelop

%package devel
Summary: .pc file for mono-tools
Requires: %{name} = %{version}-%{release} pkgconfig

%description devel
Development file for mono-tools

%package monodoc
Summary: Monodoc documentation
Requires: %{name} = %{version}-%{release} monodoc

%description monodoc
Documentation for monotools for use with monodoc

%package gendarme
Summary: Inspect your .NET and Mono assemblies
Requires: %{name} = %{version}-%{release}

%description gendarme
Inspect your .NET and Mono assemblies.

%prep
%setup -q
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
chmod 644 COPYING

find . -name "Makefile.in" -print -exec sed -i "s#GMCS#MCS#g; s#DMCS#MCS#g" {} \;
find . -name "configure.in" -print -exec sed -i "s#GMCS#MCS#g; s#DMCS#MCS#g" {} \;
sed -i "s#mono-nunit#nunit#g" configure.in
sed -i "s#mono-nunit#nunit#g" gendarme/rules/Test.Rules/Makefile.in

# disable mdoc because it is not built by Mono 6 and mcs anymore
find . -name "Makefile.in" -print -exec sed -i "s~mdoc assemble~mkdir -p doc/generated #mdoc assemble~g" {} \;
find . -name "Makefile.in" -print -exec sed -i "s~mdoc update~mkdir -p doc/generated #mdoc update~g" {} \;
find . -name "Makefile.in" -print -exec sed -i "s~install-framework_documentationDATA: ~install-framework_documentationDATA: \ninstall-framework_documentationDATADisabled: ~g" {} \;
find . -name "Makefile.in" -print -exec sed -i "s~install-rules_documentationDATA: ~install-rules_documentationDATA: \ninstall-rules_documentationDATADisabled: ~g" {} \;

%build
# need to run autoconf >= 2.69 to support aarch64
autoconf
%configure --libdir=%{_prefix}/lib --disable-docs
make V=1
# no smp flags - breaks the build

%install
make DESTDIR=%{buildroot} install

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
        --vendor fedora \
%endif
        --dir %{buildroot}%{_datadir}/applications \
        --add-category Development \
        --delete-original \
        %{buildroot}%{_datadir}/applications/monodoc.desktop

mkdir -p %{buildroot}%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv %{buildroot}%{_prefix}/lib/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING AUTHORS ChangeLog README
%{_bindir}/create-native-map
%{_bindir}/gasnview
%{_bindir}/monodoc
%{_bindir}/mprof*
%{_bindir}/gsharp
%{_bindir}/gd2i
%{_bindir}/mperfmon
%{_bindir}/gui-compare
%{_bindir}/emveepee
%{_bindir}/minvoke
%{_prefix}/lib/gsharp/gsharp.exe*
%{_prefix}/lib/create-native-map
%{_prefix}/lib/mperfmon/*
%dir %{_prefix}/lib/gui-compare
%{_prefix}/lib/gui-compare/gui-compare.exe*
%{_prefix}/lib/mono/1.0/gasnview.exe
%{_prefix}/lib/monodoc/browser.exe
%{_prefix}/lib/minvoke/minvoke.exe
%dir %{_prefix}/lib/minvoke
%dir %{_prefix}/lib/mono-tools
%{_prefix}/lib/mono-tools/mprof*
%{_prefix}/lib/mono-tools/Mono.Profiler.Widgets*
%{_prefix}/lib/mono-tools/emveepee.exe*
%{_mandir}/man1/mprof*
%{_mandir}/man1/create-native-map.1.gz
%{_datadir}/pixmaps/monodoc.png
%{_datadir}/applications/gsharp.desktop
%{_datadir}/applications/monodoc.desktop
%{_prefix}/lib/monodoc/MonoWebBrowserHtmlRender.dll
%{_mandir}/man1/mperfmon*
%{_mandir}/man1/gd2i*
%{_datadir}/icons/hicolor/

%files gendarme
%{_bindir}/gendarme*
%{_datadir}/applications/gendarme-wizard.desktop
%{_datadir}/pixmaps/gendarme.svg
%{_mandir}/man1/gendarme*
%{_prefix}/lib/gendarme/*.dll
%{_prefix}/lib/gendarme/*.exe
%{_prefix}/lib/gendarme/*.xml

%files devel
%{_libdir}/pkgconfig/*.pc

%files monodoc
%dir %{_prefix}/lib/monodoc/web
%{_prefix}/lib/monodoc/web/*
%{_mandir}/man5/gendarme*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.2-24
- Rebuilt for latest SharpZipLib

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 14 2021 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.2-22
- Rebuilt for latest SharpZipLib

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.2-20
- Rebuilt for latest SharpZipLib

* Fri Oct 30 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.2-19
- Rebuilt for Mono 6.12, fix building with latest SharpZipLib

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.2-16
- built without docs because mdoc.exe is not built with Mono 6 and mcs anymore

* Thu Aug 08 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.2-15
- apply patch to fix issue with building with latest Cecil 0.10.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.2-13
- build against separate package sharpziplib, not the ancient sharpziplib bundled with Mono (fixes bug 1583295)
- fix issue with not well-formed XML markup in a comment for s390x

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 02 2018 Timotheus Pokorra <tp@tbits.net> - 4.2-10
- fix FTBFS due to retired webkitgtk. dropping ilcontrast for that reason.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-5
- mono rebuild for aarch64 support

* Wed Sep 14 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.2-4
- calling autoconf >= 2.69 to support aarch64 (#926162)

* Sat Aug 06 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.2-3
- using unbundled mono-cecil (#1360620)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 4.2-1
- Updated to 4.2

* Mon Jan 04 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 3.10-5
- replace define with global, according to http://fedoraproject.org/wiki/Packaging:Guidelines#.25global_preferred_over_.25define
- do not use dmcs anymore, use mcs instead (related to #1294967)

* Wed Aug 05 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 3.10-4
- do not use mono-nunit anymore but depend on new package nunit

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 3.10-2
- fixes for mono4

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 3.10-1
- Update to 3.10
- Rebuild (mono4)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 Richard Hughes <richard@hughsie.com> - 2.10-11
- Split out gendarme and ilcontrast as subpackages so the different applications
  are visible in gnome-software.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.10-8
- Remove --vendor from desktop-file-install for F19+

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Christian Krause <chkr@fedoraproject.org> - 2.10-4
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Sat Apr 30 2011 Christian Krause <chkr@fedoraproject.org> - 2.10-3
- Rebuilt against mono 2.10.2

* Tue Apr 26 2011 Dan Horák <dan[at]danny.cz> - 2.10-2
- updated the supported arch list

* Tue Mar 29 2011 Christian Krause <chkr@fedoraproject.org> - 2.10-1
- Update to 2.10
- Disable GeckoHtmlRenderer
- Minor spec file cleanup

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Christian Krause <chkr@fedoraproject.org> - 2.8-4
- Don't build gtkhtml renderer since gtkhtml-sharp is not
  available anymore (BZ 660867).

* Wed Dec 22 2010 Paul <paul@all-the-johnsons.co.uk> - 2.8-3
- rebuilt

* Wed Dec 22 2010  Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.8-2
- Rebuild

* Sun Oct 03 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.8-1
- Bump to 2.8 preview 8
- Remove BR mono-jscript

* Wed Jun 23 2010 Christian Krause <chkr@fedoraproject.org> - 2.6.2-1
- Bump to the 2.6.2 release
- Cleanup spec file

* Wed Dec 23 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.6.1-1
- Bump to the 2.6.1 release
- Removed webkit patch

* Thu Nov 26 2009 Christian Krause <chkr@fedoraproject.org> - 2.6-3
- Fix monodoc crash when using WebKit html renderer (BZ 538555)

* Thu Nov 26 2009 Christian Krause <chkr@fedoraproject.org> - 2.6-2
- Restore version 2.6
- Re-apply Dennis Gilmore's sparc64 changes

* Sun Oct 04 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.6-1
- Bump to 2.6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Christian Krause <chkr@fedoraproject.org> - 2.4.2-4
- Add version to requirement of gtkhtml-sharp to distinguish between
gtk-sharp and gnome-desktop-sharp

* Sat Jul 11 2009 Christian Krause <chkr@fedoraproject.org> - 2.4.2-3
- Add mono(webkit-sharp) as run-time requirement since it is needed by the
webkit engine of monodoc (BZ 478650)
- More minor spec file beautifications to fix rpmlint warnings

* Sat Jul 11 2009 Christian Krause <chkr@fedoraproject.org> - 2.4.2-2
- Add BR webkit-sharp-devel to build the webkit engine for monodoc (BZ 478650)
- Add mono(gtkhtml-sharp) as run-time requirement since it is needed by the
gtkhtml engine of monodoc (BZ 478650)
- Minor spec file beautification to fix some rpmlint warnings

* Tue Jun 09 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.4.2-1
- Bump to 2.4.2 preview 1
- Add support for ppc and ppc64

* Mon Apr 06 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.4-8.1
- remove ppc

* Thu Mar 26 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.4-8
- Full 2.4 release

* Wed Mar 18 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.4-7.RC3
- bump to RC3

* Thu Mar 12 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.4-6.RC2
- bump to RC2
- Add BR mono-web-devel

* Fri Feb 27 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.4-5.RC1
- bump to RC1
- Fix libdir problem for monodoc

* Fri Feb 20 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.4-4.20092002svn127416
- update from svn
- tagged as preview 3 release

* Tue Feb 10 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.4-3.20091002svn126075
- update from svn

* Mon Feb 02 2009  Paul F. Johnson <paul@all-the-johnsons.co.uk> -.2.4-3.20090202svn125131
- update from svn
- retagged for pre-release 1
- removed guicompare.dlls

* Sat Jan 24 2009  Paul F. Johnson <paul@all-the-johnsons.co.uk> -.2.4-2.20090124svn124416
- update from svn
- altered BRs and Rs to use mono-2.4

* Fri Jan 16 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.4-1.20091601svn123182
- Move to 2.4 svn branch

* Sun Jan 11 2009  Paul F. Johnson <paul@all-the-johnsons.co.uk> -.2.2-10.RC2.20090111svn122974
- update from svn
- bump to RC2

* Sun Jan 04 2009  Paul F. Johnson <paul@all-the-johnsons.co.uk> -.2.2-9.RC1.20090104svn122377
- update from svn

* Tue Dec 30 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> -.2.2-9.RC1.20081230svn122166
- update from svn

* Wed Dec 24 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> -.2.2-9.RC1.20081224svn122098
- Bump to RC1 svn branch

* Fri Dec 19 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.2-8.pre3.20081219svn121827
- Update from svn
- Re-enable ppc build

* Mon Dec 15 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.2-3.pre3.20081215svn121681
- Bump to preview 3
- Updated to svn

* Mon Dec 15 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.2-7.pre2.20081215svn121502
- Updated to svn

* Sat Dec 06 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.2-6.pre2
- Bump to preview 2
- use sed to remove the patches

* Sat Nov 29 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.2-5.pre1.1
- Dropped the last patch and sedded it instead

* Sat Nov 29 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.2-5.pre1
- More patches. Crumbs - why can't these guys just use $(libdir)?

* Sat Nov 29 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.2-4.pre1
- More patches

* Sat Nov 29 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.2-3.pre1
- actually apply the configure patch helps...

* Wed Nov 26 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.2-2.pre1
- added configure patch

* Thu Nov 20 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.2-1.pre1
- bump to 2.2 preview 1
- fix patch files
- branch off monodoc documentation

* Fri Oct 03 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.0-7
- bump to rc3

* Wed Oct 01 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.0-6
- bump to rc3

* Tue Sep 09 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.0-5
- bump to 2.0 RC 1
- spec file chanages

* Fri Aug 29 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.0-4
- additional BRs included

* Thu Aug 28 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0-3
- include unowned directories

* Fri Aug 15 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-2
- reworked the patchfiles
- removed monodir (not used)
- spec file fix

* Sun Aug 03 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-1
- bump to 2.0 preview 1
- spec file fixes

* Tue Jul 08 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9-4
- added br gnome-desktop-sharp
- fix for archs

* Mon Jul 07 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9-3.1
- rebuild

* Tue Jun 03 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9-3
- added BR desktop-file-utils

* Tue May 06 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9-2.1
- rebuild

* Wed Apr 30 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9-2
- added hunspell-devel

* Mon Apr 21 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9-1
- bump

* Mon Jan 14 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.6-3
- spec file fixes
- excludearch ppc64

* Fri Jan 04 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.6-2
- license fix

* Fri Jan 04 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.6-1
- bump
- spec file fixes
- removed support for under FC7

* Fri Feb 23 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.3-2
- fix for mock

* Thu Feb 15 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.3-1
- bump
- a couple of small spec file fixes
- disabled installing the gnunit apps as theyre broken currently

* Sun Jan 28 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.1-4
- added gettext-devel for findlangs to work

* Thu Jan 18 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.1-3
- added gecko-sharp2-devel and gnome-sharp-devel 

* Fri Dec 01 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.1-2
- various spec file changes
- rename spec and package to be mono-tools

* Sat Nov 25 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.1-1
- bump
- added addition files and devel subpackage

* Sat Oct 14 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.1.17-1
- bump

* Thu Sep 07 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.1.11-1
- Initial import, debug and the likes

