%define packname car
%global packver 2.0
# Note that some R packages do not use packrel
%define packrel 22

%global __suggests_exclude ^R\\((MatrixModels|SparseM|alr4|leaps|lme4|pbkrtest|quantreg|rgl|survey)\\)

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          24%{?dist}
Source0:          http://cran.r-project.org/src/contrib/car_%{packver}-%{packrel}.tar.gz
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              http://cran.r-project.org/web/packages/car/index.html
Summary:          Companion to Applied Regression package for R
BuildRequires:    R-devel, tex(latex)
BuildArch:        noarch

%description
This package accompanies J. Fox, An R and S-PLUS Companion to Applied
Regression, Sage, 2002. The package contains mostly functions for applied
regression, linear models, and generalized linear models, with an emphasis on
regression diagnostics, particularly graphical diagnostic methods.  There are
also some utility functions. With some exceptions, it does not duplicate
capabilities in the basic distribution of R, nor in widely used packages.
Where relevant, the functions in car are consistent with na.action = na.omit
or na.exclude.

%prep
%setup -q -c -n %{packname}
#Fix permissions
find -type f | xargs chmod -x
#Fix encoding
iconv -f iso-8859-1 -t utf-8 < car/NEWS | tr -d '\r' > car/NEWS.utf-8
touch -r car/NEWS car/NEWS.utf-8
mv car/NEWS.utf-8 car/NEWS

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_datadir}/R/library %{packname}
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/R.css

%check
# Use --no-install until R-leaps is available
%{_bindir}/R CMD check --no-install %{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/doc/
%doc %{_datadir}/R/library/%{packname}/html/
%doc %{_datadir}/R/library/%{packname}/CITATION
%doc %{_datadir}/R/library/%{packname}/DESCRIPTION
%doc %{_datadir}/R/library/%{packname}/NEWS
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/data
%{_datadir}/R/library/%{packname}/help

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.22-23
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.0.22-21
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.0.22-17
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 2.0.22-15
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 2.0.22-11
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun  6 2020 Tom Callaway <spot@fedoraproject.org> - 2.0.22-8
- rebuild for R 4
- NOTE: There is a much newer version of this
  but it needs some missing dependencies to be packaged

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.22-6
- Exclude Suggests for unavailable packages

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.22-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 José Matos <jamatos@fedoraproject.org> - 2.0.22-1
- Rebuild last version without the added dependencies (that still need to be added to Fedora)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 21 2015 José Matos <jamatos@fedoraproject.org> - 2.0.25-1
- Update to 2.0-25

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 16 2013 Orion Poplawski <orion@cora.nwra.com> 2.0.19-1
- Update to 2.0-19

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 2.0.16-1
- update to modern versioning, 2.0-16

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 7 2012 Orion Poplawski <orion@cora.nwra.com> 2.0-15
- Update to 2.0-15
- Update spec to current guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 7 2011 Orion Poplawski <orion@cora.nwra.com> 2.0-11
- Update to 2.0-11

* Tue Feb 8 2011 Orion Poplawski <orion@cora.nwra.com> 2.0-9
- Update to 2.0-9

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-17.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 13 2009 Orion Poplawski <orion@cora.nwra.com> 1.2-16.1
- Rebuild for R 2.10.0

* Wed Nov 4 2009 Orion Poplawski <orion@cora.nwra.com> 1.2-16
- Update to 1.2-16

* Fri Oct 2 2009 Orion Poplawski <orion@cora.nwra.com> 1.2-15
- Update to 1.2-15

* Mon Aug 10 2009 Orion Poplawski <orion@cora.nwra.com> 1.2-8
- Update to 1.2-14

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Orion Poplawski <orion@cora.nwra.com> 1.2-6
- Update to 1.2-12

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 14 2009 Orion Poplawski <orion@cora.nwra.com> 1.2-5
- Update to 1.2-11

* Thu Oct 23 2008 Orion Poplawski <orion@cora.nwra.com> 1.2-4
- Update to 1.2-9

* Wed May 7 2008 Orion Poplawski <orion@cora.nwra.com> 1.2-3
- Update to 1.2-8
- Fix URLs

* Wed Feb 13 2008 Orion Poplawski <orion@cora.nwra.com> 1.2-2
- Fix file permissions, line endings and encoding

* Wed Feb 13 2008 Orion Poplawski <orion@cora.nwra.com> 1.2-1
- Initial package creation
