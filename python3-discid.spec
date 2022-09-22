%global srcname python3-discid
%global sum Libdiscid Python bindings
%global desc Python-discid implements Python bindings for MusicBrainz libdiscid.

Name:    %{srcname}
Version: 1.2.0
Release: 6%{?dist}
Summary: %{sum}
URL:     https://github.com/JonnyJD/python-discid
License: LGPLv3+

Source0: https://github.com/JonnyJD/python-discid/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx

Requires: libdiscid


%description
%{desc}

%prep
%autosetup -n python-discid-%{version}

%build
%py3_build

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc/ html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files
%{python3_sitelib}/discid-*.egg-info
%{python3_sitelib}/discid/
%license COPYING COPYING.LESSER
%doc README.rst CHANGES.rst
%docdir /html

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.10

* Mon May 17 2021 Matthew Ruszczyk <mruszczyk17@gmail.com> - 1.2.0-1
- Initial RPM release
