Name:           python-array-api-strict
Version:        2.0.1
Release:        %{autorelease}
Summary:        Strict implementation of the Python array API


License:        BSD-3-Clause
URL:            https://github.com/data-apis/array-api-strict
Source:         %{pypi_source array_api_strict}

# Fix test_iter with Python 3.14.0b1
# Rebased from https://github.com/data-apis/array-api-strict/pull/154 (merged)
Patch:          Fix-test_iter-with-Python-3.14-beta-1.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis

%global _description %{expand:
array_api_strict is a strict, minimal implementation of the Python array API.

The purpose of array-api-strict is to provide an implementation of the array
API for consuming libraries to test against so they can be completely sure
their usage of the array API is portable.

It is not intended to be used by end-users. End-users of the array API should
just use their favorite array library (NumPy, CuPy, PyTorch, etc.) as usual. It
is also not intended to be used as a dependency by consuming libraries.
Consuming library code should use the array-api-compat package to support the
array API. Rather, it is intended to be used in the test suites of consuming
libraries to test their array API usage.}

%description %{_description}

%package -n     python3-array-api-strict
Summary:        %{summary}

%description -n python3-array-api-strict %{_description}

%prep
%autosetup -p1 -n array_api_strict-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l array_api_strict


%check
%pytest


%files -n python3-array-api-strict -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
