%global srcname ducc0
%global stable 1
#%%global commit 4a007f4bacf4d8b7e8cc5523f4d7dd515d7dc19f
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
#%%global date 20230208

Name:           python-%{srcname}
%if "%{?stable}"
Version:        0.36.0
%else
Version:        0.28.0^%{date}%{shortcommit}
%endif
Release:        %autorelease
Summary:        Programming tools for numerical computation

License:        GPL-2.0-or-later AND (GPL-2.0-or-later OR BSD-3-Clause)
URL:            https://pypi.python.org/pypi/%{srcname}
%if "%{?stable}"
Source0:        %{pypi_source ducc0}
%else
Source0:        https://github.com/mreineck/ducc/archive/%{commit}/ducc-%{commit}.tar.gz
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
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
%if "%{?stable}"
%autosetup -p1 -n %{srcname}-%{version}
# Remove egg files from source
rm -rf %{srcname}.egg-info
%else
%autosetup -p1 -n ducc-%{commit}
%endif

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
%doc README.md


%changelog
%autochangelog
