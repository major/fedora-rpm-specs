%global pypi_name markdown-it-py

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        3%{?dist}
Summary:        Python port of markdown-it

License:        MIT
URL:            https://github.com/executablebooks/markdown-it-py
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
Markdown parser done right. Its features:
Follows the CommonMark spec for baseline parsing.
Has configurable syntax: you can add new rules and even replace existing ones.
Pluggable: Adds syntax extensions to extend the parser.
High speed & safe by default
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Remove unnecessary shebang
sed -i '1{\@^#!/usr/bin/env python@d}' markdown_it/cli/parse.py
# Remove coverage (it resides in testing extra which we want to use)
# Upstream issue to move those to another extra:
# https://github.com/executablebooks/markdown-it-py/issues/195
sed -i '/"coverage",/d' pyproject.toml
sed -i '/"pytest-cov",/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x testing

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files markdown_it

%check
# Skipped test uses linkify-it-py extra which we don't have
%pytest tests/ -k "not test_linkify"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE LICENSE.markdown-it
%doc README.md
%{_bindir}/markdown-it


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.11

* Tue Apr 19 2022 Lumír Balhar <lbalhar@redhat.com> - 2.1.0-1
- Update to 2.1.0
Resolves: rhbz#2075950

* Mon Jan 31 2022 Karolina Surma <ksurma@redhat.com> - 2.0.1-1
- Update to 2.0.1
Resolves: rhbz#2028769
- Generate test dependencies from upstream data instead of hardcoding them

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 Karolina Surma <ksurma@redhat.com> - 1.1.0-4
- Enable more tests in %%check using pytest-regressions

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.10

* Thu May 13 2021 Karolina Surma <ksurma@redhat.com> - 1.1.0-1
- Initial package.
