Name:      python-pathvalidate
Version:   2.5.2
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
