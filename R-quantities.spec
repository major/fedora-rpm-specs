%global packname  quantities
%global rlibdir   %{_libdir}/R/library

Name:           R-%{packname}
Version:        0.1.6
Release:        6%{?dist}
Summary:        Quantity Calculus for R Vectors

License:        MIT
URL:            https://cran.r-project.org/package=%{packname}
Source0:        https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

BuildRequires:  R-devel >= 3.1.0, R-Rcpp-devel >= 0.12.10
BuildRequires:  R-units >= 0.6.7, R-errors >= 0.3.4, R-testthat
BuildRequires:  R-dplyr, R-vctrs, R-pillar
# BuildRequires:  R-tidyr, R-knitr, R-markdown

%description
Integration of the 'units' and 'errors' packages for a complete quantity
calculus system for R vectors, matrices and arrays, with automatic
propagation, conversion, derivation and simplification of magnitudes and
uncertainties.
Documentation about 'units' and 'errors' is provided in the papers by Pebesma,
Mailund & Hiebert (2016, <doi:10.32614/RJ-2016-061>) and by Ucar, Pebesma &
Azcorra (2018, <doi:10.32614/RJ-2018-075>), included in those packages as
ignettes; see 'citation("quantities")' for details.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
export LANG=C.UTF-8
export _R_CHECK_FORCE_SUGGESTS_=0
%{_bindir}/R CMD check --ignore-vignettes %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

%changelog
* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 0.1.6-6
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 0.1.6-2
- Rebuilt for R 4.1.0

* Sat Feb 27 2021 Iñaki Úcar <iucar@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.1.4-1
- update to 0.1.4
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.2-4
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Iñaki Úcar <iucar@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Wed Oct 03 2018 Iñaki Úcar <iucar@fedoraproject.org> - 0.1.1-2
- Remove 'rm -rf %{buildroot}', not needed

* Mon Oct 01 2018 Iñaki Úcar <iucar@fedoraproject.org> - 0.1.1-1
- Initial package for Fedora
