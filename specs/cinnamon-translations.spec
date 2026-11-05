%global forgeurl https://github.com/linuxmint/cinnamon-translations
%global tag      %{version}

%global _trans_version 2018.12.11

Name:           cinnamon-translations
Version:        6.8.0
Release:        %{autorelease}
%{forgemeta}
Summary:        Translations for Cinnamon and Nemo

License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        http://packages.linuxmint.com/pool/main/m/mint-translations/mint-translations_%{_trans_version}.tar.xz
BuildRequires:  gettext
BuildRequires:  make

BuildArch:      noarch

%description
Translations for Cinnamon, Nemo and Mintlocale.

%prep
%forgeautosetup -p1
tar -xf %{SOURCE1}

%build
%{make_build}
%{make_build} -C mint-translations

%install
# install mint translations for mintlocale
%{_bindir}/find mint-translations -not -name 'mintlocale.mo' -type f -delete
%{_bindir}/find . -name 'cinnamon-bluetooth.mo' -type f -delete
%{__cp} -pr mint-translations/%{_datadir}/linuxmint/locale .%{_datadir}
%{__cp} -pr .%{_prefix} %{buildroot}

%find_lang cinnamon
%find_lang mintlocale
%find_lang nemo
%find_lang nemo-extensions
%find_lang cinnamon-control-center
%find_lang cinnamon-screensaver
%find_lang cinnamon-session
%find_lang cinnamon-settings-daemon

%files -f cinnamon.lang -f mintlocale.lang -f nemo.lang -f nemo-extensions.lang -f cinnamon-control-center.lang -f cinnamon-screensaver.lang -f cinnamon-session.lang -f cinnamon-settings-daemon.lang
%license COPYING


%changelog
%autochangelog