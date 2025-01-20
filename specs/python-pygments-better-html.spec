Name:           python-pygments-better-html
Version:        0.1.5
Release:        4%{?dist}
Summary:        Better line numbers for Pygments HTML

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.5-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 20 2024 Simon de Vlieger <cmdr@supakeen.com> - 0.1.5-1
- Update to upstream version 0.1.5.

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.4-9
- Rebuilt for Python 3.13

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
