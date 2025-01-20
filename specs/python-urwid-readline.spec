%global upstream_name urwid_readline
Name:           python-urwid-readline
Version:        0.15.1
Release:        2%{?dist}
Summary:        A textbox edit widget for urwid that supports readline shortcuts

License:        MIT
URL:            https://github.com/rr-/urwid_readline
Source0:        %{url}/archive/%{version}/%{upstream_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%global _description %{expand:
A textbox edit widget for urwid that supports readline shortcuts.}


%description %_description

%package -n     python3-urwid-readline
Summary:        %{summary}

%description -n python3-urwid-readline %_description


%prep
%autosetup -p1 -n %{upstream_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{upstream_name}


%check
%pytest


%files -n python3-urwid-readline -f %{pyproject_files}
%doc README.md
%license LICENSE LICENSE.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 24 2024 Lumír Balhar <lbalhar@redhat.com> - 0.15.1-1
- Update to 0.15.1 (rhbz#2314354)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.13-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.13-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.13-2
- Rebuilt for Python 3.11

* Tue Jan 18 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 0.13-1
- Initial build
