%global packname expm
%global packver 0.999
%global packrel 6

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          16%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{packver}-%{packrel}.tar.gz
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              http://cran.r-project.org/web/packages/expm
Summary:          Computation of the matrix exponential and related quantities
BuildRequires:    R-devel >= 3.4.0, tetex-latex, R-Matrix R-methods

%description
Efficient calculation of the exponential of a matrix. The package
contains an R interface and a C API that package authors can use.

%prep
%setup -q -c -n %{packname}

%build

%install
# Specific installation procedure for R
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%check
# Needs unpackaged 'RColorBrewer' 'sfsmisc'
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/data
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/demo/
%{_libdir}/R/library/%{packname}/help
%dir %{_libdir}/R/library/%{packname}/po
%lang(en) %{_libdir}/R/library/%{packname}/po/en*/
%lang(fr) %{_libdir}/R/library/%{packname}/po/fr/
%{_libdir}/R/library/%{packname}/libs/%{packname}.so
%{_libdir}/R/library/%{packname}/test-tools.R

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.999.6-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.999.6-13
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.999.6-9
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug  3 2022 Tom Callaway <spot@fedoraproject.org> - 0.999.6-7
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 0.999.6-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Tom Callaway <spot@fedoraproject.org> - 0.999.6-1
- update to 0.999-6

* Thu Aug 13 2020 Tom Callaway <spot@fedoraproject.org> - 0.999.5-1
- update to 0.999-5

* Mon Aug 10 2020 Tom Callaway <spot@fedoraproject.org> - 0.999.4-8
- rebuild for FlexiBLAS R

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 0.999.4-6
- rebuild for R 4

* Tue Feb 18 2020 Tom Callaway <spot@fedoraproject.org> - 0.999.4-5
- rebuild for R without libRlapack.so

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.999.4-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 22 2019 Tom Callaway <spot@fedoraproject.org> 0.999.4-1
- update to 0.999-4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 0.999.2-6
- rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Tom Callaway <spot@fedoraproject.org> - 0.999.2-4
- rebuild for new libgfortran

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.999.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Tom Callaway <spot@fedoraproject.org> - 0.999.2-1
- update to 0.999-2

* Tue Feb 14 2017 Tom Callaway <spot@fedoraproject.org> - 0.999.1-1
- update to 0.999-1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May  8 2014 Tom Callaway <spot@fedoraproject.org> - 0.99.1.1-1
- initial package
