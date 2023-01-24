%global packname gamlss.dist
%global packver  6.0-5
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          6.0.5
Release:          %autorelease
Summary:          Distributions for Generalized Additive Models for Location Scale and Shape

License:          GPLv2 or GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-MASS, R-graphics, R-stats, R-methods, R-grDevices
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel >= 3.5.0
BuildRequires:    tex(latex)
BuildRequires:    R-MASS
BuildRequires:    R-graphics
BuildRequires:    R-stats
BuildRequires:    R-methods
BuildRequires:    R-grDevices

%description
A set of distributions which can be used for modelling the response variables
in Generalized Additive Models for Location Scale and Shape, Rigby and
Stasinopoulos (2005), <doi:10.1111/j.1467-9876.2005.00510.x>. The distributions
can be continuous, discrete or mixed distributions. Extra distributions can be
created, by transforming, any continuous distribution defined on the real line,
to a distribution defined on ranges 0 to infinity or 0 to 1, by using a "log"
or a "logit" transformation respectively.


%prep
%setup -q -c -n %{packname}

# Fix permissions.
chmod -x \
    %{packname}/NAMESPACE %{packname}/R/*.R \
    %{packname}/man/*.Rd %{packname}/src/ST3.?


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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%doc %{rlibdir}/%{packname}/Distributions-2010.pdf


%changelog
%autochangelog
