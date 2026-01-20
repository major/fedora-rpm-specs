Name:           R-stringdist
Version:        %R_rpm_version 0.9.17
Release:        %autorelease
Summary:        Approximate String Matching, Fuzzy Text Search, and String Distance Functions

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.9.15

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

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
