%global app_id io.github.lainsce.Notejot

Name:           notejot
Summary:        Jot your ideas
Version:        3.5.1
Release:        %autorelease
# The entire source is GPLv3+, except:
#   src/Widgets/NoteTheme.vala
#   src/Widgets/MoveToDialog.vala
#   src/Widgets/EditNotebookDialog.vala
# which are GPLv2+; and
#   data/io.github.lainsce.Notejot.metainfo.xml.in
# which is CC0. This results in an effective license of GPLv3+.
License:        GPLv3+

URL:            https://github.com/lainsce/notejot
Source0:        %{url}/archive/%{version}/notejot-%{version}.tar.gz

# Add <launchable/> tag to AppStream metadata
#
# https://www.freedesktop.org/software/appstream/docs/chap-Quickstart.html#qsr-app-launchable-info
#
# Omitting this tag now now triggers a hard validation error in “appstreamcli
# validate”:
#
# https://github.com/ximion/appstream/commit/ad98bfd8db789c80507e82278d6d766acba4937c
Patch:          %{url}/pull/380.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
# When available, it is also used by upstream tests.
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gcc

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)

Requires:       hicolor-icon-theme

Summary(cs):    Zapiš si své nápady
Summary(da):    Notér dine ideer
Summary(de_DE): Notieren Sie Ihre Ideen
Summary(es):    Anota sus ideas
Summary(fr):    Notez vos idées
Summary(gl):    Apunte as súas ideas
Summary(hr):    Zapiši svoje ideje
Summary(it):    Annota le tue idee
Summary(ja):    アイデアを書き留めよう！
Summary(lt):    Greitai užsirašykite savo idėjas
Summary(nl):    Noteer je ideeën
Summary(pl):    Notuj swoje pomysły
Summary(pt_BR): Anote suas ideias
Summary(pt):    Anote as suas ideias
Summary(ru):    Запишите ваши идеи
Summary(sv):    Skriv ner dina idéer


%description
A stupidly-simple notes application for any type of short term notes or ideas.

  • 🟡 Color your notes in 8 different colors
  • 📓 Classify them in notebooks
  • 🔤 Format text to your liking
  • 📌 Pin your most important ones

%description -l cs
Velice jednoduchá poznámková aplikace pro každý typ poznámek nebo nápadů.

  • 🟡 Obarvěte si své poznámky až 8 různými barvami
  • 📓 Roztřiďte si je do zápisníků
  • 🔤 Naformátujte si text podle sebe
  • 📌 Připni si ty nejdůležitější

%description -l da
En simpel post-it note applikation for enhver type af korttids tanker eller
ideer.

%description -l de-DE
Eine total einfache Notizen-Anwendung für so ziemlich jede Art von kleinen
Notizen oder Ideen.

%description -l es
Una aplicación de notas estúpidamente simple para cualquier tipo de notas o
ideas a corto plazo.

  • 🟡 Coloree sus notas en 8 colores diferentes
  • 📓 Clasifíquelas en cuadernos
  • 🔤 Formatee a su gusto
  • 📌 Fije sus notas más importantes

%description -l fr
Une application de notes très simple pour tout type de notes ou d’idées à court
terme.

  • 🟡 Colorez vos notes avec 8 coleurs différentes
  • 📓 Rangez les dans des carnets de notes
  • 🔤 Formatez le texte comme vous le préferez
  • 📌 Épinglez vos notes les plus importantes

%description -l gl
Un aplicativo de notas sinxelo para calquera tipo de notas ou ideas a curto
prazo.

%description -l hr
Jednostavan program za zapisivanje bilježaka bilo koje vrste ili ideja.

  • 🟡 Oboji bilješke u osam raznih boja
  • 📓 Klasificiraj ih u bilježnicama
  • 🔤 Formatiraj tekst po volji
  • 📌 Prikvači svoje najvažnije bilješke

%description -l it
Un’applicazione di note adesive stupidamente semplice per qualsiasi tipo di
note a breve termine o idee.

  • 🟡 Colora le tue note in 8 colori diversi
  • 📓 Classificali nei taccuini
  • 🔤 Formatta il testo a tuo piacimento
  • 📌 Appunta i tuoi più importanti

%description -l ja
超シンプルなメモアプリです。

%description -l lt
Kvailai paprasti lipnūs užrašai bet kokio tipo trumpoms pastaboms ar idėjoms.

%description -l nl
Een doodeenvoudige notitietoepassing voor het opschrijven van korte notities of
ideeën.

  • 🟡 Voorzie je notities van een kleur (8 verschillende om uit te kiezen)
  • 📓 Deel ze op in notitieboeken
  • 🔤 Gebruik alle tekstopmaak die je maar wilt
  • 📌 Zet de belangrijkste bovenaan

%description -l pl
Głupio prosta aplikacja do notowania różnych krótkoterminowych notatek lub
pomysłów.

%description -l pt_BR
Um aplicativo estupidamente simples para qualquer tipo de notas curtas ou
idéias.

  • 🟡 Pinte suas notas com 8 cores diferentes
  • 📓 Classifique-as em cadernos
  • 🔤 Formate o texto como quiser
  • 📌 Fixe as mais importantes

%description -l pt
Uma aplicação estupidamente simples de notas aderentes para qualquer tipo
de notas a curto prazo ou ideias.

%description -l ru
Невероятно простое приложение для любого типа быстрых заметок или идей.

  • 🟡 Разукрасьте свои заметки в 8 разных цветов
  • 📓 Классифицируйте их в блокнотах
  • 🔤 Отформатируйте текст по своему вкусу
  • 📌 Закрепите самые важные из них

%description -l sv
Ett löjligt enkelt anteckningsprogram för alla typer av kortvariga anteckningar
eller idéer.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{app_id}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{app_id}.desktop

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{app_id}.metainfo.xml
# Matches what gnome-software and others use:
appstreamcli validate --nonet \
    %{buildroot}/%{_metainfodir}/%{app_id}.metainfo.xml


%files -f %{app_id}.lang
%doc README.md
%license LICENSE

%{_bindir}/%{app_id}

%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/icons/hicolor/*/actions/*.svg
%{_metainfodir}/%{app_id}.metainfo.xml


%changelog
%autochangelog
