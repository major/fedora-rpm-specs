Name:		xtv
Version:	1.0
Release:	5%{?dist}
Summary:	A file manager for the Linux console/xterm

License:	GPLv3+
URL:		http://sites.google.com/site/mohammedisam2000/home/projects
Source0:	http://sites.google.com/site/mohammedisam2000/home/projects/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:	cmake cups-devel cups

%description
The XTree View (XTV) is a file manager which is run under the Linux console/
xterm. It provides an easy way to manage files/directories, and perform various
operations on them by using menus and keyboard shortcuts.

%prep
%setup -q

%build
%cmake .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -D man/man1/xtv.1 %{buildroot}%{_mandir}/man1/xtv.1
install -D info/xtv.info %{buildroot}%{_infodir}/xtv.info

%files
%{_bindir}/xtv
%{_mandir}/man1/xtv.1*
%{_infodir}/xtv.*
%doc README COPYING


%changelog
* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-2
- Added Properties dialog box

* Tue Mar 18 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-1
- First release
