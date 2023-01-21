# Invoke with "--with tests" to enable tests
# Currently disabled by default as it requires network by default
%bcond_with tests

Name:       khal
Version:    0.9.10
Release:    15%{?git_tag}%{?dist}
Summary:    CLI calendar application

License:    MIT
URL:        https://github.com/pimutils/%{name}
Source0:    https://files.pythonhosted.org/packages/source/k/%{name}/%{name}-%{version}.tar.gz

# In theory documentation requires sphinxcontrib.newsfeed to generate
# a blog of the changelog. We only need the manpage. We also fix a Makefile error
# which happens when using .tar.gz
Patch0:     khal-0.8.2-sphinx-docfix.patch
BuildArch:  noarch

BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-configobj
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-sphinx

Requires:       python3-click >= 3.2
Requires:       python3-configobj
Requires:       python3-dateutil
Requires:       python3-icalendar
Requires:       python3-urwid
Requires:       python3-tzlocal
Requires:       python3-pytz
Requires:       python3-pyxdg
Requires:       vdirsyncer >= 0.8.1-2

%description
Khal is a standards based CLI (console) calendar program. CalDAV compatibility
is achieved by using vdir/vdirsyncer as a back-end, allowing syncing of
calendars with a variety of other programs on a host of different platforms.

%prep
%setup -q
%patch0 -p1 -b .doc

%build
%{__python3} setup.py build
cd doc
# Not using _smp_flags as sphinx barfs with it from time to time
PYTHONPATH=.. make SPHINXBUILD=sphinx-build-3 man html text
cd ..

%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
install -d "$RPM_BUILD_ROOT%{_mandir}/man1"
cp -r doc/build/man/%{name}.1 "$RPM_BUILD_ROOT%{_mandir}/man1"
# Remove extra copy of text docs
rm -vrf doc/build/html/_sources
rm -fv doc/build/html/{.buildinfo,objects.inv}

%check
# needs python3-tox bz #1010767
%if %{with tests}
tox -e py27
%endif


%files
%doc AUTHORS.txt README.rst CONTRIBUTING.rst khal.conf.sample doc/build/html doc/build/text
%license COPYING
%{python3_sitelib}/*
%{_bindir}/ikhal
%{_bindir}/khal
%{_mandir}/man1/%{name}.1.*

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.10-13
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.10-10
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.10-7
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.10-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.10-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Timothée Floure <fnux@fedoraproject.org> - 0.9.10-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 06 2017 Michele Baldessari <michele@acksyn.org> - 0.9.8-1
- New upstream release

* Sat Sep 16 2017 Michele Baldessari <michele@acksyn.org> - 0.9.7-1
- New upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Michele Baldessari <michele@acksyn.org> - 0.9.6-1
- New upstream release

* Mon Apr 10 2017 Michele Baldessari <michele@acksyn.org> - 0.9.5-1
- New upstream release

* Thu Mar 30 2017 Michele Baldessari <michele@acksyn.org> - 0.9.4-1
- New upstream release

* Tue Mar 07 2017 Michele Baldessari <michele@acksyn.org> - 0.9.3-1
- New upstream release

* Thu Feb 16 2017 Michele Baldessari <michele@acksyn.org> - 0.9.2-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-2
- Rebuild for Python 3.6

* Sat Oct 08 2016 Ben Boeckel <mathstuf@gmail.com> - 0.8.4-1
- update to 0.8.4

* Sun Sep 04 2016 Michele Baldessari <michele@acksyn.org> - 0.8.3-1
- New upstream

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 22 2016 Michele Baldessari <michele@acksyn.org> - 0.8.2-1
- New upstream

* Sat Apr 02 2016 Michele Baldessari <michele@acksyn.org> - 0.7.0-4
- Bump build to keep rawhide > f24

* Sat Apr 02 2016 Michele Baldessari <michele@acksyn.org> - 0.7.0-2
- Update github link
- Port to python3 (BZ 1323246)

* Sat Nov 28 2015 Michele Baldessari <michele@acksyn.org> - 0.7.0-1
- update to 0.7.0 (BZ 1285573)

* Sat Aug 08 2015 Ben Boeckel <mathstuf@gmail.com> - 0.6.0-1
- update to 0.6.0
- respin patches
- use PyPI tarball

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Michele Baldessari <michele@acksyn.org> - 0.5.0-2
- Fix build

* Wed Jun 03 2015 Michele Baldessari <michele@acksyn.org> - 0.5.0-1
- New upstream

* Mon Mar 02 2015 Michele Baldessari <michele@redhat.com> - 0.4.0-10
- Fix build

* Mon Mar 02 2015 Michele Baldessari <michele@redhat.com> - 0.4.0-9
- Disable python3 port until khal supports it fully

* Sun Mar 01 2015 Michele Baldessari <michele@redhat.com> - 0.4.0-8
- Fix broken build

* Sun Mar 01 2015 Michele Baldessari <michele@redhat.com> - 0.4.0-7
- Port to python3

* Sun Mar 01 2015 Michele Baldessari <michele@redhat.com> - 0.4.0-6
- Fix check section and make it work when run with tests enabled

* Sun Feb 15 2015 Michele Baldessari <michele@redhat.com> - 0.4.0-5
- Apply proper upstream fix for issue 159

* Sat Feb 14 2015 Michele Baldessari <michele@redhat.com> - 0.4.0-4
- Fix for issue https://github.com/geier/khal/issues/158
- Temp fix for issue 159

* Tue Feb 10 2015 Michele Baldessari <michele@redhat.com> - 0.4.0-3
- Add documentation

* Wed Feb 04 2015 Michele Baldessari <michele@redhat.com> - 0.4.0-2
- Fix the doc build

* Tue Feb 03 2015 Michele Baldessari <michele@redhat.com> - 0.4.0-1
- New upstream

* Mon Jan 05 2015 Michele Baldessari <michele@redhat.com> - 0.3.1-2
- Fixed some missing requires

* Wed Oct 01 2014 Michele Baldessari <michele@redhat.com> - 0.3.1-1
- Initial packaging
