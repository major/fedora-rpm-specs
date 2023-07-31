%bcond_without tests

Name:           python-pingouin
Version:        0.5.3
Release:        %autorelease
Summary:        Statistical package in Python based on Pandas

License:        GPL-3.0-only
URL:            https://pingouin-stats.org/
# PyPI tar does not contain docs and tests
Source0:        https://github.com/raphaelvallat/pingouin/archive/v%{version}/pingouin-%{version}.tar.gz

# hotfix: CI crash in test_power_chi2
# https://github.com/raphaelvallat/pingouin/pull/344
Patch:          https://github.com/raphaelvallat/pingouin/pull/344.patch

# Fix in flatten_list for Python 3.12
# https://github.com/raphaelvallat/pingouin/pull/370
Patch:          https://github.com/raphaelvallat/pingouin/pull/370.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

# The odd combination of an arched package with only noarch binary packages
# makes it easier for us to detect with arch-dependent test failures, since the
# tests will always be run on every platform, and easier for us to skip failing
# tests if necessary, since we can be sure that %%ifarch macros work as
# expected.
#
# Since the package still contains no compiled machine code, we still have no
# debuginfo.
%global debug_package %{nil}

%global _description %{expand:
Pingouin is an open-source statistical package written in Python 3 and based
mostly on Pandas and NumPy. Some of its main features are listed below. For a
full list of available functions, please refer to the API documentation.

  1. ANOVAs: N-ways, repeated measures, mixed, ancova
  2. Pairwise post-hocs tests (parametric and non-parametric) and pairwise
     correlations
  3. Robust, partial, distance and repeated measures correlations
  4. Linear/logistic regression and mediation analysis
  5. Bayes Factors
  6. Multivariate tests
  7. Reliability and consistency
  8. Effect sizes and power analysis
  9. Parametric/bootstrapped confidence intervals around an effect size or a
     correlation coefficient
 10. Circular statistics
 11. Chi-squared tests
 12. Plotting: Bland-Altman plot, Q-Q plot, paired plot, robust correlation…

Pingouin is designed for users who want simple yet exhaustive statistical
functions.

For example, the ttest_ind function of SciPy returns only the T-value and the
p-value. By contrast, the ttest function of Pingouin returns the T-value, the
p-value, the degrees of freedom, the effect size (Cohen’s d), the 95%
confidence intervals of the difference in means, the statistical power and the
Bayes Factor (BF10) of the test.}

%description %_description

%package -n python3-pingouin
Summary:        %{summary}
BuildArch:      noarch

%description -n python3-pingouin %_description

%package doc
Summary:        Documentation and examples for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%prep
%autosetup -n pingouin-%{version} -p1
# Version was upper-bounded in 2223ca5a89c28511dc54101ed0b9501425fcca47; this
# is possibly a “Temp fix for bug in plot_paired.” Anyway, we cannot respect
# the version bound.
sed -r -i 's/(numpy)<.*/\1/' requirements-test.txt

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:requirements-test.txt}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pingouin

%check
%if %{with tests}
%pytest -v
%endif

%files -n python3-pingouin -f %{pyproject_files}
%doc CODE_OF_CONDUCT.md
%doc README.rst

%files doc
%license LICENSE
%doc notebooks

%changelog
%autochangelog
