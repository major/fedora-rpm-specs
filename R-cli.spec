%bcond_without check

%global packname cli
%global packver  3.6.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Helpers for Developing Command Line Interfaces

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-utils
# Suggests:  R-callr, R-covr, R-crayon, R-digest, R-glue >= 1.6.0, R-grDevices, R-htmltools, R-htmlwidgets, R-knitr, R-methods, R-mockery, R-processx, R-ps >= 1.3.4.9000, R-rlang >= 1.0.2.9003, R-rmarkdown, R-rprojroot, R-rstudioapi, R-testthat, R-tibble, R-whoami, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-glue >= 1.6.0
BuildRequires:    R-utils
%if %{with check}
BuildRequires:    R-callr
BuildRequires:    R-crayon
BuildRequires:    R-digest
BuildRequires:    R-glue >= 1.6.0
BuildRequires:    R-grDevices
BuildRequires:    R-htmltools
BuildRequires:    R-htmlwidgets
BuildRequires:    R-knitr
BuildRequires:    R-methods
BuildRequires:    R-mockery
BuildRequires:    R-processx
BuildRequires:    R-ps >= 1.3.4.9000
BuildRequires:    R-rlang >= 1.0.2.9003
BuildRequires:    R-rmarkdown
BuildRequires:    R-rprojroot
BuildRequires:    R-rstudioapi
BuildRequires:    R-testthat
BuildRequires:    R-tibble
BuildRequires:    R-whoami
BuildRequires:    R-withr
%endif

%description
A suite of tools to build attractive command line interfaces ('CLIs'), from
semantic elements: headings, lists, alerts, paragraphs, etc. Supports
custom themes via a 'CSS'-like language. It also contains a number of lower
level 'CLI' elements: rules, boxes, trees, and 'Unicode' symbols with
'ASCII' alternatives. It support ANSI colors and text styles as well.


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
%if %{with check}
export LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes --no-manual %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/logo.txt
%{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/shiny


%changelog
%autochangelog
