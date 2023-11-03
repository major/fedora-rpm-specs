%bcond_with bootstrap

%global packname processx
%global packver  3.8.2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Execute and Control System Processes

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-ps >= 1.2.0, R-R6, R-utils
# Suggests:  R-callr >= 3.7.3, R-cli >= 3.3.0, R-codetools, R-covr, R-curl, R-debugme, R-parallel, R-rlang >= 1.0.2, R-testthat >= 3.0.0, R-webfakes, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-ps >= 1.2.0
BuildRequires:    R-R6
BuildRequires:    R-utils
%if %{without bootstrap}
BuildRequires:    R-callr >= 3.7.3
BuildRequires:    R-cli >= 3.3.0
BuildRequires:    R-codetools
BuildRequires:    R-curl
BuildRequires:    R-debugme
BuildRequires:    R-parallel
BuildRequires:    R-rlang >= 1.0.2
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-webfakes
BuildRequires:    R-withr
%endif

%description
Tools to run system processes in the background. It can check if a
background process is running; wait on a background process to finish; get
the exit status of finished processes; kill background processes. It can
read the standard output and error of the processes, using non-blocking
connections. 'processx' can poll a process for standard output or error,
with a timeout. It can also poll several processes at once.


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

# FIXME: Why does this not install?
install -pm 0644 %{packname}/README.md %{buildroot}%{rlibdir}/%{packname}/


%check
%if %{without bootstrap}
%{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/README.md
%doc %{rlibdir}/%{packname}/CODE_OF_CONDUCT.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/bin
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/libs/client.so


%changelog
%autochangelog
