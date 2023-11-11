%global app_id com.github.donadigo.appeditor

Name:           appeditor
Summary:        Edit application menu
Version:        1.1.5
Release:        %autorelease
# The entire source is GPL-3.0-only, except:
#   - data/com.github.donadigo.appeditor.appdata.xml.in is CC0-1.0, which is
#     allowed for content only
License:        GPL-3.0-only AND CC0-1.0

URL:            https://github.com/donadigo/appeditor
Source:         %{url}/archive/%{version}/appeditor-%{version}.tar.gz

# Fix flickering titlebar (fix #103)
# https://github.com/donadigo/appeditor/issues/103#issuecomment-756924055
# https://github.com/donadigo/appeditor/pull/139
Patch:          %{url}/pull/139.patch
# Fix deprecated top-level developer_name in AppData XML
# https://github.com/donadigo/appeditor/pull/135
Patch:          %{url}/pull/135.patch
# Ensure all text files have terminal newlines
# https://github.com/donadigo/appeditor/pull/136
Patch:          %{url}/pull/136.patch
# Remove executable bit from files that are not script-like
# https://github.com/donadigo/appeditor/pull/138
Patch:          %{url}/pull/138.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       contractor
Requires:       hicolor-icon-theme

Summary(ca):    Modifiqueu el menú d’aplicacions
Summary(de):    Keine Anwendungen gefunden
Summary(es):    Editar el menú de aplicaciones
Summary(fr):    Modifier le menu des applications
Summary(it):    Modifica Menù Applicazione
Summary(ja):    アプリケーションメニューを編集します
Summary(lt):    Programų nerasta
Summary(nl_NL): Toepassingenmenu bewerken
Summary(pt):    Editar menu da aplicações
Summary(pt_BR): Editar menu da aplicações
Summary(ru):    Изменяйте меню приложений
Summary(sv):    Redigera programmenyn
Summary(tr):    Uygulama menülerini düzenle

%description
Edit application entries shown in application menu and their properties.

Features include:

  • Hide and show applications from the application menu
  • Create new application entries
  • Change application’s display name, icon and more

%description -l ca
Modifiqueu les entrades mostrades al menú d’aplicacions i les seves propietats.

Funcionalitats distintives:

  • Amagueu i mostreu entrades al menú d’aplicacions
  • Creeu-ne de noves
  • Canvieu el nom visible, la icona i molt més per cada aplicació

# %%description -l de
# (only partially translated upstream)

%description -l es
Edite las entradas del menú de aplicaciones y sus propiedades.

Algunas de las funcionalidades son:

  • Ocultar y mostrar entradas del menú de aplicaciones
  • Crear entradas de aplicación nuevas
  • Cambiar el nombre mostrado de una aplicación, su icono y más

%description -l fr
Modifiez les raccourcis et leurs propriétés dans le menu des applications.

Fonctionnalités incluses:

  • Masquer et afficher les applications du menu des applications
  • Créer de nouveaux raccourcis d’application
  • Changer le nom d’une application, son icône, etc

%description -l it
Modifica le voci dell’applicazione visualizzate nel menu le relative proprietà.

Funzionalità incluse:

  • Mostra e nascondi le applicazioni nel Menù Applicazioni
  • Crea nuova voce applicazione
  • Cambia il nome visualizzato dell’applicazione, la sua icona ed altro

%description -l ja
アプリケーションメニューに表示されるアプリケーションのエントリーとプロパティ
を編集します。

含まれる機能:

  • アプリケーションをアプリケーションメニューから隠したり表示したりします
  • 新しいアプリケーションのエントリーを作成します
  • アプリケーションの表示名やアイコンなどを変更します

# %%description -l lt
# (only partially translated upstream)

%description -l nl_NL
Bewerk menu-items uit het toepassingenmenu, inclusief hun eigenschappen.

Het bevat de volgende mogelijkheden:

  • Toon en verberg items uit het toepassingenmenu
  • Maak nieuwe menu-items
  • Pas de weergavenaam, het pictogram en meer aan

%description -l pt
Editar entradas de aplicações mostradas no menu das aplicações e as suas
propriedades.

Características incluídas:

  • Esconde e mostra aplicações do menu de aplicações
  • Criar novas entradas de aplicações
  • Alterar o nome de exibição da aplicação, ícone e mais

%description -l pt_BR
Editar entradas de aplicações mostradas no menu das aplicações e as suas
propriedades.

Características incluídas:

  • Esconde e mostra aplicações do menu de aplicações
  • Criar novas entradas de aplicações
  • Alterar o nome de exibição da aplicação, ícone e mais

%description -l ru
Редактирование описания и свойств программ в меню приложений.

Доступные возможности:

  • Скрытие и отображение программ в меню приложений
  • Создание новых записей о приложениях
  • Изменение отображаемого имени приложение, значка и многого другого

%description -l sv
Redigera programposterna som visas i menyn, och dess egenskaper.

Funktioner:

  • Dölj och visa program i programmenyn.
  • Skapa nya programposter.
  • Ändra programmens visningsnamn, ikon och mer.

%description -l tr
Uygulama menüsünde gösterilen uygulama girişlerini ve özelliklerini düzenleyin.

Özellikler şunlardır:

  • Uygulama menüsünden uygulamaları gizleme ve gösterme
  • Yeni uygulama girişleri oluşturma
  • Uygulamanın görünen adını, simgesini ve daha fazlasını değiştirin


%prep
%autosetup -n appeditor-%{version} -p1
rm -rv external


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
    %{buildroot}/%{_metainfodir}/%{app_id}.appdata.xml
# Matches what gnome-software and others use:
appstreamcli validate --no-net --explain \
    %{buildroot}/%{_metainfodir}/%{app_id}.appdata.xml


%files -f %{app_id}.lang
%doc README.md
%license LICENSE

%{_bindir}/%{app_id}

%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/contractor/%{app_id}.contract
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{app_id}.svg
%{_metainfodir}/%{app_id}.appdata.xml


%changelog
%autochangelog
