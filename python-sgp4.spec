%global srcname sgp4

Name:           python-%{srcname}
Version:        2.23
Release:        %autorelease
Summary:        Compute position and velocity of earth-orbiting satellites
# Python code is MIT, backend algorithms are based on SGP4 code
# which is made available through its usage permission notice
License:        MIT AND SGP4
URL:            https://pypi.python.org/pypi/%{srcname}
Source:         %{pypi_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-devel

# For tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)

Provides:       bundled(sgp4)

%global _description %{expand:
This Python package computes the position and velocity of an earth-orbiting
satellite, given the satellite’s TLE orbital elements from a source like
CelesTrak. It implements the most recent version of SGP4, and is regularly
run against the SGP4 test suite to make sure that its satellite position
predictions agree to within 0.1 mm with the predictions of the standard
distribution of the algorithm. This error is far less than the 1–3 km/day
by which satellites themselves deviate from the ideal orbits described in
TLE files.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import
%pytest sgp4/tests.py


%files -n python3-%{srcname} -f %{pyproject_files}


%changelog
%autochangelog
