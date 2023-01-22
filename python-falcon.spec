%global commit      381621701f2de4da91c526f1f8f2c6fc82c3216b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global common_description %{expand:
Falcon is a minimalist ASGI/WSGI framework for building mission-critical REST
APIs and microservices, with a focus on reliability, correctness, and
performance at scale.  When it comes to building HTTP APIs, other frameworks
weigh you down with tons of dependencies and unnecessary abstractions. Falcon
cuts to the chase with a clean design that embraces HTTP and the REST
architectural style.}


Name:           python-falcon
Version:        4.0.0~^1.%{shortcommit}
Release:        2%{?dist}
Summary:        Fast ASGI+WSGI framework for building data plane APIs at scale
License:        Apache-2.0
URL:            https://falconframework.org
Source:         https://github.com/falconry/falcon/archive/%{commit}/falcon-%{shortcommit}.tar.gz

# downstream-only patch to remove bundled library
Patch:          0001-Use-system-mimeparse.patch

BuildRequires:  gcc


%description %{common_description}


%package -n python3-falcon
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools pip wheel cython}
# requirements/tests
BuildRequires:  %{py3_dist pytest pyyaml requests testtools}
BuildRequires:  %{py3_dist pytest-asyncio httpx uvicorn aiofiles websockets}
BuildRequires:  %{py3_dist cbor2 msgpack mujson ujson python-mimeparse}


%description -n python3-falcon %{common_description}


%prep
%autosetup -p 1 -n falcon-%{commit}
rm -rf falcon/vendor


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files falcon


%check
# test_float_converter in tests/test_uri_converters.py fails with:
# TypeError: Expected unicode, got float
# skip for now so we can resolve rhbz#2098905
%pytest -k 'not test_float_converter' tests


%files -n python3-falcon -f %{pyproject_files}
%doc README.rst
%{_bindir}/falcon-bench
%{_bindir}/falcon-inspect-app
%{_bindir}/falcon-print-routes


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0~^1.3816217-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 26 2022 Carl George <carl@george.computer> - 4.0.0~^1.3816217-1
- Update to latest upstream snapshot
- Resolves rhbz#2098905 rhbz#2113624 rhbz#2068564

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Python Maint <python-maint@redhat.com> - 3.0.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Carl George <carl@george.computer> - 3.0.1-1
- Latest upstream
- Resolves: rhbz#1959197

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.10

* Wed Apr 21 2021 Carl George <carl@george.computer> - 3.0.0-2
- Run media handlers tests

* Mon Apr 12 2021 Carl George <carl@george.computer> - 3.0.0-1
- Latest upstream
- Fixes: rhbz#1684836

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Javier Peña <jpena@redhat.com> - 2.0.0-1
- Updated to upstream 2.0.0
- This version removed Python 2.7 support

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Carl George <carl@george.computer> - 1.4.1-7
- Disable python2 subpackage on Fedora 31+ rhbz#1701670
- Run tests from buildroot, not builddir

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-4
- Rebuilt for Python 3.7

* Mon Feb 26 2018 Carl George <carl@george.computer> - 1.4.1-3
- Add BuildRequires for gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Carl George <carl@george.computer> - 1.4.1-1
- Latest upstream rhbz#1535255

* Tue Jan 16 2018 Carl George <carl@george.computer> - 1.4.0-1
- Latest upstream rhbz#1528076
- Recommend ujson on Fedora

* Thu Sep 07 2017 Carl George <carl@george.computer> - 1.3.0-1
- Latest upstream
- Enable python34 EPEL subpackage

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Carl George <carl.george@rackspace.com> - 1.2.0-4
- The test test_deprecated_decorator fails in Koji, add patch006 to skip

* Fri Jun 09 2017 Carl George <carl.george@rackspace.com> - 1.2.0-3
- Only run test suite on F26+ due to pytest 3 requirement

* Thu May 04 2017 Carl George <carl.george@rackspace.com> - 1.2.0-2
- Spec file clean up
- Fix rpmlint error caused by srcname being undefined

* Tue May 02 2017 Carl George <carl.george@rackspace.com> - 1.2.0-1
- Latest upstream
- Switch from nosetests to pytest
- Require mimeparse >= 1.5.2 (related rhbz#1339379)
- Add Patch005 to create versioned scripts
- Include LICENSE

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 24 2016 Carl George <carl.george@rackspace.com> - 1.0.0-1
- Latest upstream
- Patch002 and Patch003 fixed upstream
- Patch004 added to make test suite pass with old version of mimeparse

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Carl George <carl.george@rackspace.com> - 0.3.0-4
- Specify minimum version of python-six
- Change python3 control macros to a bcond macro
- Add bcond macro to optionally require explicit python2 names

* Mon Nov 16 2015 Carl George <carl.george@rackspace.com> - 0.3.0-3
- Add patch to disable coverage
- Add patch to skip test_request_cookie_parsing on Python 3.5

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Sep 01 2015 Carl George <carl.george@rackspace.com> - 0.3.0-1
- Upstream 0.3.0
- Add patch1 to fix GH#558
- Update to new packaging guidelines
- Add new test suite dependencies
- Call nosetests directly

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 05 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.10-5
- Upstream 0.1.10
- No python3 in EL7

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 24 2014 Jamie Lennox <jamielennox@redhat.com> - 0.1.8-2
- Remove now missing doc files
- Remove installed test files

* Thu Feb 27 2014 Jamie Lennox <jamielennox@redhat.com> - 0.1.8-1
- Bump to 0.1.8

* Mon Sep 23 2013 Jamie Lennox <jamielennox@redhat.com> - 0.1.7-1
- Add Python 3 packaging details and patch to fix for Python 3.
- Remove falcon-bench from package.
- Added check section.

* Wed Sep 18 2013 Jamie Lennox <jamielennox@redhat.com> - 0.1.7-1
- Initial package.
