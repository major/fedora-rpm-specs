%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%define texmflocal   %(kpsewhich -var-value TEXMFLOCAL)

Name:           tetex-elsevier
# upstream is unversioned, the version is constructed with the latest 
# file timestamp, in the format YYYYMMDD
Version:        0.1.20090917
Release:        29%{?dist}
Summary:        Elsevier LaTeX style files and documentation

License:        LPPL
URL:            http://www.elsevier.com/locate/latex
# Put this one as Source0 so it's easy to uncompress
Source1:        http://www.elsevier.com/framework_authors/misc/elsart.cls
Source2:        http://www.elsevier.com/framework_authors/misc/elsart1p.cls
Source3:        http://www.elsevier.com/framework_authors/misc/elsart3p.cls
Source4:        http://www.elsevier.com/framework_authors/misc/elsart5p.cls
Source7:        http://www.elsevier.com/framework_authors/misc/template-harv.tex
Source8:        http://www.elsevier.com/framework_authors/misc/template-num.tex
Source9:        http://www.elsevier.com/framework_authors/misc/elsart-harv.bst
Source10:       http://www.elsevier.com/framework_authors/misc/elsart-num.bst
Source11:       http://www.elsevier.com/framework_authors/misc/elsart-num-names.bst
Source12:       http://www.elsevier.com/framework_authors/misc/elsart-num-sort.bst
Source13:       http://www.elsevier.com/framework_authors/misc/CHANGES
Source14:       http://www.elsevier.com/framework_authors/misc/README
Source15:       http://www.elsevier.com/framework_authors/misc/instructions-num.tex
Source16:       http://www.elsevier.com/framework_authors/misc/instructions-harv.tex
Source18:       README.package

Buildarch:      noarch
BuildRequires:  tex(latex)
BuildRequires:  tex(lineno.sty)

Requires:       tex(latex)

Requires(post): tex(tex)
Requires(postun): tex(tex)

# This package has not been updated nor used by Elsevier since 2009.
# While it is still working, there seems to be no point in packaging it any more:
# no active use, possible packaging burden, outdated spec, not part of texlive
# It is a leaf package.
# All in all, retiring is the best option.
# As a preparation for that:
Provides: deprecated()

%description
LaTeX style files and documentation for the Elsevier publisher, legacy files.
See texlive-elsarticle for elsarticle.

%prep
%setup -q -c -T
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
 %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} \
 %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE18} .

# remove dos end of lines and keep timestamps
for file in CHANGES *.cls *.bst *.tex; do
  sed -e 's/\r//' $file > $file.tmp
  touch -r $file $file.tmp
  mv $file.tmp $file
done

%build
pdflatex instructions-num
pdflatex instructions-num
pdflatex instructions-harv
pdflatex instructions-harv


%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 $RPM_BUILD_ROOT%{texmflocal}/tex/latex/elsevier/
install -d -m755 $RPM_BUILD_ROOT%{texmflocal}/bibtex/bst/elsevier/
cp -p *.cls $RPM_BUILD_ROOT%{texmflocal}/tex/latex/elsevier/
cp -p *.bst $RPM_BUILD_ROOT%{texmflocal}/bibtex/bst/elsevier/

# Link .pdf files into texmflocal tree for texdoc
install -d -m755 $RPM_BUILD_ROOT%{texmflocal}/doc/latex/elsevier
for file in *.pdf; do
    ln -s %{_pkgdocdir}/$file $RPM_BUILD_ROOT%{texmflocal}/doc/latex/elsevier
done


%post
mktexlsr %{texmflocal} >/dev/null 2>&1 || :


%postun
mktexlsr %{texmflocal} >/dev/null 2>&1 || :


%files
%doc README README.package CHANGES *.pdf template-*.tex
%{texmflocal}/tex/latex/elsevier/
%{texmflocal}/bibtex/bst/elsevier/
%{texmflocal}/doc/latex/elsevier/


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20090917-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Michael J Gruber <mjg@fedoraproject.org> - 0.1.20090917-28
- deprecate

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20090917-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20090917-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20090917-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20090917-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Michael J Gruber <mjg@fedoraproject.org> - 0.1.20090917-23
- clarify status in README.package

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20090917-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Michael J Gruber <mjg@fedoraproject.org> - 0.1.20090917-21
- remove elsarticle which is in texlive-elsarticle{,-doc}

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20090917-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20090917-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20090917-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Michael J Gruber <mjg@fedoraproject.org> - 0.1.20090917-17
* call mktexlsr on texmflocal only (bug #1534725)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20090917-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20090917-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20090917-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20090917-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20090917-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 05 2013 Michael J Gruber <mjg@fedoraproject.org> - 0.1.20090917-11
- Use the actual texlive local tree, not the documented one (#971778).

* Sun Nov  3 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.1.20090917-10
- Honor setups with unversioned doc dirs (#993901).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20090917-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 01 2013 Michael J Gruber <mjg@fedoraproject.org> - 0.1.20090917-8
- adjust texmf tree to current texlive layout

* Fri Feb 22 2013 Michael J Gruber <mjg@fedoraproject.org> - 0.1.20090917-7
- adjust BR to new texlive (fix FTB for doc)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20090917-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20090917-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20090917-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20090917-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 25 2009 Mary Ellen Foster <mefoster at gmail.com> - 0.1.20090917-2
- Link documentation files into texmf for texdoc (fixes bug 541131)

* Fri Oct 30 2009 Mary Ellen Foster <mefoster at gmail.com> - 0.1.20090917-1
- Update to new upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20081007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Mary Ellen Foster <mefoster at gmail.com> - 0.1.20081024-2
- Better location for the elsarticle files

* Mon Jun 22 2009 Mary Ellen Foster <mefoster at gmail.com> - 0.1.20081024-1
- Add the elsarticle class as well

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20071024-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 28 2007 Patrice Dumas <pertusus@free.fr> 0.1.20071024-1
- update to the new version
- correct urls
- build the manuals

* Tue Aug 22 2006 Patrice Dumas <pertusus@free.fr> 0.1.20060516-3
- correct bst files place

* Fri Aug 11 2006 Patrice Dumas <pertusus@free.fr> 0.1.20060516-2
- really keep the timestamps

* Fri Aug 11 2006 Patrice Dumas <pertusus@free.fr> 0.1.20060516-1
- keep files timestamps, even for installed files
- remove unneeded tetex-latex BuildRequires
- correct the version by using the right month from the file timestamps

* Thu Aug 10 2006 Patrice Dumas <pertusus@free.fr> 0.1.20060416-3
- don't ship the ifac style, it is not redistributable

* Wed Aug  9 2006 Patrice Dumas <pertusus@free.fr> 0.1.20060416-2
- Ship a README.fedora file instead of packaging the web page

* Wed Aug  9 2006 Patrice Dumas <pertusus@free.fr> 0.1.20060416-1
- Initial Release
