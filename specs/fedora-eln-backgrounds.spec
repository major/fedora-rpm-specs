%global short_name backgrounds

Name:           fedora-eln-backgrounds
Version:        1.3
Release:        %autorelease
Summary:        Fedora ELN default desktop background

License:        CC-BY-SA-4.0
URL:            https://docs.fedoraproject.org/en-US/eln/
Source0:        https://github.com/fedora-eln/%{short_name}/archive/refs/tags/%{version}.tar.gz
Source1:        gbp2kwp.py

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  ImageMagick
BuildRequires:  python3

%if 0%{?eln}
Provides:       system-backgrounds = %{version}-%{release}
Provides:       system-backgrounds-gnome = %{version}-%{release}
Provides:       system-backgrounds-kde = %{version}-%{release}
Provides:       system-backgrounds-compat = %{version}-%{release}
# for upgrade compatibility
Provides:       desktop-backgrounds-gnome = %{version}-%{release}
Obsoletes:      desktop-backgrounds-gnome
Provides:       desktop-backgrounds-kde = %{version}-%{release}
Obsoletes:      desktop-backgrounds-kde
Provides:       desktop-backgrounds-compat = %{version}-%{release}
Obsoletes:      desktop-backgrounds-compat
%endif


%description
This package contains desktop backgrounds for the Fedora ELN default theme.


%prep
%autosetup -n %{short_name}-%{version}


%build
%make_build


%install
%make_install

python3 %{S:1} -a "Fedora ELN SIG" -l "CC-BY-SA-4.0" -d %{buildroot} default/gnome-backgrounds-fedora-eln.xml

%if %{defined eln}
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
install -m 644 \
    default/10_org.gnome.desktop.background.default.gschema.override \
    default/10_org.gnome.desktop.screensaver.default.gschema.override \
    %{buildroot}%{_datadir}/glib-2.0/schemas

ln -s fedora-eln/default/fedora-eln-01-day.png %{buildroot}%{_datadir}/backgrounds/default.png
ln -s fedora-eln/default/fedora-eln-01-night.png %{buildroot}%{_datadir}/backgrounds/default-dark.png
ln -s fedora-eln/default/fedora-eln.xml %{buildroot}%{_datadir}/backgrounds/default.xml

ln -s Fedora_ELN_Default %{buildroot}%{_datadir}/wallpapers/Default
%endif

%files
%license CC-BY-SA-4.0 Attribution
%dir %{_datadir}/backgrounds
%dir %{_datadir}/backgrounds/fedora-eln
%dir %{_datadir}/backgrounds/fedora-eln/default
%dir %{_datadir}/gnome-background-properties/
%{_datadir}/backgrounds/fedora-eln/default/fedora-eln*.{png,xml}
%{_datadir}/gnome-background-properties/fedora-eln.xml
%dir %{_datadir}/wallpapers/
%{_datadir}/wallpapers/Fedora_ELN*/
%if %{defined eln}
%{_datadir}/backgrounds/default*.{png,xml}
%{_datadir}/glib-2.0/schemas/*.override
%{_datadir}/wallpapers/Default
%endif

%changelog
%autochangelog
