Name:           pidgin-save-conv-order
Version:        1.0
Release:        14%{?dist}
Summary:        Pidgin plugin to save order
Summary(de):    Pidgin Konversationsreihenfolge speichern
Summary(sr):    Сачувај редослед разговора
Summary(fr):    Enregistrer l'ordre des conversations

License:        GPLv2+
URL:            https://github.com/kgraefe/%{name}
Source0:        https://github.com/kgraefe/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  pidgin-devel
BuildRequires:  libappstream-glib
BuildRequires:  intltool

Requires:       pidgin

%global plugindir %(pkg-config --variable=plugindir pidgin)

%description
This plugin saves the order of the chats and IMs and restores it the next time
you open a conversation.

%description -l de
Dieses Plugin speichert die Reihenfolge von Chats und IMs und stellt diese
wieder her, wenn eine neue Konversation geöffnet wird.

%description -l sr
Овај прикључак чува редослед ћаскања и брзих порука и враћа их приликом
следећег отварања разговора.


%prep
%setup -qn %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} plugindir=%{plugindir}
rm -f %{buildroot}%{plugindir}/save_conv_order.{la,a}
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml

%files -f %{name}.lang
%doc AUTHORS.md CHANGES.md README.md
%license COPYING
%{plugindir}/save_conv_order.so
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 07 2017 Daniel Vrátil <dvratil@fedoraproject.org> - 1.0-2
- use find_lang
- fix mixed tabs and spaces
- fix license
- add localized summary and description

* Tue Mar 28 2017 Daniel Vrátil <dvratil@fedoraproject.org> - 1.0-1
- Initial package
