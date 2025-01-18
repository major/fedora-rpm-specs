Summary: Emacs Speech interface
Name: emacspeak
Version: 60.0
Release: 2%{?dist}
# main lisp files are GPL2+
License: GPL-2.0-or-later AND BSD-3-Clause
Source: https://github.com/tvraman/emacspeak/releases/download/%{version}/%{name}-%{version}.tar.bz2
URL: http://emacspeak.sourceforge.net/
BuildRequires: emacs
BuildRequires: espeak-ng-devel
BuildRequires: gcc-c++
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: texinfo
BuildRequires: tcl-devel < 1:9
BuildRequires: make
Requires: emacs(bin) >= %{_emacs_version}
Requires: tclx

%description
Emacspeak is a speech interface that allows visually impaired users to
interact independently and efficiently with the computer. Emacspeak has
dramatically changed how the author and hundreds of blind and visually
impaired users around the world interact with the personal computer and
the Internet. A rich suite of task-oriented speech-enabled tools provides
efficient speech-enabled access to the evolving semantic WWW.
When combined with Linux running on low-cost PC hardware,
Emacspeak/Linux provides a reliable, stable speech-friendly solution that
opens up the Internet to visually impaired users around the world.

%prep
%setup -q

chmod a-x etc/COPYRIGHT

%build
# use set_build_flags when available for F27 etc
CXXFLAGS="${CXXFLAGS:-%__global_cxxflags}" ; export CXXFLAGS ; \
LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS
make emacspeak
make espeak


%install
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/emacspeak
cp -pr bash-utils etc lisp media servers sounds stumpwm xsl %{buildroot}%{_datadir}/emacs/site-lisp/emacspeak/

make -C servers/native-espeak install LIBPARENTDIR=%{buildroot}%{_libdir}
ln -sf %{_libdir}/emacspeak/servers/native-espeak/tclespeak.so %{buildroot}%{_datadir}/emacs/site-lisp/emacspeak/servers/native-espeak/

mkdir -p %{buildroot}%{_bindir}
sed -e "s/FLAVOR/emacs/" -e "s!ELCDIR!%{_datadir}/emacs/site-lisp/emacspeak!" etc/emacspeak.sh > %{buildroot}%{_bindir}/emacspeak
chmod 0755 %{buildroot}%{_bindir}/emacspeak

mkdir -p %{buildroot}%{_infodir}
cp -p info/*.info* %{buildroot}%{_infodir}

# remove unwanted data files
( cd %{buildroot}%{_datadir}/emacs/site-lisp/emacspeak
  rm etc/bootstrap.sh
  rm -r etc/pickup-c
  rm -r servers/*outloud*
  rm servers/mac
  rm servers/native-espeak/tclespeak.{cpp,o}
  rm etc/COPYRIGHT
  chmod a-x servers/.servers servers/tts-lib.tcl
  find \( -name .nosearch -o -name Makefile \) -delete
)

%files
%license etc/COPYRIGHT
%doc README*
%{_bindir}/emacspeak
%{_datadir}/emacs/site-lisp/emacspeak/
%{_libdir}/emacspeak
%{_infodir}/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 60.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Jens Petersen <petersen@redhat.com> - 60.0-1
- Update to 60.0
- https://tvraman.github.io/emacspeak/blog/Announce-60.html

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 59.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 29 2024 Parag Nemade <pnemade AT fedoraproject DOT org> - 59.0-3
- Migrate existing license tag to SPDX expression

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 59.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Jens Petersen <petersen@redhat.com> - 59.0-1
- update to 59.0
- http://tvraman.github.io/emacspeak/blog/Announce-59.html

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 54.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 54.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 54.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 54.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 54.0-5
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 54.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 54.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Jens Petersen <petersen@redhat.com> - 54.0-2
- drop the dependency on espeak

* Tue Jun 29 2021 Jens Petersen <petersen@redhat.com> - 54.0-1
- update to 54
- https://github.com/tvraman/emacspeak/blob/54.0/etc/NEWS-54.0
- build with the espeak-ng library

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 45.0-11
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 45.0-8
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 45.0-5
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 45.0-2
- Perl 5.28 rebuild

* Mon Feb 19 2018 Jens Petersen <petersen@redhat.com> - 45.0-1
- update to 45.0

* Mon Feb 19 2018 Jens Petersen <petersen@redhat.com> - 40.0-12
- BR gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 40.0-8
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 40.0-6
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 40.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 40.0-3
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 40.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Nov  7 2014 Jens Petersen <petersen@redhat.com> - 40.0-1
- update to 40.0

* Mon Oct 20 2014 Jens Petersen <petersen@redhat.com> - 39.0-6
- requires emacs(bin) (#1154511)

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 39.0-5
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 39.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 39.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 39.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Fri Nov 29 2013 Jens Petersen <petersen@redhat.com> - 39.0-1
- update to 39.0

* Tue Nov 12 2013 Jens Petersen <petersen@redhat.com> - 38.0-7
- build espeak module with optflags (#225727)

* Thu Oct 24 2013 Jens Petersen <petersen@redhat.com> - 38.0-6
- update the old FSF address that was in some of the elisp files

* Thu Oct 24 2013 Jens Petersen <petersen@redhat.com> - 38.0-5
- require and default to espeak

* Wed Oct 23 2013 Jens Petersen <petersen@redhat.com> - 38.0-4
- build espeak module, so package is now arch
- does not need findutils to build (#225727)
- use %%global instead of %%define (#225727)
- lots of rpmlint cleanup (#225727)
  remove outloud, dtk, mac, and devel server files
  remove python files for now

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 25 2013 Petr Pisar <ppisar@redhat.com> - 38.0-2
- Perl 5.18 rebuild

* Tue Jul 23 2013 Jens Petersen <petersen@redhat.com> - 38.0-1
- update to 38.0

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 37.0-3
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 37.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Jens Petersen <petersen@redhat.com> - 37.0-1
- update to 37.0

* Mon Jul 30 2012 Jens Petersen <petersen@redhat.com> - 36.0-2
- patch tclsh8.4_ia32 in 32-outloud

* Wed Jul 25 2012 Jens Petersen <petersen@redhat.com> - 36.0-1
- update to 36.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Jens Petersen <petersen@redhat.com> - 29.0-1
- update to 29.0
- no longer need emacspeak-28.0-no-httpd.patch and emacspeak-28.0-tmpfile.patch

* Fri Sep 26 2008 Jens Petersen <petersen@redhat.com> - 28.0-3
- (CVE-2008-4191) fix tmpfile vulnerability in extract-table.pl with
  emacspeak-28.0-tmpfile.patch from upstream svn (#463821)

* Fri Sep 26 2008 Jens Petersen <petersen@redhat.com> - 28.0-2
- fix broken generated deps reported by mtasaka (#463899)
- script the replacement of tcl with tclsh to fix missing dtk-soft
- replace python2.4 with python in HTTPSpeaker.py

* Thu Sep 25 2008 Jens Petersen <petersen@redhat.com> - 28.0-1
- update to 28.0 with emacspeak-28.0-no-httpd.patch
- replace emacspeak-tcl-pkgreq-tclx.patch with sed
- emacspeak-no-linux-espeak.patch no longer needed
- update emacspeak-15.0-fixpref.patch for patch fuzz

* Thu Oct  4 2007 Jens Petersen <petersen@redhat.com> - 26-3.fc8
- use requires instead of prereq for post and preun install-info

* Mon Aug 13 2007 Jens Petersen <petersen@redhat.com>
- some lisp subdirs are BSD

* Mon Jun  4 2007 Jens Petersen <petersen@redhat.com> - 26-2
- update emacspeak-tcl-pkgreq-tclx.patch for espeak script

* Mon May 21 2007 Jens Petersen <petersen@redhat.com> - 26-1
- update to 26
- add emacspeak-no-linux-espeak.patch for missing linux-espeak

* Thu Mar  1 2007 Jens Petersen <petersen@redhat.com> - 25-3
- require emacs (lxo)

* Wed Jan 24 2007 Jens Petersen <petersen@redhat.com> - 25-2
- fix emacspeak-tcl-pkgreq-tclx.patch for ssh-outloud

* Mon Jan 22 2007 Jens Petersen <petersen@redhat.com> - 25-1
- update to version 25
  - update emacspeak-tcl-pkgreq-tclx.patch
- protect install-info in %%post and %%preun (Ville Skyttä, #223685)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 23.0-2.1
- rebuild

* Wed Feb  8 2006 Jens Petersen <petersen@redhat.com> - 23.0-2
- tweak tcl scripts to run tclsh and require Tclx instead, since tclx-8.4
  no longer provides _bindir/tcl

* Sat Feb  4 2006 Jens Petersen <petersen@redhat.com> - 23.0-1
- update to 23.0 release
- make package noarch
- remove .cvsignore files
- remove unnecessary playlists and file (Jef Spaleta, #177760)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar  9 2005 Jens Petersen <petersen@redhat.com> - 21.0-2
- rebuild with gcc 4

* Thu Dec  2 2004 Jens Petersen <petersen@redhat.com> - 21.0-1
- update to latest version

* Wed Oct  6 2004 Jens Petersen <petersen@redhat.com> - 17.0-7
- drop requirement on emacs for emacs-nox users
  (Lars Hupfeldt Nielsen, 134479)

* Thu Sep 30 2004 Jens Petersen <petersen@redhat.com> - 17.0-6
- buildrequire texinfo (Maxim Dzumanenko,124183)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan 13 2003 Jens Petersen <petersen@redhat.com> 17.0-3
- bring back sbin to install path for install-info

* Thu Jan  9 2003 Jeff Johnson <jbj@redhat.com> 17.0-2
- filter unwanted perl(HTML::TableExtract) dependency.

* Mon Jan  6 2003 Jens Petersen <petersen@redhat.com> 17.0-1
- update to 17.0
- adjust source url
- quieten setup
- remove some obsolete cleanup deletions
- use _datadir, _infodir, _bindir, _prefix, and buildroot
- clean buildroot before installing, and at the end
- actually install info dir file entry on install (#74136)
- don't include texi and sgml files in docs dir
- encode spec changelog in utf-8

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jun 10 2002 Trond Eivind Glomsrød <teg@redhat.com> 16.0-1
- 16.0
- Get rid of some zero length files
- Update URL, file location

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Apr  1 2002 Trond Eivind Glomsrød <teg@redhat.com> 15.0-4
- Fix %%preun (#62484)

* Thu Mar 28 2002 Trond Eivind Glomsrød <teg@redhat.com> 15.0-3
- Remove traces of the buildroot from /usr/bin/emacspeak (#62198)

* Fri Mar 22 2002 Trond Eivind Glomsrød <teg@redhat.com> 15.0-2
- Remove CVS directories
- Various other cleanups

* Tue Mar  5 2002 Trond Eivind Glomsrød <teg@redhat.com>
- Add Changelog
- s/Copyright/License/
- Remove vendor/packager
- Use Buildroot
