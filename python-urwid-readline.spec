%global upstream_name urwid_readline
Name:           python-urwid-readline
Version:        0.13
Release:        6%{?dist}
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
