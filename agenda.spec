%global app_id com.github.dahenson.agenda

Name:           agenda
Summary:        A simple, slick, speedy and no-nonsense task manager
Version:        1.1.2
Release:        %autorelease
# The entire source is GPL-3.0-or-later, except:
#   - data/Agenda.css is GPL-2.0-or-later; it is not installed directly, but is
#     incorporated in the executable as a “resource”
#   - data/com.github.dahenson.agenda.appdata.xml.in is CC0-1.0, which is
#     allowed for content only
#
# Additionally, the following do not affect the License because they are not
# part of the binary RPM:
#
#   - test/TestCase.vala is LGPL-2.0-or-later
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND CC0-1.0

URL:            https://github.com/dahenson/agenda
Source:         %{url}/archive/%{version}/agenda-%{version}.tar.gz

# Add <launchable/> tag to AppStream metadata
# https://github.com/dahenson/agenda/pull/148
#
# https://www.freedesktop.org/software/appstream/docs/chap-Quickstart.html#qsr-app-launchable-info
#
# Omitting this tag now now triggers a hard validation error in “appstreamcli
# validate”:
#
# https://github.com/ximion/appstream/commit/ad98bfd8db789c80507e82278d6d766acba4937c
Patch:          0001-Add-launchable-tag-to-AppStream-metadata.patch
# Convert homepage link from HTTP to HTTPS in AppData XML
# https://github.com/dahenson/agenda/pull/152/commits/39bd498e8959e14e6a3ac7530ae49eb71aa91599
#
# From:
#
# Convert HTTP links to HTTPS
# https://github.com/dahenson/agenda/pull/152
#
# Rebased on 1.1.2 and on top of PR#148
Patch:          0002-Convert-homepage-link-from-HTTP-to-HTTPS-in-AppData-.patch
# Fix deprecated top-level developer_name in AppData XML
# https://github.com/dahenson/agenda/pull/151
#
# Rebased on 1.1.2 and on top of PR#148 and PR#152
Patch:          0003-Fix-deprecated-top-level-developer_name-in-AppData-X.patch
Patch:          0004-Add-a-developer-ID-in-AppData-XML.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

BuildRequires:  hardlink

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gcc

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme

Summary(ca):    Un gestor de tasques fàcil d’utilitzar
Summary(de):    Ein einfacher, handlicher, schneller und nützlicher Aufgaben Verwalter
Summary(es):    Un administrador de tareas simple, pulido, rápido y sin complicaciones
Summary(fr):    Un gestionnaire de tâches simple, rapide et élégant
Summary(gl):    Un xestor de tarefas pulido, sinxelo, rápido e sen complicacións
Summary(it):    Un promemoria semplice, elegante, veloce e senza fronzoli
Summary(ja):    タスクを完了しましょう
Summary(ka):    მარტივი, მოხერხებული, სწრაფი დავალებების მმართველი ყოველგვარი უაზრობების გარეშე
Summary(ko):    간단하고 미려한 일정 관리자
Summary(lt):    Paprasta, vikri, greita, dalykiška užduočių tvarkytuvė
Summary(ms):    Pengurus tugas yang ringkas dan pantas
# This translation is for the alternative summary, “Get things done”
Summary(nl):    Rond taken af
Summary(pl):    Prosty, gładki, szybki i niebezsensowny menedżer zadań
Summary(pt):    Um gestor de tarefas simples, liso, rápido e sem falhas
Summary(ru):    Простой и быстрый менеджер задач
Summary(sr):    Једноставан, гладак, брз и без којештарија управник задатака
Summary(tr):    Basit, şık, hızlı ve zırvalıksız görev yöneticisi
Summary(ur):    ﺎﯿﮐ ﺱﺍﺩہ، ہﻮﺸﯾﺍﺭ، ﻑﻭﺮﯾ ﺍﻭﺭ ﺲﯾﺩﺍہ ﺱﺍﺩہ ٹﺎﺴﮐ ﻢﯿﻨﯿﺟﺭ
Summary(zh_CN): 简单流畅、快速不脑残的任务规划管理器

%description
A task manager to help you keep track of the tasks that matter most.

Sometimes, you just need a task list to keep you motivated. Agenda provides a
way to write down your tasks and tick them off as you complete them. The list
is saved automatically, so you can close the list to get it out of the way
without losing your place.

Key Features:

  • Saves your task list automatically
  • See your completed tasks until you choose to delete them
  • Autocompletion for previously added tasks
  • Undo/Redo with Ctrl-Z and Ctrl-Y
  • Quit with the Esc key

%description -l ja
最も重要なタスクの記録に便利な、タスク管理アプリです。

モチベーションを維持するために、タスクリストが必要なときはありませんか。
Agenda を使えば、タスクを登録して、終わったらチェックマークをつけていくこと
ができます。リストは自動的に保存されるので、最新の状態を失うことなくリストを
閉じられます。

主な機能:

  • タスクリストを自動的に保存します
  • 完了したタスクは、削除しない限り確認できます
  • 以前に追加したタスクを自動補完します
  • Esc キーで終了できます

%description -l nl
Een taakbeheerder die u helpt de belangrijkste taken bij te houden.

Soms heeft u een taak nodig om u bezig te houden. Agenda biedt de mogelijkheid
uw taken te noteren en ze nadien af te vinken. De lijst wordt automatisch
opgeslagen, dus u kunt de lijst sluiten zonder uw taken kwijt te raken.

Kenmerken:

  • Slaat uw taken automatisch op
  • Bekijk uw afgeronde taken totdat u besluit ze te verwijderen
  • Taaknamen worden automatisch aangevuld
  • Sluit af met de Esc-toets

%description -l pt
Um gestor de tarefas que o ajuda a manter o controle das tarefas que são mais
importantes.

Às vezes, você só precisa precisa de uma lista de tarefas para o manter
motivado. O Agenda proporciona uma forma de escrever as suas tarefas e ir
assinalando aquelas que vai completando. A lista é gravada automaticamente,
para que a possa fechar e tira-la do seu caminho sem que se perca.

Funcionalidades principais:

  • Guarda a sua lista de tarefas automaticamente
  • Veja as suas tarefas completadas até decidir apaga-las
  • Preenchimento automático para tarefas adicionadas anteriormente
  • Fechar com a tecla Esc


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{app_id}

# Upstream installs the same SVG icon in many size-specific directories like
# /usr/share/icons/hicolor/64x64@2/; we can save space by hardlinking these
# together.
hardlink -c -v '%{buildroot}%{_datadir}/icons/hicolor'


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{app_id}.desktop

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{app_id}.appdata.xml
# Matches what gnome-software and others use:
appstreamcli validate --no-net --explain \
    %{buildroot}/%{_metainfodir}/%{app_id}.appdata.xml


%files -f %{app_id}.lang
%doc README.md
%license LICENSE

%{_bindir}/%{app_id}

%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{app_id}.svg
%{_metainfodir}/%{app_id}.appdata.xml


%changelog
%autochangelog
