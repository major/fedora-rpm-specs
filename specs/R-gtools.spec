%global packname gtools
%global packver  3.9.3
%global rlibdir  %{_libdir}/R/library

# Some tests use the network.
%bcond_with network

%bcond_with suggests

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Summary:          Various R Programming Tools

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:          GPL-2.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods, R-stats, R-utils
# Imports:
# Suggests:  R-car, R-gplots, R-knitr, R-rstudioapi, R-SGP, R-taxize
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-stats
BuildRequires:    R-utils
%if %{with suggests}
BuildRequires:    R-car
BuildRequires:    R-gplots
BuildRequires:    R-knitr
BuildRequires:    R-rstudioapi
BuildRequires:    R-SGP
BuildRequires:    R-taxize
%endif


%description
Functions to assist in R programming, including:
    - assist in developing, updating, and maintaining R and R packages,
    - calculate the logit and inverse logit transformations,
    - test if a value is missing, empty or contains only NA and NULL values,
    - manipulate R's .Last function,
    - define macros,
    - detect odd and even integers,
    - convert strings containing non-ASCII characters (like single quotes) to
      plain ASCII,
    - perform a binary search,
    - sort strings containing both numeric and character components,
    - create a factor variable from the quantiles of a continuous variable,
    - enumerate permutations and combinations,
    - calculate and convert between fold-change and log-ratio,
    - calculate probabilities and generate random numbers from Dirichlet
      distributions,
    - apply a function over adjacent subsets of a vector,
    - modify the TCP_NODELAY flag for socket objects,
    - efficient 'rbind' of data frames, even if the column names don't match,
    - generate significance stars from p-values,
    - convert characters to/from ASCII codes,
    - convert character vector to ASCII representation.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with network}
 %if %{with suggests}
  %{_bindir}/R CMD check %{packname}
 %else
  _R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
 %endif
%else
 # No network for examples that check R version.
 rm %{packname}/tests/test_setTCPNoDelay.R
 %if %{with suggests}
  %{_bindir}/R CMD check %{packname} --no-examples
 %else
  _R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples
 %endif
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.9.3-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 3.9.3-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 3.9.3-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 3.9.3-1
- update to 3.9.3
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun  8 2021 Tom Callaway <spot@fedoraproject.org> - 3.9.2-1
- update to 3.9.2
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 3.8.2-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.8.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.8.1-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.8.1-1
- Update to latest version

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 3.5.0-2
- rebuild for R 3.5.0

* Tue Mar 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 3.5.0-1
- initial package for Fedora
