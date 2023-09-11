%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global pkgname Xfce-Theme-Manager
Name:		xfce-theme-manager
Version:	0.3.9
Release:	%autorelease
Summary:	A theme manager for Xfce
License:	GPLv3	
URL:		https://github.com/KeithDHedger/Xfce-Theme-Manager
# wget https://github.com/KeithDHedger/Xfce-Theme-Manager/archive/xfce-theme-manager-0.3.8.tar.gz
Source0:	https://github.com/KeithDHedger/Xfce-Theme-Manager/archive/%{pkgname}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	cairo-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	xfce4-dev-tools
BuildRequires:	xfconf-devel

%description
A theme manager allowing easy configuration of themes,
window borders, controls, icons and cursors for Xfce

%prep
%autosetup -n %{pkgname}-%{version} -p1


%build
#run autoreconf, not needed when upstream moves to  new automake
autoreconf -v -f -i -I.
%configure
make %{?_smp_mflags} xfcethememanager_CFLAGS="%{optflags} -export-dynamic" xfcethememanager_CXXFLAGS="%{optflags} -export-dynamic -Wunused -Wunused-function -Wno-unused-result -fPIC"


%install
make install DESTDIR=%{buildroot} docfilesdir="%{_pkgdocdir}"
desktop-file-install	\
--delete-original	\
--dir=%{buildroot}%{_datadir}/applications	\
--remove-key=Categories	\
--add-category=GTK	\
--add-category=Settings	\
--add-category=DesktopSettings	\
--add-category=X-XFCE-SettingsDialog	\
--add-category=X-XFCE-PersonalSettings	\
--add-category=X-XFCE	\
--set-name="Xfce Theme Manager"	\
%{buildroot}/%{_datadir}/applications/%{pkgname}.desktop


%files
%doc ChangeLog* Xfce-Theme-Manager/resources/docs/gpl-3.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{pkgname}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/Xfce-Theme-Manager/scripts
%{_mandir}/man1/%{name}.1.*
%{_mandir}/*/man1/%{name}.1.*

%changelog
%autochangelog
