Name:           python-strictyaml
Version:        1.7.3
Release:        %autorelease
Summary:        Parses and validates a restricted subset of YAML

# SPDX
License:        MIT
URL:            http://hitchdev.com/strictyaml
%global forgeurl https://github.com/crdoconnor/strictyaml
Source0:        %{forgeurl}/archive/%{version}/strictyaml-%{version}.tar.gz
# https://github.com/crdoconnor/strictyaml/issues/152
Source1:        https://sourceforge.net/p/ruamel-yaml/code/ci/0.16.13/tree/LICENSE?format=raw#/LICENSE-ruamel-yaml

BuildArch:      noarch

BuildRequires:  python3-devel

# We do not attempt to build the documentation, since it requires an
# idiosyncratic build system (see https://hitchdev.com/) that is hopelessly
# entangled with the idea of downloading dependencies from PyPI. An offline
# build would be nearly impossible.

%global common_description %{expand:
StrictYAML is a type-safe YAML parser that parses and validates a restricted
subset of the YAML specification.

Priorities:

  • Beautiful API
  • Refusing to parse the ugly, hard to read and insecure features of YAML like
    the Norway problem.
  • Strict validation of markup and straightforward type casting.
  • Clear, readable exceptions with code snippets and line numbers.
  • Acting as a near-drop in replacement for pyyaml, ruamel.yaml or poyo.
  • Ability to read in YAML, make changes and write it out again with comments
    preserved.
  • Not speed, currently.}

%description %{common_description}


%package -n     python3-strictyaml
Summary:        %{summary}

# Upstream bundled/vendored a slightly older version of ruamel.yaml after an
# update with API changes was too difficult to support. This is intended to be
# a temporary workaround until the vendored library can be replaced with a
# custom parser for StrictYAML. See
# https://github.com/crdoconnor/strictyaml/issues/151 for discussion, and
# strictyaml/ruamel/__init__.py for version information.
Provides:       bundled(python3dist(ruamel-yaml)) = 0.16.13

%description -n python3-strictyaml %{common_description}


%prep
%autosetup -n strictyaml-%{version}
cp -p '%{SOURCE1}' .
# Upstream’s idiosyncratic build system normally handles this:
sed -r -i 's/(__version__ *= *")DEVELOPMENT_VERSION"/\1%{version}"/' \
    'strictyaml/__init__.py'


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l strictyaml


%check
# There are no tests. (If there were, it would be as hard to run them as it is
# to build the documentation.) We therefore do an import-only “smoke test.” We
# must skip one module in the bundled ruamel-yaml because it does not include
# the compiled C extension (_ruamel_yaml).
%pyproject_check_import -e strictyaml.ruamel.cyaml


%files -n python3-strictyaml -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
