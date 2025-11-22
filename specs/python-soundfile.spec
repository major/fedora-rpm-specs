# Created by pyp2rpm-3.3.10
%global pypi_name soundfile
%global pypi_version 0.13.1

Name:           python-%{pypi_name}
Version:        0.13.1
Release:        1%{?dist}
Summary:        An audio library based on libsndfile, CFFI and NumPy

License:        BSD-3-Clause
URL:            https://github.com/bastibe/python-soundfile
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 1
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-pip
BuildRequires:  libsndfile-devel

%description
python-soundfile |version| |python| |status| |license||contributors|
|downloads|The soundfile < module is an audio library based on libsndfile, CFFI
and NumPy. Full documentation is available on soundfile module can read and
write sound files. File reading/writing is supported through libsndfile < which
is a free, cross-platform, open-source (LGPL) library for reading and writing
many...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(cffi) >= 1
Requires:       python3dist(numpy)
Requires:       python3-libs
%description -n python3-%{pypi_name}
python-soundfile |version| |python| |status| |license||contributors|
|downloads|The soundfile < module is an audio library based on libsndfile, CFFI
and NumPy. Full documentation is available on soundfile module can read and
write sound files. File reading/writing is supported through libsndfile < which
is a free, cross-platform, open-source (LGPL) library for reading and writing
many...

%package -n python-%{pypi_name}-doc
Summary:        soundfile documentation
%description -n python-%{pypi_name}-doc
Documentation for soundfile

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/_soundfile.py
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Nov 18 2025 Gwyn Ciesla <gwync@protonmail.com> - 0.13.1-1
- 0.13.1

* Tue Apr 02 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.12.1-1
- Initial package.
