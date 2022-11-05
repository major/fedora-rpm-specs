Summary: Locale and ISO 2022 support for Unicode terminals

%global AppVersion 20221028

Name: luit
Version: 2.0.%{AppVersion}
Release: 1%{?dist}
License: MIT
URL: https://invisible-island.net/%{name}/
Source0: https://invisible-mirror.net/archives/%{name}/%{name}-%{AppVersion}.tgz
BuildRequires: gcc
BuildRequires: make
BuildRequires: zlib-devel

%description
Luit is a filter that can be run between an arbitrary application and a
UTF-8 terminal emulator.  It will convert application output  from  the
locale's  encoding  into  UTF-8,  and convert terminal input from UTF-8
into the locale's encoding.

Unlike the older XFree86/Xorg version of luit, this does not rely upon
the fontenc package.

%prep

%setup -q -n %{name}-%{AppVersion}

%build

%configure

%make_build

%install
%make_install

%files
%license COPYING
%doc %{name}.log.html
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
* Wed Nov 02 2022 Thomas E. Dickey <dickey@his.com> - 2.0.20221028-1
- update configure script

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20210218-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20210218-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Thomas E. Dickey <dickey@his.com> - 2.0.20210218-1
- address review comments
