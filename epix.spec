## This package has not architecture dependent files,
## except for the -static library that uses.
%global debug_package %{nil}

Name:    epix
Summary: Utilities for mathematically accurate figures
Version: 1.2.19
Release: 7%{?dist}
License: GPLv2+
URL:     https://mathcs.holycross.edu/~ahwang/current/ePiX.html
Source0: https://mathcs.holycross.edu/~ahwang/epix/epix-%{version}_withpdf.tar.bz2

BuildRequires: gcc-c++, libtool, automake
BuildRequires: ghostscript
BuildRequires: texinfo
BuildRequires: texlive
BuildRequires: texlive-comment
BuildRequires: texlive-eepic
BuildRequires: texlive-kpathsea-bin
BuildRequires: texlive-latex-bin-bin
BuildRequires: texlive-pst-tools
BuildRequires: fedora-obsolete-packages

## ePiX needs a static library to work; it's packaged in the -static subpackage
Requires: %{name}-static = %{version}-%{release}

Requires: %{name}-bash-completion = %{version}-%{release}

Requires: ghostscript
Requires: ImageMagick
Requires: texlive-comment
Requires: texlive-epstopdf-bin
Requires: texlive-eepic
Requires: texlive-pst-tools
Requires: fedora-obsolete-packages

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
BuildRequires: make
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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.2.19-3
- texlive-tetex is now packaged inside the rpm fedora-obsolete-packages

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 22 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.2.19-1
- Release 1.2.19

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.2.18-7
- Remove obsolete requirements for %%post/%%preun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.2.18-5
- Fix the Configure WARNING: 'missing' script is too old or missing

* Sat Aug 11 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.2.18-4
- Renovate SPEC file

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.2.18-1
- Update to 1.2.18

* Sun Sep 17 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.2.17-4
- Fix dependencies

* Thu Aug 24 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.2.17-3
- Rebuild for ImageMagick

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.2.17-1
- Update to 1.2.17

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.2.16-1
- Update to 1.2.16

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.2.15-2
- Fix bz#1263007

* Fri Aug 21 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.2.15-1
- Update to 1.2.15

* Mon Jun 22 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.2.14-9
- Fixed texlive-epstopdf-bin request
- Removed useless files

* Sun Jun 21 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.2.14-8
- Used %%license tag
- Made -data and -doc sub-packages
- Spec cleaning
- Fixed the emacs- sub-package

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Antonio Trande <sagitter@fedoraproject.org> 1.2.14-4
- Added a conditional macro for docdir in fedora<20
- Rearrangement of documentation files

* Sat May 17 2014 Antonio Trande <sagitter@fedoraproject.org> 1.2.14-3
- doc sub-package not built anymore

* Fri May 16 2014 Antonio Trande <sagitter@fedoraproject.org> 1.2.14-2
- Fixed documentation directories definition

* Wed May 14 2014 Antonio Trande <sagitter@fedoraproject.org> 1.2.14-1
- Update to 1.2.14

* Wed Dec 18 2013 Antonio Trande <sagitter@fedoraproject.org> 1.2.13-3
- Fix Requires for emacs and bash-completion subpackages

* Wed Dec 18 2013 Antonio Trande <sagitter@fedoraproject.org> 1.2.13-2
- BR lines rearranged
- Unzip all manuals and 'sample_src' archive
- Added bash-completion subpackage
- Added -emacs subpackage
- Added bash Requires

* Sun Dec 15 2013 Antonio Trande <sagitter@fedoraproject.org> 1.2.13-1
- First package
