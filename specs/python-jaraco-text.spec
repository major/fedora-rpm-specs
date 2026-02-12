%global pypi_name jaraco_text
%global pkg_name jaraco-text

# Requires jaraco.tidelift to be packaged
%bcond docs 0
# Some test deps are missing in EPEL9
%bcond tests %[0%{?epel} != 9]
# Change the build backend in EPEL because `setuptools>=77` is needed
%bcond hatch %[0%{?epel} && 0%{?epel} <= 10]

Name:           python-%{pkg_name}
Version:        4.2.0
Release:        %autorelease
Summary:        Module for text manipulation

License:        MIT
URL:            https://github.com/jaraco/jaraco.text
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
%if %{with hatch}
BuildRequires:  tomcli
%endif

%description
%{summary}

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
%{summary}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if %{with hatch}
tomcli set pyproject.toml lists str "build-system.requires" "hatchling" "hatch-vcs" "coherent.licensed"
tomcli set pyproject.toml str "build-system.build-backend" "hatchling.build"
tomcli set pyproject.toml str "tool.hatch.version.source" "vcs"
tomcli set pyproject.toml lists str "tool.hatch.build.targets.wheel.packages" "jaraco"
%endif

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test -x inflect} %{?with_docs:-x doc}

%build
%pyproject_wheel

%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# with docs
%endif

%install
%pyproject_install
install -pm 0644 jaraco/text/Lorem\ ipsum.txt \
    %{buildroot}%{python3_sitelib}/jaraco/text/
%pyproject_save_files jaraco

%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif

%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst NEWS.rst

%pyproject_extras_subpkg -n python3-%{pkg_name} inflect

%if %{with docs}
%package -n     python-%{pkg_name}-doc
Summary:        jaraco.text documentation

%description -n python-%{pkg_name}-doc
Documentation for jaraco.text

%files -n python-%{pkg_name}-doc
%doc html
%license LICENSE
# with docs
%endif

%changelog
%autochangelog
