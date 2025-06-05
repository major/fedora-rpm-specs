# enable http extra
# pyshacl_server needs -x http to work, with python-sanic and python-sanic-ext
# which are not packaged.
# (python3dist(sanic) < 23~~ with python3dist(sanic) >= 22.12)
# (python3dist(sanic-ext) < 23.6~~ with python3dist(sanic-ext) >= 23.3)
%bcond http 0

%global pypi_name pyshacl

Name:           python-pyshacl
Version:        0.30.1
Release:        %autorelease
Summary:        Python validator for SHACL

License:        Apache-2.0
URL:            https://github.com/RDFLib/pySHACL
Source:         %{url}/archive/v%{version}/pyshacl-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
This is a pure Python module which allows for the validation of RDF graphs
against Shapes Constraint Language (SHACL) graphs. This module uses the rdflib
Python library for working with RDF and is dependent on the OWL-RL Python module
for OWL2 RL Profile based expansion of data graphs.}

%description %_description

%package -n python3-pyshacl
Summary:        %{summary}

%description -n python3-pyshacl %_description

%if %{with http}
%pyproject_extras_subpkg -n python3-pyshacl http
%endif

%prep
%autosetup -p1 -n pySHACL-%{version}
rm -rfv pyshacl/*.spec

# python-rdflib doesn't ship the html modul so it's not required by pySHACL
# https://github.com/RDFLib/pySHACL/commit/5e93bd42e2259c980599533dbbe4a8036487283c
sed -i '/rdflib/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t %{?with_http:-x http}

%build
%pyproject_wheel

%install
%pyproject_install

mkdir -p %{buildroot}%{_mandir}/man1/
%py3_test_envvars help2man --no-discard-stderr pyshacl -o %{buildroot}%{_mandir}/man1/pyshacl.1
%if %{with http}
%py3_test_envvars help2man --no-discard-stderr pyshacl_server -o %{buildroot}%{_mandir}/man1/pyshacl_server.1
%endif
%py3_test_envvars help2man --no-discard-stderr pyshacl_validate -o %{buildroot}%{_mandir}/man1/pyshacl_validate.1

%if %{without http}
rm -rfv %{buildroot}%{_bindir}/pyshacl_server
%endif

# Fix permissions
chmod +x %{buildroot}%{python3_sitelib}/pyshacl/cli.py

# remove duplicate md files
pushd %{buildroot}%{python3_sitelib}
rm -rfv CHANGELOG.md \
        CONTRIBUTING.md \
        CONTRIBUTORS.md \
        FEATURES.md \
        LICENSE.txt \
        README.md
popd

%pyproject_save_files -L pyshacl

# Deduplicate, the binaries are identical, the script uses arg0 to determine
# the function to run.
%fdupes %{buildroot}%{_bindir}
%fdupes %{buildroot}%{python3_sitelib}

%check
# Disable network dependent tests
# Disable test_js depending on not packaged pyduktape2
%pytest -k "not test_cmdline_web and not test_cmdline_jsonld and not \
            test_web_retrieve and not test_web_retrieve_fail and not \
            test_owl_imports and not test_owl_imports_fail and not \
            test_98 and not test_108 and not test_154 and not test_js"

%files -n python3-pyshacl -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS.md  FEATURES.md README.md
%{_bindir}/pyshacl
%{_bindir}/pyshacl_rules
%if %{with http}
%{_bindir}/pyshacl_server
%endif
%{_bindir}/pyshacl_validate
%{_mandir}/man1/pyshacl*.1*

%changelog
%autochangelog
