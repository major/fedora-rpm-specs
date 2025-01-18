# R-thematic not available
%bcond_with suggests

%global packname bslib
%global packver  0.4.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Summary:          Custom Bootstrap Sass Themes for shiny and rmarkdown

# Main: MIT
# Bootstrap libraries:
# * bootstrap: MIT
# * bootstrap-sass: MIT
# * bootstrap-colorpicker: MIT
# * bootstrap-accessibility-plugin: BSD
# * bootswatch: MIT
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:          LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-grDevices, R-htmltools >= 0.5.2, R-jsonlite, R-sass >= 0.4.0, R-jquerylib >= 0.1.3, R-rlang, R-cachem, R-memoise
# Suggests:  R-shiny >= 1.6.0, R-rmarkdown >= 2.7, R-thematic, R-knitr, R-testthat, R-withr, R-rappdirs, R-curl, R-magrittr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-grDevices
BuildRequires:    R-htmltools >= 0.5.2
BuildRequires:    R-jsonlite
BuildRequires:    R-sass >= 0.4.0
BuildRequires:    R-jquerylib >= 0.1.3
BuildRequires:    R-rlang
BuildRequires:    R-cachem
BuildRequires:    R-memoise
# Suggests
%if %{with suggests}
BuildRequires:    R-shiny >= 1.6.0
BuildRequires:    R-rmarkdown >= 2.7
BuildRequires:    R-thematic
BuildRequires:    R-knitr
BuildRequires:    R-testthat
BuildRequires:    R-withr
BuildRequires:    R-rappdirs
BuildRequires:    R-curl
BuildRequires:    R-magrittr
%endif

%description
Simplifies custom CSS styling of both shiny and rmarkdown via Bootstrap Sass.
Supports both Bootstrap 3 and 4 as well as their various Bootswatch themes. An
interactive widget is also provided for previewing themes in real time.


%prep
%setup -q -c -n %{packname}

# Fix executable bits.
chmod -x %{packname}/inst/lib/*/dist/*/_variables.scss


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

install -p %{packname}/LICENSE.note %{buildroot}%{rlibdir}/%{packname}/


%check
%if %{with suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples --no-vignettes --no-tests
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%license %{rlibdir}/%{packname}/LICENSE.note
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/bs3compat
%{rlibdir}/%{packname}/css-precompiled
%{rlibdir}/%{packname}/custom
%{rlibdir}/%{packname}/fonts
%dir %{rlibdir}/%{packname}/lib
%dir %{rlibdir}/%{packname}/lib/bs3
%doc %{rlibdir}/%{packname}/lib/bs3/CHANGELOG.md
%license %{rlibdir}/%{packname}/lib/bs3/LICENSE
%doc %{rlibdir}/%{packname}/lib/bs3/README.md
%{rlibdir}/%{packname}/lib/bs3/assets
%{rlibdir}/%{packname}/lib/bs3/eyeglass-exports.js
%{rlibdir}/%{packname}/lib/bs3/package.json
%dir %{rlibdir}/%{packname}/lib/bs4
%license %{rlibdir}/%{packname}/lib/bs4/LICENSE
%doc %{rlibdir}/%{packname}/lib/bs4/README.md
%{rlibdir}/%{packname}/lib/bs4/dist/
%{rlibdir}/%{packname}/lib/bs4/package.json
%{rlibdir}/%{packname}/lib/bs4/scss/
%dir %{rlibdir}/%{packname}/lib/bs5
%license %{rlibdir}/%{packname}/lib/bs5/LICENSE
%doc %{rlibdir}/%{packname}/lib/bs5/README.md
%{rlibdir}/%{packname}/lib/bs5/dist/
%{rlibdir}/%{packname}/lib/bs5/package.json
%{rlibdir}/%{packname}/lib/bs5/scss/
%dir %{rlibdir}/%{packname}/lib/bsw3
%doc %{rlibdir}/%{packname}/lib/bsw3/README.md
%license %{rlibdir}/%{packname}/lib/bsw3/LICENSE
%{rlibdir}/%{packname}/lib/bsw3/cerulean/
%{rlibdir}/%{packname}/lib/bsw3/cosmo/
%{rlibdir}/%{packname}/lib/bsw3/cyborg/
%{rlibdir}/%{packname}/lib/bsw3/darkly/
%{rlibdir}/%{packname}/lib/bsw3/flatly/
%{rlibdir}/%{packname}/lib/bsw3/journal/
%{rlibdir}/%{packname}/lib/bsw3/lumen/
%{rlibdir}/%{packname}/lib/bsw3/paper/
%{rlibdir}/%{packname}/lib/bsw3/readable/
%{rlibdir}/%{packname}/lib/bsw3/sandstone/
%{rlibdir}/%{packname}/lib/bsw3/simplex/
%{rlibdir}/%{packname}/lib/bsw3/slate/
%{rlibdir}/%{packname}/lib/bsw3/spacelab/
%{rlibdir}/%{packname}/lib/bsw3/superhero/
%{rlibdir}/%{packname}/lib/bsw3/united/
%{rlibdir}/%{packname}/lib/bsw3/yeti/
%{rlibdir}/%{packname}/lib/bsw3/package.json
%dir %{rlibdir}/%{packname}/lib/bsw4
%doc %{rlibdir}/%{packname}/lib/bsw4/README.md
%license %{rlibdir}/%{packname}/lib/bsw4/LICENSE
%{rlibdir}/%{packname}/lib/bsw4/dist/
%{rlibdir}/%{packname}/lib/bsw4/package.json
%dir %{rlibdir}/%{packname}/lib/bsw5
%doc %{rlibdir}/%{packname}/lib/bsw5/README.md
%license %{rlibdir}/%{packname}/lib/bsw5/LICENSE
%{rlibdir}/%{packname}/lib/bsw5/dist/
%{rlibdir}/%{packname}/lib/bsw5/package.json
%dir %{rlibdir}/%{packname}/lib/bs-a11y-p
%license %{rlibdir}/%{packname}/lib/bs-a11y-p/LICENSE.md
%{rlibdir}/%{packname}/lib/bs-a11y-p/package.json
%{rlibdir}/%{packname}/lib/bs-a11y-p/plugins/
%{rlibdir}/%{packname}/lib/bs-a11y-p/src/
%dir %{rlibdir}/%{packname}/lib/bs-colorpicker
%doc %{rlibdir}/%{packname}/lib/bs-colorpicker/README.md
%license %{rlibdir}/%{packname}/lib/bs-colorpicker/LICENSE
%{rlibdir}/%{packname}/lib/bs-colorpicker/css/
%{rlibdir}/%{packname}/lib/bs-colorpicker/js/
%{rlibdir}/%{packname}/lib/bs-colorpicker/package.json
%{rlibdir}/%{packname}/nav-spacer/
%{rlibdir}/%{packname}/package.json
%{rlibdir}/%{packname}/rmarkdown/
%{rlibdir}/%{packname}/sass-utils
%{rlibdir}/%{packname}/themer-demo
%{rlibdir}/%{packname}/themer

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.0-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.4.0-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.4.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Tom Callaway <spot@fedoraproject.org> - 0.4.0-1
- update to 0.4.0
- rebuild for R 4.2.1
- bootstrap on

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-3
- Rebuild for R 4.1

* Sun May 09 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-2
- Add explicit license breakdown

* Sun Apr 25 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-1
- initial package for Fedora
