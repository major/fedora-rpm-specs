%global pkgname flufl-lock

Name:           python-%{pkgname}
Version:        8.0.2
Release:        4%{?dist}
Summary:        NFS-safe file locking with timeouts for POSIX systems

License:        Apache-2.0
URL:            https://gitlab.com/warsaw/flufl.lock
Source0:        https://files.pythonhosted.org/packages/source/f/flufl.lock/flufl_lock-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# for tests
# we don't actually test code cov.
# upstream default pytest flags have --cov
# so this is easier than a patch.  we add
# the --no-cov flag below to avoid running coverage
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-sybil

%global _description %{expand:
The flufl.lock library provides an NFS-safe file-based locking algorithm
influenced by the GNU/Linux "open(2)" man page, under the description of
the "O_EXCL" option.}

%description %{_description}


%package -n python3-%{pkgname}
Summary:        %{summary}

%description -n python3-%{pkgname} %{_description}


%prep
%autosetup -n flufl_lock-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flufl


%check
# this file causes pytest to do weird things
# so let's get it out of the way
rm -f conftest.py
%pytest --no-cov


%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.rst docs/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 8.0.2-2
- Rebuilt for Python 3.13

* Fri Feb 02 2024 jonathanspw <jonathan@almalinux.org> - 8.0.2-1
- Update to 8.0.2 rhbz#2216613

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 7.1.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Jonathan Wright <jonathan@almalinux.org> - 7.1.1-1
- Update to 7.1.1
- rhbz#1852603

* Thu Aug 25 2022 Jonathan Wright <jonathan@almalinux.org> - 7.1-1
- Update to 7.1
- rhbz#1852603

* Thu Aug 25 2022 Jonathan Wright <jonathan@almalinux.org> - 6.0-1
- Updated to 6.0-1
- Spec file modernization

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.2-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2-2
- Rebuilt for Python 3.7

* Thu Feb 15 2018 Aurelien Bompard <abompard@fedoraproject.org> - 3.2-1
- Version 3.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Aurelien Bompard <abompard@fedoraproject.org> - 2.4.1-5
- Fix BuildRequires name

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-2
- Rebuild for Python 3.6

* Wed Sep 14 2016 Aurelien Bompard <abompard@fedoraproject.org> - 2.4.1-1
- Initial package.
