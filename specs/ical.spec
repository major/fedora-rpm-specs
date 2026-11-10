%global         forgeurl0 https://github.com/carlbyington2/ical
%global         version0  4.0.2
%global         tag       v%{version0}
%forgemeta

Summary: An X Window System-based calendar program
Name:    ical
Version: %{forgeversion}
Source:  %{forgesource}
URL:     %{forgeurl}
Release: 2%{?dist}
License: GPL-2.0-only AND NTP AND CC0-1.0

BuildRequires:  autoconf automake libtool
BuildRequires:  make gcc-c++
BuildRequires:  tcl-devel tk-devel
# for reading iCalendar files
BuildRequires:  libical-devel, libicu-devel
# for %%check section
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# packages required at runtime
Requires:       tcl tk
# for printing to pdf
Requires:       python3-reportlab
# for print preview
Requires:       evince
# since we have icons
Requires:       hicolor-icon-theme


%description
ical is an X Window System based calendar program. ical will
create/edit/delete entries, create repeating entries, remind you about
upcoming appointments, print and list item occurrences, and allow
shared calendars between different users.

%prep
%forgeautosetup
libtoolize --copy --force
aclocal
autoheader
automake --add-missing
autoconf


%conf
%configure --with-tclconfig=%{_libdir} --with-rpmversion=%{version} --prefix=/usr


%build
%make_build OPTF="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"


%install
%make_install
chmod 755 %{buildroot}%{_libdir}/%{name}/v%{version}/contrib/ical2zsh
chmod 755 %{buildroot}%{_libdir}/%{name}/v%{version}/contrib/icalweekly
chmod 755 %{buildroot}%{_libdir}/%{name}/v%{version}/contrib/oster_termine


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.five-ten-sg.ical.metainfo.xml


%files
%doc %{_pkgdocdir}
%{_bindir}/ical*
%{_mandir}/man1/ical.1*
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/*/%{name}.svg
%{_metainfodir}/com.five-ten-sg.ical.metainfo.xml
%license COPYING COPYRIGHT.ORIG


%changelog
%autochangelog
