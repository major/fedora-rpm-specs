Name:           pdfarranger
Version:        1.10.0
Release:        %autorelease
Summary:        PDF file merging, rearranging, and splitting

License:        GPLv3
URL:            https://github.com/pdfarranger/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-pip

# For checks only
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Requires:       python3-pikepdf >= 1.15.1
Recommends:     python3-img2pdf >= 0.3.4

# These seem to be included in the default desktop install
Requires:       python3-gobject
Requires:       gtk3
Requires:       python3-cairo
Requires:       poppler-glib
Requires:       python3-dateutil >= 2.4.0

Provides:       pdfshuffler = %{version}-%{release}
Obsoletes:      pdfshuffler < 0.6.1-1

# The repository changed to pdfarranger/pdfarranger but we leave the app_id
# for now.
%global app_id com.github.jeromerobert.pdfarranger
%global python3_wheelname %{name}-*-py3-none-any.whl

%description
PDF Arranger is a small python-gtk application, which helps the user to merge 
or split pdf documents and rotate, crop and rearrange their pages using an 
interactive and intuitive graphical interface. It is a frontend for pikepdf.

PDF Arranger is a fork of Konstantinos Poulios’s PDF-Shuffler.


%prep
%autosetup -n %{name}-%{version}

# py3_build / py3_install do not work with this setup.py but building
# a wheel works just fine
%build
%py3_build_wheel

%install
%py3_install_wheel %{python3_wheelname}
%find_lang %{name}
ln -s pdfarranger %{buildroot}%{_bindir}/pdfshuffler

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%license COPYING
%doc README.md
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.dist-info/
%{_mandir}/man*/*.*
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/%{name}/
%{_bindir}/pdfarranger
%if 0%{?fedora} > 31
%{_bindir}/pdfshuffler
%endif

%changelog
%autochangelog
