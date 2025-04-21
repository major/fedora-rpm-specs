%global packname  RUnit
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.4.32
Release:          %autorelease
Summary:          R Unit test framework

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:          GPL-2.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Patch0:           R-RUnit-0.4.25-no-buildroot-path-in-html.patch

# Here's the R view of the dependencies world:
# Depends:   R-utils >= 2.5.0, R-methods >= 2.5.0, R-graphics >= 2.5.0
# Imports:
# Suggests:  R-XML >= 3.1.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils >= 2.5.0
BuildRequires:    R-methods >= 2.5.0
BuildRequires:    R-graphics >= 2.5.0
# BuildRequires:    R-XML >= 3.1.0 # not in EPEL

%description
R functions implementing a standard Unit Testing framework, with additional
code inspection and report generation tools.


%prep
%setup -q -c -n %{packname}

%patch -P0 -p1 -b .no-buildroot-path-in-html


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export _R_CHECK_FORCE_SUGGESTS_=0
%{_bindir}/R CMD check --ignore-vignettes --no-manual %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/share
%{rlibdir}/%{packname}/unitTests


%changelog
%autochangelog
