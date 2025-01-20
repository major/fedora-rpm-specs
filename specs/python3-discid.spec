Name:    python3-discid
Version: 1.2.0
Release: 16%{?dist}
Summary: Libdiscid Python bindings
URL:     https://github.com/JonnyJD/python-discid
License: LGPL-3.0-or-later

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
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
%{python3} setup.py check


%files -f %{pyproject_files}
%license COPYING COPYING.LESSER
%doc README.rst CHANGES.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.0-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.0-10
- Rebuilt for Python 3.12

* Mon Apr 24 2023 Peter Oliver <rpm@mavit.org.uk> - 1.2.0-9
- SPDX migration.

* Sat Mar 25 2023 Peter Oliver <rpm@mavit.org.uk> - 1.2.0-8
- Don’t build the documentation (since we weren’t installing it anyway).
  Fixes #2180481.
- Follow latest Python packaging guidelines.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
