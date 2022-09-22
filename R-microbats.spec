%global packname microbats
%global ver 0.1
%global packrel 1

%global _description %{expand:
A nature-inspired metaheuristic algorithm based on the echolocation behavior
of microbats that uses frequency tuning to optimize problems in both
continuous and discrete dimensions. This R package makes it easy to
implement the standard bat algorithm on any user-supplied function.
The algorithm was first developed by Xin-She Yang in 2010 
(<doi:10.1007/978-3-642-12538-6_6>, <doi:10.1109/CINTI.2014.7028669>.}

Name:             R-%{packname}
Version:          %{ver}.%{packrel}
Release:          6%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
License:          GPLv2
URL:              https://cran.r-project.org/web/packages/microbats/index.html
Summary:          An implementation of Bat Algorithm in R
BuildRequires:    R-devel, tex(latex)

BuildArch:        noarch

Requires:         R-core

%description %_description

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_datadir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_datadir}/R/library/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/help

%changelog
* Fri Aug 19 2022 Tom Callaway <spot@fedoraproject.org> - 0.1.1-6
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 0.1.1-2
- Rebuilt for R 4.1.0

* Tue Apr 27 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.1-1
- Initial package
