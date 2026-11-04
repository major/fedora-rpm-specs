Summary: Screen lock and screen saver
Name: xlockmore
Version: 5.90
Release: %autorelease
License: xlock AND HPND AND HPND-sell-variant AND SGI-OpenGL AND X11 AND (GPL-2.0-or-later OR MIT)
URL: http://sillycycle.com/xlockmore.html
Source0: http://sillycycle.com/xlock/xlockmore-%{version}.tar.xz
BuildRequires: make
BuildRequires: gcc gcc-c++
BuildRequires: pam-devel
BuildRequires: mesa-libGL-devel mesa-libGLU-devel
BuildRequires: desktop-file-utils libXdmcp-devel
BuildRequires: motif-devel gtk2-devel
BuildRequires: libXau-devel
Patch0: xlockmore-ignore-void.patch
%if 0%{?rhel}
Requires: gnome-icon-theme
%else
Requires: gnome-icon-theme-legacy
%endif

%description
Locks the local X display until a password is entered.

%package motif
Summary: Motif based frontend for xlockmore
License: xlock
Requires: %{name} = %{version}-%{release}

%description motif
Motif based frontend for xlockmore.

%package gtk
Summary: GTK based frontend for xlockmore
License: xlock
Requires: %{name} = %{version}-%{release}

%description gtk
GTK based frontend for xlockmore.

%prep
%setup -q
%patch -P 0 -p 1

%{__sed} -i -e "s,/lib,/%{_lib},g;s,-Wno-format,,g;" configure

# See README for X(M)LOCKLDFLAGS explanation
%{__sed} -i "/^XLOCKLDFLAGS$/d" configure
%{__sed} -i "/^XMLOCKLDFLAGS$/d" configure

%build
%configure --with-crypt --enable-pam --enable-syslog --disable-setuid --disable-mb

# Work around BZ#2341574
sed -i 's/^CC =.*/\0 -std=c17/' xglock/Makefile

# See README for X(M)LOCKLDFLAGS explanation
sed -i 's/@XLOCKLDFLAGS@//' modes/Makefile
sed -i 's/@XMLOCKLDFLAGS@//' xmlock/Makefile

%{__make} %{?_smp_mflags}

%install
%{__install} -D -m0755 xlock/xlock %{buildroot}%{_bindir}/xlock
%{__install} -D -m0755 xmlock/xmlock %{buildroot}%{_bindir}/xmlock
%{__install} -D -m0755 xglock/xglock %{buildroot}%{_bindir}/xglock
%{__install} -p -D -m0644 xlock/xlock.man %{buildroot}%{_mandir}/man1/xlock.1
%{__install} -p -D -m0644 xlock/XLock.ad %{buildroot}%{_libdir}/X11/app-defaults/XLock
%{__install} -p -D -m0644 xmlock/XmLock.ad %{buildroot}%{_libdir}/X11/app-defaults/XmLock
%{__chmod} 644 README
%{__chmod} 644 docs/Revisions


%{__mkdir_p} %{buildroot}%{_sysconfdir}/pam.d
cat > %{buildroot}%{_sysconfdir}/pam.d/xlock << EOF
#%PAM-1.0
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    include      system-auth
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications

cat >> %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Xlock
Comment=Screen Saver
Encoding=UTF-8
Icon=gnome-lockscreen
Exec=xlock
Terminal=false
Type=Application
EOF

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	--delete-original \
	--add-category X-Fedora \
	--add-category Application \
	--add-category Graphics \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README docs/*
%doc %{_mandir}/man1/xlock.1*
%{_bindir}/xlock
%{_libdir}/X11/app-defaults/XLock
%config(noreplace) %{_sysconfdir}/pam.d/xlock
%{_datadir}/applications/*

%files motif
%{_bindir}/xmlock
%{_libdir}/X11/app-defaults/XmLock

%files gtk
%{_bindir}/xglock

%changelog
%autochangelog
