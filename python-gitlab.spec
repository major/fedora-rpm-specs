# Created by pyp2rpm-3.3.0
%global pypi_name gitlab

Name:           python-%{pypi_name}
Version:        3.14.0
Release:        2%{?dist}
Summary:        Interact with GitLab API

License:        LGPLv3
URL:            https://github.com/python-gitlab/python-gitlab
Source0:        https://files.pythonhosted.org/packages/source/p/python-gitlab/python-gitlab-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

# drop the -doc package. To much effort to keep working
Provides:  python-%{pypi_name}-doc = %{version}-%{release}
Obsoletes: python-%{pypi_name}-doc <= 3.3.0

%description
Interact with GitLab API

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Interact with GitLab API

%package -n python-%{pypi_name}-doc
Summary:        Python gitlab documentation
%description -n python-%{pypi_name}-doc
Documentation for gitlab

%prep
%autosetup -p1 -n python-%{pypi_name}-%{version}

# Relax some dependencies
sed -i 's/requests==.*/requests/'                    requirements.txt
sed -i 's/requests-toolbelt==.*/requests-toolbelt/'  requirements.txt
sed -i 's/pytest==.*/pytest/'       requirements-lint.txt requirements-test.txt
sed -i 's/PyYaml==.*/PyYaml/'       requirements-lint.txt requirements-test.txt
sed -i 's/responses==.*/responses/' requirements-lint.txt requirements-test.txt
sed -i 's/coverage==.*/coverage/'   requirements-test.txt
sed -i 's/build==.*/build/'         requirements-test.txt

# not available in rawhide 11 Aug 2022
sed -i 's/pytest-console-scripts.*//' requirements-test.txt
sed -i 's/pytest-github-actions-annotate-failures.*//' requirements-test.txt

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files gitlab

%check
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%{_bindir}/gitlab
%doc README.rst

%changelog
* Mon May 15 2023 Steve Traylen <steve.traylen@cern.ch> - 3.14.0-2
- Rebuild for new python-requests-toolbelt (rhbz#2203755)

* Thu Apr 13 2023 Steve Traylen <steve.traylen@cern.ch> - 3.14.0-1
- New 3.14.0 version

* Thu Mar 2 2023 Steve Traylen <steve.traylen@cern.ch> - 3.13.0-1
- New 3.13.0 version

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 6 2023 Steve Traylen <steve.traylen@cern.ch> - 3.12.0-1
- New 3.12.0 version

* Sun Aug 28 2022 Steve Traylen <steve.traylen@cern.ch> - 3.9.0-1
- New 3.9.0 version

* Sun Aug 28 2022 Steve Traylen <steve.traylen@cern.ch> - 3.8.1-3
- Relax exact dependencies for requests and pytest

* Thu Aug 18 2022 Nikola Forró <nforro@redhat.com> - 3.8.1-3
- Re-enable tox tests

* Thu Aug 18 2022 Nikola Forró <nforro@redhat.com> - 3.8.1-2
- Do not try to remove shebangs from cli.py scripts, they are no longer there


* Thu Aug 11 2022 Steve Traylen <steve.traylen@cern.ch> - 3.8.1-1
- New 3.8.1 version
- Migrate to pyproject macros
- Drop -doc package

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.11

* Thu Apr 14 2022 Steve Traylen <steve.traylen@cern.ch> - 3.3.0-1
- New 3.3.0 version

* Mon Jan 31 2022 Steve Traylen <steve.traylen@cern.ch> - 3.1.1-1
- New 3.1.1 version, Use default sphinx theme rather than furo.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 9 2021 Steve Traylen <steve.traylen@cern.ch> - 2.10.1-1
- New 2.10.1 version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.7.1-2
- Rebuilt for Python 3.10

* Mon May 24 2021 Stephen Gallagher <sgallagh@redhat.com> - 2.7.1-1
- New 2.7.1 version
- Adds support for setting merge request approval rules

* Mon Mar 8 2021 Steve Traylen <steve.traylen@cern.ch> - 2.6.0-1
- New 2.6.0 version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Steve Traylen <steve.traylen@cern.ch> - 2.4.0-1
- New 2.4.0 version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Steve Traylen <steve.traylen@cern.ch> - 1.15.0-1
- New 1.15.0 version

* Mon Dec 16 2019 Steve Traylen <steve.traylen@cern.ch> - 1.14.0-1
- New 1.14.0 version

* Wed Nov 13 2019 Steve Traylen <steve.traylen@cern.ch> - 1.13.0-1
- New 1.13.0 version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 09 2019 Neal Gompa <ngompa13@gmail.com> - 1.7.0-1
- Update to 1.7.0
- Drop redundant runtime dependencies specified for auto-generated ones

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-6
- Subpackage python2-gitlab has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-5
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.7

* Wed May 16 2018 Steve Traylen <steve.traylen@cern.ch> - 1.3.0-3
- Correct copy paste error.

* Wed May 16 2018 Steve Traylen <steve.traylen@cern.ch> - 1.3.0-2
- Specify COPYING file. Add BR on python-mock.

* Fri May 11 2018 Steve Traylen <steve.traylen@cern.ch> - 1.3.0-1
- Initial package.
