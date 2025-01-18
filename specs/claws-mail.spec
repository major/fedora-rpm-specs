%global pluginapi 4.3.0.0

# dillo plugin crashes
# Gtk-WARNING **: xx:xx:xx.xxx: GtkSocket: only works under X11
# Gdk-WARNING **: xx:xx:xx.xxx: gdkwindow-x11.c:5653 drawable is not a native X11 window
# Segmentation fault (core dumped)
%global with_dillo 0
# added 20210720
Obsoletes: claws-mail-plugins-dillo < 4.0.0-1

%global with_python2 0
%global with_python3 1
%if 0%{?rhel} && 0%{?rhel} < 9
%global with_python2 1
%endif

# toggle to avoid temporary docbook-utils and Tex Live dependency issues
%if 0%{?fedora}
%global build_manual 1
%endif

# added 2023-11-20
%if 0%{?fedora} > 36
Obsoletes: claws-mail-plugin-gdata < 4.2.0-1
%endif

Name:           claws-mail
Version:        4.3.0
Release:        7%{?dist}
Summary:        Email client and news reader based on GTK+
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://claws-mail.org
Source0:        https://claws-mail.org/releases/%{name}-%{version}.tar.xz

# rhbz#1179279
Patch11:        claws-mail-system-crypto-policies.patch

BuildRequires:  gcc, flex, bison, make
BuildRequires:  pkgconfig(glib-2.0) >= 2.20
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(gnutls) >= 2.2
BuildRequires:  libgcrypt-devel
BuildRequires:  openldap-devel >= 2.0.7
BuildRequires:  pkgconfig(enchant-2) >= 2.0.0
%if !0%{?rhel}
%ifnarch s390 s390x
BuildRequires:  pilot-link-devel
%endif
%endif
BuildRequires:  bzip2-devel
BuildRequires:  pkgconfig(gpgme) >= 1.1.1
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libstartup-notification-1.0) >= 0.5
BuildRequires:  pkgconfig
BuildRequires:  gettext gettext-devel
# actually 1.9.1 with TLS SNI patches, which are integrated into 1.9.2
BuildRequires:  libetpan-devel >= 1.9.2
%if !0%{?rhel}
BuildRequires:  compface-devel
%endif
BuildRequires:  perl-devel perl-generators perl(ExtUtils::Embed)
BuildRequires:  libSM-devel
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  pkgconfig(dbus-1) >= 0.60
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.60
BuildRequires:  libtool autoconf automake
%if 0%{?build_manual}
BuildRequires:  docbook-utils docbook-utils-pdf
%endif

BuildRequires:  pkgconfig(libcurl)
BuildRequires:  libxml2-devel pkgconfig(expat)
BuildRequires:  libidn-devel
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  libytnef-devel
BuildRequires:  ghostscript
BuildRequires:  pkgconfig(poppler-glib) >= 0.12.0
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(libnotify) >= 0.4.3

%if 0%{?with_python2}
BuildRequires:  python2 python2-devel pygtk2-devel
%endif
%if 0%{?with_python3}
BuildRequires:  python3 python3-devel pkgconfig(pygobject-3.0)
%endif
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.6
BuildRequires:  pkgconfig(libical) >= 2.0

BuildRequires:  gumbo-parser-devel
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(librsvg-2.0) >= 2.39.0
BuildRequires:  pkgconfig(cairo) >= 1.0.0

# for TLS SNI capable libetpan
Requires: libetpan%{?_isa} >= 1.9.2

# Fedora 41 gdk-pixbuf2 has dropped the XPM loader (= "others"),
# so for now there must be an explicit dependency as to avoid missing icons with backtrace
%if 0%{?fedora} > 40
Requires: gdk-pixbuf2-modules-extra%{?_isa}
%endif

# provide plugin api version (see /usr/include/claws-mail/common/version.h)
Provides:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description
Claws Mail is an email client (and news reader), based on GTK+, featuring
quick response, graceful and sophisticated interface, easy configuration,
intuitive operation, abundant features, and extensibility.

%package        devel
Summary:        Development package for %{name}

%description    devel
The %{name}-devel package contains the header files
and pkgconfig file needed for development with %{name}.


%package plugins
Summary: Additional plugins for Claws Mail
Requires: %{name}-plugins-acpi-notifier
Requires: %{name}-plugins-address-keeper
Requires: %{name}-plugins-archive
Requires: %{name}-plugins-att-remover
Requires: %{name}-plugins-attachwarner
Requires: %{name}-plugins-bogofilter
%if !0%{?rhel}
Requires: %{name}-plugins-bsfilter
%endif
Requires: %{name}-plugins-clamd
%if 0%{?with_dillo}
Requires: %{name}-plugins-dillo
%endif
Requires: %{name}-plugins-fancy
Requires: %{name}-plugins-fetchinfo
Requires: %{name}-plugins-libravatar
Requires: %{name}-plugins-litehtml-viewer
Requires: %{name}-plugins-mailmbox
Requires: %{name}-plugins-managesieve
Requires: %{name}-plugins-newmail
Requires: %{name}-plugins-notification
Requires: %{name}-plugins-pdf-viewer
Requires: %{name}-plugins-perl
Requires: %{name}-plugins-pgp
%if 0%{?with_python2}%{?with_python3}
Requires: %{name}-plugins-python
%endif
Requires: %{name}-plugins-rssyl
Requires: %{name}-plugins-smime
Requires: %{name}-plugins-spamassassin
Requires: %{name}-plugins-spam-report
Requires: %{name}-plugins-tnef
Requires: %{name}-plugins-vcalendar

%description plugins
Meta-package to add all additional plugin packages for Claws Mail.


%package plugins-acpi-notifier
Summary:        ACPI notification plugin for Claws Mail 
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-acpi-notifier
Enables mail notification via LEDs on some laptops. Options can be found on
the 'Plugins/Acpi Notifier' page of the preferences.


%package plugins-address-keeper
Summary:        Never forget a typed address in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-address-keeper
This plugin allows saving outgoing addresses to a designated folder
in the address book. Addresses are saved only if not found in the
address book to avoid unwanted duplicates.


%package plugins-archive
Summary:        Archiving features for Claws Mail 
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-archive
%{summary}


%package plugins-attachwarner
Summary:        Attachment warner plugin for Claws Mail 
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-attachwarner
Warns when the user composes a message mentioning an attachment in the message
body but without attaching any files to the message. 


%package plugins-att-remover
Summary:        Attachments remover plugin for Claws Mail 
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-att-remover
Enables the removal of attachments from emails. When right-clicking a message,
choose 'Remove attachments' from the sub-menu.

%package plugins-bogofilter
Summary:        Bogofilter plugin for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
Requires:       bogofilter

%description plugins-bogofilter
%{summary}

%if !0%{?rhel}
%package plugins-bsfilter
Summary:        Bayesian spam filtering for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
Requires:       bsfilter

%description plugins-bsfilter
Bayesian spam filtering for Claws Mail using Bsfilter.
%endif


%package plugins-clamd
Summary:        Use Clam AntiVirus to scan messages in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-clamd
This plugin uses Clam AntiVirus to scan all messages that are
received from an IMAP, LOCAL or POP account.
When a message attachment is found to contain a virus it can be
deleted or saved in a specially designated folder.
Options can be found in /Configuration/Preferences/Plugins/Clam AntiVirus.


%if 0%{?with_dillo}
%package plugins-dillo
Summary:        Display HTML emails in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
Requires:       dillo

%description plugins-dillo
This plugin renders HTML email via the Dillo web browser.
%endif


%package plugins-fancy
Summary:        Display HTML emails in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-fancy
This plugin renders HTML email via the GTK+ port of the WebKit library.


%package plugins-fetchinfo
Summary:        Modify headers of downloaded messages in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-fetchinfo
This plugin inserts headers containing some download information:
UIDL, Sylpheeds account name, POP server, user ID and retrieval time.


%package plugins-keyword_warner
Summary:        Keyword warner plugin for Claws Mail
Requires:	claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-keyword_warner
This plugin shows a warning when sending or queueing a message and a
reference to one or more keywords is found in the message text.


%package plugins-libravatar
Summary:        Libravatar plugin for Claws Mail
Requires:	claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-libravatar
This plugin allows showing the profile picture associated to email
addresses provided by https://www.libravatar.org/. You can read
more about what is this at http://wiki.libravatar.org/description/.


%package plugins-litehtml-viewer
Summary:        LiteHTML plugin for Claws Mail
Requires:	claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-litehtml-viewer
This is an HTML viewer plugin that uses the litehtml to render the
HTML message parts in the Claws Mail message view window. Users of
old Fancy plugin may find this viewer more similar than other HTML
viewer plugins, though you may miss some feature.


%package plugins-mailmbox
Summary:        Add support for mailboxes in mbox format to Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-mailmbox
This plugin provides direct support for mailboxes in mbox format.

%package plugins-managesieve
Summary:        Add Manage sieve support to Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-managesieve
Manage sieve filters on a server using the ManageSieve protocol.

%package plugins-newmail
Summary:        Make Claws Mail write a message header summary to a file
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-newmail
Write a message header summary to a log file (defaults to ~/Mail/NewLog) on
arrival of new mail *after* sorting.


%package plugins-notification
Summary:        Various ways to notify about new messages in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-notification
This plugin collects various ways to notify the user of new (and possibly
unread) mail. Currently, a pop-up and a mail banner are implemented.


%package plugins-pdf-viewer
Summary:        Enables the viewing of PDF and PostScript attachments
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-pdf-viewer
This plugin handles PDF and Postscript attachments.


%package plugins-perl
Summary:        Perl based extended filtering engine for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-perl
This plugin provides an extended filtering engine for the email client
Claws Mail. It allows for the use of full perl power in email filters.

%package plugins-pgp
Summary:        PGP plugin for signing and encrypting with Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
# Fedora 19 required pinentry-gtk as pinentry-qt failed silently #981923
Requires:       pinentry-gui

%description plugins-pgp
%{summary}


%if 0%{?with_python2}%{?with_python3}
%package plugins-python
Summary:        Python scripting access to Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-python
This plugin offers a Python scripting access to Claws Mail. Python code can be
entered interactively into an embedded Python console or stored in scripts
under ~/.claws-mail/python-scripts. The scripts are then accessible via the
menu of the main window.
%endif


%package plugins-rssyl
Summary:        RSS plugin for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-rssyl
Allows you to read your favorite RSS news feeds in Claws Mail. RSS 1.0,
2.0 and Atom feeds are currently supported.


%package plugins-smime
Summary:        S/MIME support for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
Requires:       claws-mail-plugins-pgp%{?_isa} = %{version}-%{release}

%description plugins-smime
This plugin handles S/MIME signed and/or encrypted mails. You can decrypt
mails, verify signatures or sign and encrypt your own mails.


%package plugins-spamassassin
Summary:        Spamassassin plugin for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi
Requires:       spamassassin

%description plugins-spamassassin
%{summary}


%package plugins-spam-report
Summary:        Report spam mail to various places with Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-spam-report
This plugin for Claws Mail can report spam mail to various places.


%package plugins-tnef
Summary:        TNEF message parsing for Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-tnef
This plugin allows reading of application/ms-tnef attachments.


%package plugins-vcalendar
Summary:        Handling of vCalendar messages in Claws Mail
Requires:       claws-mail(plugin-api)%{?_isa} = %pluginapi

%description plugins-vcalendar
This plugin enables vCalendar message handling like that produced by
Evolution or Outlook. It also supports subscribing to remote webCal feeds, and
exporting of your meetings or all your calendars.


%prep
%setup -q

%if 0%{?fedora} > 20
%patch 11 -p1 -b.syscrypto
%endif

# guard for pluginapi
SOURCEAPI=$(grep -A 1 VERSION_NUMERIC src/common/version.h | tr -d '\n' | perl -ne 's/[\\\s]//g; m/(\d+),(\d+),(\d+),(\d+)/; print("$1.$2.$3.$4");')
[ "%pluginapi" == "$SOURCEAPI" ] || exit -1

#cat << EOF > README.Fedora
#Firefox and Claws Mail
#
#    Be sure to set the TMPDIR environment variable, so both applications
#    always use the same directory for temporary files. Else the directory
#    would vary depending on whether or not Claws Mail is launched as mailer
#    from within Firefox. [ https://bugzilla.redhat.com/956380 ]
#EOF


%build
autoreconf -f
%configure --disable-dependency-tracking \
           --disable-rpath \
%if 0%{?rhel}
           --disable-bsfilter-plugin \
%endif
%if 0%{?with_dillo}
           --enable-dillo-plugin \
%else
           --disable-dillo-plugin \
%endif
           --enable-fancy-plugin \
           --enable-litehtml_viewer-plugin \
%if 0%{?with_python2}%{?with_python3}
           --enable-python-plugin \
%else
           --disable-python-plugin \
%endif
           --enable-libetpan

# change DEFAULT_INC_PATH for the optional external "inc" tool to match
# Fedora's "nmh" package // unimportant fix, but add a grep guard, too
sed -i -e 's!\"/usr/bin/mh/inc\"!\"/usr/bin/inc\"!g' src/common/defs.h
grep DEFAULT_INC_PATH src/common/defs.h || exit -1

# avoid relinking with several shared libs used by libperl
# when linking with libperl
grep 'PERL_LDFLAGS *=' configure || exit -1
sed -i 's!\(PERL_LDFLAGS *=\).*$!\1-lperl!g' configure

%if 0%{?with_python2}
# a really ugly hack to have the Python plug-in dlopen the versioned
# run-time lib, with grep guards so we don't need a patch
#
# ensure that the definition exists
grep 'PYTHON_SHARED_LIB=.*\.so\"$' configure || exit -1
# append .1.0
sed -i 's!\(PYTHON_SHARED_LIB=.*\.so\)\"$!\1.1.0\"!' configure
# ensure that the definition no longer ends with .so"
grep 'PYTHON_SHARED_LIB=.*\.so\"$' configure && exit -1
# ensure that the code that uses it is still there
grep 'dlopen.*PYTHON_SHARED_LIB' src/plugins/python/* -R || exit -1
%endif

make %{?_smp_mflags} LIBTOOL=%{_bindir}/libtool

%install
%if 0%{?rhel}
rm -rf %{buildroot}
%endif
export LIBTOOL=%{_bindir}/false
make DESTDIR=%{buildroot} install

%find_lang claws-mail

# use provided desktop file
desktop-file-install \
--add-category="Office" \
--remove-category="GTK" \
--remove-key="Encoding" \
--remove-key="Info" \
--dir=%{buildroot}%{_datadir}/applications \
%{name}.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

rm -f %{buildroot}%{_infodir}/dir

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
find %{buildroot}%{_libdir}/claws-mail/plugins/ -type f -name \
"*.a" -exec rm -f {} ';'

%if 0%{?build_manual}
# we include the manual in the doc section
rm -rf _tmp_manual && mkdir _tmp_manual
mv %{buildroot}%{_datadir}/doc/claws-mail/manual _tmp_manual
rm -f %{buildroot}%{_datadir}/doc/claws-mail/RELEASE_NOTES
%endif

# cleanup non utf8 files
for file in AUTHORS;
do iconv -f iso8859-1 -t utf-8 ${file} > \
 ${file}.conv && mv -f ${file}.conv ${file}
done;

# don't think we need icon-theme.cache
rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache

# set same date on config.h across builds for multilib (#340871)
touch -r NEWS %{buildroot}%{_includedir}/%{name}/config.h


%files -f claws-mail.lang
%license COPYING
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README RELEASE_NOTES
%if 0%{?build_manual}
%doc _tmp_manual/manual
%endif
%{_bindir}/*
%dir %{_libdir}/claws-mail
%dir %{_libdir}/claws-mail/plugins
%dir %{_libdir}/claws-mail/web_extensions
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
#%%{_datadir}/appdata/claws-mail.appdata.xml

%files devel
%{_includedir}/claws-mail/
%{_libdir}/pkgconfig/claws-mail.pc

%files plugins
# meta-package only which pulls in all plugin packages

%files plugins-acpi-notifier
%{_libdir}/claws-mail/plugins/acpi_notifier*

%files plugins-archive
%{_libdir}/claws-mail/plugins/archive*

%files plugins-attachwarner
%{_libdir}/claws-mail/plugins/attachwarner*

%files plugins-address-keeper
%{_libdir}/claws-mail/plugins/address_keeper*

%files plugins-att-remover
%{_libdir}/claws-mail/plugins/att_remover*

%files plugins-bogofilter
%{_libdir}/claws-mail/plugins/bogofilter.so

%if !0%{?rhel}
%files plugins-bsfilter
%{_libdir}/claws-mail/plugins/bsfilter*
%endif

%files plugins-clamd
%{_libdir}/claws-mail/plugins/clamd*

%if 0%{?with_dillo}
%files plugins-dillo
%{_libdir}/claws-mail/plugins/dillo*
%endif

%files plugins-fancy
%{_libdir}/claws-mail/plugins/fancy*
%{_libdir}/claws-mail/web_extensions/fancy*

%files plugins-fetchinfo
%{_libdir}/claws-mail/plugins/fetchinfo*

%files plugins-keyword_warner
%{_libdir}/claws-mail/plugins/keyword_warner*

%files plugins-mailmbox
%{_libdir}/claws-mail/plugins/mailmbox*

%files plugins-managesieve
%{_libdir}/claws-mail/plugins/managesieve.so

%files plugins-newmail
%{_libdir}/claws-mail/plugins/newmail.so

%files plugins-notification
%{_libdir}/claws-mail/plugins/notification.so

%files plugins-pdf-viewer
%{_libdir}/claws-mail/plugins/pdf_viewer.so

%files plugins-perl
%{_libdir}/claws-mail/plugins/perl.so

%files plugins-pgp
%{_libdir}/claws-mail/plugins/pgp*.so
%{_libdir}/claws-mail/plugins/pgp*.deps

%if 0%{?with_python2}%{?with_python3}
%files plugins-python
%{_libdir}/claws-mail/plugins/python*
%endif

%files plugins-libravatar
%{_libdir}/claws-mail/plugins/libravatar*

%files plugins-litehtml-viewer
%{_libdir}/claws-mail/plugins/litehtml_viewer*

%files plugins-rssyl
%{_libdir}/claws-mail/plugins/rssyl*

%files plugins-smime
%{_libdir}/claws-mail/plugins/smime.so
%{_libdir}/claws-mail/plugins/smime.deps

%files plugins-spamassassin
%{_libdir}/claws-mail/plugins/spamassassin.so

%files plugins-spam-report
%{_libdir}/claws-mail/plugins/spamreport.so

%files plugins-tnef
%{_libdir}/claws-mail/plugins/tnef*

%files plugins-vcalendar
%{_libdir}/claws-mail/plugins/vcalendar*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 15 2024 Michael Schwendt <mschwendt@fedoraproject.org> - 4.3.0-6
- require new gdk-pixbuf2-modules-extra package (arch-specific), since
  Fedora 41 gdk-pixbuf2 has dropped the XPM loader (= "others") suddenly,
  which causes missing icons and an intercepted backtrace

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3.0-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 4.3.0-3
- Perl 5.40 rebuild

* Tue Jun 11 2024 Python Maint <python-maint@redhat.com> - 4.3.0-2
- Rebuilt for Python 3.13

* Mon Jun 10 2024 Michael Schwendt <mschwendt@fedoraproject.org> - 4.3.0-1
- Upgrade to 4.3.0.

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.2.0-5
- Rebuilt for Python 3.13

* Fri Mar 01 2024 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.2.0-4
- Rebuild against gumbo-parser-0.12.1.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Michael Schwendt <mschwendt@fedoraproject.org> - 4.2.0-1
- Upgrade to 4.2.0.
- Remove obsolete patches.
- Remove and obsolete -gdata plugin.
- Trim changelog section by a few years.
- Update web_extensions dir entry to new location.
- libgumbo 0.12 (gumbo-parser) does not exist in Fedora yet -> bug 2245541
- New configure script explicitly searches also for webkit2gtk4.1
- Merge new Source URL and webkit pkgconfig BR from PR #5

* Sat Nov  4 2023 Michael Schwendt <mschwendt@fedoraproject.org>
- update webkit2gtk3-devel BR to webkit2gtk4.0-devel since it's been
  a virtual Provides for some time anyway

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 4.1.1-8
- Perl 5.38 rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 4.1.1-7
- Rebuilt for Python 3.12

* Tue May  2 2023 Michael Schwendt <mschwendt@fedoraproject.org> - 4.1.1-5
- Merge upstream fix for bug 4670,
  'To/CC incorrectly escaped with a trailing backslash'
