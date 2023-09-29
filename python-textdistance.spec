# Not packaged in Fedora:
# python-abydos
%bcond abydos 0
# python-distance
%bcond distance 0
# python-pyxDamerauLevenshtein
%bcond pdl 0

%global forgeurl https://github.com/orsinium/textdistance
%global tag %{version}

Name:           python-textdistance
Version:        4.5.0
Release:        %autorelease
Summary:        Compute distance between the two texts

%forgemeta

# SPDX
License:        MIT
URL:            %{forgeurl}
# The PyPI sdist lacks tests, so we must use the GitHub archive.
Source:         %{forgesource}

# Remove executable bit from filesystem permissions of README.md
Patch:          https://github.com/life4/textdistance/pull/85.patch
# Update URL and name for python-Levenshtein
# https://github.com/life4/textdistance/pull/86
#
# Rebased on 4.4.0; changes to constraints.txt removed so the patch will
# apply to the PyPI sdist, which lacks it
#
# It’s good in general to use the name preferred by upstream (Levenshtein
# rather than python-Levenshtein), but it’s also important because the
# python-Levenshtein package currently lacks virtual Provides for
# python3-python-Levenshtein.
Patch:          textdistance-4.4.0-pr-86.patch
# Replace deprecated license_file with license_files in setup.cfg
Patch:          https://github.com/life4/textdistance/pull/87.patch

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
%if %{with abydos} && %{with pdl}
%pyproject_extras_subpkg -n python3-textdistance extras common extra
%endif

# We don’t choose to provide a metapackage for the “benchmark”/“benchmarks”
# extra; besides missing dependencies, we think that it is akin to the “test”
# and “lint” extras in not being intended for library *users*.

%if %{with pdl}
%pyproject_extras_subpkg -n python3-textdistance DamerauLevenshtein
%endif

%if %{with abydos} && %{with distance}
%pyproject_extras_subpkg -n python3-textdistance Hamming
%endif

%pyproject_extras_subpkg -n python3-textdistance Jaro JaroWinkler Levenshtein


%prep
%forgeautosetup -p1

# This really doesn’t belong in the test extras!
sed -r -i 's/^([[:blank:]]*)(.*\b(isort)\b)/\1# \2/' setup.py


%generate_buildrequires
%pyproject_buildrequires -x test,Jaro,JaroWinkler,Levenshtein
%{pyproject_buildrequires \
  -x test \
%if %{with abydos} && %{with pdl}
  -x extras -x common -x extra \
%endif
%if %{with pdl}
  -x DamerauLevenshtein \
%endif
%if %{with abydos} && %{with distance}
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
%if %{without abydos}
k="${k-}${k+ and } not test_compare[DamerauLevenshtein]"
k="${k-}${k+ and } not test_compare[Hamming]"
k="${k-}${k+ and } not test_compare[Levenshtein]"
k="${k-}${k+ and } not test_list_of_numbers[DamerauLevenshtein]"
k="${k-}${k+ and } not test_list_of_numbers[Hamming]"
k="${k-}${k+ and } not test_list_of_numbers[Levenshtein]"
k="${k-}${k+ and } not test_qval[1-DamerauLevenshtein]"
k="${k-}${k+ and } not test_qval[1-Hamming]"
k="${k-}${k+ and } not test_qval[1-Levenshtein]"
k="${k-}${k+ and } not test_qval[2-DamerauLevenshtein]"
k="${k-}${k+ and } not test_qval[2-Hamming]"
k="${k-}${k+ and } not test_qval[2-Levenshtein]"
k="${k-}${k+ and } not test_qval[3-DamerauLevenshtein]"
k="${k-}${k+ and } not test_qval[3-Hamming]"
k="${k-}${k+ and } not test_qval[3-Levenshtein]"
k="${k-}${k+ and } not test_qval[DamerauLevenshtein]"
k="${k-}${k+ and } not test_qval[Hamming]"
k="${k-}${k+ and } not test_qval[Levenshtein]"
k="${k-}${k+ and } not test_qval[None-DamerauLevenshtein]"
k="${k-}${k+ and } not test_qval[None-Hamming]"
k="${k-}${k+ and } not test_qval[None-Levenshtein]"
%endif

%pytest -v -k "${k-}" -n auto


%files -n python3-textdistance -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
