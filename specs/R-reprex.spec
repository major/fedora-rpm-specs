%global packname reprex
%global packver  2.1.1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Prepare Reproducible Example Code via the Clipboard

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Fix test with lifecycle 1.0.3+
# https://github.com/tidyverse/reprex/pull/434
#Patch0:           R-reprex-fix-test-lifecycle-1.0.3.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-callr >= 3.6.0, R-cli >= 3.2.0, R-clipr >= 0.4.0, R-fs, R-glue, R-knitr >= 1.23, R-lifecycle, R-rlang >= 1.0.0, R-rmarkdown, R-rstudioapi, R-utils, R-withr >= 2.3.0
# Suggests:  R-covr, R-fortunes, R-miniUI, R-mockr, R-rprojroot, R-sessioninfo, R-shiny, R-spelling, R-styler >= 1.2.0, R-testthat >= 3.0.2
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         pandoc >= 1.12.3
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    pandoc >= 1.12.3
BuildRequires:    R-callr >= 3.6.0
BuildRequires:    R-cli >= 3.2.0
BuildRequires:    R-clipr >= 0.4.0
BuildRequires:    R-fs
BuildRequires:    R-glue
BuildRequires:    R-knitr >= 1.23
BuildRequires:    R-lifecycle >= 1.0.3
BuildRequires:    R-rlang >= 1.0.3
BuildRequires:    R-rmarkdown
BuildRequires:    R-rstudioapi
BuildRequires:    R-utils
BuildRequires:    R-withr >= 2.3.0
BuildRequires:    R-fortunes
BuildRequires:    R-miniUI
BuildRequires:    R-mockr
BuildRequires:    R-rprojroot
BuildRequires:    R-sessioninfo
BuildRequires:    R-shiny
BuildRequires:    R-spelling
BuildRequires:    R-styler >= 1.2.0
BuildRequires:    R-testthat >= 3.2.1

%description
Convenience wrapper that uses the 'rmarkdown' package to render small snippets
of code to target formats that include both code and output. The goal is to
encourage the sharing of small, reproducible, and runnable examples on
code-oriented websites, such as <https://stackoverflow.com> and
<https://github.com>, or in email. The user's clipboard is the default source
of input code and the default target for rendered output. 'reprex' also
extracts clean, runnable R code from various common formats, such as copy/paste
from an R session.


%prep
%setup -q -c -n %{packname}
#%%patch -P0 -p1 -b .fixme

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/addins
%{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/templates


%changelog
%autochangelog
