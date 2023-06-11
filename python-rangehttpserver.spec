%global desc %{expand: \
SimpleHTTPServer with support for Range requests.}

Name:           python-rangehttpserver
Version:        1.3.3
Release:        %autorelease
Summary:        SimpleHTTPServer with support for Range requests

License:        Apache-2.0
URL:            https://github.com/danvk/RangeHTTPServer
Source0:        %{url}/archive/%{version}/RangeHTTPServer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: python3dist(pytest)

%description
%{desc}

%package -n python3-rangehttpserver
Summary: %{summary}

Requires: python3dist(requests)
%description -n python3-rangehttpserver
%{desc}

%prep
%autosetup -n RangeHTTPServer-%{version}

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} ';'

# the server_test removed because need network
# Upstream Issue
# https://github.com/danvk/RangeHTTPServer/issues/21
rm -rf tests/server_test.py

chmod 0644 RangeHTTPServer/__init__.py RangeHTTPServer/__main__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files RangeHTTPServer

%check
%{pytest}

%files -n python3-rangehttpserver -f %{pyproject_files}
%license LICENSE
%doc README

%changelog
%autochangelog
