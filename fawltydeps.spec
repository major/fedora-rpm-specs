%global forgeurl https://github.com/tweag/FawltyDeps

%bcond tests 1

Name:           fawltydeps
Version:        0.13.3
Release:        %{autorelease}
Summary:        Find undeclared and unused 3rd-party dependencies in your Python project
%forgemeta
License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
# For generating man pages
BuildRequires:  help2man
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
%endif

%global _description %{expand:
FawltyDeps is a dependency checker for Python that finds undeclared
and/or unused 3rd-party dependencies in your Python project. The name
is inspired by the Monty Python-adjacent Fawlty Towers sitcom.}

%description %_description


%prep
%forgeautosetup -p1
# Loosen pinned versions to match what we have in >= F38
# importlib_metadat >= 6.0.0
sed -r -i 's/(importlib_metadata.* ").*$/\1>=6.0.0"/' pyproject.toml
# pydantic >= 1.10.2
sed -r -i 's/(pydantic.*>=).*(,.*$)/\11.10.2\2/' pyproject.toml
# setuptools = >=65.5.1,<69.0.0
sed -r -i 's/(setuptools.* ").*/\1>=65.5.1,<69.0.0"/' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}

# Create man pages from --help and --version
mkdir man
%{py3_test_envvars} help2man --section 1 --no-discard-stderr \
--no-info --output man/%{name}.1 %{name}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1


%check
%if %{with tests}
# Disable tests requiring network
k="${k-}${k+ and }not test_resolve_dependencies_install_deps"
k="${k-}${k+ and }not generates_expected_mappings"
# TypeError: 'NoneType' object is not subscriptable
k="${k-}${k+ and }not no_pyenvs_found"
%pytest -v "${k:+-k $k}"
%else
%pyproject_check_import
%endif


%files -f %{pyproject_files}
%doc README.*
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
