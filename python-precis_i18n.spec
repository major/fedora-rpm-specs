%global srcname precis_i18n

Name:           python-%{srcname}
Version:        1.0.5
Release:        1%{?dist}
Summary:        Python library for internationalized usernames and passwords

License:        MIT
URL:            https://github.com/byllyfish/precis_i18n
Source0:        https://github.com/byllyfish/precis_i18n/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global desc %{expand:
If you want your application to accept Unicode user names and passwords, you
must be careful in how you validate and compare them. The PRECIS framework
makes internationalized user names and passwords safer for use by applications.
PRECIS profiles transform Unicode strings into a canonical form, suitable for
comparison.

This Python module implements the PRECIS Framework as described in:

  PRECIS Framework: Preparation, Enforcement, and Comparison of
  Internationalized Strings in Application Protocols (RFC 8264)

  Preparation, Enforcement, and Comparison of Internationalized Strings
  Representing Usernames and Passwords (RFC 8265)

  Preparation, Enforcement, and Comparison of Internationalized Strings
  Representing Nicknames (RFC 8266)}

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{python3} setup.py test

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.rst

%changelog
* Sat Jan 07 2023 Michael Kuhn <suraia@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5
- Update to newer Python packaging guidelines

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.1-14.20200622git1498def50914
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13.20200622git1498def50914
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12.20200622git1498def50914
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.1-11.20200622git1498def50914
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10.20200622git1498def50914
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9.20200622git1498def50914
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-8.20200622git1498def50914
- Use a snapshot of the current current upstream git.
- Add derived-props-13.0.txt for Python 3.9.
- Replace ":" with "_" in profile names. (rhbz#1792953)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-2
- Support Unicode 12.1 for Python 3.8.

* Mon Jul 22 2019 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-1
- Upstream release 1.0.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Michal Schmidt <mschmidt@redhat.com> - 1.0-2
- In the package description spell "Unicode" with uppercase U.

* Wed Jan 23 2019 Michal Schmidt <mschmidt@redhat.com> - 1.0-1
- Initial package.
