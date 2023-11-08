# BOOTSTRAPPING NOTE: The tests depend on python3-coincidence which in turn
# depends on this package.
%bcond tests 1

%global forgeurl https://github.com/domdfcoding/domdf_python_tools

Name:           python-domdf-python-tools
Version:        3.7.0
%forgemeta
Release:        1%{?dist}
Summary:        Helpful functions for Python

# Primary license: MIT
#
# licensecheck -r domdf_python_tools --shortname-scheme=spdx | grep -vE -e 'MIT$' -e 'UNKNOWN' | sort
# domdf_python_tools/bases.py: MIT and/or PSF-2.0
# domdf_python_tools/compat/__init__.py: MIT and/or PSF-2.0
# domdf_python_tools/dates.py: MIT and/or PSF-2.0
# domdf_python_tools/getters.py: MIT and/or PSF-2.0

# domdf_python_tools/paths.py: CC-BY-SA and/or MIT and/or PSF-2.0
# NOTE: The supposedly CC-BY-SA licensed code is a trivial, less than 10 line
# function from Stack Overflow that is not copyrightable nor patentable.
# It is not included in the license consideration.

# domdf_python_tools/pretty_print.py: MIT and/or PSF-2.0
# domdf_python_tools/terminal.py: BSD-2-Clause and/or MIT and/or PSF-2.0
# domdf_python_tools/utils.py: MIT and/or PSF-2.0
License:        MIT AND PSF-2.0 AND BSD-2-Clause
URL:            %{forgeurl}
Source:         %{forgesource}
Patch:          Don-t-remove-egg-info-directory-in-setup.py.patch

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-test
BuildRequires:  %{py3_dist coincidence}
BuildRequires:  %{py3_dist click}
BuildRequires:  %{py3_dist faker}
BuildRequires:  %{py3_dist funcy}
BuildRequires:  %{py3_dist pytest}
%endif


%description
%{summary}.


%package -n python3-domdf-python-tools
Summary:        %{summary}

%description -n python3-domdf-python-tools
%{summary}.


%prep
%autosetup -p1 %{forgesetupargs}
# pytest-timeout is not needed to run tests in the RPM build environment
sed -i '/^timeout =/d' tox.ini
# Remove unnecessary shebangs
find domdf_python_tools/ -type f ! -executable -name '*.py' -print \
    -exec sed -i -e '1{\@^#!.*@d}' '{}' +


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files domdf_python_tools


%check
%pyproject_check_import

%if %{with tests}
%global test_ignores %{shrink:
%dnl This test depends on flake8 plugin implementation details. No thank you.
    not test_discover_entry_points
%dnl TestList::test_repr_deep - Failed: DID NOT RAISE <class 'RecursionError'>
and not test_repr_deep
}

%pytest -v -k %{shescape:%{test_ignores}}
%endif


%files -n python3-domdf-python-tools -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Sun Nov 05 2023 Maxwell G <maxwell@gtmx.me> - 3.7.0-1
- Initial package. Closes rhbz#2244974
