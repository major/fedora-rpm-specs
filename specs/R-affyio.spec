%define packname  affyio
%define Rversion  3.4.0

Name:             R-%{packname}
Version:          1.66.0
Release:          10%{dist}
Summary:          Tools for parsing Affymetrix data files
Summary(fr):      Outils d'analyse de fichier de données de puces affymetrix
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:          LicenseRef-Callaway-LGPLv2+
URL:              http://bioconductor.org/packages/release/bioc/html/affyio.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Patch0:           affyio-fix-DESCRIPTION-Depends.patch
BuildRequires:    R-devel >= %{Rversion} tex(latex) zlib-devel R-methods

%description
Routines for parsing Affymetrix data files based upon file format 
information. Primary focus is on accessing the CEL and CDF file formats.

%description -l fr
Scripts pour analyser les fichiers de données issuent de puces affymetrix
basé sur les informations fournis pas les extensions. Un des premier 
objectifs est de convertir les données dans des fichiers au format
CEL ou CDF.

%prep
%setup -q -c -n %{packname}
sed -i '/Imports: zlibbioc/d' %{packname}/DESCRIPTION
sed -i '/import(zlibbioc)/d' %{packname}/NAMESPACE
%patch -P0 -p1 -b .fixdep

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_libdir}/R/library 
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css


%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 1.66.0-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.66.0-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.66.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug  2 2022 Tom Callaway <spot@fedoraproject.org> - 1.66.0-1
- update to 1.66.0
- R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.62.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.62.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.62.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 1.62.0-1
- update to 1.62.0

* Wed Feb  3 2021 Tom Callaway <spot@fedoraproject.org> - 1.60.0-1
- update to 1.60.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.58.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.58.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.58.0-1
- rebuild for R 4
- update to 1.58.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov  7 2019 Tom Callaway <spot@fedoraproject.org> - 1.56.0-1
- update to 1.56.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.50.0-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.50.0-1
- update to 1.50.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.46.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.46.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Tom Callaway <spot@fedoraproject.org> - 1.46.0-1
- update to 1.46.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 pingou <pingou@pingoured.fr> 1.32.0-1
- Update to version 1.32.0

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 pingou <pingou@pingoured.fr> 1.30.0-1
- Update to version 1.30.0

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 07 2013 pingou <pingou@pingoured.fr> 1.28.0-1
- Update to version 1.28.0

* Thu Apr 04 2013 pingou <pingou@pingoured.fr> 1.26.0-1
- Update to version 1.26.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> 1.22.0-1
- Update to 1.22.0

* Wed Jun 22 2011 pingou <pingou@pingoured.fr> 1.20.0-1
- Update to version 1.20.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 pingou <pingou@pingoured.fr> 1.18.0-1
- Update to version 1.18.0

* Tue May 11 2010 pingou <pingou@pingoured.fr> 1.16.0-1
- Update to version 1.16.0
- Fix url to a more stable form
- Remove R on post/postun since there is no post/postun

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 1.14.0-1
- Update to 1.14.0
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 29 2009 pingou <pingou@pingoured.fr> - 1.12.0-2
- version 1.20.0 != 1.12.0

* Wed Apr 29 2009 pingou <pingou@pingoured.fr> - 1.12.0-1
- Update to Bioconductor 2.4 and R 2.9.0
- Add requires to R-methods

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 pingou <pingou-at-pingoured.fr> 1.10.1-2
- Typo on the release number

* Thu Jan 22 2009 pingou <pingou-at-pingoured.fr> 1.10.1-1
- Update to newest version

* Sun Nov 30 2008 pingou <pingoufc4-at-yahoo.fr> 1.10.0-3
- Own the folder libs -- #473618

* Thu Nov 20 2008 pingou <pingoufc4-at-yahoo.fr> 1.10.0-2
- Correct the Source0

* Mon Oct 27 2008 pingou <pingoufc4-at-yahoo.fr> 1.10.0-1
- Update to version 1.10.0 for R >= 2.8.0

* Fri Sep 05 2008 pingou <pingoufc4-at-yahoo.fr> 1.8.1-1
- Update to version 1.8.1

* Fri May 02 2008 Pingou <pingoufc4@yahoo.fr> 1.8.0-1
- Update to bioconductor 2.2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.6.1-3
- Autorebuild for GCC 4.3

* Sat Feb 09 2008 Pingou <pingoufc4@yahoo.fr> 1.6.1-2
- Change on the URL

* Mon Oct 08 2007 Pingou <pingoufc4@yahoo.fr> 1.6.1-1
- Update to bioconductor 2.1 

* Wed Aug 29 2007 Pingou <pingoufc4@yahoo.fr> 1.4.1-2
- Change in the license tag to fit the guide lines

* Mon Jul 02 2007 Pingou <pingoufc4@yahoo.fr> 1.4.1-1
- initial package for Fedora

