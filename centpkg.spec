# In order to use unversioned python macros in the spec file, we need to
# explicitly define %%__python.
%global __python %{_bindir}/python3

%if %{defined el8}
%global __python %{_libexecdir}/platform-python
%endif

%if %{defined el7}
%global __python %{_bindir}/python
%endif


Name:           centpkg
Version:        0.6.7
Release:        2%{?dist}
Summary:        CentOS utility for working with dist-git
License:        GPLv2+
URL:            https://git.centos.org/centos/centpkg
Source0:        %{url}/archive/%{version}/centpkg-%{version}.tar.gz
BuildArch:      noarch

%if %{defined el7}
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-six
BuildRequires:  python-rpkg
# The equivalent dependencies are added automatically everywhere except el7.
Requires:       python-pycurl
Requires:       pyOpenSSL
Requires:       python-rpkg >= 1.65
Requires:       python-six
%else
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-rpkg
# Auto dependencies are not showing the version.
Requires:       python3-rpkg >= 1.65
%endif

# /etc/koji.conf.d/stream.conf was previously part of streamkoji
Conflicts:      streamkoji < 1.1-3


%description
Provides the centpkg command for working with dist-git.


%package sig
Summary:        CentOS SIG utility for working with dist-git
Requires:       %{name} = %{version}-%{release}


%description sig
Provides the centpkg-sig command for working with dist-git.


%prep
%autosetup -p 1


%build
%py_build
%{__python} doc/centpkg_man_page.py > centpkg.1


%install
%py_install
install -D -p -m 0644 src/stream.conf      %{buildroot}%{_sysconfdir}/koji.conf.d/stream.conf
install -D -p -m 0644 src/centpkg.conf     %{buildroot}%{_sysconfdir}/rpkg/centpkg.conf
install -D -p -m 0644 src/centpkg-sig.conf %{buildroot}%{_sysconfdir}/rpkg/centpkg-sig.conf
install -D -p -m 0644 src/centpkg.bash     %{buildroot}%{_datadir}/bash-completion/completions/centpkg
install -D -p -m 0644 centpkg.1            %{buildroot}%{_mandir}/man1/centpkg.1


%files
%license COPYING
%doc README.md
%config(noreplace) %{_sysconfdir}/koji.conf.d/stream.conf
%config(noreplace) %{_sysconfdir}/rpkg/centpkg.conf
%{_bindir}/%{name}
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py%{python_version}.egg-info
%{_datadir}/bash-completion/completions/centpkg
%{_mandir}/man1/centpkg.1*


%files sig
%{_bindir}/%{name}-sig
%config(noreplace) %{_sysconfdir}/rpkg/centpkg-sig.conf


%changelog
* Thu Sep 08 2022 Troy Dawson <tdawson@redhat.com> - 0.6.7-2
- centpkg 0.6.7 requires rpkg 1.65 or greater

* Thu Sep 08 2022 Troy Dawson <tdawson@redhat.com> - 0.6.7-1
- Latest upstream

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.6.6-5
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Carl George <carl@george.computer> - 0.6.6-3
- Backport upstream patch for "name 'header' is not defined" error

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Mohan Boddu <mboddu@bhujji.com> - 0.6.6-1
- Latest upstream

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.5-2
- Rebuilt for Python 3.10

* Tue May 25 2021 Carl George <carl@george.computer> - 0.6.5-1
- Latest upstream

* Wed Apr 28 2021 Carl George <carl@george.computer> - 0.6.4-1
- Latest upstream

* Fri Apr 16 2021 Carl George <carl@george.computer> - 0.6.3-1
- Latest upstream

* Tue Apr 13 2021 Carl George <carl@george.computer> - 0.6.2-1
- Latest upstream
- Add stream koji profile

* Thu Apr 08 2021 Carl George <carl@george.computer> - 0.6.1-1
- Latest upstream
- Add bash completion support
- Add manpage support

* Tue Mar 30 2021 Carl George <carl@george.computer> - 0.5.1-3
- Fix epel7/python2 compatibility

* Thu Mar 25 2021 Carl George <carl@george.computer> - 0.5.1-2
- Add missing el7 requirements

* Thu Mar 25 2021 Carl George <carl@george.computer> - 0.5.1-1
- Latest version

* Thu Feb 25 2021 mkonecny@redhat.com 0.5.0-1
- Add centpkg-sig command

* Mon Nov 28 2016 brian@bstinson.com 0.4.6-1
- Tracking updates to rpkg (thanks pavlix)
- Fix the URL building code in the sources method

* Sat Jan 31 2015 Brian Stinson bstinson@ksu.edu - 0.4.4-1
- New version correcting the anonymous pull URLs

* Sun Dec 14 2014 Brian Stinson bstinson@ksu.edu - 0.4.3-1
- Use the authenticated git url for centpkg pulls

* Sun Dec 14 2014 Brian Stinson bstinson@ksu.edu - 0.4.2-1
- Fix the koji config path in centpkg.conf

* Sun Dec 14 2014 Brian Stinson bstinson@ksu.edu - 0.4.1-1
- Fix a disttag regression and add a "patch" version number

* Sat Nov 23 2014 Brian Stinson bstinson@ksu.edu - 0.2-1
- The srpm workflow to the CBS works now

* Sat Jul 05 2014 Brian Stinson bstinson@ksu.edu - 0.1-2
- Update readme and add exception checking when running toplevel commands

* Sat Jul 05 2014 Brian Stinson bstinson@ksu.edu - 0.1-1
- Local builds and mockbuilds work
