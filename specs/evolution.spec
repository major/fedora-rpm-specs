%undefine __cmake_in_source_build

%global _changelog_trimtime %(date +%s -d "1 year ago")
%global _python_bytecompile_extra 0

# correct Obsoletes for evolution-tests when this is changed
%global enable_installed_tests 0

%global tnef_support 0
%if 0%{?fedora}
%global tnef_support 1
%endif

%define glib2_version 2.66
%define gtk3_version 3.22
%define gnome_autoar_version 0.1.1
%define gnome_desktop_version 2.91.3
%define intltool_version 0.35.5
%define libgweather_version 3.91
%define geocode_glib_version 3.26.3
%define sqlite_version 3.7.17
%define libsoup_version 3.1.1
%define webkit2gtk_version 2.34.0

%define last_anjal_version 0.3.2-3
%define last_libgal2_version 2:2.5.3-2
%define last_evo_nm_version 3.5.0
%define last_evo_perl_version 3.21.90

%define ldap_support 1
%define libnotify_support 1
%define libpst_support 1

# Coverity scan can override this to 0, to skip checking in gtk-doc generated code
%{!?with_docs: %global with_docs 1}

%if 0%{?flatpak}
%global with_docs 0
%endif

%define evo_plugin_dir %{_libdir}/evolution/plugins

### Abstract ###

Name: evolution
Version: 3.57.2
Release: 1%{?dist}
Summary: Mail and calendar client for GNOME
License: GPL-2.0-or-later AND GFDL-1.3-or-later
URL: https://gitlab.gnome.org/GNOME/evolution/-/wikis/home
Source: http://download.gnome.org/sources/%{name}/3.57/%{name}-%{version}.tar.xz
Source1: flatpak-evolution-fix-service-names.sh
Source2: flatpak-evolution-wrapper.sh.in

# 0-99: General patches
# enable corresponding autopatch below to make them applied

# 100-199: Flatpak-specific patches
# https://gitlab.gnome.org/GNOME/evolution-data-server/-/merge_requests/144
Patch100: configurable-dbus-prefix.patch

# Approximate version number
Provides: bundled(libgnomecanvas) = 2.30.0

Obsoletes: anjal <= %{last_anjal_version}
Obsoletes: libgal2 <= %{last_libgal2_version}
Obsoletes: evolution-NetworkManager < %{last_evo_nm_version}
Obsoletes: evolution-perl < %{last_evo_perl_version}
Obsoletes: evolution-rss < 3.45.2

%if !%{enable_installed_tests}
Obsoletes: evolution-tests <= 3.31.1
%endif

%global eds_version %{version}

## Dependencies ###

%if ! 0%{?flatpak}
Requires: %{_bindir}/killall
Requires: gvfs
%endif
Requires: evolution-data-server >= %{eds_version}
Requires: gspell
Requires: highlight
Requires: %{name}-langpacks = %{version}-%{release}

### Build Dependencies ###

%if ! 0%{?flatpak}
BuildRequires: %{_bindir}/killall
%endif
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gettext
%if %{with_docs}
BuildRequires: gtk-doc
%endif
BuildRequires: highlight
BuildRequires: intltool >= %{intltool_version}
BuildRequires: itstool
BuildRequires: pkgconfig
BuildRequires: yelp-tools

BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(camel-1.2) >= %{eds_version}
BuildRequires: pkgconfig(enchant-2)
BuildRequires: pkgconfig(gail-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gmodule-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gnome-autoar-0) >= %{gnome_autoar_version}
BuildRequires: pkgconfig(gnome-autoar-gtk-0) >= %{gnome_autoar_version}
BuildRequires: pkgconfig(gnome-desktop-3.0) >= %{gnome_desktop_version}
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(gspell-1)
BuildRequires: pkgconfig(gweather4) >= %{libgweather_version}
BuildRequires: pkgconfig(geocode-glib-2.0) >= %{geocode_glib_version}
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(libcmark)
BuildRequires: pkgconfig(libebackend-1.2) >= %{eds_version}
BuildRequires: pkgconfig(libebook-1.2) >= %{eds_version}
BuildRequires: pkgconfig(libecal-2.0) >= %{eds_version}
BuildRequires: pkgconfig(libedataserver-1.2) >= %{eds_version}
BuildRequires: pkgconfig(libedataserverui-1.2) >= %{eds_version}
BuildRequires: pkgconfig(libsoup-3.0) >= %{libsoup_version}
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(nspr)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(sqlite3) >= %{sqlite_version}
BuildRequires: pkgconfig(webkit2gtk-4.1) >= %{webkit2gtk_version}
BuildRequires: pkgconfig(webkit2gtk-web-extension-4.1) >= %{webkit2gtk_version}

%if %{tnef_support}
BuildRequires: pkgconfig(libytnef)
%endif

%if %{ldap_support}
BuildRequires: openldap-devel >= 2.0.11
%endif

%if %{libnotify_support}
BuildRequires: pkgconfig(libnotify)
%endif

%if %{libpst_support}
BuildRequires: pkgconfig(libpst)
%endif

%description
Evolution is the GNOME mailer, calendar, contact manager and
communications tool.  The components which make up Evolution
are tightly integrated with one another and act as a seamless
personal information-management tool.

%package devel
Summary: Development files for building against %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig(camel-1.2) >= %{eds_version}
Requires: pkgconfig(enchant-2)
Requires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
Requires: pkgconfig(gspell-1)
Requires: pkgconfig(gweather4) >= %{libgweather_version}
Requires: pkgconfig(libebackend-1.2) >= %{eds_version}
Requires: pkgconfig(libebook-1.2) >= %{eds_version}
Requires: pkgconfig(libecal-2.0) >= %{eds_version}
Requires: pkgconfig(libedataserver-1.2) >= %{eds_version}
Requires: pkgconfig(libsoup-3.0) >= %{libsoup_version}
Requires: pkgconfig(libxml-2.0)
Obsoletes: libgal2-devel <= %{last_libgal2_version}

%description devel
Development files needed for building things which link against %{name}.

%if %{with_docs}

%package devel-docs
Summary: Developer documentation for Evolution
Requires: devhelp
Requires: %{name}-devel = %{version}-%{release}
BuildArch: noarch

%description devel-docs
This package contains developer documentation for Evolution.

%endif

%package langpacks
Summary: Translations for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description langpacks
This package contains translations for %{name}.

%if %{with_docs}
%package help
Summary: Help files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: yelp
BuildArch: noarch

%description help
This package contains user documentation for %{name}.
%endif

%package bogofilter
Summary: Bogofilter plugin for Evolution
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: bogofilter

%description bogofilter
This package contains the plugin to filter junk mail using Bogofilter.

%package spamassassin
Summary: SpamAssassin plugin for Evolution
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: spamassassin

%description spamassassin
This package contains the plugin to filter junk mail using SpamAssassin.

%if %{libpst_support}
%package pst
Summary: PST importer plugin for Evolution
Requires: %{name}%{?_isa} = %{version}-%{release}

%description pst
This package contains the plugin to import Microsoft Personal Storage Table
(PST) files used by Microsoft Outlook and Microsoft Exchange.
%endif

%if %{enable_installed_tests}
%package tests
Summary: Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python2-behave
Requires: python2-dogtail

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.
%endif

%prep
%autosetup -p1 -S gendiff -N

# General patches
# %%autopatch -p1 -m 0 -M 99

# Flatpak-specific patches
%if 0%{?flatpak}
%autopatch -p1 -m 100 -M 199
%endif

# Remove the welcome email from Novell
for inbox in src/mail/default/*/Inbox; do
  echo -n "" > $inbox
done

%if 0%{?flatpak}
mv data/org.gnome.Evolution.desktop.in.in data/org.gnome.Evolution.desktop.in.i
cat data/org.gnome.Evolution.desktop.in.i | sed -e "s/Icon=evolution/Icon=org.gnome.Evolution/" >data/org.gnome.Evolution.desktop.in.in
%endif

%build

# define all of our flags, this is kind of ugly :(
%if %{ldap_support}
%define ldap_flags -DWITH_OPENLDAP=ON
%else
%define ldap_flags -DWITH_OPENLDAP=OFF
%endif

%define ssl_flags -DENABLE_SMIME=ON

if ! pkg-config --exists nss; then
  echo "Unable to find suitable version of mozilla nss to use!"
  exit 1
fi

%if %{with_docs}
%define gtkdoc_flags -DENABLE_GTK_DOC=ON -DWITH_HELP=ON
%else
%define gtkdoc_flags -DENABLE_GTK_DOC=OFF -DWITH_HELP=OFF
%endif

%if %{enable_installed_tests}
%define tests_flags -DENABLE_INSTALLED_TESTS=ON
%else
%define tests_flags -DENABLE_INSTALLED_TESTS=OFF
%endif

%if %{tnef_support}
%global tnef_flags -DENABLE_YTNEF=ON
%else
%global tnef_flags -DENABLE_YTNEF=OFF
%endif

%if 0%{?flatpak}
%global temp_home "-DTEMP_HOME=1"
%else
%global temp_home ""
%endif

CFLAGS="$RPM_OPT_FLAGS -fPIC -DLDAP_DEPRECATED -Wno-sign-compare -Wno-deprecated-declarations %temp_home"
export CFLAGS

%cmake -DENABLE_MAINTAINER_MODE=OFF \
	-DVERSION_SUBSTRING=" (%{version}-%{release})" \
	%ldap_flags %ssl_flags %gtkdoc_flags %tests_flags %tnef_flags \
	-DENABLE_PLUGINS=all \
	%if 0%{?flatpak}
	"-DWITH_WMCLASS_OVERRIDE=evolution.bin" \
	%endif
	-DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
	-DLIB_INSTALL_DIR:PATH=%{_libdir} \
	-DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
	-DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
	%if "%{?_lib}" == "lib64"
		-DLIB_SUFFIX=64 \
	%endif
	%{nil}

%cmake_build

%if %{with_docs}

# Replace identical images in the help by links.
# This reduces the RPM size by several megabytes.
helpdir=$RPM_BUILD_ROOT%{_datadir}/gnome/help/%{name}
for f in $helpdir/C/figures/*.png; do
  b="$(basename $f)"
  for d in $helpdir/*; do
    if [ -d "$d" -a "$d" != "$helpdir/C" ]; then
      g="$d/figures/$b"
      if [ -f "$g" ]; then
        if cmp -s $f $g; then
          rm "$g"; ln -s "../../C/figures/$b" "$g"
        fi
      fi
    fi
  done
done

# %%{with_docs}
%endif

%install
%cmake_install

%if 0%{?flatpak}
%{S:1} <%{S:2} >flatpak-evolution-wrapper.sh
chmod a+x flatpak-evolution-wrapper.sh
mv $RPM_BUILD_ROOT%{_bindir}/evolution $RPM_BUILD_ROOT%{_bindir}/evolution.bin
cp flatpak-evolution-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/evolution
%endif

%find_lang evolution --all-name --with-gnome

grep "%{_datadir}/locale" evolution.lang > translations.lang
%if %{with_docs}
grep -v "%{_datadir}/locale" evolution.lang > help.lang
%endif

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_mandir}/man1/*

# GSettings schemas:
%{_datadir}/GConf/gsettings/evolution.convert

%{_datadir}/glib-2.0/schemas/org.gnome.evolution.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.shell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.addressbook.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.calendar.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.mail.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.importer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.bogofilter.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.spamassassin.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.text-highlight.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.attachment-reminder.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.autocontacts.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.email-custom-header.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.external-editor.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.face-picture.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.itip.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.mail-notification.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.prefer-plain.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.publish-calendar.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.sender-validator.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.templates.gschema.xml

# The main executable
%{_bindir}/evolution

%if 0%{?flatpak}
%{_bindir}/evolution.bin
%endif

%{_datadir}/metainfo/org.gnome.Evolution.metainfo.xml

# Desktop files:
%{_datadir}/applications/org.gnome.Evolution.desktop

# Icons:
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*

# The main data directory
# (have not attempted to split this up into an explicit list)
%dir %{_datadir}/evolution
%{_datadir}/evolution

# Modules:
%dir %{_libdir}/evolution
%dir %{_libdir}/evolution/modules
%{_libdir}/evolution/modules/module-accounts-window.so
%{_libdir}/evolution/modules/module-addressbook.so
%{_libdir}/evolution/modules/module-appearance-settings.so
%{_libdir}/evolution/modules/module-backup-restore.so
%{_libdir}/evolution/modules/module-book-config-carddav.so
%{_libdir}/evolution/modules/module-book-config-google.so
%{_libdir}/evolution/modules/module-book-config-ldap.so
%{_libdir}/evolution/modules/module-book-config-local.so
%{_libdir}/evolution/modules/module-cal-config-caldav.so
%{_libdir}/evolution/modules/module-cal-config-contacts.so
%{_libdir}/evolution/modules/module-cal-config-google.so
%{_libdir}/evolution/modules/module-cal-config-local.so
%{_libdir}/evolution/modules/module-cal-config-weather.so
%{_libdir}/evolution/modules/module-cal-config-webcal.so
%{_libdir}/evolution/modules/module-cal-config-webdav-notes.so
%{_libdir}/evolution/modules/module-calendar.so
%{_libdir}/evolution/modules/module-composer-autosave.so
%{_libdir}/evolution/modules/module-composer-to-meeting.so
%{_libdir}/evolution/modules/module-config-lookup.so
%{_libdir}/evolution/modules/module-contact-photos.so
%{_libdir}/evolution/modules/module-gravatar.so
%{_libdir}/evolution/modules/module-itip-formatter.so
%{_libdir}/evolution/modules/module-mail-config.so
%{_libdir}/evolution/modules/module-mail.so
%{_libdir}/evolution/modules/module-mailto-handler.so
%{_libdir}/evolution/modules/module-mdn.so
%{_libdir}/evolution/modules/module-offline-alert.so
%{_libdir}/evolution/modules/module-prefer-plain.so
%{_libdir}/evolution/modules/module-plugin-lib.so
%{_libdir}/evolution/modules/module-plugin-manager.so
%{_libdir}/evolution/modules/module-rss.so
%{_libdir}/evolution/modules/module-settings.so
%{_libdir}/evolution/modules/module-startup-wizard.so
%{_libdir}/evolution/modules/module-text-highlight.so
%{_libdir}/evolution/modules/module-vcard-inline.so
%{_libdir}/evolution/modules/module-webkit-editor.so
%{_libdir}/evolution/modules/module-webkit-inspector.so

%if %{tnef_support}
%{_libdir}/evolution/modules/module-tnef-attachment.so
%endif

%{_libdir}/evolution-data-server/camel-providers/libcamelrss.so
%{_libdir}/evolution-data-server/camel-providers/libcamelrss.urls
%{_libdir}/evolution-data-server/ui-modules/module-evolution-alarm-notify.so

# Shared libraries:
%{_libdir}/evolution/libevolution-mail-composer.so
%{_libdir}/evolution/libeabutil.so
%{_libdir}/evolution/libeabwidgets.so
%{_libdir}/evolution/libecontacteditor.so
%{_libdir}/evolution/libecontactlisteditor.so
%{_libdir}/evolution/libecontactprint.so
%{_libdir}/evolution/libemail-engine.so
%{_libdir}/evolution/libevolution-mail-formatter.so
%{_libdir}/evolution/libevolution-shell.so
%{_libdir}/evolution/libessmime.so
%{_libdir}/evolution/libevolution-util.so
%{_libdir}/evolution/libevolution-addressbook-importers.so
%{_libdir}/evolution/libevolution-calendar.so
%{_libdir}/evolution/libevolution-calendar-importers.so
%{_libdir}/evolution/libevolution-mail-importers.so
%{_libdir}/evolution/libevolution-mail.so
%{_libdir}/evolution/libevolution-rss-common.so
%{_libdir}/evolution/libevolution-smime.so
%{_libdir}/evolution/libgnomecanvas.so

# WebKit2 Extensions
%{_libdir}/evolution/web-extensions/libewebextension.so
%{_libdir}/evolution/web-extensions/webkit-editor/module-webkit-editor-webextension.so

# Various libexec programs:
%dir %{_libexecdir}/evolution
%{_libexecdir}/evolution/evolution-backup
%{_libexecdir}/evolution/killev

# The plugin directory:
%dir %{evo_plugin_dir}

# The various plugins follow; they are all part of the main package:
# (note that there are various resources such as ui and pixmap files that
# are built as part of specific plugins but which are currently packaged using
# globs above; the purpose of the separation below is to be more explicit about
# which plugins we ship)
%{evo_plugin_dir}/org-gnome-evolution-attachment-reminder.eplug
%{evo_plugin_dir}/liborg-gnome-evolution-attachment-reminder.so

%{evo_plugin_dir}/org-gnome-email-custom-header.eplug
%{evo_plugin_dir}/liborg-gnome-email-custom-header.so

%{evo_plugin_dir}/org-gnome-evolution-bbdb.eplug
%{evo_plugin_dir}/liborg-gnome-evolution-bbdb.so

%{evo_plugin_dir}/org-gnome-external-editor.eplug
%{evo_plugin_dir}/liborg-gnome-external-editor.so

%{evo_plugin_dir}/org-gnome-face.eplug
%{evo_plugin_dir}/liborg-gnome-face.so

%{evo_plugin_dir}/org-gnome-mailing-list-actions.eplug
%{evo_plugin_dir}/liborg-gnome-mailing-list-actions.so

%{evo_plugin_dir}/org-gnome-mail-notification.eplug
%{evo_plugin_dir}/liborg-gnome-mail-notification.so

%{evo_plugin_dir}/org-gnome-mail-to-task.eplug
%{evo_plugin_dir}/liborg-gnome-mail-to-task.so

%{evo_plugin_dir}/org-gnome-prefer-plain.eplug
%{evo_plugin_dir}/liborg-gnome-prefer-plain.so

%{evo_plugin_dir}/org-gnome-publish-calendar.eplug
%{evo_plugin_dir}/liborg-gnome-publish-calendar.so

%{evo_plugin_dir}/org-gnome-save-calendar.eplug
%{evo_plugin_dir}/liborg-gnome-save-calendar.so

%{evo_plugin_dir}/org-gnome-evolution-sender-validation.eplug
%{evo_plugin_dir}/liborg-gnome-evolution-sender-validation.so

%{evo_plugin_dir}/org-gnome-templates.eplug
%{evo_plugin_dir}/liborg-gnome-templates.so

%{evo_plugin_dir}/org-gnome-dbx-import.eplug
%{evo_plugin_dir}/liborg-gnome-dbx-import.so


%files devel
%{_includedir}/evolution
%{_libdir}/pkgconfig/evolution-calendar-3.0.pc
%{_libdir}/pkgconfig/evolution-mail-3.0.pc
%{_libdir}/pkgconfig/evolution-shell-3.0.pc
%{_libdir}/pkgconfig/libemail-engine.pc

%if %{with_docs}

%files devel-docs
%doc %{_datadir}/gtk-doc/html/evolution-mail-composer
%doc %{_datadir}/gtk-doc/html/evolution-mail-engine
%doc %{_datadir}/gtk-doc/html/evolution-mail-formatter
%doc %{_datadir}/gtk-doc/html/evolution-shell
%doc %{_datadir}/gtk-doc/html/evolution-util

%endif

%files langpacks -f translations.lang

%if %{with_docs}
%files help -f help.lang
%endif

%files bogofilter
%{_libdir}/evolution/modules/module-bogofilter.so
%{_datadir}/metainfo/org.gnome.Evolution-bogofilter.metainfo.xml

%files spamassassin
%{_libdir}/evolution/modules/module-spamassassin.so
%{_datadir}/metainfo/org.gnome.Evolution-spamassassin.metainfo.xml

%if %{libpst_support}
%files pst
%{_datadir}/metainfo/org.gnome.Evolution-pst.metainfo.xml
%{evo_plugin_dir}/org-gnome-pst-import.eplug
%{evo_plugin_dir}/liborg-gnome-pst-import.so
%endif

%if %{enable_installed_tests}
%files tests
%{_libexecdir}/%{name}/installed-tests
%{_datadir}/installed-tests
%endif

%changelog
%autochangelog
