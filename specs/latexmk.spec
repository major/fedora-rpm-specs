Name:           latexmk
Version:        4.86a
Release:        %autorelease
Summary:        A make-like utility for LaTeX files

%global upstreamver %(sed 's/\\.//' <<< %{version})

License:        GPL-2.0-or-later
URL:            https://www.cantab.net/users/johncollins/latexmk/
Source0:        %{url}%{name}-%{upstreamver}.zip
Source1:        latexmkrc
Source2:        latexmk-README.fedora

BuildArch:      noarch
BuildRequires:  perl-generators

Requires:       tex-latex-bin, ghostscript, xdg-utils

%description
Latexmk is a perl script for running LaTeX the correct number of times to
resolve cross references, etc.; it also runs auxiliary programs (bibtex,
makeindex if necessary, and dvips and/or a previewer as requested).  It has
a number of other useful capabilities, for example to start a previewer and
then run latex whenever the source files are updated, so that the previewer
gives an up-to-date view of the document.  The script runs on both UNIX and
MS-WINDOWS (95, ME, XP, etc).  This script is a corrected and improved
version of the original version of latexmk.

Before using a previewer, read the file README.fedora.

%prep
%autosetup -n %{name}

%conf
# Invoke perl directly
sed -i.orig "s|^#\!/usr/bin/env perl|#\!/usr/bin/perl -w|" latexmk.pl
touch -r latexmk.pl.orig latexmk.pl
rm latexmk.pl.orig

%build
cp -p %{SOURCE2} README.fedora

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}
install -m 0755 -p latexmk.pl %{buildroot}%{_bindir}/latexmk
install -m 0644 -p latexmk.1 %{buildroot}%{_mandir}/man1
install -m 0644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}

# Remove files we don't want in the docs
rm -f extra-scripts/*.bat

%files
%{_bindir}/latexmk
%{_mandir}/man1/latexmk.1*
%config(noreplace) %{_sysconfdir}/latexmkrc
%doc CHANGES README README.fedora extra-scripts example_rcfiles
%doc latexmk.pdf
%license COPYING

%changelog
%autochangelog
