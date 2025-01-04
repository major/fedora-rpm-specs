%global srcname pretty-yaml

Name:          python-%{srcname}
Version:       25.1.0
Release:       %autorelease
Summary:       A module to produce a bit more pretty and human-readable YAML-serialized data

License:       WTFPL
URL:           https://github.com/mk-fg/pretty-yaml
Source:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3dist(pytest)
BuildRequires: help2man

%global _description %{expand:
PyYAML-based python module to produce a bit more pretty and human-readable
YAML-serialized data.

This module is for serialization only, see ruamel.yaml module for literate YAML
parsing (keeping track of comments, spacing, line/column numbers of values,
etc).}

%description %{_description}

%package -n python3-%{srcname}
Summary:    %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L pyaml
mkdir -p %{buildroot}%{_mandir}/man1
export PYTHONPATH="$PYTHONPATH:%{buildroot}%{python3_sitelib}"
help2man --no-discard-stderr %{buildroot}%{_bindir}/pyaml -o %{buildroot}%{_mandir}/man1/pyaml.1

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license COPYING
%{_mandir}/man1/pyaml.1*
%{_bindir}/pyaml

%changelog
%autochangelog
