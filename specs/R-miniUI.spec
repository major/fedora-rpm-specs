%global packname  miniUI
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.1.1.1
Release:          24%{?dist}
Summary:          Shiny UI Widgets for Small Screens

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:          GPL-3.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-shiny >= 0.13, R-htmltools >= 0.3, R-utils
# Suggests:
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-shiny >= 0.13
BuildRequires:    R-htmltools >= 0.3
BuildRequires:    R-utils

%description
Provides UI widget and layout functions for writing Shiny apps that work well
on small screens.


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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/www


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Apr 18 2025 Iñaki Úcar <iucar@fedoraproject.org> - 0.1.1.1-23
- R-maint-sig mass rebuild

* Fri Apr 18 2025 Iñaki Úcar <iucar@fedoraproject.org> - 0.1.1.1-22
- R-maint-sig mass rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.1.1-20
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.1.1.1-18
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.1.1.1-14
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 0.1.1.1-12
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 0.1.1.1-8
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.1.1.1-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1.1-1
- initial package for Fedora
