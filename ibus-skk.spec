Name:		ibus-skk
Version:	1.4.3
Release:	%{?autorelease}%{!?autorelease:1%{?dist}}
Summary:	Japanese SKK input method for ibus

License:	GPL-2.0-or-later
URL:		http://github.com/ueno/ibus-skk
Source0:	http://cloud.github.com/downloads/ueno/ibus-skk/%{name}-%{version}.tar.xz
Patch:		ibus-skk-1.4.3-coalesce-commit-text.patch

BuildRequires:	vala
BuildRequires:	intltool
BuildRequires:	libskk-devel >= 0.0.11
BuildRequires:	ibus-devel
BuildRequires:	gtk3-devel
BuildRequires:	desktop-file-utils
BuildRequires: make
Requires:	ibus, skkdic

%description
A Japanese Simple Kana Kanji Input Method Engine for ibus.

%prep
%autosetup -p1
rm src/*vala.stamp
# don't touch XKB layout under Fedora
sed -i 's!<layout>jp</layout>!<layout>default</layout>!' src/skk.xml.in.in

%build
%configure
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
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/skk.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>skk.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Simple Kana-Kanji</name>
  <summary>Japanese input method</summary>
  <description>
    <p>
      The SKK input method is designed for entering Japanese text.
      The input method was originally invented by Masahiko Sato in 1987 and it is
      quite different from other Japanese input methods in the way it handles input.
    </p>
    <p>
      While other Japanese input methods treat input as a sentence, SKK treats it as a
      word and leaves control of sentence construction to users.
      Though it is not what normal users expect, advanced users can input Japanese
      with SKK more efficiently.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://github.com/ueno/ibus-skk/</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

desktop-file-validate %{buildroot}/%{_datadir}/applications/ibus-setup-skk.desktop

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README ChangeLog
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/ibus-skk
%{_libexecdir}/ibus-*-skk
%{_datadir}/ibus/component/skk.xml
%{_datadir}/applications/ibus-setup-skk.desktop


%changelog
%autochangelog
