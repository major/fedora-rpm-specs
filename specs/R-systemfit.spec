%global packname systemfit
%global packver 1.1
%global packrel 26

%global __suggests_exclude ^R\\((plm|sem)\\)

Summary:        Simultaneous Equation Estimation R Package
Name:		R-%{packname}
Version:	%{packver}.%{packrel}
Release:	10%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Source0:        http://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrel}.tar.gz
URL:		http://www.systemfit.org
BuildRequires:	R-devel >= 3.2.0, R-Matrix, R-car >= 2.0.0, R-lmtest, tex(latex)
BuildRequires:	R-sandwich
BuildArch:	noarch


%description
This R package contains functions for fitting simultaneous systems of linear
and nonlinear equations using Ordinary Least Squares (OLS), Weighted Least
Squares (WLS), Seemingly Unrelated Regressions (SUR), Two-Stage Least Squares
(2SLS), Weighted Two-Stage Least Squares (W2SLS), Three-Stage Least Squares
(3SLS), and Weighted Three-Stage Least Squares (W3SLS).


%prep
%setup -q -c -n %{packname}
iconv -f iso-8859-1 -t utf-8 < systemfit/man/systemfit.Rd > systemfit/man/systemfit.Rd_
mv systemfit/man/systemfit.Rd_ systemfit/man/systemfit.Rd


%build


%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_datadir}/R/library %{packname}
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_datadir}/R/library/R.css


%check
#We have to use --no-install because we don't have all of the suggested
#dependencies
%{_bindir}/R CMD check --no-install  %{packname}


%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/doc
%doc %{_datadir}/R/library/%{packname}/html
%doc %{_datadir}/R/library/%{packname}/NEWS
%{_datadir}/R/library/%{packname}/CITATION
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/data
%{_datadir}/R/library/%{packname}/help


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.26-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.26-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.26-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 1.1.26-1
- update to 1.1-26
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.1.24-5
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.24-2
- rebuild for R 4

* Thu Mar 19 2020 José Matos <jamatos@fedoraproject.org> - 1.1.24-1
- Update to 1.1-24

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.22-6
- Exclude Suggests for unavailable packages

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.22-5
- Remove explicit dependencies provided by automatic dependency generator

* Sat Aug 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.22-4
- Remove unnecessary _R_make_search_index

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep  1 2018 José Matos <jamatos@fedoraproject.org> - 1.1.22-1
- update to 1.1-22
- update url and source0 to newer versions

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 1.1.15-1
- update to 1.1.15

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 5 2011 Orion Poplawski <orion@cora.nwra.com> - 1.1.11-1
- Update to 1.1-11, use new Fedora versioning

* Tue Feb 8 2011 Orion Poplawski <orion@cora.nwra.com> - 1.1-9
- Update to 1.1-9

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun 3 2010 Orion Poplawski <orion@cora.nwra.com> - 1.1-4
- Upstream re-released 1.1-4 with a slight change (again).  Oh joy.

* Sun Jan 10 2010 Orion Poplawski <orion@cora.nwra.com> - 1.1-3
- Upstream re-released 1.1-4 with a slight change.  Oh joy.

* Thu Nov 19 2009 Orion Poplawski <orion@cora.nwra.com> - 1.1-2
- Update spec for R 2.10.0 (fixes FTBFS bug #538892)

* Mon Aug 10 2009 Orion Poplawski <orion@cora.nwra.com> - 1.1-1
- Update to 1.1-4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Orion Poplawski <orion@cora.nwra.com> - 1.0-6
- Update to 1.0-9
- Fix latex requires

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 23 2008 Orion Poplawski <orion@cora.nwra.com> - 1.0-4
- Update to 1.0-7
- New source URL

* Mon Jul 14 2008 Orion Poplawski <orion@cora.nwra.com> - 1.0-3
- Add BR R-lmtest
- Use "--no-install" in %%check to avoid missing suggested dependencies

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-2
- fix license tag

* Thu Feb 14 2008 Orion Poplawski <orion@cora.nwra.com> - 1.0-1
- Update to 1.0-2

* Wed Feb 13 2008 Orion Poplawski <orion@cora.nwra.com> - 0.8-7
- Update to 0.8-5

* Wed Aug 15 2007 Orion Poplawski <orion@cora.nwra.com> - 0.8-6
- Update to 0.8-3

* Thu Jul 12 2007 Orion Poplawski <orion@cora.nwra.com> - 0.8-5
- Convert systemfit.Rd to UTF-8

* Thu Jul 12 2007 Orion Poplawski <orion@cora.nwra.com> - 0.8-4
- Fix URL
- Add Requires: R

* Wed Jul 11 2007 Orion Poplawski <orion@cora.nwra.com> - 0.8-3
- Update to 0.8-2
- Comply with R packaging guidelines

* Mon Mar 19 2007 Orion Poplawski <orion@cora.nwra.com> - 0.8-2
- Make noarch

* Tue Mar 06 2007 Orion Poplawski <orion@cora.nwra.com> - 0.8-1
- Initial package
