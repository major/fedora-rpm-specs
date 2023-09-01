%global pypi_name u-msgpack-python

Name:           python-%{pypi_name}
Version:        2.8.0
Release:        1%{?dist}
Summary:        A portable, lightweight MessagePack serializer and deserializer

License:        MIT
URL:            https://github.com/vsergeev/u-msgpack-python
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
A lightweight MessagePack serializer and deserializer module written in pure
Python. It is fully compliant with the latest MessagePack specification.
In particular, it supports the new binary, UTF-8 string, and
application-defined ext types.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A lightweight MessagePack serializer and deserializer module written in pure
Python. It is fully compliant with the latest MessagePack specification.
In particular, it supports the new binary, UTF-8 string, and
application-defined ext types.


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files umsgpack


%check
%tox


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
* Tue Aug 29 2023 Charalampos Stratakis <cstratak@redhat.com> - 2.8.0-1
- Update to 2.8.0
Resolves: rhbz#2140895

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.7.1-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.7.1-6
- Rebuilt for Python 3.11

* Fri Feb 4 2022 Steve Traylen <steve.traylen@cern.ch> - 2.7.1-5
- Migrate to pyproject macros
- Use GitHub tarball to have tox.ini

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 2.7.1-2
- Rebuilt for Python 3.10

* Fri Mar 19 2021 Charalampos Stratakis <cstratak@redhat.com> - 2.7.1-1
- Update to 2.7.1 (rhbz#1891279)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 24 2020 Tomas Hrnciar <thrnciar@redhat.com> - 2.7.0-1
- Update to 2.7.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Tomas Hrnciar <thrnciar@redhat.com> - 2.6.0-1
- Update to 2.6.0

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.2-1
- Update to 2.5.2 (#1697452)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 20 2018 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-1
- Initial package
