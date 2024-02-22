%global pypi_name xmlschema
Name:           python-%{pypi_name}
Version:        2.4.0
Release:        %autorelease
Summary:        A Python XML Schema validator and decoder

License:        MIT
URL:            https://github.com/brunato/xmlschema
Source0:        %{pypi_source}

# Skip tests requiring an internet connection
Patch:          https://github.com/sissaschool/xmlschema/pull/365.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
The xmlschema library is an implementation of XML Schema for Python.

This library arises from the needs of a solid Python layer for processing XML
Schema based files for MaX (Materials design at the Exascale) European project.
A significant problem is the encoding and the decoding of the XML data files
produced by different simulation software. Another important requirement is
the XML data validation, in order to put the produced data under control.
The lack of a suitable alternative for Python in the schema-based decoding
of XML data has led to build this library. Obviously this library can be
useful for other cases related to XML Schema based processing, not only for
the original scope.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}  %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
sed -i 's/~=/>=/' setup.py tox.ini  # https://bugzilla.redhat.com/show_bug.cgi?id=1758141
sed -i 's/==/>=/' tox.ini  # too strict test deps
sed -i '/memory_profiler/d' tox.ini # optional test dep, not packaged in Fedora, not worth testing
%py3_shebang_fix %{pypi_name}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/xmlschema-json2xml
%{_bindir}/xmlschema-validate
%{_bindir}/xmlschema-xml2json


%changelog
%autochangelog
