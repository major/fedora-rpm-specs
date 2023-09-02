%global pypi_name pyroaring

Name:           python-%{pypi_name}
Version:        0.4.2
Release:        %{autorelease}
Summary:        Fast and lightweight set for unsigned 32 bits integers

# pyroaring/roaring.c and pyroaring/roaring.h are dual licensed
License:        MIT or Apache-2.0
URL:            https://github.com/Ezibenroc/PyRoaringBitMap
Source:         %{pypi_source %{pypi_name}}

BuildRequires:  gcc, gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-Cython < 3~~

%global _description %{expand:
An efficient and light-weight ordered set of 32 bits integers. This is
a Python wrapper for the C library CRoaring.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


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
