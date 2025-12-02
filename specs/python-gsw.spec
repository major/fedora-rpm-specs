Name:           python-gsw
Version:        3.6.20
Release:        %autorelease
Summary:        Gibbs Seawater Oceanographic Package of TEOS-10

License:        BSD-3-Clause
URL:            https://www.teos-10.org/
Source:         %pypi_source gsw

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  gcc
# Test dependencies.
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Python implementation of the Thermodynamic Equation of Seawater 2010 (TEOS-10)
based primarily on NumPy ufunc wrappers of the GSW-C implementation.
}

%description %_description

%package -n     python3-gsw
Summary:        %{summary}

%description -n python3-gsw %_description

%prep
%autosetup -p1 -n gsw-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l gsw

%check
%pytest

%files -n python3-gsw -f %{pyproject_files}

%changelog
%autochangelog
