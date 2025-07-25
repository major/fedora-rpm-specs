%bcond tests 1

Name:           fawltydeps
Version:        0.20.0
Release:        %{autorelease}
Summary:        Find undeclared and unused 3rd-party dependencies in your Python project

%global forgeurl https://github.com/tweag/FawltyDeps
%global tag v%{version}
%forgemeta

License:        MIT
URL:            https://tweag.github.io/FawltyDeps/
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


%pyproject_extras_subpkg -n %{name} uv


%prep
%forgeautosetup -p1

# Don't impose upper bounds (= "^x.y")
sed -r \
    -e 's/\^([0-9])/>=\1/g' \
    -i pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x uv


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
%pyproject_check_import
%if %{with tests}
# Disable tests requiring network
k="${k-}${k+ and }not test_resolve_dependencies_install_deps"
k="${k-}${k+ and }not generates_expected_mappings"
# TypeError: 'NoneType' object is not subscriptable
k="${k-}${k+ and }not no_pyenvs_found"
%pytest -r fEs "${k:+-k ${k:-}}"
%endif


%files -f %{pyproject_files}
%doc README.*
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
