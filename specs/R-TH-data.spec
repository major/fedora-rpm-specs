%global packname TH.data
%global packver 1.1
%global packrel 2

%global with_check 0

# Cannot use . in name
Name:             R-TH-data
Version:          %{packver}.%{packrel}
Release:          8%{?dist}
Summary:          Data for other R packages

License:          GPL-3.0-only
URL:              https://CRAN.R-project.org/package=TH.data
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrel}.tar.gz

Requires:         R-core
Suggests:         R-gdata
Suggests:         R-plyr
Suggests:         R-dplyr

BuildRequires:    R-devel
BuildRequires:    tex(latex), tex(upquote.sty)
BuildRequires:    R-survival
BuildRequires:    R-MASS
# required for check (R-dplyr is only available in Fedora 30+)
%if 0%{?fedora} >= 30 && %{with_check}
BuildRequires:    R-gdata
BuildRequires:    R-plyr
BuildRequires:    R-dplyr
%endif
BuildArch:        noarch

%description
Data for other R packages.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_datadir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/R.css


%check
%if 0%{?fedora} >= 30 && %{with_check}
%{_bindir}/R CMD check %{packname}
%else
#We have to use --no-install because we don't have all of the suggested dependencies
%{_bindir}/R CMD check --no-install %{packname}
%endif


%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/data/
%{_datadir}/R/library/%{packname}/doc/
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/rda/
%{_datadir}/R/library/%{packname}/PSGLMM_MEE/
%{_datadir}/R/library/%{packname}/demo/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.2-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.2-2
- R-maint-sig mass rebuild

* Wed Apr 19 2023 Tom Callaway <spot@fedoraproject.org> - 1.1.2-1
- update to 1.1-2
- correct license tag to SPDX syntax

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.1.1-1
- update to 1.1-1
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 1.0.10-8
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.0.10-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 José Matos <jamatos@fedoraproject.org> - 1.0.10-2
- Take advantage that all the Suggests packages are available and do the full tests (F-30+)

* Sun Apr 14 2019 José Matos <jamatos@fedoraproject.org> - 1.0.10-1
- update to 1.0.10
- add Suggests: as defined in the DESCRIPTION

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep  1 2018 José Matos <jamatos@fedoraproject.org> - 1.0.9-1
- update to 1.0-9
- remove buildroot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul  1 2018 José Matos <jamatos@fedoraproject.org> - 1.0.6-6
- In the check stage pass --no-install since we do not have all the
  recommended dependencies
- Fix files list

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 21 2015 José Matos <jamatos@fedoraproject.org> - 1.0.6-1
- Update to 1.0-6

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 28 2014 Orion Poplawski <orion@cora.nwra.com> - 1.0.3-1
- Update to 1.0-3

* Fri Jan 10 2014 Orion Poplawski <orion@cora.nwra.com> - 1.0.2-2
- Fix license

* Thu Jan 9 2014 Orion Poplawski <orion@cora.nwra.com> - 1.0.2-1
- Initial package
