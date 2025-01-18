%global packname BH
%global packver 1.78.0
%global packrel 0

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          13%{?dist}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrel}.tar.gz
# Automatically converted from old format: Boost - review is highly recommended.
License:          BSL-1.0
URL:              https://cran.r-project.org/package=%{packname}
Summary:          Boost C++ Header Files for R
BuildRequires:    R-devel >= 3.0.0, tex(latex)
BuildArch:        noarch

%description
Boost provides free peer-reviewed portable C++ source libraries. A large part 
of Boost is provided as C++ template code which is resolved entirely at 
compile-time without linking. This package aims to provide the most useful 
subset of Boost libraries for template use among CRAN package. By placing 
these libraries in this package, we offer a more efficient distribution 
system for CRAN as replication of this code in the sources of other packages 
is avoided. 

%package devel
Summary:        Boost C++ Header Files for R

%description devel
Boost provides free peer-reviewed portable C++ source libraries. A large part 
of Boost is provided as C++ template code which is resolved entirely at 
compile-time without linking. This package aims to provide the most useful 
subset of Boost libraries for template use among CRAN package. By placing 
these libraries in this package, we offer a more efficient distribution 
system for CRAN as replication of this code in the sources of other packages 
is avoided.

%prep
%setup -q -c -n %{packname}
# Remove spurious exec permissions
for i in `find %{packname}/inst/include/boost |grep hpp`; do chmod -x $i; done

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_datadir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/R.css

%check
%{_bindir}/R CMD check %{packname}

%files devel
%license %{_datadir}/R/library/%{packname}/LICENSE_1_0.txt
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/NEWS.Rd
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/include

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.78.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul  24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.78.0.0-12
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.78.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.78.0.0-10
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.78.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.78.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.78.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.78.0.0-6
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.78.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug  2 2022 Tom Callaway <spot@fedoraproject.org> - 1.78.0.0-4
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.78.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.78.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Tom Callaway <spot@fedoraproject.org> - 1.78.0.0-1
- update to 1.78.0-0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.75.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 1.75.0.0-3
- rebuild for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.75.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Tom Callaway <spot@fedoraproject.org> - 1.75.0.0-1
- update to 1.75.0-0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.72.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 José Abílio Matos <jamatos@fc.up.pt> - 1.72.0.3-4
- bump version to ensure upgrade path (due to a F32 rebuild)

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.72.0.3-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.72.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Tom Callaway <spot@fedoraproject.org> - 1.72.0.3-1
- update to 1.72.0-3

* Tue Dec 17 2019 Tom Callaway <spot@fedoraproject.org> - 1.72.0.2-1
- update to 1.72.0-2

* Mon Dec 16 2019 Tom Callaway <spot@fedoraproject.org> - 1.72.0.1-1
- update to 1.72.0-1

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.69.0.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.69.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar  6 2019 Tom Callaway <spot@fedoraproject.org> - 1.69.0.1-1
- update to 1.69.0-1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 1.66.0.1-1
- update to 1.66.0-1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.62.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.62.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.62.0.1-2
- remove spurious exec permissions

* Tue May 30 2017 Tom Callaway <spot@fedoraproject.org> - 1.62.0.1-1
- initial package
