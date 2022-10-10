%bcond_with tests

%global sysname gsecrets
%global oldname gnome-passwordsafe

Name:           secrets
Version:        7.0
Release:        %autorelease
Summary:        Manage your passwords

License:        GPLv3
URL:            https://gitlab.gnome.org/World/secrets
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildArch:      noarch
# https://bugzilla.redhat.com/show_bug.cgi?id=2029547#c24
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_architecture_support
ExcludeArch:    s390x

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.59
BuildRequires:  python3-devel >= 3.8

BuildRequires:  python3dist(pykeepass) >= 4.0.3
BuildRequires:  python3dist(pyotp) >= 2.4.0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(validators)
BuildRequires:  python3dist(zxcvbn)

BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.66
BuildRequires:  pkgconfig(gtk4) >= 4.6.2
BuildRequires:  pkgconfig(libadwaita-1) >= 1.1.99

%if %{with tests}
BuildRequires:  python3-gobject
BuildRequires:  python3dist(pytest)
%endif

Requires:       hicolor-icon-theme
Requires:       libadwaita >= 1.1.99
Requires:       python3-gobject
Requires:       python3-pykeepass >= 4.0.3
Requires:       python3-pyotp >= 2.4.0
Requires:       python3-validators
Requires:       python3-zxcvbn

Provides:       %{oldname} = %{version}-%{release}
Obsoletes:      %{oldname} <= 5.1-6

%description
Secrets is a password manager which integrates perfectly with the GNOME
desktop and provides an easy and uncluttered interface for the management of
password databases.

Features:
  * Create or import KeePass safes
  * Assign a color and additional attributes to entries
  * Add attachments to your encrypted database
  * Generate cryptographically strong passwords
  * Change the password or keyfile of your database
  * Quickly search your favorite entries
  * Automatic database lock during inactivity
  * Adaptive interface
  * Support for two-factor authentication


%prep
%autosetup


%build
%meson \
  %if %{with tests}
  -Dtests=true \
  %endif
  %{nil}
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%if %{with tests}
%meson_test
%endif


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/mime/packages/*.xml
%{_metainfodir}/*.xml
%{python3_sitelib}/%{sysname}/


%changelog
%autochangelog
