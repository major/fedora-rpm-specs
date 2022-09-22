Name:             datanommer
Version:          0.2.0
Release:          25%{?dist}
Summary:          A storage consumer for the Fedora Message Bus (fedmsg)

License:          GPLv3+
URL:              https://pypi.python.org/pypi/datanommer
Source0:          https://pypi.python.org/packages/source/d/%{name}/%{name}-%{version}.tar.gz
BuildArch:        noarch


BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-datanommer-models
BuildRequires:    python3-datanommer-consumer
BuildRequires:    datanommer-commands

Requires:         python3-datanommer-models
Requires:         python3-datanommer-consumer
Requires:         datanommer-commands


%description
This is datanommer.  It is comprised of only a fedmsg consumer that
stuffs every message in a sqlalchemy database.

There are also a handful of CLI tools to dump information from the
database.

%prep
%setup -q -n %{name}-%{version}

# Make sure that epel/rhel picks up the correct version of sqlalchemy
%{__awk} 'NR==1{print "import __main__; __main__.__requires__ = __requires__ = [\"sqlalchemy>=0.7\"]; import pkg_resources"}1' setup.py > setup.py.tmp
%{__mv} setup.py.tmp setup.py

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}

%files
%doc README.rst LICENSE
%{python3_sitelib}/%{name}-%{version}*egg-info/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.0-22
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-19
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-17
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Ralph Bean <rbean@redhat.com> - 0.2.0-14
- Update to python3.

* Sun Jul 22 2018 Kevin Fenzi <kevin@scrye.com> - 0.2.0-13
- FIx FTBFS bug #1603744

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.0-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-2
- Add a forgotten file declaration on the egg-info.
* Mon Nov 12 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-1
- Split up components into their own packages.
- Stripped out almost all content in this package.
* Mon Oct 08 2012 Ralph Bean <rbean@redhat.com> - 0.1.8-2
- Remove requirement on python-bunch.
* Thu Oct 04 2012 Ralph Bean <rbean@redhat.com> - 0.1.8-1
- More flexible database field types.
* Fri Sep 28 2012 Ralph Bean <rbean@redhat.com> - 0.1.7-1
- New upstream with a db table for compose messages.
* Wed Sep 26 2012 Ralph Bean <rbean@redhat.com> - 0.1.6-1
- Upstream release requiring the latest python-moksha-hub for API tweaks.
* Mon Sep 24 2012 Ralph Bean <rbean@redhat.com> - 0.1.5-1
- Upstream release removed the gpl->LICENSE symlink.  More trouble than it was
  worth.
* Wed Sep 19 2012 Ralph Bean <rbean@redhat.com> - 0.1.4-1
- Depend on the very latest fedmsg to dispel confusion.
* Thu Sep 06 2012 Ralph Bean <rbean@redhat.com> - 0.1.3-2
- Remove whitespace between config and noreplace.
* Thu Aug 30 2012 Ralph Bean <rbean@redhat.com> - 0.1.3-1
- Initial package for Fedora
