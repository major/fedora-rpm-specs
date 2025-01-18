%define packname  qvalue
%define Rversion  3.0.0

Name:             R-%{packname}
Version:          2.24.0
Release:          15%{dist}
Summary:          Q-value estimation for false discovery rate control
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:          LicenseRef-Callaway-LGPLv2+
URL:              http://bioconductor.org/packages/release/bioc/html/qvalue.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
BuildRequires:    R-devel >= %{Rversion} tex(latex) R-splines R-ggplot2 R-grid R-reshape2 R-knitr
BuildRequires:    tex(fullpage.sty)

%description
It takes a list of p-values resulting from the simultaneous
testing of many hypotheses and estimates their q-values.
The q-value of a test measures the proportion of false positives
incurred (called the false discovery rate) when that particular
test is called significant. Various plots are automatically
generated, allowing one to make sensible significance cut-offs.
Several mathematical results have recently been shown on the
conservative accuracy of the estimated q-values from this software.
The software can be applied to problems in genomics, brain imaging,
astrophysics, and data mining.

This package is a part of the Bioconductor (bioconductor.org) project.

%prep
%setup -q -c -n %{packname}

%build

%install
sed -i -e 's/\r$//' %{packname}/inst/doc/qvalue.Rnw

mkdir -p %{buildroot}%{_datadir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_datadir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_datadir}/R/library/R.css

chmod -x %{buildroot}%{_datadir}/R/library/%{packname}/doc/*

%check
%{_bindir}/R CMD check --ignore-vignettes %{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/doc
%doc %{_datadir}/R/library/%{packname}/html
%doc %{_datadir}/R/library/%{packname}/DESCRIPTION
%doc %{_datadir}/R/library/%{packname}/NEWS
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/data
%{_datadir}/R/library/%{packname}/help


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.24.0-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.24.0-12
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 12 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.24.0-8
- Ignore vignettes

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.24.0-7
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 04 2022 Iñaki Úcar <iucar@fedoraproject.org> - 2.24.0-5
- R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 2.24.0-1
- update to 2.24.0
- Rebuilt for R 4.1.0

* Thu Feb  4 2021 Tom Callaway <spot@fedoraproject.org> - 2.22.0-1
- update to 2.22.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 José Abílio Matos <jamatos@fc.up.pt> - 2.18.0-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 2.18.0-1
- update to 2.18.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.12.0-1
- Update to 2.12.0

* Mon Jul 02 2018 José Abílio Matos <jamatos@fc.up.pt> - 1.38.0-7
- rebuild with R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 02 2014 pingou <pingou@pingoured.fr> 1.38.0-1
- Update to version 1.38.0

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 pingou <pingou@pingoured.fr> 1.36.0-1
- Update to version 1.36.0

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 07 2013 pingou <pingou@pingoured.fr> 1.34.0-1
- Update to version 1.34.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 pingou <pingou@pingoured.fr> 1.32.0-1
- Update to version 1.32.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 pingou <pingou@pingoured.fr> 1.30.0-1
- Update to version 1.30.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> 1.28.0-1
- update to 1.28.0

* Wed Jun 22 2011 pingou <pingou@pingoured.fr> 1.26.0-1
- Update to version 1.26.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 pingou <pingou@pingoured.fr> 1.24.0-1
- Update to version 1.24.0

* Tue May 11 2010 pingou <pingou@pingoured.fr> 1.22.0-1
- Update to version 1.22.0
- Fix url to a more stable form
- Remove R on post an postun since there are no post/postun

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 1.20.0-1
- Update to 1.20.0
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0
- Fix BR tex(latex)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 29 2009 pingou <pingou@pingoured.fr> - 1.18.0-1
- Update to Bioconductor 2.4 and R 2.9.0

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 pingou <pingoufc4-at-yahoo.fr> 1.16.0-1
- Update to version 1.16.0

* Tue Jun 25 2008 pingou <pingoufc4-at-yahoo.fr> 1.14.0-3
- Change the url

* Tue May 27 2008 pingou <pingoufc4-at-yahoo.fr> 1.14.0-2
- Rebuild

* Tue May 27 2008 pingou <pingoufc4-at-yahoo.fr> 1.14.0-1
- Update to version 1.14.0

* Tue Jan 08 2008 Pingou <pingoufc4@yahoo.fr> 1.12.0-2
- Fix problem on the doc

* Sat Jan 05 2008 Pingou <pingoufc4@yahoo.fr> 1.12.0-1
- Initial package for Fedora
