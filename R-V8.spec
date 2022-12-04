%global packname V8
%global packver  4.2.2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          4.2.2
Release:          %autorelease
Summary:          Embedded JavaScript and WebAssembly Engine for R

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# nodejs does not build on all arches
ExclusiveArch:    %{nodejs_arches}

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp >= 0.12.12, R-jsonlite >= 1.0, R-curl >= 1.0, R-utils
# Suggests:  R-testthat, R-knitr, R-rmarkdown
# LinkingTo:
# Enhances:

Requires:         js-underscore
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    v8-devel
BuildRequires:    web-assets-devel
BuildRequires:    js-underscore
BuildRequires:    R-Rcpp-devel >= 0.12.12
BuildRequires:    R-jsonlite >= 1.0
BuildRequires:    R-curl >= 1.0
BuildRequires:    R-utils
BuildRequires:    R-testthat
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    glyphicons-halflings-fonts

# This is not packaged and it's only used to make sure example docs build when
# offline anyway.
Provides:         bundled(js-crossfilter) = 1.3.12

%description
An R interface to V8: Google's open source JavaScript and WebAssembly engine.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Replace bundled copy with symlink to packaged version (note that this cannot
# be done in prep because R CMD INSTALL copies symlink targets.)
ln -sf %{_jsdir}/underscore/underscore-min.js \
    %{buildroot}%{rlibdir}/%{packname}/js/underscore.js


%check
export LANG=C.UTF-8
# Vignettes use the network.
%{_bindir}/R CMD check %{packname} --ignore-vignettes


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/js
%{rlibdir}/%{packname}/wasm
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
%autochangelog
