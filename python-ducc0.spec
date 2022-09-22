%global srcname ducc0

Name:           python-%{srcname}
Version:        0.25.0
Release:        %autorelease
Summary:        Programming tools for numerical computation

License:        GPLv2+ and BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

# Fix pyproject.toml warnings
Patch:          ducc0-0.24_pyproject.patch

ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
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

# there's no other way to disable ducc to inject custom C flags
sed -i 's|extra_compile_args=extra_compile_args|extra_compile_args=\[\]|g' setup.py
sed -i 's|extra_link_args=python_module_link_args|extra_link_args=\[\]|g' setup.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ducc0


%check
%pyproject_check_import
%pytest -q python/test


%files -n python3-%{srcname} -f %{pyproject_files}


%changelog
%autochangelog
