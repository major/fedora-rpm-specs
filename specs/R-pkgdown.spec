%global packname pkgdown
%global packver  2.0.6
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((leaflet|rticles)\\)

# Tests and vignettes use the network.
%bcond_with network

# Not available yet.
%global with_loop 0

Name:             R-%{packname}
Version:          %{packver}
Release:          9%{?dist}
Summary:          Make Static HTML Documentation for a Package

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-callr >= 2.0.2, R-crayon, R-desc, R-digest, R-downlit, R-fs >= 1.3.0, R-httr >= 1.4.2, R-magrittr, R-memoise, R-openssl, R-purrr, R-ragg, R-rematch2, R-rlang >= 0.3.0, R-rmarkdown >= 1.1.9007, R-tibble, R-tools, R-whisker, R-withr, R-xml2 >= 1.3.1, R-yaml
# Suggests:  R-covr, R-htmlwidgets, R-jsonlite, R-knitr, R-leaflet, R-pkgload >= 1.0.2, R-testthat >= 2.1.0, R-rticles, R-rsconnect, R-rstudioapi
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-bslib >= 0.3.1
BuildRequires:    R-callr >= 2.0.2
BuildRequires:    R-cli
BuildRequires:    R-desc
BuildRequires:    R-digest
BuildRequires:    R-downlit >= 0.4.0
BuildRequires:    R-fs >= 1.4.0
BuildRequires:    R-httr >= 1.4.2
BuildRequires:    R-jsonlite
BuildRequires:    R-magrittr
BuildRequires:    R-memoise
BuildRequires:    R-purrr
BuildRequires:    R-ragg
BuildRequires:    R-rlang >= 1.0.0
BuildRequires:    R-rmarkdown >= 1.1.9007
BuildRequires:    R-tibble
BuildRequires:    R-whisker
BuildRequires:    R-withr >= 2.4.3
BuildRequires:    R-xml2 >= 1.3.1
BuildRequires:    R-yaml
# Suggests
BuildRequires:    R-evaluate
BuildRequires:    R-htmltools
BuildRequires:    R-htmlwidgets
BuildRequires:    R-knitr
BuildRequires:    R-lifecycle
BuildRequires:    R-methods
BuildRequires:    R-openssl
BuildRequires:    R-pkgload >= 1.0.2
BuildRequires:    R-rsconnect
BuildRequires:    R-rstudioapi
BuildRequires:    R-sass
BuildRequires:    R-testthat >= 3.1.3
BuildRequires:    R-tools
%if %{with_loop}
BuildRequires:    R-rticles
# Not packaged
BuildRequires:    R-diffviewer
%endif

%description
Generate an attractive and useful website from a source package. pkgdown
converts your documentation, vignettes, README, and more to HTML making it easy
to share information about your package online.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without network}
ARGS='--no-tests --no-vignettes'
%endif
%if %{with_loop}
%{_bindir}/R CMD check %{packname} $ARGS
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} $ARGS
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
%{rlibdir}/%{packname}/BS3
%{rlibdir}/%{packname}/BS5
%{rlibdir}/%{packname}/highlight-styles
%dir %{rlibdir}/%{packname}/po
%lang(de) %{rlibdir}/%{packname}/po/de
%lang(dk) %{rlibdir}/%{packname}/po/dk
%lang(es) %{rlibdir}/%{packname}/po/es
%lang(fr) %{rlibdir}/%{packname}/po/fr
%lang(ko) %{rlibdir}/%{packname}/po/ko
%lang(kr) %{rlibdir}/%{packname}/po/kr
%lang(pt) %{rlibdir}/%{packname}/po/pt
%lang(tr) %{rlibdir}/%{packname}/po/tr
%lang(zh_CN) %{rlibdir}/%{packname}/po/zh_CN


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.0.6-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.0.6-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 2.0.6-1
- update to 2.0.6
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 1.6.1-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.1-1
- Update to latest version (#1876595)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.5.1-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.1-1
- Update to latest version

* Thu Mar 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-2
- Exclude Suggests for unavailable packages

* Wed Sep 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-1
- Update to latest version

* Sun Sep 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- initial package for Fedora
