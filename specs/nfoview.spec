Name:           nfoview
Version:        2.1
Release:        %autorelease
Summary:        Viewer for NFO files

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://otsaloma.io/nfoview/
Source0:        https://github.com/otsaloma/nfoview/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-gobject-devel

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib

Requires:       shared-mime-info
Requires:       hicolor-icon-theme
Requires:       python3-gobject
Requires:       terminus-fonts

%description
NFO Viewer is a simple viewer for NFO files, which are "ASCII" art in
the CP437 codepage. The advantages of using NFO Viewer instead of a
text editor are preset font and encoding settings, automatic window
size and clickable hyperlinks.

%prep
%autosetup

%build
%make_build PREFIX=%{_prefix}


%install
%make_install PREFIX=%{_prefix}

desktop-file-install                                        \
    --add-category="TextTools;"                             \
    --remove-category="Viewer;"                             \
    --delete-original                                       \
    --dir=%{buildroot}%{_datadir}/applications              \
    %{buildroot}%{_datadir}/applications/io.otsaloma.nfoview.desktop
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.otsaloma.nfoview.appdata.xml

%files -f %{name}.lang
%doc AUTHORS.md NEWS.md README.md
%license COPYING
%{_mandir}/man*/%{name}.*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_metainfodir}/io.otsaloma.nfoview.appdata.xml
%{_datadir}/applications/io.otsaloma.nfoview.desktop
%{_datadir}/icons/hicolor/*/apps/io.otsaloma.nfoview*

%changelog
%autochangelog
