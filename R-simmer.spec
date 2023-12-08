%global packname simmer
%global rlibdir %{_libdir}/R/library

%global __suggests_exclude ^R\\((rticles|simmer\\.plot)\\)

Name:           R-%{packname}
Version:        4.4.6.3
Release:        %autorelease
Summary:        Discrete-Event Simulation for R

License:        GPL-2.0-or-later
URL:            https://cran.r-project.org/package=%{packname}
Source0:        %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

BuildRequires:  R-devel >= 3.1.2
BuildRequires:  R-Rcpp-devel >= 0.12.9
BuildRequires:  R-magrittr, R-testthat
# BuildRequires:  R-knitr, R-rmarkdown, R-rticles, R-simmer.plot

%description
A process-oriented and trajectory-based Discrete-Event Simulation (DES)
package for R. It is designed as a generic yet powerful framework. The
architecture encloses a robust and fast simulation core written in 'C++'
with automatic monitoring capabilities. It provides a rich and flexible R
API that revolves around the concept of trajectory, a common path in the
simulation model for entities of the same type.
Documentation about 'simmer' is provided by several vignettes included in
this package, via the paper by Ucar, Smeets & Azcorra (2019,
<doi:10.18637/jss.v090.i02>), and the paper by Ucar, Hernández, Serrano &
Azcorra (2018, <doi:10.1109/MCOM.2018.1700960>); see 'citation("simmer")'
for details.

%package devel
Summary:        Development Files for R-%{packname}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       R-core-devel%{?_isa}

%description devel
Header files for %{packname}.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
export LANG=C.UTF-8
export _R_CHECK_FORCE_SUGGESTS_=0
%{_bindir}/R CMD check --no-manual --ignore-vignettes %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

%files devel
%{rlibdir}/%{packname}/include

%changelog
%autochangelog
