%bcond_without tests

Name:           python-mock
Version:        4.0.3
Release:        %autorelease
Summary:        Deprecated, use unittest.mock from the standard library instead

License:        BSD-2-Clause
URL:            https://github.com/testing-cabal/mock
Source0:        %{url}/archive/%{version}/mock-%{version}.tar.gz

# Fix tests that should test mock but were testing unittest.mock
# Merged upstream
Patch1:         %{url}/commit/f3e3d82aab.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif


%description
This is a deprecated package.

The mock module is now part of the Python standard library,
available as unittest.mock in Python 3.3 onwards.

https://fedoraproject.org/wiki/Changes/DeprecatePythonMock


%package -n python%{python3_pkgversion}-mock
Summary:        %{summary}

# This package is deprecated, no new packages in Fedora can depend on it
# https://fedoraproject.org/wiki/Changes/DeprecatePythonMock
Provides:       deprecated()

%description -n python%{python3_pkgversion}-mock
This is a deprecated package.

The mock module is now part of the Python standard library,
available as unittest.mock in Python 3.3 onwards.

https://fedoraproject.org/wiki/Changes/DeprecatePythonMock


%prep
%autosetup -p1 -n mock-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif

%install
%pyproject_install
%pyproject_save_files -l mock


%files -n python%{python3_pkgversion}-mock -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
