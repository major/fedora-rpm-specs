%global pypi_name lark-parser

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        11%{?dist}
Summary:        Lark is a modern general-purpose parsing library for Python
License:        MIT
Url:            https://github.com/lark-parser/lark
Source:         https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# Adjust imports for Python 3.11, merged upstream
# https://github.com/lark-parser/lark/pull/1140
Patch:          python3.11.patch

BuildArch:      noarch

%description
Lark is a modern general-purpose parsing library for Python.

Lark focuses on simplicity and power. It lets you choose between
two parsing algorithms:

Earley : Parses all context-free grammars (even ambiguous ones)!
It is the default.

LALR(1): Only LR grammars. Outperforms PLY and most if not all
other pure-python parsing libraries.

Both algorithms are written in Python and can be used interchangeably
with the same grammar (aside for algorithmic restrictions).
See "Comparison to other parsers" for more details.

Lark can auto magically build an AST from your grammar, without any
more code on your part.

Features:

- EBNF grammar with a little extra
- Earley & LALR(1)
- Builds an AST auto magically based on the grammar
- Automatic line & column tracking
- Automatic token collision resolution (unless both tokens are regexps)
- Python 2 & 3 compatible
- Unicode fully supported

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Lark is a modern general-purpose parsing library for Python.

Lark focuses on simplicity and power. It lets you choose between
two parsing algorithms:

Earley : Parses all context-free grammars (even ambiguous ones)!
It is the default.

LALR(1): Only LR grammars. Outperforms PLY and most if not all
other pure-python parsing libraries.

Both algorithms are written in Python and can be used interchangeably
with the same grammar (aside for algorithmic restrictions).
See "Comparison to other parsers" for more details.

Lark can auto magically build an AST from your grammar, without any
more code on your part.

Features:

- EBNF grammar with a little extra
- Earley & LALR(1)
- Builds an AST auto magically based on the grammar
- Automatic line & column tracking
- Automatic token collision resolution (unless both tokens are regexps)
- Python 2 & 3 compatible
- Unicode fully supported

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install
rm -rfv %{buildroot}/%{python3_sitelib}/lark-stubs/

%check
%{python3} -m tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md examples
%{python3_sitelib}/lark_parser-*.egg-info
%{python3_sitelib}/lark/

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.0-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-7
- Don't import deprecated sre_parse and sre_constants modules

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 05 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-2
- Rebuilt for Python 3.9

* Sat Mar 07 2020 Thomas Andrejak <thomas.andrejak@gmail.com> - 0.8.2-1
- Update to 0.8.2

* Mon Feb 24 2020 Thomas Andrejak <thomas.andrejak@gmail.com> - 0.8.1-1
- Update to 0.8.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Thomas Andrejak <thomas.andrejak@c-s.fr> - 0.7.8-1
- Update to 0.7.8

* Fri Oct 25 2019 Thomas Andrejak <thomas.andrejak@c-s.fr> - 0.7.7-1
- Update to 0.7.7

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Scott K Logan <logans@cottsay.net> - 0.7.1-1
- Update to 0.7.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 0.6.4-2
- Fix package naming

* Mon Sep 24 2018 Thomas Andrejak <thomas.andrejak@gmail.com> - 0.6.4-1
- Initial package
