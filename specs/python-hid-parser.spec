%bcond_without check
%global pname hid-parser
%global commit 4b7944f4999e152c678cd7fa76278b7e2535c3ff
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20211206

Name:           python-hid-parser
Version:        0.0.3
Release:        14.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:        Parse HID report descriptors
License:        MIT
URL:            https://github.com/usb-tools/python-hid-parser
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# compatibility with pytest 8
# downstream-only patch, upstream seems dead
# https://github.com/usb-tools/python-hid-parser/pull/23
Patch:          https://github.com/usb-tools/python-hid-parser/pull/23.patch#/%{name}-pytest-8.patch
# https://github.com/usb-tools/python-hid-parser/pull/18
Patch:          https://github.com/usb-tools/python-hid-parser/pull/18.patch#/%{name}-fix-GenericDesktopControls-Rz.patch
# backport fix from solaar fork
Patch:          %{name}-solaar.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _desc %{expand:
python-hid-parser is a typed pure Python library to parse HID report
descriptors.
}

%description %_desc

%package     -n python3-%{pname}
Summary:        %{summary}

%description -n python3-%{pname} %_desc

%prep
%autosetup -p1 -n %{name}-%{commit}
%generate_buildrequires
%if %{with check}
%pyproject_buildrequires -x test
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hid_parser

%if %{with check}
%check
%pytest
%endif

%files -n python3-%{pname} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.0.3-14.20211206git4b7944f
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-13.20211206git4b7944f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.0.3-12.20211206git4b7944f
- Rebuilt for Python 3.14

* Fri May 09 2025 Dominik Mierzejewski <dominik@greysector.net> - 0.0.3-11.20211206git4b7944f
- update to 20211206 snapshot
- backport fixes from Solaar and upstream PRs

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-10.20210228git7d94740
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-9.20210228git7d94740
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.3-8.20210228git7d94740
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-7.20210228git7d94740
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-6.20210228git7d94740
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5.20210228git7d94740
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.0.3-4.20210228git7d94740
- Rebuilt for Python 3.12

* Fri Apr 21 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.0.3-3.20210228git7d94740
- update to latest git HEAD

* Wed Mar 08 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.0.3-2
- use automatic BuildRequires generation
- conditionalize running tests

* Fri Jan 06 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.0.3-1
- initial build for Fedora
