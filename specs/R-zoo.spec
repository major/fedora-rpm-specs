# This is the CRAN name
%global packname zoo
# This is the main package version
%global packver 1.8
# Note that some R packages do not use packrel
%global packrel 12

%global with_suggests 0

%global __suggests_exclude ^R\\((AER|mondate|strucchange|tis|tseries|xts)\\)

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          8%{?dist}
License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrel}.tar.gz

Summary:          Z's ordered observations for irregular time series
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils
BuildRequires:    R-graphics
BuildRequires:    R-grDevices
BuildRequires:    R-lattice >= 0.20.27

%if %{with_suggests}
BuildRequires:    R-AER
BuildRequires:    R-coda
BuildRequires:    R-chron
BuildRequires:    R-ggplot2 >= 3.0.0
BuildRequires:    R-mondate
BuildRequires:    R-scales
BuildRequires:    R-stinepack
BuildRequires:    R-strucchange
BuildRequires:    R-timeDate
BuildRequires:    R-timeSeries
BuildRequires:    R-tis
BuildRequires:    R-tseries
BuildRequires:    R-xts
%endif

%package          devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description
An S3 class with methods for totally ordered indexed observations. It is
particularly aimed at irregular time series of numeric vectors/matrices and
factors. zoo's key design goals are independence of a particular index/date/
time class and consistency with with ts and base R by providing methods to
extend standard generics.

%description    devel
The %{name}-devel  package contains Header and libraries files for
developing applications that use %{name}

%prep
%setup -q -c -n %{packname}
#Fix line endings
sed -i -e 's/\r//' zoo/inst/doc/zoo*.Rnw


%build


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css


%check
#We have to use --no-install because we don't have all of the suggested
#dependencies
%{_bindir}/R CMD check --no-install %{packname}


%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/demo
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/CITATION
%doc %{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/THANKS
%doc %{_libdir}/R/library/%{packname}/WISHLIST
%doc %{_libdir}/R/library/%{packname}/TODO
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs

%files devel
%{_libdir}/R/library/%{packname}/include

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.8.12-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.8.12-2
- R-maint-sig mass rebuild

* Wed Apr 19 2023 Tom Callaway <spot@fedoraproject.org> - 1.8.12-1
- update to 1.8-12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Tom Callaway <spot@fedoraproject.org> - 1.8.10-1
- update to 1.8-10
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 1.8.9-1
- update to 1.8-9
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 1.8.8-2
- rebuild for R 4

* Sat May 16 2020 José Matos <jamatos@fedoraproject.org> - 1.8.8-1
- update to 1.8-8

* Wed Mar 18 2020 José Matos <jamatos@fedoraproject.org> - 1.8.7-1
- update to 1.8-7

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.6-4
- Exclude Suggests for unavailable packages

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.6-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 José Matos <jamatos@fedoraproject.org> - 1.8.6-1
- update to 1.8-6
- add all the suggests packages available in Fedora (BR and Suggests)

* Sat Mar 30 2019 José Matos <jamatos@fedoraproject.org> - 1.8.5-1
- update to 1.8-5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 José Matos <jamatos@fedoraproject.org> - 1.8.3-1
- update to 1.8-3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 José Matos <jamatos@fedoraproject.org> - 1.8.2-1
- update to 1.8-2
- clean spec file

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.8.1-1
- update to 1.8-1, rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May  7 2016 José Matos <jamatos@fedoraproject.org> - 1.7.13-1
- update to 1.7-13

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 17 2015 José Matos <jamatos@fedoraproject.org> - 1.7.12-1
- update to 1.7-12
- update license to GPL2 or GPL3
- remove conditional statment that is true for all supported versions
  of Fedora and EPEL
- add -devel subpackage

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 16 2013 Orion Poplawski <orion@cora.nwra.com> 1.7.10-1
- Update to 1.7-10

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 1.7.9-1
- update to 1.7.9

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 8 2011 Tom Callaway <spot@fedoraproject.org> 1.7.6-2
- disable tests on el4
- add el conditional for tex BR

* Tue Nov 8 2011 Tom Callaway <spot@fedoraproject.org> 1.7.6-1
- convert to new model
- rebuild for 2.14.0

* Mon Nov 7 2011 Orion Poplawski <orion@cora.nwra.com> 1.7-6
- Update to 1.7-6
- No longer noarch

* Tue Feb 8 2011 Orion Poplawski <orion@cora.nwra.com> 1.6-5
- Update to 1.6-4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 13 2010 Orion Poplawski <orion@cora.nwra.com> 1.6-3
- Update to 1.6-3

* Sun Jan 10 2010 Orion Poplawski <orion@cora.nwra.com> 1.6-2
- Update to 1.6-2

* Thu Nov 12 2009 Orion Poplawski <orion@cora.nwra.com> 1.5-9
- Rebuild for R 2.10.0

* Fri Oct 2 2009 Orion Poplawski <orion@cora.nwra.com> 1.5-8
- Update to 1.5-8

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 4 2008 Orion Poplawski <orion@cora.nwra.com> 1.5-5
- Update to 1.5-4

* Tue May 20 2008 Orion Poplawski <orion@cora.nwra.com> 1.5-4
- Add a couple more doc files

* Mon May 12 2008 Orion Poplawski <orion@cora.nwra.com> 1.5-3
- Include time series in summary
- Fix up build requires for older versions

* Fri May 9 2008 Orion Poplawski <orion@cora.nwra.com> 1.5-2
- Fix URL
- Fix line endings
- Change requires to tex(latex)

* Wed May 7 2008 Orion Poplawski <orion@cora.nwra.com> 1.5-1
- Initial package creation
