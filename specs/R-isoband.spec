%bcond_with suggests

%global packname isoband
%global packver  0.2.7
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((sf)\\)

Name:             R-%{packname}
Version:          %{packver}
Release:          9%{?dist}
Summary:          Generate Isolines and Isobands from Regularly Spaced Elevation Grids

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-grid, R-utils
# Suggests:  R-covr, R-ggplot2, R-knitr, R-magick, R-microbenchmark, R-rmarkdown, R-sf, R-testthat, R-xml2
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-grid
BuildRequires:    R-utils
%if %{with suggests}
BuildRequires:    R-knitr
BuildRequires:    R-microbenchmark
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
BuildRequires:    R-xml2
BuildRequires:    R-ggplot2
BuildRequires:    R-magick
BuildRequires:    R-sf
%endif

%description
A fast C++ implementation to generate contour lines (isolines) and contour
polygons (isobands) from regularly spaced grids containing elevation data.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with suggests}
%{_bindir}/R CMD check %{packname}
%else
# _R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples --no-vignettes || ( cat %{packname}.Rcheck/tests/testthat.R* && exit 1 )
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/extdata
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.2.7-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.2.7-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Tom Callaway <spot@fedoraproject.org> - 0.2.7-1
- update to 0.2.7

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 0.2.5-1
- update to 0.2.5

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 0.2.4-2
- Rebuilt for R 4.1.0

* Wed Mar 10 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-1
- Update to latest version (#1934758)
- Un-bundle catch1, to fix build with latest glibc

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3-1
- Update to latest version (#1903110)

* Mon Aug 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- initial package for Fedora
