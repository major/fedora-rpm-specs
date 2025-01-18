%global packname lintr
%global packver  3.1.1
%global rlibdir  %{_datadir}/R/library

%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          6%{?dist}
Summary:          A 'Linter' for R Code

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-backports >= 1.1.7, R-codetools, R-cyclocomp, R-digest, R-glue, R-knitr, R-rex, R-stats, R-utils, R-xml2 >= 1.0.0, R-xmlparsedata >= 1.0.5
# Suggests:  R-bookdown, R-covr, R-httr >= 1.2.1, R-jsonlite, R-mockery, R-patrick, R-rlang, R-rmarkdown, R-rstudioapi >= 0.2, R-testthat >= 3.1.5, R-tibble, R-tufte, R-withr
# LinkingTo:
# Enhances:  R-data.table

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-backports >= 1.1.7
BuildRequires:    R-codetools
BuildRequires:    R-cyclocomp
BuildRequires:    R-digest
BuildRequires:    R-glue
BuildRequires:    R-knitr
BuildRequires:    R-rex
BuildRequires:    R-stats
BuildRequires:    R-utils
BuildRequires:    R-xml2 >= 1.0.0
BuildRequires:    R-xmlparsedata >= 1.0.5
# Suggests
%if %{with_suggests}
BuildRequires:    R-bookdown
BuildRequires:    R-covr
BuildRequires:    R-httr >= 1.2.1
BuildRequires:    R-jsonlite
BuildRequires:    R-mockery
BuildRequires:    R-patrick
BuildRequires:    R-rlang
BuildRequires:    R-rmarkdown
BuildRequires:    R-rstudioapi >= 0.2
BuildRequires:    R-testthat >= 3.1.5
BuildRequires:    R-tibble
BuildRequires:    R-tufte
BuildRequires:    R-withr
%endif

%description
Checks adherence to a given style, syntax errors and possible semantic
issues.  Supports on the fly checking of R code edited with 'RStudio IDE',
'Emacs', 'Vim', 'Sublime Text' and 'Atom'.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-tests --no-examples
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
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/example/
%{rlibdir}/%{packname}/extdata/
%{rlibdir}/%{packname}/lintr/
%{rlibdir}/%{packname}/rstudio/
%{rlibdir}/%{packname}/syntastic/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 3.1.1-4
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Tom Callaway <spot@fedoraproject.org> - 3.1.1-1
- update to 3.1.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 5 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 3.0.2-1
- Update to 3.0.2

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.1-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 17 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1 (RHBZ #2126458)

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 3.0.0-1
- update to 3.0.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 2.0.1-5
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.0.1-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- initial package for Fedora
