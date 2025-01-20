Name:           python-kanboard
Version:        1.1.6
Release:        2%{?dist}
Summary:        Client library for Kanboard API

License:        MIT
URL:            https://github.com/kanboard/python-api-client
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Kanboard is project management software that focuses on the Kanban
methodology.

This package provides client library for Kanboard API.
}

%description %_description

%package -n python3-kanboard
Summary:        %{summary}

%description -n python3-kanboard %_description


%prep
%autosetup -p1 -n python-api-client-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files kanboard


%check
%{python3} -m unittest


%files -n python3-kanboard -f %{pyproject_files}
%doc README.rst
%doc LICENSE


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 13 2024 Alois Mahdal <n9042e84@vornet.cz> - 1.1.6-1
- Update to 1.1.6 (close RHBZ#2331054)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.5-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.5-2
- Rebuilt for Python 3.12

* Tue Feb 14 2023 Alois Mahdal <n9042e84@vornet.cz> - 1.1.5-1
- Update to 1.1.5 (close RHBZ#2169228)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Alois Mahdal <n9042e84@vornet.cz> - 1.1.4-1
- Update to 1.1.4 (close RHBZ#2117947)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.3-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild


* Fri Jan 14 2022 Alois Mahdal <n9042e84@vornet.cz> - 1.1.3-1
- initial packaging
