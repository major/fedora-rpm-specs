%bcond_without tests

%global _description %{expand:
Pingouin is an open-source statistical package written in Python 3 and based on
Pandas and NumPy.

It provides easy-to-grasp functions for computing several statistical
functions:

- ANOVAs: one- and two-ways, repeated measures, mixed, ancova
- Post-hocs tests and pairwise comparisons
- Robust correlations
- Partial correlation, repeated measures correlation and intraclass correlation
- Bayes Factor
- Tests for sphericity, normality and homoscedasticity
- Effect sizes (Cohen's d, Hedges'g, AUC, Glass delta, eta-square...)
- Parametric/bootstrapped confidence intervals around an effect size or a
  correlation coefficient
- Circular statistics
- Linear/logistic regression and mediation analysis

Pingouin is designed for users who want simple yet exhaustive statistical
functions.}

Name:           python-pingouin
Version:        0.5.2
Release:        %autorelease
Summary:        Statistical package in Python based on Pandas

# Documentation pulls in bootstrap, bootswatch, jquery which are MIT
License:        GPLv3 and MIT
URL:            https://pingouin-stats.org/
# PyPI tar does not contain docs and tests
Source0:        https://github.com/raphaelvallat/pingouin/archive/v%{version}/pingouin-%{version}.tar.gz

# Use scikit-learn>=1.1.2
# https://github.com/raphaelvallat/pingouin/pull/300
#
# Rebased on 0.5.2.
Patch:          pingouin-0.5.2-scikit-learn-1.1.2.patch

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
%if %{with tests}
# Only required and works in TRAVIS, so not needed here
sed -r -i 's/^(pytest-travis-fold)$/# \1/' requirements-test.txt
%endif

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:requirements-test.txt}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pingouin

%check
%if %{with tests}
%pytest
%endif

%files -n python3-pingouin -f %{pyproject_files}
%doc CODE_OF_CONDUCT.md
%doc README.rst

%files doc
%license LICENSE
%doc notebooks

%changelog
%autochangelog
