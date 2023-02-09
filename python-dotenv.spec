Name:           python-dotenv
Version:        0.21.1
Release:        2%{?dist}
Summary:        Read key-value pairs from a .env file and set them as environment variables

License:        BSD
URL:            https://github.com/theskumar/python-dotenv
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Reads the key/value pair from .env file and adds them to environment variable.


%package -n     python3-dotenv
Summary:        %{summary}
Recommends:     python3-dotenv+cli

%description -n python3-dotenv
Reads the key/value pair from .env file and adds them to environment variable.


%prep
%autosetup

# Get rid of dependency on python-cov, drop --cov... options from pytest
# Downstream-only change, based on Fedora's linters policy
sed -Ei -e "/^  pytest-cov$/d" \
        -e "s/--cov //" \
        -e "s/--cov-[[:alnum:]]+(=| +)[^ ]+ //g" \
    tox.ini

%if 0%{?rhel}
# Avoid IPython dependency in tests only needed for optional integration
sed -i -e '/ipython/d' requirements.txt tox.ini
%endif


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files dotenv


%check
%tox


%files -n python3-dotenv -f %{pyproject_files}
%doc README.md

%pyproject_extras_subpkg -n python3-dotenv cli
%{_bindir}/dotenv


%changelog
* Tue Feb 07 2023 Miro Hrončok <mhroncok@redhat.com> - 0.21.1-2
- Drop unwanted build dependency on pytest-cov

* Mon Jan 23 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.21.1-1
- 0.21.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 12 2022 Karolina Surma <ksurma@redhat.com> - 0.21.0-1
- Update to 0.21.0
Resolves: rhbz#2068308

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.19.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 0.19.2-1
- Update to 0.19.2

* Thu Aug 19 2021 Tomas Hrnciar <thrnciar@redhat.com> - 0.19.0-1
- Update to 0.19.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Lumír Balhar <lbalhar@redhat.com> - 0.18.0-1
- Update to 0.18.0
Resolves: rhbz#1974239

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.17.1-2
- Rebuilt for Python 3.10

* Wed Apr 28 2021 Karolina Surma <ksurma@redhat.com> - 0.17.1-1
- Update to 0.17.1
Resolves rhbz#1945975

* Thu Apr 01 2021 Tomas Hrnciar <thrnciar@redhat.com> - 0.16.0-1
- Update to 0.16.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Lumír Balhar <lbalhar@redhat.com> - 0.15.0-1
- Update to 0.15.0 (#1892507)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.0-2
- Add python-dotenv[cli] subpackage with /usr/bin/dotenv

* Thu Jul 09 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.0-1
- Update to 0.14.0
- Fixes rhbz#1709002

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-2
- Rebuilt for Python 3.9

* Mon May 04 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-1
- Update to 0.13.0 (#1709002)
- Fix failing tests with click 7.1 (#1830984)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-1
- Initial package
