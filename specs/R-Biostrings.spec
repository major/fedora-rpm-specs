%global packname  Biostrings
%global Rvers     4.0.0
%global IRange    2.30.1

Name:             R-%{packname}
Version:          2.64.1
Release:          10%{dist}
Summary:          String objects representing biological sequences
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/Biostrings.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:    R-devel >= %{Rvers} tex(latex) R-methods R-utils R-IRanges-devel >= %{IRange}
BuildRequires:    R-XVector-devel >= 0.29.2, R-BiocGenerics >= 0.37.0, R-S4Vectors-devel >= 0.27.12
BuildRequires:    R-graphics, R-methods, R-stats, R-utils, R-grDevices, R-crayon, R-GenomeInfoDb

%description
Memory efficient string containers, string matching algorithms, and other
utilities, for fast manipulation of large biological sequences or set of
sequences.

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

# architecture dependent package
mkdir -p %{buildroot}%{_libdir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

# Empty file
rm -f %{buildroot}%{_libdir}/R/library/%{packname}/doc/GenomeSearching.R

%check
# Requires for R-BSgenome which cannot build without R-Biostring
#%%{_bindir}/R CMD check %%{packname}

%files
#i386 arch
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc
%{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/unitTests/

%files devel
%{_libdir}/R/library/%{packname}/include

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.64.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.64.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.64.1-8
- R-maint-sig mass rebuild

* Sat Apr  20 2024 Miroslav Suchý <msuchy@redhat.com> - 2.64.1-7
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.64.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.64.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.64.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.64.1-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.64.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 2.64.1-1
- update to 2.64.1
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.60.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.60.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.60.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 2.60.1-1
- update to 2.60.1
- Rebuilt for R 4.1.0

* Wed Feb  3 2021 Tom Callaway <spot@fedoraproject.org> - 2.58.0-1
- update to 2.58.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 2.56.0-1
- update to 2.56.0
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Tom Callaway <spot@fedoraproject.org> - 2.54.0-1
- update to 2.54.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.48.0-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.48.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.48.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.48.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 2.48.0-1
- update to 2.48.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Tom Callaway <spot@fedoraproject.org> - 2.44.0-1
- update to 2.44.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec  7 2015 Tom Callaway <spot@fedoraproject.org> - 2.38.2-1
- update to 2.38.2

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Tom Callaway <spot@fedoraproject.org> - 2.36.1-1
- update to 2.36.1, drop doc off DESCRIPTION

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun  9 2014 Tom Callaway <spot@fedoraproject.org> - 2.32.0-1
- update to 2.32.0

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 pingou <pingou@pingoured.fr> 2.30.1-1
- Update to version 2.30.1

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 07 2013 pingou <pingou@pingoured.fr> 2.28.0-1
- Update to version 2.28.0

* Wed Feb 13 2013 pingou <pingou@pingoured.fr> 2.26.3-1
- Update to version 2.26.3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 pingou <pingou@pingoured.fr> 2.26.2-1
- Update to version 2.26.2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> 2.22.0-1
- update to 2.22.0

* Sat Jul 02 2011 pingou <pingou@pingoured.fr> 2.20.1-1
- Update to version 2.20.1

* Tue Mar 15 2011 pingou <pingou@pingoured.fr> 2.18.4-1
- Update to version 2.18.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 pingou <pingou@pingoured.fr> 2.18.2-1
- Update to version 2.18.2

* Tue Oct 26 2010 pingou <pingou@pingoured.fr> 2.18.0-1
- Update to version 2.18.0

* Tue Sep 07 2010 pingou <pingou@pingoured.fr> 2.16.9-1
- Update to version 2.16.9

* Thu Jul 01 2010 pingou <pingou@pingoured.fr> 2.16.6-1
- Update to version 2.16.6
- Update the url and source to a more stable format

* Sat Jun 05 2010 pingou <pingou@pingoured.fr> 2.16.4-1
- Update to version 2.16.4
- Update to R-2.11.0
- Remove the post/postun scriplet
- Update R and BR to R-core and R-devel

* Tue Mar 02 2010 pingou <pingou@pingoured.fr> 2.14.12-1
- Update to 2.14.12

* Thu Jan 14 2010 pingou <pingou@pingoured.fr> 2.14.10-1
- Update to 2.14.10

* Thu Dec 17 2009 pingou <pingou@pingoured.fr> 2.14.9-2
- Update dependancy to IRanges 1.4.8

* Thu Dec 17 2009 pingou <pingou@pingoured.fr> 2.14.9-1
- Update to 2.14.9

* Fri Dec 04 2009 pingou <pingou@pingoured.fr> 2.14.7-2
- Remove the folder R-ex

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 2.14.7-1
- Update to 2.14.7
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0

* Fri Sep 18 2009 pingou <pingou@pingoured.fr> 2.12.9-1
- Update to 2.12.9

* Sun Aug 23 2009 pingou <pingou@pingoured.fr> 2.12.8-1
- Update to 2.12.8

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 pingou <pingou@pingoured.fr> 2.12.7-1
- Update to 2.12.7
 
* Fri Jun 12 2009 pingou <pingou@pingoured.fr> 2.12.6-1
- Update to 2.12.6

* Wed May 06 2009 pingou <pingou@pingoured.fr> 2.12.1-2
- Solve dependencies issue (Add R-Biobase as R and BR)
/
* Fri May 01 2009 pingou <pingou@pingoured.fr> 2.12.1-1
- Update to 2.12.1

* Tue Apr 28 2009 pingou <pingou@pingoured.fr> 2.12.0-1
- Update to Bioconductor 2.4 for R 2.9.0

* Fri Apr 03 2009 pingou <pingou@pingoured.fr> 2.11.47-1
- Update to the development version of bioconductor

* Wed Apr 01 2009 pingou <pingou -AT- pingoured.fr> 2.10.21-2
- Update URL to remove an unused macro
- Improve english in the comments
- Remove pkgconfig as BR of the -devel

* Fri Mar 13 2009 pingou <pingou -AT- pingoured.fr> 2.10.21-1
- initial package for Fedora
