%global pypi_name myst-parser

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        4%{?dist}
Summary:        A commonmark compliant parser, with bridges to docutils & sphinx

# SPDX
License:        MIT
URL:            https://github.com/executablebooks/MyST-Parser
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

# Fix test failures with Sphinx 7+
Patch:          https://github.com/executablebooks/MyST-Parser/commit/4f670fc04.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# Test dependencies- upstream uses tox with complicated matrix
# mixed with coverage, it's easier to set the ones we want here
BuildRequires:  python3-pytest
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-docutils
BuildRequires:  python3-pytest-regressions
BuildRequires:  python3-pytest-param-files
BuildRequires:  python3-sphinx-pytest
BuildRequires:  python3-linkify-it-py


%global _description %{expand:
A fully-functional markdown flavor and parser for Sphinx.
MyST allows you to write Sphinx documentation entirely in markdown.
MyST markdown provides a markdown equivalent of the reStructuredText syntax,
meaning that you can do anything in MyST that you can do with reStructuredText.
It is an attempt to have the best of both worlds: the flexibility and
extensibility of Sphinx with the simplicity and readability of Markdown.
}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}


%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n MyST-Parser-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files myst_parser

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/myst-anchors
%{_bindir}/myst-docutils-demo
%{_bindir}/myst-docutils-html
%{_bindir}/myst-docutils-html5
%{_bindir}/myst-docutils-latex
%{_bindir}/myst-docutils-xml
%{_bindir}/myst-docutils-pseudoxml
%{_bindir}/myst-inv

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 30 2023 Karolina Surma <ksurma@redhat.com> - 2.0.0-3
- Fix test failures with Sphinx 7+

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Karolina Surma <ksurma@redhat.com> - 2.0.0-1
- Update to 2.0.0
Resolves: rhbz#2214625

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.12

* Tue Mar 21 2023 Karolina Surma <ksurma@redhat.com> - 1.0.0-1
- Update to 1.0.0
Resolves: rhbz#2174349

* Mon Mar 20 2023 Karolina Surma <ksurma@redhat.com> - 0.18.1-5
- Backport fixes for tests failing with Sphinx 5.3

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 09 2022 Karolina Surma <ksurma@redhat.com> - 0.18.1-3
- Skip tests failing with Sphinx 5.2+

* Mon Oct 03 2022 Karolina Surma <ksurma@redhat.com> - 0.18.1-1
- Update to 0.18.1
Resolves: rhbz#2130162

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Karolina Surma <ksurma@redhat.com> - 0.18.0-1
- Update to 0.18.0
Resolves: rhbz#2094341

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.17.2-2
- Rebuilt for Python 3.11

* Tue Apr 26 2022 Lumír Balhar <lbalhar@redhat.com> - 0.17.2-1
- Update to 0.17.2
Resolves: rhbz#2075787

* Fri Feb 11 2022 Karolina Surma <ksurma@redhat.com> - 0.17.0-1
- Update to 0.17.0
Resolves: rhbz#2053497

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Karolina Surma <ksurma@redhat.com> - 0.16.0-1
- Update to 0.16.0
Resolves: rhbz#2031343
- Reenable skipped upstream tests in %%check

* Mon Aug 30 2021 Lumír Balhar <lbalhar@redhat.com> - 0.15.2-1
- Update to 0.15.2
Resolves: rhbz#1998385

* Wed Aug 18 2021 Karolina Surma <ksurma@redhat.com> - 0.15.1-3
- Enable more tests in %%check by using pytest-regressions
- Backport upstream patch to fix tests with Sphinx 4.1+

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Lumír Balhar <lbalhar@redhat.com> - 0.15.1-1
- Update to 0.15.1
Resolves: rhbz#1973481

* Mon Jun 14 2021 Karolina Surma <ksurma@redhat.com> - 0.15.0-1
- Update to 0.15.0
Resolves: rhbz#1971209

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.14.0-2
- Rebuilt for Python 3.10

* Fri May 14 2021 Karolina Surma <ksurma@redhat.com> - 0.14.0-1
- Initial package.
