%global srcname astroquery

Name:           python-%{srcname}
Version:        0.4.11
Release:        %autorelease
Summary:        Python module to access astronomical online data resources

License:        BSD-3-Clause
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

# This package is imported but is not listed as a dep
BuildRequires:  %{py3_dist pillow}
Requires:  %{py3_dist pillow}

%description
Astroquery is an astropy affiliated package that contains a collection of tools
to access online Astronomical data.

%package -n python3-%{srcname}
Summary:  %{summary}

%description -n python3-%{srcname}
Astroquery is an astropy affiliated package that contains a collection of tools
to access online Astronomical data.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
# test deps not in Fedora (pytest-dependency)
%pyproject_buildrequires 


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files astroquery

%check
%pyproject_check_import -e '*.test*' -e '*.conftest' -e '*.dace'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
