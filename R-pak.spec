%global packname pak
%global packver  0.1.2.1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.1.2.1
Release:          8%{?dist}
Summary:          Another Approach to Package Installation

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# Upstream master has removed these files, so won't go upstream.
Patch0001:        0001-Skip-more-tests-if-offline.patch
# https://github.com/r-lib/pak/pull/203
Patch0002:        0002-Fix-version-of-rprojroot-dependency.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-assertthat, R-base64enc, R-callr >= 3.0.0.9002, R-cli >= 1.0.0, R-cliapp >= 0.0.0.9002, R-crayon >= 1.3.4, R-curl >= 3.2, R-desc >= 1.2.0, R-filelock >= 1.0.2, R-glue >= 1.3.0, R-jsonlite, R-lpSolve, R-pkgbuild >= 1.0.2, R-pkgcache >= 1.0.3, R-prettyunits, R-processx >= 3.2.1, R-ps >= 1.3.0, R-R6, R-rematch2, R-rprojroot >= 1.3.2, R-tibble, R-utils
# Suggests:  R-covr, R-mockery, R-pingr, R-testthat, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-assertthat
BuildRequires:    R-base64enc
BuildRequires:    R-callr >= 3.0.0.9002
BuildRequires:    R-cli >= 1.0.0
BuildRequires:    R-cliapp >= 0.0.0.9002
BuildRequires:    R-crayon >= 1.3.4
BuildRequires:    R-curl >= 3.2
BuildRequires:    R-desc >= 1.2.0
BuildRequires:    R-filelock >= 1.0.2
BuildRequires:    R-glue >= 1.3.0
BuildRequires:    R-jsonlite
BuildRequires:    R-lpSolve
BuildRequires:    R-pkgbuild >= 1.0.2
BuildRequires:    R-pkgcache >= 1.0.3
BuildRequires:    R-prettyunits
BuildRequires:    R-processx >= 3.2.1
BuildRequires:    R-ps >= 1.3.0
BuildRequires:    R-R6
BuildRequires:    R-rematch2
BuildRequires:    R-rprojroot >= 1.3.2
BuildRequires:    R-tibble
BuildRequires:    R-utils
BuildRequires:    R-covr
BuildRequires:    R-mockery
BuildRequires:    R-pingr
BuildRequires:    R-testthat
BuildRequires:    R-withr

%description
The goal of 'pak' is to make package installation faster and more reliable.
In particular, it performs all HTTP operations in parallel, so metadata
resolution and package downloads are fast. Metadata and package files are
cached on the local disk as well. 'pak' has a dependency solver, so it
finds version conflicts before performing the installation. This version of
'pak' supports CRAN, 'Bioconductor' and 'GitHub' packages as well.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1
%patch0002 -p1
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


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
%{rlibdir}/%{packname}/tools
%{rlibdir}/%{packname}/WORDLIST


%changelog
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
