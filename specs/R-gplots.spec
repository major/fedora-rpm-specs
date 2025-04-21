%global packname gplots
%global packver  3.2.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Various R Programming Tools for Plotting Data

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:          GPL-2.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-gtools, R-stats, R-caTools, R-KernSmooth, R-methods
# Suggests:  R-grid, R-MASS, R-knitr, R-r2d2
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-gtools
BuildRequires:    R-stats
BuildRequires:    R-caTools
BuildRequires:    R-KernSmooth
BuildRequires:    R-methods
BuildRequires:    R-grid
BuildRequires:    R-MASS
BuildRequires:    R-knitr
# Not in Fedora
# BuildRequires:  R-r2d2

%description
Various R programming tools for plotting data, including:
- calculating and plotting locally smoothed summary function,
- enhanced versions of standard plots,
- manipulating colors,
- calculating and plotting two-dimensional data summaries,
- enhanced regression diagnostic plots,
- formula-enabled interface to 'stats::lowess' function,
- displaying textual data in plots,
- plotting a matrix where each cell contains a dot whose size reflects the
  relative magnitude of the elements,
- plotting "Venn" diagrams,
- displaying Open-Office style plots,
- plotting multiple data on same region, with separate axes,
- plotting means and confidence intervals,
- spacing points in an x-y plot so they don't overlap.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/venn.Rnw


%changelog
%autochangelog
