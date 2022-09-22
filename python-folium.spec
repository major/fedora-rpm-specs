Name:           python-folium
Version:        0.12.1.20211119.post1
Release:        4%{?dist}
Summary:        Python library for visualizing data on a Leaflet map

License:        MIT
URL:            https://python-visualization.github.io/folium/

%global _upstream_version 0.12.1.post1

# Use PyPI, since setup.py uses use_scm_version, which doesn't work with
# GitHub tarballs.
Source0:        %{pypi_source folium %_upstream_version}

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
%autosetup -p1 -n folium-%{_upstream_version}


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
# For the instructions on running tests, please refer to:
# https://github.com/python-visualization/folium/blob/main/.github/CONTRIBUTING.md#contributing-code


%files -n python3-folium -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1.20211119.post1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.12.1.20211119.post1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1.20211119.post1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Roman Inflianskas <rominf@aiven.io> - 0.12.1.20211119.post1-1
- Initial package
