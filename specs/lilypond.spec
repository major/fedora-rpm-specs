# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 0

Name:		lilypond
Version:	2.25.20
Release:	2%{?dist}
Summary:	A typesetting system for music notation

License:	GPL-3.0-only
URL:		https://lilypond.org
Source0:	https://lilypond.org/download/sources/v2.25/lilypond-%{version}.tar.gz
Source1:        century-schoolbook-l.metainfo.xml
Patch0:		lilypond-2.21.2-gcc44-relocate.patch

Requires:	ghostscript >= 8.15
Obsoletes: 	lilypond-fonts <= 2.12.1-1
Requires:	lilypond-emmentaler-fonts = %{version}-%{release}

Requires:	texlive-tex-gyre

BuildRequires:  gcc-c++
BuildRequires:  t1utils bison flex ImageMagick gettext
BuildRequires:  python3-devel
BuildRequires:  mftrace >= 1.1.19
BuildRequires:  guile30-devel
BuildRequires:  ghostscript >= 8.15
BuildRequires:  pango-devel >= 1.12.0
BuildRequires:  fontpackages-devel
BuildRequires:	perl-Pod-Parser perl(Math::Trig)
BuildRequires:	rsync
BuildRequires:  texlive-metapost
BuildRequires:  make
BuildRequires:  cairo-devel

%description
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

%package emmentaler-fonts
Summary:        Lilypond emmentaler fonts
Requires:       fontpackages-filesystem
Requires:	lilypond-fonts-common = %{version}-%{release}
BuildArch:	noarch

%description emmentaler-fonts
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

These are the emmentaler fonts included in the package.

%package fonts-common
Summary:        Lilypond fonts common dir
Requires:       fontpackages-filesystem
Obsoletes:      lilypond-texgyre-cursor-fonts <= 2.23.11-1
Obsoletes:      lilypond-texgyre-heros-fonts <= 2.23.11-1
Obsoletes:      lilypond-texgyre-schola-fonts <= 2.23.11-1
Obsoletes:      lilypond-c059-fonts <= 2.23.11-1
Obsoletes:      lilypond-nimbus-fonts <= 2.23.11-1
BuildArch:	noarch

%description fonts-common
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

This contains the directory common to all lilypond fonts.

%prep
%setup -q

%patch -P 0 -p0

%build
PYTHON=/usr/bin/python3
export PYTHON
%configure --disable-checking \
	--enable-documentation=no \
        --enable-cairo-backend \
	--with-texgyre-dir=/usr/share/texlive/texmf-dist/fonts/opentype/public/tex-gyre/
make %{?_smp_mflags} bytecode


%install
make install-bytecode DESTDIR=$RPM_BUILD_ROOT package_infodir=%{_infodir} \
	vimdir=%{_datadir}/vim/vimfiles

# Symlink lilypond-init.el in emacs' site-start.d directory
pushd $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
mkdir site-start.d
ln -s ../lilypond-init.el site-start.d
popd


%find_lang %{name}

mkdir -p $RPM_BUILD_ROOT%{_fontdir}
mv $RPM_BUILD_ROOT%{_datadir}/lilypond/%{version}/fonts/otf/*.otf $RPM_BUILD_ROOT%{_fontdir}
rmdir $RPM_BUILD_ROOT%{_datadir}/lilypond/%{version}/fonts/otf
ln -s %{_fontdir} $RPM_BUILD_ROOT%{_datadir}/lilypond/%{version}/fonts/otf


%files -f %{name}.lang
%license COPYING
%doc AUTHORS.txt DEDICATION INSTALL.txt
%doc NEWS.txt README.md ROADMAP VERSION
%{_bindir}/*
%{_datadir}/lilypond
%{_datadir}/emacs/site-lisp
%{_datadir}/vim/vim*
%{_libdir}/%{name}/%{version}/ccache/lily/

%_font_pkg -n emmentaler emmentaler*otf

%files fonts-common
%doc COPYING

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 07 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.25.20-4
- 2.25.20
- Fix vim files path.

* Fri Aug 02 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.25.16-3
- Rebuild to fix missing automatic Requires (fix RHBZ#2302532)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 14 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.25.16-1
- 2.25.16

* Sat Feb 03 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.25.12-1
- 2.25.12

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.25.11-1
- 2.25.11

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.25.4-2
- Patch for crash, BZ 2208024

* Mon Apr 24 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.25.4-1
- 2.25.4

* Mon Apr 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.25.3-1
- 2.25.3

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.25.2-2
- migrated to SPDX license

* Tue Feb 21 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.25.2-1
- 2.25.2

* Mon Jan 23 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.25.1-1
- 2.25.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.25.0-1
- 2.25.0

* Mon Nov 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.82-1
- 2.23.82

* Mon Nov 14 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.81-1
- 2.23.81

* Mon Oct 24 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.80-1
- 2.23.80

* Mon Oct 10 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.14-1
- 2.23.14

* Mon Sep 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.13-1
- 2.23.13

* Tue Sep 13 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.12-3
- Enable Cairo backend

* Tue Sep 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.12-2
- Update vim version.

* Thu Aug 25 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.12-1
- 2.23.12

* Mon Jul 25 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.11-1
- 2.23.11

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.23.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.10-2
- Build with guile bytecode for improved performance.

* Mon Jun 27 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.10-1
- 2.23.10

* Mon May 23 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.9-1
- 2.23.9

* Mon Apr 25 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.8-1
- 2.23.8

* Tue Apr 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.7-1
- 2.23.7

* Mon Feb 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.23.6-1
- 2.23.6

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.23.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.23.5-1
- 2.23.5

* Mon Nov 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.23.4-1
- 2.23.4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.23.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.23.3-1
- 2.23.3

* Mon Apr 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.23.2-1
- 2.23.2

* Tue Mar 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.23.1-1
- 2.23.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.23.0-2
- Upstream patch for ascii issue, move to Guile 2.2.

* Mon Jan 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.23.0-1
- 2.23.0

* Wed Jan 20 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.22.0-2
- Revert to guile 1.8 per upstream.

* Tue Jan 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.22.0-1
- 2.22.0

* Tue Dec 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.21.82-1
- 2.21.82

* Mon Dec 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.21.81-1
- 2.21.81

* Wed Nov 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.21.80-1
- 2.21.80

* Tue Sep 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.21.6-1
- 2.21.6

* Mon Aug 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.21.5-1
- 2.21.5

* Wed Aug 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.21.4-2
- Patch for CVE-2020-17353.

* Fri Jul 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.21.4-1
- 2.21.4

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.21.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.21.3-1
- 2.21.3

* Wed Jul 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.21.2-1
- 2.21.2

* Sat Jun 20 2020 Tomas Korbar <tkorbar@redhat.com> - 2.21.1-2
- Changed required guile version to 2.2

* Wed May 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.21.1-1
- 2.21.1

* Mon Mar 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.20.0-1
- 2.20.0

* Mon Feb 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.19.84-2
- Fix vim version.

* Fri Feb 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.19.84-1
- 2.19.84

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.83-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.83-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 2.19.83-2
- Remove hardcoded gzip suffix from GNU info pages

* Wed Apr 10 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.19.83-1
- 2.19.83.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.82-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.19.82-3
- Update vim file location, BR fix.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.19.82-1
- 2.19.82

* Fri May 18 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.19.81-6
- Replace the previous patch with the one the upstream formally pushed

* Wed May 09 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.19.81-5
- Fix std::vector out-of-range detected by gcc8 -Wp,-D_GLIBCXX_ASSERTIONS
  (bug 1568274)

* Thu Mar 15 2018 Tom Callaway <spot@fedoraproject.org> - 2.19.81-4
- fix texlive related deps

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.19.81-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Jan 29 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.19.81-1
- 2.19.81
- Minor spec cleanup.
- Add C059 and Nimbus fonts.

* Mon Oct 16 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.80-1
- 2.19.80

* Mon Aug 07 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.65-1
- 2.19.65

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.64-1
- 2.19.64

* Wed Jun 28 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.63-1
- 2.19.63

* Wed Jun 14 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.62-1
- 2.19.62

* Mon May 22 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.61-1
- 2.19.61

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue May 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.60-1
- 2.19.60

* Mon Apr 10 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.59-1
- 2.19.59

* Wed Mar 29 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.58-1
- 2.19.58

* Tue Mar 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.57-1
- 2.19.57

* Mon Feb 27 2017 Jon Ciesla <limburgher@gmail.com> - 2.19.56-1
- 2.19.56

* Mon Feb 13 2017 Jon Ciesla <limburgher@gmail.com> - 2.19.55-1
- 2.19.55

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 06 2017 Jon Ciesla <limburgher@gmail.com> - 2.19.54-2
- Fix vim file location, BZ 1410875.

* Wed Jan 04 2017 Jon Ciesla <limburgher@gmail.com> - 2.19.54-1
- 2.19.54

* Mon Dec 19 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.53-1
- 2.19.53

* Mon Dec 05 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.52-1
- 2.19.52

* Mon Nov 21 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.51-1
- 2.19.51

* Mon Nov 07 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.50-1
- 2.19.50

* Tue Oct 18 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.49-1
- 2.19.49

* Wed Sep 14 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.48-1
- 2.19.48

* Wed Aug 31 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.47-1
- 2.19.47

* Wed Jul 27 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.46-1
- 2.19.46.
- Added %%{?_smp_mflags}

* Fri Jul 22 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.45-2
- Patch for crash, BZ 1359215.

* Sun Jul 10 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.45-1
- 2.19.45.

* Wed Jun 22 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.44-1
- 2.19.44.

* Fri Jun 10 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.43-1
- 2.19.43.

* Thu May 19 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.42-1
- 2.19.42.

* Mon May 02 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.41-1
- 2.19.41.

* Mon Apr 18 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.40-1
- 2.19.40.

* Fri Apr 01 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.39-2
- Patch to fix emmentaler brace area, fixing BZ 1235779.

* Fri Apr 01 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.39-1
- 2.19.39.

* Mon Mar 14 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.38-1
- 2.19.38.

* Thu Mar 03 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.37-3
- Revised patch from upstream, https://codereview.appspot.com/287350043

* Mon Feb 29 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.37-2
- Fix FTBFS, BZ 1307746.

* Mon Feb 29 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.37-1
- 2.19.37.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.36-1
- 2.19.36.

* Mon Jan 04 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.35-1
- 2.19.35.

* Wed Dec 23 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.34-1
- 2.19.34.

* Mon Dec 07 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.33-1
- 2.19.33.

* Tue Nov 24 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.32-1
- 2.19.32.

* Wed Nov 11 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.31-1
- 2.19.31.

* Mon Oct 26 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.30-1
- 2.19.30.

* Tue Oct 20 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.29-1
- 2.19.29.

* Mon Sep 28 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.28-1
- 2.19.28.

* Mon Sep 14 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.27-1
- 2.19.27.

* Fri Sep 11 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.26-2
- Fix font obsoletes.

* Mon Aug 31 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.26-1
- 2.19.26.
- century-schoolbook-l and nimbus fonts removed.
- texgyre cursor, hera and schola fonts added.

* Mon Aug 10 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.25-1
- 2.19.25.

* Tue Jul 28 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.24-1
- 2.19.24.

* Tue Jul 21 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.23-1
- 2.19.23.

* Mon Jun 29 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.22-1
- 2.19.22.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.21-1
- 2.19.21.

* Fri May 15 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.20-1
- 2.19.20.

* Tue Apr 28 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.19-1
- 2.19.19.
- Add nimbus fonts.

* Mon Apr 06 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.18-1
- 2.19.18.

* Mon Mar 16 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.17-1
- 2.19.17.

* Sun Mar 01 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.16-1
- 2.19.16.

* Thu Jan 29 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.15-1
- 2.19.15, to fix BZ 1149230.

* Sun Oct 19 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.18.2-4
- Add metainfo file to show CenturySchL-Roma font in gnome-software

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Jon Ciesla <limburgher@gmail.com> - 2.18.2-1
- 2.18.2.

* Fri Jan 03 2014 Jon Ciesla <limburgher@gmail.com> - 2.18.0-1
- 2.18.0, BZ 1047196.

* Mon Dec 09 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.97-1
- 2.17.97.

* Mon Nov 25 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.96-1
- 2.17.96.

* Mon Nov 04 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.30-1
- 2.17.30.

* Wed Oct 23 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.29-1
- 2.17.29.

* Mon Sep 09 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.26-1
- 2.17.26.
- Fix vim dir, BZ 1005394.

* Mon Aug 26 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.25-1
- 2.17.25.

* Tue Aug 13 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.24-1
- Fix FTBFS, 992140.  Updated to latest as 2.16.x will not build
- with texlive > 2012.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Jon Ciesla <limburgher@gmail.com> - 2.16.2-1
- New stable upstream.

* Sat Nov 10 2012 Jon Ciesla <limburgher@gmail.com> - 2.16.1-1
- New stable upstream.

* Fri Aug 24 2012 Jon Ciesla <limburgher@gmail.com> - 2.16.0-1
- New stable upstream.

* Sun Aug 12 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.95-1
- New upstream.

* Sat Aug 04 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.42-1
- New upstream.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 06 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.41-1
- New upstream.

* Wed Jun 06 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.40-2
- Make fonts noarch, BZ 826841.

* Wed Jun 06 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.40-1
- New upstream.

* Wed May 23 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.39-1
- RC.

* Fri May 11 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.38-2
- Patch for gcc bug, BZ 820998.

* Fri May 04 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.38-1
- New stable release.

* Fri Apr 20 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.37-1
- New upstream.
- Decruft spec.

* Mon Apr 09 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.36-1
- New upstream.

* Wed Mar 28 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.35-1
- New upstream.

* Tue Mar 20 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.34-1
- New upstream.

* Fri Mar 09 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.33-1
- New upstream.

* Tue Mar 06 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.32-1
- New upstream.

* Wed Feb 29 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.31-1
- New upstream.

* Sat Feb 18 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.30-1
- New upstream.

* Fri Feb 10 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.29-1
- New upstream.

* Sat Feb 04 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.28-1
- New upstream.

* Wed Jan 25 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.27-1
- New upstream.

* Tue Jan 17 2012 Dan Horák <dan[at]danny.cz> - 2.15.26-2
- excluding s390 is no longer needed

* Mon Jan 16 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.26-1
- New upstream.

* Sun Jan 08 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.24-1
- New upstream.

* Wed Dec 28 2011 Jon Ciesla <limburgher@gmail.com> - 2.15.23-1
- New upstream.

* Fri Dec 16 2011 Jon Ciesla <limburgher@gmail.com> - 2.15.22-1
- New upstream.

* Thu Dec 08 2011 Jon Ciesla <limburgher@gmail.com> - 2.15.21-1
- New upstream.

* Mon Nov 28 2011 Jon Ciesla <limb@jcomserv.net> - 2.15.20-1
- New upstream.

* Tue Nov 22 2011 Jon Ciesla <limb@jcomserv.net> - 2.15.19-1
- New upstream.

* Sat Nov 12 2011 Jon Ciesla <limb@jcomserv.net> - 2.15.18-1
- New upstream.

* Fri Oct 28 2011 Jon Ciesla <limb@jcomserv.net> - 2.15.16-1
- New upstream.

* Fri Oct 21 2011 Jon Ciesla <limb@jcomserv.net> - 2.15.14-1
- New upstream.

* Thu Jul 28 2011 Jon Ciesla <limb@jcomserv.net> - 2.14.2-1
- New upstream.

* Mon Jun 13 2011 Jon Ciesla <limb@jcomserv.net> - 2.14.1-1
- New upstream.

* Mon Jun 06 2011 Jon Ciesla <limb@jcomserv.net> - 2.14.0-1
- New upstream.

* Tue May 31 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.63-1
- New upstream.

* Fri May 27 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.62-1
- New upstream.

* Mon May 02 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.61-1
- New upstream.

* Mon Apr 18 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.60-1
- New upstream.

* Mon Apr 11 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.59-1
- New upstream.

* Thu Apr 07 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.58-1
- New upstream.

* Mon Apr 04 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.57-1
- New upstream.

* Thu Mar 31 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.56-1
- New upstream.

* Fri Mar 25 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.55-1
- New upstream.

* Mon Mar 14 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.54-1
- New upstream.

* Fri Mar 11 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.53-2
- Fixed license tag, BZ 684215.

* Tue Mar 08 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.53-1
- New upstream.

* Wed Mar 02 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.52-1
- New upstream.

* Fri Feb 25 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.51-1
- New upstream.

* Mon Feb 14 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.50-1
- New upstream.

* Thu Feb 10 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.49-1
- New upstream.

* Tue Feb 08 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.48-1
- New upstream.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.47-1
- New upstream.

* Wed Jan 12 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.46-1
- New upstream.

* Wed Jan 12 2011 Dan Horák <dan[at]danny.cz> - 2.13.45-2
- exclude s390 because fontforge fails with an internal error

* Fri Jan 07 2011 Jon Ciesla <limb@jcomserv.net> - 2.13.45-1
- New upstream.

* Wed Dec 29 2010 Jon Ciesla <limb@jcomserv.net> - 2.13.39-3
- Scriptlet fix.

* Mon Dec 20 2010 Jon Ciesla <limb@jcomserv.net> - 2.13.39-2
- Update for new vim, BZ 663889.

* Mon Nov 15 2010 Jon Ciesla <limb@jcomserv.net> - 2.13.39-1
- Update to first Beta for 2.14.x to fix FTBFS BZ 631363.

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 2.12.3-3
- recompiling .py files against Python 2.7 (rhbz#623331)

* Thu Jul 15 2010 Jon Ciesla <limb@jcomserv.net> - 2.12.3-2
- Update for new licensing guidelines.

* Mon Jan 04 2010 Jon Ciesla <limb@jcomserv.net> - 2.12.3-1
- Update to 2.12.3.
- Dropped consts patch, upstreamed.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Jon Ciesla <limb@jcomserv.net> - 2.12.2-4
- Update for vim 7.2, BZ 503429.

* Wed Mar 04 2009 Caolán McNamara <caolanm@redhat.com> - 2.12.2-3
- fix up strchr const rets for const arg

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Jon Ciesla <limb@jcomserv.net> - 2.12.2-1
- Update to 2.12.2.
- Patch for gcc 4.4.

* Thu Feb 19 2009 Jon Ciesla <limb@jcomserv.net> - 2.12.1-6
- Split out feta and parmesan type1 fonts.

* Fri Jan 23 2009 Jon Ciesla <limb@jcomserv.net> - 2.12.1-5
- Final font corrections.

* Thu Jan 22 2009 Jon Ciesla <limb@jcomserv.net> - 2.12.1-4
- More font refinements.

* Wed Jan 21 2009 Jon Ciesla <limb@jcomserv.net> - 2.12.1-3
- Drop feta-fonts package cruft.

* Wed Jan 14 2009 Jon Ciesla <limb@jcomserv.net> - 2.12.1-2
- Implementing font_pkg.

* Tue Jan 06 2009 Jon Ciesla <limb@jcomserv.net> - 2.12.1-1
- Update to 2.12.1.
- Droppedn parse-scm patch, applied upstream.

* Tue Dec 30 2008 Jon Ciesla <limb@jcomserv.net> - 2.12.0-3
- Split out fonts subpackage, BZ 477416.

* Tue Dec 30 2008 Jon Ciesla <limb@jcomserv.net> - 2.12.0-2
- Re-fix Source0 URL.

* Wed Dec 17 2008 Jon Ciesla <limb@jcomserv.net> - 2.12.0-1
- New upstream, BZ 476836.
- Fixed Source0 URL.
- Patched to allow Python 2.6.
- Patch for parse-scm fix.

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.11.57-2
- Rebuild for Python 2.6

* Mon Sep 08 2008 Jon Ciesla <limb@jcomserv.net> - 2.11.57-1
- Upgrade to new upstream.

* Wed Aug 27 2008 Jon Ciesla <limb@jcomserv.net> - 2.10.33-4
- Spec cleanup, fix for BZ 456842, vim file locations.

* Mon Apr  7 2008 Christopher Aillon <caillon@redhat.com> - 2.10.33-3
- Fix the build against GCC 4.3; simply missing some #includes

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.10.33-2
- Autorebuild for GCC 4.3

* Thu Sep 20 2007 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.33-1
- New release.
- Fix source URL.
- Change licence from GPL to GPLv2.

* Tue Aug 21 2007 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.29-1
- New release. Remove old patch.

* Wed Aug  1 2007 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.25-2
- Patch to fix problems with recent versions of fontforge.

* Fri Jul 27 2007 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.25-1
- New release & new source URL.

* Tue Mar 20 2007 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.20-1
- New release.

* Thu Feb 15 2007 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.17-1
- New release. Fix bug 225410.

* Thu Jan 25 2007 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.13-1
- New release.

* Wed Jan 17 2007 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.11-1
- New release.

* Fri Jan  5 2007 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.8-1
- New release.
- Fix source URL.

* Sat Dec 23 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.4-1
- New release.
- Finish fixing bug 219400.

* Wed Dec 13 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.2-2
- New release.
- Fix bug 219400.

* Mon Dec  4 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.1-1
- New release.

* Mon Nov 13 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.0-1
- New release. Update build requirements for 2.10 series.

* Fri Nov  3 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.8-1
- New release.

* Mon Oct  9 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.7-1
- New release.

* Wed Sep  6 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.6-2
- Rebuild for FC6
- Update directory for vim.
- Don't ghost .pyo files, as per changes in packaging guidelines (bug 205387).

* Thu Aug 10 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.6-1
- New release.

* Tue Jun  6 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.4-1
- New release.

* Sat May 20 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.3-1
- New upstream, remove patch.
- Put docs in separate SRPM.

* Mon May 15 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.2-3
- Fixes to dependencies, encoding of info files.
- Add docs as separate tarball (building them fails without ghostscript 8.50).

* Mon May 15 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.2-2
- Patch to fix segfault in fontconfig.

* Sat May 13 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.2-1
- New release.

* Tue May  2 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.1-4
- Add missing BuildRequires.
- Specify location of NCSB fonts to configure script.
- Disable parallel build.

* Tue Apr 25 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.1-3
- Make .so file executable.

* Tue Apr 25 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.1-2
- Use gettext.

* Mon Apr 10 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.1-1
- Initial build.
