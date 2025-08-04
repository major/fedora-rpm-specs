Name: evolution-rspam
Summary: Evolution Plugin for reporting spam
Version: 0.6.0
Release: 51%{?dist}
License: GPL-2.0-or-later
Source: http://gnome.eu.org/%{name}-%{version}.tar.xz
URL: http://gnome.eu.org/evo/index.php/Report_as_Spam

Patch0: evolution-rspam-0.6.0-evo38.patch
Patch1: evolution-rspam-0.6.0-convert-fix.patch
Patch2: evolution-rspam-0.6.0-globals-clash.patch
Patch3: evolution-rspam-0.6.0-evo312.patch
Patch4: evolution-rspam-0.6.0-evo313.patch
Patch5: evolution-rspam-0.6.0-evo3136.patch
Patch6: evolution-rspam-0.6.0-source-double-unref.patch
Patch7: evolution-rspam-0.6.0-activity-leak.patch
Patch8: evolution-rspam-0.6.0-evo3_23_2.patch
Patch9: evolution-rspam-0.6.0-fix-po-charset.patch
Patch10: evolution-rspam-0.6.0-no-gtkuimanager.patch
Patch11: evolution-rspam-0.6.0-spamcop-flush-outbox-on-send.patch
Patch12: evolution-rspam-0.6.0-gcc-changes.patch
Patch13: evolution-rspam-0.6.0-drop-gconf-requirement.patch
Patch14: evolution-rspam-0.6.0-evo3_57_1.patch
Patch15: evolution-rspam-0.6.0-am_nls.patch

Requires: perl-Razor-Agent
Requires: pyzor
Requires: evolution >= 3.55.1

BuildRequires: gettext, evolution-devel >= 3.55.1, perl(XML::Parser), intltool
BuildRequires: autoconf, automake, gettext-devel, gnome-common, libtool
BuildRequires: make

%description
Rspam Evolution Plugin enables Evolution Mail client to report email messages
as spam to checksum-based and statistical filtering networks.
It supports Razor network, DCC, SpamCop and Pyzor.
This plugins requires a pretty new version of evolution to build.
See README for more information about required programs.

%prep
%autosetup -p1 -S gendiff

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name \*\.la -print | xargs rm -f
%find_lang rspam

# remove old GConf schemas
#find $RPM_BUILD_ROOT/%{_sysconfdir}/gconf/schemas -name '*.schemas' -exec rm {} \;

%files -f rspam.lang
%{_datadir}/GConf/gsettings/evolution-rspam.convert
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.evolution-rspam.gschema.xml
%{_datadir}/evolution/ui/*.ui
%{_libdir}/evolution/plugins/org-gnome-sa-rspam.eplug
%{_libdir}/evolution/plugins/liborg-gnome-sa-rspam.so
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%doc NEWS
%doc README
%doc TODO

%changelog
%autochangelog
