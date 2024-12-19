%global module_name erfa
%global pypi_name pyerfa
# tests need pytest-astropy, needs astropy, needs pyerfa
%bcond_without tests

Name:           python-pyerfa
Version:        2.0.1.5
Release:        %autorelease
Summary:        Python wrapper for the ERFA library
License:        BSD-3-Clause
URL:            https://github.com/liberfa/pyerfa
Source0:        %{pypi_source}

# Python BuildRequires
BuildRequires:  python3-devel
BuildRequires:  erfa-devel
BuildRequires:  gcc


%description
PyERFA is the Python wrapper for the ERFA library (Essential Routines for
Fundamental Astronomy), a C library containing key algorithms for astronomy,
which is based on the SOFA library published by the International Astronomical
Union (IAU). All C routines are wrapped as Numpy universal functions, so that
they can be called with scalar or array inputs.


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
PyERFA is the Python wrapper for the ERFA library (Essential Routines for
Fundamental Astronomy), a C library containing key algorithms for astronomy,
which is based on the SOFA library published by the International Astronomical
Union (IAU). All C routines are wrapped as Numpy universal functions, so that
they can be called with scalar or array inputs.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t


%build
# Build using system liberfa, not bundled one
export PYERFA_USE_SYSTEM_LIBERFA=1 
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{module_name}


%check
%if %{with tests}
%{tox}
%else
%py3_check_import %{module_name}
%endif

%files -n  python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.rst
%doc AUTHORS.rst CHANGES.rst README.rst


%changelog
%autochangelog
