%global packname gargle
%global packver  1.4.0
%global rlibdir  %{_datadir}/R/library

%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          8%{?dist}
Summary:          Utilities for Working with Google APIs

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli >= 3.0.0, R-fs >= 1.3.1, R-glue >= 1.3.0, R-httr >= 1.4.0, R-jsonlite, R-rappdirs, R-rlang >= 1.0.0, R-rstudioapi, R-stats, R-utils, R-withr
# Suggests:  R-aws.ec2metadata, R-aws.signature, R-covr, R-httpuv, R-knitr, R-mockr, R-rmarkdown, R-sodium, R-spelling, R-testthat >= 3.1.2
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli >= 3.0.1
BuildRequires:    R-fs >= 1.3.1
BuildRequires:    R-glue >= 1.3.0
BuildRequires:    R-httr >= 1.4.5
BuildRequires:    R-jsonlite
BuildRequires:    R-lifecycle
BuildRequires:    R-openssl
BuildRequires:    R-rappdirs
BuildRequires:    R-rlang >= 1.0.0
BuildRequires:    R-stats
BuildRequires:    R-utils
BuildRequires:    R-withr
# Suggests
%if %{with_suggests}
BuildRequires:    R-aws.ec2metadata
BuildRequires:    R-aws.signature
BuildRequires:    R-httpuv
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-sodium
BuildRequires:    R-spelling
BuildRequires:    R-testthat >= 3.1.7
%endif

%description
Provides utilities for working with Google APIs
<https://developers.google.com/apis-explorer>.  This includes functions and
classes for handling common credential types and for preparing, executing, and
processing HTTP requests.


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
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples --no-tests
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
%{rlibdir}/%{packname}/discovery-doc-ingest
%{rlibdir}/%{packname}/pseudo-oob
%{rlibdir}/%{packname}/secret
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.0-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.0-2
- R-maint-sig mass rebuild

* Wed Apr 19 2023 Tom Callaway <spot@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  8 2022 Tom Callaway <spot@fedoraproject.org> - 1.2.1-1
- update to 1.2.1

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 1.2.0-1
- update to 1.2.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.1.0-2
- Rebuilt for R 4.1.0

* Sat Apr 03 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version (#1945859)

* Fri Mar 05 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version (#1934743)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.5.0-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-1
- Update to latest version

* Mon Aug 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- initial package for Fedora
