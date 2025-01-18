%global _lto_cflags %nil

Name:       distcc
Version:    3.4
Release:    8%{?dist}
Summary:    Distributed C/C++ compilation
License:    GPL-2.0-or-later
URL:        https://github.com/distcc/distcc
Source0:    https://github.com/distcc/distcc/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    hosts.sample
Source2:    distccd.service
Patch0:     distcc-localhost.patch
Patch1:     crash.patch
Patch2:     479.patch

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: which
BuildRequires: libtool
BuildRequires: popt-devel
BuildRequires: gtk3-devel
BuildRequires: pango-devel
BuildRequires: python3-devel
Buildrequires: python3-setuptools
BuildRequires: desktop-file-utils
BuildRequires: avahi-devel
BuildRequires: krb5-devel
BuildRequires: binutils-devel
BuildRequires: systemd-rpm-macros
BuildRequires: make

%description
distcc is a program to distribute compilation of C or C++ code across
several machines on a network. distcc should always generate the same
results as a local compile, is simple to install and use, and is often
two or more times faster than a local compile.


%package    gnome
Summary:    Gnome frontend of distcc monitoring tool
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description gnome
This package contains the Gnome frontend of the distcc monitoring tool.


%package     server
Summary:    Server for distributed C/C++ compilation
License:    GPL-2.0-or-later

Requires:   %{name}%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%description server
This package contains the compilation server needed to use %{name}.


%prep
%setup -q
%patch -P 0 -p0
%patch -P 1 -p0
%patch -P 2 -p1

%build
export PYTHON='/usr/bin/python3'
./autogen.sh
export CFLAGS="%{optflags} -fcommon"
%configure --with-gtk --disable-Werror --with-auth
%make_build


%install
%make_install

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

# Install sample hosts file
install -Dm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/hosts

# Install sample distccd config file
install -Dm 0644 contrib/redhat/sysconfig $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/distccd

# Install distcdd unit file
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -Dm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/distccd.service

# Install distcc dirs
mkdir -p $RPM_BUILD_ROOT/usr/lib/distcc
mkdir -p $RPM_BUILD_ROOT/usr/lib/gcc-cross
if [ ! -d $RPM_BUILD_ROOT/usr/lib64 ]; then
  mkdir -p $RPM_BUILD_ROOT/usr/lib64
fi
ln -s /usr/lib/distcc $RPM_BUILD_ROOT/usr/lib64/distcc

rm -rf $RPM_BUILD_ROOT%{_docdir}/*

%post server
%systemd_post distccd.service
%{_sbindir}/update-distcc-symlinks > /dev/null 2>&1

%preun server
%systemd_preun distccd.service

%postun server
%systemd_postun_with_restart distccd.service

%files
%license COPYING
%doc AUTHORS doc/* NEWS README.pump TODO
%doc INSTALL README survey.txt
%{_bindir}/distcc
%{_bindir}/distccmon-text
%{_bindir}/lsdistcc
%{_bindir}/pump
%{_mandir}/man1/distcc.*
%{_mandir}/man1/distccmon*
%{_mandir}/man1/pump*
%{_mandir}/man1/include_server*
%{_mandir}/man1/lsdistcc*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/hosts
%{python3_sitearch}/include_server*


%files gnome
%{_bindir}/distccmon-gnome
%{_datadir}/pixmaps/distccmon-gnome.png
%{_datadir}/applications/*.desktop


%files server
%license COPYING
%doc README
%{_bindir}/distccd
%{_unitdir}/*
%{_sysconfdir}/default/distcc
%{_sysconfdir}/distcc/*allow*
%{_mandir}/man1/distccd*
%config(noreplace) %{_sysconfdir}/sysconfig/distccd
%{_sbindir}/update-distcc-symlinks
%dir /usr/lib/distcc
/usr/lib64/distcc
%dir /usr/lib/gcc-cross

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.4-7
- Patch for Py_ssize_t

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.4-5
- Rebuilt for Python 3.13

* Tue Feb 13 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.4-4
- Disable LTO to fix distccmon-gnome crash, 2263992.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.4-1
- 3.4

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.3.5-14
- Rebuilt for Python 3.12

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.3.5-13
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.3.5-11
- BR setuptools.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3.5-9
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.5-6
- Rebuilt for Python 3.10

* Wed Mar 24 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.3.5-5
- Fix desktop file icon path.

* Mon Mar 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.3.5-4
- Silence update-distcc-symlinks at install time.

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3.5-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.3.5-1
- 3.3.5

* Mon Nov 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.3.3-10
- Spec cleanup, fix FTBFS.

* Wed Sep 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.3.3-9
- Use gtk, not gnome, for monitor.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.3-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.3.3-5
- Build with -fcommon for gcc10.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.3-2
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.3.3-1
- 3.3.3

* Tue Aug 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.3.2-1
- Python 3.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.2rc1-23
- Honor clients.allow

* Thu Feb 21 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.2rc1-22
- Restrict to localhost by default.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.2rc1-19
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.2rc1-17
- Drop --verbose, BZ 1523785.

* Thu Dec 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.2rc1-16
- Patch for argument bug, BZ 1527368
- Move required components for pump to client package, BZ 1525851

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2rc1-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2rc1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 Jon Ciesla <limburgher@gmail.com> - 3.2rc1-9
- Enable authentication support, BZ 1201039.

* Wed Aug 20 2014 Andy Grover <agrover@redhat.com> - 3.2rc1-8
- Add patch distcc-minilzo-2.08.patch, to fix CVE-2014-4607 (BZ 1131791)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2rc1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2rc1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Jon Ciesla <limburgher@gmail.com> - 3.2rc1-5
- Fixed unversioned docdir issue, BZ 993722.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2rc1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Jon Ciesla <limburgher@gmail.com> - 3.2rc1-3
- chmod -x .service, BZ 963912

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2rc1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Jon Ciesla <limburgher@gmail.com> - 3.2rc1-1
- Latest upstream, BZ 870200.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 3.1-6
- Add hardened build.

* Tue Jan 31 2012 Jon Ciesla <limburgher@gmail.com> - 3.1-5
- Migrate to systemd, BZ 770409.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 3.1-3
- Rebuild for libpng 1.5.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 07 2010 Jon Ciesla <limb@jcomserv.net> - 3.1-1
- New upstream, BZ 641032.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 22 2008 Denis Leroy <denis@poolshark.org> - 2.18.3-4
- Added Avahi support patch from Lennart

* Tue Feb 19 2008 Denis Leroy <denis@poolshark.org> - 2.18.3-3
- LSB header for init script

* Mon Feb 18 2008 Denis Leroy <denis@poolshark.org> - 2.18.3-2
- Fixed Source0 URL, fixed init script

* Mon Feb  4 2008 Denis Leroy <denis@poolshark.org> - 2.18.3-1
- First version

