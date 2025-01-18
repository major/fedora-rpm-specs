%bcond_with bootstrap

%global packname dplyr
%global packver  1.1.4
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((Lahman|RMySQL|RPostgreSQL)\\)

Name:             R-%{packname}
Version:          %{packver}
Release:          3%{?dist}
Summary:          A Grammar of Data Manipulation

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli >= 3.4.0, R-generics, R-glue >= 1.3.2, R-lifecycle >= 1.0.3, R-magrittr >= 1.5, R-methods, R-pillar >= 1.5.1, R-R6, R-rlang >= 1.0.6, R-tibble >= 2.1.3, R-tidyselect >= 1.2.0, R-utils, R-vctrs >= 0.5.2
# Suggests:  R-bench, R-broom, R-callr, R-covr, R-DBI, R-dbplyr >= 2.2.1, R-ggplot2, R-knitr, R-Lahman, R-lobstr, R-microbenchmark, R-nycflights13, R-purrr, R-rmarkdown, R-RMySQL, R-RPostgreSQL, R-RSQLite, R-stringi >= 1.7.6, R-testthat >= 3.1.5, R-tidyr >= 1.3.0, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli >= 3.4.0
BuildRequires:    R-generics
BuildRequires:    R-glue >= 1.3.2
BuildRequires:    R-lifecycle >= 1.0.3
BuildRequires:    R-magrittr >= 1.5
BuildRequires:    R-methods
BuildRequires:    R-pillar >= 1.9.0
BuildRequires:    R-R6
BuildRequires:    R-rlang >= 1.1.0
BuildRequires:    R-tibble >= 3.2.0
BuildRequires:    R-tidyselect >= 1.2.0
BuildRequires:    R-utils
BuildRequires:    R-vctrs >= 0.6.0
BuildRequires:    R-callr
BuildRequires:    R-DBI
BuildRequires:    R-ggplot2
BuildRequires:    R-knitr
BuildRequires:    R-lobstr
BuildRequires:    R-microbenchmark
BuildRequires:    R-purrr
BuildRequires:    R-rmarkdown
BuildRequires:    R-RSQLite
BuildRequires:    R-stringi >= 1.7.6
BuildRequires:    R-testthat >= 3.1.5
BuildRequires:    R-withr
%if %{without bootstrap}
BuildRequires:    R-bench
BuildRequires:    R-broom
BuildRequires:    R-dbplyr >= 2.2.1
BuildRequires:    R-nycflights13
BuildRequires:    R-tidyr >= 1.3.0
BuildRequires:    R-ggplot2
%endif

Obsoletes: %{name}-devel < 0.8.5-4

%description
A fast, consistent tool for working with data frame like objects, both in
memory and out of memory.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
# Lahman is not yet packaged.
# RMySQL/RPostgreSQL are old wrappers, so won't be packaged by me at least.
sed -i \
    -e 's/covr, //g' \
    -e 's/Lahman, //g' \
    -e 's/RMySQL, RPostgreSQL, //g' \
    %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%if %{without bootstrap}
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
%{rlibdir}/%{packname}/data
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.4-1
- Update to latest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.2-5
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.2-1
- R-maint-sig mass rebuild
- Update to the latest version

* Mon Feb 27 2023 Tom Callaway <spot@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.0.10-1
- update to 1.0.10
- rebuild for R 4.2.1
- bootstrap on

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 1.0.6-2
- bootstrap off

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 1.0.6-1
- update to 1.0.6
- bootstrap
- Rebuilt for R 4.1.0

* Sat Mar 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.5-1
- Update to latest version (#1935731)

* Sun Feb 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.4-1
- Update to latest version (#1916807)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- Update to latest version (#1841868)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.8.5-2
- rebuild for R 4
- broom is now an R package so it does not need to be excluded
- remove from BuildRequires other packages that are not yet available

* Sun Mar 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.5-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.4-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.3-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.0.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.0.1-1
- initial package for Fedora
