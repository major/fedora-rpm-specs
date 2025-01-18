%bcond_with bootstrap

%global packname rstudioapi
%global packver  0.13
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.13
Release:          17%{?dist}
Summary:          Safely Access the RStudio API

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-testthat, R-knitr, R-rmarkdown, R-clipr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
%if %{without bootstrap}
BuildRequires:    R-testthat
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-clipr
%endif

%description
Access the RStudio API (if available) and provide informative error
messages when it's not.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
%{_bindir}/R CMD check --ignore-vignettes %{packname}
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
%{rlibdir}/%{packname}/resources


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.13-15
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 28 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.13-11
- Ignore vignettes

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.13-10
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 0.13-8
- rebuild for R 4.2.1
- bootstrap

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 0.13-4
- bootstrap off

* Tue Jun  8 2021 Tom Callaway <spot@fedoraproject.org> - 0.13-3
- Rebuilt for R 4.1.0
- bootstrap

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.13-1
- Update to latest version (#1896605)

* Wed Nov 11 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12-1
- Update to latest version (#1896605)
- Rename check condition to bootstrap and enable tests

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 0.11-2
- conditionalize check to break testthat loop
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.11-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.10-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.10-1
- Update to latest version

* Fri Feb 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.0-1
- Update to latest version
- Enable documentation

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7-1
- initial package for Fedora
