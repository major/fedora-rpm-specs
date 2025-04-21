%global packname sfsmisc
%global packver  1.1
%global packrev  20
%global rlibdir  %{_datadir}/R/library

%bcond_with suggests

Name:             R-%{packname}
Version:          %{packver}.%{packrev}
Release:          %autorelease
Summary:          Utilities from 'Seminar fuer Statistik' ETH Zurich

License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrev}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-grDevices, R-utils, R-stats, R-tools
# Suggests:  R-datasets, R-tcltk, R-cluster, R-lattice, R-MASS, R-Matrix, R-nlme, R-lokern, R-Rmpfr, R-gmp
# LinkingTo:
# Enhances:

BuildArch:        noarch
Suggests:         procps-ng
BuildRequires:    procps-ng
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-grDevices
BuildRequires:    R-utils
BuildRequires:    R-stats
BuildRequires:    R-tools
%if %{with suggests}
BuildRequires:    R-datasets
BuildRequires:    R-tcltk
BuildRequires:    R-cluster
BuildRequires:    R-lattice
BuildRequires:    R-MASS
BuildRequires:    R-Matrix
BuildRequires:    R-nlme
BuildRequires:    R-lokern
BuildRequires:    R-Rmpfr
BuildRequires:    R-gmp
%endif

%description
Useful utilities ['goodies'] from Seminar fuer Statistik ETH Zurich, some
of which were ported from S-plus in the 1990s. For graphics, have pretty
(Log-scale) axes, an enhanced Tukey-Anscombe plot, combining histogram and
boxplot, 2d-residual plots, a 'tachoPlot()', pretty arrows, etc. For
robustness, have a robust F test and robust range(). For system support,
notably on Linux, provides 'Sys.*()' functions with more access to system
and CPU information. Finally, miscellaneous utilities such as simple
efficient prime numbers, integer codes, Duplicated(), toLatex.numeric() and
is.whole().


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
%if %{with suggests}
%{_bindir}/R CMD check --no-examples %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check --no-examples --no-vignettes %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo


%changelog
%autochangelog
