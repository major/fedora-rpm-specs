Name:           python-pygments-better-html
Version:        0.1.4
Release:        8%{?dist}
Summary:        Better line numbers for Pygments HTML

License:        BSD
URL:            https://github.com/Kwpolska/pygments_better_html
Source0:        %{pypi_source pygments_better_html}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This library provides improved line numbers for the Pygments HTML formatter.
}

%description %_description

%package -n python3-pygments-better-html
Summary: %{summary}

%description -n python3-pygments-better-html %_description

%prep
%autosetup -p1 -n pygments_better_html-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pygments_better_html

%check
%pyproject_check_import

%files -n python3-pygments-better-html -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.4-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.4-2
- Rebuilt for Python 3.11

* Mon Feb 21 2022 supakeen <cmdr@supakeen.com> - 0.1.4-1
- Initial version of the package.
