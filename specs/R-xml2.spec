%global packname xml2
%global packver  1.4.0
%global rlibdir  %{_libdir}/R/library

%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Parse XML

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   cli, methods, rlang (≥ 1.1.0)
# Suggests:  	covr, curl, httr, knitr, magrittr, mockery, rmarkdown, testthat (≥ 3.2.0), xslt
# LinkingTo:
# Enhances:

BuildRequires:    libxml2-devel
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli
BuildRequires:    R-methods
BuildRequires:    R-rlang >= 1.1.0
BuildRequires:    R-testthat >= 3.2.0
%if %{with_suggests}
BuildRequires:    R-curl
BuildRequires:    R-httr
BuildRequires:    R-knitr
BuildRequires:    R-magrittr
BuildRequires:    R-mockery
BuildRequires:    R-rmarkdown
BuildRequires:    R-xslt
%endif

%description
Work with XML files using a simple, consistent interface. Built on top of
the 'libxml2' C library.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
# Examples use the network.
%if %{with_suggests}
%{_bindir}/R CMD check %{packname} --no-examples
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes --no-examples --no-tests
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
# not actually a license text
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%files devel
%{rlibdir}/%{packname}/include


%changelog
%autochangelog
