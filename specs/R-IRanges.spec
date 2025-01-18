%global packname  IRanges
%global Rvers     4.0.0
%global suggests  0

Name:             R-%{packname}
Version:          2.30.1
Release:          10%{dist}
Summary:          Low-level containers for storing sets of integer ranges
# Automatically converted from old format: Artistic 2.0 and Copyright only - review is highly recommended.
License:          Artistic-2.0 AND LicenseRef-Callaway-Copyright-only
# See https://www.redhat.com/archives/fedora-r-devel-list/2009-April/msg00001.html
URL:              http://bioconductor.org/packages/release/bioc/html/IRanges.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:    R-devel >= %{Rvers} tex(latex)
BuildRequires:    R-methods R-stats R-RUnit R-utils R-stats4 R-BiocGenerics >= 0.39.2
BuildRequires:    R-S4Vectors-devel >= 0.33.3
%if %{suggests}
BuildRequires:    R-GenomicRanges
BuildRequires:    R-BSgenome.Celegans.UCSC.ce2
BuildRequires:    R-XVector
BuildRequires:    R-Rsamtools
BuildRequires:    R-GenomicAlignments
BuildRequires:    R-GenomicFeatures
BuildRequires:    R-pasillaBamSubset
BuildRequires:    R-RUnit
BuildRequires:    R-BiocStyle
%endif

%description
The IRanges class and its extensions are low-level containers
for storing sets of integer ranges. A typical use of these containers
in biology is for representing a set of chromosome regions.
More specific extensions of the IRanges class will typically
allow the storage of additional information attached to each
chromosome region as well as a hierarchical relationship between
these regions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}


# x86/x86_64 -> Architecture dependent package
mkdir -p %{buildroot}%{_libdir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

%check
%if %{suggests}
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/unitTests

%files devel
%{_libdir}/R/library/%{packname}/include

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.30.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.30.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.30.1-8
- R-maint-sig mass rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.30.1-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.30.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.30.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.30.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.30.1-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 2.30.1-1
- update to 2.30.1
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 2.26.0-1
- update to 2.26.0
- Rebuilt for R 4.1.0

* Wed Feb  3 2021 Tom Callaway <spot@fedoraproject.org> - 2.24.1-1
- update to 2.24.1

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 2.22.2-1
- update to 2.22.2
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Tom Callaway <spot@fedoraproject.org> - 2.20.1-1
- update to 2.20.1

* Mon Nov  4 2019 Tom Callaway <spot@fedoraproject.org> - 2.20.0-1
- update to 2.20.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.16.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  8 2019 Tom Callaway <spot@fedoraproject.org> - 2.16.0-1
- update to 2.16.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 2.14.10-1
- update to 2.14.10, rebuild for R 3.5.0

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 2.12.0-1
- update to 2.12.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Tom Callaway <spot@fedoraproject.org> - 2.10.1-1
- update to 2.10.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.8.1-1
- Update to 2.8.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec  7 2015 Tom Callaway <spot@fedoraproject.org> - 2.4.4-1
- update to 2.4.4

* Fri Jul 03 2015 pingou <pingou@pingoured.fr> 2.2.5-1
- Update to version 2.2.5

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Tom Callaway <spot@fedoraproject.org> - 2.2.1-1
- update to 2.2.1
- fix DESCRIPTION to not be doc
- bootstrap pass

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 pingou <pingou@pingoured.fr> 1.22.9-1
- Update to version 1.22.9

* Mon Jun  9 2014 Tom Callaway <spot@fedoraproject.org> - 1.22.8-1
- update to 1.22.8

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb  3 2014 Tom Callaway <spot@fedoraproject.org> - 1.20.6-2
- fix XVector to be a conditionalized BR

* Mon Jan 27 2014 pingou <pingou@pingoured.fr> 1.20.6-1
- Update to version 1.20.6

* Fri Jan 24 2014 Tom Callaway <spot@fedoraproject.org> - 1.20.6-1
- update to 1.20.6

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 pingou <pingou@pingoured.fr> 1.18.2-1
- Update to version 1.18.2

* Mon Apr 15 2013 Tom Callaway <spot@fedoraproject.org> - 1.18.0-2
- disable bootstrap

* Sun Apr 07 2013 pingou <pingou@pingoured.fr> 1.18.0-1
- Update to version 1.18.0

* Thu Feb 28 2013 pingou <pingou@pingoured.fr> 1.16.6-1
- Update to version 1.16.6

* Wed Feb 13 2013 pingou <pingou@pingoured.fr> 1.16.5-1
- Update to version 1.16.5

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 pingou <pingou@pingoured.fr> 1.16.4-1
- Update to version 1.16.4
- + BR: R-GenomicRanges

* Mon Jul 23 2012 pingou <pingou@pingoured.fr> 1.14.4-2
- + BR: R-BiocGenerics

* Mon Jul 23 2012 pingou <pingou@pingoured.fr> 1.14.4-1
- Update to version 1.14.4

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> 1.12.1-1
- update to 1.12.1

* Wed Jun 22 2011 pingou <pingou@pingoured.fr> 1.10.4-1
- Update to version 1.10.4

* Tue Mar 15 2011 pingou <pingou@pingoured.fr> 1.8.9-1
- Update to version 1.8.9

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 pingou <pingou@pingoured.fr> 1.8.8-1
- Update to version 1.8.8

* Mon Dec 13 2010 pingou <pingou@pingoured.fr> 1.8.7-1
- Update to version 1.8.7

* Thu Nov 25 2010 pingou <pingou@pingoured.fr> 1.8.3-1
- Update to version 1.8.3

* Sun Nov 07 2010 pingou <pingou@pingoured.fr> 1.8.2-1
- Update to version 1.8.2
- Change requires from R to R-core

* Thu Oct 14 2010 pingou <pingou@pingoured.fr> 1.6.17-1
- Update to version 1.6.17

* Tue Sep 07 2010 pingou <pingou@pingoured.fr> 1.6.16-1
- Update to version 1.6.16

* Mon Jul 05 2010 pingou <pingou@pingoured.fr> 1.6.8-2
- Remove Require post and postun
- Change the URL and source0 to a more stable form
- Fix BR to tex(latex)

* Tue Jun 29 2010 pingou <pingou@pingoured.fr> 1.6.8-1
- Update to version 1.6.8

* Sat Jun 05 2010 pingou <pingou@pingoured.fr> 1.6.5-1
- Update to version 1.6.5

* Tue May 11 2010 pingou <pingou@pingoured.fr> 1.6.1-1
- Update to version 1.6.1

* Sat Mar 27 2010 pingou <pingou@pingoured.fr> 1.4.16-1
- Update to 1.4.16

* Thu Feb 11 2010 pingou <pingou@pingoured.fr> 1.4.11-1
- Update to 1.4.11

* Mon Feb 01 2010 pingou <pingou@pingoured.fr> 1.4.10-1
- Update to 1.4.10

* Thu Dec 17 2009 pingou <pingou@pingoured.fr> 1.4.9-1
- Update to 1.4.9

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 1.4.7-1
- Update to 1.4.7
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 pingou <pingou@pingoured.fr> 1.2.3-1
- Update to 1.2.3

* Wed Apr 29 2009 pingou <pingou@pingoured.fr> 1.2.0-2
- Update the file section to package doc
- Update the Requires and BR to take into account R version

* Tue Apr 28 2009 pingou <pingou@pingoured.fr> 1.2.0-1
- Update to Bioconductor 2.4 and R-2.9.0

* Wed Apr 01 2009 pingou <pingou@pingoured.fr> 1.1.55-1
- New release from bioconductor 2.4 which includes the change in
 the description file for the license used
- Update the license to its correct format

* Sun Mar 22 2009 pingou <pingou -AT- pingoured.fr> 1.0.14-3
- The main package owns the directory
- Remove pkgconfig as R for the devel package
- Define becomes global

* Sat Mar 21 2009 pingou <pingou -AT- pingoured.fr> 1.0.14-2
- Add R-Matrix as R and BR

* Fri Mar 13 2009 pingou <pingou -AT- pingoured.fr> 1.0.14-1
- Update to 1.0.14

* Wed Feb 18 2009 pingou <pingou -AT- pingoured.fr> 1.0.11-1
- initial package for Fedora
