Name:		xdg-user-dirs
Version:	0.19
Release:	%autorelease
Summary:	Handles user special directories

License:	GPL-2.0-or-later AND MIT
URL:		https://freedesktop.org/wiki/Software/xdg-user-dirs
Source0:	https://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gettext-devel
BuildRequires:	git-core
BuildRequires:	docbook-style-xsl
BuildRequires:	libxslt
BuildRequires:	systemd-rpm-macros
%if 0%{?fedora} && 0%{?fedora} < 42
BuildRequires:  desktop-file-utils
%endif

Requires:	%{_sysconfdir}/xdg/autostart

%description
Contains xdg-user-dirs-update that updates folders in a users
homedirectory based on the defaults configured by the administrator.

%prep
%autosetup -S git_am

%conf
autoreconf -fiv -I ./m4
%configure

%build
%make_build

%install
%make_install

%find_lang %name

%if 0%{?fedora} && 0%{?fedora} < 42
desktop-file-edit --remove-key=X-systemd-skip %{buildroot}%{_sysconfdir}/xdg/autostart/xdg-user-dirs.desktop
rm -rf %{buildroot}%{_userunitdir}
%endif

%if ! (0%{?fedora} && 0%{?fedora} < 42)
%post
%systemd_user_post xdg-user-dirs.service

%preun
%systemd_user_preun xdg-user-dirs.service

%postun
%systemd_user_postun_with_reload xdg-user-dirs.service
%endif


%files -f %{name}.lang
%license COPYING
%doc NEWS AUTHORS README.md
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.conf
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.defaults
%{_sysconfdir}/xdg/autostart/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%if ! (0%{?fedora} && 0%{?fedora} < 42)
%{_userunitdir}/xdg-user-dirs.service
%endif


%changelog
%autochangelog
