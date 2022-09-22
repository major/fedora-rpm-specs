# a test fails, a vignette uses Internet
%bcond_with check

%global packname sass
%global packver  0.4.2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Syntactically Awesome Style Sheets (Sass)

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Unbundle-libsass.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-fs, R-rlang >= 0.4.10, R-htmltools >= 0.5.1, R-R6, R-rappdirs
# Suggests:  R-testthat, R-knitr, R-rmarkdown, R-withr, R-shiny, R-curl
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-fs
BuildRequires:    R-rlang >= 0.4.10
BuildRequires:    R-htmltools >= 0.5.1
BuildRequires:    R-R6
BuildRequires:    R-rappdirs
%if %{with check}
BuildRequires:    R-testthat
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-withr
BuildRequires:    R-shiny
BuildRequires:    R-curl
%endif
BuildRequires:    pkgconfig(libsass) >= 3.6.4

%description
An SCSS compiler, powered by the LibSass library. With this, R developers can
use variables, inheritance, and functions to generate dynamic style sheets. The
package uses the Sass CSS extension language, which is stable, powerful, and
CSS compatible.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1
rm -r src/libsass
sed -i '/src\/libsass/d' MD5
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with check}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples --no-vignettes --no-tests
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/sass-color
%{rlibdir}/%{packname}/sass-font
%{rlibdir}/%{packname}/sass-size
%{rlibdir}/%{packname}/sass-theme


%changelog
%autochangelog
