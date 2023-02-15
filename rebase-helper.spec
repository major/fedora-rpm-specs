%{?python_enable_dependency_generator}

%global pkgname rebasehelper

Name:           rebase-helper
Version:        0.28.0
Release:        1%{?dist}
Summary:        The tool that helps you to rebase your package to the latest version

License:        GPLv2+
URL:            https://github.com/rebase-helper/rebase-helper
Source0:        https://github.com/rebase-helper/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-setuptools_scm_git_archive
BuildRequires:  python3-specfile
BuildRequires:  python3-rpm
BuildRequires:  python3-rpkg
BuildRequires:  python3-koji
BuildRequires:  python3-pyquery
BuildRequires:  python3-copr
BuildRequires:  python3-pam
BuildRequires:  python3-requests
BuildRequires:  python3-requests-gssapi
BuildRequires:  python3-GitPython
BuildRequires:  python3-ansicolors
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-m2r
BuildRequires:  python3-pytest
BuildRequires:  python3-unidiff

Requires:       git
Requires:       rpm-build
Requires:       mock
Requires:       python3-setuptools
Requires:       python3-koji
Requires:       python3-unidiff

Recommends:     licensecheck
Recommends:     rpmlint
Recommends:     libabigail
Recommends:     pkgdiff >= 1.6.3
Recommends:     rpminspect-data-fedora


%description
rebase-helper is a tool which helps package maintainers to rebase their
packages to latest upstream versions.
There are several steps that need to be done when rebasing a package.
The goal of rebase-helper is to automate most of these steps.


%prep
%setup -q

# remove bundled egg-info
rm -rf %{pkgname}.egg-info


%build
%py3_build

# generate man page
make SPHINXBUILD=sphinx-build-3 man

# generate bash completion script
make PYTHON=%{__python3} PYTHONPATH=$(pwd) completion

# generate sample configuration file
make PYTHON=%{__python3} PYTHONPATH=$(pwd) sample_config


%install
%py3_install

# install man page
mkdir -p %{buildroot}%{_datadir}/man/man1/
install -p -m 0644 build/man/rebase-helper.1 %{buildroot}%{_datadir}/man/man1

# install bash completion
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
install -p -m 0644 build/rebase-helper.bash %{buildroot}%{_datadir}/bash-completion/completions/rebase-helper


%check
PYTHONPATH=$(pwd) py.test-3 -v tests


%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%doc build/rebase-helper.cfg
%{_bindir}/%{name}
%{python3_sitelib}/%{pkgname}/
%{python3_sitelib}/%{pkgname}-*-py%{python3_version}.egg-info
%{_mandir}/man1/rebase-helper.1*
%{_datadir}/bash-completion/completions/rebase-helper


%changelog
* Mon Feb 13 2023 Packit <hello@packit.dev> - 0.28.0-1
News in version 0.28.0:

- *debuginfo* packages are now skipped when running **sonamecheck**
- Replaced our own implementation of lookaside cache client with *rpkg*
- Switched from docker to podman in GitHub Actions
- Added a 30 seconds time limit to bugzilla queries
- Dropped support for Python < 3.9 and EPEL 8
- Switched to [specfile](https://github.com/packit/specfile) library
- Removed `--keep-comments` option

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Packit <hello@packit.dev> - 0.27.0-1
News in version 0.27.0:

- Added support for `rpmuncompress` being used by `rpm` >= 4.18
- Replaced hardcoded references to *master* branch
- Fixed typos in `%preun`, `%postun` and `%generate_buildrequires` section names
- Fixed parsing of macros with multiline bodies in `` output
- Fixed parsing issue in **rpmdiff** checker
- **rebase-helper** now removes any existing submodule configuration from upstream tarballs before rebasing to avoid errors due to submodules not being checked out
- **rebase-helper** now warns about a potential rename that can't be handled automatically, such as `README` to `README.md`
- **rebase-helper** is now able to handle unexpected `git rebase` errors


* Tue Jun 21 2022 Nikola Forró <nforro@redhat.com> - 0.26.0-4
- Add support for rpmuncompress (#2093918)

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.26.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 27 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.26.0-1
- Release 0.26.0 (Nikola Forró)
- Use long options with rpmdiff (Nikola Forró)
- Make copr project creation more robust (František Nečas)
- spec: sources may not be defined (Tomas Tomecek)
- Explicitly specify encoding as per PEP597 (František Nečas)
- Re-enable fixed subscriptable check (František Nečas)
- Do not traceback when setting the original locale fails (Nikola Forró)
- Use an older version of base images (František Nečas)
- Fix release checkout reference syntax (František Nečas)
- Replace webhooks with Github Actions (František Nečas)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.25.0-1
- Release 0.25.0 (Nikola Forró)
- Switch from python docker images to UBI (Nikola Forró)
- Make container with tests privileged (František Nečas)
- Replace soon-to-be deprecated distutils (František Nečas)
- Fix licensecheck availability test (Nikola Forró)
- Fix macro value detection in set_tag (František Nečas)
- Support exception chaining (PEP 3134) in autoargs (Nikola Forró)
- Fix for Sphinx 4 (Nikola Forró)
- Install required library stubs (František Nečas)
- Migrate to Github actions (František Nečas)
- Use Fedora registry for Fedora images (Nikola Forró)
- Add glibc-langpack-de to base images (Nikola Forró)
- CONTRIBUTING.md: Start a contributing file (Stef Walter)
- FIXUP for review (Stef Walter)
- Use C locale for updating %changelog (Stef Walter)
- Change approach to lookaside cache servers (Nikola Forró)
- Add lookaside cache preset for centpkg (Nikola Forró)
- Avoid using deprecated mock option (Nikola Forró)
- Add missing make to BuildRequires (Nikola Forró)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.24.0-2
- Rebuilt for Python 3.10

* Wed Feb 10 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.24.0-1
- Release 0.24.0 (Nikola Forró)
- Fix collections deprecation in test_tags (František Nečas)
- Add EPEL 8 to packit config (Nikola Forró)
- Make unidiff a regular requirement (Nikola Forró)
- Add missing python3-setuptools_scm_git_archive to base images (Nikola Forró)
- Refactor SpecFile._process_patches() (Nikola Forró)
- Sanitize paths in patches before applying with git-apply (Nikola Forró)
- Suppress errors also when deleting macros (Nikola Forró)
- Add option to disable removing comments (František Nečas)
- Ignore only Patch/Source tags when removing comments (František Nečas)
- Add --no-changelog-entry option (Nikola Forró)
- Suppress errors when expanding macros during parsing of tags (Nikola Forró)
- Mark test_rebase as xfail (Nikola Forró)
- update packit.yaml (Tomas Tomecek)
- Limit koji buildtool to a single architecture (Nikola Forró)
- Fix updating build dict when getting old build from Koji (Nikola Forró)
- Add rpms namespace to integration data path (Nikola Forró)
- Only use opportunistic authentication with Fedora servers (Nikola Forró)
- Update URL of lookaside cache downloads (Nikola Forró)
- Allow to specify lookaside cache configuration preset (Nikola Forró)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.23.1-1
- new upstream release: 0.23.1

* Fri Aug 28 2020 rebase-helper <rebase-helper@localhost.local> - 0.23.0-1
- new upstream release: 0.23.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.22.0-2
- Rebuilt for Python 3.9

* Tue Mar 31 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.22.0-1
- new upstream release: 0.22.0

* Fri Feb 21 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.21.0-1
- new upstream release: 0.21.0

* Mon Feb 03 2020 Nikola Forró <nforro@redhat.com> - 0.20.0-3
- Remove deprecated encoding parameter in json.load for Python 3.9 (#1796391)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Nikola Forró <nforro@redhat.com> - 0.20.0-1
- new upstream release: 0.20.0

* Thu Sep 26 2019 Nikola Forró <nforro@redhat.com> - 0.19.0-1
- new upstream release: 0.19.0

* Thu Aug 22 2019 Nikola Forró <nforro@redhat.com> - 0.18.0-1
- new upstream release: 0.18.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.2-2
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Nikola Forró <nforro@redhat.com> - 0.17.2-1
- new upstream release: 0.17.2

* Tue Aug 06 2019 Nikola Forró <nforro@redhat.com> - 0.17.1-1
- new upstream release: 0.17.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Nikola Forró <nforro@redhat.com> - 0.16.3-1
- New release 0.16.3 (#1686469)

* Fri Mar 01 2019 Nikola Forró <nforro@redhat.com> - 0.16.1-1
- New release 0.16.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.0-2
- Enable python dependency generator

* Fri Dec 21 2018 Nikola Forró <nforro@redhat.com> - 0.15.0-1
- New release 0.15.0

* Fri Oct 05 2018 Nikola Forró <nforro@redhat.com> - 0.14.0-1
- New release 0.14.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-2
- Rebuilt for Python 3.7

* Wed May 23 2018 Nikola Forró <nforro@redhat.com> - 0.13.2-1
- New release 0.13.2 (#1562375)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Nikola Forró <nforro@redhat.com> - 0.12.0-1
- New release 0.12.0 (#1527597)

* Wed Oct 04 2017 Nikola Forró <nforro@redhat.com> - 0.11.0-1
- New release 0.11.0 (#1498782)

* Wed Aug 30 2017 Nikola Forró <nforro@redhat.com> - 0.10.1-1
- New release 0.10.1 (#1486607)

* Fri Aug 25 2017 Nikola Forró <nforro@redhat.com> - 0.10.0-1
- New release 0.10.0 (#1485315)
- Update for python3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Nikola Forró <nforro@redhat.com> - 0.9.0-1
- New release 0.9.0
- Install generated man page
- Add missing python-copr dependency (#1391461)

* Tue Nov 22 2016 Petr Hracek <phracek@redhat.com> - 0.8.0-3
- Fix for result dir (#1397312)

* Wed Aug 17 2016 Petr Hracek <phracek@redhat.com> - 0.8.0-2
- Fix bug caused by dependency to python-pyquery (#1363777)

* Sun Jul 31 2016 Tomas Hozza <thozza@redhat.com> - 0.8.0-1
- New release 0.8.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 26 2016 Nikola Forró <nforro@redhat.com> - 0.7.3-2
- Clear output data on Application initialization

* Mon Apr 11 2016 Petr Hracek <phracek@redhat.com> - 0.7.3-1
- New upstream release 0.7.3. It contains fixes. (#1325599)

* Tue Mar 15 2016 Petr Hracek <phracek@redhat.com> - 0.7.2-1
- New upstream release 0.7.2

* Mon Feb 22 2016 Petr Hracek <phracek@redhat.com> - 0.7.1-1
- New upstream version 0.7.1 (#1310640)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Petr Hracek <phracek@redhat.com> - 0.7.0-1
- New upstream version 0.7.0 (#1298403)

* Mon Nov 09 2015 Petr Hracek <phracek@redhat.com> - 0.6.2-1
- New upstream version 0.6.2 (#1280294)
- support upstream monitoring service

* Fri Jul 31 2015 Petr Hracek <phracek@redhat.com> - 0.6.0-1
- New upstream version 0.6.0 (#1249518)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Petr Hracek <phracek@redhat.com> - 0.5.0-1
- New upstream version 0.5.0 #1224680

* Thu Mar 05 2015 Petr Hracek <phracek@redhat.com> - 0.4.0-3
- Add man page (#1185985)

* Mon Jan 19 2015 Petr Hracek <phracek@redhat.com> - 0.4.0-2
- Remove dependency to pkgdiff from setup (#1176563)

* Fri Dec 05 2014 Petr Hracek <phracek@redhat.com> - 0.4.0-1
- New upstream release

* Fri Jul 25 2014 Petr Hracek <phracek@redhat.com> - 0.3.1-1
- New upstream release
- Add --build-only option
- Catch Keyboard Interupted
- Add --continue option for rebases

* Tue Jul 08 2014 Tomas Hozza <thozza@redhat.com> - 0.3.0-0.4.20140624git
- Add requires on pkgdiff

* Mon Jun 23 2014 Petr Hracek <phracek@redhat.com> - 0.3.0-0.3.20140624git
- Include LICENSE text file
- use __python2 macros

* Mon Jun 23 2014 Petr Hracek <phracek@redhat.com> - 0.3.0-0.2.20140623git
- Removed shebang from __init__.py file

* Mon Jun 23 2014 Petr Hracek <phracek@redhat.com> - 0.3.0-0.1.20140623git
- Initial version

