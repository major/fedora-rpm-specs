%global packname remotes
%global packver  2.4.2
%global rlibdir  %{_datadir}/R/library

# Tests require the network.
%bcond_with network

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Summary:          R Package Installation from Remote Repositories

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods, R-stats, R-tools, R-utils
# Suggests:  R-brew, R-callr, R-codetools, R-curl, R-covr, R-git2r >= 0.23.0, R-knitr, R-mockery, R-pkgbuild >= 1.0.1, R-pingr, R-rmarkdown, R-rprojroot, R-testthat, R-webfakes, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-stats
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-brew
BuildRequires:    R-callr
BuildRequires:    R-codetools
BuildRequires:    R-curl
BuildRequires:    R-git2r >= 0.23.0
BuildRequires:    R-knitr
BuildRequires:    R-mockery
BuildRequires:    R-pkgbuild >= 1.0.1
BuildRequires:    R-pingr
BuildRequires:    R-rmarkdown
BuildRequires:    R-rprojroot
BuildRequires:    R-testthat
BuildRequires:    R-webfakes
BuildRequires:    R-withr

%description
Download and install R packages stored in GitHub, GitLab, Bitbucket,
Bioconductor, or plain subversion or git repositories. This package provides
the 'install_*' functions in devtools. Indeed most of the code was copied over
from devtools.


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

# FIXME: Why does this not install?
install -p %{packname}/{README,NEWS}.md %{buildroot}%{rlibdir}/%{packname}/


%check
%if %{with network}
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%else
%{_bindir}/R CMD check --ignore-vignettes %{packname} --no-tests --no-examples
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/README.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/install-github.R
%{rlibdir}/%{packname}/install-github.Rin


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.4.2-8
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.4.2-4
- Ignore vignettes

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.4.2-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 2.4.2-1
- update to 2.4.2
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 19 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4.0-3
- Correct license tag to MIT

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 2.4.0-1
- update to 2.4.0
- Rebuilt for R 4.1.0

* Sat Apr 03 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.0-1
- Update to latest version (#1945759)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.0-1
- Update to latest version

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 2.1.1-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-1
- Update to latest version

* Wed Apr 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.4-1
- Update to latest version

* Tue Apr 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.3-1
- Update to latest version

* Fri Feb 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- initial package for Fedora
