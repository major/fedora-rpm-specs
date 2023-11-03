%global pypi_name spdx-tools
%global github_name tools-python

Name:           python-%{pypi_name}
# 0.8.0 is out, but we need to wait until
# https://github.com/nexB/scancode-toolkit/pull/3456 is merged
# Update: merged, needs to be release
Version:        0.7.1
Release:        %autorelease
Summary:        Python library to parse, validate and create SPDX documents

License:        Apache-2.0
URL:            https://github.com/spdx/tools-python
Source:         %url/archive/v%{version}/%{github_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  help2man
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
Python library to parse, validate and create SPDX documents.

Features:

 - API to create and manipulate SPDX v2.2 and v2.3 documents
 - Parse, convert, create and validate SPDX files
 - supported formats: Tag/Value, RDF, JSON, YAML, XML
 - visualize the structure of a SPDX document by creating an AGraph. Note: This
   is an optional feature and requires additional installation of optional
   dependencies.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -p1 -n %{github_name}-%{version}
sed -i '/\[tool\.setuptools_scm\]/a fallback_version = "%{version}"' pyproject.toml
for lib in $(find . -type f -iname "*.py"); do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files spdx
mkdir -p %{buildroot}%{_mandir}/man1/
PYTHONPATH=%{buildroot}%{python3_sitelib} help2man --no-discard-stderr --version-string=%{version} -s 1 -N -o %{buildroot}%{_mandir}/man1/pyspdxtools_convertor.1 %{buildroot}%{_bindir}/pyspdxtools_convertor
PYTHONPATH=%{buildroot}%{python3_sitelib} help2man --no-discard-stderr --version-string=%{version} -s 1 -N -o %{buildroot}%{_mandir}/man1/pyspdxtools_parser.1 %{buildroot}%{_bindir}/pyspdxtools_parser

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md CONTRIBUTING.md README.md 
%doc examples/
%license LICENSE
%{_bindir}/pyspdxtools*
%{_mandir}/man1/pyspdxtools*.1*

%changelog
%autochangelog
