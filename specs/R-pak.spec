%global packname pak
%global packver  0.5.1
%global rlibdir  %{_datadir}/R/library
%bcond_with suggests

Name:             R-%{packname}
Version:          0.5.1
Release:          8%{?dist}
Summary:          Another Approach to Package Installation

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:          GPL-3.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-tools, R-utils
# Suggests:  R-callr >= 3.7.0, R-cli >= 3.2.0, R-covr, R-curl >= 4.3.2, R-desc >= 1.4.1, R-digest, R-distro, R-filelock >= 1.0.2, R-gitcreds, R-glue >= 1.6.2, R-jsonlite, R-mockery, R-pingr, R-pkgcache >= 2.0.4, R-pkgdepends >= 0.4.0, R-pkgsearch >= 3.1.0, R-prettyunits, R-processx >= 3.8.1, R-ps >= 1.6.0, R-rprojroot >= 2.0.2, R-rstudioapi, R-testthat, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    tex(inconsolata.sty)
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-testthat
%if %{with suggests}
BuildRequires:    R-callr >= 3.7.0
BuildRequires:    R-cli >= 3.2.0
BuildRequires:    R-covr
BuildRequires:    R-curl >= 4.3.2
BuildRequires:    R-desc >= 1.4.1
BuildRequires:    R-digest
BuildRequires:    R-distro
BuildRequires:    R-filelock >= 1.0.2
BuildRequires:    R-gitcreds
BuildRequires:    R-glue >= 1.6.2
BuildRequires:    R-jsonlite
BuildRequires:    R-mockery
BuildRequires:    R-pingr
BuildRequires:    R-pkgcache >= 2.0.4
BuildRequires:    R-pkgdepends >= 0.4.0
BuildRequires:    R-pkgsearch >= 3.1.0
BuildRequires:    R-prettyunits
BuildRequires:    R-processx >= 3.8.1
BuildRequires:    R-ps >= 1.6.0
BuildRequires:    R-rprojroot >= 2.0.2
BuildRequires:    R-rstudioapi
BuildRequires:    R-withr
%endif

%description
The goal of 'pak' is to make package installation faster and more reliable.
In particular, it performs all HTTP operations in parallel, so metadata
resolution and package downloads are fast. Metadata and package files are
cached on the local disk as well. 'pak' has a dependency solver, so it
finds version conflicts before performing the installation. This version of
'pak' supports CRAN, 'Bioconductor' and 'GitHub' packages as well.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes
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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/header.md
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/library
%{rlibdir}/%{packname}/tools
%{rlibdir}/%{packname}/WORDLIST

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.1-7
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.5.1-5
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Tom Callaway <spot@fedoraproject.org> - 0.5.1-1
- update to 0.5.1
- conditionalize suggests entirely

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.1.2.1-9
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 04 2022 Iñaki Úcar <iucar@fedoraproject.org> - 0.1.2.1-7
- R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 0.1.2.1-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.2.1-1
- Update to latest version (#1899792)

* Wed Sep 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.2-2
- Fix runtime dependency version

* Wed Sep 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.2-1
- initial package for Fedora
