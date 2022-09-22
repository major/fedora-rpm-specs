Summary: A system for electronic distribution of mathematics
Name: logiweb
Version: 0.2.12
Release: 15%{?dist}
License: GPLv2+
Url: http://logiweb.eu/
Source0: http://logiweb.eu/0.2/%{version}/download/%{name}-%{version}.tar.gz

ExcludeArch: aarch64 %{power64} s390 s390x

BuildRequires:  gcc
BuildRequires: clisp, vim-common, tex(latex), dvipdfm
BuildRequires: make
Requires: tex(latex), dvipdfm, gcc

%description
Logiweb allows to web publish 'Logiweb pages', i.e.
journal quality articles which contain machine readable objects
like  programs, testsuites, definitions, axioms, lemmas, and
proofs. Among other, Logiweb is suited for literate programming,
for publication of machine verified proofs, and for writing
proof checkers. Logiweb allows Logiweb pages to reference
previously published Logiweb pages such that programs on a page
may call programs on referenced pages, proofs on a page may
reference lemmas on referenced pages, and so on.

%prep
%setup -q

%build
# Compilation of lgwam.c may be slow and memory consuming, c.f.
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=37448
# Using CFLAGS=optflags makes things worse and is like asking
# for trouble. But compilation has succeeded on a 4GB machine.
rm -f src/pages.c
ulimit -s unlimited
make CFLAGS="%{optflags}"

%install
make \
  DESTDIR=%{buildroot} \
  BINDIR=%{buildroot}%{_bindir} \
  MANDIR=%{buildroot}%{_mandir} \
  DOCDIR=%{buildroot}%{_docdir}/%{name} \
  install


%files
%doc README COPYING CHANGELOG TODO

# lgwam is invoked using #!/usr/bin/lgwam, so its path is hardcoded
/usr/bin/lgwam
%{_bindir}/lgc
%{_mandir}/man1/lgc.1.gz
%{_mandir}/man1/lgwam.1.gz
%{_mandir}/man5/lgc.5.gz
%{_mandir}/man5/lgc.conf.5.gz
%{_mandir}/man5/logiweb.5.gz
%{_mandir}/man7/logiweb.7.gz
%{_docdir}/%{name}/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul  3 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.12-1
- Update to 0.2.12

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 23 2010 Klaus Grue <grue@diku.dk> 0.2.8-11
- In present rpmspec: Added gcc to Requires
- In lgwam.c: changed execl() error message to execl(/usr/bin/gcc)

* Thu Mar 25 2010 Klaus Grue <grue@diku.dk> 0.2.8-10
- In present rpmspec: Changed to tex(latex) in Requires and BuildRequires

* Fri Mar 19 2010 Klaus Grue <grue@diku.dk> 0.2.8-9
- In present rpmspec: Added "ExcludeArch: ppc64"
- In present rpmspec: Claimed ownership of %%{_docdir}/%%{name}/
- Removed execute permission for src/testsuite/pages/compile.sh
- Changed to '/bin/bash compile.sh' in src/testsuite/pages/makefile

* Mon Mar 15 2010 Klaus Grue <grue@diku.dk> 0.2.8-8
- In makefile: Removed 'ulimit -s unlimited'
- In src/boot/lgc/makefile: Removed 'ulimit -s unlimited'
- In present rpmspec: Added 'ulimit -s unlimited' to %%build
- Recognize optimized constructs by name when fingerprints are absent:
- In src/boot/lgc/optimize.lisp: Let *opti* default to :undefined
- In src/boot/lgc/codify.lisp: Use *opti2* when *opti* equals :undefined
- Replace src/boot/lgc/fingerprint.lisp by empty file

* Fri Mar 12 2010 Klaus Grue <grue@diku.dk> 0.2.8-7
- Undid changes back to 0.2.8-4
- In makefile: Added 'ulimit -s unlimited' two places
- In makefile: Added rpmtest4 target for testing i386 build
- In lgwam.c:  PRINTGC in lgwam.c set back to FALSE
- In lgwam.c:  Printing pointer sized when PRINTGC is TRUE (c.f. 0.2.8-5)

* Mon Feb 22 2010 Klaus Grue <grue@diku.dk> 0.2.8-6
- Now it is configurable whether normal output goes to stdout or stderr
- Increased verbosity of lgc to '-v 4' in SELFARG in makefile

* Sun Feb 21 2010 Klaus Grue <grue@diku.dk> 0.2.8-5
- Now printing pointer sized when PRINTGC is TRUE
- Now all output PRINTGC output goes to stderr

* Sat Feb 20 2010 Klaus Grue <grue@diku.dk> 0.2.8-4
- Computation of amount of physical RAM has been corrected
- Changed 'Heap too small' message to 'Ran out of physical RAM'

* Thu Feb 18 2010 Klaus Grue <grue@diku.dk> 0.2.8-3
- Rebuild of 0.2.8-2 to get ulimit right
- PRINTGC in lgwam.c has be set to TRUE to get debugging information

* Wed Feb 17 2010 Klaus Grue <grue@diku.dk> 0.2.8-2
- Thanks to Mamoru Tasaka, Fedora, for patience and help building on Koji
- In src/boot/lgc/makefile: Set ulimit
- Present rpmspec now BuildRequires vim-common, texlive-latex, and dvipdfm

* Mon Feb 08 2010 Klaus Grue <grue@diku.dk> 0.2.8-1
- To allow Fedora build, main.lisp no longer configures *terminal-io*

* Fri Feb 05 2010 Klaus Grue <grue@diku.dk> 0.2.7-1
- Updated src/dist/cygwin/README
- Updated src/dist/cygwin/setup.exe
- Removed obsolete documentation in lgc/src/dist/
- Removed handling of obsolete documentation in lgc/makefile
- Changed year 2009 to 2010 in copyright notice in lgc/src/lgc.lgs
- Added info on DESTDIR in README and makefile
- Added src/boot/ for generating pages.c from scratch
- Added 'BuildRequires: clisp' to this rpmspec
- Changed 'make %%{?_smp_mflags}' to 'make' in this rpmspec
- Added 'rm -f src/pages.c' to %%build in this rpmspec
- Removed '---' in 'Cannot parse beyond this point' error message

* Tue Jan 05 2010 Klaus Grue <grue@diku.dk> 0.2.6-1
- Repaired date of changelog entry 0.2.5
- Did backport. Version 0.1.10 is a backport of Version 0.2.6
- In base.lgs: Made header charge monotonic to allow backport
- In lgc.lgs:  Changed eager to late define to avoid warning in backport
- In man.5:    Corrected two urls
- In makefile: Changed '--exclude dist' to '--exclude ${DIR}/dist' two places

* Sat Dec 05 2009 Klaus Grue <grue@diku.dk> 0.2.5-1
- Moved some standard constructs from lgc.lgs to base.lgs
- Added makefile to /usr/share/doc/logiweb/examples/
- In lgwam.c:  Introduced reduced size default testsuite
- In lgc.lgs:  ""D may now occur in body (but still not in string)
- In lgc.lgs:  Removed redundant 'fetch' messages at verbosity level 3
- In lgc.lgs:  Changed 'unpack' to 'trisect' and 'structure' to'unpack'
- In lgc.lgs:  Bugfix: Verifier now accepts pages with no definitions
- In base.lgs: page...end page no longer macro expands charge definitions
- In check.lgs:Corrected Curry and uncurry unitacs

* Sun Oct 04 2009 Klaus Grue <grue@diku.dk> 0.2.4-1
- In makefile: rpm target now copies logiweb.spec to dist/yum
- In lgc.lgs:  corrected chargedef generation in page ( " , " ) ... end page
- In base.lgs: enhanced error message layout

* Sun Sep 20 2009 Klaus Grue <grue@diku.dk> 0.2.3-1
- Thanks to    Fabian Affolter, Fedora
- In rpmspec:  Added %%{?dist} macro to Release field
- In rpmspec:  Changed License field from GPLv2 to GPLv2+
- In rpmspec:  Corrected value of Source field
- In rpmspec:  Renamed Source field to Source0
- In rpmspec:  Changed BuildRoot field to recommended value
- In rpmspec:  Added %%{?_smp_mflags} macro in build section
- In makefile: Added CFLAGS variable
- In rpmspec:  Transferred %%{optflags} to CFLAGS in build section
- In lgwam.c:  Got rid of 140 warnings from -Wall in %%{optflags}
- In rpmspec:  Used macros in file section
- In rpmspec:  Changed examples/* to examples/ in file section
- In rpmspec:  Changed $${RPM_BUILD_ROOT} to %%{buildroot}
- In rpmspec:  Changed defattr(-,root,root) to defattr(-,root,root,-)
- In makefile: Made install target preserve timestamps
- In rpmspec:  Transferred values to BINDIR, MANDIR, and DOCDIR
- In makefile: Install now copies logiweb.* and version to /usr/share/...
- In makefile: Changed $${RPM11} to $${RPM11}* to cope with %%{?dist}
- In makefile: Added /usr/share/doc/logiweb/examples to cygwin package
- In makefile: Added rpmtest3 target which exercises mock

* Tue Sep 15 2009 Klaus Grue <grue@diku.dk> 0.2.2-1
- Added rpmtest1 and rpmtest2 make targets
- Modified rpm make target to make rpmlint happy
- Added SIGSEGV handling

* Wed Sep 2 2009 Klaus Grue <grue@diku.dk> 0.2.1-1
- Modified make targets for generating Debian packages

* Wed Aug 26 2009 Klaus Grue <grue@diku.dk> 0.2.0-1
- Ported from clisp to C
- Modified Logiweb source language
