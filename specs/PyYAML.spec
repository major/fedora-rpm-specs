Name:           PyYAML
Version:        6.0.2
Release:        %autorelease
Summary:        YAML parser and emitter for Python

# SPDX
License:        MIT
URL:            https://github.com/yaml/pyyaml
Source:         https://github.com/yaml/pyyaml/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libyaml-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%global _description\
YAML is a data serialization format designed for human readability and\
interaction with scripting languages.  PyYAML is a YAML parser and\
emitter for Python.\
\
PyYAML features a complete YAML 1.1 parser, Unicode support, pickle\
support, capable extension API, and sensible error messages.  PyYAML\
supports standard YAML tags and provides Python-specific tags that\
allow to represent an arbitrary Python object.\
\
PyYAML is applicable for a broad range of tasks from complex\
configuration files to object serialization and persistence.

%description %_description


%package -n python3-pyyaml
Summary:        %summary
%py_provides    python3-yaml
%py_provides    python3-PyYAML

%description -n python3-pyyaml %_description


%prep
%autosetup -p1 -n pyyaml-%{version}
chmod a-x examples/yaml-highlight/yaml_hl.py

# remove pre-generated file
rm -rf ext/_yaml.c


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files yaml _yaml


%check
%pytest


%files -n python3-pyyaml -f %{pyproject_files}
%doc CHANGES README.md examples


%changelog
%autochangelog
