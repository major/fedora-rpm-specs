Name:           python-systemd
Version:        235
Release:        %autorelease
Summary:        Python module wrapping libsystemd functionality

License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/python-systemd
Source0:        https://github.com/systemd/python-systemd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  systemd-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  web-assets-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Python module for native access to the libsystemd facilities. Functionality
includes sending of structured messages to the journal and reading journal
files, querying machine and boot identifiers and a lists of message identifiers
provided by systemd. Other functionality provided the library is also wrapped.}

%description %_description

%package -n python3-systemd
Summary:        %{summary}

%{?python_provide:%python_provide python3-systemd}
Provides:       systemd-python3 = %{version}-%{release}
Provides:       systemd-python3%{?_isa} = %{version}-%{release}
Obsoletes:      systemd-python3 < 230

%description -n python3-systemd %_description

%package doc
Summary:        HTML documentation for %{name}
Requires:       js-jquery

%description doc
%{summary}.

%prep
%autosetup -p1
sed -i 's/py\.test/pytest/' Makefile

%build
make PYTHON=%{__python3} build
make PYTHON=%{__python3} SPHINX_BUILD=sphinx-build-3 sphinx-html
rm -r build/html/.buildinfo build/html/.doctrees

%install
%make_install PYTHON=%{__python3}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -rv build/html %{buildroot}%{_pkgdocdir}/
ln -vsf %{_jsdir}/jquery/latest/jquery.min.js %{buildroot}%{_pkgdocdir}/html/_static/jquery.js
cp -p README.md NEWS %{buildroot}%{_pkgdocdir}/

%check
# if the socket is not there, skip doc tests
test -f /run/systemd/journal/stdout || \
     sed -i 's/--doctest[^ ]*//g' pytest.ini
make PYTHON=%{__python3} check

%files -n python3-systemd
%license LICENSE.txt
%doc %{_pkgdocdir}
%exclude %{_pkgdocdir}/html
%{python3_sitearch}/systemd/
%{python3_sitearch}/systemd_python*.egg-info

%files doc
%doc %{_pkgdocdir}/html

%changelog
%autochangelog
