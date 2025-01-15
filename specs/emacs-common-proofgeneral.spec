%global pkg     proofgeneral
%global giturl  https://github.com/ProofGeneral/PG

# Get post-4.5 release bug fixes and support for prooftree 0.14
%global commit  1ffca70b2fcfd1c524f9b9e5ceebae07d3b745b6
%global date    20240912
%global forgeurl %{giturl}

Name:           emacs-common-%{pkg}
Version:        4.5
Summary:        Emacs mode for standard interaction interface for proof assistants

%forgemeta

# The code is GPL-3.0-or-later.
# The icons are CC-BY-SA-3.0, except for the search icon.
# The search icon is CC-BY-SA-2.0.
License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC-BY-SA-2.0
Release:        9%{?dist}
URL:            https://proofgeneral.github.io/
VCS:            git:%{giturl}.git
Source0:        %{forgesource}
Source1:        io.github.%{pkg}.metainfo.xml
# Backwards compatibility shell script launcher
Source2:        %{pkg}
# Additional icon sizes created with gimp from icons in the source file
Source3:        %{pkg}-96x96.png
Source4:        %{pkg}-256x256.png

# Patch 0 - Fedora specific, don't do an "install-info" in the make process
# (which would occur at build time), but instead put it into a scriptlet
Patch:          pg-4.2-Makefile.patch

# Bring the desktop file up to date with current standards.
Patch:          pg-4.2-desktop.patch

# Fix some places where looking-back is called without enough arguments
Patch:          pg-4.5-looking-back.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  emacs-nox
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  tex-cm-super
BuildRequires:  tex-ec
BuildRequires:  texinfo-tex

Requires:       hicolor-icon-theme

Recommends:     prooftree

%description
Proof General is a generic front-end for proof assistants (also known
as interactive theorem provers) based on Emacs.

Proof General allows one to edit and submit a proof script to a proof
assistant in an interactive manner:
- It tracks the goal state, and the script as it is submitted, and
  allows for easy backtracking and block execution.
- It adds toolbars and menus to Emacs for easy access to proof
  assistant features.
- It integrates with Emacs Unicode support for some provers to provide
  output using proper mathematical symbols.
- It includes utilities for generating Emacs tags for proof scripts,
  allowing for easy navigation.

Proof General supports a number of different proof assistants
(Isabelle, Coq, PhoX, and LEGO to name a few) and is designed to be
easily extendable to work with others.

%package -n emacs-%{pkg}
Summary:        Compiled elisp files to run Proof General under GNU Emacs
Requires:       emacs(bin) %{?_emacs_version:>= %{_emacs_version}}
Requires:       emacs-common-%{pkg} = %{version}-%{release}

%description -n emacs-%{pkg}
Proof General is a generic front-end for proof assistants based on Emacs.

This package contains the byte compiled elisp packages to run Proof
General with GNU Emacs.

%prep
%forgeautosetup -p0

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Fix rpmlint complaints:
# Remove .cvsignore files
find . -name .cvsignore -delete

# Fix non UTF-8 documentation and theory files
for f in phox/sqrt2.phx; do
  mv $f $f.orig
  iconv -f iso-8859-1 -t utf8 $f.orig > $f
  fixtimestamp $f
done

%build
# Make full copies of emacs versions, set options in the proofgeneral start
# script
make clean
make EMACS=emacs compile bashscripts perlscripts doc

%install
%define full_doc_dir %{_datadir}/doc/%{pkg}
%define full_man_dir %{_mandir}/man1

%define doc_options DOCDIR=%{buildroot}%{full_doc_dir} MANDIR=%{buildroot}%{full_man_dir} INFODIR=%{buildroot}%{_infodir}
%define common_options PREFIX=%{buildroot}%{_prefix} DEST_PREFIX=%{_prefix} DESKTOP=%{buildroot}%{_datadir} BINDIR=%{buildroot}%{_bindir} %{doc_options}

%define emacs_options ELISP_START=%{buildroot}%{_emacs_sitestartdir} ELISP=%{buildroot}%{_emacs_sitelispdir}/%{pkg} DEST_ELISP=%{_emacs_sitelispdir}/%{pkg}

make EMACS=emacs %{common_options} %{emacs_options} install install-doc

# Do not install the INSTALL or COPYING files
rm %{buildroot}%{full_doc_dir}/{COPYING,INSTALL}

# Validate the desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/proofgeneral.desktop

# Install the AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/io.github.%{pkg}.metainfo.xml

# Install the backwards compatibility launcher
cp -p %{SOURCE2} %{buildroot}%{_bindir}

# Install additional icon sizes
install -Dpm 644 %{SOURCE3} \
  %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/%{pkg}.png
install -Dpm 644 %{SOURCE4} \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{pkg}.png

%files
%license COPYING
%{full_doc_dir}
%{full_man_dir}/*
%{_infodir}/*
%{_bindir}/*
%{_datadir}/application-registry/%{pkg}.applications
%{_datadir}/applications/%{pkg}.desktop
%{_datadir}/icons/hicolor/*/apps/%{pkg}.png
%{_datadir}/mime-info/%{pkg}.*
%{_metainfodir}/io.github.%{pkg}.metainfo.xml

%files -n emacs-%{pkg}
%{_emacs_sitestartdir}/*.el
%{_emacs_sitelispdir}/%{pkg}/

%changelog
* Sat Sep 28 2024 Jerry James <loganjerry@gmail.com> - 4.5-9
- Update to git head for prooftree 0.14 support

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 4.5-5
- Stop building for 32-bit x86

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Jerry James <loganjerry@gmail.com> - 4.5-4
- Validate appdata with appstream-util

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 19 2022 Jerry James <loganjerry@gmail.com> - 4.5-3
- Add patch to silence warnings about an overly long docstring
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 4.5-1
- Version 4.5
- License change from GPLv2 to GPLv3+

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 19 2021 Jerry James <loganjerry@gmail.com> - 4.4-15.20211013gitfd04605
- 13 Oct 2021 git snapshot for numerous updates and bug fixes
- Install metainfo instead of appdata and reenable validation

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Jerry James <loganjerry@gmail.com> - 4.4-11.20200506gitea62543
- May 6 2020 git snapshot so emacs-mmm dependency can be dropped (bz 1837683)
- Remove the -el subpackage as required by current package guidelines

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar  3 2018 Jerry James <loganjerry@gmail.com> - 4.4-6
- Install additional icon sizes

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.4-4
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 25 2016 Jerry James <loganjerry@gmail.com> - 4.4-1
- New upstream release
- New project URLs
- Update the AppData file and validate it on installation
- Use the license macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Jerry James <loganjerry@gmail.com> - 4.2-2
- Add AppData file

* Sat Aug 24 2013 Jerry James <loganjerry@gmail.com> - 4.2-1
- New upstream release (fixes bz 972343)
- Fix eps2pdf BR (bz 913972 and 992196)
- Add BRs for newer versions of texlive
- Drop upstreamed -elisp patch
- Add upstream workaround for Emacs 24.3 byte-compilation error

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Jerry James <loganjerry@gmail.com> - 4.1-1
- New upstream release
- Upstream no longer supports XEmacs
- Upstream no longer bundles X-Symbol
- Remove unnecessary spec file elements (defattr, etc.)
- Move desktop files into places where they will be used

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 29 2009 Alan Dunn <amdunn@gmail.com> 3.7.1-4
- Incorporated comments from Jerry James about applying his patch:
  patch now applied unconditionally (regardless of Fedora version
  which was used as a somewhat imperfect way to control XEmacs
  version).
- Patch descriptions moved upward in spec file in accordance with
  examples in guidelines.

* Thu Jul 09 2009 Alan Dunn <amdunn@gmail.com> 3.7.1-3
- Added xemacs patch that fixes compilation problems for X-Symbol code.

* Thu Jul 02 2009 Alan Dunn <amdunn@gmail.com> 3.7.1-2
- Excluded bundled X-symbol, mmm-mode.
- Changed requires for these bundled packages.

* Tue Apr 07 2009 Alan Dunn <amdunn@gmail.com> 3.7.1-1
- Initial Fedora RPM.
