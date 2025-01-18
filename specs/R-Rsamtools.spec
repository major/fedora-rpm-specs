%global packname  Rsamtools
%global rlibdir %{_libdir}/R/library

%global __suggests_exclude ^R\\((BSgenome\\.Hsapiens\\.UCSC\\.hg19|BiocStyle|GenomicFeatures|KEGG\\.db|RNAseqData\\.HNRNPC\\.bam\\.chr14|ShortRead|TxDb\\.Dmelanogaster\\.UCSC\\.dm3\\.ensGene|TxDb\\.Hsapiens\\.UCSC\\.hg18\\.knownGene|graph)\\)

Name:             R-%{packname}
Version:          2.18.0
Release:          3%{dist}
Summary:          R interface to samtools
License:          Artistic-2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/Rsamtools.html
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Patch0:           0001-format-security-fix.patch
BuildRequires:    R-devel >= 3.5.0 tex(latex) R-methods R-IRanges-devel >= 2.13.12
BuildRequires:    R-GenomicRanges >= 1.31.8 R-Biostrings-devel >= 2.47.6
BuildRequires:    R-BiocGenerics >= 0.25.1 R-bitops R-XVector-devel >= 0.19.7
BuildRequires:    R-Rhtslib-devel >= 1.17.7 R-GenomeInfoDb >= 1.1.3
BuildRequires:    R-S4Vectors-devel >= 0.17.25 R-utils R-BiocParallel R-stats
BuildRequires:    libcurl-devel
Provides:         R-Rsamtools-devel = %{version}-%{release}
Obsoletes:        R-Rsamtools-devel <= 1.34.1

%description
This package provides an interface to the 'samtools', 'bcftools',
and 'tabix' utilities (see 'LICENCE') for manipulating SAM
(Sequence Alignment / Map), binary variant call (BCF) and
compressed indexed tab-delimited (tabix) files.

%prep
%setup -q -c -n %{packname}
pushd %{packname}
%patch -P0 -p1
popd

sed -i 's|zlibbioc, ||g' %{packname}/DESCRIPTION
sed -i '/import(zlibbioc)/d' %{packname}/NAMESPACE

%build

%install
mkdir -p %{buildroot}%{rlibdir}
R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
# Testing tests optional deps we don't package
# _R_CHECK_FORCE_SUGGESTS_=false %%{_bindir}/R CMD check %%{packname}

%files
%dir %{rlibdir}/%{packname}/
%doc %{rlibdir}/%{packname}/doc/
%doc %{rlibdir}/%{packname}/html/
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta/
%{rlibdir}/%{packname}/R/
%{rlibdir}/%{packname}/extdata/
%{rlibdir}/%{packname}/help/
%{rlibdir}/%{packname}/scripts/
%{rlibdir}/%{packname}/unitTests/
%{rlibdir}/%{packname}/libs/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.18.0-1
- Update to latest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.12.0-8
- R-maint-sig mass rebuild

* Sat Apr  20 2024 Miroslav Suchý <msuchy@redhat.com> - 2.12.0-7
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.12.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 2.12.0-1
- update to 2.12.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 2.8.0-1
- update to 2.8.0
- Rebuilt for R 4.1.0

* Thu Feb  4 2021 Tom Callaway <spot@fedoraproject.org> - 2.6.0-1
- update to 2.6.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 2.4.0-1
- update to 2.4.0
- rebuild for R 4

* Wed Feb  5 2020 Tom Callaway <spot@fedoraproject.org> - 2.2.1-1
- update to 2.2.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.3-2
- Exclude Suggests for unavailable packages

* Wed Oct 30 2019 Tom Callaway <spot@fedoraproject.org> - 2.0.3-1
- update to 2.03 (devel package dies off)

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.34.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb  7 2019 Tom Callaway <spot@fedoraproject.org> - 1.34.1-1
- update to 1.34.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.32.0-1
- update to 1.32.0

* Fri Mar 23 2018 Tom Callaway <spot@fedoraproject.org> - 1.30.0-1
- update to 1.30.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.28.0-1
- update to 1.28.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Tom Callaway <spot@fedoraproject.org> - 1.20.2-1
- update to 1.20.2
- fix DESCRIPTION to not be doc
- add -static provide (bz 967213)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.16.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 19 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.16.0-2
- Rebuild to fix debuginfo (#1113404)

* Mon Jun  9 2014 Tom Callaway <spot@fedoraproject.org> - 1.16.0-1
- update to 1.16.0

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Tom Callaway <spot@fedoraproject.org> - 1.14.2-1
- update to 1.14.2

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 1.12.0-1
- update to 1.12.0

* Fri Apr  5 2013 Tom Callaway <spot@fedoraproject.org> - 1.10.2-3
- add R-bitops as a BuildRequires
- fix license tag

* Mon Apr  1 2013 Tom Callaway <spot@fedoraproject.org> - 1.10.2-2
- cleanup spec (drop unnecessary macro for exec'ing R, unnecessary BR: R)

* Fri Feb 22 2013 Tom Callaway <spot@fedoraproject.org> - 1.10.2-1
- initial package
