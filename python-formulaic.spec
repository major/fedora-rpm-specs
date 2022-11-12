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
Version:        0.5.2
Release:        %{autorelease}
Summary:        A high-performance implementation of Wilkinson formulas

License:        MIT
URL:            https://github.com/matthewwardrop/formulaic
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Backports https://github.com/matthewwardrop/formulaic/commit/e5dedcb0feed39f5ff6e2326d727ca65d247f26d to v0.5.2
# fork lives at https://github.com/sanjayankur31/formulaic/tree/fedora-0.5.2
Patch0:         0001-fix-correct-pytest-usage.patch

BuildArch:      noarch

%description %_description

%package -n python3-formulaic
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sympy
BuildRequires:  git-core

%description -n python3-formulaic %_description

%prep
%autosetup -n formulaic-%{version} -S git

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files formulaic

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{pytest}

%files -n python3-formulaic -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
