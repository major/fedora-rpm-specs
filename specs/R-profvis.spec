%bcond_with bootstrap

%global packname profvis
%global packver  0.3.7
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          15%{?dist}
Summary:          Interactive Visualizations for Profiling R Code

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:          GPL-3.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-htmlwidgets >= 0.3.2, R-stringr
# Suggests:  R-knitr, R-ggplot2, R-rmarkdown, R-testthat, R-devtools, R-shiny, R-htmltools
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-htmlwidgets >= 0.3.2
BuildRequires:    R-stringr
%if %{without bootstrap}
BuildRequires:    R-knitr
BuildRequires:    R-ggplot2
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
BuildRequires:    R-devtools
BuildRequires:    R-shiny
BuildRequires:    R-htmltools
%endif

Provides:         bundled(js-highlight) = 6.2.0
Provides:         bundled(js-jquery1) = 1.12.4
Provides:         bundled(js-d3) = 3.5.6

%description
Interactive visualizations for profiling R code.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
%{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%dir %{rlibdir}/%{packname}/htmlwidgets
%license %{rlibdir}/%{packname}/htmlwidgets/lib/d3/LICENSE
%license %{rlibdir}/%{packname}/htmlwidgets/lib/highlight/LICENSE
%dir %{rlibdir}/%{packname}/htmlwidgets/lib/d3
%{rlibdir}/%{packname}/htmlwidgets/lib/d3/d3.min.js
%dir %{rlibdir}/%{packname}/htmlwidgets/lib/highlight
%{rlibdir}/%{packname}/htmlwidgets/lib/highlight/default.css
%{rlibdir}/%{packname}/htmlwidgets/lib/highlight/highlight.js
%{rlibdir}/%{packname}/htmlwidgets/lib/highlight/textmate.css
%{rlibdir}/%{packname}/htmlwidgets/lib/jquery/
%{rlibdir}/%{packname}/htmlwidgets/lib/profvis/
%{rlibdir}/%{packname}/htmlwidgets/profvis.js
%{rlibdir}/%{packname}/htmlwidgets/profvis.yaml
%{rlibdir}/%{packname}/shinymodule


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.7-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.7-12
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.7-8
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 0.3.7-6
- bootstrap on
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 0.3.7-2
- bootstrap off

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 0.3.7-1
- update to 0.3.7
- bootstrap
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.6-6
- Re-bundle js-jquery1, fixes rhbz#1866721

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.6-3
- rebuild for R 4

* Sun Mar 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.6-2
- Fix link to jQuery

* Mon Mar 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.6-1
- initial package for Fedora
