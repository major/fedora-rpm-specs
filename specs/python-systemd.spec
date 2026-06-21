Name:           python-systemd
Version:        236
Release:        %autorelease
Summary:        Python module wrapping libsystemd functionality

License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/python-systemd
Source0:        https://github.com/systemd/python-systemd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  systemd-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-meson-python
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

%build
%pyproject_wheel -Csetup-args="-Ddocs=true"

%install
%pyproject_install
%pyproject_save_files -L systemd

mkdir -p %{buildroot}%{_pkgdocdir}
mv %{buildroot}/usr/doc/python-systemd/html %{buildroot}%{_pkgdocdir}/
ln -vsf --relative %{_jsdir}/jquery/latest/jquery.min.js %{buildroot}%{_pkgdocdir}/html/_static/jquery.js
cp -p README.md NEWS %{buildroot}%{_pkgdocdir}/

%check
%pytest -v %{buildroot}%{python3_sitearch}/systemd/test/

%files -n python3-systemd -f %{pyproject_files}
%license LICENSE.txt
%doc %{_pkgdocdir}
%exclude %{_pkgdocdir}/html

%files doc
%doc %{_pkgdocdir}/html

%changelog
%autochangelog
