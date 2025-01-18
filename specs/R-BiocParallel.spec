%global packname  BiocParallel

%global __suggests_exclude ^R\\((BBmisc|BatchJobs|BiocStyle|RNAseqData\\.HNRNPC\\.bam\\.chr14|Rmpi|ShortRead|TxDb\\.Hsapiens\\.UCSC\\.hg19\\.knownGene|VariantAnnotation|batchtools)\\)

Name:             R-%{packname}
Version:          1.30.3
Release:          10%{?dist}
Summary:          Bioconductor facilities for parallel evaluation
# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License:          GPL-2.0-only OR GPL-3.0-only
URL:              http://www.bioconductor.org/packages/release/bioc/html/BiocParallel.html
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         texlive-latex
# Depends
BuildRequires:    R-devel >= 3.5.0, R-methods
# Imports
BuildRequires:    R-stats, R-utils, R-futile.logger, R-parallel, R-snow, R-codetools
# LinkingTo
BuildRequires:    R-BH-devel
BuildRequires:    gcc, gcc-c++
BuildRequires:    autoconf automake

%description
This package provides modified versions and novel implementation of functions
for parallel evaluation, tailored to use with Bioconductor objects.

%prep
%setup -c -q -n %{packname}
chmod -x BiocParallel/inst/snow/RMPInode.R
pushd %{packname}
autoreconf -ifv
popd

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

%check
# All sorts of missing Suggests prevents this from working.
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/doc/
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/unitTests/
%{_libdir}/R/library/%{packname}/*.sh
%{_libdir}/R/library/%{packname}/snow/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Miroslav Suchý <msuchy@redhat.com> - 1.30.3-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.30.3-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.30.3-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 1.30.3-1
- update to 1.30.3
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.26.0-1
- update to 1.26.0
- Rebuilt for R 4.1.0

* Wed Feb  3 2021 Tom Callaway <spot@fedoraproject.org> - 1.24.1-1
- update to 1.24.1

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.22.0-1
- update to 1.22.0
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.20.0-2
- Exclude Suggests for unavailable packages

* Tue Nov  5 2019 Tom Callaway <spot@fedoraproject.org> - 1.20.0-1
- update to 1.20.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16.5-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb  6 2019 Tom Callaway <spot@fedoraproject.org> - 1.16.5-1
- update to 1.16.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.14.1-1
- update to 1.14.1

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 1.12.0-1
- update to 1.12.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.10.1-1
- initial package
