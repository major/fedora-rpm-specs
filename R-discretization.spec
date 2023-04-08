%bcond_without check

%global packname discretization
%global rlibdir  %{_datadir}/R/library
%global ver 1.0-1.1

Name:             R-%{packname}
Version:          1.0.1.1
Release:          1%{?dist}
License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source:           %{url}&version=%{ver}#/%{packname}_%{ver}.tar.gz
Summary:          Data Preprocessing, Discretization for Classification

BuildRequires:    R-devel, tex(latex)

BuildArch:        noarch

%description
A collection of supervised discretization algorithms. It can also
be grouped in terms of top-down or bottom-up, implementing
the discretization algorithms.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%if %{with check}
export LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help

%changelog
* Wed Apr 5 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.0.1.1-1
- Initial package
