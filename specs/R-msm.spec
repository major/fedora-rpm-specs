%global packname msm

%global __suggests_exclude ^R\\((flexsurv|minqa|mstate|numDeriv)\\)

Name:             R-%{packname}
Version:          1.8.2
Release:          %autorelease
# Automatically converted from old format: GPLv2+ and GPLv3+ - review is highly recommended.
License:          GPL-2.0-or-later AND GPL-3.0-or-later
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Summary:          Multi-state Markov and hidden Markov models in continuous time
BuildRequires:    R-devel >= 3.4.0, tetex-latex
BuildRequires:    R-mvtnorm-devel, R-survival, R-expm, R-generics, R-tibble

%description
Functions for fitting general continuous-time Markov and hidden Markov
multi-state models to longitudinal data.  Both Markov transition rates
and the hidden Markov output process can be modeled in terms of
covariates.  A variety of observation schemes are supported, including
processes observed at arbitrary times, completely-observed processes,
and censored states.

%prep
%setup -q -c -n %{packname}
# Fix some permissions and formats
# find . -type f -perm 755 -exec chmod 644 {} \;
find . -type f -name '*.[hc]' -exec chmod 644 {} \;

# Fix the encoding of the NEWS file
chmod 644 %{packname}/inst/NEWS
iconv -f ISO88591 -t UTF8 -o NEWS %{packname}/inst/NEWS
mv -f NEWS %{packname}/inst

%build

%install
# Specific installation procedure for R
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

# Remove the temporary object files
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)

# Remove the generic cascading style sheet for R
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css


%check
# check needs a lot.
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/CITATION
%doc %{_libdir}/R/library/%{packname}/data
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/NEWS.md
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/%{packname}.so

%changelog
%autochangelog
