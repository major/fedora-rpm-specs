Name:           pidgin-privacy-please
Version:        0.7.1
Release:        24%{?dist}
Summary:        Security and Privacy plugin for Pidgin
Summary(fr):    Plugin de sécurité et confidentialité pour Pidgin

License:        GPLv3
URL:            http://code.google.com/p/pidgin-privacy-please/
Source0:        http://pidgin-privacy-please.googlecode.com/files/%{name}-%{version}.tar.gz
%if 0%{?rhel} <= 5
ExcludeArch:    ppc
%endif
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  pidgin-devel >= 2.5
Requires:       pidgin >= 2.5


%description
pidgin-privacy-please is a Pidgin plugin to stop spammers from annoying you.
It offers the following features:
  - Block individual users
  - Auto-reply to blocked messages
  - Block messages from people who are not on your contact list (with an
optional auto-reply)
  - Block messages using regular expressions, either against the message
sender, the message content, or both
  - Suppress repeated/all authorization requests
  - Suppress OSCAR (ICQ/AIM) authorization requests
  - Automatically show user info on authorization requests
  - Block jabber headline messages (eg. alerts from the MSN transport)
  - Block AOL system messages
  - Challenge-response bot-check 
%description -l fr
pidgin-privacy-please est un plugin pour Pidgin qui va empêcher les spammeurs
de vous ennuyer.
Il offre les fonctionnalités suivantes :
  - Blocage d'utilisateurs
  - Réponse automatique pour les messages bloqués
  - Bloque les messages des personnes qui ne sont pas dans votre liste de
contacts (avec une réponse automatique en option)
  - Filtre les messages en utilisant des expressions régulières, dans
l'expéditeur du message, son contenu, ou les deux
  - Supprime les demandes d'autorisation répétées
  - Supprime les demandes d'autorisation d'OSCAR (ICQ / AIM)
  - Affiche automatiquement les informations de l'utilisateur qui demandes une
autorisation
  - Bloque les messages titre de jabber (ex: alertes de transport MSN)
  - Bloque les messages système d'AOL
  - Contrôle des bot par la méthode Challenge-réponse


%prep
%setup -q -n %{name}-%{version}%{?prever}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot} INSTALL="install -p"
%find_lang %{name}

# remove .la file
%{__rm} %{buildroot}/%{_libdir}/pidgin/libpidgin_pp.la



%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/pidgin/libpidgin_pp.so


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.7.1-2
- Bump for F16

* Tue Aug 16 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.7.1-1
- Upstream 0.7.1

* Mon Jun 27 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.7.0-1
- Upstream 0.7.0

* Sat Nov 06 2010 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.6.4-2
- Fix build failed on RHEL5/6

* Sat Nov 06 2010 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.6.4-1
- Upstream 0.6.4

* Fri Jul 16 2010 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.6.3-2
- Add BR intltool
- Exclude ppc only for RHEL <= 5

* Wed Jul 14 2010 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.6.3-1
- Upstream 0.6.3

* Thu Nov 05 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.6.1-1
- Upstream 0.6.1

* Thu Aug 27 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.6.0-1
- Upstream 0.6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 24 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.5.4-1
- Upstream 0.5.4

* Tue Apr 7 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.5.3-2
- Modifications for EL5

* Mon Mar 16 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.5.3-1
- Upstream 0.5.3

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 05 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.5.2-2
- Correction on URL and Source0
- Correction on install and buildroot variable

* Mon Jan 05 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 0.5.2-1
- Initial package
