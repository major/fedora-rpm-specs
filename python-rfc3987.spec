Name:           python-rfc3987
Version:        1.3.8
Release:        2%{?dist}
Summary:        Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)

License:        GPL-3.0-or-later
URL:            https://github.com/dgerber/rfc3987
Source:         %{pypi_source rfc3987}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This module provides regular expressions according to RFC 3986 "Uniform
Resource Identifier (URI): Generic Syntax" <http://tools.ietf.org/html/rfc3986>
and RFC 3987 "Internationalized Resource Identifiers (IRIs)"
<http://tools.ietf.org/html/rfc3987>, and utilities for composition and
relative resolution of references.}


%description %{_description}


%package -n     python3-rfc3987
Summary:        %{summary}


%description -n python3-rfc3987 %{_description}


%prep
%autosetup -n rfc3987-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files rfc3987

# Remove shebang
sed -i -e '/^#!\//, 1d' %{buildroot}%{python3_sitelib}/rfc3987.py


%check
%{python3} -m doctest -v rfc3987.py


%files -n python3-rfc3987 -f %{pyproject_files}
%doc README.txt


%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.3.8-2
- Rebuilt for Python 3.12

* Wed Feb 15 2023 Carl George <carl@george.computer> - 1.3.8-1
- Update to version 1.3.8
- Convert to pyproject macros

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.7-20
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.7-17
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.7-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.7-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.7-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.7-8
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.7-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.7-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 1.3.7-2
- Remove shebang from rfc3987.py

* Tue Apr 11 2017 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 1.3.7-1
- Update to 1.3.7
- Include license text from tarball

* Wed Dec 21 2016 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 1.3.6-2
- Call doctest in %%check

* Mon Jul 18 2016 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 1.3.6-1
- Initial packaging
