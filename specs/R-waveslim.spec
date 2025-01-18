%define packname waveslim

%global __suggests_exclude ^R\\((fftw|covr)\\)

Summary: R module, Basic wavelet routines for 1,2 and 3-dimensional signal processing
Name: R-%{packname}
Version: 1.8.4
Release: 10%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Source0: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{version}.tar.gz
URL: http://waveslim.r-forge.r-project.org/
BuildRequires: R-devel, tetex-latex, gcc-gfortran


%description
Basic wavelet routines for time series (1D), image (2D)
and array (3D) analysis.  The code provided here is based on
wavelet methodology developed in Percival and Walden (2000);
Gencay, Selcuk and Whitcher (2001); the dual-tree complex wavelet
transform (CWT) from Kingsbury (1999, 2001) as implemented by
Selesnick; and Hilbert wavelet pairs (Selesnick 2001, 2002).  All
figures in chapters 4-7 of GSW (2001) are reproducible using this
package and R code available at the book website(s) below.

%prep
%setup -q -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
cd ..; R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
%{__rm} -rf %{buildroot}%{_libdir}/R/library/R.css

%check
# Wants fftw
# cd ..;%{_bindir}/R CMD check %{packname}

%files
%{_libdir}/R/library/%{packname}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.4-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.8.4-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.8.4-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.8.4-1
- update to 1.8.4
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 1.8.2-6
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.8.2-2
- rebuild for R 4

* Sun Mar 15 2020 José Matos <jamatos@fedoraproject.org> - 1.8.2-1
- update to 1.8.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.5.1-4
- Exclude Suggests for unavailable packages

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.5.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 José Matos <jamatos@fedoraproject.org> - 1.7.5.1-1
- update to 1.7.5.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1.7.5-8
- rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.7.5-4
- rebuild for R 3.4.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 21 2015 José Matos <jamatos@fedoraproject.org> - 1.7.5-1
- Update to 1.7.5

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 23 2013 José Matos <jamatos@fedoraproject.org> - 1.7.3-1
- update to 1.7.3

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 1.7.2-1
- update to 1.7.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> - 1.6.4-2
- rebuild for R 2.14.0

* Thu Mar 17 2011 José Matos <jamatos@fedoraproject.org> - 1.6.4-1
- Update to latest stable release.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 28 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.1-5
- update scriptlets, url

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 José Matos <jamatos[AT]fc.up.pt> - 1.6.1-2
- Rebuild for gcc 4.3

* Mon Jan  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.1-1
- bump to 1.6.1

* Mon Jan  7 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.6-5
- BuildRequires: R-devel rather than just R

* Mon Aug 27 2007 José Matos <jamatos[AT]fc.up.pt> - 1.6-4
- License fix, rebuild for devel (F8).

* Thu Apr 26 2007 José Matos <jamatos[AT]fc.up.pt> - 1.6-3
- Create install dir.

* Thu Apr 26 2007 José Matos <jamatos[AT]fc.up.pt> - 1.6-2
- Rebuild for R 2.5.

* Sat Apr 21 2007 José Matos <jamatos[AT]fc.up.pt> - 1.6-1
- New upstream version.

* Tue Oct 17 2006 José Matos <jamatos[AT]fc.up.pt> - 1.5-5
- Rebuild for R 2.4.0.

* Thu Sep 14 2006 José Matos <jamatos[AT]fc.up.pt> - 1.5-4
- Rebuild for FC6.

* Sun Jun  4 2006 José Matos <jamatos[AT]fc.up.pt> - 1.5-3
- Rebuild for R-2.3.x

* Wed Mar 08 2006 José Matos <jamatos[AT]fc.up.pt> 1.5-2
- Rename License to GPL only, add gfortran as BR, add DESCRIPTION to %%doc

* Fri Mar 03 2006 José Matos <jamatos[AT]fc.up.pt> 1.5-1
- Initial package creation
