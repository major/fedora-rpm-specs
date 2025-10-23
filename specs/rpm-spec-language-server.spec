Name:           rpm-spec-language-server
Version:        0.0.2
Release:        1%{?dist}
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

# Relax poetry dependencies
sed -i 's/pygls = "^2.0"/pygls = "*"/' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'rpm_spec_language_server'


%check
# Some tests are failing
# See https://github.com/dcermak/rpm-spec-language-server/issues/455#issuecomment-3429420682
%pytest \
    --deselect tests/test_extract_docs.py::test_fetch_upstream_spec_md \
    --deselect tests/test_extract_docs.py::test_parse_upstream_spec_md \
    --deselect tests/test_extract_docs.py::test_cache_creation \
    --deselect tests/test_extract_docs.py::test_spec_md_fetched_from_upstream_if_not_in_rpm_package

%pyproject_check_import


%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/rpm_lsp_server


%changelog
* Tue Oct 21 2025 Jakub Kadlcik <frostyx@email.cz> - 0.0.2-1
- New upstream version

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.0.1-9
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.0.1-8
- Rebuilt for Python 3.14.0rc2 bytecode

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
