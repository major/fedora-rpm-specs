Name:       ibus-input-pad
Version:    1.5.0
Release:    %autorelease
Summary:    Input Pad for IBus
License:    GPL-2.0-or-later
URL:        https://github.com/fujiwarat/input-pad/wiki
Source0:    https://github.com/fujiwarat/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
# Patch0:     %%{name}-HEAD.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  ibus-devel
BuildRequires:  input-pad-devel
BuildRequires:  make
Requires:       ibus

%description
The input pad engine for IBus platform.

%prep
%autosetup -S git

%build
#autoreconf -v -f -i
%configure \
    --disable-static
%make_build

%install
%make_install

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
cat > $RPM_BUILD_ROOT%{_metainfodir}/input-pad.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>input-pad.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Input Pad</name>
  <summary>Input Pad input method</summary>
  <description>
    <p>
      The Input Pad input method is designed for entering special symbols.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://github.com/fujiwarat/input-pad/wiki</url>
  <url type="bugtracker">https://github.com/fujiwarat/ibus-input-pad/issues</url>
  <url type="help">https://github.com/fujiwarat/input-pad/wiki/Installation</url>
  <screenshots>
    <screenshot type="default">
      <caption>Input Pad for IBus</caption>
      <image type="source" width="1600" height="900">https://raw.githubusercontent.com/fujiwarat/input-pad/master/web/images/screenshot1.png</image>
    </screenshot>
  </screenshots>
  <update_contact>fujiwara_AT_redhat.com</update_contact>
</component>
EOF

%find_lang %{name}

%check
desktop-file-validate \
    $RPM_BUILD_ROOT%{_datadir}/applications/ibus-setup-input-pad.desktop
appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%doc AUTHORS README
%license COPYING
%{_libexecdir}/ibus-engine-input-pad
%{_libexecdir}/ibus-setup-input-pad
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/ibus-setup-input-pad.desktop
%{_datadir}/ibus/component/*

%changelog
%autochangelog
