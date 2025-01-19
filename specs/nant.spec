%global debug_package %{nil}
%global monodir %{_prefix}/lib
%global bootstrap 0

Summary: NAnt is a build tool for Mono and .NET
Name: nant
Version: 0.92
Release: 39%{?dist}
Epoch: 1
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Url: http://nant.sourceforge.net/

Source0: http://downloads.sourceforge.net/nant/%{name}-%{version}-src.tar.gz
Patch1: nant-0.92-no_ndoc.patch
Patch2: nant-0.92-system_nunit.patch
Patch3: nant-0.90-no_sharpcvslib.patch
Patch4: nant-0.90-system_sharpziplib.patch
Patch5: nant-0.92-system_log4net.patch
Patch6: nant-0.92-no_netdumbster.patch
Patch7: nant-fixmono42_scripttask.patch
Patch8: nant-0.92-mono-4.5.patch
Patch9: nant-0.92-mono-4.5-config.patch

BuildRequires: make
BuildRequires: mono-devel
BuildRequires: nunit2-devel >= 2.6.4
%if 0%{bootstrap}
# Nothing here if we're bootstrapping
%else
BuildRequires: log4net-devel
%endif
Requires:      nunit2
# Mono only available on these:
ExclusiveArch: %mono_arches

# nunit2 fails to build on armv7hl. Mono crashes. see bug 1923663
# it is too much work to switch to nunit (version 3) at the moment.
ExcludeArch:    armv7hl

%if 0%{bootstrap}
# In bootstrap mode, filter requires of the prebuilt DLLs. Some of these
# require older mono runtime, creating broken rpm deps.
%filter_requires_in %{_prefix}/lib/NAnt/
# Also filter provides of the prebuilt DLLs
%filter_provides_in %{_prefix}/lib/NAnt/
%filter_setup
%endif

%description
NAnt is a free .NET build tool. In theory it is kind of like make
without make's wrinkles. In practice it's a lot like Ant.

%package docs
Summary:	Documentation package for nant
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description docs
Documentation for nant

%package devel
Summary:	Development file for nant
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Development file for %{name}

%prep
%setup -q -n %{name}-%{version}

# install to libdir instead of datadir
sed -i -e "/property name=\"install\.share\"/ s/'share'/'lib'/" NAnt.build
sed -i -e "s,/share/,/lib/," etc/nant.pc.in

# Remove NDoc support
%patch -P1 -p1 -b .no_ndoc
rm src/NAnt.DotNet/Tasks/NDocTask.cs
rm -Rf src/NDoc.Documenter.NAnt
find lib -name 'NDoc*.dll' | xargs rm

# Remove NUnit1 support and fix build with system NUnit.
# Based on Debian's 004-nant-nunit_2.4.dpatch
%patch -P2 -p1 -b .system_nunit
find lib -iname 'nunit*' | xargs rm

# Remove SharpCvsLib support
%patch -P3 -p1 -b .no_sharpcvslib
find lib -name "*SharpCvsLib*.dll" | xargs rm
find lib -name "scvs.exe" | xargs rm

# Use system SharpZipLib which is older than the one bundled with nant
# https://bugzilla.novell.com/show_bug.cgi?id=426065
%patch -P4 -p1 -F 3 -b .system_sharpziplib
find lib -name "*SharpZipLib*.dll" | xargs rm

%patch -P6 -p1 -b .no_netdumbster
rm tests/NAnt.Core/Tasks/MailTaskTest.cs

find . -type d|xargs chmod 755
find . -type f|xargs chmod 644
sed -i 's/\r//' doc/license.html
sed -i 's/\r//' COPYING.txt
sed -i 's/\r//' README.txt
sed -i 's/\r//' doc/releasenotes.html

# Clean out the prebuilt files (unless we're bootstrapping)
# If we're not bootstrapping, leave the files alone:
%if 0%{bootstrap}
echo "BOOTSTRAP BUILD"
%else
echo "NORMAL BUILD, NUKING PREBUILT BUNDLED DLL FILES"
rm -rf lib/*
%endif

# Use system log4net, unless we're bootstrapping.
%if 0%{bootstrap}
# do nothing
%else
%patch -P5 -p1 -b .system_log4net
%endif

%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1

#Fixes for Mono 4
sed -i "s#gmcs#mcs#g" Makefile
sed -i "s#TARGET=mono-2.0#TARGET=mono-4.5#g" Makefile
sed -i "s#dmcs#mcs#g" src/NAnt.Console/App.config
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

%build
make

%install
make install prefix=%{_prefix} DESTDIR=%{buildroot}
find examples -name \*.dll -o -name \*.exe|xargs rm -f
rm -rf %{buildroot}%{_datadir}/NAnt/doc
rm -rf %{buildroot}%{_prefix}/lib/doc/NAnt

# Flush out the binary bits that we used to build, unless we're bootstrapping.
%if 0%{bootstrap}
# Do nothing
%else
rm -rf %{buildroot}%{_prefix}/lib/NAnt/bin/lib
rm -rf %{buildroot}%{_prefix}/lib/NAnt/bin/log4net.dll
%endif

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT/%{_prefix}/lib/pkgconfig/* $RPM_BUILD_ROOT/%{_libdir}/pkgconfig


%files
%{!?_licensedir:%global license %%doc}
%license COPYING.txt
%doc README.txt doc/*.html
%{_bindir}/nant
%{monodir}/NAnt/

%files docs
%doc examples/* doc/help/*

%files devel
%{_libdir}/pkgconfig/nant.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.92-38
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1:0.92-30
- disable arch armv7hl

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-27
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 03 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1:0.92-24
- Properly support mono-4.5 target framework by adding an extra section to the config file

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:0.92-17
- Rebuild due to bug in RPM (RHBZ #1468476)

* Thu Mar 16 2017 Timotheus Pokorra <tp@tbits.net> - 1:0.92-16
- Rebuilt for log4net 2.0.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Tom Callaway <spot@fedoraproject.org> - 1:0.92-14
- rebuild for new log4net

* Thu Oct 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 1:0.92-13
- Non bootstrap build

* Thu Oct 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 1:0.92-12
- aarch64 bootstrap

* Fri Aug 26 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> 1:0.92-11
- requires nunit2 to build, does not work with nunit (version 3)

* Thu Jun 16 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> 1:0.92-10
- fix for Mono 4.2 for compiling ScriptTasks (see https://github.com/nant/nant/issues/161)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Tom Callaway <spot@fedoraproject.org> - 0.92-8
- rebuild for new log4net

* Fri Nov 20 2015 Than Ngo <than@redhat.com> - 0.92-7
- non-bootstrap build

* Fri Nov 20 2015 Than Ngo <than@redhat.com> - 0.92-6
- enable bootstrap for s390*/powerpc64

* Sat Nov 14 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> 1:0.92-5
- force a rebuild so that nant requires the updated log4net (fixes bug #1281954)

* Thu Jul 16 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> 1:0.92-4
- fix post bootstrap build, require nunit-devel >= 2.6.4 (fixes bug #1239705)
- also fix problems with missing NDoc and netDumbster dlls

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.92-2
- Post bootstrap (mono4) rebuild
- Minor spec cleanups, use %%license
- use %%mono_arches

* Fri May 15 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> 0.92-1
- upgrade to NAnt 0.92, build for Mono 4

* Tue Oct 14 2014 Karsten Hopp <karsten@redhat.com> 0.90-17
- change exclusivearch from ppc64 to power64 macro to include ppc64le

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.90-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun  9 2014 Tom Callaway <spot@fedoraproject.org> - 1:0.90-15
- rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.90-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Kalev Lember <kalevlember@gmail.com> - 1:0.90-13
- Drop scrollkeeper handling

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.90-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.90-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.90-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.90-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Christian Krause <chkr@fedoraproject.org> - 1:0.90-8
- Unbootstrap

* Sun Nov 20 2011 Christian Krause <chkr@fedoraproject.org> - 1:0.90-7
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Tue Apr 19 2011 Dan Horák <dan[at]danny.cz> - 1:0.90-6
- updated the supported arch list

* Sat Apr 09 2011 Kalev Lember <kalev@smartlink.ee> - 1:0.90-5
- Unbootstrap

* Fri Apr 08 2011 Kalev Lember <kalev@smartlink.ee> - 1:0.90-4
- Fixed build in bootstrap mode
- Added a patch to build without NDoc
- Added a patch to build with system mono-nunit instead of the bundled copy and
  removed support for mono-nunit22
- Build without SourceControl support to avoid SharpCvsLib dep
- Patch to build with system SharpZipLib
- Build with system log4net if we aren't bootstrapping

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.90-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1:0.90-2.1
- Fix bootstrap makefile

* Mon Oct 25 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1:0.90-2
- More build path fixes

* Mon Oct 25 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1:0.90-1.1
- Correct build paths

* Thu Oct 14 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1:0.90-1
- Bump to 0.90
- Replace patch 2, fix other patches
- Fix mono-1.0 bits
- Add devel subpackage

* Thu Feb 11 2010 Karsten Hopp <karsten@redhat.com> 1:0.85-34
- enable builds on s390(x)

* Tue Dec  1 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1:0.85-33
- disable bootstrap

* Tue Dec  1 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1:0.85-32.1
- bootstrap again

* Thu Oct 29 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:0.85-31
- rebuild because mono-ndoc "cleverly" encodes its build date into its ABI ver

* Fri Jul 31 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.85-30
- clarify comments on bootstrapping

* Thu Jul 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.85-29
- unbootstrap

* Thu Jul 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.85-28.1
- bootstrap to get mono-ndoc rebuilt

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.85-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar  3 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.85-27
- unbootstrap

* Mon Mar  2 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.85-26.2
- fix BR to be wrapped by bootstrap

* Mon Mar  2 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.85-26.1
- bootstrap... again. *sigh*

* Mon Mar  2 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.85-26
- disable bootstrap

* Mon Mar  2 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.85-25.1
- proper conditionals for bootstrapping

* Mon Mar  2 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.85-24.1
- bootstrap hack (to recover from mass rebuild)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.85-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.85-23
- undo bootstrapping hack
- readd BR mono-sharpcvslib-devel (yes, it is circular, mono is a mess)

* Tue Dec 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.85-22.1
- bootstrapping hack
- don't monkey with patches, bad form

* Thu Dec 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1:0.85-22
- rebuild
- removed BR mono-sharpcvslib-devel (circular dep with mono-sharpcvslib)

* Fri Jun 06 2008 Caolán McNamara <caolanm@redhat.com> - 1:0.85-21
- rebuild for dependancies

* Thu Apr 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.85-20
- don't use prebuilt binary bits

* Mon Apr  7 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1:0.85-19
- Downgrade to 0.85 because of issues with boo package as discussed on
  bug #435898).  add Epoch: 1 :(
- Add nant-0.85-api.patch from David Nielsen to enable build on F-9

* Thu Mar 06 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.86-5
- bump to beta 1

* Mon Nov 12 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.85-17
- removed excludearch in favour of exclusivearch

* Mon Nov 12 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.85.15
- removed fc5 and fc6 support
- fixed small errors in the code base

* Sun Dec 17 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.85-11
- No longer the RC release

* Sat Sep 16 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.85-10
- more hacks and slashes...

* Sat Sep 16 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.85-9
- more 64bit fixes

* Sat Sep 16 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.85-8
- scrollkeeper fixes

* Wed Sep 06 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.85-7
- FC5 and FC6 fixes (libdir)

* Wed Jul 19 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.85-6
- Security fix to spec file
- Other spec file fixes

* Sun Jul 09 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.85-5
- fixes to EOLs
- added R scrollkeeper
- changed group

* Sat Jul 08 2006 John Mahowald  <jpmahowald@gmail.com> - 0.85-4
- libdir fix

* Wed Jun 07 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.85-rc4-3
- Added docs package
- Added post and postun for docs
- Removed debuginfo package (empty)

* Sat Jun 03 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.85-rc4-1
- Initial import for FC Extras

