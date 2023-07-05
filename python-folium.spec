Name:           python-folium
Version:        0.14.0
Release:        4%{?dist}
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
* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.14.0-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.14.0-2
- Drop support for i686

* Sat Dec 17 2022 Roman Inflianskas <rominf@aiven.io> - 0.14.0-1
- Update to 0.14.0 (resolves rhbz#2152748)
- Add importability checks
- Update testing instructions

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
