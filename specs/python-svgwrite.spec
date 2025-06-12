%global pypi_name svgwrite

Name:           python-%{pypi_name}
Version:        1.4.3
Release:        %autorelease
Summary:        Python library to create SVG drawings

License:        MIT
URL:            https://github.com/mozman/svgwrite
Source0:        %{pypi_name}-%{version}.zip
Patch0:         0001-Skip-test-that-needs-internet-connection.patch

BuildArch: noarch

%description
Python library to create SVG drawings.

%package -n     python3-%{pypi_name}
Summary:        Python 3 library to create SVG drawings
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pyparsing
BuildRequires:  python3-pytest
Requires:       python3-setuptools
Requires:       python3-pyparsing
%{?python_provide:%python_provide python3-%{pypi_name}}

%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{pypi_name}
Python 3 library to create SVG drawings.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%pyproject_wheel


%install
%pyproject_install
# Remove shebang
for lib in %{buildroot}%{python3_sitelib}/%{pypi_name}/{,*/}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%check
%{__python3} -m unittest discover -s tests

%files -n python3-%{pypi_name}
%license LICENSE.TXT
%doc NEWS.rst README.rst
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{python3_sitelib}/%{pypi_name}/


%changelog
%autochangelog
