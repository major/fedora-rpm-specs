Name:           python-yte
Version:        1.5.4
Release:        %autorelease
Summary:        YAML template engine with Python expressions

# SPDX
License:        MIT
URL:            https://github.com/yte-template-engine/yte
# GitHub archive contains tests; PyPI sdist does not
Source0:        %{url}/archive/v%{version}/yte-%{version}.tar.gz
# Man page written for Fedora in groff_man(7) format based on --help output
Source1:        yte.1

BuildArch:      noarch

BuildRequires:  python3-devel

# For tests, from [tool.poetry.dev-dependencies] in pyproject.toml, with
# coverage/linters/etc. removed and version upper bounds removed:
BuildRequires:  python3dist(pytest) >= 7.0

%global common_description %{expand:
YTE is a template engine for YAML format that utilizes the YAML structure in
combination with Python expressions for enabling to dynamically build YAML
documents.

The key idea of YTE is to rely on the YAML structure to enable conditionals,
loops and other arbitrary Python expressions to dynamically render YAML files.
Python expressions are thereby declared by prepending them with a ? anywhere in
the YAML. Any such value will be automatically evaluated by YTE, yielding plain
YAML as a result. Importantly, YTE templates are still valid YAML files (for
YAML, the ? expressions are just strings).

Documentation of YTE can be found at https://yte-template-engine.github.io.}

%description %{common_description}


%package -n python3-yte
Summary:        %{summary}

%description -n python3-yte %{common_description}


%prep
%autosetup -n yte-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files yte
install -t '%{buildroot}%{_mandir}/man1' -m 0644 -p -D '%{SOURCE1}'


%check
%pytest tests.py


%files -n python3-yte -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%doc docs/main.md

%{_bindir}/yte
%{_mandir}/man1/yte.1*


%changelog
%autochangelog
