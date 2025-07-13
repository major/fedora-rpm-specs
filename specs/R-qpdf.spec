%global packname  qpdf
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.4.1
Release:          %autorelease
Summary:          Split, Combine and Compress PDF Files

License:          Apache-2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Patch0001:        0001-Don-t-download-files-during-build.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp, R-askpass, R-curl
# Suggests:  R-testthat
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel
BuildRequires:    R-askpass
BuildRequires:    R-curl
BuildRequires:    qpdf-devel >= 8.1.0
BuildRequires:    R-testthat

%description
Content-preserving transformations transformations of PDF files such as split,
combine, and compress. This package interfaces directly to the 'qpdf' C++ API
and does not require any command line utilities. Note that 'qpdf' does not read
actual content from PDF files: to extract text and data you need the 'pdftools'
package.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch -P0001 -p1

# Remove bundled libqpdf to be sure it's not used.
rm -r src/{include,libqpdf}
popd


%build


%install
export EXTERNAL_QPDF=yes

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
%autochangelog
