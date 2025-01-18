%bcond_without check

%global packname niarules
%global rlibdir  %{_datadir}/R/library
%global ver 0.1.0

Name:             R-%{packname}
Version:          %{ver}
Release:          4%{?dist}
License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source:           %{url}&version=%{version}#/%{packname}_%{ver}.tar.gz
Summary:          Numerical Association Rule Mining using Nature-Inspired Algorithms

BuildRequires:    R-devel, tex(latex)
BuildRequires:    tex(inconsolata.sty)
Requires:         R-core

%if %{with check}
BuildRequires:    R-testthat
%endif

BuildArch:        noarch

%description
Framework is devoted to mining numerical association rules
through the utilization of nature-inspired algorithms for
optimization.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%if %{with check}
export LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%doc %{rlibdir}/%{packname}/CODE_OF_CONDUCT.md
%doc %{rlibdir}/%{packname}/CONTRIBUTING.md
%doc %{rlibdir}/%{packname}/examples/
%doc %{rlibdir}/%{packname}/extdata/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.1.0-2
- R-maint-sig mass rebuild

* Thu Mar 28 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.0-1
- Initial package
