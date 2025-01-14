%global packname stringdist
%global packver  0.9.15
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Approximate String Matching, Fuzzy Text Search, and String Distance Functions

License:          GPL-3.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-parallel
# Suggests:  R-tinytest
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-parallel
BuildRequires:    R-tinytest

%description
Implements an approximate string matching version of R's native 'match'
function. Also offers fuzzy text search based on various string distance
measures. Can calculate various string distances based on edits
(Damerau-Levenshtein, Hamming, Levenshtein, optimal sting alignment), qgrams
(q-gram, cosine, jaccard distance) or heuristic metrics (Jaro, Jaro-Winkler).
An implementation of soundex is provided as well. Distances can be computed
between character vectors while taking proper care of encoding or between
integer vectors representing generic sequences. This package is built for speed
and runs in parallel by using 'openMP'. An API for C or C++ is exposed as well.
Reference: MPJ van der Loo (2014) <doi:10.32614/RJ-2014-011>.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Seems useless.
rm %{buildroot}%{rlibdir}/%{packname}/include/Doxyfile


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/tinytest

%files devel
%{rlibdir}/%{packname}/include


%changelog
%autochangelog
