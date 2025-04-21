%global packname statnet.common
%global packver  4.11.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Common R Scripts and Utilities Used by the Statnet Project Software

License:          GPL-3.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-utils, R-methods, R-coda, R-parallel, R-tools
# Suggests:  R-covr, R-rlang >= 1.1.1, R-MASS, R-Matrix
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils
BuildRequires:    R-methods
BuildRequires:    R-coda
BuildRequires:    R-parallel
BuildRequires:    R-tools
BuildRequires:    R-rlang >= 1.1.1
BuildRequires:    R-MASS
BuildRequires:    R-Matrix

%description
Non-statistical utilities used by the software developed by the Statnet
Project. They may also be of use to others.


%prep
%setup -q -c -n %{packname}

sed -i '/covr/d' %{packname}/DESCRIPTION

# Duplicate of NEWS.
rm %{packname}/NEWS.md


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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/CITATION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/templates


%changelog
%autochangelog
