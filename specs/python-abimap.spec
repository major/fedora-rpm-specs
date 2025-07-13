%global module_name abimap

Name:           python-%{module_name}
Version:        0.4.0
Release:        %autorelease
License:        MIT
Summary:        A helper for library maintainers to use symbol versioning
Url:            https://github.com/ansasaki/abimap

Source:         https://files.pythonhosted.org/packages/source/a/%{module_name}/%{module_name}-%{version}.tar.gz

# This patch removes the test which depends on pytest-console-scripts
Patch0:         python-abimap-0.4.0-disable-script-test.patch
# This patch removes sphinx napoleon extension
Patch1:         python-abimap-0.3.1-remove-docs-napoleon.patch
# This patch removes sphinx rtd theme
Patch2:         python-abimap-0.4.0-remove-docs-rtd-theme.patch
# This patch adjusts the requirements-test.txt
Patch3:         python-abimap-0.4.0-adjust-test-requirements.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  make

%description
This script allows to generate and update symbol version linker scripts which
adds version information to the exported symbols. The script is intended to be
integrated as part of a shared library build to check for changes in the set
of exported symbols and update the symbol version linker script accordingly.

%package -n python%{python3_pkgversion}-%{module_name}
Summary:        A helper for library maintainers to use symbol versioning
%py_provides python%{python3_pkgversion}-%{module_name}

%description -n python%{python3_pkgversion}-%{module_name}
This script allows to generate and update symbol version linker scripts which
adds version information to the exported symbols. The script is intended to be
integrated as part of a shared library build to check for changes in the set
of exported symbols and update the symbol version linker script accordingly.

%package -n python-%{module_name}-doc
Summary:        Documentation for python-%{module_name}
%description -n python-%{module_name}-doc
Documentation for python-%{module_name}

%prep
%autosetup -n %{module_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module_name}.egg-info

%generate_buildrequires
# Include test requirements
%pyproject_buildrequires -t %{_builddir}/%{module_name}-%{version}/requirements-test.txt

%build
%pyproject_wheel
# Generate html docs
PYTHONPATH=${PWD}/src:${PWD}/tests \
    %{python3} -m sphinx -E -b html docs html
# Generate manpage
PYTHONPATH=${PWD}/src:${PWD}/tests \
    %{python3} -m sphinx -E -b man docs man
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
# Install man page
mkdir -p %{buildroot}%{_mandir}/man1
install ${PWD}/man/abimap.1 %{buildroot}%{_mandir}/man1/abimap.1

%check
%tox

%files -n python%{python3_pkgversion}-%{module_name}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{_bindir}/abimap
%dir %{python3_sitelib}/abimap
%{python3_sitelib}/abimap/*
%{python3_sitelib}/abimap-%{version}.dist-info/
%{_mandir}/man1/abimap.1*

%files -n python-%{module_name}-doc
%license LICENSE
%doc html

%changelog
%autochangelog
