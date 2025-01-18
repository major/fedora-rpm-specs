%global packname snow
%global packver 0.4
%global packrel 4

%global __suggests_exclude ^R\\((Rmpi)\\)

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          19%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{packver}-%{packrel}.tar.gz
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Summary:          Simple Network of Workstations
BuildRequires:    R-devel >= 3.0.0, tex(latex), R-utils
# Suggests
BuildRequires:    R-rlecuyer
BuildArch:        noarch

%description
Support for simple parallel computing in R.

%prep
%setup -q -c -n %{packname}

chmod -x snow/inst/RMPInode.R

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_datadir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/R.css

# do not need on Linux
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/%{packname}/*.bat

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/RMPI*
%{_datadir}/R/library/%{packname}/RSOCK*
%{_datadir}/R/library/%{packname}/RunSnow*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.4-18
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.4.4-16
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.4.4-12
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 0.4.4-1
- update to 0.4-4
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 0.4.3-7
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.4.3-4
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.3-2
- Exclude Suggests for unavailable packages

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 0.4.3-1
- 0.4-3

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.2-8
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Tom Callaway <spot@fedoraproject.org> - 0.4.2-4
- rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 0.4.2-1
- initial package
