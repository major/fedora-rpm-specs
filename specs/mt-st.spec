Summary: Tool for controlling tape drives
Name: mt-st
Version: 1.8
Release: 2%{?dist}
License: GPL-1.0-or-later
URL: https://github.com/iustin/mt-st
Source0: https://github.com/iustin/mt-st/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: stinit.service
BuildRequires: gcc
BuildRequires: make
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape devices)
can control rewinding, ejecting, skipping files and blocks and more.

Install mt-st if you need a tool to  manage tape drives.


%prep
%autosetup


%build
make CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"


%install
COMPLETIONDIR=%{buildroot}%{bash_completions_dir}
%make_install EXEC_PREFIX=/usr COMPLETIONINSTALLDIR=$COMPLETIONDIR SBINDIR=%{buildroot}%{_bindir}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/stinit.service
cd $COMPLETIONDIR
mv mt-st mt


%post
%systemd_post stinit.service

%preun
%systemd_preun stinit.service

%postun
%systemd_postun_with_restart stinit.service


%files
%doc COPYING README.md stinit.def.examples
%{_bindir}/mt
%{_bindir}/stinit
%{_mandir}/man1/mt.1*
%{_mandir}/man8/stinit.8*
%{_unitdir}/stinit.service
%{_datadir}/bash-completion/


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Feb 27 2025 Dan Horák <dan[at]danny.cz> - 1.8-1
- rebased to 1.8
- update for https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin (rhbz#2340890)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 19 2024 Dan Horák <dan[at]danny.cz> - 1.7-6
- handle completions better

* Mon Mar 18 2024 Dan Horák <dan[at]danny.cz> - 1.7-5
- update BR

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 24 2023 Dan Horák <dan[at]danny.cz> - 1.7-1
- rebased to 1.7 (#2189101)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 07 2020 Paweł Marciniak <sunwire+repo@gmail.com> - 1.4-4
- Make will no longer be in BuildRoot by default

* Mon Oct 12 2020 Paweł Marciniak <sunwire+repo@gmail.com> - 1.4-3
- Fix not working autocompletion

* Thu Sep 24 2020 Dan Horák <dan[at]danny.cz> - 1.4-2
- install completions to system directory

* Wed Sep 16 2020 Paweł Marciniak <sunwire+repo@gmail.com> - 1.4-1
- rebased to 1.4

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Dan Horák <dan[at]danny.cz> - 1.3-1
- rebased to 1.3 (#1849416)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Dan Horák <dan[at]danny.cz> - 1.1-22
- fix includes (#1583414)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 22 2014 Dan Horák <dan[at]danny.cz> - 1.1-15
- update man page (#948457)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Dan Horák <dan[at]danny.cz> - 1.1-11
- print all options in stinit's help (#948457)
- switch to systemd scriptlet macros

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Dan Horák <dan[at]danny.cz> - 1.1-9
- spec cleanup

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Jon Ciesla <limburgher@gmail.com> - 1.1-7
- Migrate to systemd, BZ 789926.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 26 2009 Dan Horák <dan[at]danny.cz> - 1.1-4
- stinit initscript updated (#541592)
- fixed License

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug  4 2008 Dan Horak <dan[at]danny.cz> - 1.1-1
- update to upstream version 1.1
- rebase patches

* Mon May 26 2008 Radek Brich <rbrich@redhat.com> - 0.9b-6
- add init script to call /sbin/stinit (#249665)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9b-5
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> - 0.9b-4
- update License
- rebuild for BuildID

* Wed Feb  7 2007 Jindrich Novy <jnovy@redhat.com> - 0.9b-3
- spec fixes
- use mtio.h from kernel-headers instead of the mt-st one

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.9b-2.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.9b-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.9b-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Oct 25 2005 Jindrich Novy <jnovy@redhat.com> 0.9b-2
- fix misleading description of "fsfm" and "bsfm" commands (#171340)

* Thu Sep 22 2005 Jindrich Novy <jnovy@redhat.com> 0.9b-1
- update to mt-st 0.9b

* Thu Apr  7 2005 Jindrich Novy <jnovy@redhat.com> 0.8-5
- add SDLT600 entry to stinit.def.examples,
  suggested by Ralf-Peter Rohbeck (#153305)

* Fri Mar  4 2005 Jindrich Novy <jnovy@redhat.com> 0.8-4
- rebuilt with gcc4

* Thu Feb 10 2005 Jindrich Novy <jnovy@redhat.com> 0.8-3
- remove -D_FORTIFY_SOURCE=2 from CFLAGS, present in RPM_OPT_FLAGS

* Wed Feb  9 2005 Jindrich Novy <jnovy@redhat.com> 0.8-2
- rebuilt with -D_FORTIFY_SOURCE=2

* Mon Aug 09 2004 Jindrich Novy <jnovy@redhat.com> 0.8-1
- updated to 0.8
- updated .redhat patch
- license fixup to GPL

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 26 2003 Than Ngo <than@redhat.com> 0.7-11.1
- add config file for Quantum DLT drive bug #91550

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Feb 22 2003 Than Ngo <than@redhat.com> 0.7-9
- add density code for Quantum SDLT320 from tibbs@math.uh.edu (#84843)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 0.7-7
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Than Ngo <than@redhat.com> 0.7-5
- don't forcibly strip binaries
- clean up a patch file

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Feb 26 2002 Than Ngo <than@redhat.com> 0.7-3
- rebuild

* Wed Feb 20 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.7-2
- Add density code 0x48 for Quantum SDLT220 tape drive (#59442)

* Tue Feb 19 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.7-1
- Update to 0.7

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Apr 24 2001 Than Ngo <than@redhat.com>
- update to 0.6, supports all ioctls up to kernel 2.4.0

* Thu Aug 17 2000 Jeff Johnson <jbj@redhat.com>
- summaries from specspo.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed Jun 14 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Sat Apr 15 2000 Jeff Johnson <jbj@redhat.com>
- permit leading whitespace in config file.
- cortrect spelling error.

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages

* Fri Jan 14 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for Red Hat 6.2.

* Sun Sep  5 1999 Jeff Johnson <jbj@redhat.com>
- enable "datcompression" command (#3654).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Wed Feb 10 1999 Preston Brown <pbrown@redhat.com>
- upgrade to .5b, which fixes some cmd. line arg issues (bugzilla #18)

* Thu Jul 23 1998 Jeff Johnson <jbj@redhat.com>
- package for 5.2.

* Sun Jul 19 1998 Andrea Borgia <borgia@cs.unibo.it>
- updated to version 0.5
- removed the touch to force the build: no binaries are included!
- added to the docs: README.stinit, stinit.def.examples
- made buildroot capable

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
