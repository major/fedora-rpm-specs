Summary:        A Tool for manipulating BibTeX data bases
Name:           BibTool
Version:        2.68
Release:        %autorelease
Source0:        https://github.com/ge-ne/bibtool/releases/download/BibTool_2_68/BibTool-%{version}.tar.gz
Source1:        https://github.com/ge-ne/bibtool/releases/download/BibTool_2_68/BibTool-%{version}.tar.gz.asc
# Imported from public key servers; author provides no fingerprint!
Source2:        gpgkey-E2A609830CE1675666671B86EA2168BE699213A2.gpg
URL:            http://www.gerd-neugebauer.de/software/TeX/BibTool/
Patch0:         0001-build-BibTool-against-system-regex.patch
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
%autochangelog
