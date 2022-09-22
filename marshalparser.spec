Name:           marshalparser
Version:        0.3.1
Release:        3%{?dist}
Summary:        Parser for Python internal Marshal format

License:        MIT
URL:            https://github.com/fedora-python/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# For tests on various pyc files
BuildRequires:  python3.6
BuildRequires:  python3.7
BuildRequires:  python3.8
BuildRequires:  python3.9
BuildRequires:  python3.10

%generate_buildrequires
%pyproject_buildrequires -t

%description
Parser for Python internal Marshal format which can fix pyc files
reproducibility.

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
%tox

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.1-2
- Rebuilt for Python 3.11

* Mon May 16 2022 Lumír Balhar <lbalhar@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 13 2021 Lumír Balhar <lbalhar@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.6-2
- Rebuilt for Python 3.10

* Fri Apr 30 2021 Lumír Balhar <lbalhar@redhat.com> - 0.2.6-1
- Update to 0.2.6

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Lumír Balhar <lbalhar@redhat.com> - 0.2.5-1
- Update to 0.2.5

* Tue Dec 08 2020 Lumír Balhar <lbalhar@redhat.com> - 0.2.4-1
- Update to 0.2.4

* Wed Nov 11 2020 Lumír Balhar <lbalhar@redhat.com> - 0.2.3-1
- Update to 0.2.3 (#1896208)

* Tue Nov 10 2020 Lumír Balhar <lbalhar@redhat.com> - 0.2.2-1
- Update to 0.2.2 (#1896208)

* Wed Sep 16 2020 Lumír Balhar <lbalhar@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Wed Jul 29 2020 Lumír Balhar <lbalhar@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Lumír Balhar <lbalhar@redhat.com> - 0.1.1-1
- Initial package
