Name:      python-pathvalidate
Version:   3.2.1
Release:   1%{?dist}
Summary:   Library to sanitize/validate a string such as file-names/file-paths/etc

License:   MIT
URL:       https://github.com/thombashi/pathvalidate
Source0:   %{pypi_source pathvalidate}
BuildArch: noarch

%description
%{summary}.

%package -n python3-pathvalidate
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-allpairspy
BuildRequires:  python3-click
BuildRequires:  python3-tcolorpy

%description -n python3-pathvalidate
%{summary}.

%prep
%autosetup -n pathvalidate-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files pathvalidate


%check
%{pytest}


%files -n python3-pathvalidate -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
* Sat Aug 24 2024 Jonny Heggheim <hegjon@gmail.com> - 3.2.1-1
- Updated to version 3.2.1

* Sat Jul 27 2024 Sandro <devel@penguinpee.nl> - 3.2.0-5
- Adapt tests for Python >= 3.13 (RHBZ#2259547)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Jonny Heggheim <hegjon@gmail.com> - 3.2.0-1
- Updated to version 3.2.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.5.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 21 2022 Jonny Heggheim <hegjon@gmail.com> - 2.5.2-1
- Updated to version 2.5.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jonny Heggheim <hegjon@gmail.com> - 2.5.0-5
- Disable tests on Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.5.0-4
- Rebuilt for Python 3.11

* Wed Mar 16 2022 Jonny Heggheim <hegjon@gmail.com> - 2.5.0-3
- Migrated to the %pyproject RPM macros

* Fri Feb 25 2022 Jonny Heggheim <hegjon@gmail.com> - 2.5.0-2
- Enabled unit tests

* Thu Feb 24 2022 Jonny Heggheim <hegjon@gmail.com> - 2.5.0-1
- Updated to version 2.5.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.2-3
- Rebuilt for Python 3.10

* Fri Mar 19 2021 Jonny Heggheim <hegjon@gmail.com> - 2.3.2-2
- Enabled unit tests

* Fri Mar 05 2021 Jonny Heggheim <hegjon@gmail.com> - 2.3.2-1
- Initial package
