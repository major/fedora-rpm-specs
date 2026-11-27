%global forgeurl https://github.com/linuxmint/lightdm-settings
%global tag      %{version}

Name:		lightdm-settings
Version:	2.1.3
Release:	%autorelease
%forgemeta
Summary:	Configuration tool for the LightDM display manager

License:	GPL-3.0-or-later
URL:        %{forgeurl}
Source0:    %{forgesource}

BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	make

Requires:	filesystem
Requires:	gtk3
Requires:	hicolor-icon-theme
Requires:	polkit
Requires:	python3-xapp
Requires:	python3-gobject
Requires:	python3-setproctitle
Requires:	slick-greeter

%description
This tool currently lets users configure slick-greeter.

%prep
%forgeautosetup -p1

%build
%make_build

%install
# No install-target in Makefile.
%{__cp} -pr .%{_prefix} %{buildroot}

# Set exec-permissions where needed.
%{__chmod} -c 0755 %{buildroot}%{_bindir}/%{name} \
	 %{buildroot}%{_prefix}/lib/%{name}/%{name}

# Find localizations and build manifest.
%find_lang %{name}

%check
%{_bindir}/desktop-file-validate \
	%{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license debian/copyright COPYING
%doc debian/changelog README.md
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/polkit-1/actions/org.x.%{name}.policy

%changelog
%autochangelog