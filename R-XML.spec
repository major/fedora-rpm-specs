%global packname XML
%global packver  3.99-0.16.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.99.0.16.1
Release:          %autorelease
Summary:          Tools for Parsing and Generating XML Within R and S-Plus

License:          BSD-3-Clause
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods, R-utils
# Imports:
# Suggests:  R-bitops, R-RCurl
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    tex(inconsolata.sty)
BuildRequires:    R-methods
BuildRequires:    R-utils
BuildRequires:    R-bitops
BuildRequires:    R-RCurl
BuildRequires:    libxml2-devel

%description
Many approaches for both reading and creating XML (and HTML) documents
(including DTDs), both local and accessible via HTTP or FTP.  Also offers
access to an XPath "interpreter".


%prep
%setup -q -c -n %{packname}


%build


%install
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
%license %{rlibdir}/%{packname}/COPYRIGHTS
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/exampleData
%{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/FAQ.html


%changelog
%autochangelog
