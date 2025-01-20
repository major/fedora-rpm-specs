%global modname pyramid
%global sum The Pyramid web application framework, a Pylons project
%global desc Pyramid is a small, fast, down-to-earth, open source Python web development\
framework. It makes real-world web application development and deployment more\
fun, more predictable, and more productive.

Name:           python-%{modname}
Version:        2.0.2
Release:        6%{?dist}
Summary:        %{sum}

License:        BSD-4-Clause
URL:            https://trypyramid.com/
Source0:        %pypi_source %{modname}

# Allow InstancePropertyHelper to accept properties with names on Python 3.13+
Patch:          https://github.com/Pylons/pyramid/pull/3762.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%{desc}


%package -n python3-pyramid
Summary:        %{sum}

%description -n python3-pyramid
%{desc}


%prep
%autosetup -n pyramid-%{version} -p1

# Remove bundled egg info
rm -rf %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires -x testing


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}

# Create the Python 3 executables.
for e in pserve prequest proutes pshell ptweens pviews pdistreport; do
    mv %{buildroot}/%{_bindir}/$e %{buildroot}/%{_bindir}/$e-%{python3_version};
    ln -s %{_bindir}/$e-%{python3_version} %{buildroot}/%{_bindir}/$e-3;
    ln -s %{_bindir}/$e-%{python3_version} %{buildroot}/%{_bindir}/$e
done;


%check
%pyproject_check_import
%pytest tests


%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst
%{_bindir}/pdistreport-%{python3_version}
%{_bindir}/pdistreport-3
%{_bindir}/pdistreport
%{_bindir}/prequest-%{python3_version}
%{_bindir}/prequest-3
%{_bindir}/prequest
%{_bindir}/proutes-%{python3_version}
%{_bindir}/proutes-3
%{_bindir}/proutes
%{_bindir}/pserve-%{python3_version}
%{_bindir}/pserve-3
%{_bindir}/pserve
%{_bindir}/pshell-%{python3_version}
%{_bindir}/pshell-3
%{_bindir}/pshell
%{_bindir}/ptweens-%{python3_version}
%{_bindir}/ptweens-3
%{_bindir}/ptweens
%{_bindir}/pviews-%{python3_version}
%{_bindir}/pviews-3
%{_bindir}/pviews


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Mattia Verga <mattia.verga@proton.me> - 2.0.2-4
- Rebuilt for Python 3.13
- Fixes: rhbz#2291872

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 27 2023 Mattia Verga <mattia.verga@proton.me> - 2.0.2-1
- Update to 2.0.2
- Fixes CVE-2023-40587

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.12

* Sat Feb 04 2023 Mattia Verga <mattia.verga@proton.me> - 2.0.1-1
- Update to 2.0.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Mattia Verga <mattia.verga@proton.me> - 2.0-1
- Update to 2.0
- Use SPDX identifier in license tag
- Use modern python macros for packaging

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 1.10.5-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.10.5-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Kevin Fenzi <kevin@scrye.com> - 1.10.5-1
- Update to 1.10.5. Fixes rhbz#1895793

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-4
- Subpackage python2-pyramid has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-1
- Update to 1.10.4 (#1699203) to fix Python 3.8 test failures (#1698157)

* Tue Mar 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.10.2-1
- Update to 1.10.2.
- https://docs.pylonsproject.org/projects/pyramid/en/1.10-branch/changes.html

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.9.2-1
- Update to 1.9.2
- Require webob >= 1.7.0

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.9.1-7
- Use the py2 version of the macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-5
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.9.1-4
- Use /usr/bin/python2 instead of /usr/bin/python when building.

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
