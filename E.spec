Name:		E
Version:	2.6
Release:	6%{?dist}
Summary:	Equational Theorem Prover

# The content is GPL-2.0-or-later OR LGPL-2.1-or-later.  The remaining licenses
# cover the various fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
License:	(GPL-2.0-or-later OR LGPL-2.1-or-later) AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
URL:		https://www.eprover.org/
Source0:	https://wwwlehre.dhbw-stuttgart.de/~sschulz/WORK/E_DOWNLOAD/V_%{version}/%{name}.tgz
# Bibliography file, courtesy of Debian, with modifications by Jerry James
Source1:	eprover.bbl
# Unbundle picosat
Patch0:		%{name}-picosat.patch
# Fix potential buffer overflows due to use of sprintf
Patch1:		%{name}-format-overflow.patch
# Fix linking in SIMPLE_APPS
Patch2:		%{name}-simple-apps.patch

BuildRequires:	gcc
BuildRequires:	help2man
BuildRequires:	make
BuildRequires:	picosat-devel
BuildRequires:	tex(latex)
BuildRequires:	tex(supertabular.sty)
# You can verify the CASC results here: http://www.cs.miami.edu/~tptp/CASC/J4/

%description
E is a purely equational theorem prover for full first-order logic.
That means it is a program that you can stuff a mathematical
specification (in first-order format) and a hypothesis into, and which
will then run forever, using up all of your machines' resources.  Very
occasionally it will find a proof for the hypothesis and tell you so.

E's inference core is based on a modified version of the superposition
calculus for equational clausal logic.  Both clausification and
reasoning on the clausal form can be documented in checkable proof
objects.

E was the best-performing open source software prover in the 2008 CADE
ATP System Competition (CASC) in the FOF, CNF, and UEQ divisions.  In
the 2011 competition, it won second place in the FOF division, and
placed highly in CNF and UEQ.

%prep
%autosetup -p0 -n %{name}

# Fix the character encoding of one file
iconv -f ISO8859-1 -t UTF-8 DOC/E-REMARKS > DOC/E-REMARKS.utf8
touch -r DOC/E-REMARKS DOC/E-REMARKS.utf8
mv -f DOC/E-REMARKS.utf8 DOC/E-REMARKS

# Preserve timestamps when installing
sed -i 's|cp \$1|cp -p $1|' development_tools/e_install

# Put the bibliography file where LaTeX will see it
cp -p %{SOURCE1} DOC

# Make sure we do not use the bundled picosat
rm -fr include/picosat.h CONTRIB

%build
# Set up Fedora CFLAGS and paths
sed -e "s|^EXECPATH = .*|EXECPATH = %{buildroot}%{_bindir}|" \
    -e "s|^MANPATH = .*|MANPATH = %{buildroot}%{_mandir}/man1|" \
    -e "s|^CFLAGS.*|CFLAGS     = %{build_cflags} \$(BUILDFLAGS) -I../include|" \
    -e "s|^LDFLAGS.*|LDFLAGS    = %{build_ldflags}|" \
    -i Makefile.vars

# smp_mflags causes unwelcome races, so we will not use it
make remake
make man

%install
%make_install

%check
./PROVER/eprover -s --tstp-in EXAMPLE_PROBLEMS/TPTP/SYN190-1.p \
  | sed '/Freeing FVIndex/d' | tail -1 > test-results
echo "# SZS status Unsatisfiable" > test-expected-results
diff -u test-results test-expected-results


%files
%license COPYING
%doc README.md README.server
%doc DOC/ANNOUNCE
%doc DOC/bug_reporting
%doc DOC/CONTRIBUTORS
%doc DOC/E-*.html
%doc DOC/eprover.pdf
%doc DOC/E-REMARKS
%doc DOC/E-REMARKS.english
%doc DOC/grammar.txt
%doc DOC/NEWS
%doc DOC/sample_proofs.html
%doc DOC/sample_proofs_tstp.html
%doc DOC/TODO
%doc DOC/TSTP_Syntax.txt
%doc DOC/WISHLIST
%{_bindir}/checkproof
%{_bindir}/e_axfilter
%{_bindir}/e_deduction_server
%{_bindir}/e_ltb_runner
%{_bindir}/e_stratpar
%{_bindir}/eground
%{_bindir}/ekb_create
%{_bindir}/ekb_delete
%{_bindir}/ekb_ginsert
%{_bindir}/ekb_insert
%{_bindir}/epclextract
%{_bindir}/eprover
%{_mandir}/man1/checkproof.1*
%{_mandir}/man1/e_axfilter.1*
%{_mandir}/man1/e_deduction_server.1*
%{_mandir}/man1/e_ltb_runner.1*
%{_mandir}/man1/e_stratpar.1*
%{_mandir}/man1/eground.1*
%{_mandir}/man1/ekb_create.1*
%{_mandir}/man1/ekb_delete.1*
%{_mandir}/man1/ekb_ginsert.1*
%{_mandir}/man1/ekb_insert.1*
%{_mandir}/man1/epclextract.1*
%{_mandir}/man1/eprover.1*

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 2.6-4
- Convert License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul  1 2021 Jerry James <loganjerry@gmail.com> - 2.6-1
- Version 2.6

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug  3 2020 Jerry James <loganjerry@gmail.com> - 2.5-1
- Version 2.5

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Jerry James <loganjerry@gmail.com> - 2.4-1
- New upstream release
- Add -simple-apps patch

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Jerry James <loganjerry@gmail.com> - 2.3-1
- New upstream release
- Add -format-overflow patch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 2.2-1
- New upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 2.1-1
- New upstream release
- Unbundle picosat

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul  8 2017 Jerry James <loganjerry@gmail.com> - 2.0-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep  1 2016 Jerry James <loganjerry@gmail.com> - 1.9.1-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 16 2015 Jerry James <loganjerry@gmail.com> - 1.9-2
- Link with RPM_LD_FLAGS

* Wed Jul 22 2015 Jerry James <loganjerry@gmail.com> - 1.9-1
- New upstream release

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 Jerry James <loganjerry@gmail.com> - 1.8.001-4
- Use license macro

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep  3 2013 Jerry James <loganjerry@gmail.com> - 1.8.001-1
- New upstream version

* Mon Jul 29 2013 Jerry James <loganjerry@gmail.com> - 1.8-1
- New upstream version
- Drop now unneeded -alias patch

* Mon Mar 25 2013 Jerry James <loganjerry@gmail.com> - 1.7-1
- New upstream release

* Wed Feb 13 2013 Jerry James <loganjerry@gmail.com> - 1.6-2
- Add tex(supertabular.sty) BR due to TeXLive 2012 changes

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug  6 2012 Jerry James <loganjerry@gmail.com> - 1.6-1
- New upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May  7 2012 Jerry James <loganjerry@gmail.com> - 1.5-1
- New upstream release

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gamil.com> - 1.4-2
- Rebuild for GCC 4.7

* Mon Aug 22 2011 Jerry James <loganjerry@gmail.com> - 1.4-1
- New upstream release
- Rebuild man pages with newer version of help2man
- Use the Makefile's install target instead of rolling our own

* Sat Jul  2 2011 Jerry James <loganjerry@gmail.com> - 1.3-1
- New upstream release

* Tue Jun 21 2011 Jerry James <loganjerry@gmail.com> - 1.2.001-1
- New upstream release
- Now dual-licensed: GPLv2+ or LGPLv2+
- Drop unnecessary spec file elements (BuildRoot, etc.)
- Use virtual provides for the BRs instead of files
- Install the man pages

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 David A. Wheeler <dwheeler at, dwheeler.com> 1.0.002-3
- Work around local tags

* Mon Dec 22 2008 David A. Wheeler <dwheeler at, dwheeler.com> 1.0.002-2
- Repaired for python2 variations (different releases have different versions
  of python2)

* Mon Dec 22 2008 David A. Wheeler <dwheeler at, dwheeler.com> 1.0.002-1
- Added python2.5 as BuildRequires
- Update to E version 1.0 ("Temi").  This includes...
- Improved eproof script signal handling.
- Fixed a number of warnings with the latest gcc version.
- Updated proof objects to latest SZS ontology.

* Tue Aug 19 2008 David A. Wheeler <dwheeler at, dwheeler.com> 0.999.006-2
- Change executable permissions from 0775 to 0755 
- Use compilation switches (e.g., -O2 instead of pointless -O6, and use -g)
 
* Tue Aug 19 2008 David A. Wheeler <dwheeler at, dwheeler.com> 0.999.006-1
- Initial package

