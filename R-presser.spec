%global packname presser
%global packver  1.1.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1.0
Release:          8%{?dist}
Summary:          Lightweight Web Server for Testing

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-stats, R-tools, R-utils
# Suggests:  R-callr, R-curl, R-glue, R-jsonlite, R-testthat, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-stats
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-callr
BuildRequires:    R-curl
BuildRequires:    R-glue
BuildRequires:    R-jsonlite
BuildRequires:    R-testthat
BuildRequires:    R-withr

%description
Create a web app that makes it easier to test web clients without using the
internet. It includes a web app framework with path matching and parameters
and templates. Can parse various 'HTTP' request bodies. Can send 'JSON'
data or files from the disk. Includes a web app that implements the
<https://httpbin.org> web service.


%prep
%setup -q -c -n %{packname}


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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/credits
%{rlibdir}/%{packname}/examples


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Tom Callaway <spot@fedoraproject.org> - 1.1.0-7
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 1.1.0-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- initial package for Fedora
