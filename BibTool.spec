Summary:        A Tool for manipulating BibTeX data bases
Name:           BibTool
Version:        2.68
Release:        10%{?dist}
Source0:        https://github.com/ge-ne/bibtool/releases/download/BibTool_2_68/BibTool-%{version}.tar.gz
Source1:        https://github.com/ge-ne/bibtool/releases/download/BibTool_2_68/BibTool-%{version}.tar.gz.asc
# Imported from public key servers; author provides no fingerprint!
Source2:        gpgkey-E2A609830CE1675666671B86EA2168BE699213A2.gpg
URL:            http://www.gerd-neugebauer.de/software/TeX/BibTool/
Patch0:         BibTool-2.51-regex.patch
Patch1:         0001-old-font-commands-added.patch
Patch2:         0001-make-doc-work-with-LuaTeX-0.85.patch
Patch3:         0001-fix-duplicate-case-fix.patch
Patch4:         0001-support-for-make-check-fixed.patch
License:        GPL-2.0-or-later AND CC-BY-SA-3.0
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tex(latex) tex-bibtex tex-makeindex tex(luatex85.sty)
BuildRequires:  gnupg2
# make check requires (standard in the Fedora buildroot, not EPEL):
BuildRequires:  perl-interpreter perl(base) perl(strict) perl(warnings) perl(Time::HiRes)

%description
BibTeX provides an easy to use means to integrate citations and
bibliographies into LaTeX documents. But the user is left alone with
the management of the BibTeX files. The program BibTool is intended to
fill this gap. BibTool allows the manipulation of BibTeX files which
goes beyond the possibilities --- and intentions --- of BibTeX.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name} -p 1
sed -i -e 's%^#!/usr/local/bin/tclsh%#! %{_bindir}/tclsh%' Tcl/bibtool.tcl
sed -i -e 's%^#!/usr/local/bin/perl%#! %{_bindir}/perl%' Perl/bibtool.pl
# configure will recreate the directory, but only with config.h within
rm -rf regex-0.12

%build
%configure --libdir=%{_datadir}
sed -i -e 's#@kpathsea_lib_static@##' makefile
%make_build CFLAGS="$RPM_OPT_FLAGS"
make doc

%check
make check

%install
make install INSTALLPREFIX=$RPM_BUILD_ROOT INSTALL='install -p -m 755'
make install-man INSTALLPREFIX=$RPM_BUILD_ROOT INSTALL='install -p -m 644'

%files
%license COPYING
%doc Changes.tex README.md THANKS
%doc doc/bibtool.pdf doc/ref_card.pdf
%doc Perl/ Tcl/
%{_bindir}/bibtool
%{_datadir}/BibTool/
%{_mandir}/man1/bibtool.1*

%changelog
* Wed Mar 29 2023 Michael J Gruber <mjg@fedoraproject.org> - 2.68-10
- Adjust patch macro usage to rpm >= 4.18

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.68-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 Michael J Gruber <mjg@fedoraproject.org> - 2.68-8
- SPDX migration

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.68-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Michael J Gruber <mjg@fedoraproject.org> - 2.68-6
- enable test suite as per packaging guidelines

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.68-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.68-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 14 2020 Michael J Gruber <mjg@fedoraproject.org> - 2.68-1
- rebase to BibTool 2.68 (bz # 1823402)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Michael J Gruber <mjg@fedoraproject.org> - 2.67-11
- switch to SSL source URL
- verify package signature

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Michael J Gruber <mjg@fedoraproject.org> - 2.67-8
- fix FTBFS (#1603259) in rawhide

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 7 2018 Orion Poplawski <orion@nwra.com> - 2.67-6
- Add BR gcc
- Use %%license and other spec cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Michael J Gruber <mjg@fedoraproject.org> - 2.67-1
- rebase to BibTool 2.67

* Tue Nov 29 2016 Michael J Gruber <mjg@fedoraproject.org> - 2.66-3
- make doc work with newer KOMA classes 

* Tue Nov 29 2016 Michael J Gruber <mjg@fedoraproject.org> - 2.66-2
- make doc work with LuaTeX 0.85

* Tue Nov 22 2016 Michael J Gruber <mjg@fedoraproject.org> - 2.66-1
- bugfix and feature release

* Tue Aug 02 2016 Michael J Gruber <mjg@fedoraproject.org> - 2.65-1
- bugfix and feature release

* Tue Jun 07 2016 Michael J Gruber <mjg@fedoraproject.org> - 2.64-1
- rebase to BibTool 2.64

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Michael J Gruber <mjg@fedoraproject.org> - 2.63-1
- rebase to BibTool 2.63

* Mon Oct 12 2015 Michael J Gruber <mjg@fedoraproject.org> - 2.61-1
- rebase to BibTool 2.61

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Michael J Gruber <mjg@fedoraproject.org> - 2.58-1
- rebase to BibTool 2.58
- drop obsolete patch

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.55-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.55-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Michael J Gruber <mjg@fedoraproject.org> 2.55-3
- adjust BR to new texlive (fix FTB for doc)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Michael J Gruber <mjg@fedoraproject.org> 2.55-1
- rebase to BibTool 2.55
- dump patch1
- fix configure droppings in makefile (botched kpathsea detection)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Michael J Gruber <mjg@fedoraproject.org> 2.53-1
- rebase to BibTool 2.53

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 18 2011 Michael J Gruber <mjg@fedoraproject.org> 2.51-1
- rebase to BibTool 2.51
- remove DESTDIR part of regex_DESTDIR patch (use INSTALLPREFIX from 2.51)
- fix Doc/Makefile
- follow switch from dvi doc to pdf doc
- remove exec bit for installed man
- convert latin1 file to UTF-8

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.48-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.48-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.48-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 Patrice Dumas <pertusus@free.fr> 2.48-7
- add #define __USE_GNU since in regex GNU extensions are used
- keep timestamps and fix man page permissions

* Mon Jan 29 2007 Patrice Dumas <pertusus@free.fr> 2.48-6
- use system regex (#225108)
- honor optflags (#225108)
- merge honor_DESTDIR diff with regex changes in regex_DESTDIR
- don't ship c_lib.dvi

* Sun Sep 10 2006 Patrice Dumas <pertusus@free.fr> 2.48-5
- rebuild for FC6

* Thu Feb 16 2006 Patrice Dumas <pertusus@free.fr> 2.48-4
- rebuild for fc5

* Fri Sep  2 2005 Patrice Dumas <pertusus@free.fr> 2.48-3
- change shebangs in example scripts

* Thu Jul 14 2005 Patrice Dumas <pertusus@free.fr> 2.48-2
- update to 2.48
- use fedora template 

* Mon Sep 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.44-1mdk
- added in contribs by Guillaume Rousse <g.rousse@linux-mandrake.com>
- first mdk release
