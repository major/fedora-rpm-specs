%global appname com.github.alecaddd.sequeler

Name:           sequeler
Summary:        Friendly SQL Client
Version:        0.8.2
Release:        %autorelease
# The entire source is GPLv3+ (the LICENSE file is GPLv3, and both
# data/com.github.alecaddd.sequeler.appdata.xml.in.in and debian/copyright
# indicate GPLv3+ is intended), except:
#   - the Vala sources (all .vala files under src/ or its subdirectories),
#     which are GPLv2+
#   - vapi/linux.vapi, which is LGPLv2+
#   - data/com.github.alecaddd.sequeler.appdata.xml.in.in, which is CC0.
# This results in an effective license of GPLv3+.
License:        GPLv3+

URL:            https://github.com/Alecaddd/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gcc

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libgda-5.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       hicolor-icon-theme

Recommends:     libgda-mysql
Recommends:     libgda-postgres
Recommends:     libgda-sqlite

Summary(de):    Benutzerfreundlicher SQL-Client
Summary(fr):    Un simple client SQL
Summary(lt):    Draugiška SQL kliento programa

%description
Easily connect to your local or remote database.

Store your Database Connections in the library, connect over SSH tunnel, type
and execute SQL commands directly in the app, and do everything you need to do
without the necessity of opening the terminal.

Supported Databases:
  • SQLite
  • MySQL
  • MariaDB
  • PostgreSQL

Features Include:
  • Test Connections before saving them
  • View Table structure, content, and relations
  • Write multiple custom SQL Queries
  • Switch between light and dark mode
  • Handy keyboard shortcuts to quit (ctrl+q), create new connection
    (ctrl+shift+n), open a new window (ctrl+n)

%description -l de
Verbinden Sie sich mit einer beliebigen lokalen oder externen Datenbank.

Speichern Sie Ihre Datenbankverbindungen in der integrierten Bibliothek, führen
Sie SQL-Befehle direkt in der Anwendung aus, und tun Sie alles, was Sie tun
müssen, ohne das Terminal öffnen zu müssen.

  • SQLite
  • MySQL
  • MariaDB
  • PostgreSQL

Zu den Funktionen gehören:
  • Verbindung vor dem Speichern testen
  • Anzeigen von Tabellenstruktur, Inhalt und Beziehungen
  • Mehrere benutzerdefinierte SQL-Abfragen schreiben
  • Zwischen dem hellen und dunklen Modus umschalten
  • Tastenkombinationen zum Beenden (Strg+q), Erstellen einer neuen Verbindung
    (Strg+Shift+n), mehrere Instanzen (Strg+n)

%description -l fr
Connectez-vous facilement à une base de données locale ou distante.

Stockez vos connexions de base de données dans la bibliothèque intégrée, tapez
et exécutez les commandes SQL directement dans l’application, et faites tout ce
dont vous avez besoin pour vous passer la nécessité d’ouvrir le terminal.

  • SQLite
  • MySQL
  • MariaDB
  • PostgreSQL

Fonctionnalités incluses :
  • Tester les connexions avant de les enregistrer
  • Voir la structure, le contenu et les relations des tables
  • Écrire plusieurs requêtes SQL personnalisées
  • Changer entre le thème clair et le thème sombre
  • Raccourcis clavier pour quitter (Ctrl+Q), créer une nouvelle
    connexion(Ctrl+Maj+N), Ouvrir une nouvelle instance (Ctrl+N)

%description -l lt
Lengvai prisijunkite prie bet kurios vietinės ar nuotolinės duomenų bazės.

Laikykite savo duomenų bazių ryšius įtaisytoje bibliotekoje, tiesiogiai
programoje rašykite ir vykdykite SQL komandas ir atlikite viską, ką reikia be
būtinybės atverti terminalą.

  • SQLite
  • MySQL
  • MariaDB
  • PostgreSQL

Ypatybės:
  • Prieš įrašant ryšius, juos išbandyti
  • Rodyti lentelės struktūrą, turinį ir sąsajos ryšius
  • Rašyti keletą tinkintų SQL užklausų
  • Perjungti tarp šviesios ir tamsios veiksenos
  • Patogūs klaviatūros susiejimai, norint išeiti (ctrl (vald)+q), sukurti
    naują ryšį (ctrl (vald)+shift (lyg2)+n), keli egzemplioriai (ctrl (vald)+n)


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml
# Matches what gnome-software and others use:
appstreamcli validate --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc AUTHORS README.md
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/*/%{appname}.svg
%{_datadir}/icons/hicolor/{16x16,24x24}/{actions,status}/*.svg
%{_metainfodir}/%{appname}.appdata.xml


%changelog
%autochangelog
