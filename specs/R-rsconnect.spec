%bcond_with bootstrap

%global packname rsconnect
%global packver  0.8.28
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((plumber)\\)

# Not yet available.
%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Summary:          Deployment Interface for R Markdown Documents and Shiny Applications

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:          GPL-2.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-curl, R-digest, R-jsonlite, R-openssl >= 2.0.0, R-packrat >= 0.6, R-rstudioapi >= 0.5, R-tools, R-yaml >= 2.1.5
# Suggests:  R-MASS, R-RCurl, R-callr, R-httpuv, R-knitr, R-plumber >= 0.3.2, R-reticulate, R-rmarkdown >= 1.1, R-shiny, R-sourcetools, R-testthat, R-xtable
# LinkingTo:
# Enhances:

BuildArch:        noarch

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-curl
BuildRequires:    R-digest
BuildRequires:    R-jsonlite
BuildRequires:    R-openssl >= 2.0.0
BuildRequires:    R-packrat >= 0.6
BuildRequires:    R-rstudioapi >= 0.5
BuildRequires:    R-tools
BuildRequires:    R-yaml >= 2.1.5
%if %{without bootstrap}
BuildRequires:    R-MASS
BuildRequires:    R-RCurl
BuildRequires:    R-callr
BuildRequires:    R-httpuv
BuildRequires:    R-knitr
%if %{with_suggests}
BuildRequires:    R-plumber >= 0.3.2
%endif
BuildRequires:    R-reticulate
BuildRequires:    R-rmarkdown >= 1.1
BuildRequires:    R-shiny
BuildRequires:    R-sourcetools
BuildRequires:    R-testthat
BuildRequires:    R-xtable
%endif

%description
Programmatic deployment interface for 'RPubs', 'shinyapps.io', and 'RStudio
Connect'. Supported content types include R Markdown documents, Shiny
applications, Plumber APIs, plots, and static web content.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Remove bundled fallback cert store.
rm inst/cert/cacert.pem
sed -i -e '/cacert.pem/d' MD5

# Remove extra shebang.
sed -i -e '1d' inst/resources/environment.py
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/cert
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/resources


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.28-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.8.28-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.8.28-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Tom Callaway <spot@fedoraproject.org> - 0.8.28-1
- update to 0.8.28

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 0.8.27-1
- update to 0.8.27
- rebuild for R 4.2.1
- bootstrap on

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 0.8.18-2
- bootstrap off

* Fri Jun 11 2021 Tom Callaway <spot@fedoraproject.org> - 0.8.18-1
- Update to 0.8.18
- Rebuilt for R 4.1.0

* Fri Apr 09 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.17-1
- Update to latest version (#1947760)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.8.16-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.16-1
- Update to latest version

* Sun Aug 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.15-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.13-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.13-1
- initial package for Fedora
