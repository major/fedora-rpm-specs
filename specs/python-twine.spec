%global srcname twine

%bcond_without tests
%bcond_without docs
%bcond_with internet

Name:           python-%{srcname}
Version:        6.1.0
Release:        1%{?dist}
Summary:        Collection of utilities for interacting with PyPI

License:        Apache-2.0
URL:            https://github.com/pypa/%{srcname}
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Twine is a utility for interacting with PyPI.
Currently it only supports registering projects and uploading distributions.

%package -n %{srcname}
Summary:        Twine is a utility for publishing Python packages on PyPI

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
# Test dependencies
BuildRequires:  python3dist(build)
BuildRequires:  python3dist(jaraco-envs)
BuildRequires:  python3dist(munch)
BuildRequires:  python3dist(portend)
BuildRequires:  python3dist(pretend)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
%if %{with docs}
# Doc (manpage) deps
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinxcontrib-programoutput)
%endif
# with docs
%if %{with internet}
# pytest-services and pytest-socket are not packaged yet
#BuildRequires:  python3dist(pytest-services)
#BuildRequires:  python3dist(pytest-socket)
BuildRequires:  gcc
BuildRequires:  libffi-devel
BuildRequires:  git-core
%endif
# with internet

%endif
# with tests

Obsoletes:      python2-%{srcname} < 1.12.2-3
Obsoletes:      python3-%{srcname} < 1.12.2-3

%description -n %{srcname}
Twine is a utility for interacting with PyPI.
Currently it only supports registering projects and uploading distributions.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%if %{without internet}
sed -i '/--disable-socket/d' pytest.ini
%endif

%build
%pyproject_wheel
%if %{with docs}
PYTHONPATH=$PWD sphinx-build-3 -b man docs/ docs/build/man -c docs/
rm -r docs/build/man/.doctrees
%endif

%install
%pyproject_install
%pyproject_save_files twine
%if %{with docs}
install -p -D -T -m 0644 docs/build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1
%endif

%if %{with tests}
%check
%pytest -v \
%if %{without internet}
      --deselect tests/test_integration.py \
      --deselect tests/test_upload.py::test_check_status_code_for_wrong_repo_url \
%endif
;
# without internet
%endif
# with tests

%files -n %{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst AUTHORS
%if %{with docs}
%{_mandir}/man1/%{srcname}.1*
%endif
%{_bindir}/twine

%changelog
* Wed Jan 29 2025 Karolina Surma <ksurma@redhat.com> - 6.1.0-1
- Update to 6.1.0
- Fixes: rhbz#2339188

* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 04 2024 Charalampos Stratakis <cstratak@redhat.com> - 6.0.1-1
- Update to 6.0.1
Resolves: rhbz#2329634

* Tue Oct 22 2024 Tomáš Hrnčiar <thrnciar@redhat.com> - 5.1.1-2
- Unpin pkginfo, skip failing test

* Tue Oct 08 2024 Charalampos Stratakis <cstratak@redhat.com> - 5.1.1-1
- Update to 5.1.1
- Fixes: rhbz#2280943

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 5.0.0-5
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 5.0.0-3
- Rebuilt for Python 3.13

* Wed Apr 24 2024 Tomáš Hrnčiar <thrnciar@redhat.com> - 5.0.0-2
- Backport upstream patch needed for compatibility with python-pkginfo 1.10.0

* Sun Mar 17 2024 Charalampos Stratakis <cstratak@redhat.com> - 5.0.0-1
- Update to 5.0.0
- Resolves: rhbz#2263785

* Thu Feb 29 2024 Michel Lind <salimma@fedoraproject.org> - 4.0.2-4
- Add bcond for documentation building
- Fix warnings when regenerating the RPM by moving post-endif comments to new lines

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 28 2023 Charalampos Stratakis <cstratak@redhat.com> - 4.0.2-1
- Update to 4.0.2
Resolves: rhbz#2150064

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 4.0.1-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Charalampos Stratakis <cstratak@redhat.com> - 4.0.1-1
- Update to 4.0.1
Resolves: rhbz#2092433

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 4.0.0-2
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Charalampos Stratakis <cstratak@redhat.com> - 4.0.0-1
- Update to 4.0.0
Resolves: rhbz#2070773

* Thu Feb 24 2022 Charalampos Stratakis <cstratak@redhat.com> - 3.8.0-1
- Update to 3.8.0 (#2049983)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Charalampos Stratakis <cstratak@redhat.com> - 3.7.1-1
- Update to 3.7.1(#2030010)

* Thu Dec 02 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 3.7.0-1
- Update to 3.7.0
- Fixes: rhbz(#2028309)

* Wed Nov 10 2021 Charalampos Stratakis <cstratak@redhat.com> - 3.6.0-1
- Update to 3.6.0 (#2019939)

* Tue Aug 03 2021 Charalampos Stratakis <cstratak@redhat.com> - 3.4.2-1
- Update to 3.4.2 (#1984151)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Lumír Balhar <lbalhar@redhat.com> - 3.4.1-1
- Update to 3.4.1
Resolves: rhbz#1939380

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Charalampos Stratakis <cstratak@redhat.com> - 3.3.0-1
- Update to 3.3.0 (#1910336)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.2.0-1
- Update to 3.2.0 (#1850277)

* Fri Jun 05 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.1.1-1
- Update to 3.1.1 (#1755042)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.15.0-1
- Update to 1.15.0 (#1750057).
- https://github.com/pypa/twine/blob/1.15.0/docs/changelog.rst

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Jeremy Cline <jcline@redhat.com> - 1.12.2-3
- Bump the obsoletes so the upgrade path from F29 works
- Include the manpage since the dep chain for docs building is broken

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.12.2-1
- Update to 1.12.2 (#1551178).
- https://github.com/pypa/twine/blob/1.12.2/docs/changelog.rst

* Tue Nov 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.10.0-6
- Drop python2 subpackage

* Mon Sep 24 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-5
- Make the keyring dependency optional
- Run tests

* Thu Sep 13 2018 Jeremy Cline <jeremy@jcline.org> - 1.10.0-4
- Update the summary of the "twine" package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-2
- Rebuilt for Python 3.7

* Thu Mar 08 2018 Jeremy Cline <jeremy@jcline.org> - 1.10.0-1
- Update to latest upstream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 Jeremy Cline <jeremy@jcline.org> - 1.9.1-4
- Re-add the Python 2 package (rhbz #1512552)

* Tue Oct 31 2017 Jeremy Cline <jeremy@jcline.org> - 1.9.1-3
- Drop pythonX- subpackages as Twine is a CLI (rhbz #1507815)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Jeremy Cline <jeremy@jcline.org> - 1.9.1-1
- Update to 1.9.1 (#1448841)
- Add python-keyring and python-tqdm as dependencies
- Remove python-clint as a dependency

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-2
- Rebuild for Python 3.6

* Tue Aug 09 2016 Jeremy Cline <jeremy@jcline.org> - 1.8.1-1
- Update to 1.8.1

* Mon Jul 18 2016 Jeremy Cline <jeremy@jcline.org> - 1.7.4-3
- Keep objects.inv to support intersphinx documentation

* Mon Jul 18 2016 Jeremy Cline <jeremy@jcline.org> - 1.7.4-2
- Add clint as a build dependency so the tests pass

* Fri Jul 15 2016 Jeremy Cline <jeremy@jcline.org> - 1.7.4-1
- Update to the latest upstream release
- Add clint as a dependency

* Tue Jul 12 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-5
- Remove unnecessary shebang in __main__.py that caused rpmlint errors

* Mon Jul 11 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-4
- Mark man pages as docs

* Mon Jul 11 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-3
- Use python_version macro rather than hardcoding version numbers.

* Fri Jul 08 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-2
- Update Source0 url to the <name>-<version>.tar.gz format

* Thu Jun 09 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-1
- Initial commit
