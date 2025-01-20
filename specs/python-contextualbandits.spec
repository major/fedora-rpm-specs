%global pypi_name contextualbandits

%global _description %{expand:
This Python package contains implementations of methods from different papers
dealing with contextual bandit problems, as well as adaptations from typical
multi-armed bandits strategies. It aims to provide an easy way to prototype
and compare ideas, to reproduce research papers that don't provide 
easily-available implementations of their proposed algorithms, and to
serve as a guide in learning about contextual bandits.}

%global commit          331b9ef640c4315e6fb10f41d73e8a5e0e484038
%global snapshotdate    20232604
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        0.3.21
Release:        11%{?dist}
Summary:        Python implementations of algorithms for contextual bandits

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/david-cortes/contextualbandits

# we fetch the latest tarball from the upstream
# we do not rely on Pypi version (no docs, no LICENSE included)
Source0:        %url/archive/%{commit}/%{pypi_name}-%{commit}.tar.gz

# Stop building for i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  Cython

# For documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{commit}
rm -rf %{pypi_name}.egg-info
# remove toml file. It is actually not used in real build.
rm -rf pyproject.toml

%generate_buildrequires
echo 'python3dist(numpy)'
echo 'python3dist(scipy)'
echo 'python3dist(pandas)'
echo 'python3dist(scikit-learn)'
echo 'python3dist(joblib)'

%build
%pyproject_wheel

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%files doc
%license LICENSE
%doc html/
%doc example/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 24 2024 Orion Poplawski <orion@nwra.com> - 0.3.21-10
- Rebuild with numpy 2.x (rhbz#2333879)

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.21-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.3.21-7
- Rebuilt for Python 3.13

* Wed Mar 06 2024 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.21-6
- Stop building for i686

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 0.3.21-2
- Rebuilt for Python 3.12

* Tue Jun 6 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.21-1
- Update to 0.3.21

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 2 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.20-1
- Update to the latest upstream's release

* Fri Oct 14 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.19-1
- Update to the latest upstream's release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 8 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.17.3-1
- Update to the latest upstream's release

* Mon Jul 04 2022 Python Maint <python-maint@redhat.com> - 0.3.17-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 3 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.17-2
- Port to pyproject-rpm-macros

* Sat Jan 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.17-1
- Update to the latest upstream's release
- Remove patch

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.14-2
- Rebuilt for Python 3.10

* Sun Apr 18 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.14-1
- Initial package
