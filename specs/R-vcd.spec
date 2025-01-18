%bcond_without check

%global packname vcd
%global ver 1.4
%global packrel 13

%global _description %{expand:
Visualization techniques, data sets, summary and inference procedures aimed
particularly at categorical data. Special emphasis is given to highly
extensible grid graphics. The package was package was originally inspired
by the book "Visualizing Categorical Data" by Michael Friendly and is now
the main support package for a new book, "Discrete Data Analysis with R"
by Michael Friendly and David Meyer (2015).}

Name:             R-%{packname}
Version:          %{ver}.%{packrel}
Release:          2%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:          GPL-2.0-only
URL:              https://cran.r-project.org/web/packages/vcd/index.html
Summary:          Visualizing categorical data

BuildRequires:    R-devel, tex(latex)
BuildRequires:    R-colorspace
BuildRequires:    R-lmtest

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
%if %{with check}
export _R_CHECK_FORCE_SUGGESTS_=0 LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes --no-tests %{packname}
%endif

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%doc %{_datadir}/R/library/%{packname}/CITATION
%doc %{_datadir}/R/library/%{packname}/NEWS.Rd
%doc %{_datadir}/R/library/%{packname}/doc
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/data
%{_datadir}/R/library/%{packname}/demo


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 20 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.4.13-1
- Update to 1.4-13

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.12-4
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.12-2
- R-maint-sig mass rebuild

* Fri Feb 23 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.4.12-1
- Update to 1.4-12

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.11-2
- R-maint-sig mass rebuild

* Wed Mar 15 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.4.11-1
- Update to 1.4-11

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 1.4.10-1
- update to 1.4-10
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.4.8-2
- Rebuilt for R 4.1.0

* Sun May 2 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.4.8-1
- Initial package
