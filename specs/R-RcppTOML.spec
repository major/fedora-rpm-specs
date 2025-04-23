%global packname RcppTOML
%global rlibdir %{_libdir}/R/library

Name:           R-%{packname}
Version:        0.2.3
Release:        %autorelease
Summary:        'Rcpp' Bindings to Parser for "Tom's Obvious Markup Language"

License:        GPL-2.0-or-later
URL:            https://cran.r-project.org/package=%{packname}
Source0:        %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

BuildRequires:  R-devel >= 3.3.0
BuildRequires:  R-Rcpp-devel >= 1.0.8
BuildRequires:  R-tinytest
BuildRequires:  tomlplusplus-devel

%description
The configuration format defined by 'TOML' (which expands to "Tom's
Obvious Markup Language") specifies an excellent format (described
at <https://toml.io/en/>) suitable for both human editing as well as
the common uses of a machine-readable format. This package uses 'Rcpp'
to connect to the 'toml++' parser written by Mark Gillard to R.

%package devel
Summary:        Development Files for R-%{packname}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       R-core-devel%{?_isa}
Requires:       tomlplusplus-devel

%description devel
Header files for %{packname}.

%prep
%setup -q -c -n %{packname}

# unbundle toml++
rm -r %{packname}/inst/include/toml++
ln -s %{_includedir}/toml++ %{packname}/inst/include/toml++

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# and again
rm -r %{buildroot}%{rlibdir}/%{packname}/include/toml++
ln -s %{_includedir}/toml++ %{buildroot}%{rlibdir}/%{packname}/include/toml++

%check
export LANG=C.UTF-8
export _R_CHECK_FORCE_SUGGESTS_=0
%{_bindir}/R CMD check --no-manual --ignore-vignettes %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/toml

%files devel
%{rlibdir}/%{packname}/include

%changelog
%autochangelog
