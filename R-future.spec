%global packname future
%global packver  1.32.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Unified Parallel and Distributed Processing in R for Everyone

License:          LGPL-2.1-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-digest, R-globals >= 0.16.1, R-listenv >= 0.8.0, R-parallel, R-parallelly >= 1.34.0, R-utils
# Suggests:  R-methods, R-RhpcBLASctl, R-R.rsp, R-markdown
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-digest
BuildRequires:    R-globals >= 0.16.1
BuildRequires:    R-listenv >= 0.8.0
BuildRequires:    R-parallel
BuildRequires:    R-parallelly >= 1.34.0
BuildRequires:    R-utils
BuildRequires:    R-methods
BuildRequires:    R-RhpcBLASctl
BuildRequires:    R-R.rsp
BuildRequires:    R-markdown
# A test needs this
BuildRequires:    hostname

%description
The purpose of this package is to provide a lightweight and unified Future
API for sequential and parallel processing of R expression via futures.
The simplest way to evaluate an expression in parallel is to use `x %<-% {
expression }` with `plan(multisession)`. This package implements
sequential, multicore, multisession, and cluster futures.  With these, R
expressions can be evaluated on the local machine, in parallel a set of
local machines, or distributed on a mix of local and remote machines.
Extensions to this package implement additional backends for processing
futures via compute cluster schedulers, etc. Because of its unified API,
there is no need to modify any code in order switch from sequential on the
local machine to, say, distributed processing on a remote compute cluster.
Another strength of this package is that global variables and functions are
automatically identified and exported as needed, making it straightforward
to tweak existing code to make use of futures.


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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/vignettes-static
%{rlibdir}/%{packname}/WORDLIST


%changelog
%autochangelog
