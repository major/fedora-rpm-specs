Name:		dt-schema
Version:	2024.05
Release:	3%{?dist}
Summary:	Tooling for devicetree validation using YAML and jsonschema
License:	BSD-2-Clause
URL:		http://devicetree.org/
Source0:	https://github.com/devicetree-org/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	gcc
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm

%description
This tool contains test code for devicetree schema validation using the
json-schema vocabulary. Schema files are written in YAML (a superset of
JSON), and operate on the YAML encoding of Devicetree data. Devicetree
data must be transcoded from DTS to YAML before being used by this tool.

%prep
%autosetup -p1

# Working with upstream to resolve.
sed -i 's/>=4.1.2,<4.18//'  pyproject.toml
sed -i 's/pylibfdt/libfdt/' pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files dtschema

%check
%py3_check_import dtschema

%files -f %{pyproject_files}
%license LICENSE.txt
%{_bindir}/dt*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 23 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 2024.05-1
- Initial package
