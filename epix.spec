## This package has not architecture dependent files,
## except for the -static library that uses.
%global debug_package %{nil}

Name:    epix
Summary: Utilities for mathematically accurate figures
Version: 1.2.22
Release: %autorelease
License: GPL-2.0-or-later
URL:     https://mathcs.holycross.edu/~ahwang/current/ePiX.html
Source0: https://mathcs.holycross.edu/~ahwang/epix/epix-%{version}_withpdf.tar.bz2

BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: automake
BuildRequires: make
BuildRequires: ghostscript
BuildRequires: texinfo
BuildRequires: texlive
BuildRequires: texlive-comment
BuildRequires: texlive-eepic
BuildRequires: texlive-kpathsea-bin
BuildRequires: texlive-latex-bin-bin
BuildRequires: texlive-pst-tools

## ePiX needs a static library to work; it's packaged in the -static subpackage
Requires: %{name}-static = %{version}-%{release}

Requires: %{name}-bash-completion = %{version}-%{release}

Requires: ghostscript
Requires: ImageMagick
Requires: texlive-comment
Requires: texlive-epstopdf-bin
Requires: texlive-eepic
Requires: texlive-pst-tools

%description
ePiX (pronounced like "epic" with a soft "k", playing on "TeX"), a
collection of command line utilities for *nix, creates mathematically
accurate figures, plots, and movies using easy-to-learn syntax. The
output is expressly designed for use with LaTeX.

%package devel
Summary: Header files for %{name}
%description devel
Header files for %{name}.

%package static
Summary: Static library of %{name}
%description static
This package provides a static library of %{name}.

%package data
Summary: Documentation and samples for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
%description data
This package provides .ps .pdf documentation manuals and
sample files of %{name}.

%package bash-completion
Summary: Bash completion support for %{name}
BuildArch: noarch
Requires: bash
%description bash-completion
Bash completion support for the %{name}'s utilities.

%package -n emacs-%{name}
Summary: Compiled elisp files to run %{name} under GNU Emacs
BuildArch: noarch
BuildRequires: emacs
Requires: emacs(bin) >= %{_emacs_version}
Obsoletes: %{name}-emacs < 1.2.14-8

%description -n emacs-%{name}
This package contains the byte compiled elisp packages to run %{name}
with GNU Emacs.

%prep
%autosetup -n %{name}-%{version}

## UTF-8 validating and timestamps preserving
for f in THANKS; do
 iconv -f iso8859-1 -t utf8 $f > $f.new && \
 touch -r $f $f.new && \
 mv $f.new $f
done

##Rename README file of samples
cp -p samples/README samples/samples-README

## Try to fix the Configure WARNING: 'missing' script is too old or missing
autoreconf -ivf

%build
%configure --enable-epix-el
%make_build

%{_emacs_bytecompile} *.el

%install
%make_install

## These directories are not useful
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}/notes

## Rearrangement of documentation files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/samples
install -pm 644 samples/*  $RPM_BUILD_ROOT%{_datadir}/%{name}/samples
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/samples/Makefile*
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/samples/*.tar.gz
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/*.sh

gzip -df doc/manual.pdf.gz
mv doc/manual.pdf epix-manual.pdf
gzip -df doc/manual.ps.gz
mv doc/manual.ps epix-manual.ps

rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/manual.*
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/*_src.tar.gz

## Make bash completion file
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
cp -p $RPM_BUILD_ROOT%{_docdir}/%{name}/config/bash_completions  $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/config/bash_completions

## Make emacs plugin
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
cp -p $RPM_BUILD_ROOT%{_docdir}/%{name}/config/%{name}.el $RPM_BUILD_ROOT%{_emacs_sitestartdir}
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/config/%{name}.el

## Remove config dir
rm -rf $RPM_BUILD_ROOT%{_pkgdocdir}/config

%files
%doc README THANKS ChangeLog NEWS POST-INSTALL
%license COPYING
%{_bindir}/elaps
%{_bindir}/epix
%{_bindir}/flix
%{_bindir}/laps
%{_infodir}/%{name}*
%{_mandir}/man1/epix.1*
%{_mandir}/man1/elaps.1*
%{_mandir}/man1/laps.1*
%{_mandir}/man1/flix.1*

%files devel
%doc README THANKS ChangeLog NEWS POST-INSTALL
%license COPYING
%{_includedir}/%{name}/
%{_includedir}/%{name}.h

%files static
%doc README POST-INSTALL
%license COPYING
%{_libdir}/%{name}/

%files data
%doc epix-manual.* README THANKS ChangeLog NEWS POST-INSTALL
%doc samples/samples-README
%license COPYING
%{_datadir}/%{name}/

%files bash-completion
%doc README POST-INSTALL
%license COPYING
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}

%files -n emacs-%{name}
%doc README POST-INSTALL
%license COPYING
%{_emacs_sitelispdir}/%{name}/
%{_emacs_sitestartdir}/*.el

%changelog
%autochangelog
