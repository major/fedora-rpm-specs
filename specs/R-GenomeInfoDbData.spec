%global packname GenomeInfoDbData
%global packver 1.2.8

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Source0:          http://www.bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{packver}.tar.gz
License:          Artistic-2.0
URL:              http://www.bioconductor.org/packages/release/data/annotation/html/GenomeInfoDbData.html
Summary:          Species and taxonomy ID look up tables used by GenomeInfoDb
BuildRequires:    R-devel >= 3.5.0, tex(latex)
BuildArch:        noarch

%description
Files for mapping between NCBI taxonomy ID and species. Used by functions 
in the GenomeInfoDb package.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_datadir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/data
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/scripts

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.8-8
- R-maint-sig mass rebuild

* Sat Apr  20 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.8-7
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.8-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 1.2.8-1
- update to 1.2.8
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 1.2.6-1
- update to 1.2.6
- rebuild for R 4.1.0

* Thu Feb  4 2021 Tom Callaway <spot@fedoraproject.org> - 1.2.4-1
- update to 1.2.4

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.2.3-1
- update to 1.2.3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 1.2.2-1
- update to 1.2.2

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 1.0.0-1
- update to 1.0.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Tom Callaway <spot@fedoraproject.org> - 0.99.0-1
- initial package
