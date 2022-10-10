Name:           python-folium
Version:        0.13.0
Release:        1%{?dist}
Summary:        Python library for visualizing data on a Leaflet map

License:        MIT
URL:            https://python-visualization.github.io/folium/

# Use PyPI, since setup.py uses use_scm_version, which doesn't work with
# GitHub tarballs.
Source0:        %{pypi_source folium}

BuildArch:      noarch
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
# No checks here since quite a few packages for testing are not yet in Fedora
# repositories; also, tests for this package depend on an internet connection.
# $ sudo dnf install [BUILT_PACKAGE]
# $ git clone https://github.com/python-visualization/folium
# $ cd folium
# $ git checkout v%{version}
# $ # Install as much as possible from Fedora repositories
# $ echo chromedriver 'python3dist(cartopy)' 'python3dist(check-manifest)' 'python3dist(fiona)' 'python3dist(ipykernel)' 'python3dist(matplotlib)' 'python3dist(nbconvert)' 'python3dist(nbsphinx)' 'python3dist(owslib)' 'python3dist(pandas)' 'python3dist(pillow)' 'python3dist(pytest)' 'python3dist(pytest-cov)' 'python3dist(pytest-xdist)' 'python3dist(scipy)' 'python3dist(selenium)' 'python3dist(wheel)' | xargs -n1 sudo dnf install -y
# $ pip install -r requirements-dev.txt
# $ cd tests
# $ pytest

%files -n python3-folium -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt


%changelog
* Sat Oct 08 2022 Roman Inflianskas <rominf@aiven.io> - 1.3.0-1
- Update to 1.3.0 (resolves rhbz#2133104)
- Update testing instructions

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1.20211119.post1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.12.1.20211119.post1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1.20211119.post1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Roman Inflianskas <rominf@aiven.io> - 0.12.1.20211119.post1-1
- Initial package
