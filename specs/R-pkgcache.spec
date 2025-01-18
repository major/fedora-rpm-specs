%global packname pkgcache
%global packver  2.1.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          8%{?dist}
Summary:          Cache 'CRAN'-Like Metadata and R Packages

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-callr >= 2.0.4.9000, R-cli >= 3.2.0, R-curl >= 3.2, R-filelock, R-jsonlite, R-prettyunits, R-processx >= 3.3.0.9001, R-R6, R-rappdirs, R-tools, R-utils
# Suggests:  R-covr, R-debugme, R-desc, R-fs, R-mockery, R-pillar, R-pingr, R-rprojroot, R-sessioninfo, R-spelling, R-testthat >= 3.0.0, R-webfakes >= 1.1.5, R-withr, R-zip
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-callr >= 2.0.4.9000
BuildRequires:    R-cli >= 3.2.0
BuildRequires:    R-curl >= 3.2
BuildRequires:    R-filelock
BuildRequires:    R-jsonlite
BuildRequires:    R-prettyunits
BuildRequires:    R-processx >= 3.3.0.9001
BuildRequires:    R-R6
BuildRequires:    R-rappdirs
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-covr
BuildRequires:    R-debugme
BuildRequires:    R-desc
BuildRequires:    R-fs
BuildRequires:    R-mockery
BuildRequires:    R-pillar
BuildRequires:    R-pingr
BuildRequires:    R-rprojroot
BuildRequires:    R-sessioninfo
BuildRequires:    R-spelling
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-webfakes >= 1.1.5
BuildRequires:    R-withr
BuildRequires:    R-zip

%description
Metadata and package cache for CRAN-like repositories. This is a utility
package to be used by package management tools that want to take advantage
of caching.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
# Tries to access the network
%if 0
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
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/fixtures

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.1.0-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.1.0-2
- R-maint-sig mass rebuild

* Wed Apr 19 2023 Tom Callaway <spot@fedoraproject.org> - 2.1.0-1
- update to 2.1.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  8 2022 Tom Callaway <spot@fedoraproject.org> - 2.0.2-1
- update to 2.0.2

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 2.0.1-1
- update to 2.0.1
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.2.2-1
- update to 1.2.2
- Rebuilt for R 4.1.0
- disable check

* Sun Apr 25 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-1
- Update to latest version (#1949433)

* Tue Mar 02 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version (#1933854)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 11 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- Update to latest version (#1887160)

* Wed Sep 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-2
- Fix tests when offline

* Sat Sep 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- initial package for Fedora
