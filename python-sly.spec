%global commit f8fcbb080c4bc4ff14bd30876386edd63d8362cb
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-sly
Version:        0.4
Release:        0.31.%{shortcommit}%{?dist}
Summary:        An implementation of lex and yacc for Python 3

License:        BSD
URL:            https://sly.readthedocs.io
Source0:        https://github.com/dabeaz/sly/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(pytest)

%global _description %{expand:
SLY is a pure Python implementation of the lex and yacc tools commonly
used to write parsers and compilers. Parsing is based on the same
LALR(1) algorithm used by many yacc tools.}

%description %_description

%package -n python3-sly
Summary:        %{summary}

%description -n python3-sly %_description

%prep
%autosetup -p1 -n sly-%{commit}

%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files sly


%check
%pytest

%files -n python3-sly -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.31.f8fcbb0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4-0.30.f8fcbb0
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.29.f8fcbb0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.28.f8fcbb0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4-0.27.f8fcbb0
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.26.f8fcbb0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Roman Inflianskas <rominf@aiven.io> - 0.4-0.25
- Initial package
