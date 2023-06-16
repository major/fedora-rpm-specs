Name:           python-license-expression
Version:        30.1.0
Release:        2%{?dist}
Summary:        Library to parse, compare, simplify and normalize license expressions
# `irc-notify.py` in the tarball is licensed under GPL, but not re-distributed
License:        Apache-2.0
URL:            https://github.com/nexB/license-expression/
Source0:        %{pypi_source license-expression}

BuildArch:      noarch

%global _description \
This module defines a mini language to parse, validate, simplify, normalize and\
compare license expressions using a boolean logic engine.\
\
This supports SPDX license expressions and also accepts other license naming\
conventions and license identifiers aliases to resolve and normalize licenses.\
\
Using boolean logic, license expressions can be tested for equality,\
containment, equivalence and can be normalized or simplified.

%description %{_description}

%package -n     python3-license-expression
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-license-expression %{_description}

%prep
%autosetup -n license-expression-%{version}
# Remove bundled egg-info
rm -r src/*.egg-info/
rm PKG-INFO
# Set fallback_version
sed -i 's/^fallback_version.*/fallback_version = "%{version}"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files license_expression

%check
%pytest

%files -n python3-license-expression -f %{pyproject_files}
%license apache-2.0.LICENSE NOTICE
%doc README.rst

%changelog
* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 30.1.0-2
- Rebuilt for Python 3.12

* Fri Feb 03 2023 Carmen Bianca BAKKER <carmenbianca@fedoraproject.org> - 30.1.0-1
- new version

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 30.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 06 2022 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 30.0.0-1
- new version

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 1.0-1
- new version

* Mon Sep 02 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.999-1
- New package.
