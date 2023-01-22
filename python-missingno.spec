%bcond_without tests

%global pypi_name missingno
%global desc %{expand: \
Messy datasets? Missing values? missingno provides a small toolset
of flexible and easy-to-use missing data visualizations and utilities
that allows you to get a quick visual summary of the completeness
(or lack thereof) of your dataset.}

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        5%{?dist}
Summary:        Missing data visualization module for Python
License:        MIT
URL:            https://github.com/ResidentMario/missingno
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%?python_enable_dependency_generator

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(seaborn)
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-cov)
BuildRequires: python3dist(pytest-mpl)
BuildRequires: python3dist(numpy)
BuildRequires: python3dist(scipy)
BuildRequires: python3dist(pandas)
BuildRequires: python3dist(geopandas)
BuildRequires: python3dist(geoplot)
BuildRequires: python3dist(matplotlib)
BuildRequires: quilt

Requires: python3dist(pandas)
Requires: python3dist(geopandas)
Requires: python3dist(geoplot)

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} ';'

%build
%py3_build

%install
%py3_install

%check
mkdir -p ~/.config/matplotlib/
echo "backend: Agg" > ~/.config/matplotlib/matplotlibrc
export PYTHONPATH=".:$RPM_BUILD_ROOT/%{python3_sitelib}"
# https://github.com/ResidentMario/missingno/blob/master/CONTRIBUTING.md#testing
# temporarily disabled: failing unreliably
#%%{pytest} --mpl-generate-path=tests/baseline tests/viz_tests.py
%{pytest} tests/util_tests.py

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md CONFIGURATION.md paper.bib paper.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-4
- Drop support for i686

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.0-1
- Update to latest release
- Replace nose with pytest
- remove uneeded patch

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.2-8
- Remove unused descartes dependencies

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.2-8
- Rebuilt for Python 3.10

* Sun Mar 28 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.2-7
- Patch to fix test setup with latest Pandas

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.4.2-5
- Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-4
- Rebuilt for Python 3.9

* Sun Mar 29 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.2-3
- Exclude deprecated geoplot test
- https://github.com/ResidentMario/missingno/commit/5b99ad5840f4fef8169e50b0e542eae9ea5cd00e
- https://bugzilla.redhat.com/show_bug.cgi?id=1816251

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.4.2-1
- New upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.4.0-2
- Fix comment #1 on BZ #1655725

* Mon Dec 03 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.4.0-1
- Initial import
