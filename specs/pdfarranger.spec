Name:           pdfarranger
Version:        1.13.0
Release:        %autorelease
Summary:        PDF file merging, rearranging, and splitting

License:        GPL-3.0-or-later
URL:            https://github.com/pdfarranger/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gettext
BuildRequires:  python3-devel

# For checks only
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

# For dogtail tests
# pyproject_buildrequires without '-R'
BuildRequires:	python3-dogtail
BuildRequires:	xorg-x11-server-Xvfb
BuildRequires:	dbus-daemon
# dnf provides /usr/share/glib-2.0/schemas/org.gnome.desktop.interface.gschema.xml
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  gobject-introspection
# all runtime requires:
BuildRequires:  python3-gobject
BuildRequires:  gtk3
BuildRequires:  python3-cairo
BuildRequires:  poppler-glib
BuildRequires:  python3-img2pdf


Recommends:     python3-img2pdf >= 0.3.4

# These seem to be included in the default desktop install
Requires:       python3-gobject
Requires:       gtk3
Requires:       python3-cairo
Requires:       poppler-glib

Provides:       pdfshuffler = %{version}-%{release}
Obsoletes:      pdfshuffler < 0.6.1-1

# The repository changed to pdfarranger/pdfarranger but we leave the app_id
# for now.
%global app_id com.github.jeromerobert.pdfarranger

%description
PDF Arranger is a small python-gtk application, which helps the user to merge 
or split pdf documents and rotate, crop and rearrange their pages using an 
interactive and intuitive graphical interface. It is a frontend for pikepdf.

PDF Arranger is a fork of Konstantinos Poulios’s PDF-Shuffler.

%prep
%autosetup -p1 -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}
%find_lang %{name}
ln -s pdfarranger %{buildroot}%{_bindir}/pdfshuffler

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
python3 -X tracemalloc -u -m unittest -v -f tests.test_core
python3 -X tracemalloc -u -m unittest -v -f tests.test_exporter
# main gui tests curently failing, may be due to outdated dogtail package
# python3 -X tracemalloc -u -m unittest -v tests.test

%files -f %{name}.lang -f %{pyproject_files}
%license COPYING
%doc README.md
%{_mandir}/man1/pdfarranger.1*
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/%{name}/
%{_bindir}/pdfarranger
%{_bindir}/pdfshuffler

%changelog
%autochangelog
