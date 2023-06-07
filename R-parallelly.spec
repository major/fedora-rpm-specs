%global packname parallelly
%global packver  1.36.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Enhancing the 'parallel' Package

License:          LGPL-2.1-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-parallel, R-tools, R-utils
# Suggests:
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-parallel
BuildRequires:    R-tools
BuildRequires:    R-utils

%description
Utility functions that enhance the 'parallel' package and support the
built-in parallel backends of the 'future' package.  For example,
availableCores() gives the number of CPU cores available to your R process
as given by the operating system, 'cgroups' and Linux containers, R
options, and environment variables, including those set by job schedulers
on high-performance compute clusters. If none is set, it will fall back to
parallel::detectCores(). Another example is makeClusterPSOCK(), which is
backward compatible with parallel::makePSOCKcluster() while doing a better
job in setting up remote cluster workers without the need for configuring
the firewall to do port-forwarding to your local computer.


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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST


%changelog
%autochangelog
