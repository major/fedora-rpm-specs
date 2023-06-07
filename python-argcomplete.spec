# Disable check to avoid pulling unwanted package (fish) into RHEL 9
%if 0%{?rhel} >= 9 && !0%{?epel}
%bcond_with check
%else
%bcond_without check
%endif

Name:          python-argcomplete
Summary:       Bash tab completion for argparse
Version:       2.0.0
Release:       8%{?dist}
License:       ASL 2.0
URL:           https://github.com/kislyuk/argcomplete
Source0:       %pypi_source argcomplete

# Fish in Fedora contains git hash in version which breaks tests,
# this patch removes it
Patch1:        0001-Remove-commit-hash-from-Fish-version.patch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

%if %{with check}
BuildRequires: tcsh
BuildRequires: fish
BuildRequires: /usr/bin/pip
BuildRequires: python3-pexpect
BuildRequires: python3-wheel
%endif

BuildArch:     noarch

%global _description %{expand:
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

 * You are using bash as your shell
 * You are using argparse to manage your command line arguments/options

Argcomplete is particularly useful if your program has lots of
options or subparsers, and if your program can dynamically suggest
completions for your argument/option values (for example, if the user
is browsing resources over the network).}

%description %_description

%package -n python3-argcomplete
Summary:        %{summary}
%description -n python3-argcomplete %_description

%prep
%autosetup -p1 -n argcomplete-%{version}
# Remove useless BRs
sed -i -r -e '/tests_require = /s/"(coverage|flake8|wheel)"[, ]*//g' setup.py

# https://github.com/kislyuk/argcomplete/issues/255
# https://github.com/kislyuk/argcomplete/issues/256
sed -i -e "1s|#!.*python.*|#!%{__python3}|" test/prog scripts/*
sed -i -e "s|python |python3 |" test/test.py

%build
%py3_build

%install
%py3_install

# do not attempt to install to %%bash_completions_dir, see https://bugzilla.redhat.com/2211862
install -Dp -m0644 argcomplete/bash_completion.d/%{name} %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

%if %{with check}
%check
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1914782
# upstream: https://github.com/kislyuk/argcomplete/issues/337
echo "set enable-bracketed-paste off" > .inputrc
export INPUTRC=$PWD/.inputrc

%{python3} setup.py test
%endif

%files -n python3-argcomplete
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/argcomplete-*.egg-info/
%{python3_sitelib}/argcomplete/
%{_bindir}/activate-global-python-argcomplete
%{_bindir}/python-argcomplete-check-easy-install-script
%{_bindir}/python-argcomplete-tcsh
%{_bindir}/register-python-argcomplete
%{_sysconfdir}/bash_completion.d/%{name}

%changelog
* Mon Jun 05 2023 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-8
- Move the Bash completion files to /etc/bash_completion.d to fix rhbz#2211862

* Mon May 22 2023 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-7
- Fix build with pip 23.1.2+
- Fixes: rhbz#2209020

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 12 2022 Todd Zullinger <tmz@pobox.com> - 2.0.0-5
- Install bash-completion in default location

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 2.0.0-1
- Update to 2.0.0
- Fixes: rhbz#2036728
- Fixes: rhbz#2034200

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 1.12.3-2
- Rebuilt for Python 3.10

* Thu Apr 29 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.12.3-1
- Update to 1.12.3
- Resolves: rhbz#1951096

* Wed Feb 17 2021 Lumír Balhar <lbalhar@redhat.com> - 1.12.2-1
- Update to 1.12.2
Resolves: rhbz#1882968

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-1
- Update to 1.12.0
- Fixes rhbz#1856103

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-1
- Update to 1.11.1 (#1709038)
- Fix tests with Fish 3.1 (#1808322)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-2
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.10.0-1
- Update to 1.10.0
- Adjust source0 to point to pypi

* Tue Apr 02 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.5-1
- Update to 1.9.5

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.4-1
- Update to 1.9.4
- Drop python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.3-3
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 19 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.3-1
- Update to 1.9.3

* Wed Nov 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.2-1
- Update to 1.9.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Thu Jan 26 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Sat Jan 07 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.7.0-1
- Update to 1.7.0 (RHBZ #1339845)

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.1.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Mar 27 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.1-1
- Update to 1.1.1 (RHBZ #1320348)

* Mon Feb 22 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.0-1
- Update to 1.1.0 (RHBZ #1310473)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-3
- Ship bash completion file within RPM

* Sat Nov 14 2015 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.0-2
- A few minor changes to simplify and take care of cornercases

* Sat Nov 14 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@laptop> - 1.0.0-1
- Update to latest version (#1227119)
- Use %%license
- Update to new python packaging style
- Remove 2to3 invocation, the code is already python3 compatible
- Move scripts to python3 subpackage
- Add Provides:/usr/bin/register-python-activate so packages can depend on it

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 0.8.9-4
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 2 2015 - Steve Traylen <steve.traylen@cern.ch> 0.8.8-2
- Add python3 package (#1225934)

* Tue Jun 02 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.8.9-1
- Update to 0.8.9 (#1227119)

* Tue May 5 2015 - Steve Traylen <steve.traylen@cern.ch> 0.8.8-1
- Updating package to 0.8.8

* Sun Dec 14 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.8.4-1
- Updating package to 0.8.4

* Fri Sep 12 2014 - Steve Traylen <steve.traylen@cern.ch> 0.8.1-1
- Updating package to 0.8.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.8.0-1
- Updating package to 0.8.0

* Sun Mar 30 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.7.1-1
- Updating package to 0.7.1

* Mon Mar 24 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.7.0-1
- Updating package to 0.7.0

* Mon Jan 13 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.6.7-2
- Removing '%%exclude %%{python_sitelib}/test' fom %%files as no longer needed.

* Mon Jan 13 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.6.7-1
- Applying latest patch of argcomplete.

* Wed Jan 8 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.6.3-4
- Pushing new build for update as previous was not picked up.

* Wed Oct 16 2013 - Dale Macartney <dbmacartney@gmail.com> 0.6.3-3
- Correct missing files for el6

* Tue Oct 15 2013 - Dale Macartney <dbmacartney@gmail.com> 0.6.3-2
- Initial packaging for Fedora Project and including LICENSE.rst in docs

* Thu Jan 31 2013 - Marco Neciarini <marco.nenciarini@2ndquadrant.it> 0.3.5-1
- Initial packaging.
