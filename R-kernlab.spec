%global packname kernlab
%global packvers 0.9
%global packrel 31
%global rlibdir %{_libdir}/R/library

Name:		R-%{packname}
Version:	%{packvers}.%{packrel}
Release:	%autorelease
Summary:	GNU R package for kernel-based machine learning lab

License:	GPL-2.0-only
URL:		https://CRAN.R-project.org/package=%{packname}
Source:		%{url}&version=%{packvers}-%{packrel}#/%{packname}_%{packvers}-%{packrel}.tar.gz

BuildRequires:	R-devel
BuildRequires:	tex(latex)

ExcludeArch:	%{ix86} s390x

%description
Kernel-based machine learning methods for classification,
regression, clustering, novelty detection, quantile regression
and dimensionality reduction. Among other methods 'kernlab'
includes Support Vector Machines, Spectral Clustering, 
Kernel PCA, Gaussian Processes and a QP solver.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%license %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

%changelog
%autochangelog
