Name:           python-x2go
Version:        0.6.1.4
Release:        %autorelease
Summary:        Python module providing X2Go client API

License:        AGPL-3.0-or-later
URL:            https://www.x2go.org/
Source0:        https://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
# Rename SafeConfigParser to ConfigParser
Patch0:         https://gitlab.x2go.org/x2go/client/libs/python-x2go/-/merge_requests/7.patch

BuildArch:      noarch

BuildRequires: make

%description
X2Go is a server based computing environment with:
   - session resuming
   - low bandwidth support
   - session brokerage support
   - client side mass storage mounting support
   - audio support
   - authentication by smartcard and USB stick

This Python module allows you to integrate X2Go client support into your
Python applications by providing a Python-based X2Go client API.


%package        doc
Summary:        Python X2Go client API documentation

%description    doc
This package contains the Python X2Go client API documentation.


%package -n python%{python3_pkgversion}-x2go
Summary:        Python module providing X2Go client API
BuildRequires:  python%{python3_pkgversion}-devel
# For doc build
BuildRequires:  /usr/bin/sphinx-build-3
BuildRequires:  python%{python3_pkgversion}-xlib
Requires:       nxproxy
Requires:       python%{python3_pkgversion}-requests
# Prefered over json
Requires:       python%{python3_pkgversion}-simplejson
Requires:       python%{python3_pkgversion}-xlib


%description -n python%{python3_pkgversion}-x2go
X2Go is a server based computing environment with:
   - session resuming
   - low bandwidth support
   - session brokerage support
   - client side mass storage mounting support
   - audio support
   - authentication by smartcard and USB stick

This Python module allows you to integrate X2Go client support into your
Python applications by providing a Python-based X2Go client API.


%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
make -C docs SPHINXBUILD=/usr/bin/sphinx-build-3 html

%install
%pyproject_install
%pyproject_save_files -l x2go

%files -n python%{python3_pkgversion}-x2go -f %{pyproject_files}
%doc ChangeLog README* TODO

%files doc
%doc docs/build/html

%changelog
%autochangelog
