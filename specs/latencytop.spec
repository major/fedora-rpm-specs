Name:           latencytop
Version:        0.5
Release:        %autorelease
Summary:        System latency monitor (with GUI)

License:        GPL-2.0-only
URL:            http://www.latencytop.org/
Source0:        http://www.latencytop.org/download/%{name}-%{version}.tar.gz
Patch0:         latencytop-Makefile-fixes.patch
Patch1:         latencytop-Makefile-default-to-no-gtk.patch
Patch2:         latencytop-remove-the-fsync-view.patch
Patch3:         latencytop-better-error-message.patch
Patch4:         latencytop-add-return-type-c99.patch

BuildRequires:  gcc make
BuildRequires:  ncurses-devel glib2-devel gtk2-devel pkgconfig
Requires:       %{name}-common = %{version}-%{release}

%description
LatencyTOP is a tool for software developers (both kernel and userspace), aimed
at identifying where in the system latency is happening, and what kind of
operation/action is causing the latency to happen so that the code can be
changed to avoid the worst latency hiccups.
This package contains a build of LatencyTOP with GUI interface. For a build
without GUI install %{name}-tui instead.

%package tui
Summary:        System latency monitor (text interface only)
Requires:       %{name}-common = %{version}-%{release}

%description tui
LatencyTOP is a tool for software developers (both kernel and userspace), aimed
at identifying where in the system latency is happening, and what kind of
operation/action is causing the latency to happen so that the code can be
changed to avoid the worst latency hiccups.
This package contains a build of LatencyTOP without GUI support (and with few
dependencies).

%package common
Summary:        System latency monitor (shared files for both GUI and TUI builds)

%description common
LatencyTOP is a tool for software developers (both kernel and userspace), aimed
at identifying where in the system latency is happening, and what kind of
operation/action is causing the latency to happen so that the code can be
changed to avoid the worst latency hiccups.
This package contains files needed by both the GUI and TUI builds of LatencyTOP.

%prep
%autosetup -p1

%build
export CFLAGS="${CFLAGS:-%{optflags}}"
# make two builds, first without GUI, then with
make %{?_smp_mflags}
mv latencytop latencytop-tui
make clean
make %{?_smp_mflags} HAS_GTK_GUI=1

%install
make install DESTDIR=%{buildroot} SBINDIR=%{_sbindir}
install -m 0755 latencytop-tui %{buildroot}%{_sbindir}/
ln -s latencytop.8 %{buildroot}%{_mandir}/man8/latencytop-tui.8

%files
%{_sbindir}/latencytop

%files tui
%{_sbindir}/latencytop-tui

%files common
%{_datadir}/%{name}
%{_mandir}/man8/*

%changelog
%autochangelog
