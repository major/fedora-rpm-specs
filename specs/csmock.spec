# disable in source builds on EPEL <9
%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

Name:       csmock
Version:    3.8.0
Release:    2%{?dist}
Summary:    A mock wrapper for Static Analysis tools

License:    GPL-3.0-or-later
URL:        https://github.com/csutils/%{name}
Source0:    https://github.com/csutils/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:    https://github.com/csutils/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc

# gpg --keyserver pgp.mit.edu --recv-key 992A96E075056E79CD8214F9873DB37572A37B36
# gpg --output kdudka.pgp --armor --export kdudka@redhat.com
Source2:    kdudka.pgp

BuildRequires: cmake3
BuildRequires: gnupg2
BuildRequires: help2man

%if 0%{?rhel} == 7
%global python3_pkgversion 36
%global __python %{python3}
%endif

BuildRequires: python%{python3_pkgversion}-GitPython
BuildRequires: python%{python3_pkgversion}-devel

Requires: csmock-common                 >= %{version}-%{release}
Requires: csmock-plugin-clang           >= %{version}-%{release}
Requires: csmock-plugin-cppcheck        >= %{version}-%{release}
Requires: csmock-plugin-gitleaks        >= %{version}-%{release}
Requires: csmock-plugin-shellcheck      >= %{version}-%{release}

BuildArch: noarch

%description
This is a metapackage pulling in csmock-common and basic csmock plug-ins.

%package -n csbuild
Summary: Tool for plugging static analyzers into the build process
Requires: cscppc
Requires: csclng
Requires: csdiff
Requires: csmock-common
Requires: cswrap
Requires: python%{python3_pkgversion}-GitPython

%description -n csbuild
Tool for plugging static analyzers into the build process, free of mock.

%package common
Summary: Core of csmock (a mock wrapper for Static Analysis tools)
Requires: csdiff > 3.5.1
Requires: csgcca
Requires: cswrap
Requires: mock >= 5.7
Requires: tar
Requires: xz
%if 0%{?rhel} != 7
Recommends: modulemd-tools
%endif

%description common
This package contains the csmock tool that allows to scan SRPMs by Static
Analysis tools in a fully automated way.

%package plugin-bandit
Summary: csmock plug-in providing the support for Bandit.
Requires: csmock-common

%description plugin-bandit
This package contains the bandit plug-in for csmock.

%package plugin-cbmc
Summary: csmock plug-in providing the support for cbmc
Requires: csexec
Requires: csmock-common

%description plugin-cbmc
This package contains the cbmc plug-in for csmock.

%package plugin-clang
Summary: csmock plug-in providing the support for Clang
Requires: csclng
Requires: csmock-common

%description plugin-clang
This package contains the clang plug-in for csmock.

%package plugin-clippy
Summary: csmock plug-in providing the support for Rust Clippy.
Requires: csmock-common

%description plugin-clippy
This package contains the Rust Clippy plug-in for csmock.

%package plugin-cppcheck
Summary: csmock plug-in providing the support for Cppcheck
Requires: cscppc
Requires: csmock-common

%description plugin-cppcheck
This package contains the cppcheck plug-in for csmock.

%package plugin-divine
Summary: csmock plug-in providing the support for divine
Requires: csexec
Requires: csmock-common

%description plugin-divine
This package contains the divine plug-in for csmock.

%package plugin-gitleaks
Summary: experimental csmock plug-in
Requires: csmock-common

%description plugin-gitleaks
This package contains the gitleaks plug-in for csmock.

%package plugin-infer
Summary: csmock plug-in providing the support for Infer
Requires: csmock-common

%description plugin-infer
This package contains the Infer plug-in for csmock.

%package plugin-pylint
Summary: csmock plug-in providing the support for Pylint.
Requires: csmock-common

%description plugin-pylint
This package contains the pylint plug-in for csmock.

%package plugin-semgrep
Summary: csmock plug-in providing the support for semgrep scan
Requires: csmock-common

%description plugin-semgrep
This package contains the semgrep plug-in for csmock.

%package plugin-shellcheck
Summary: csmock plug-in providing the support for ShellCheck.
Requires: csmock-common
Requires: csmock-plugin-shellcheck-core

%description plugin-shellcheck
This package contains the shellcheck plug-in for csmock.

%package plugin-shellcheck-core
Conflicts: csmock-plugin-shellcheck < %{version}-%{release}
Summary: script to run shellcheck on a directory tree
%if 0%{?rhel} != 7
Recommends: ShellCheck
%endif

%description plugin-shellcheck-core
This package contains the run-shellcheck.sh script to run shellcheck on a directory tree.

%package plugin-smatch
Summary: csmock plug-in providing the support for smatch
Requires: csmatch
Requires: csmock-common
Requires: cswrap

%description plugin-smatch
This package contains the smatch plug-in for csmock.

%package plugin-snyk
Summary: csmock plug-in providing the support for snyk
Requires: csmock-common

%description plugin-snyk
This package contains the snyk plug-in for csmock.

%package plugin-strace
Summary: csmock plug-in providing the support for strace
Requires: csexec
Requires: csmock-common

%description plugin-strace
This package contains the strace plug-in for csmock.

%package plugin-symbiotic
Summary: csmock plug-in providing the support for symbiotic
Requires: csexec
Requires: csmock-common

%description plugin-symbiotic
This package contains the symbiotic plug-in for csmock.

%package plugin-valgrind
Summary: csmock plug-in providing the support for valgrind
Requires: csexec
Requires: csmock-common

%description plugin-valgrind
This package contains the valgrind plug-in for csmock.

%package plugin-unicontrol
Summary: experimental csmock plug-in
Requires: csmock-common

%description plugin-unicontrol
This package contains the unicontrol plug-in for csmock.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake3                                       \
    -DVERSION='%{name}-%{version}-%{release}' \
    -DPython3_EXECUTABLE='%{__python3}'
%cmake3_build

%install
%cmake3_install

# needed to create the csmock RPM
%files

%files -n csbuild
%license COPYING
%{_bindir}/csbuild
%{_mandir}/man1/csbuild.1*
%{_datadir}/csbuild/scripts/run-scan.sh

%files common
%license COPYING
%doc README
%dir %{_datadir}/csmock
%dir %{_datadir}/csmock/scripts
%dir %{python3_sitelib}/csmock
%dir %{python3_sitelib}/csmock/plugins
%{_bindir}/csmock
%{_mandir}/man1/csmock.1*
%{_datadir}/csmock/cwe-map.csv
%{_datadir}/csmock/scripts/enable-keep-going.sh
%attr(755,root,root) %{_datadir}/csmock/scripts/chroot-fixups
%{_datadir}/csmock/scripts/patch-rawbuild.sh
%{python3_sitelib}/csmock/__init__.py*
%{python3_sitelib}/csmock/common
%{python3_sitelib}/csmock/plugins/__init__.py*
%{python3_sitelib}/csmock/plugins/gcc.py*
%{python3_sitelib}/csmock/__pycache__/__init__.*
%{python3_sitelib}/csmock/plugins/__pycache__/__init__.*
%{python3_sitelib}/csmock/plugins/__pycache__/gcc.*

%files plugin-bandit
%{_datadir}/csmock/scripts/run-bandit.sh
%{python3_sitelib}/csmock/plugins/bandit.py*
%{python3_sitelib}/csmock/plugins/__pycache__/bandit.*

%files plugin-cbmc
%{python3_sitelib}/csmock/plugins/cbmc.py*
%{python3_sitelib}/csmock/plugins/__pycache__/cbmc.*

%files plugin-clang
%{python3_sitelib}/csmock/plugins/clang.py*
%{python3_sitelib}/csmock/plugins/__pycache__/clang.*

%files plugin-clippy
%{_datadir}/csmock/scripts/convert-clippy.py*
%if 0%{?rhel} == 7
%{_datadir}/csmock/scripts/__pycache__/convert-clippy.*
%endif
%{_datadir}/csmock/scripts/inject-clippy.sh
%{python3_sitelib}/csmock/plugins/clippy.py*
%{python3_sitelib}/csmock/plugins/__pycache__/clippy.*

%files plugin-cppcheck
%{python3_sitelib}/csmock/plugins/cppcheck.py*
%{python3_sitelib}/csmock/plugins/__pycache__/cppcheck.*

%files plugin-divine
%{python3_sitelib}/csmock/plugins/divine.py*
%{python3_sitelib}/csmock/plugins/__pycache__/divine.*

%files plugin-gitleaks
%{python3_sitelib}/csmock/plugins/gitleaks.py*
%{python3_sitelib}/csmock/plugins/__pycache__/gitleaks.*

%files plugin-infer
%{_datadir}/csmock/scripts/filter-infer.py*
%if 0%{?rhel} == 7
%{_datadir}/csmock/scripts/__pycache__/filter-infer.*
%endif
%{_datadir}/csmock/scripts/install-infer.sh
%{python3_sitelib}/csmock/plugins/infer.py*
%{python3_sitelib}/csmock/plugins/__pycache__/infer.*

%files plugin-pylint
%{_datadir}/csmock/scripts/run-pylint.sh
%{python3_sitelib}/csmock/plugins/pylint.py*
%{python3_sitelib}/csmock/plugins/__pycache__/pylint.*

%files plugin-semgrep
%{python3_sitelib}/csmock/plugins/semgrep.py*
%{python3_sitelib}/csmock/plugins/__pycache__/semgrep.*

%files plugin-shellcheck
%{python3_sitelib}/csmock/plugins/shellcheck.py*
%{python3_sitelib}/csmock/plugins/__pycache__/shellcheck.*

%files plugin-shellcheck-core
%license COPYING
%dir %{_datadir}/csmock
%dir %{_datadir}/csmock/scripts
%{_datadir}/csmock/scripts/run-shellcheck.sh

%files plugin-smatch
%{python3_sitelib}/csmock/plugins/smatch.py*
%{python3_sitelib}/csmock/plugins/__pycache__/smatch.*

%files plugin-snyk
%{python3_sitelib}/csmock/plugins/snyk.py*
%{python3_sitelib}/csmock/plugins/__pycache__/snyk.*

%files plugin-strace
%{python3_sitelib}/csmock/plugins/strace.py*
%{python3_sitelib}/csmock/plugins/__pycache__/strace.*

%files plugin-symbiotic
%{python3_sitelib}/csmock/plugins/symbiotic.py*
%{python3_sitelib}/csmock/plugins/__pycache__/symbiotic.*

%files plugin-valgrind
%{python3_sitelib}/csmock/plugins/valgrind.py*
%{python3_sitelib}/csmock/plugins/__pycache__/valgrind.*

%files plugin-unicontrol
%{_datadir}/csmock/scripts/find-unicode-control.py*
%if 0%{?rhel} == 7
%{_datadir}/csmock/scripts/__pycache__/find-unicode-control.*
%endif
%{python3_sitelib}/csmock/plugins/unicontrol.py*
%{python3_sitelib}/csmock/plugins/__pycache__/unicontrol.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Kamil Dudka <kdudka@redhat.com> - 3.8.0-1
- update to latest upstream

* Wed Sep 25 2024 Kamil Dudka <kdudka@redhat.com> - 3.7.1-1
- update to latest upstream

* Fri Sep 06 2024 Kamil Dudka <kdudka@redhat.com> - 3.7.0-1
- update to latest upstream

* Fri Aug 02 2024 Kamil Dudka <kdudka@redhat.com> - 3.6.1-1
- update to latest upstream

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Kamil Dudka <kdudka@redhat.com> 3.6.0-1
- update to latest upstream (introduces plug-ins for clippy and semgrep)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.5.3-2
- Rebuilt for Python 3.13

* Wed Mar 20 2024 Kamil Dudka <kdudka@redhat.com> 3.5.3-1
- update to latest upstream (fixes CVE-2024-2243)

* Thu Feb 29 2024 Kamil Dudka <kdudka@redhat.com> 3.5.2-1
- update to latest upstream

* Wed Jan 24 2024 Kamil Dudka <kdudka@redhat.com> 3.5.1-1
- update to latest upstream

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 10 2023 Kamil Dudka <kdudka@redhat.com> 3.5.0-1
- update to latest upstream

* Fri Jul 21 2023 Kamil Dudka <kdudka@redhat.com> 3.4.2-1
- update to latest upstream

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.4.1-2
- Rebuilt for Python 3.12

* Thu Apr 06 2023 Kamil Dudka <kdudka@redhat.com> 3.4.1-1
- update to latest upstream

* Wed Feb 22 2023 Kamil Dudka <kdudka@redhat.com> 3.4.0-1
- migrate to SPDX license
- update to latest upstream release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Kamil Dudka <kdudka@redhat.com> 3.3.5-1
- update to latest upstream release

* Tue Sep 06 2022 Kamil Dudka <kdudka@redhat.com> 3.3.4-1
- update to latest upstream release

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Kamil Dudka <kdudka@redhat.com> 3.3.3-1
- update to latest upstream release

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3.2-2
- Rebuilt for Python 3.11

* Mon May 09 2022 Kamil Dudka <kdudka@redhat.com> 3.3.2-1
- update to latest upstream release

* Tue Mar 15 2022 Kamil Dudka <kdudka@redhat.com> 3.3.1-2
- verify GPG signature of upstream tarball when building the package

* Tue Mar 15 2022 Kamil Dudka <kdudka@redhat.com> 3.3.1-1
- update to latest upstream release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 16 2021 Kamil Dudka <kdudka@redhat.com> 3.3.0-1
- update to latest upstream release

* Tue Nov 30 2021 Kamil Dudka <kdudka@redhat.com> 3.2.0-1
- update to latest upstream release

* Thu Nov 11 2021 Kamil Dudka <kdudka@redhat.com> 3.1.0-1
- update to latest upstream release

* Mon Oct 04 2021 Kamil Dudka <kdudka@redhat.com> 3.0.0-1
- update to latest upstream release

* Tue Aug 31 2021 Kamil Dudka <kdudka@redhat.com> 2.9.0-1
- update to latest upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.8.0-2
- Rebuilt for Python 3.10

* Fri May 21 2021 Kamil Dudka <kdudka@redhat.com> 2.8.0-1
- update to latest upstream release

* Wed Feb 17 2021 Kamil Dudka <kdudka@redhat.com> 2.7.1-1
- update to latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Kamil Dudka <kdudka@redhat.com> 2.7.0-1
- update to latest upstream release

* Tue Oct 20 2020 Kamil Dudka <kdudka@redhat.com> 2.6.0-1
- update to latest upstream release

* Wed Aug 19 2020 Kamil Dudka <kdudka@redhat.com> 2.5.0-1
- update to latest upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.9

* Wed Feb 05 2020 Kamil Dudka <kdudka@redhat.com> 2.4.0-1
- update to latest upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Kamil Dudka <kdudka@redhat.com> 2.3.0-1
- update to latest upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Kamil Dudka <kdudka@redhat.com> 2.2.1-1
- update to latest upstream release

* Thu Oct 18 2018 Kamil Dudka <kdudka@redhat.com> 2.2.0-1
- update to latest upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-2
- Rebuilt for Python 3.7

* Thu May 03 2018 Kamil Dudka <kdudka@redhat.com> 2.1.1-1
- update to latest upstream release
- introduce the experimental bandit plug-in

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Kamil Dudka <kdudka@redhat.com> 2.1.0-1
- update to latest upstream release

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.4-3
- Build require Python 2 only when needed

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kamil Dudka <kdudka@redhat.com> 2.0.4-1
- update to latest upstream release

* Wed Feb 15 2017 Kamil Dudka <kdudka@redhat.com> 2.0.3-1
- update to latest upstream release
- update project URL and source URL

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-2
- Rebuild for Python 3.6

* Wed Nov 30 2016 Kamil Dudka <kdudka@redhat.com> 2.0.2-1
- update to latest upstream

* Wed Sep 14 2016 Kamil Dudka <kdudka@redhat.com> 2.0.1-1
- update to latest upstream

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 20 2016 Kamil Dudka <kdudka@redhat.com> 2.0.0-1
- update to latest upstream
- force using Python 3

* Thu Apr 28 2016 Kamil Dudka <kdudka@redhat.com> 1.9.2-1
- update to latest upstream

* Mon Mar 21 2016 Kamil Dudka <kdudka@redhat.com> 1.9.1-1
- update to latest upstream

* Wed Feb 03 2016 Kamil Dudka <kdudka@redhat.com> 1.9.0-1
- update to latest upstream

* Thu Jul 23 2015 Kamil Dudka <kdudka@redhat.com> 1.8.3-1
- update to latest upstream

* Mon Jul 13 2015 Kamil Dudka <kdudka@redhat.com> 1.8.2-1
- update to latest upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Kamil Dudka <kdudka@redhat.com> 1.8.1-1
- update to latest upstream

* Wed Apr 01 2015 Kamil Dudka <kdudka@redhat.com> 1.8.0-1
- update to latest upstream

* Tue Mar 03 2015 Kamil Dudka <kdudka@redhat.com> 1.7.2-1
- update to latest upstream

* Wed Feb 25 2015 Kamil Dudka <kdudka@redhat.com> 1.7.1-1
- update to latest upstream

* Wed Feb 18 2015 Kamil Dudka <kdudka@redhat.com> 1.7.0-1
- update to latest upstream

* Mon Jan 19 2015 Kamil Dudka <kdudka@redhat.com> 1.6.1-1
- update to latest upstream

* Wed Dec 17 2014 Kamil Dudka <kdudka@redhat.com> 1.6.0-1
- update to latest upstream (introduces the csbuild subpackage)

* Thu Dec 11 2014 Michael Scherer <misc@zarb.org> 1.5.1-2
- fix the description of the csmock-plugin-shellcheck subpackage (#1173134)

* Thu Nov 06 2014 Kamil Dudka <kdudka@redhat.com> 1.5.1-1
- update to latest upstream

* Fri Sep 19 2014 Kamil Dudka <kdudka@redhat.com> 1.5.0-1
- update to latest upstream

* Fri Sep 05 2014 Kamil Dudka <kdudka@redhat.com> 1.4.1-1
- update to latest upstream

* Wed Sep 03 2014 Kamil Dudka <kdudka@redhat.com> 1.4.0-1
- update to latest upstream

* Wed Aug 20 2014 Kamil Dudka <kdudka@redhat.com> 1.3.2-1
- update to latest upstream

* Fri Aug 01 2014 Kamil Dudka <kdudka@redhat.com> 1.3.1-1
- update to latest upstream
- install plug-ins to %%{python2_sitelib} instead of %%{python_sitearch}

* Thu Jul 17 2014 Kamil Dudka <kdudka@redhat.com> 1.2.3-1
- update to latest upstream

* Fri Jul 04 2014 Kamil Dudka <kdudka@redhat.com> 1.2.2-1
- update to latest upstream

* Thu Jun 19 2014 Kamil Dudka <kdudka@redhat.com> 1.1.1-1
- update to latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Kamil Dudka <kdudka@redhat.com> 1.0.7-1
- update to latest upstream

* Tue Feb 25 2014 Kamil Dudka <kdudka@redhat.com> 1.0.3-2
- further spec file improvements per Fedora Review Request (#1066029)

* Mon Feb 24 2014 Kamil Dudka <kdudka@redhat.com> 1.0.3-1
- update to new upstream release
- abandon RHEL-5 compatibility per Fedora Review Request (#1066029)

* Wed Feb 19 2014 Kamil Dudka <kdudka@redhat.com> 1.0.2-1
- packaged for Fedora
