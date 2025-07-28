Name:    python3-discid
Version: 1.3.0
Release: %autorelease
Summary: Libdiscid Python bindings
URL:     https://github.com/metabrainz/python-discid
License: LGPL-3.0-or-later

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: libdiscid
BuildRequires: python3-devel
BuildRequires: python3dist(pytest)

Requires: libdiscid


%description
Python-discid implements Python bindings for MusicBrainz libdiscid.


%prep
%autosetup -n python-discid-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files discid


%check
%pytest


%files -f %{pyproject_files}
%license COPYING COPYING.LESSER
%doc README.rst CHANGES.rst


%changelog
%autochangelog
