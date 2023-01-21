Name:           python-jupyterlab-server
Version:        2.19.0
Release:        1%{?dist}
Summary:        A set of server components for JupyterLab and JupyterLab like applications
License:        BSD-3-Clause
URL:            https://jupyterlab-server.readthedocs.io
Source:         %{pypi_source jupyterlab_server}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
JupyterLab Server sits between JupyterLab and Jupyter Server, and provides
a set of REST API handlers and utilities that are used by JupyterLab.
It is a separate project in order to accommodate creating JupyterLab-like
applications from a more limited scope.}


%description %_description

%package -n     python3-jupyterlab-server
Summary:        %{summary}

%description -n python3-jupyterlab-server %_description


%prep
%autosetup -p1 -n jupyterlab_server-%{version}
# jupyterlab-server[openapi] and its tests depend on this chain:
# - openapi_core
#   - pathable
#   - jsonschema-spec
#   - openapi-spec-validator
#     - jsonschema-spec
#       - pathable
sed -i '/"openapi-spec-validator/d' pyproject.toml
sed -i '/"openapi_core/d' pyproject.toml
sed -i '/"jupyterlab_server\[openapi\]/d' pyproject.toml
# Remove also coverage deps from tests
sed -i '/"pytest-cov/d' pyproject.toml
sed -i '/"codecov/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jupyterlab_server


%check
# We need to skip some tests to run them without openapi_core
# test_which uses unversioned python command
# test_process_app timeouts in COPR
%pytest --ignore=tests/test_{labapp,listings_api,settings_api,themes_api,translation_api,workspaces_api}.py \
        -k "not test_which and not test_process_app"

%files -n python3-jupyterlab-server -f %{pyproject_files}
%doc README.md


%changelog
* Thu Jan 19 2023 Lumír Balhar <lbalhar@redhat.com> - 2.19.0-1
- Update to 2.19.0 (rhbz#2161301)

* Tue Jan 10 2023 Lumír Balhar <lbalhar@redhat.com> - 2.18.0-1
- Update to 2.18.0 (rhbz#2157908)

* Mon Jan 02 2023 Lumír Balhar <lbalhar@redhat.com> - 2.17.0-1
- Update to 2.17.0 (rhbz#2156011)

* Sun Dec 04 2022 Lumír Balhar <lbalhar@redhat.com> - 2.16.3-1
- Initial package