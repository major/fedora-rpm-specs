%global srcname astroquery

Name:           python-%{srcname}
Version:        0.4.7
Release:        %autorelease
Summary:        Python module to access astronomical online data resources

License:        BSD-3-Clause
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

#BuildRequires:  python3-astropy
#BuildRequires:  python3-beautifulsoup4
#BuildRequires:  python3-html5lib
#BuildRequires:  python3-keyring
#BuildRequires:  python3-pyvo
#BuildRequires:  python3-requests
# Doc generation not yet working with rawhide 
#BuildRequires:  python3-sphinx

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
%py3_check_import astroquery

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
