%global packname dbplyr
%global packver  2.5.0
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((Lahman|RPostgreSQL)\\)

# Not yet available.
%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          3%{?dist}
Summary:          A 'dplyr' Back End for Databases

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-blob >= 1.2.0, R-cli >= 3.4.1, R-DBI >= 1.0.0, R-dplyr >= 1.1.0, R-glue >= 1.2.0, R-lifecycle >= 1.0.3, R-magrittr, R-methods, R-pillar >= 1.5.0, R-purrr >= 1.0.1, R-R6 >= 2.2.2, R-rlang >= 1.0.6, R-tibble >= 1.4.2, R-tidyr >= 1.3.0, R-tidyselect >= 1.2.0, R-utils, R-vctrs >= 0.5.0, R-withr
# Suggests:  R-bit64, R-covr, R-knitr, R-Lahman, R-nycflights13, R-odbc, R-RMariaDB >= 1.0.2, R-rmarkdown, R-RPostgres >= 1.1.3, R-RPostgreSQL, R-RSQLite >= 2.2.15, R-testthat >= 3.0.2
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-blob >= 1.2.0
BuildRequires:    R-cli >= 3.4.1
BuildRequires:    R-DBI >= 1.1.3
BuildRequires:    R-dplyr >= 1.1.2
BuildRequires:    R-glue >= 1.6.2
BuildRequires:    R-lifecycle >= 1.0.3
BuildRequires:    R-magrittr
BuildRequires:    R-methods
BuildRequires:    R-pillar >= 1.9.0
BuildRequires:    R-purrr >= 1.0.1
BuildRequires:    R-R6 >= 2.2.2
BuildRequires:    R-rlang >= 1.1.1
BuildRequires:    R-tibble >= 3.2.1
BuildRequires:    R-tidyr >= 1.3.0
BuildRequires:    R-tidyselect >= 1.2.1
BuildRequires:    R-utils
BuildRequires:    R-vctrs >= 0.6.3
BuildRequires:    R-withr
BuildRequires:    R-bit64
BuildRequires:    R-knitr
BuildRequires:    R-nycflights13
BuildRequires:    R-odbc
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 3.1.10
BuildRequires:    R-RMariaDB
BuildRequires:    R-RPostgres
BuildRequires:    R-RSQLite
%if %{with_suggests}
BuildRequires:    R-Lahman
BuildRequires:    R-RPostgreSQL
%endif

%description
A 'dplyr' back end for databases that allows you to work with remote database
tables as if they are in-memory data frames. Basic features works with any
database that has a 'DBI' back end; more advanced features require 'SQL'
translation to be provided by the package author.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION

# Fix executable bits.
chmod -x README.md
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
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


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.5.0-1
- Update to latest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.3.1-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.3.1-2
- R-maint-sig mass rebuild

* Fri Mar  3 2023 Tom Callaway <spot@fedoraproject.org> - 2.3.1-1
- update to 2.3.1

* Fri Jan 20 2023 Tom Callaway <spot@fedoraproject.org> - 2.3.0-1
- update to 2.3.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 04 2022 Iñaki Úcar <iucar@fedoraproject.org> - 2.2.1-1
- R 4.2.1, update to 2.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 2.1.1-2
- Rebuilt for R 4.1.0

* Wed Apr 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.1-1
- Update to latest version (#1946640)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0-1
- Update to latest version (#1893966)

* Fri Aug 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4-1
- Update to latest version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.3-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.3-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version

* Mon Mar 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- initial package for Fedora
