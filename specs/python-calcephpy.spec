%global srcname calcephpy

Name:           python-%{srcname}
Version:        4.0.5
Release:        %autorelease
Summary:        Astronomical library to access planetary ephemeris files

License:        CECILL-2.0 OR CECILL-B OR CECILL-C
URL:            https://pypi.python.org/pypi/calcephpy
Source0:        %{pypi_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Documentation build doesn't work anymore because it relies on several
# sphinx extensions not packaged / not packageable in Fedora
Obsoletes:      python3-calcephpy-docs < 4.0.0


%global _description %{expand:
This is the Python module of calceph.
Calceph is a library designed to access the binary planetary ephemeris files,
such INPOPxx, JPL DExxx and SPICE ephemeris files.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  python3-devel
# For import smoke test
BuildRequires:  python3dist(numpy)

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Remove egg files from source
rm -r %{srcname}.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
export CPPFLAGS="$CXXFLAGS"
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname} -l


%check
# Provided tests are only for the C library
%py3_check_import calcephpy


%files -n python3-%{srcname} -f %{pyproject_files}


%changelog
%autochangelog
