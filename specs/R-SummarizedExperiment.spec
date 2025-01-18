%global packname SummarizedExperiment
%global packver 1.26.1

%global __suggests_exclude ^R\\((AnnotationDbi|BiocStyle|GenomicFeatures|HDF5Array|TxDb\\.Hsapiens\\.UCSC\\.hg19\\.knownGene|airway|annotate|hgu95av2\\.db|rhdf5)\\)

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{packver}.tar.gz
License:          Artistic-2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/%{packname}.html
Summary:          SummarizedExperiment container
BuildRequires:    R-devel >= 4.0.0, texlive-latex, R-methods, R-MatrixGenerics >= 1.1.3, R-GenomicRanges >= 1.41.5, R-Biobase
BuildRequires:    R-DelayedArray >= 0.15.10, R-utils, R-stats, R-tools, R-Matrix, R-BiocGenerics >= 0.37.0
BuildRequires:    R-S4Vectors-devel >= 0.27.12, R-IRanges-devel >= 2.23.9, R-GenomeInfoDb >= 1.13.1
BuildArch:        noarch

%description
The SummarizedExperiment container contains one or more assays, each
represented by a marix-like object of numeric or other mode. The rows
typically represent genomic ranges of interest and the columns represent
samples.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_datadir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/R.css

%check
# Too many missing deps
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/NEWS
%{_datadir}/R/library/%{packname}/doc
%{_datadir}/R/library/%{packname}/extdata
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/scripts
%{_datadir}/R/library/%{packname}/unitTests

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.26.1-8
- R-maint-sig mass rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 1.26.1-7
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.26.1-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 03 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.26.1-1
- R 4.2.1, update to 1.26.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.22.0-1
- update to 1.22.0
- Rebuilt for R 4.1.0

* Thu Feb  4 2021 Tom Callaway <spot@fedoraproject.org> - 1.20.0-1
- update to 1.20.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.18.1-1
- update to 1.18.1
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16.0-2
- Exclude Suggests for unavailable packages

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 1.16.0-1
- update to 1.16.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10.1-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.10.1-1
- update to 1.10.1

* Fri Mar 23 2018 Tom Callaway <spot@fedoraproject.org> - 1.8.1-1
- update to 1.8.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.6.3-1
- initial package

