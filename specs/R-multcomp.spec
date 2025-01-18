%define packname multcomp
%global packver  1.4
%define packrel  23

%global __suggests_exclude ^R\\((ISwR|SimComp|coin|coxme|lme4|robustbase|tram)\\)

Summary:        Simultaneous inference for general linear hypotheses R Package
Name:           R-%{packname}
Version:        %{packver}.%{packrel}
Release:        8%{?dist}
License:        GPL-2.0-only
Source0:        http://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrel}.tar.gz
URL:            http://cran.r-project.org/web/packages/multcomp/index.html
BuildArch:      noarch
BuildRequires:  R-devel >= 3.0.0, tex(latex)
BuildRequires:  R-stats, R-graphics
BuildRequires:  R-TH-data >= 1.0.2
BuildRequires:  R-mvtnorm >= 1.0.10
BuildRequires:  R-sandwich >= 2.3.0
BuildRequires:  R-survival >= 2.39.4
BuildRequires:  R-codetools
#For a test
BuildRequires:  R-lmtest
#Needed for more testing coverage, but not in fedora yet
#BuildRequires:  R-lme4

%description
This R package contains functions for simultaneous tests and confidence
intervals for general linear hypotheses in parametric models, including
linear, generalized linear, linear mixed effects, and survival models.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_datadir}/R/library %{packname}
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_datadir}/R/library/R.css

%check
#We have to use --no-install because we don't have all of the suggested
#dependencies
%{_bindir}/R CMD check --no-install %{packname}


%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/demo
%doc %{_datadir}/R/library/%{packname}/deprecated
%doc %{_datadir}/R/library/%{packname}/doc
%doc %{_datadir}/R/library/%{packname}/html
%doc %{_datadir}/R/library/%{packname}/CITATION
%doc %{_datadir}/R/library/%{packname}/DESCRIPTION
%doc %{_datadir}/R/library/%{packname}/NEWS
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/MCMT
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/data
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/multcomp_VA.R
%{_datadir}/R/library/%{packname}/multcomp_coxme.R


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.23-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.23-2
- R-maint-sig mass rebuild

* Wed Mar 15 2023 Tom Callaway <spot@fedoraproject.org> - 1.4.23-1
- update to 1.4-23

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.4.20-1
- update to 1.4-20
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.4.17-1
- update to 1.4-17
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.13-1
- update to 1.4-13
- rebuild for R 4

* Thu Mar 19 2020 José Matos <jamatos@fedoraproject.org> - 1.4.12-1
- update to 1.4-12

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.10-4
- Exclude Suggests for unavailable packages

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.10-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 30 2019 José Matos <jamatos@fedoraproject.org> - 1.4.10-1
- update to 1.4-10

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep  1 2018 José Matos <jamatos@fedoraproject.org> - 1.4.8-1
- update to 1.4-8

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May  7 2016 José Matos <jamatos@fedoraproject.org> - 1.4.5-2
- update to 1.4-5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 José Matos <jamatos@fedoraproject.org> - 1.4.1-1
- Update to 1.4-1

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 José Matos <jamatos@fedoraproject.org> - 1.4.0-1
- update to 1.4-0

* Wed Feb 18 2015 Orion Poplawski <orion@cora.nwra.com> - 1.3.9-1
- Update to 1.3-9

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 6 2014 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-1
- Update to 1.3-2

* Wed Jan 8 2014 Orion Poplawski <orion@cora.nwra.com> - 1.3.1-1
- Update to 1.3-1

* Wed Oct 16 2013 Orion Poplawski <orion@cora.nwra.com> - 1.3.0-1
- Update to 1.3-0

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 1.2.17-1
- update to 1.2-17

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 7 2011 Orion Poplawski <orion@cora.nwra.com> - 1.2-8
- Update to 1.2-8

* Wed Jun 22 2011 Orion Poplawski <orion@cora.nwra.com> - 1.2-7
- Update to 1.2-6
- Drop --no-latex in check, no longer needed

* Tue Feb 8 2011 Orion Poplawski <orion@cora.nwra.com> - 1.2-6
- Update to 1.2-5

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 7 2010 Orion Poplawski <orion@cora.nwra.com> - 1.2-4
- Update to 1.2-4
- Add patch to fix noinstall build

* Thu Jun 3 2010 Orion Poplawski <orion@cora.nwra.com> - 1.1-7
- Update to 1.1-7
- Add BR on R-lmtest for a build time test

* Sun Jan 10 2010 Orion Poplawski <orion@cora.nwra.com> - 1.1-3
- Update to 1.1-3

* Fri Nov 6 2009 Orion Poplawski <orion@cora.nwra.com> - 1.1-2.1
- Remove missing files

* Fri Oct 2 2009 Orion Poplawski <orion@cora.nwra.com> - 1.1-2
- Update to 1.1-2

* Mon Aug 10 2009 Orion Poplawski <orion@cora.nwra.com> - 1.1-1
- Update to 1.1-1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Orion Poplawski <orion@cora.nwra.com> - 1.0-5
- Update to 1.0-7

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 14 2009 Orion Poplawski <orion@cora.nwra.com> - 1.0-3
- Update to 1.0-5

* Thu Oct 23 2008 Orion Poplawski <orion@cora.nwra.com> - 1.0-2
- Update to 1.0-3

* Thu Sep 4 2008 Orion Poplawski <orion@cora.nwra.com> - 1.0-1
- Update to 1.0-2

* Wed Apr 2 2008 Orion Poplawski <orion@cora.nwra.com> - 1.0-0
- Update to 1.0-0
- Update URL

* Tue Mar 4 2008 Orion Poplawski <orion@cora.nwra.com> - 0.993-1
- Update to 0.993-1

* Fri Feb 15 2008 Orion Poplawski <orion@cora.nwra.com> - 0.992-4
- Update to 0.992-8

* Mon Jul 23 2007 Orion Poplawski <orion@cora.nwra.com> - 0.992-3
- Update to 0.992-5
- Update license tag

* Mon Jul 23 2007 Orion Poplawski <orion@cora.nwra.com> - 0.992-2
- Update to 0.992-4, requires R-mvtnorm >= 0.8
- Fix URL and tabs/spaces

* Wed Jul 11 2007 Orion Poplawski <orion@cora.nwra.com> - 0.992-1
- Update to 0.992-2
- Comply with R packaging guidelines

* Mon Mar 19 2007 Orion Poplawski <orion@cora.nwra.com> - 0.991.8-1
- Initial package
