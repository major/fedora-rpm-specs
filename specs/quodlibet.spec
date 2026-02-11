Name:		quodlibet
Version:	4.7.1
Release:	%autorelease
Summary:	A music management program

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://quodlibet.readthedocs.org/en/latest/
Source0:	https://github.com/quodlibet/quodlibet/releases/download/release-%{version}/quodlibet-%{version}.tar.gz
Source1:	https://github.com/quodlibet/quodlibet/releases/download/release-%{version}/quodlibet-%{version}.tar.gz.sig
Source2:	https://keys.openpgp.org/vks/v1/by-fingerprint/E0AA0F031DBD80FFBA57B06D5A62D0CAB6264964
Source3:	README.fedora

# https://github.com/quodlibet/quodlibet/pull/4741
Patch:		https://github.com/quodlibet/quodlibet/commit/93d2de93663245bd3b2aadc2ea6085991cd7da35.patch
# https://github.com/quodlibet/quodlibet/pull/4843
Patch:		https://github.com/quodlibet/quodlibet/commit/85631a63fe1b431adacc2a4245f2c59cb8145975.patch
# https://github.com/quodlibet/quodlibet/pull/4845
Patch:		https://github.com/quodlibet/quodlibet/commit/5cecd9b3579d27ebe594d20f8841d531261a7daf.patch
# https://github.com/quodlibet/quodlibet/pull/4846
Patch:		https://github.com/quodlibet/quodlibet/commit/2742dc8da188d4da4a45f775540a04b00f847d05.patch
Patch:		https://github.com/quodlibet/quodlibet/commit/060c938a13249c2809fece6e8e11c088783887f8.patch

BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 3.5
BuildRequires:	(python3-setuptools if python3-devel >= 3.12)
# needed for py_byte_compile
BuildRequires:	python3-devel
# needed for tests
BuildRequires:	glibc-langpack-en
BuildRequires:	gnupg2
BuildRequires:	gobject-introspection
BuildRequires:	gstreamer1
BuildRequires:	gstreamer1-plugins-good
BuildRequires:	gtk3 >= 3.18
BuildRequires:	libmodplug
BuildRequires:	python3-feedparser
BuildRequires:	python3-flaky
BuildRequires:	python3-gobject >= 3.18
BuildRequires:	python3-mutagen >= 1.14
BuildRequires:	python3-pytest
BuildRequires:	python3-pyvirtualdisplay
BuildRequires:	xine-lib

Requires:	exfalso = %{version}-%{release}
Requires:	gstreamer1
Requires:	gstreamer1-plugins-base
Requires:	gstreamer1-plugins-good
Requires:	python3-dbus

%description
Quod Libet is a music management program. It provides several different ways
to view your audio library, as well as support for Internet radio and
audio feeds. It has extremely flexible metadata tag editing and searching
capabilities.
Supported file formats include Ogg Vorbis, MP3, FLAC, MOD/XM/IT, Musepack,
Wavpack, and MPEG-4 AAC.


%package -n exfalso
Summary: Tag editor for various music files

Requires:	adwaita-icon-theme
Requires:	gtk3 >= 3.18
Requires:	hicolor-icon-theme
Requires:	libsoup >= 2.44
Requires:	pkgconfig
Requires:	python3-gobject >= 3.18
Requires:	python3 >= 3.5
Requires:	python3-mutagen >= 1.14
Requires:	python3-feedparser

# for musicbrainz plugin
Requires:	python3-musicbrainzngs >= 0.6


%description -n exfalso
Ex Falso is a tag editor with the same tag editing interface as Quod Libet,
but it does not play files.
Supported file formats include Ogg Vorbis, MP3, FLAC, MOD/XM/IT, Musepack,
Wavpack, and MPEG-4 AAC.


%package zsh-completion
Summary: zsh completion files for %{name}
Requires: quodlibet = %{version}-%{release}
Requires: zsh

%description zsh-completion
This package installs %{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 1

install -pm 0644 %{S:3} .


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications		\
	--delete-original					\
	%{buildroot}%{_datadir}/applications/io.github.quodlibet.QuodLibet.desktop
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications		\
	--delete-original					\
	%{buildroot}%{_datadir}/applications/io.github.quodlibet.ExFalso.desktop

%find_lang quodlibet


%check
%pytest -m "not network"


%files
%doc README.fedora
%{_bindir}/quodlibet
%{_datadir}/applications/io.github.quodlibet.QuodLibet.desktop
%{_datadir}/bash-completion/completions/quodlibet
%{_datadir}/gnome-shell/search-providers/io.github.quodlibet.QuodLibet-search-provider.ini
%{_datadir}/icons/hicolor/*x*/apps/io.github.quodlibet.QuodLibet.png
%{_datadir}/dbus-1/services/net.sacredchao.QuodLibet.service
%{_datadir}/metainfo/io.github.quodlibet.QuodLibet.appdata.xml
%{_mandir}/man1/quodlibet.1*


%files -n exfalso -f %{name}.lang -f %{pyproject_files}
%license COPYING
%doc NEWS.rst README.rst
%{_bindir}/exfalso
%{_bindir}/operon
%{_datadir}/applications/io.github.quodlibet.ExFalso.desktop
%{_datadir}/bash-completion/completions/operon
%{_mandir}/man1/exfalso.1*
%{_mandir}/man1/operon.1*
%{_datadir}/icons/hicolor/*x*/apps/io.github.quodlibet.ExFalso.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/io.github.quodlibet.ExFalso.appdata.xml


%files zsh-completion
%{_datadir}/zsh/site-functions/_quodlibet


%changelog
%autochangelog
