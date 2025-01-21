%{?python_enable_dependency_generator}
# Based on spec created by pyp2rpm-2.0.0
%global pypi_name yamllint

Name:           %{pypi_name}
Version:        1.35.1
Release:        5%{?dist}
Summary:        A linter for YAML files

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/adrienverge/yamllint
Source0:        https://pypi.python.org/packages/source/y/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pathspec
BuildRequires:  python3-PyYAML
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description
A linter for YAML files.

yamllint does not only check for syntax validity, but for weirdnesses like key
repetition and cosmetic problems such as lines length, trailing spaces,
indentation, etc.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%pyproject_wheel

%{__make} SPHINXBUILD=/usr/bin/sphinx-build-3 -C docs man
gzip docs/_build/man/%{pypi_name}.1

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%pyproject_install

mkdir -p %{buildroot}%{_mandir}/man1/
install -m0644 docs/_build/man/%{pypi_name}.1.gz %{buildroot}%{_mandir}/man1/

%check
%{__python3} -m unittest discover

%files
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi_name}
%{_mandir}/man1/%{pypi_name}.1.gz
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*
%exclude %{python3_sitelib}/tests

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.35.1-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.35.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.35.1-2
- Rebuilt for Python 3.13

* Fri Feb 16 2024 Adrien Vergé <adrienverge@gmail.com> - 1.35.1-1
- Update to latest upstream version

* Thu Feb 15 2024 Adrien Vergé <adrienverge@gmail.com> - 1.35.0-1
- Update to latest upstream version

* Tue Feb 06 2024 Adrien Vergé <adrienverge@gmail.com> - 1.34.0-1
- Update to latest upstream version

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 09 2023 Adrien Vergé <adrienverge@gmail.com> - 1.33.0-1
- Update to latest upstream version

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.32.0-2
- Rebuilt for Python 3.12

* Mon May 22 2023 Adrien Vergé <adrienverge@gmail.com> - 1.32.0-1
- Update to latest upstream version

* Fri Apr 21 2023 Adrien Vergé <adrienverge@gmail.com> - 1.31.0-1
- Update to latest upstream version

* Fri Apr 14 2023 Adrien Vergé <adrienverge@gmail.com> - 1.30.0-2
- Update 'check' step to stop using setup.py

* Wed Mar 22 2023 Adrien Vergé <adrienverge@gmail.com> - 1.30.0-1
- Update to latest upstream version

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Adrien Vergé <adrienverge@gmail.com> - 1.29.0-1
- Update to latest upstream version

* Mon Sep 12 2022 Adrien Vergé <adrienverge@gmail.com> - 1.28.0-1
- Update to latest upstream version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Adrien Vergé <adrienverge@gmail.com> - 1.27.1-1
- Update to latest upstream version

* Fri Jul 08 2022 Adrien Vergé <adrienverge@gmail.com> - 1.27.0-1
- Update to latest upstream version

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.26.3-2
- Rebuilt for Python 3.11

* Sun Feb 13 2022 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.26.3-1
- Update for 1.26.3

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.26.0-2
- Rebuilt for Python 3.10

* Fri Jan 29 2021 Adrien Vergé <adrienverge@gmail.com> - 1.26.0-1
- Update to latest upstream version

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Adrien Vergé <adrienverge@gmail.com> - 1.25.0-1
- Update to latest upstream version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Adrien Vergé <adrienverge@gmail.com> - 1.24.2-1
- Update to latest upstream version

* Wed Jul 15 2020 Adrien Vergé <adrienverge@gmail.com> - 1.24.0-1
- Update to latest upstream version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.23.0-2
- Rebuilt for Python 3.9

* Fri Apr 17 2020 Adrien Vergé <adrienverge@gmail.com> - 1.23.0-1
- Update to latest upstream version

* Tue Mar 24 2020 Adrien Vergé <adrienverge@gmail.com> - 1.21.0-1
- Update to latest upstream version

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 26 2019 Adrien Vergé <adrienverge@gmail.com> - 1.20.0-1
- Update to latest upstream version

* Tue Oct 15 2019 Adrien Vergé <adrienverge@gmail.com> - 1.18.0-1
- Update to latest upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-2
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Adrien Vergé <adrienverge@gmail.com> - 1.17.0-1
- Update to latest upstream version

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 7 2019 Adrien Vergé <adrienverge@gmail.com> - 1.16.0-1
- Update to latest upstream version

* Mon Feb 11 2019 Adrien Vergé <adrienverge@gmail.com> - 1.15.0-1
- Update to latest upstream version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.14.0-2
- Enable python dependency generator

* Mon Jan 14 2019 Adrien Vergé <adrienverge@gmail.com> - 1.14.0-1
- Update to latest upstream version

* Wed Nov 14 2018 Adrien Vergé <adrienverge@gmail.com> - 1.13.0-1
- Update to latest upstream version

* Wed Oct 17 2018 Adrien Vergé <adrienverge@gmail.com> - 1.12.1-1
- Update to latest upstream version

* Thu Oct 4 2018 Adrien Vergé <adrienverge@gmail.com> - 1.12.0-1
- Update to latest upstream version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-2
- Rebuilt for Python 3.7

* Sun Apr 29 2018 Adrien Vergé <adrienverge@gmail.com> - 1.11.1-1
- Update to latest upstream version

* Wed Feb 21 2018 Adrien Vergé <adrienverge@gmail.com> - 1.11.0-1
- Update to latest upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 5 2017 Adrien Vergé <adrienverge@gmail.com> - 1.10.0-1
- Update to latest upstream version

* Mon Oct 16 2017 Adrien Vergé <adrienverge@gmail.com> - 1.9.0-1
- Update to latest upstream version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Adrien Vergé <adrienverge@gmail.com> - 1.8.1-1
- Update to latest upstream version
- Update dependencies

* Tue Apr 25 2017 Adrien Vergé <adrienverge@gmail.com> - 1.7.0-1
- Update to latest upstream version

* Sun Feb 26 2017 Adrien Vergé <adrienverge@gmail.com> - 1.6.1-1
- Update to latest upstream version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-2
- Rebuild for Python 3.6

* Wed Nov 30 2016 Adrien Vergé <adrienverge@gmail.com> - 1.6.0-1
- Update to latest upstream version

* Sat Oct 8 2016 Adrien Vergé <adrienverge@gmail.com> - 1.5.0-1
- Update to latest upstream version

* Tue Sep 27 2016 Adrien Vergé <adrienverge@gmail.com> - 1.4.1-1
- Update to latest upstream version

* Mon Sep 19 2016 Adrien Vergé <adrienverge@gmail.com> - 1.4.0-1
- Update to latest upstream version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Adrien Vergé <adrienverge@gmail.com> - 1.3.2-1
- Update to latest upstream version

* Mon Jun 27 2016 Adrien Vergé <adrienverge@gmail.com> - 1.3.0-1
- Update to latest upstream version

* Fri Jun 24 2016 Adrien Vergé <adrienverge@gmail.com> - 1.2.2-1
- Update to latest upstream version

* Fri Mar 25 2016 Adrien Vergé <adrienverge@gmail.com> - 1.2.1-1
- Update to latest upstream version
- Justify summary

* Mon Mar 7 2016 Adrien Vergé <adrienverge@gmail.com> - 1.2.0-1
- Update to latest upstream version
- Fix 'License:' field (from GPLv3 to GPLv3+)
- Add license file from upstream

* Fri Feb 26 2016 Adam Miller <maxamillion@gmail.com> - 1.0.3-2
- Fix permissions on man page install

* Wed Feb 24 2016 Adam Miller <maxamillion@gmail.com> - 1.0.3-1
- Update to latest upstream
- Add man page

* Thu Feb 18 2016 Adam Miller <maxamillion@gmail.com> - 0.7.2-1
- Initial package.
