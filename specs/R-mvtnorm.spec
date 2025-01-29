%global packname	mvtnorm
#%%global packver		1.3
%global packver         1.1
%global packrel		3

Summary:	Multivariate normal and T distribution R Package
Name:		R-%{packname}
Version:	%{packver}.%{packrel}
Release:	%autorelease
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
Source0:	https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrel}.tar.gz
URL:		https://cran.r-project.org/web/packages/mvtnorm/index.html

# qrng is not packaged for Fedora yet - https://cran.r-project.org/src/contrib/qrng_0.0-10.tar.gz
#Source1:        qrng_0.0-10.tar.gz

BuildRequires:	R-devel >= 3.5.0
BuildRequires:	tex(latex)
BuildRequires:	gcc-gfortran
BuildRequires:	R-stats
BuildRequires:	R-methods

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description
This R package computes multivariate normal and t probabilities, quantiles
and densities.

%description    devel
The %{name}-devel  package contains Header and libraries files for
developing applications that use %{name}

%prep
#tar zxf %{SOURCE1}
%setup -q -c -n %{packname}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
#pushd ..
#%%{_bindir}/R CMD INSTALL qrng -l %%{buildroot}%%{_libdir}/R/library
#popd
%{_bindir}/R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/CITATION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs

%files devel
%{_libdir}/R/library/%{packname}/C_API_Example
%{_libdir}/R/library/%{packname}/include

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.3-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.3-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.3-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Tom Callaway <spot@fedoraproject.org> - 1.1.3-1
- update to 1.1-3
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 1.1.2-1
- update to 1.1.2
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.0-1
- update to 1.1-0
- rebuild for R 4

* Thu Feb 06 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.0.12-1
- Upgrade to 1.0.12

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 1.0.11-1
- update to 1.0-11

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.10-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 30 2019 José Matos <jamatos@fedoraproject.org> - 1.0.10-1
- update to 1.0.10

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1.0.7-1
- update to 1.0.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.0.6-1
- update to 1.0-6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 José Matos <jamatos@fedoraproject.org> - 1.0.3-1
- Update to 1.0_3

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9996-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9996-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9996-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 16 2013 Orion Poplawski - 0.9.9996-1
- Update to 0.9-9996

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9994-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 0.9.9994-1
- update to 0.9.9994

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9991-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9991-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9991-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 8 2011 Tom Callaway <spot@fedoraproject.org> - 0.9.9991-1
- update spec
- rebuild for R-2.14.0

* Mon Nov 7 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9-9991
- Update to 0.9-9991

* Tue Feb 8 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9-96
- Update to 0.9-96

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 21 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-9
- Update to 0.9-9

* Thu Nov 19 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-8.1
- Update to 0.9-8
- Update spec for R 2.10.0 (fixes FTBFS bug #539041)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.9-7
- Update to 0.9-7

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 4 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-1
- Update to 0.9-2

* Sat Feb  9 2008 Orion Poplawski <orion@cora.nwra.com> - 0.8-4
- Rebuild for gcc 3.4

* Thu Aug 23 2007 Orion Poplawski <orion@cora.nwra.com> - 0.8-3
- Update license tag to GPLv2
- Rebuild for ppc32

* Tue Jul 24 2007 Orion Poplawski <orion@cora.nwra.com> - 0.8-2
- Update to 0.8-1, fixes test

* Mon Jul 23 2007 Orion Poplawski <orion@cora.nwra.com> - 0.8-1
- Update to 0.8-0

* Wed Jul 11 2007 Orion Poplawski <orion@cora.nwra.com> - 0.7-2
- Comply with R packaging guidelines

* Mon Mar 19 2007 Orion Poplawski <orion@cora.nwra.com> - 0.7-1
- Initial package
