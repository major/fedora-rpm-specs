%global packname devtools
%global packver  2.4.2
%global rlibdir  %{_datadir}/R/library

# Not available yet.
%bcond_with suggests

%if %{without suggests}
%global __suggests_exclude ^R\\((BiocManager)\\)
%endif

Name:             R-%{packname}
Version:          2.4.2
Release:          15%{?dist}
Summary:          Tools to Make Developing R Packages Easier

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-usethis >= 2.0.1
# Imports:   R-callr >= 3.6.0, R-cli >= 2.4.0, R-desc >= 1.3.0, R-ellipsis >= 0.3.1, R-fs >= 1.5.0, R-httr >= 1.4.2, R-lifecycle >= 1.0.0, R-memoise >= 2.0.0, R-pkgbuild >= 1.2.0, R-pkgload >= 1.2.1, R-rcmdcheck >= 1.3.3, R-remotes >= 2.3.0, R-rlang >= 0.4.10, R-roxygen2 >= 7.1.1, R-rstudioapi >= 0.13, R-rversions >= 2.0.2, R-sessioninfo >= 1.1.1, R-stats, R-testthat >= 3.0.2, R-tools, R-utils, R-withr >= 2.4.1
# Suggests:  R-BiocManager >= 1.30.12, R-covr >= 3.5.1, R-curl >= 4.3, R-digest >= 0.6.27, R-DT >= 0.17, R-foghorn >= 1.3.2, R-gh >= 1.2.1, R-gmailr >= 1.0.0, R-knitr >= 1.31, R-lintr >= 2.0.1, R-MASS, R-mockery >= 0.4.2, R-pingr >= 2.0.1, R-pkgdown >= 1.6.1, R-rhub >= 1.1.1, R-rmarkdown >= 2.7, R-spelling >= 2.2
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel >= 3.0.2
BuildRequires:    tex(latex)
BuildRequires:    R-usethis >= 2.0.1
BuildRequires:    R-callr >= 3.6.0
BuildRequires:    R-cli >= 2.4.0
BuildRequires:    R-covr >= 3.5.1
BuildRequires:    R-desc >= 1.3.0
BuildRequires:    R-ellipsis >= 0.3.1
BuildRequires:    R-httr >= 1.4.2
BuildRequires:    R-lifecycle >= 1.0.0
BuildRequires:    R-memoise >= 2.0.0
BuildRequires:    R-pkgbuild >= 1.2.0
BuildRequires:    R-pkgload >= 1.2.1
BuildRequires:    R-rcmdcheck >= 1.3.3
BuildRequires:    R-remotes >= 2.3.0
BuildRequires:    R-rlang >= 0.4.10
BuildRequires:    R-roxygen2 >= 7.1.1
BuildRequires:    R-rstudioapi >= 0.13
BuildRequires:    R-rversions >= 2.0.2
BuildRequires:    R-sessioninfo >= 1.1.1
BuildRequires:    R-stats
BuildRequires:    R-testthat >= 3.0.2
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-withr >= 2.4.1
%if %{with suggests}
BuildRequires:    R-BiocManager >= 1.30.12
%endif
BuildRequires:    R-curl >= 4.3
BuildRequires:    R-digest >= 0.6.27
BuildRequires:    R-DT >= 0.17
BuildRequires:    R-foghorn >= 1.3.2
BuildRequires:    R-gh >= 1.2.1
BuildRequires:    R-gmailr >= 1.0.0
BuildRequires:    R-knitr >= 1.31
BuildRequires:    R-lintr >= 2.0.1
BuildRequires:    R-MASS
BuildRequires:    R-mockery >= 0.4.2
BuildRequires:    R-pingr >= 2.0.1
BuildRequires:    R-pkgdown >= 1.6.1
BuildRequires:    R-rhub >= 1.1.1
BuildRequires:    R-rmarkdown >= 2.7
BuildRequires:    R-spelling >= 2.2

%description
Collection of package development tools.


%prep
%setup -q -c -n %{packname}
# remove conflicting test
rm -f %{packname}/tests/testthat/test-vignettes.R


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with suggests}
%{_bindir}/R CMD check --ignore-vignettes%{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/rstudio


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.2-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.4.2-12
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 12 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.4.2-8
- Ignore vignettes

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.4.2-7
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 2.4.2-5
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 2.4.2-1
- update to 2.4.2
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.2-1
- Update to latest version (#1880296)

* Sun Aug 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.1-1
- Update to latest version (rhbz#1823027)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.1.0-2
- rebuild for R 4

* Sat Feb 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Sat Feb 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-3
- Remove explicit runtime requirements

* Thu Jun 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- Fix incorrect files list

* Wed May 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- initial package for Fedora
