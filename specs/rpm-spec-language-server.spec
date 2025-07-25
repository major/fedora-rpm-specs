Name:           rpm-spec-language-server
Version:        0.0.1
Release:        7%{?dist}
Summary:        Language Server for RPM spec files

License:        GPL-2.0-or-later
URL:            https://github.com/dcermak/rpm-spec-language-server
Source:         %{URL}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

# Test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-typeguard


%description
This is a server implementing the Language Server Protocol for RPM Spec files.

Supported LSP endpoints:

- Autocompletion of macro names, spec sections and preamble keywords
- Jump to macro definition
- Expand macros on hover
- Breadcrumbs/document sections


%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'rpm_spec_language_server'


%check
%pytest
%pyproject_check_import


%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/rpm_lsp_server


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jun 06 2025 Python Maint <python-maint@redhat.com> - 0.0.1-6
- Rebuilt for Python 3.14

* Mon Feb 03 2025 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-5
- Remove unused and duplicated BuildRequires

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Python Maint <python-maint@redhat.com> - 0.0.1-2
- Rebuilt for Python 3.13

* Tue Apr 02 2024 Jakub Kadlcik <frostyx@email.cz>
- Initial package
