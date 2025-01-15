%global giturl  https://github.com/eprover/eprover

Name:		E
Version:	3.2.5
Release:	%autorelease
Summary:	Equational Theorem Prover

# The content is GPL-2.0-or-later OR LGPL-2.1-or-later.  The remaining licenses
# cover the various fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
License:	(GPL-2.0-or-later OR LGPL-2.1-or-later) AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
URL:		https://www.eprover.org/
VCS:		git:%{giturl}.git
Source0:	%{giturl}/archive/%{name}-%{version}.tar.gz
# Bibliography file, courtesy of Debian, with modifications by Jerry James
Source1:	eprover.bbl
# Unbundle picosat
Patch:		%{name}-picosat.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

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
%autosetup -p0 -n eprover-%{name}-%{version}

%conf
# Fix the character encoding of one file
iconv -f ISO8859-1 -t UTF-8 DOC/E-REMARKS > DOC/E-REMARKS.utf8
touch -r DOC/E-REMARKS DOC/E-REMARKS.utf8
mv -f DOC/E-REMARKS.utf8 DOC/E-REMARKS

# Preserve timestamps when installing
sed -i 's|cp \$1|cp -p $1|' development_tools/e_install

# Put the bibliography file where LaTeX will see it
cp -p %{SOURCE1} DOC

# Make sure we do not use the bundled picosat
rm -fr CONTRIB

%build
# Set up Fedora CFLAGS and paths
sed -e "s|^EXECPATH = .*|EXECPATH = %{buildroot}%{_bindir}|" \
    -e "s|^MANPATH = .*|MANPATH = %{buildroot}%{_mandir}/man1|" \
    -e "s|^CFLAGS.*|CFLAGS     = %{build_cflags} \$(BUILDFLAGS) -I../include|" \
    -e "s|^LDFLAGS.*|LDFLAGS    = %{build_ldflags}|" \
    -i Makefile.vars

# smp_mflags causes unwelcome races, so we will not use it
make remake
ln -s eprover-ho PROVER/eprover
make man

# We need one more pdflatex invocation to fix up cross references
cd DOC
bibtex eprover || :
pdflatex eprover
cd -

%install
%make_install
mv %{buildroot}%{_bindir}/eprover-ho %{buildroot}%{_bindir}/eprover

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
%autochangelog
