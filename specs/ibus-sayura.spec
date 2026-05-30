Name:       ibus-sayura
Version:    1.3.2
Release:    %autorelease
Summary:    The Sinhala engine for IBus input platform
License:    GPL-2.0-or-later
URL:        https://github.com/pravins/ibus-sayura
Source0:    https://github.com/user-attachments/files/28340200/%{name}-%{version}.tar.gz

# This is a test patch so not submitted to upstream yet
# This patch is created by Mike Fabian
Patch0:     fix-for-wayland-rhbz1724759.patch

BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  ibus-devel
BuildRequires: make
Requires:   ibus
%description
The Sayura engine for IBus platform. It provides Sinhala input method.

%prep
%autosetup -p1

%build
%configure --disable-static
# make -C po update-gmo
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/sayura.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>sayura.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Sayura</name>
  <summary>Sihali input method</summary>
  <description>
    <p>
      The Sayura input method is designed for entering Sinhala text.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://fedorahosted.org/ibus-sayura/</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <languages>
    <lang percentage="100">si</lang>
  </languages>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_libexecdir}/ibus-engine-sayura
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/ibus-sayura
%{_datadir}/ibus/component/*

%changelog
%autochangelog

