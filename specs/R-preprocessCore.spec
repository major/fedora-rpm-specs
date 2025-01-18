%global packname  preprocessCore
%global Rvers     3.4.0

Name:             R-%{packname}
Version:          1.58.0
Release:          10%{dist}
Summary:          A collection of pre-processing functions
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:          LicenseRef-Callaway-LGPLv2+
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Source1:          preprocessCore_license
BuildRequires:    R-devel >= %{Rvers} tex(latex) R-stats gcc
BuildRequires:    autoconf, automake, libtool
Patch0:           R-preprocessCore-dlsym-pthread_get_minstack-fix.patch

%package           devel
Summary:           Development files for %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description
A library of core preprocessing routines

%description    devel
The %{name}-devel  package contains Header and libraries files for
developing applications that use %{name}

%prep
%setup -q -c -n %{packname}
%patch -P0 -p1 -b .dlsym
pushd %{packname}
autoreconf -ifv .
popd

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

## Keep the headers of place for the -devel
## see: https://www.redhat.com/archives/fedora-r-devel-list/2009-March/msg00001.html

install -m 664 -p %{SOURCE1}  %{buildroot}%{_libdir}/R/library/%{packname}

%check
%if 0
# 2020-09-10: sh: line 1: 1879370 Segmentation fault      (core dumped) LANGUAGE=en _R_CHECK_INTERNALS2_=1 '/usr/lib64/R/bin/R' --vanilla > 'preprocessCore-Ex.Rout' 2>&1 <
%ifnarch s390x
%{_bindir}/R CMD check %{packname}
%endif
%endif

%files
#i386 arch
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/preprocessCore_license
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/help

%files          devel
%{_libdir}/R/library/%{packname}/include/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.58.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 1.58.0-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.58.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.58.0-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.58.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.58.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.58.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.58.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.58.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Tom Callaway <spot@fedoraproject.org> - 1.58.0-1
- update to 1.58.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.54.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.54.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 1.54.0-1
- update to 1.54.0
- Rebuilt for R 4.1.0

* Thu Feb  4 2021 Tom Callaway <spot@fedoraproject.org> - 1.52.1-1
- update to 1.52.1
- disable tests

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Tom Callaway <spot@fedoraproject.org> - 1.50.0-5
- rebuild for FlexiBLAS R

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Tom Callaway <spot@fedoraproject.org> - 1.50.0-2
- use dlsym to access __pthread_get_minstack to avoid dependency issue with GLIBC_PRIVATE (bz1849669, bz1849369)

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.50.0-1
- update to 1.50.0
- rebuild for R 4

* Tue Feb 18 2020 Tom Callaway <spot@fedoraproject.org> - 1.48.0-4
- rebuild against R without libRlapack.so
- apply upstream change to love openblas

* Sat Feb  1 2020 Tom Callaway <spot@fedoraproject.org> - 1.48.0-3
- fix FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov  7 2019 Tom Callaway <spot@fedoraproject.org> - 1.48.0-1
- update to 1.48.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.42.0-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.42.0-1
- update to 1.42.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.38.1-1
- update to 1.38.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 pingou <pingou@pingoured.fr> 1.26.1-1
- Update to version 1.26.1

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May  7 2014 Tom Callaway <spot@fedoraproject.org> 1.26.0-1
- update to 1.26.0 (R 3.1.0)

* Mon Jan 27 2014 pingou <pingou@pingoured.fr> 1.24.0-1
- Update to version 1.24.0

* Sun Dec 22 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.22.0-3
- Add blas-devel and lapack-devel as BR

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 07 2013 pingou <pingou@pingoured.fr> 1.22.0-1
- Update to version 1.22.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 pingou <pingou@pingoured.fr> 1.20.0-1
- Update to version 1.20.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 pingou <pingou@pingoured.fr> 1.18.0-1
- Update to version 1.18.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Tom Callaway <spot@fedoraproject.org> 1.16.0-2
- rebuild for R 2.14.0

* Thu Nov 03 2011 pingou <pingou@pingoured.fr> 1.16.0-1
- Update to version 1.16.0

* Wed Jun 22 2011 pingou <pingou@pingoured.fr> 1.14.0-1
- Update to version 1.14.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 pingou <pingou@pingoured.fr> 1.12.0-1
- Update to version 1.12.0

* Sat Jun 05 2010 pingou <pingou@pingoured.fr> 1.10.0-1
- Update to version 1.10.0
- Update source0 and URL to a more stable form
- Update R and BR to R-core and R-devel
- Update to R-2.11.0

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 1.8.0-1
- Update to 1.8.0
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0
- Fix BR tex(latex)

* Tue Aug 04 2009 pingou <pingou@pingoured.fr> 1.6.0-2
- Add the file preprocessCore_license which contains the mail from upstream regarding the license

* Sat Aug 01 2009 pingou <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora
