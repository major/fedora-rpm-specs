# disable in source builds on EPEL <9
%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

# python2 is not available on RHEL > 7 and Fedora
%if 0%{?rhel} > 7 || 0%{?fedora}
%bcond_with python2
%else
%bcond_without python2
%endif

# build csdiff-static on 64bit RHEL-10+ and Fedora
%if 0%{?__isa_bits} == 64 && (0%{?rhel} > 9 || 0%{?fedora})
%bcond_without static
%else
%bcond_with static
%endif

# python3 support is optional
%bcond_without python3

Name:       csdiff
Version:    3.5.3
Release:    1%{?dist}
Summary:    Non-interactive tools for processing code scan results in plain-text

License:    GPL-3.0-or-later
URL:        https://github.com/csutils/csdiff
Source0:    https://github.com/csutils/csdiff/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:    https://github.com/csutils/csdiff/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc
# gpg --keyserver pgp.mit.edu --recv-key 992A96E075056E79CD8214F9873DB37572A37B36
# gpg --output kdudka.pgp --armor --export kdudka@redhat.com
Source2:    kdudka.pgp

# the following upstream commit is needed to work with up2date csdiff/csgrep
# https://github.com/csutils/csmock/commit/48b09b3a
Conflicts:  csmock-plugin-shellcheck <= 2.5

# Use Boost 1.69 on EPEL 7
%if 0%{?rhel} == 7
BuildRequires: boost169-devel
%endif
# Use Boost 1.78 on EPEL 8 and 9
%if 0%{?rhel} == 8 || 0%{?rhel} == 9
BuildRequires: boost1.78-devel
%endif
# Use boost-devel everywhere else
%if 0%{?rhel} > 9 || 0%{?fedora}
BuildRequires: boost-devel
%endif

BuildRequires: cmake3
BuildRequires: gcc-c++
BuildRequires: gnupg2
BuildRequires: help2man
BuildRequires: make

%if 0%{?rhel} == 7
Provides: bundled(boost_json)
Provides: bundled(boost_nowide)
%else
# needed for csfilter-kfp --kfp-git-url
Recommends: git-core
%endif

%description
This package contains the csdiff tool for comparing code scan defect lists in
order to find out added or fixed defects, and the csgrep utility for filtering
defect lists using various filtering predicates.

%if %{with static}
%package static
Summary:        Statically linked csgrep-static executable
BuildRequires:  boost-static
BuildRequires:  glibc-static
BuildRequires:  libstdc++-static

%description static
This pacakge contains a statically linked csgrep-static executable needed
for context embedding in legacy build environments.
%endif

%if %{with python2}
%package -n python2-%{name}
Summary:        Python interface to csdiff for Python 2
BuildRequires:  python2-devel
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
This package contains the Python 2 binding for the csdiff tool for comparing
code scan defect lists to find out added or fixed defects.
%endif

%if %{with python3}
%package -n python3-%{name}
Summary:        Python interface to csdiff for Python 3
BuildRequires:  python3-devel
%if 0%{?rhel} == 7
# fallback for epel7 buildroots with outdated RPM macros
%{?python_provide:%python_provide python3-%{name}}
%else
%py_provides    python3-%{name}
%endif

%description -n python3-%{name}
This package contains the Python 3 binding for the csdiff tool for comparing
code scan defect lists to find out added or fixed defects.
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%if 0%{?rhel} == 7
# Set paths for CMake's FindBoost
export BOOST_INCLUDEDIR=/usr/include/boost169
export BOOST_LIBRARYDIR=/usr/lib64/boost169
%endif

make version.cc
%cmake3                                    \
    -DCSGREP_STATIC=%{?with_static:ON}     \
    -DPYCSDIFF_PYTHON2=%{?with_python2:ON} \
    -DPYCSDIFF_PYTHON3=%{?with_python3:ON} \
    -DVERSION='%{name}-%{version}-%{release}'
%cmake3_build

%install
%cmake3_install

%check
%ctest3

%files
%doc README
%license COPYING
%{_bindir}/csdiff
%{_bindir}/csfilter-kfp
%{_bindir}/csgrep
%{_bindir}/cshtml
%{_bindir}/cslinker
%{_bindir}/cssort
%{_bindir}/cstrans-df-run
%{_datadir}/%{name}
%{_mandir}/man1/csdiff.1*
%{_mandir}/man1/csfilter-kfp.1*
%{_mandir}/man1/csgrep.1*
%{_mandir}/man1/cshtml.1*
%{_mandir}/man1/cslinker.1*
%{_mandir}/man1/cssort.1*
%{_mandir}/man1/cstrans-df-run.1*

%if %{with static}
%files static
%{_libexecdir}/csgrep-static
%endif

%if %{with python2}
%files -n python2-%{name}
%license COPYING
%{python2_sitearch}/pycsdiff.so
%endif

%if %{with python3}
%files -n python3-%{name}
%license COPYING
%{python3_sitearch}/pycsdiff.so
%endif

%changelog
* Fri Feb 07 2025 Kamil Dudka <kdudka@redhat.com> - 3.5.3-1
- update to latest upstream release

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Kamil Dudka <kdudka@redhat.com> - 3.5.2-1
- update to latest upstream release

* Wed Sep 25 2024 Kamil Dudka <kdudka@redhat.com> - 3.5.1-1
- update to latest upstream release

* Fri Sep 06 2024 Kamil Dudka <kdudka@redhat.com> - 3.5.0-1
- csfilter-kfp: a new tool to filter known false positives
- update to latest upstream release

* Fri Aug 02 2024 Kamil Dudka <kdudka@redhat.com> - 3.4.1-1
- introduce the csdiff-static subpackage with the csgrep-static executable
- update to latest upstream release

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Kamil Dudka <kdudka@redhat.com> 3.4.0-1
- update to latest upstream release

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.13

* Fri May 03 2024 Kamil Dudka <kdudka@redhat.com> 3.3.0-1
- update to latest upstream release

* Thu Apr 25 2024 Kamil Dudka <kdudka@redhat.com> 3.2.2-1
- update to latest upstream release

* Thu Feb 29 2024 Kamil Dudka <kdudka@redhat.com> 3.2.1-1
- update to latest upstream release

* Wed Jan 24 2024 Kamil Dudka <kdudka@redhat.com> 3.2.0-1
- update to latest upstream release

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 3.1.0-2
- Rebuilt for Boost 1.83

* Tue Oct 10 2023 Kamil Dudka <kdudka@redhat.com> 3.1.0-1
- update to latest upstream release

* Mon Aug 21 2023 Kamil Dudka <kdudka@redhat.com> 3.0.4-1
- update to latest upstream release

* Fri Jul 21 2023 Kamil Dudka <kdudka@redhat.com> 3.0.3-1
- update to latest upstream release

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.0.2-2
- Rebuilt for Python 3.12

* Fri Apr 21 2023 Kamil Dudka <kdudka@redhat.com> 3.0.2-1
- update to latest upstream release

* Thu Apr 06 2023 Kamil Dudka <kdudka@redhat.com> 3.0.1-1
- migrate to SPDX license
- update to latest upstream

* Fri Mar 10 2023 Kamil Dudka <kdudka@redhat.com> 3.0.0-1
- update to latest upstream release

* Thu Feb 23 2023 Lukáš Zaoral <lzaoral@redhat.com> - 2.9.0-2
- Rebuilt for Boost 1.81 (rhbz#2172687)

* Wed Feb 22 2023 Kamil Dudka <kdudka@redhat.com> 2.9.0-1
- update to latest upstream release

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2.8.0-3
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Kamil Dudka <kdudka@redhat.com> 2.8.0-1
- update to latest upstream release

* Tue Sep 06 2022 Kamil Dudka <kdudka@redhat.com> 2.7.0-1
- update to latest upstream release

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Kamil Dudka <kdudka@redhat.com> 2.6.0-2
- remove obsolete boost-python3-devel build dependency (#2100748)

* Tue Jun 21 2022 Kamil Dudka <kdudka@redhat.com> 2.6.0-1
- update to latest upstream release

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.5.0-2
- Rebuilt for Python 3.11

* Mon May 09 2022 Kamil Dudka <kdudka@redhat.com> 2.5.0-1
- update to latest upstream release

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2.4.0-2
- Rebuilt for Boost 1.78

* Wed Apr 13 2022 Kamil Dudka <kdudka@redhat.com> 2.4.0-1
- update to latest upstream release

* Tue Mar 15 2022 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-2
- Verify GPG signature of upstream tarball when building the package

* Tue Mar 15 2022 Kamil Dudka <kdudka@redhat.com> 2.3.0-1
- update to latest upstream release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Kamil Dudka <kdudka@redhat.com> 2.2.0-1
- update to latest upstream release

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 2.1.1-4
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.1-2
- Rebuilt for Python 3.10

* Fri May 21 2021 Kamil Dudka <kdudka@redhat.com> 2.1.1-1
- update to latest upstream release

* Wed Feb 17 2021 Kamil Dudka <kdudka@redhat.com> 2.1.0-1
- update to latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2.0.0-2
- Rebuilt for Boost 1.75

* Fri Jan 08 2021 Kamil Dudka <kdudka@redhat.com> 2.0.0-1
- update to latest upstream release

* Tue Oct 20 2020 Kamil Dudka <kdudka@redhat.com> 1.9.0-1
- update to latest upstream release

* Wed Aug 19 2020 Kamil Dudka <kdudka@redhat.com> 1.8.0-1
- update to latest upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 1.7.2-3
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-2
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Kamil Dudka <kdudka@redhat.com> 1.7.2-1
- update to latest upstream release

* Tue Mar 31 2020 Kamil Dudka <kdudka@redhat.com> 1.7.1-1
- update to latest upstream release

* Wed Feb 05 2020 Kamil Dudka <kdudka@redhat.com> 1.7.0-1
- update to latest upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Kamil Dudka <kdudka@redhat.com> 1.6.1-1
- make pycsdiff build with Python 3.8 (#1705427)
- update to latest upstream release

* Mon Feb 04 2019 Kamil Dudka <kdudka@redhat.com> 1.6.0-1
- update to latest upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 1.5.0-2
- Rebuilt and patched for Boost 1.69

* Thu Oct 18 2018 Kamil Dudka <kdudka@redhat.com> 1.5.0-1
- update to latest upstream release

* Mon Oct 01 2018 Kamil Dudka <kdudka@redhat.com> 1.4.0-5
- rebuild without the python2-csdiff subpackage (#1634690)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.7

* Thu May 03 2018 Kamil Dudka <kdudka@redhat.com> 1.4.0-1
- update to latest upstream release
- make both python2 and python3 optional

* Mon Feb 19 2018 Kamil Dudka <kdudka@redhat.com> 1.3.3-4
- add explicit BR for the gcc-c++ compiler

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Kamil Dudka <kdudka@redhat.com> 1.3.3-2
- rebuild for Boost 1.66

* Mon Jan 15 2018 Kamil Dudka <kdudka@redhat.com> 1.3.3-1
- update to latest upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.2-2
- Rebuilt for Boost 1.64

* Wed Feb 15 2017 Kamil Dudka <kdudka@redhat.com> 1.3.2-1
- update to latest upstream release
- update project URL and source URL

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-4
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-3
- Rebuilt for Boost 1.63

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuild for Python 3.6

* Wed Sep 14 2016 Kamil Dudka <kdudka@redhat.com> 1.3.1-1
- update to latest upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 20 2016 Kamil Dudka <kdudka@redhat.com> 1.3.0-1
- update to latest upstream release
- introduce the python2- and python3- subpackages

* Fri May 13 2016 Kamil Dudka <kdudka@redhat.com> 1.2.3-8
- rebuild against latest boost libs to fix linking errors at run time (#1331983)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.2.3-6
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.2.3-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.2.3-3
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Kamil Dudka <kdudka@redhat.com> 1.2.3-1
- update to latest upstream release

* Tue Apr 14 2015 Kamil Dudka <kdudka@redhat.com> 1.2.2-2
- rebuild against latest boost (missing symbol _ZN5boost15program_options3argE)

* Wed Apr 01 2015 Kamil Dudka <kdudka@redhat.com> 1.2.2-1
- update to latest upstream release

* Tue Mar 03 2015 Kamil Dudka <kdudka@redhat.com> 1.2.1-1
- update to latest upstream release

* Wed Feb 18 2015 Kamil Dudka <kdudka@redhat.com> 1.2.0-1
- update to latest upstream release

* Thu Feb 05 2015 Kamil Dudka <kdudka@redhat.com> 1.1.4-2
- rebuild for boost 1.57.0

* Wed Jan 28 2015 Kamil Dudka <kdudka@redhat.com> 1.1.4-1
- update to latest upstream release

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.1.3-2
- Rebuild for boost 1.57.0

* Mon Jan 19 2015 Kamil Dudka <kdudka@redhat.com> 1.1.3-1
- update to latest upstream

* Thu Dec 18 2014 Kamil Dudka <kdudka@redhat.com> 1.1.2-1
- update to latest upstream release
- package the pycsdiff python module

* Thu Nov 06 2014 Kamil Dudka <kdudka@redhat.com> 1.1.1-1
- update to latest upstream release

* Fri Sep 19 2014 Kamil Dudka <kdudka@redhat.com> 1.1.0-1
- update to latest upstream release

* Wed Aug 20 2014 Kamil Dudka <kdudka@redhat.com> 1.0.10-1
- update to latest upstream bugfix release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Kamil Dudka <kdudka@redhat.com> 1.0.9-1
- update to latest upstream bugfix release

* Thu Jul 17 2014 Kamil Dudka <kdudka@redhat.com> 1.0.8-1
- update to latest upstream bugfix release

* Thu Jun 19 2014 Kamil Dudka <kdudka@redhat.com> 1.0.6-1
- update to latest upstream bugfix release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.0.4-2
- Rebuild for boost 1.55.0

* Mon Mar 17 2014 Kamil Dudka <kdudka@redhat.com> 1.0.4-1
- update to latest upstream

* Thu Feb 20 2014 Kamil Dudka <kdudka@redhat.com> 1.0.2-2
- abandon RHEL-5 compatibility per Fedora Review Request (#1066027)

* Wed Feb 19 2014 Kamil Dudka <kdudka@redhat.com> 1.0.2-1
- packaged for Fedora
