%global _hardened_build 1

%global gh_name seadrive-fuse
Name:           seadrive-daemon
Version:        2.0.22
Release:        3%{?dist}
Summary:        Daemon part of Seafile Drive client

License:        GPLv3
URL:            https://seafile.com
Source0:        https://github.com/haiwen/%{gh_name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libsearpc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)

%description
Seafile is a next-generation open source cloud storage system, with advanced
support for file syncing, privacy protection and teamwork.

Seafile allows users to create groups with file syncing, wiki, and discussion
to enable easy collaboration around documents within a team.

This package contains the daemon part of Seafile Drive client. The Drive
client enables you to access files on the server without syncing to local
disk.


%package -n     python3-seadrive
Summary:        Python API for Seafile Drive client daemon

BuildRequires:  python3-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-seadrive
%{summary}.


%prep
%autosetup -n %{gh_name}-%{version}


%build
./autogen.sh
%configure --disable-static PYTHON=%{__python3}
%make_build


%install
%make_install

%files
%license LICENSE
%{_bindir}/seadrive

%files -n python3-seadrive
%{python3_sitearch}/seadrive/

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.22-1
- Update to 2.0.22 (#2099894)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.16-4
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.0.16-2
- Rebuilt with OpenSSL 3.0.0

* Wed Sep 08 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.16-1
- Update to 2.0.16

* Fri Aug 06 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.15-1
- Update to 2.0.15

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.10-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.10-1
- Update to 2.0.10

* Sun Nov 01 2020 Aleksei Bavshin <alebastr89@gmail.com> - 2.0.6-1
- Initial import (#1895548)
