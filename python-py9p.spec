%global srcname py9p

Name:       python-py9p
Version:    1.0.9
Release:    28%{?dist}
Summary:    Pure Python implementation of 9P protocol (Plan9)
License:    MIT
URL:        https://github.com/svinota/%{srcname}
Source:     %{url}/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  python3-devel


%description
Protocol 9P is developed for Plan9 operating system from Bell Labs.
It is used for remote file access, and since files are key objects
in Plan9, 9P can be used also for composite file access, RPC etc.

This library provides low-level 9p2000.u API. For high-level look
into python-pyvfs.


%package -n python3-%{srcname}
Summary:  %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Protocol 9P is developed for Plan9 operating system from Bell Labs.
It is used for remote file access, and since files are key objects
in Plan9, 9P can be used also for composite file access, RPC etc.

This library provides low-level 9p2000.u API. For high-level look
into python-pyvfs.

This is a Python 3 version.


%package -n 9pfs
Summary: Plan9 filesystem server
Requires: python3-%{srcname} = %version-%release

%description -n 9pfs
Protocol 9P is developed for Plan9 operating system from Bell Labs.
It is used for remote file access, and since files are key objects
in Plan9, 9P can be used also for composite file access, RPC etc.

This package contains simple file server for the 9p protocoll.


%package -n fuse9p
Summary: Plan9 filesystem client for FUSE
Requires: python3-%{srcname} = %version-%release
Requires: python3-fuse

%description -n fuse9p
Protocol 9P is developed for Plan9 operating system from Bell Labs.
It is used for remote file access, and since files are key objects
in Plan9, 9P can be used also for composite file access, RPC etc.

This package contains FUSE client for the 9p protocol. It is in the
beta development state.


%prep
%setup -q -n %{srcname}-%{version}

# Fix the shebangs
sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' fuse9p/fuse9p 9pfs/9pfs examples/simplesrv.py examples/composite.py examples/cl.py test/test.py test/analyze.py setup.py.in

%build
# this step generates setup.py from setup.py.in
make force-version
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%files -n fuse9p
%license LICENSE
%{_bindir}/fuse9p
%{_mandir}//man1/fuse9p.*

%files -n 9pfs
%license LICENSE
%{_bindir}/9pfs
%{_mandir}//man1/9pfs.*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.9-27
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.9-24
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.9-21
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.9-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.9-18
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.9-15
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.9-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.9-9
- Rebuild for Python 3.6

* Wed Sep 21 2016 Lumir Balhar <lbalhar@redhat.com> - 1.0.9-8
- Add Python 2/3 subpackages for python-py9p module
- Switch 9pfs and fuse9p to Python 3
- Modernize specfile

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Peter V. Saveliev <peet@redhat.com> 1.0.9-2
- fedpkg import fix

* Wed Jun 12 2013 Peter V. Saveliev <peet@redhat.com> 1.0.9-1
- symlink support
- read/write improved
- 9pfs subpackage
- 9p marshalling is thread-safe now
- fuse9p stateful I/O
- Python 3 sompatibility issues

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 07 2012 Peter V. Saveliev <peet@redhat.com> 1.0.5-1
- fuse9p subpackage added (beta)
- pki authentication fixed

* Fri Oct 19 2012 Peter V. Saveliev <peet@redhat.com> 1.0.2-1
- support AES-encrypted keys
- authfs fixed

* Fri Oct 12 2012 Peter V. Saveliev <peet@redhat.com> 1.0.1-1
- Initial RH build
