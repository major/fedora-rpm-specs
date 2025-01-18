%global packname styler
%global packver  1.10.3
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((data\\.tree)\\)

%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          3%{?dist}
Summary:          Non-Invasive Pretty Printing of R Code

License:          GPL-3.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli >= 3.1.1, R-magrittr >= 2.0.0, R-purrr >= 0.2.3, R-R.cache >= 0.15.0, R-rlang >= 1.0.0, R-rprojroot >= 1.1, R-tools, R-vctrs >= 0.4.1, R-withr >= 2.3.0
# Suggests:  R-data.tree >= 0.1.6, R-digest, R-dplyr, R-here, R-knitr, R-prettycode, R-rmarkdown, R-roxygen2, R-rstudioapi >= 0.7, R-tibble >= 1.4.2, R-testthat >= 3.0.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli >= 3.1.1
BuildRequires:    R-magrittr >= 2.0.0
BuildRequires:    R-purrr >= 0.2.3
BuildRequires:    R-R.cache >= 0.15.0
BuildRequires:    R-rlang >= 1.0.0
BuildRequires:    R-rprojroot >= 1.1
BuildRequires:    R-tools
BuildRequires:    R-vctrs >= 0.4.1
BuildRequires:    R-withr >= 2.3.0
%if %{with_suggests}
BuildRequires:    R-data.tree >= 0.1.6
%endif
BuildRequires:    R-digest
BuildRequires:    R-dplyr
BuildRequires:    R-here
BuildRequires:    R-knitr
BuildRequires:    R-prettycode
BuildRequires:    R-rmarkdown
BuildRequires:    R-roxygen2
BuildRequires:    R-rstudioapi >= 0.7
BuildRequires:    R-tibble >= 1.4.2
BuildRequires:    R-testthat >= 3.0.0

%description
Pretty-prints R code without changing the user's formatting intent.


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
%if %{with_suggests}
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check --ignore-vignettes %{packname}
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
%{rlibdir}/%{packname}/rstudio


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.10.3-1
- Update to latest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.10.0-5
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 26 2023 Tom Callaway <spot@fedoraproject.org> - 1.10.0-1
- update to 1.10.0

* Fri May 12 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.9.1-3
- Ignore vignettes

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.9.1-2
- R-maint-sig mass rebuild

* Mon Mar  6 2023 Tom Callaway <spot@fedoraproject.org> - 1.9.1-1
- update to 1.9.1

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 1.7.0-1
- update to 1.7.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.4.1-3
- Rebuilt for R 4.1.0

* Sun Apr 04 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-2
- Remove unnecessary script, fixing automatic Requires

* Sun Apr 04 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-1
- Update to latest version (#1941875)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.3.2-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- initial package for Fedora
