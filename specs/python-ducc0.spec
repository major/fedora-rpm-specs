%global srcname ducc0

Name:           python-%{srcname}
Version:        0.39.1
Release:        %autorelease
Summary:        Programming tools for numerical computation

License:        GPL-2.0-or-later AND (GPL-2.0-or-later OR BSD-3-Clause)
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source ducc0}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-nanobind-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
This is a collection of basic programming tools for numerical computation,
including Fast Fourier Transforms, Spherical Harmonic Transforms,
non-equispaced Fourier transforms, as well as some concrete applications
like 4pi convolution on the sphere and gridding/degridding of radio
interferometry data.
The code is written in C++17, but provides a simple and comprehensive
Python interface.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

# Importable module is named ducc
%py_provides python3-ducc

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove egg files from source
rm -rf %{srcname}.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
export DUCC0_OPTIMIZATION="portable-debug"
export DUCC0_CFLAGS="%{build_cxxflags}"
export DUCC0_LFLAGS="%{build_ldflags}"
export SKBUILD_CMAKE_VERBOSE=true
export DUCC0_USE_NANOBIND=true
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ducc0


%check
%pyproject_check_import
%pytest -q python/test


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
