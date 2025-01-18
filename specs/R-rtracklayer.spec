%global packname  rtracklayer

%global __suggests_exclude ^R\\((BSgenome\\.Hsapiens\\.UCSC\\.hg19|GenomicFeatures|TxDb\\.Hsapiens\\.UCSC\\.hg19\\.knownGene|genefilter|hgu133plus2\\.db|humanStemCell|limma|microRNA|org\\.Hs\\.eg\\.db)\\)

Name:             R-%{packname}
Version:          1.62.0
Release:          4%{dist}
Summary:          R interface to genome browsers and their annotation tracks
# Automatically converted from old format: Artistic 2.0 and BSD - review is highly recommended.
License:          Artistic-2.0 AND LicenseRef-Callaway-BSD
URL:              http://www.bioconductor.org/packages/release/bioc/html/rtracklayer.html
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Source1:          rtracklayer_jimkent_license.txt
Patch0:           0001-fix-format-security.patch
Requires:         texlive-latex
BuildRequires:    R-devel >= 3.3.0, R-methods, R-RCurl >= 1.4.2, R-XML >= 1.98.0
BuildRequires:    R-IRanges-devel >= 2.13.13, R-GenomicRanges >= 1.37.2, R-Biostrings-devel >= 2.47.6
BuildRequires:    R-Rsamtools-devel >= 1.31.2, zlib-devel
BuildRequires:    R-XVector-devel >= 0.19.7, R-BiocGenerics >= 0.35.3, R-S4Vectors-devel >= 0.23.18
BuildRequires:    R-GenomeInfoDb >= 1.15.2, R-GenomicAlignments >= 1.15.6, R-tools
BuildRequires:    openssl-devel
BuildRequires:    R-BiocIO, R-restfulr >= 0.0.13

%description
Extensible framework for interacting with multiple genome browsers (currently
UCSC built-in) and manipulating annotation tracks in various formats
(currently GFF, BED, bedGraph, BED15, WIG, and BigWig built-in). The user may
export/import tracks to/from the supported browsers, as well as query and
modify the browser state, such as the current viewport.

%prep
%setup -c -q -n %{packname}
sed -i -e 's|zlibbioc,||' rtracklayer/DESCRIPTION
sed -i -e 's|import(zlibbioc)||' rtracklayer/NAMESPACE
pushd %{packname}
%patch -P0 -p1
popd

# This email confirms that we have permission to use the Jim Kent
# copyrighted files under the BSD license.
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

# Zero file
rm -rf %{buildroot}%{_libdir}/R/library/%{packname}/tests/quickload/T_species_Oct_2011/bedGraphData.bw

%check
# All sorts of missing Suggests prevents this from working.
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/CITATION
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/doc/
%license rtracklayer_jimkent_license.txt
%license %{_libdir}/R/library/%{packname}/LICENSE
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/data/
%{_libdir}/R/library/%{packname}/extdata/
%{_libdir}/R/library/%{packname}/demo/
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/notes/
%{_libdir}/R/library/%{packname}/scripts/
%{_libdir}/R/library/%{packname}/tests/
%{_libdir}/R/library/%{packname}/unitTests/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.62.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.62.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.62.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.62.0-1
- Update to latest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.56.1-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.56.1-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 04 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.56.1-1
- R 4.2.1, update to 1.56.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.52.0-3
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 1.52.0-1
- update to 1.52.0
- Rebuilt for R 4.1.0

* Thu Feb  4 2021 Tom Callaway <spot@fedoraproject.org> - 1.50.0-1
- update to 1.50.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.48.0-1
- update to 1.48.0
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.46.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.46.0-2
- Exclude Suggests for unavailable packages

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 1.46.0-1
- update to 1.46.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.44.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun  7 2019 Tom Callaway <spot@fedoraproject.org> - 1.44.0-1
- update to 1.44.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1.40.2-1
- update to 1.40.2

* Fri Mar 23 2018 Tom Callaway <spot@fedoraproject.org> - 1.38.3-1
- update to 1.38.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.36.3-1
- update to 1.36.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 11 2016 pingou <pingou@pingoured.fr> 1.30.2-1
- Update to version 1.30.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 03 2015 pingou <pingou@pingoured.fr> 1.28.6-1
- Update to version 1.28.6

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.22.3-4
- Add missing BR: R-XVector-devel (#1105923)

* Thu Jul 03 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.22.3-3
- Drop the patch fixing the zlibbioc import/dependency in favor of a couple of
  sed commands

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb  3 2014 Tom Callaway <spot@fedoraproject.org> - 1.22.3-1
- update to 1.22.3

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 1.20.0-1
- update to 1.20.0

* Fri Feb 22 2013 Tom Callaway <spot@fedoraproject.org> - 1.18.2-1
- update to 1.18.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Tom Callaway <spot@fedoraproject.org> 1.14.1-2
- update licensing with clarification from Jim Kent

* Thu Nov 10 2011 Tom "spot" Callaway <tcallawa@redhat.com> 1.14.1-1
- initial package for Fedora
