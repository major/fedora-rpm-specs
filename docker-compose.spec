Name:           docker-compose
Version:        1.29.2
Release:        10%{?dist}
Summary:        Multi-container orchestration for Docker
License:        ASL 2.0
URL:            https://github.com/docker/compose
Source0:        %pypi_source
BuildArch:      noarch

Patch:          pytest-7.2-compatibility.patch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-distro
BuildRequires:  python%{python3_pkgversion}-dotenv
BuildRequires:  python%{python3_pkgversion}-ddt

BuildRequires:  python%{python3_pkgversion}-cached_property >= 1.5.1
BuildRequires:  python%{python3_pkgversion}-chardet >= 3.0.4
BuildRequires:  python%{python3_pkgversion}-distro >= 1.5.0
BuildRequires:  python%{python3_pkgversion}-docker >= 5.0.0
BuildRequires:  python%{python3_pkgversion}-docker-pycreds >= 0.4.0
BuildRequires:  python%{python3_pkgversion}-dockerpty >= 0.4.1
BuildRequires:  python%{python3_pkgversion}-docopt >= 0.6.2
BuildRequires:  python%{python3_pkgversion}-idna >= 2.10
BuildRequires:  python%{python3_pkgversion}-jsonschema >= 3.2.0
BuildRequires:  python%{python3_pkgversion}-pysocks >= 1.7.1
BuildRequires:  python%{python3_pkgversion}-requests >= 2.24.0
BuildRequires:  python%{python3_pkgversion}-six >= 1.12.0
BuildRequires:  python%{python3_pkgversion}-texttable >= 1.6.2
BuildRequires:  python%{python3_pkgversion}-websocket-client >= 0.57.0
BuildRequires:  python%{python3_pkgversion}-yaml >= 5.4.1

Requires:       python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-cached_property >= 1.5.1
Requires:       python%{python3_pkgversion}-chardet >= 3.0.4
Requires:       python%{python3_pkgversion}-distro >= 1.5.0
Requires:       python%{python3_pkgversion}-docker >= 5.0.0
Requires:       python%{python3_pkgversion}-docker-pycreds >= 0.4.0
Requires:       python%{python3_pkgversion}-dockerpty >= 0.4.1
Requires:       python%{python3_pkgversion}-docopt >= 0.6.2
Requires:       python%{python3_pkgversion}-idna >= 2.10
Requires:       python%{python3_pkgversion}-jsonschema >= 3.2.0
Requires:       python%{python3_pkgversion}-pysocks >= 1.7.1
Requires:       python%{python3_pkgversion}-requests >= 2.24.0
Requires:       python%{python3_pkgversion}-six >= 1.12.0
Requires:       python%{python3_pkgversion}-texttable >= 1.6.2
Requires:       python%{python3_pkgversion}-websocket-client >= 0.57.0
Requires:       python%{python3_pkgversion}-yaml >= 5.4.1

Requires:       python%{python3_pkgversion}-attrs >= 20.3.0
Requires:       python%{python3_pkgversion}-certifi >= 2020.6.20


%description
Compose is a tool for defining and running multi-container Docker
applications. With Compose, you use a Compose file to configure your
application's services. Then, using a single command, you create and
start all the services from your configuration.

Compose is great for development, testing, and staging environments,
as well as CI workflows.

Using Compose is basically a three-step process.

1. Define your app's environment with a Dockerfile so it can be
   reproduced anywhere.
2. Define the services that make up your app in docker-compose.yml so
   they can be run together in an isolated environment:
3. Lastly, run docker-compose up and Compose will start and run your
   entire app.


%prep
%autosetup -p 1
rm -rf docker_compose.egg-info

# Remove dependency version constraints not relevant in Fedora/EPEL
sed -e 's/, < [0-9.]\+//' -i setup.py


%build
%py3_build


%install
%py3_install
install -D -p -m 644 contrib/completion/bash/docker-compose %{buildroot}%{_datadir}/bash-completion/completions/docker-compose
install -D -p -m 644 contrib/completion/zsh/_docker-compose %{buildroot}%{_datadir}/zsh/site-functions/_docker-compose
install -D -p -m 644 contrib/completion/fish/docker-compose.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/docker-compose.fish


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} --verbose tests/unit


%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{python3_sitelib}/compose
%{python3_sitelib}/docker_compose-%{version}-py%{python3_version}.egg-info
%{_datadir}/bash-completion
%{_datadir}/zsh
%{_datadir}/fish


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Python Maint <python-maint@redhat.com> - 1.29.2-9
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Lumír Balhar <lbalhar@redhat.com> - 1.29.2-7
- Fix compatibility with pytest 7.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.29.2-5
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.29.2-2
- Rebuilt for Python 3.10

* Mon May 10 2021 Michael Hampton <error@ioerror.us> - 1.29.2-1
- Update to 1.29.2

* Wed Apr 21 2021 Michael Hampton <error@ioerror.us> - 1.29.1-1
- Rebase to 1.29.1

* Mon Mar 29 2021 Michael Hampton <error@ioerror.us> - 1.28.6-1
- Rebase to 1.28.6

* Fri Feb 26 2021 Michael Hampton <error@ioerror.us> - 1.28.5-1
- Rebase to 1.28.5

* Fri Feb 19 2021 Michael Hampton <error@ioerror.us> - 1.28.4-1
- Rebase to 1.28.4

* Wed Jan 27 2021 Michael Hampton <error@ioerror.us> - 1.28.2-1
- Rebase to 1.28.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Michael Hampton <error@ioerror.us> - 1.28.0-1
- Rebase to 1.28.0

* Thu Sep 24 2020 Michael Hampton <error@ioerror.us> - 1.27.4-1
- Rebase to 1.27.4

* Wed Sep 16 2020 Michael Hampton <error@ioerror.us> - 1.27.3-2
- Requires python-docker 4.3.1

* Wed Sep 16 2020 Michael Hampton <error@ioerror.us> - 1.27.3-1
- Rebase to 1.27.3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Michael Hampton <error@ioerror.us> - 1.26.2-1
- Rebase to 1.26.2
- Add python-distro build dependency
- Add python-dotenv build dependency

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.25.4-2
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Michael Hampton <error@ioerror.us> - 1.25.4-2
- Remove patch for BZ#1705955 it is now in upstream source
- Add python-ddt build dependency

* Sat Feb 29 2020 Michael Hampton <error@ioerror.us> - 1.25.4-1
- Rebase to 1.25.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct  7 2019 Michael Hampton <error@ioerror.us> - 1.24.1-3
- Require python-docker 4.0.2-2 for ssh feature

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.24.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Sep 17 2019 Michael Hampton <error@ioerror.us> - 1.24.1-2
- Require python-docker 4.0.2 for ssh feature

* Wed Aug 28 2019 Michael Hampton <error@ioerror.us> - 1.24.1-1
- Rebase to 1.24.1 (BZ#1691898)
- Patch tests for pytest 5 compatibility (BZ#1705955)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.22.0-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Michael Hampton <error@ioerror.us> - 1.22.0-4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 08 2018 Carl George <carl@george.computer> - 1.22.0-2
- Run upstream unit tests

* Wed Jul 18 2018 Michael Hampton <error@ioerror.us> - 1.22.0-1
- Update to 1.22.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.20.1-2
- Rebuilt for Python 3.7

* Tue Mar 27 2018 Michael Hampton <error@ioerror.us> - 1.20.1-1
- Update to 1.20.1

* Wed Mar 21 2018 Michael Hampton <error@ioerror.us> - 1.20.0-1
- Update to 1.20.0

* Fri Mar 02 2018 Adam Williamson <awilliam@redhat.com> - 1.19.0-2
- Backport upstream patch for compatibility with python-docker 3.0.0

* Mon Feb 19 2018 Michael Hampton <error@ioerror.us> - 1.19.0-1
- Update to 1.19.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 26 2017 Carl George <carl@george.computer> - 1.18.0-1
- Latest upstream
- Drop patch0 and patch1, use sed on setup.py instead
- Rebase patch2

* Thu Nov  9 2017 Michael Hampton <error@ioerror.us> - 1.17.1-1
- Update to 1.17.1 (#1511455)

* Thu Nov  2 2017 Michael Hampton <error@ioerror.us> - 1.17.0-1
- Update to 1.17.0 (#1504337)

* Sun Sep 10 2017 Carl George <carl@george.computer> - 1.16.1-2
- Align dependencies with upstream
- RHEL compatibility
- Add bash, zsh, and fish completions

* Sat Sep  2 2017 Michael Hampton <error@ioerror.us> - 1.16.1-1
- Update to 1.16.1 (#1483776)

* Fri Jul 28 2017 Michael Hampton <error@ioerror.us> - 1.15.0-1
- Update to 1.15.0 (#1471093)
- Explicit python3-docker requirement
- New upstream requirements python3-pysocks, python3-certifi, python3-idna

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Michael Hampton <error@ioerror.us> - 1.14.0-1
- Update to upstream 1.14.0

* Mon May  8 2017 Michael Hampton <error@ioerror.us> - 1.13.0-1
- Update to upstream 1.13.0

* Fri Apr  7 2017 Michael Hampton <error@ioerror.us> - 1.12.0-1
- Update to upstream 1.12.0

* Thu Mar  2 2017 Michael Hampton <error@ioerror.us> - 1.11.2-1
- Update to upstream 1.11.2

* Tue Feb 28 2017 Michael Hampton <error@ioerror.us> - 1.11.1-3
- Remove requirements upper bound from setup.py; BZ#1426145
- Added new dependency python3-colorama

* Fri Feb 17 2017 Michael Hampton <error@ioerror.us> - 1.11.1-2
- python-docker-py package name changed to python-docker; BZ#1422198

* Fri Feb 10 2017 Michael Hampton <error@ioerror.us> - 1.11.1-1
- Update to upstream 1.11.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb  3 2017 Michael Hampton <error@ioerror.us> - 1.10.1-1
- Update to upstream 1.10.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-3
- Rebuild for Python 3.6

* Mon Nov 21 2016 Michael Hampton <error@ioerror.us> - 1.9.0-2
- BZ#1396852

* Sat Nov 19 2016 Michael Hampton <error@ioerror.us> - 1.9.0-1
- Update to upstream 1.9.0

* Fri Sep 23 2016 Michael Hampton <error@ioerror.us> - 1.8.1-1
- Update to upstream 1.8.1

* Sat Sep 10 2016 Michael Hampton <error@ioerror.us> - 1.8.0-2
- Port to Python 3, BZ#1374656

* Thu Jul 28 2016 Michael Hampton <error@ioerror.us> - 1.8.0-1
- Update to upstream 1.8.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 05 2016 Michael Hampton <error@ioerror.us> - 1.7.1-1
- Update to upstream 1.7.1
- Updated package description from upstream

* Thu Apr 14 2016 Michael Hampton <error@ioerror.us> - 1.7.0-1
- Update to upstream 1.7.0

* Fri Feb 05 2016 Michael Hampton <error@ioerror.us> - 1.6.0-1
- Update to upstream 1.6.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Michael Hampton <error@ioerror.us> - 1.5.2-4
- Added missing dependency python-enum34

* Mon Jan 11 2016 Michael Hampton <error@ioerror.us> - 1.5.2-3
- Added missing dependency python-jsonschema

* Wed Dec 30 2015 Michael Hampton <error@ioerror.us> - 1.5.2-2
- Updated locations of docs

* Wed Dec 30 2015 Michael Hampton <error@ioerror.us> - 1.5.2-1
- Update to upstream 1.5.2

* Wed Sep 23 2015 Michael Hampton <error@ioerror.us> - 1.4.2-1
- Fixes a regression in the 1.4.1 release that would cause
  docker-compose up without the -d option to exit immediately.

* Wed Sep 16 2015 Michael Hampton <error@ioerror.us> - 1.4.1-1
- Update to upstream 1.4.1

* Wed Aug 12 2015 Michael Hampton <error@ioerror.us> - 1.4.0-1
- Update to upstream 1.4.0
- Update Summary to match upstream summary

* Sat May 16 2015 Michael Hampton <error@ioerror.us> - 1.2.0-3
- Update Obsoletes EVR per packaging guidelines BZ#1213111

* Sun Apr 19 2015 Michael Hampton <error@ioerror.us> - 1.2.0-2
- Update location of LICENSE file

* Sat Apr 18 2015 Michael Hampton <error@ioerror.us> - 1.2.0-1
- Update to 1.2.0
- Added new doc SWARM.md
- Removed docker package requires as it is not required to build or run the
  package, only to run tests, which we can't do anyway
- Removed commented code relating to running tests, which we can't do anyway
- Made package noarch as docker-io is no longer required

* Mon Mar 23 2015 Michael Hampton <error@ioerror.us> - 1.1.0-1
- Update to 1.1.0 including upstream name change
- Requires python-dockerpty
- Requires python-docker-py >= 0.7.1-3 BZ#1197300

* Tue Mar 17 2015 Matej Stuchlik <mstuchli@redhat.com> - 1.0.1-2
- Completely remove version specs from setup.py

* Tue Mar 17 2015 Matej Stuchlik <mstuchli@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Wed Dec 03 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.0.0-5
- Remove upper bound from setup.py requires

* Wed Nov 12 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.0.0-4
- Add python-setuptools to requires

* Thu Oct 23 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.0.0-3
- Relax strict version requirements on websocket-client (#1155510)

* Tue Oct 21 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.0.0-2
- Update Requires

* Tue Oct 21 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.0.0-1
- Update to 1.0.0
- Droped the two patches

* Tue Oct 21 2014 Matej Stuchlik <mstuchli@redhat.com> - 0.5.2-2
- Explicitly disable debuginfo subpackage (#1154780)
- Add python-docker-py to Requires (#1154874)

* Thu Oct 09 2014 Matej Stuchlik <mstuchli@redhat.com> - 0.5.2-1
- Initial spec based on rhbz#1129889
