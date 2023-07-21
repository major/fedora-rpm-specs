%global _hardened_build 1

Name:           ccnet
Version:        6.1.8
Release:        18%{?dist}
Summary:        A framework for writing networked applications in C

License:        GPLv3
URL:            https://github.com/haiwen/%{name}
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}.tar.gz
Patch0:         fix-async-client-py3.patch
Patch1:         fix-packet-py3.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glib2-devel
BuildRequires:  sqlite-devel
BuildRequires:  openssl-devel
BuildRequires:  libevent-devel
BuildRequires:  libuuid-devel
BuildRequires:  libsearpc-devel
BuildRequires:  libzdb-devel
BuildRequires:  python3-devel
BuildRequires:  vala
BuildRequires: make

Requires:       sqlite


%description
Ccnet is a framework for writing networked applications in C. It provides the
following basic services:

* Peer identification
* Connection Management
* Service invocation
* Message sending

In ccnet network, there are two types of nodes, i.e., client and server.
Server has the following functions:

* User management
* Group management
* Cluster management


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
Requires:       libevent-devel
Requires:       libsearpc-devel


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -qn %{name}-%{version}
%patch0 -p1
%patch1 -p1
sed -i -e /\(DESTDIR\)/d libccnet.pc.in


%build
./autogen.sh --enable-server --enable-client
%configure --disable-static --disable-compile-demo PYTHON=/usr/bin/python3
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"


%install
%{__make} install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%check
%{__make} check


%ldconfig_scriptlets


%files
%doc HACKING README.markdown
%license LICENSE.txt
%{_libdir}/libccnet.so.*
%{_bindir}/%{name}*
%{python3_sitearch}/%{name}


%files devel
%license LICENSE.txt
%{_includedir}/*
%{_libdir}/libccnet.so
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 6.1.8-17
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.1.8-14
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 6.1.8-12
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.1.8-10
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 20:29:08 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.1.8-8
- Rebuilt for libevent 2.1.12

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.1.8-6
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Julien Enselme <jujens@jujens.eu> - 6.1.8-4
- Make this package compatible with Python 3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Julien Enselme <jujens@jujens.eu> - 6.1.8-1
- Update to 6.1.8

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Julien Enselme <jujens@jujens.eu> - 6.1.6-1
- Update to 6.1.6

* Mon Feb 19 2018 Julien Enselme <jujens@jujesn.eu> - 6.1.4-3
- Add a require for sqlite: configuration is stored in a sqlite database. Without sqlite, it cannot work.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 27 2017 Julien Enselme <jujens@jujens.eu> - 6.1.4-1
- Update to 6.1.4

* Mon Nov 06 2017 Julien Enselme <jujens@jujens.eu> - 6.1.3-1
- Update to 6.1.3

* Thu Aug 10 2017 Julien Enselme <jujens@jujens.eu> - 6.1.0-1
- Update to 6.1.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 07 2017 Julien Enselme <jujens@jujens.eu> - 6.0.6-1
- Update to 6.0.6
- Build with openSSL 1.0 instead of compat

* Tue Mar 07 2017 Julien Enselme <jujens@jujens.eu> - 6.0.4-1
- Update to 6.0.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 30 2016 Julien Enselme <jujens@jujens.eu> - 6.0.0-2
- Compile against compat-openssl10 until it is compatible with OpenSSL 1.1

* Sun Oct 23 2016 Julien Enselme <jujens@jujens.eu> - 6.0.0-1
- Update to 6.0.0
- Unretire package

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Julien Enselme <jujens@jujens.eu> - 5.1.2-1
- Update to 5.1.2

* Tue Feb 02 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.0.5-1
- Update to 5.0.5

* Thu Dec 03 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 5.0.0-1
- Update to 5.0.0
- Add license to devel subpackage
- Add optflags
- Add libzdb-devel requirement
- Add python2-devel requirement
- unused-direct-shlib-dependency

* Wed Sep 16 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 4.3.4-1
- Update to 4.3.4

* Sat Apr 11 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 4.1.4-1
- Update to 4.1.4
- Hardened build

* Wed Nov 05 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.8-1
- Update to 3.1.8

* Tue Aug 12 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.4-1
- Initial version of the package
