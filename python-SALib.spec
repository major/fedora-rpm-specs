# Tests are enabled
%bcond_without tests

%global _description %{expand:
Python implementations of commonly used sensitivity analysis methods. Useful in
systems modeling to calculate the effects of model inputs or exogenous factors
on outputs of interest.

Herman, J. and Usher, W. (2017) SALib: An open-source Python library for
sensitivity analysis. Journal of Open Source Software, 2(9).

Methods included:

- Sobol Sensitivity Analysis (Sobol 2001, Saltelli 2002, Saltelli et al. 2010)
- Method of Morris, including groups and optimal trajectories (Morris 1991,
  Campolongo et al. 2007)
- Fourier Amplitude Sensitivity Test (FAST) (Cukier et al. 1973, Saltelli et
  al. 1999)
- Delta Moment-Independent Measure (Borgonovo 2007, Plischke et al. 2013)
- Derivative-based Global Sensitivity Measure (DGSM) (Sobol and Kucherenko
  2009)
- Fractional Factorial Sensitivity Analysis (Saltelli et al. 2008)}

Name:           python-SALib
Version:        1.4.5
Release:        %autorelease
Summary:        Sensitivity Analysis Library

License:        MIT
URL:            http://salib.github.io/SALib/
Source0:        https://github.com/SALib/SALib/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-SALib
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
%endif

# Not mentioned in setup.py, so won't be picked up by the generator
Requires:  %{py3_dist pandas}
Requires:  %{py3_dist numpy} >= 1.9.0
Requires:  %{py3_dist scipy}
Requires:  %{py3_dist matplotlib} >= 1.4.3

%description -n python3-SALib %_description

%prep
%autosetup -n SALib-%{version}

# python3, not python in tests
sed -i 's/python {cli}/python3 {cli}/' tests/test_cli_sample.py
sed -i 's/python {cli}/python3 {cli}/' tests/test_cli_analyze.py

# https://github.com/SALib/SALib/commit/2eb776b6c7ff0737e4d9855709e6e24c19e36971.patch
sed -i 's/rU/r/' src/SALib/util/__init__.py

# Correct permission
chmod -x LICENSE.txt

# Remove /usr/bin/env python shebang
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# Correct end of line encoding
sed -i 's/\r$//' LICENSE.txt
sed -i 's/\r$//' src/SALib/analyze/rbd_fast.py

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%if %{with tests}
%pyproject_buildrequires -r
%else
%pyproject_buildrequires
%endif

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files SALib

# Add a shebang to missing script
sed -i "1 i \#\!%{python3}" $RPM_BUILD_ROOT/%{_bindir}/salib.py

%check
%if %{with tests}
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitelib} %{pytest}
%endif

%files -n python3-SALib -f %{pyproject_files}
%doc README.rst README-advanced.md CHANGELOG.md CITATIONS.rst AUTHORS.rst FAQ.MD
%{_bindir}/salib
%{_bindir}/salib.py

%changelog
%autochangelog
