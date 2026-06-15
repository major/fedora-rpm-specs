Name:           gkrellm
Version:        2.5.1
Release:        %autorelease
Summary:        Multiple stacked system monitors in one process
License:        GPL-3.0-or-later
URL:            https://gkrellm.srcbox.net/
Source0:        https://gkrellm.srcbox.net/releases/%{name}-%{version}.tar.bz2
Source5:        make-git-snapshot.sh
Patch1:         gkrellm-2.5.1-config.patch
Patch3:         gkrellm-2.4.0-width.patch
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(libntlm)
BuildRequires:  desktop-file-utils gettext
BuildRequires:  lm_sensors-devel libappstream-glib
BuildRequires:  make
Requires:       gdk-pixbuf2-modules-extra%{?_isa}

%description
GKrellM charts CPU, load, Disk, and all active net interfaces
automatically.  An on/off button and online timer for the PPP
interface is provided, as well as monitors for memory and swap usage,
file system, internet connections, APM laptop battery, mbox style
mailboxes, and temperature sensors on supported systems.  Also
included is an uptime monitor, a hostname label, and a clock/calendar.
Additional features are:

  * Autoscaling grid lines with configurable grid line resolution.
  * LED indicators for the net interfaces.
  * A gui popup for configuration of chart sizes and resolutions.


%package daemon
Summary:        The GNU Krell Monitors Server
Requires(pre):  systemd
Requires(post,preun,postun): systemd


%description daemon
gkrellmd listens for connections from gkrellm clients. When a gkrellm
client connects to a gkrellmd server all builtin monitors collect their
data from the server.


%package        devel
Summary:        Development files for the GNU Krell Monitors
Requires:       gtk2-devel%{?_isa}

%description devel
Development files for the GNU Krell Monitors.


%prep
%autosetup -p1

for i in docs/gkrellmd.1 docs/gkrellm.1 README Changelog.OLD Changelog-plugins.html \
    src/gkrellm.h server/gkrellmd.h; do
   sed -i -e "s@/usr/lib/gkrellm2*/plugins@%{_libdir}/gkrellm2/plugins@" $i
   sed -i -e "s@/usr/local/lib/gkrellm2*/plugins@/usr/local/%{_lib}/gkrellm2/plugins@" $i
done

# Create a sysusers.d config file
cat >gkrellm.sysusers.conf <<EOF
u gkrellmd - 'GNU Krell daemon' - -
EOF


%conf
%meson


%build
%meson_build


%install
mkdir -p %{buildroot}%{_datadir}/gkrellm2/themes
mkdir -p %{buildroot}%{_libdir}/gkrellm2/plugins

%meson_install
%find_lang %name

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

install -m0644 -D gkrellm.sysusers.conf %{buildroot}%{_sysusersdir}/gkrellm.conf


%post daemon
%systemd_post gkrellmd.service

%preun daemon
%systemd_preun gkrellmd.service

%postun daemon
%systemd_postun_with_restart gkrellmd.service


%files -f %{name}.lang
%license COPYRIGHT
%doc CHANGELOG.md Changelog.OLD README Themes.html
%{_bindir}/%{name}
%{_libdir}/gkrellm2
%{_datadir}/gkrellm2
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/*.metainfo.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files devel
%license %{_licensedir}/%{name}*
%{_includedir}/gkrellm2
%{_libdir}/pkgconfig/%{name}*.pc

%files daemon
%license %{_licensedir}/%{name}*
%{_unitdir}/gkrellmd.service
%{_sbindir}/gkrellmd
%{_mandir}/man1/gkrellmd.*
%config(noreplace) %{_sysconfdir}/gkrellmd.conf
%{_sysusersdir}/gkrellm.conf


%changelog
%autochangelog
