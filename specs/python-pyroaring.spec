%global pypi_name pyroaring
%global forgeurl https://github.com/Ezibenroc/PyRoaringBitMap

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        %{autorelease}
Summary:        Fast and lightweight set for unsigned 32 bits integers
%global tag %{version}
%forgemeta
# pyroaring/roaring.c and pyroaring/roaring.h are dual licensed
License:        MIT or Apache-2.0
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc, gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-Cython

# Leaf package. Stop building for i686.
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global _description %{expand:
An efficient and light-weight ordered set of 32 bits integers. This is
a Python wrapper for the C library CRoaring.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%tox
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
