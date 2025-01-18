%global packname crosstalk
%global packver  1.2.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Summary:          Inter-Widget Interactivity for HTML Widgets

# Mostly MIT, selectize.js is ASL 2.0
# Automatically converted from old format: MIT and ASL 2.0 - review is highly recommended.
License:          LicenseRef-Callaway-MIT AND Apache-2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# Remove extra glyphicons references; Fedora only;
# Patch0001:        0001-Remove-non-ttf-font-references.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-htmltools >= 0.3.6, R-jsonlite, R-lazyeval, R-R6
# Suggests:  R-shiny, R-ggplot2, R-testthat >= 2.1.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-htmltools >= 0.3.6
BuildRequires:    R-jsonlite
BuildRequires:    R-lazyeval
BuildRequires:    R-R6
BuildRequires:    R-shiny
BuildRequires:    R-ggplot2
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-sass
BuildRequires:    R-bslib

# MIT; inst/lib/bootstrap/
# https://github.com/twbs/bootstrap/releases/tag/v3.4.1
Provides:         bundled(xstatic-bootstrap-common) = 3.4.1
# BuildRequires:    glyphicons-halflings-fonts
# Requires:         glyphicons-halflings-fonts

# MIT; inst/lib/ionrangeslider
Provides:         bundled(js-IonDen-ionrangeslider) = 2.1.2

# MIT; inst/lib/jquery
Provides:         bundled(js-jquery) = 3.5.1

# ASL 2.0; inst/lib/selectize
Provides:         bundled(js-brianreavis-selectize) = 0.12.1

# MIT; inst/lib/strftime
Provides:         bundled(js-samsonjs-strftime) = 0.9.2

%description
Provides building blocks for allowing HTML widgets to communicate with each
other, with Shiny or without (i.e. static .html files). Currently supports
linked brushing and filtering.


%prep
%setup -q -c -n %{packname}

# pushd %{packname}
# %%patch0001 -p1
# popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# pushd %{buildroot}%{rlibdir}/%{packname}
# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
# ln -sf %{_datadir}/fonts/glyphicons-halflings/glyphicons-halflings-regular.ttf \
#     lib/bootstrap/fonts/glyphicons-halflings-regular.ttf
# popd


%check
%{_bindir}/R CMD check %{packname}


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
%{rlibdir}/%{packname}/lib
%{rlibdir}/%{packname}/www


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.0-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 1.2.0-1
- update to 1.2.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.1.1-2
- Rebuilt for R 4.1.0

* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- Update to latest version (#1915291)
- Re-bundle jQuery

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0.1-1
- initial package for Fedora
