# This package is interdependant on rst-linker to build docs
# will build both with out docs and add docs in later
%bcond_with docs 

Name:           python-jaraco-packaging
Version:        10.2.3
Release:        %autorelease
Summary:        Tools to supplement packaging Python releases

License:        MIT
URL:            https://github.com/jaraco/jaraco.packaging
Source0:        %{pypi_source jaraco_packaging}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli

%description
Tools for packaging.dependency_tree A dist-utils command for reporting the
dependency tree as resolved by setup-tools. Use after installing a package.show
A dist-utils command for reporting the attributes of a distribution, such as the
version or author name.

%package -n python3-jaraco
Summary: A Parent package for jaraco's parent dir and init file.

%description -n python3-jaraco
A Parent package for jaraco's parent dir and init file.

%package -n python3-jaraco-packaging
Summary:        %{summary}


%description -n python3-jaraco-packaging
Tools for packaging.dependency_tree A dist-utils command for reporting the
dependency tree as resolved by setup-tools. Use after installing a package.show
A dist-utils command for reporting the attributes of a distribution, such as the
version or author name.


%if %{with docs}
%package -n python-jaraco-packaging-doc
Summary:        jaraco.packaging documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(rst-linker)

%description -n python-jaraco-packaging-doc
Documentation for jaraco.packaging
%endif


%prep
%autosetup -n jaraco_packaging-%{version}
# Remove dev-only dependencies. Upstream later split the `test` dependencies out of it
# https://github.com/jaraco/skeleton/issues/138
tomcli set pyproject.toml lists delitem "project.optional-dependencies.test" "pytest-.*"


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel
%if %{with docs}
# generate html docs 
# This package requires itself to build docs :/
%{python3} -m sphinx docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install
%pyproject_save_files -l jaraco


%check
# Overriding --import-mode because it was picking up `jaraco.packaging` as `packaging`
# metadata.hunt_down_url, print-metadata.main: tests run `pip install` without `--no-build-isolation`
# sphinx._load_metadata_from_wheel: test runs `pip download`
%pytest --import-mode prepend -k "not (packaging.metadata.hunt_down_url \
or packaging.print-metadata.main \
or packaging.sphinx._load_metadata_from_wheel)"


%files -n python3-jaraco
%license LICENSE
%doc README.rst
%{python3_sitelib}/jaraco
%exclude %{python3_sitelib}/jaraco/packaging

%files -n python3-jaraco-packaging -f %{pyproject_files}
%doc README.rst

%if %{with docs}
%files -n python-jaraco-packaging-doc
%license LICENSE
%doc html 
%endif


%changelog
%autochangelog
