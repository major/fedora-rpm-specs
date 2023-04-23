%global packname svglite
%global packver  2.1.1
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((fontquiver)\\)

%global with_suggests 0

Name:             R-%{packname}
Version:          2.1.1
Release:          %autorelease
Summary:          An 'SVG' Graphics Device

# Mainly GPL; src/tinyformat.h is Boost.
License:          GPL-2.0-or-later AND BSL-1.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-systemfonts >= 1.0.0
# Suggests:  R-covr, R-fontquiver >= 0.2.0, R-htmltools, R-knitr, R-rmarkdown, R-testthat, R-xml2 >= 1.0.0
# LinkingTo: R-cpp11, R-systemfonts
# Enhances:

BuildRequires:    libpng-devel
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-systemfonts-devel >= 1.0.0
BuildRequires:    R-cpp11-devel
BuildRequires:    R-htmltools
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
BuildRequires:    R-xml2 >= 1.0.0
%if %{with_suggests}
BuildRequires:    R-fontquiver >= 0.2.0
%endif

%description
A graphics device for R that produces 'Scalable Vector Graphics'. 'svglite'
is a fork of the older 'RSvgDevice' package.


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
export LANG=C.UTF-8
%if %{with_suggests}
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check --ignore-vignettes %{packname} --no-tests
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
%autochangelog
