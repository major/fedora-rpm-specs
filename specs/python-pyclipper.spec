%global srcname pyclipper

Name:           python-%{srcname}
Version:        1.3.0.post6
Release:        %autorelease
Summary:        Cython wrapper for the C++ translation of the Angus Johnson's Clipper library

License:        MIT
URL:            https://pypi.org/project/pyclipper
Source:         %pypi_source %{srcname}

# Unbundle Clipper library from build entirely, so we can use the system copy.
Patch:          0001-Unbundle-Clipper-library-from-build-entirely.patch

BuildRequires:  gcc-c++
BuildRequires:  polyclipping-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
Pyclipper is a Cython wrapper exposing public functions and classes of the C++
translation of the Angus Johnson's Clipper library.

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
Pyclipper is a Cython wrapper exposing public functions and classes of the C++
translation of the Angus Johnson's Clipper library.


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Remove bundled polyclipping.
rm src/clipper.{cpp,hpp}
# Remove pre-generated Cython files.
rm src/pyclipper/*.cpp

# Make setup.py build Cython from source.
touch dev

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest}

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
