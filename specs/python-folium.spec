Name:           python-folium
Version:        0.19.4
Release:        %autorelease
Summary:        Python library for visualizing data on a Leaflet map

License:        MIT
URL:            https://python-visualization.github.io/folium/

# Use PyPI, since setup.py uses use_scm_version, which doesn't work with
# GitHub tarballs.
Source0:        %{pypi_source folium}

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel

%global _description %{expand:
folium builds on the data wrangling strengths of the Python ecosystem and the
mapping strengths of the Leaflet.js library. Manipulate your data in Python,
then visualize it in a Leaflet map via folium.}

%description %_description

%package -n python3-folium
Summary:        %{summary}

%description -n python3-folium %_description


%prep
%autosetup -p1 -n folium-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files folium


%check
%pyproject_check_import

# No tests here since quite a few packages for testing are not yet in Fedora
# repositories; also, tests for this package depend on an internet connection.
# $ sudo dnf install [BUILT_PACKAGE]
# $ git clone https://github.com/python-visualization/folium
# $ cd folium
# $ git checkout v[VERSION]
# $ sudo dnf install -y chromedriver conda
# $ conda create --name FOLIUM -c conda-forge python=3 --file requirements.txt --file requirements-dev.txt
# $ pip install -r requirements.txt
# $ pip install -r requirements-dev.txt
# $ pip install -e . --no-deps
# $ cd tests
# $ pytest

%files -n python3-folium -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt


%changelog
%autochangelog
