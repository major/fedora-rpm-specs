Summary: Completely configurable key-combo grabber for blackbox
Name: bbkeys
Version: 0.9.0
Release: 48%{?dist}
License: MIT
URL: http://bbkeys.sourceforge.net/
Source: http://downloads.sf.net/bbkeys/bbkeys-%{version}.tar.gz
Patch0: bbkeys-0.9.0-gcc43.patch
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: blackbox-devel, perl-interpreter
BuildRequires: libX11-devel, libXext-devel
BuildRequires: make
BuildRequires: autoconf automake

%description
bbkeys is a configurable key-grabber designed for the blackbox window manager
which is written by Brad Hughes.  It is based on the bbtools object code
created by John Kennis and re-uses some of the blackbox window manager classes
as well.  bbkeys is easily configurable via directly hand-editing the user's
~/.bbkeysrc file, or by using the GUI total blackbox configurator, bbconf.


%prep
%autosetup -p1


%build
autoreconf -vi
%configure --datadir=%{_sysconfdir}
%make_build


%install
%make_install
# Clean this up, we package the exact same files cleanly in %%doc
# and it ends up in the wrong place with our override anyway
%{__rm} -rf %{buildroot}%{_sysconfdir}/doc/


%files
%doc AUTHORS BUGS ChangeLog LICENSE NEWS README TODO
%dir %{_sysconfdir}/bbkeys/
%config(noreplace) %{_sysconfdir}/bbkeys/bbkeysrc
%config(noreplace) %{_sysconfdir}/bbkeys/defaultStyle
%{_bindir}/bbkeys
%{_mandir}/man1/bbkeys.1*
%{_mandir}/man5/bbkeysrc.5*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Peter Fordham <peter.fordham@gmail.com> - 0.9.0-42
- Add autoreconf step to build to flush non C99 compatible checks from configure.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.0-33
- spec cleanup and modernization

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 17 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.0-28
- Rebuilt to fix FTBFS, added perl as BR, fixes rhbz#1423271

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 05 2015 Jaromir Capik <jcapik@redhat.com> - 0.9.0-25
- Cleaning the spec

* Wed Jul 01 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.9.0-24
- Add dist-tag (RHBZ #1237152).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-22
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-16
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 24 2008 Matthias Saou <http://freshrpms.net/> 0.9.0-11
- Include patch to fix build failure with gcc 4.3.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 0.9.0-9
- Rebuild for new BuildID feature.

* Fri Aug  3 2007 Matthias Saou <http://freshrpms.net/> 0.9.0-8
- Fix License field, it was "GPL" but should have been "MIT" all along.
- Remove dist tag, since the package will seldom change.

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 0.9.0-7
- Remove old X build requires conditional.

* Thu Mar 29 2007 Matthias Saou <http://freshrpms.net/> 0.9.0-6
- Override _datadir as _sysconfdir to get config files in /etc.
- Mark config files as noreplace.
- Rebuild against new shared libbt from blackbox.
- Switch to use downloads.sf.net source URL.
- Tweak defattr, silence %%setup.
- Escape macros in %%changelog.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 0.9.0-5
- FC6 rebuild.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 0.9.0-4
- FC5 rebuild.

* Wed Feb  8 2006 Matthias Saou <http://freshrpms.net/> 0.9.0-3
- Rebuild for new gcc/glibc.

* Mon Jan 23 2006 Matthias Saou <http://freshrpms.net/> 0.9.0-2
- Add conditional to build with/without modular X depending on FC version.

* Fri Apr  1 2005 Matthias Saou <http://freshrpms.net/> 0.9.0-1
- Update to 0.9.0.

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 0.8.6-4
- Bump release to provide Extras upgrade path.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 0.8.6-3
- Rebuild for Fedora Core 2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.8.6-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar  6 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.6.

* Tue Aug 13 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Sat Jan 12 2002 Jason 'vanRijn' Kasper <vR@movingparts.net>
- removing README.bbkeys and adding BUGS and NEWS

* Sat Jan 5 2002 Jason 'vanRijn' Kasper <vR@movingparts.net>
- gzipping man pages by default and changing file list to reflect this

* Mon Nov 5 2001 Jason 'vanRijn' Kasper <vR@movingparts.net>
- removing bbkeysConfigC and replacing with bbkeysconf.pl

* Tue Sep 18 2001 Jason Kasper <vR@movingparts.net>
- changing to a dynamically-created bbkeys.spec

* Sun Aug 5 2001 Jason Kasper <vR@movingparts.net>
- added to file list for newly included files (docs and man pages)
- install to %%{prefix} instead of /usr

* Sun May 6 2001 Hollis Blanchard <hollis@terraplex.com>
- removed file list in favor of explicit %%files section
- install to /usr instead of /usr/local
- buildroot = /var/tmp/bbkeys-buildroot instead of /tmp/buildroot

