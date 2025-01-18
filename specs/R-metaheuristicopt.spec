%bcond_without check

%global packname metaheuristicOpt
%global rlibdir  %{_datadir}/R/library
%global ver 2.0.0

Name:             R-metaheuristicopt
Version:          %{ver}
Release:          9%{?dist}
License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source:           %{url}&version=%{ver}#/%{packname}_%{ver}.tar.gz
Summary:          Metaheuristics for Optimization

BuildRequires:    R-devel, tex(latex)

BuildArch:        noarch

%description
An implementation of metaheuristic algorithms
for continuous optimization. Currently, the
package contains the implementations of 21 algorithms.

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
%license %{rlibdir}/%{packname}/LICENSE
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.0.0-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.0.0-3
- R-maint-sig mass rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.0.0-2
- R-maint-sig mass rebuild

* Sat Apr 8 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-1
- Initial package
