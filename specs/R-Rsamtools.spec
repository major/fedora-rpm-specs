%global packname  Rsamtools
%global rlibdir %{_libdir}/R/library

%global __suggests_exclude ^R\\((BSgenome\\.Hsapiens\\.UCSC\\.hg19|BiocStyle|GenomicFeatures|KEGG\\.db|RNAseqData\\.HNRNPC\\.bam\\.chr14|ShortRead|TxDb\\.Dmelanogaster\\.UCSC\\.dm3\\.ensGene|TxDb\\.Hsapiens\\.UCSC\\.hg18\\.knownGene|graph)\\)

Name:             R-%{packname}
Version:          2.24.0
Release:          %autorelease
Summary:          R interface to samtools
License:          Artistic-2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/Rsamtools.html
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:    R-devel >= 3.5.0 tex(latex) R-methods R-IRanges-devel >= 2.13.12
BuildRequires:    R-GenomicRanges >= 1.31.8 R-Biostrings-devel >= 2.47.6
BuildRequires:    R-BiocGenerics >= 0.25.1 R-bitops R-XVector-devel >= 0.19.7
BuildRequires:    R-Rhtslib-devel >= 3.3.1 R-GenomeInfoDb >= 1.1.3
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
%autochangelog
