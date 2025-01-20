%global srcname whisper
%global sum Whisper is a file-based time-series database format for Graphite


Name:           python-whisper
Version:        1.1.10
Release:        7%{?dist}
Summary:        %{sum}

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/graphite-project/whisper

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source10:       rrd2whisper.1
Source11:       whisper-create.1
Source12:       whisper-dump.1
Source13:       whisper-fetch.1
Source14:       whisper-info.1
Source15:       whisper-merge.1
Source16:       whisper-resize.1
Source17:       whisper-set-aggregation-method.1
Source18:       whisper-update.1
Source19:       whisper-fill.1

Patch0:         python-whisper-1.1.10-whisper-resize-test-fix.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
Whisper is a fixed-size database, similar in design and purpose to RRD
(round-robin-database). It provides fast, reliable storage of numeric
data over time. Whisper allows for higher resolution (seconds per point)
of recent data to degrade into lower resolutions for long-term retention
of historical data.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
Python%{python3_pkgversion} version of the Graphite whisper module


%prep
%autosetup -p1 -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}

# remove .py suffix
for i in %{buildroot}%{_bindir}/*.py; do
    mv ${i} ${i%%.py}
done

# man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE10} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE11} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE12} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE13} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE14} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE15} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE16} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE17} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE18} %{buildroot}%{_mandir}/man1
install -D -p -m0644 %{SOURCE19} %{buildroot}%{_mandir}/man1


%check
%{__python3} test_whisper.py


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/find-corrupt-whisper-files
%{_bindir}/rrd2whisper
%{_bindir}/update-storage-times
%{_bindir}/whisper-auto-resize
%{_bindir}/whisper-auto-update
%{_bindir}/whisper-create
%{_bindir}/whisper-dump
%{_bindir}/whisper-diff
%{_bindir}/whisper-fetch
%{_bindir}/whisper-fill
%{_bindir}/whisper-info
%{_bindir}/whisper-merge
%{_bindir}/whisper-resize
%{_bindir}/whisper-set-aggregation-method
%{_bindir}/whisper-set-xfilesfactor
%{_bindir}/whisper-update
%{_mandir}/man1/rrd2whisper.1*
%{_mandir}/man1/whisper-create.1*
%{_mandir}/man1/whisper-dump.1*
%{_mandir}/man1/whisper-fetch.1*
%{_mandir}/man1/whisper-fill.1*
%{_mandir}/man1/whisper-info.1*
%{_mandir}/man1/whisper-merge.1*
%{_mandir}/man1/whisper-resize.1*
%{_mandir}/man1/whisper-set-aggregation-method.1*
%{_mandir}/man1/whisper-update.1*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.10-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.10-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 07 2023 Jonathan Steffan <jsteffan@fedoraproject.org> - 1.1.10-1
- Update to 1.1.10

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.6-13
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.6-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-8
- BuildRequire python3-six which is used but was only transitively pulled in by python3-mock

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.6-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Piotr Popieluch <piotr1212@gmail.com> - 1.1.6-1
- Update to 1.1.6

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Piotr Popieluch <piotr1212@gmail.com> - 1.1.5-1
- Update to 1.1.5

* Thu Sep 27 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.1.4-2
- Remove Python 2 subpackage

* Sat Sep 15 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.1.4-1
- Update to 1.1.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-3
- Rebuilt for Python 3.7

* Mon Apr 09 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.1.3-2
- Switch tools to use Python 3

* Mon Apr 09 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.1.3-1
- Update to 1.1.3

* Wed Feb 28 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 26 2017 Piotr Popieluch <piotr1212@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Mon Nov 06 2017 Piotr Popieluch <piotr1212@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Piotr Popieluch <piotr1212@gmail.com> - 0.10.0-0.4.rc1
- Update requires to include Python version number

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-0.2.rc1
- Rebuild for Python 3.6

* Wed Aug 31 2016 Piotr Popieluch <piotr1212@gmail.com> - - 0.10.0-0.1.rc1
- Update to rc1
- Add Python3 support
- Add %%check section

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 28 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.9.15-1
- Update to new version

* Sat Nov 07 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.9.14-1
- Update to new version
- Add whisper-diff

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-0.2.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.9.13-0.1.pre1
- update to 0.9.13-pre1

* Fri Nov 14 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.9.12-4
- conditionally define macros for EPEL 6 and below

* Wed Oct 01 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.9.12-3
- update URL
- improve description
- specify commit hash in Source URL
- include man pages from Debian
- include missing LICENSE file
- include python egg
- use loop to rename files
- be more explicit in %%files

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 02 2013 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.9.12-1
- Update to 0.9.12

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 16 2012 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.9.10-2
- Add group to be able to build against EPEL5

* Thu May 31 2012 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.9.10-1
- Initial Package
