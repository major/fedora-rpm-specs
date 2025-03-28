%if 0%{?rhel} >= 9
%bcond_with gconf
%else
%bcond_without gconf
%endif

Summary:   Writes audio CD-Rs in disk-at-once (DAO) mode
Name:      cdrdao
Version:   1.2.5
Release:   %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
URL:       http://cdrdao.sourceforge.net/
Source0:   http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# https://github.com/cdrdao/cdrdao/pull/21
# should fix whipper failure with this version of cdrdao:
# https://github.com/whipper-team/whipper/issues/591
# https://bugzilla.redhat.com/show_bug.cgi?id=2238243
Patch:     21.patch
# https://github.com/cdrdao/cdrdao/pull/25
# fixes the "cdrdao version" command broken in 1.2.5 that brasero relies on
Patch1:    cdrdao-1.2.5-Fix-version-command.patch
# https://github.com/cdrdao/cdrdao/pull/35
# Fix build with GCC 15 (C23)
Patch2:    cdrdao-1.2.5-gcc15.patch
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  gtkmm3.0-devel
BuildRequires:  libsigc++20-devel
BuildRequires:  libvorbis-devel >= 1.0
BuildRequires:  libao-devel
BuildRequires:  libmad-devel
BuildRequires:  lame-devel
#requirements to rebuild autotools
BuildRequires:  autoconf
%if %{with gconf}
BuildRequires:  GConf2-devel
%endif
BuildRequires: make

# We have removed gcdmaster sub-package in 1.2.3-10
Obsoletes: gcdmaster < 1.2.3-10

# Only exclude s390
ExcludeArch: s390 s390x


%description
Cdrdao records audio CD-Rs in disk-at-once (DAO) mode, based on a
textual description of the CD contents. Recording in DAO mode writes
the complete disc (lead-in, one or more tracks, and lead-out) in a
single step. DAO allows full control over the length and the contents
of pre-gaps, the pause areas between tracks.


%prep
%autosetup -p 1

%build
#run autoreconf to support aarch64
#not needed when upstream moves to  new automake
autoreconf -v -f -i -I.
%configure \
        --without-xdao \
        --without-scglib \
        --with-ogg-support \
        --with-mp3-support \
        --with-lame

%make_build


%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%files
%doc AUTHORS README CREDITS ChangeLog
%license COPYING
%{_bindir}/cdrdao
%{_bindir}/gcdmaster
%{_bindir}/*toc*
%{_datadir}/cdrdao
%{_datadir}/*/gcdmaster*
%dir %{_datadir}/gcdmaster/
%dir %{_datadir}/gcdmaster/glade/
%dir %{_datadir}/application-registry/
%{_datadir}/gcdmaster/glade/P*.glade
%{_datadir}/glib-2.0/schemas/org.gnome.gcdmaster.gschema.xml
%{_datadir}/mime/packages/gcdmaster.xml
%{_mandir}/*/cdrdao*
%{_mandir}/*/cue2toc*
%{_mandir}/*/gcdmaster*
%{_mandir}/*/toc2cue*
%{_mandir}/*/toc2cddb*

%changelog
%autochangelog
