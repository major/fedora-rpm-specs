%define packname  Biobase
%define Rversion  3.4.0

Name:             R-%{packname}
Version:          2.56.0
Release:          10%{dist}
Summary:          Base functions for Bioconductor
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/Biobase.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:    R-devel >= %{Rversion} tex(latex) R-tkWidgets R-BiocGenerics >= 0.27.1 R-utils R-methods

%description
Base functions for Bioconductor (bioconductor.org). Biobase provides
functions that are needed by many other Bioconductor packages or which
replace R functions.

%description -l fr
Bibliothèque contenant des fonctions requises par d'autres bibliothèques
ou qui remplacent certaines fonctions dans R

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

%check
# This library ask for the library ALL which can not be compiled without
# R-Biobase
#%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/unitTests/
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/scripts
%{_libdir}/R/library/%{packname}/ExpressionSet
%{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/Code
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/testClass.R
%{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/doc
%{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.56.0-8
- R-maint-sig mass rebuild

* Sat Apr  20 2024 Miroslav Suchý <msuchy@redhat.com> - 2.56.0-7
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.56.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 2.56.0-1
- update to 2.56.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.50.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.50.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb  3 2021 Tom Callaway <spot@fedoraproject.org> - 2.50.0-1
- update to 2.50.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.48.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.48.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.48.0-1
- update to 2.48.0
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Tom Callaway <spot@fedoraproject.org> - 2.46.0-1
- update to 2.46.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.40.0-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 2.40.0-1
- update to 2.40.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.36.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.36.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.36.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Tom Callaway <spot@fedoraproject.org> - 2.36.2-1
- update to 2.36.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun  3 2015 Tom Callaway <spot@fedoraproject.org> - 2.28.0-1
- update to 2.28.0

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun  9 2014 Tom Callaway <spot@fedoraproject.org> - 2.24.0-1
- update to 2.24.0

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.22.0-2
- Fix the name of the unitTests folder RHBZ#1099885

* Mon Jan 27 2014 pingou <pingou@pingoured.fr> 2.22.0-1
- Update to version 2.22.0

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 pingou <pingou@pingoured.fr> 2.20.1-1
- Update to version 2.20.1

* Sun Apr 07 2013 pingou <pingou@pingoured.fr> 2.20.0-1
- Update to version 2.20.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 pingou <pingou@pingoured.fr> 2.18.0-1
- Update to version 2.18.0
- + BR: R-BiocGenerics

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> 2.14.0-2
- rebuild for R 2.14.0

* Thu Nov 03 2011 pingou <pingou@pingoured.fr> 2.14.0-1
- Update to version 2.14.0

* Sun Jul 03 2011 pingou <pingou@pingoured.fr> 2.12.2-1
- Update to version 2.12.2

* Wed Jun 22 2011 pingou <pingou@pingoured.fr> 2.12.1-1
- Update to version 2.12.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 pingou <pingou@pingoured.fr> 2.10.0-1
- Update to version 2.10.0

* Tue May 11 2010 pingou <pingou@pingoured.fr> 2.8.0-1
- Update to version 2.8.0
- Fix url to a more stable form
- Fix BR for latex
- Remove R on post/postun since there is no post/postun

* Thu Dec 17 2009 pingou <pingou@pingoured.fr> 2.6.1-1
- Update to 2.6.1

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 2.6.0-1
- Update to 2.6.0
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0

* Fri Nov 20 2009 pingou <pingou@pingoured.fr> 2.4.1-2
- Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 pingou <pingou@pingoured.fr> 2.4.1-1
- Update to 2.4.1
- Remove bad french translation

* Tue Apr 28 2009 pingou <pingou@pingoured.fr> 2.4.0-1
- Update to Bioconductor 2.4 and R-2.9.0

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 pingou <pingou-at-pingoured.fr> 2.2.2-1
- New update

* Thu Jan 22 2009 pingou <pingoufc4-at-yahoo.fr> 2.2.1-1
- New update

* Thu Nov 20 2008 pingou <pingoufc4-at-yahoo.fr> 2.2.0-2
- Correct the Source0

* Mon Oct 27 2008 pingou <pingoufc4-at-yahoo.fr> 2.2.0-1
- Update to version 2.2.0 for R >= 2.8.0

* Wed Jun 25 2008 pingou <pingoufc4-at-yahoo.fr> 2.0.1-1
- Update to version 2.0.1

* Fri May 02 2008 Pingou <pingoufc4@yahoo.fr> 2.0.0-1
- Update to bioconductor 2.2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.16.1-5
- Autorebuild for GCC 4.3

* Tue Jan 08 2008 Pingou <pingoufc4@yahoo.fr> 1.16.1-4
- change on the BR

* Sun Nov 18 2007 Pingou <pingoufc4@yahoo.fr> 1.16.1-3
- Change on the description

* Sun Nov 18 2007 Pingou <pingoufc4@yahoo.fr> 1.16.1-2
- Change on the install command
- Change on the Requires
- Change on the description

* Mon Oct 08 2007 Pingou <pingoufc4@yahoo.fr> 1.16.1-1
- Update to bioconductor 2.1 

* Fri Jul 13 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-4
- Change in the R and BR section to fit the guidelines

* Tue Jul 10 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-3
- Change in post and postun to fit the packaging guidelines
- Change in prep to fit the guidelines

* Mon Jun 24 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-2
- Change de %%doc to avoid redundancy

* Thu May 17 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-1
- Submitting to Fedora Extras

* Wed Apr 25 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-0.1
- Build of the rpm
