# Not packaged in Fedora:
# python-distance
%bcond distance 0

%global forgeurl https://github.com/orsinium/textdistance
%global tag %{version}

Name:           python-textdistance
Version:        4.6.0
Release:        %autorelease
Summary:        Compute distance between the two texts

%forgemeta

# SPDX
License:        MIT
URL:            %{forgeurl}
# The PyPI sdist lacks tests, so we must use the GitHub archive.
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
# For running tests in parallel:
BuildRequires:  %{py3_dist pytest-xdist}

%global _description %{expand:
TextDistance - python library for comparing distance between two or more
sequences by many algorithms.

Features:

  • 30+ algorithms
  • Pure python implementation
  • Simple usage
  • More than two sequences comparing
  • Some algorithms have more than one implementation in one class.
  • Optional numpy usage for maximum speed.}

%description %{_description}


%package -n     python3-textdistance
Summary:        %{summary}

%description -n python3-textdistance %{_description}


# Both “common” and “extra” are equivalent to ”extras”, and are provided for
# backward compatibility and to handle typos, respectively.
%pyproject_extras_subpkg -n python3-textdistance extras common extra
%pyproject_extras_subpkg -n python3-textdistance DamerauLevenshtein
%if %{with distance}
%pyproject_extras_subpkg -n python3-textdistance Hamming
%endif
%pyproject_extras_subpkg -n python3-textdistance Jaro
%pyproject_extras_subpkg -n python3-textdistance JaroWinkler
%pyproject_extras_subpkg -n python3-textdistance Levenshtein
# We don’t choose to provide a metapackage for the “benchmark”/“benchmarks”
# extra; besides missing dependencies, we think that it is akin to the “test”
# and “lint” extras in not being intended for library *users*.


%prep
%forgeautosetup

# This really doesn’t belong in the test extras!
sed -r -i 's/^([[:blank:]]*)(.*\b(isort)\b)/\1# \2/' setup.py


%generate_buildrequires
%pyproject_buildrequires -x test,Jaro,JaroWinkler,Levenshtein
%{pyproject_buildrequires \
  -x extras -x common -x extra \
  -x test \
  -x DamerauLevenshtein \
%if %{with distance}
  -x Hamming \
%endif
  -x Jaro \
  -x JaroWinkler \
  -x Levenshtein}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files textdistance


%check
%if %{without distance}
k="${k-}${k+ and }not test_compare[Hamming]"
k="${k-}${k+ and }not test_compare[Levenshtein]"
k="${k-}${k+ and }not test_list_of_numbers[Hamming]"
k="${k-}${k+ and }not test_list_of_numbers[Levenshtein]"
k="${k-}${k+ and }not test_qval[1-Hamming]"
k="${k-}${k+ and }not test_qval[1-Levenshtein]"
k="${k-}${k+ and }not test_qval[2-Hamming]"
k="${k-}${k+ and }not test_qval[2-Levenshtein]"
k="${k-}${k+ and }not test_qval[3-Hamming]"
k="${k-}${k+ and }not test_qval[3-Levenshtein]"
k="${k-}${k+ and }not test_qval[None-Hamming]"
k="${k-}${k+ and }not test_qval[None-Levenshtein]"
%endif
%if %{without pdl}
k="${k-}${k+ and }not test_compare[DamerauLevenshtein]"
k="${k-}${k+ and }not test_list_of_numbers[DamerauLevenshtein]"
k="${k-}${k+ and }not test_qval[1-DamerauLevenshtein]"
k="${k-}${k+ and }not test_qval[2-DamerauLevenshtein]"
k="${k-}${k+ and }not test_qval[3-DamerauLevenshtein]"
k="${k-}${k+ and }not test_qval[None-DamerauLevenshtein]"
%endif
%pytest -v -k "${k-}" -n auto


%files -n python3-textdistance -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
