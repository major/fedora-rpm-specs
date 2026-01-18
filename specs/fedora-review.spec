# needed for test content
%{?perl_default_filter}
%global __provides_exclude_from %{?_provides_exclude_from:%_provides_exclude_from|}%{_datadir}/fedora-review/
%global __requires_exclude_from %{?_requires_exclude_from:%_requires_exclude_from|}%{_datadir}/fedora-review/test/

#invoke with "--with tests" to enable tests
%bcond_with tests

# See notes in make_release which patches this.
## global     git_tag  .05c5b26

# Support jenkins build number if available.
%global     build_nr %(echo "${BUILD_NUMBER:+.}${BUILD_NUMBER:-%%{nil\\}}")

Name:       fedora-review
Version:    0.11.0
Release:    3%{?build_nr}%{?git_tag}%{?dist}
Summary:    Review tool for fedora rpm packages

License:    GPL-2.0-or-later
URL:        https://pagure.io/FedoraReview
Source0:    https://releases.pagure.org/FedoraReview/fedora_review-%{version}%{?git_tag}.tar.gz

BuildArch:  noarch

BuildRequires:  mock >= 3.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-bugzilla
BuildRequires:  python3-packaging
BuildRequires:  python3-urlgrabber
BuildRequires:  python3-straight-plugin
BuildRequires:  python3-devel
BuildRequires:  python3-rpm
BuildRequires:  python3-dnf

Requires:       bc
Requires:       fedora-packager
Requires:       python3-beautifulsoup4
Requires:       python3-bugzilla
Requires:       python3-packaging
Requires:       python3-urlgrabber
Requires:       python3-straight-plugin
Requires:       python3-rpm
Requires:       python3-dnf
# licensecheck used to be in rpmdevtools, moved to devscripts later
# this is compatible with both situations without ifdefs
Requires:       %{_bindir}/licensecheck
Requires:       license-validate
# We require DNF and the repoquery command
Requires:       dnf
Requires:       dnf-command(repoquery)
# Ugh, we now require mock since we import modules from it...
Requires:       mock >= 3.0
# Used by check-large-docs
Requires:       bc

# Let's be consistent with the name used on pagure.io
Provides:       FedoraReview = %{version}-%{release}

Provides:       %{name}-php-phpci = %{version}-%{release}
Obsoletes:      %{name}-php-phpci < %{version}-%{release}


%description
This tool automates much of the dirty work when reviewing a package
for the Fedora Package Collection like:

    * Downloading SRPM & SPEC.
    * Download upstream source
    * Check md5sums
    * Build and install package in mock.
    * Run rpmlint.
    * Generate a review template, which becomes the starting
      point for the review work.

The tool is composed of plugins, one for each supported language.
As of today, there is plugins for C/C++, Ruby, java, R, perl and
python.  There is also support for external tests that can be written
in a simple way in bash.


%package plugin-ruby
Summary: Enhanced ruby tests for fedora-review
Requires: %{name} = %{version}-%{release}

%description plugin-ruby
fedora-review ruby-specific tests, not installed by default.


%package tests
Summary: Test and test data files for fedora-review
Requires: %{name} = %{version}-%{release}

%description tests
Tests are packaged separately due to space concerns.


%prep
%autosetup -p1 -n fedora_review-%{version}


%build
%py3_build


%install
%py3_install
pkg_dir="%{buildroot}/%{python3_sitelib}/FedoraReview"
ln -s %{_datadir}/%{name}/scripts $pkg_dir/scripts
ln -s %{_datadir}/%{name}/plugins $pkg_dir/plugins
cd test
bash < restore-links.sh
rm restore-links.sh remember-links
cd ..
cp -ar test "%{buildroot}%{_datadir}/%{name}"
cp -a pycodestyle.conf pylint.conf "%{buildroot}%{_datadir}/%{name}"


%check
%if %{with tests}
cd test
export REVIEW_LOGLEVEL=warning
export MAKE_RELEASE=1
mock --quiet -r fedora-38-x86_64 --init
mock --quiet -r fedora-38-x86_64 --uniqueext=hugo --init
%{__python3} -m unittest discover -f
%endif


%files
%doc README
%license COPYING AUTHORS
%{python3_sitelib}/FedoraReview
%{python3_sitelib}/fedora_review-%{version}-py%{python3_version}.egg-info
%{_bindir}/fedora-review
%{_bindir}/fedora-create-review
%{_bindir}/koji-download-scratch
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/fedora-create-review.1.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/plugins
%exclude %{_datadir}/%{name}/plugins/ruby.py
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/pycodestyle.conf
%{_datadir}/%{name}/pylint.conf

%files plugin-ruby
%{_datadir}/%{name}/plugins/ruby.py

%files tests
%doc test/README.test
%{_datadir}/%{name}/test


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sat Dec 06 2025 Jakub Kadlcik <frostyx@email.cz> - 0.11.0-2
- Drop leftover dependency on python3-nose

* Sun Nov 16 2025 Jakub Kadlcik <frostyx@email.cz> - 0.11.0-1
- New upstream version

* Thu Aug 03 2023 Benson Muite <benson_muite@emailplus.org> - 0.10.0-3
- Add bc as a required dependency

* Wed Jul 26 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.10.0-2
- Fix shebangs to properly invoke python3
- Use Fedora 38 mock chroot instead of the EOLed and unavailable Fedora 36

* Mon Jul 24 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.10.0-1
- New upstream release 0.10.0
- Use SPDX license identifier

* Tue Aug 23 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.0-1
- New upstream release 0.9.0

* Thu Apr 07 2022 Neal Gompa <ngompa13@gmail.com> - 0.8.0-1
- New upstream release 0.8.0

* Tue Nov 10 2020 Neal Gompa <ngompa13@gmail.com> - 0.7.6-1
- New upstream release 0.7.6

* Sun Feb 16 2020 Neal Gompa <ngompa13@gmail.com> - 0.7.5-1
- New upstream release 0.7.5

* Sat Dec 07 2019 Neal Gompa <ngompa13@gmail.com> - 0.7.4-1
- New upstream release 0.7.4

* Wed Sep 18 2019 Neal Gompa <ngompa13@gmail.com> - 0.7.3-1
- New upstream release 0.7.3

* Tue Apr 09 2019 Neal Gompa <ngompa13@gmail.com> - 0.7.2-1
- New upstream release 0.7.2

* Thu Mar 21 2019 Neal Gompa <ngompa13@gmail.com> - 0.7.1-1
- New upstream release 0.7.1

* Sun Mar 17 2019 Neal Gompa <ngompa13@gmail.com> - 0.7.0-1
- New upstream release 0.7.0
- Switch to Python 3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.1-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Björn Esser <besser82@fedoraproject.org> - 0.6.1-6
- Fix shebangs in %%{_bindir}

* Fri Jun 02 2017 Björn Esser <besser82@fedoraproject.org> - 0.6.1-5
- Add mock-option '--no-bootstrap-chroot' to defaults, if mock >= 1.4.1
- Update spec file to recent guidelines
- Change package url and source to Pagure

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 06 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6.1-3
- Drop requirement to python-argparse now that it has been in python's stdlib
  for so long

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 02 2016 Alec Leamas <leamas.alec@gmail.com> - 0.6.1-1.f03e4e7
- New upstream release 0.6.1

* Tue Feb 16 2016 Orion Poplawski <orion@cora.nwra.com> - 0.6.0-4
- Exclude test content from perl requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 Alec Leamas <leamas.alec@gmail.com> - 0.6.0-1.afb5485
- Update to 0.6.0

* Mon May 04 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.5.3-1
- Update to 0.5.3

* Wed Apr 22 2015 Adam Miller <maxamillion@fedoraproject.org> - 0.5.2-3
- Add conditional for unittest2 for epel7 (thanks mcepl@redhat.com for the fix)

* Mon Jan 19 2015 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5.2-2
- Add patch for rhbz#1151943

* Mon Jul 14 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5.2-1
- Update to latest upstream bugfix release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 13 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5.1-2
- Backport fixes for several bugs
- Resolves: rhbz#1044580
- Resolves: rhbz#1049042

* Fri Dec 13 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5.1-1
- Update to latest upstream (0.5.1)

* Tue Oct 15 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5.0-3
- Really use phpcompatinfo instead of phpci

* Mon Oct 14 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5.0-2
- Fix requires for licensecheck (#1016309)
- Remove separate php plugin subpackage (#971875)

* Fri Aug 30 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5.0-1
- Updating to upstream 0.5.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.4.1-3
- Perl 5.18 rebuild

* Thu May 30 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.4.1-2
- Backport fix for #967571

* Mon Apr 29 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.4.1-1
- Update to latest upstream version

* Tue Feb 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.4.0-4
- Fix rhbz912182
- Reorganize patches a bit

* Fri Feb  8 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.4.0-3
- Fix rhbz908830 and rhbz908830
- Add patch for REVIEW_NO_MOCKGROUP_TEST environment variable
- Remove old patch

* Mon Feb 04 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.0-2
- Add Patch0 (0001-Fix-syntax-error.patch) from Ralph Bean fixing fedora-create-review

* Mon Jan 28 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.4.0-1
- Updating to upstream 0.4.0

* Wed Nov 07 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.3.1-3
- Backport from upstream's git fix to RHBZ#874246 (Patch0)

* Thu Oct 25 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.3.1-2
- Add symlink to scripts directory so they are loaded

* Tue Sep 25 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.3.1-1
- Update to lastest upstream (0.3.1)
- Fix loading of system-wide plugins
- Add back suport for EL6

* Mon Sep 24 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.3.0-1
- Update to lastest upstream (0.3.0)
- Remove no longer needed build workarounds

* Thu Aug  9 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.2.2-1
- Update to lastest upstream (0.2.2)
- Add koji-download-scratch script

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.2.0-1
- Update to latest release (0.2.0)

* Fri Feb 24 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.3-1
- Update to latest bugfix release

* Fri Jan 13 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.2-1
- Update to latest bugfix release
- Add fedora-create-review script

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan 11 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-2
- Add wget as requires

* Wed Nov 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.1-1
- New upstream bugfix release

* Wed Nov 16 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.0-2
- Remove things not needed in el6+

* Thu Nov 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.0-1
- Initial packaging work for Fedora
