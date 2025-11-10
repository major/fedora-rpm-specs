Summary: Completely configurable key-combo grabber for blackbox
Name: bbkeys
Version: 0.9.0
Release: %autorelease
License: MIT
URL: http://bbkeys.sourceforge.net/
Source: http://downloads.sf.net/bbkeys/bbkeys-%{version}.tar.gz
Patch0: bbkeys-0.9.0-gcc43.patch
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: blackbox-devel, perl-interpreter
BuildRequires: libX11-devel, libXext-devel
BuildRequires: make
BuildRequires: autoconf automake

%description
bbkeys is a configurable key-grabber designed for the blackbox window manager
which is written by Brad Hughes.  It is based on the bbtools object code
created by John Kennis and re-uses some of the blackbox window manager classes
as well.  bbkeys is easily configurable via directly hand-editing the user's
~/.bbkeysrc file, or by using the GUI total blackbox configurator, bbconf.


%prep
%autosetup -p1


%build
autoreconf -vi
%configure --datadir=%{_sysconfdir}
%make_build


%install
%make_install
# Clean this up, we package the exact same files cleanly in %%doc
# and it ends up in the wrong place with our override anyway
%{__rm} -rf %{buildroot}%{_sysconfdir}/doc/


%files
%doc AUTHORS BUGS ChangeLog LICENSE NEWS README TODO
%dir %{_sysconfdir}/bbkeys/
%config(noreplace) %{_sysconfdir}/bbkeys/bbkeysrc
%config(noreplace) %{_sysconfdir}/bbkeys/defaultStyle
%{_bindir}/bbkeys
%{_mandir}/man1/bbkeys.1*
%{_mandir}/man5/bbkeysrc.5*


%changelog
%autorelease
