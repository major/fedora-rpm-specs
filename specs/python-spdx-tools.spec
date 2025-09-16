%global pypi_name spdx-tools
%global github_name tools-python

Name:           python-%{pypi_name}
Version:        0.8.3
Release:        %autorelease
Summary:        Python library to parse, validate and create SPDX documents

License:        Apache-2.0
URL:            https://github.com/spdx/tools-python
Source:         %url/archive/v%{version}/%{github_name}-%{version}.tar.gz

# Update excepted typecheck error after beartype update
# https://github.com/spdx/tools-python/pull/841
# https://github.com/spdx/tools-python/commit/6817ca7056cadfd71c5619b7d75452461e4bbb18
Patch:          0001-Update-excepted-typecheck-error-after-beartype-updat.patch
# relationship_writer: properly access __annotations__ dict #858
# https://github.com/spdx/tools-python/pull/858
Patch:          0002-relationship_writer-properly-access-__annotations__-.patch

BuildArch:      noarch
BuildRequires:  help2man
BuildRequires:  python3-devel
BuildRequires:  python3dist(pyshacl)
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
Python library to parse, validate and create SPDX documents.

Features:

 - API to create and manipulate SPDX v2.2 and v2.3 documents
 - Parse, convert, create and validate SPDX files
 - supported formats: Tag/Value, RDF, JSON, YAML, XML
 - visualize the structure of a SPDX document by creating an AGraph. Note: This
   is an optional feature and requires additional installation of optional
   dependencies.
 - experimental support for the upcoming SPDX v3 specification. Note, however,
   that support is neither complete nor stable at this point, as the spec is
   still evolving. SPDX3-related code is contained in a separate subpackage
   "spdx3" and its use is optional. We do not recommend using it in production
   code yet.}

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
%pyproject_save_files spdx_tools
mkdir -p %{buildroot}%{_mandir}/man1/
PYTHONPATH=%{buildroot}%{python3_sitelib} help2man --no-discard-stderr --version-string=%{version} -s 1 -N -o %{buildroot}%{_mandir}/man1/pyspdxtools.1 %{buildroot}%{_bindir}/pyspdxtools

%check
%pytest -k "not test_spdx2_convert_to_spdx3 and not test_json_writer and not test_write_tag_value"
rm -rfv %{buildroot}%{python3_sitelib}/spdx_tools/spdx/parser/tagvalue/parser.out \
        %{buildroot}%{python3_sitelib}/spdx_tools/spdx/parser/tagvalue/parsetab.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md CONTRIBUTING.md README.md 
%doc examples/
%license LICENSE
%{_bindir}/pyspdxtools*
%{_mandir}/man1/pyspdxtools.1*

%changelog
%autochangelog
