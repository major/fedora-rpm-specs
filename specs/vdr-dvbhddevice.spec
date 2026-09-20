# Upstream has tagged no release and publishes no tarballs; dvbhddevice.c has
# carried 2.2.0 for years while the code kept moving, so the package follows
# git and versions the snapshot.
%global commit          945eaa1a7d0be6dd226a0b45364100642b01cd68
# Bitbucket names both the archive it serves and the directory inside it after
# the 12 character short hash, so Version, Source0 and %%autosetup all agree.
%global shortcommit     %(c=%{commit}; echo ${c:0:12})
%global snapdate        20260823

%global pname           dvbhddevice

# The plugin .so is dlopen()ed by VDR, never linked against, so it must not
# turn up as a provide; the ABI it needs is expressed by vdr(abi) below.
%global __provides_exclude_from ^%{vdr_libdir}/.*\.so.*$

Name:           vdr-%{pname}
Version:        2.2.0^%{snapdate}git%{shortcommit}
Release:        3%{?dist}
Epoch:          1
Summary:        VDR output device plugin for TechnoTrend S2-6400 DVB cards

# COPYING is GPLv2, and README and the libhdffcmd headers offer "either
# version 2 of the License, or (at your option) any later version".
License:        GPL-2.0-or-later
URL:            https://bitbucket.org/powARman/dvbhddevice
Source0:        %{url}/get/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
# Creates PLUGIN_OPTIONS so the init script can pass arguments to the plugin.
Source1:        %{name}.conf

BuildRequires:  binutils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libjpeg-devel
BuildRequires:  make
BuildRequires:  vdr-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
The dvbhddevice plugin implements a VDR output device for the "Full Featured
TechnoTrend S2-6400" DVB card. Decoding and OSD rendering run on the card's
HDFF firmware rather than on the CPU; the plugin drives that firmware through
the HDFF command library, which is part of this source tree and is linked in
statically.

%prep
%autosetup -n powARman-%{pname}-%{shortcommit}
# The only non-ASCII byte in the tree is a latin-1 'a' umlaut in HISTORY.
iconv -f iso-8859-1 -t utf-8 HISTORY -o HISTORY.utf8 && touch -r HISTORY HISTORY.utf8 && mv HISTORY.utf8 HISTORY

%build
# Compiler flags come from vdr.pc, which records the ones VDR itself was built
# with, so the plugin ABI matches. %%make_build supplies LDFLAGS from the
# environment.
%make_build

%install
%make_install
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf

%find_lang %{name}

%check
# VDR resolves VDRPluginCreator after dlopen(); a plugin that does not export
# it links cleanly and then fails at runtime.
nm -D --defined-only %{buildroot}%{vdr_libdir}/libvdr-%{pname}.so.%{vdr_apiversion} \
    | grep -q ' VDRPluginCreator$'

%files -f %{name}.lang
%license COPYING
%doc HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{vdr_libdir}/libvdr-%{pname}.so.%{vdr_apiversion}

%changelog
* Fri Sep 18 2026 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.0^20260823git945eaa1a7d0b-3
- remove duplicate BR binutils

* Wed Sep 09 2026 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.0^20260823git945eaa1a7d0b-2
- Add Epoch 1 to allow vdr-dvbhddevice to be installed with newer VDR versions

* Tue Sep 08 2026 Dirk Nehring <dnehring@gmx.net> - 2.2.0^20260823git945eaa1a7d0b-1
- Update to snapshot 945eaa1a7d0b
- Drop vdr-dvbhddevice-fsf-address.patch, applied upstream
- Add binutils to BuildRequires for the nm call in %%check
- Carry the full commit hash so Source0 names the revision unambiguously
- Drop vdr-dvbhddevice.rpmlintrc; its only filter never matches in a buildroot
  that has vdr-devel, and rpmlint reports the filter itself as unused there

* Sat Aug 15 2026 Dirk Nehring <dnehring@gmx.net> - 2.2.0^20250418gita4ab40ea79bf-1
- Modernize to rpmautospec in a dist-git layout
- Split dvbhddevice out of the vdr package into a standalone plugin package
- Add %%check verifying the VDRPluginCreator export
