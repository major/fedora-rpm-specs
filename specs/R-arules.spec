%bcond_with check

%global packname arules
%global ver 1.7
%global packrel 9
%global rlibdir %{_libdir}/R/library

%global _description %{expand:
Provides the infrastructure for representing, manipulating and analyzing 
transaction data and patterns (frequent itemsets and association rules). 
Also provides C implementations of the association mining algorithms 
Apriori and Eclat. Hahsler, Gruen and Hornik (2005) 
<doi:10.18637/jss.v014.i15>.}

Name:             R-%{packname}
Version:          1.7.9
Release:          2%{?dist}
Summary:          Mining Association Rules and Frequent Itemsets

License:          GPL-3.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          %{url}&version=%{ver}-%{packrel}#/%{packname}_%{ver}-%{packrel}.tar.gz
Source1:          https://github.com/mhahsler/arules/raw/master/LICENSE

BuildRequires:    R-devel
BuildRequires:    R-generics >= 0.1.3
BuildRequires:    tex(latex)
%if %{with check}
BuildRequires:    R-XML
BuildRequires:    R-testthat >= 3.0.0
%endif
BuildRequires:    gcc-c++

%description %_description

%prep
%setup -q -c -n %{packname}
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *so)
rm -f %{buildroot}%{rlibdir}/R.css

# we skip only examples (one example suggests pmml which is missing)
%check
%if %{with check}
export _R_CHECK_FORCE_SUGGESTS_=0 LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes --no-examples %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/CITATION
%license LICENSE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/libs

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 17 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.7.9-1
- Update to 1.7.9

* Wed Oct 16 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.7.8-1
- Update to 1.7.8

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.7.7-4
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 4 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.7.7-1
- Update to 1.7.7

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.7.6-2
- R-maint-sig mass rebuild

* Fri Apr 7 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.7.6-1
- Update to 1.7.6

* Wed Mar 15 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.7.5-1
- Update to 1.7.5

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 01 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.7.4-1
- Update to 1.7.4 + rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 7 2021 Tom Callaway <spot@fedoraproject.org> - 1.6.8-1
- update to 1.6.8
- rebuild for R 4.1.0

* Mon Apr 5 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.6.7-2
- New version

* Wed Mar 17 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.6.6-2
- Added LICENSE from upstream's repo

* Tue Mar 16 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.6.6-1
- Enable tests

* Thu Feb 18 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.6.6-1
- Initial package creation
