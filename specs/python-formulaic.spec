%global _description %{expand:
Formulaic is a high-performance implementation of Wilkinson formulas for
Python.

It provides:

- high-performance dataframe to model-matrix conversions.
- support for reusing the encoding choices made during conversion of one
  data-set on other datasets.
- extensible formula parsing.
- extensible data input/output plugins, with implementations for:
  - input:
    - pandas.DataFrame
    - pyarrow.Table
  - output:
    - pandas.DataFrame
    - numpy.ndarray
    - scipy.sparse.CSCMatrix
- support for symbolic differentiation of formulas (and hence model matrices).}

Name:           python-formulaic
Version:        1.1.1
Release:        %{autorelease}
Summary:        A high-performance implementation of Wilkinson formulas

# SPDX
License:        MIT
URL:            https://github.com/matthewwardrop/formulaic
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

# The dependency libarrow is ExcludeArch on 32-bit platforms, and is the sole
# dependent package, python-pybids, plus:
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description %_description

%package -n python3-formulaic
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sympy

%description -n python3-formulaic %_description

%pyproject_extras_subpkg -n python3-formulaic arrow calculus

%prep
%autosetup -n formulaic-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x arrow,calculus

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l formulaic

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{pytest}

%files -n python3-formulaic -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
