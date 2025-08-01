%global packname R6
%global packver 2.6.1

%global __suggests_exclude ^R\\((pryr)\\)

Name:             R-%{packname}
Version:          %{packver}
Release:          4%{?dist}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
License:          MIT
URL:              http://cran.r-project.org/web/packages/R6/index.html
Summary:          Classes with Reference Semantics
BuildRequires:    R-devel >= 3.0.0, tetex-latex
# For tests
# BuildRequires:  R-testthat
# Not in fedora yet
# BuildRequires:  R-pryr
# These are in, but with tests disabled, no reason to pull them into the BuildRoot
# BuildRequires:  R-knitr
# BuildRequires:  R-microbenchmark
# BuildRequires:  R-ggplot2
# BuildRequires:  R-scales
BuildArch:        noarch

%description
The R6 package allows the creation of classes with reference semantics,
similar to R's built-in reference classes. Compared to reference classes,
R6 classes are simpler and lighter-weight, and they are not built on S4
classes so they do not require the methods package. These classes allow
public and private members, and they support inheritance, even when the
classes are defined in different packages.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_datadir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/R.css

%check
# Can't run this yet, needs lots of deps
%if 0
%{_bindir}/R CMD check %%{packname}
%endif

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/LICENSE
%doc %{_datadir}/R/library/%{packname}/html
%doc %{_datadir}/R/library/%{packname}/NEWS.md
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/help

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Apr 18 2025 Iñaki Úcar <iucar@fedoraproject.org> - 2.6.1-3
- R-maint-sig mass rebuild

* Fri Apr 18 2025 Iñaki Úcar <iucar@fedoraproject.org> - 2.6.1-2
- R-maint-sig mass rebuild

* Fri Feb 21 2025 Tom Callaway <spot@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.5.1-10
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.5.1-6
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 2.5.1-4
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 20 2021 Tom Callaway <spot@fedoraproject.org> - 2.5.1-1
- update to 2.5.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 2.5.0-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Tom Callaway <spot@fedoraproject.org> - 2.5.0-1
- update to 2.5.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 2.4.1-4
- Rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4.1-2
- Exclude Suggests for unavailable packages

* Wed Nov 13 2019 Tom Callaway <spot@fedoraproject.org> - 2.4.1-1
- update to 2.4.1

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 2.4.0-1
- update to 2.4.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.2-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Tom Callaway <spot@fedoraproject.org> - 2.2.2-1
- update to 2.2.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Tom Callaway <spot@fedoraproject.org> - 2.2.1-1
- initial package
