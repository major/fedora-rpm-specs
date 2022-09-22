Name:           python-mpd2
Version:        3.0.5
Release:        %autorelease
Summary:        Python library providing a client interface for MPD

License:        LGPLv3+
URL:            https://github.com/Mic92/python-mpd2
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{_bindir}/tox

%description
Python library providing a client interface for MPD.

%package -n python3-mpd2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Summary:        Python 3 mpd2 module

%description -n python3-mpd2
Python3 library providing a client interface for MPD.


%package doc
Summary:    Examples for %{name}

%description doc
This package contains examples for %{name}.

%prep
%autosetup -n %{name}-%{version}
echo "whitelist_externals = coverage" >> tox.ini

# Remove unecessary shebang
sed -i '/^#!\/usr\/bin\/env.*python$/ d' mpd/tests.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mpd

%check
%{tox}

%files -n python3-mpd2 -f %{pyproject_files}
%doc README.rst

%files doc
%license LICENSE.txt
%doc examples


%changelog
%autochangelog
