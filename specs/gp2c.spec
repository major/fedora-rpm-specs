%bcond autoreconf 1

%global upver 0.0.14pl1

Name:           gp2c
Version:        %{gsub %{upver} pl .}
Release:        %autorelease
Summary:        PARI/GP script to C program translator

# The entire source is GPL-2.0-or-later (see README), except:
#   - src/parse.h and src/parse.c are (GPL-3.0-or-later WITH
#     Bison-exception-2.2)
License:        GPL-2.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2
# Additionally, some files that belong to the build system and therefore do not
# contribute to the license of the binary RPMs have other licenses:
#
# FSFULLR:
#   - aclocal.m4
# FSFUL AND GPL-2.0-or-later
# (GPL-2.0-or-later is because it is derived from configure.ac)
#   - configure
# X11:
#   - config/install-sh
SourceLicense:  %{license} AND FSFUL AND FSFULLR AND X11
URL:            https://pari.math.u-bordeaux.fr/
VCS:            git:https://pari.math.u-bordeaux.fr/git/gp2c.git
Source0:        %{url}pub/pari/GP2C/gp2c-%{upver}.tar.gz
Source1:        %{url}pub/pari/GP2C/gp2c-%{upver}.tar.gz.asc
# Public key 0x4522e387, Bill Allombert <Bill.Allombert@math.u-bordeaux.fr>
Source2:        gpgkey-42028EA404A2E9D80AC453148F0E7C2B4522E387.gpg

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
%endif

BuildRequires:  pari-gp
BuildRequires:  pari-devel

BuildRequires:  tex(latex)

BuildRequires:  gpgverify

Requires:       gcc
Requires:       pari-devel%{?_isa}

Recommends:     pari-gp

%description
GP2C is a PARI/GP script to C program translator.


%package        doc
Summary:        Documentation for gp2c
BuildArch:      noarch

%description    doc
This package contains documentation for GP2C.


%prep
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -n gp2c-%{upver}

# Convert to Unicode
iconv -f ISO8859-1 -t UTF-8 ChangeLog > ChangeLog.utf8
touch -r ChangeLog ChangeLog.utf8
mv ChangeLog.utf8 ChangeLog

# Regenerate the documentation
rm -v doc/*.{dvi,html,pdf}


%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif
%configure --with-paricfg='%{_libdir}/pari/pari.cfg'


%build
%make_build

# Build the documentation
# The makefile does not invoke LaTex enough times, so do it manually
cd doc
pdflatex -interaction=nonstopmode gp2c.tex
pdflatex -interaction=nonstopmode gp2c.tex
pdflatex -interaction=nonstopmode gp2c.tex
pdflatex -interaction=nonstopmode type.tex
pdflatex -interaction=nonstopmode type.tex
cd -


%install
%make_install

# We will install the files we want with %%doc below
rm -vrf '%{buildroot}%{_docdir}/gp2c'


%check
%make_build check


%files
%license COPYING
%doc README
%{_bindir}/gp2c
%{_bindir}/gp2c-run
%{_mandir}/man1/gp2c.1*
%{_mandir}/man1/gp2c-run.1*
%{_datadir}/gp2c/


%files doc
%license COPYING
%doc AUTHORS
%doc ChangeLog
%doc BUGS
%doc README
%doc doc/*.pdf
%doc doc/*.png


%changelog
%autochangelog
