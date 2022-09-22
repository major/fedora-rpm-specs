%global texmf %{_datadir}/texmf

Summary: Culmus Hebrew fonts support for LaTeX
Name: tex-fonts-hebrew
Version: 0.1
Release: 37%{?dist}
URL: http://culmus.sf.net
# There is no real upstream for this package. It was based on Yotam Medini's
# http://www.medini.org/hebrew/culmus2ltx-2003-02-28.tar.gz but is now
# maintained specifically for Fedora.
Source: tetex-fonts-hebrew-%{version}.tar.gz

# hebrew.ldf is LPPL, everything else is GPL+
License: GPL+ and LPPL

#for afm2tfm we need
BuildRequires: make
BuildRequires: texlive-dvips-bin
#for vptovf we need
BuildRequires: texlive-fontware-bin

BuildRequires: culmus-aharoni-clm-fonts
BuildRequires: culmus-caladings-clm-fonts
BuildRequires: culmus-david-clm-fonts
BuildRequires: culmus-drugulin-clm-fonts
BuildRequires: culmus-ellinia-clm-fonts
BuildRequires: culmus-frank-ruehl-clm-fonts
BuildRequires: culmus-hadasim-clm-fonts
BuildRequires: culmus-miriam-clm-fonts
BuildRequires: culmus-miriam-mono-clm-fonts
BuildRequires: culmus-nachlieli-clm-fonts
BuildRequires: culmus-simple-clm-fonts
BuildRequires: culmus-stamashkenaz-clm-fonts
BuildRequires: culmus-stamsefarad-clm-fonts
BuildRequires: culmus-yehuda-clm-fonts

#for directory ownership
Requires: texlive-base
#for updating path /usr/share/texlive/texmf-config/web2c/updmap.cfg
Requires: texlive-kpathsea-bin
#for /usr/share/texmf/fonts/map/dvips/updmap/culmus.map we need following
Requires: culmus-aharoni-clm-fonts
Requires: culmus-caladings-clm-fonts
Requires: culmus-david-clm-fonts
Requires: culmus-drugulin-clm-fonts
Requires: culmus-ellinia-clm-fonts
Requires: culmus-frank-ruehl-clm-fonts
Requires: culmus-hadasim-clm-fonts
Requires: culmus-miriam-clm-fonts
Requires: culmus-miriam-mono-clm-fonts
Requires: culmus-nachlieli-clm-fonts
Requires: culmus-simple-clm-fonts
Requires: culmus-stamashkenaz-clm-fonts
Requires: culmus-stamsefarad-clm-fonts
Requires: culmus-yehuda-clm-fonts

BuildArch: noarch
Requires(post): /usr/bin/texhash /usr/bin/updmap-sys /usr/bin/texconfig-sys /usr/bin/texconfig
Requires(postun): /usr/bin/texhash /usr/bin/updmap-sys /usr/bin/texconfig-sys /usr/bin/texconfig

%description
Support using the Culmus Hebrew fonts in LaTeX.

%prep
%setup -q -n tetex-fonts-hebrew-%{version}

%build
sed -i 's/^culmusdir=/#culmusdir=/' mkCLMtfm.sh
culmusdir=%{_datadir}/fonts/culmus make

%install
make TEXMFDIR=%{buildroot}%{texmf} CULMUSDIR=../../../../fonts/culmus install
TEXMFDIR=%{buildroot}%{texmf}
mkdir -p $TEXMFDIR/fonts/map/dvips/updmap/
mv $TEXMFDIR/fonts/map/dvips/culmus.map $TEXMFDIR/fonts/map/dvips/updmap/

%files
%doc hebhello.tex culmus-ex.tex GNU-GPL
%{texmf}/fonts
%{texmf}/tex

%post
/usr/bin/texhash >/dev/null 2>&1 || :
if [ "$1" = "1" ]; then
  /usr/bin/updmap-sys --quiet --nohash --enable Map=culmus.map >/dev/null 2>&1 || :
fi

%postun
if [ "$1" = "0" ]; then
  /usr/bin/updmap-sys --quiet --nohash --disable Map=culmus.map >/dev/null 2>&1 || :
fi
/usr/bin/texhash >/dev/null 2>&1 || :

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Than Ngo <than@redhat.com> - 0.1-29
- Resolves: #1336452, #1593189, #1631920, #1596118, scriptlet failures

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.1-20
- Resolves:rh#921852 - Four culmus subpackages are not listed in build require
- Added BR: and R: for the following packages
- culmus-hadasim-clm-fonts, culmus-simple-clm-fonts
- culmus-stamashkenaz-clm-fonts, culmus-stamsefarad-clm-fonts

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.1-18
- Resolves:rh#903267-spec cleanup
- Change the dependecies for new textlive package in Fedora

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Dan Kenigsberg <danken@cs.technion.ac.il> - 0.1-13
- should obsolete tetex-fonts-hebrew-0.1-11. Bug #485639

* Wed Jul 22 2009 Dan Kenigsberg <danken@cs.technion.ac.il> - 0.1-12
- Rebuilt against existing David Type1 fonts. Bug #509697
- Require specific culmus font packages and obsolete tetex-fonts-hebrew-0.1-9. Bug #485639

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 15 2009 Caolán McNamara <caolanm@redhat.com> 0.1-10
- fonts-hebrew -> culmus-fonts-compat
* Sat Jun  4 2008 Dan Kenigsberg <danken@cs.technion.ac.il> 0.1-9
- Support texlive
* Sat Dec  1 2007 Dan Kenigsberg <danken@cs.technion.ac.il> 0.1-8
- Link to newly-named culmus-fonts. Bug #391161
* Sat Sep 16 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 0.1-7
- Rebuild for Fedora Extras 6
* Sun Jul  9 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 0.1-6
- bump version to mend upgrade path. Bug #197127
* Wed Jun 21 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 0.1-5
- Change summary line and directory ownership according to 195585#c8
* Tue Jun 20 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 0.1-4
- steal scriptlets from tetex-font-kerkis
* Mon Jun 19 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 0.1-3
- change spec (and a bit of mkCLMtfm) according to bug 195585#c5
* Thu Jun 15 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 0.1-1
- Initial build.
