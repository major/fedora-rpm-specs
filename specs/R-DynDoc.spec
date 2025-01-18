%define packname  DynDoc
%define Rversion  3.0.0

Name:             R-%{packname}
Version:          1.74.0
Release:          10%{dist}
Summary:          Functions for dynamic documents
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/DynDoc.html
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
BuildRequires:    R-devel >= %{Rversion} tex(latex) R-methods, R-utils
#ExclusiveArch:    armv7, ppc, go_arch

%description
A set of functions to create and interact with dynamic documents and
vignettes.

%prep
%setup -c -q -n %{packname}

%build

%install
%{__rm} -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_datadir}/R/library

# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/DESCRIPTION
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/help

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.74.0-8
- R-maint-sig mass rebuild

* Sat Apr  20 2024 Miroslav Suchý <msuchy@redhat.com> - 1.74.0-7
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.74.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug  3 2022 Tom Callaway <spot@fedoraproject.org> - 1.74.0-1
- update to 1.74.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.70.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.70.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.70.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 1.70.0-1
- update to 1.70.0

* Thu Feb  4 2021 Tom Callaway <spot@fedoraproject.org> - 1.68.0-1
- update to 1.68.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.66.0-1
- update to 1.66.0
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.64.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov  5 2019 Tom Callaway <spot@fedoraproject.org> - 1.64.0-1
- update to 1.64.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.58.0-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.58.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.58.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.58.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.58.0-1
- Update to 1.58.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 pingou <pingou@pingoured.fr> 1.52.0-1
- Update to version 1.52.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 02 2014 pingou <pingou@pingoured.fr> 1.42.0-1
- Update to version 1.42.0

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 pingou <pingou@pingoured.fr> 1.40.0-1
- Update to version 1.40.0

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 07 2013 pingou <pingou@pingoured.fr> 1.38.0-1
- Update to version 1.38.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 pingou <pingou@pingoured.fr> 1.36.0-1
- Update to version 1.36.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 pingou <pingou@pingoured.fr> 1.34.0-1
- Update to version 1.34.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> 1.32.0-2
- rebuild for R 2.14.0

* Thu Nov 03 2011 pingou <pingou@pingoured.fr> 1.32.0-1
- Update to version 1.32.0

* Wed Jun 22 2011 pingou <pingou@pingoured.fr> 1.30.0-1
- Update to version 1.30.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 pingou <pingou@pingoured.fr> 1.28.0-1
- Update to version 1.28.0

* Tue May 11 2010 pingou <pingou@pingoured.fr> 1.26.0-1
- Update to version 1.26.0
- Update url and source0 to more stable link
- Requires R-core instead of R
- Requires tex(latex)

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 1.24.0-1
- Update to 1.24.0
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 pingou <pingou@pingoured.fr> 1.22.0-1
- Update to Bioconductor 2.4 and R-2.9.0

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 pingou <pingoufc4-at-yahoo.fr> 1.20.0-1
- Update to version 1.20.0 for R >= 2.8.0

* Wed Jun 25 2008 Pingou <pingoufc4@yahoo.fr> 1.18.0-2
- Change the url

* Fri May 02 2008 Pingou <pingoufc4@yahoo.fr> 1.18.0-1
- Update to bioconductor 2.2

* Mon Oct 08 2007 Pingou <pingoufc4@yahoo.fr> 1.17.0-1
- Update to bioconductor 2.1

* Wed Aug 29 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-5
-Change the license tag

* Fri Jul 13 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-4
- Change in the BR and R to fit the guidelines

* Tue Jul 10 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-3
- Change _libdir to _datadir as it is a noarch package
- Change in the files section to mark the folder
- Change in the post and postun section to fit with the packaging guidelines
- Change in the prep section to fit with the packaging guidelines

* Wed May 23 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-2
- Submitting to Fedora Extras

* Wed May 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.14.0-1
- initial package for Fedora
