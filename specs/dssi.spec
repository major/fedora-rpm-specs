Summary:      Disposable Soft Synth Interface
Name:         dssi
Version:      1.1.1
Release:      %autorelease
# Automatically converted from old format: MIT - review is highly recommended.
License:      MIT
URL:          http://dssi.sourceforge.net/
Source0:      http://download.sf.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Source1:      http://download.sf.net/sourceforge/%{name}/README
# Fix 64bit plugin path
# http://sourceforge.net/tracker/?func=detail&aid=2798711&group_id=104230&atid=637350
Patch1:       %{name}-lib64.patch
Patch2:       %{name}-liblo.patch

BuildRequires: alsa-lib-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: ladspa-devel
BuildRequires: liblo-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: make
# for the examples
BuildRequires: qt4-devel

%description
Disposable Soft Synth Interface (DSSI, pronounced "dizzy") is a proposal for a
plugin API for software instruments (soft synths) with user interfaces,
permitting them to be hosted in-process by Linux audio applications. Think of
it as LADSPA-for-instruments, or something comparable to a simpler version of
VSTi.

%package examples
Summary:  DSSI plugin examples
License:  LicenseRef-Callaway-Public-Domain
Requires: %{name} = %{version}

%description examples
Example plugins for the Disposable Soft Synth Interface.

%package devel
Summary:  Libraries, includes, etc to develop DSSI applications
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:  LGPL-2.1-or-later
Requires: alsa-lib-devel
Requires: ladspa-devel
Requires: pkgconfig

%description devel
Libraries, include files, etc you can use to develop DSSI based applications.

%prep
%autosetup -p1

cp -a %{SOURCE1} README.%{version}

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%check
# Build and run the tests
make -C tests controller CFLAGS="$CFLAGS -Wno-error=cpp"
tests/controller

%files
%license COPYING
%doc README* ChangeLog doc/TODO
%{_bindir}/dssi_osc_send
%{_bindir}/dssi_osc_update
%{_bindir}/jack-dssi-host
%{_bindir}/dssi_analyse_plugin
%{_bindir}/dssi_list_plugins
%dir %{_libdir}/dssi
%{_mandir}/man1/*

%files examples
%{_libdir}/dssi/less_trivial_synth.so
%{_libdir}/dssi/less_trivial_synth
%{_libdir}/dssi/trivial_sampler.so
%{_libdir}/dssi/trivial_sampler
%{_libdir}/dssi/trivial_synth.so
%{_libdir}/dssi/karplong.so
%{_bindir}/trivial_sampler
%{_bindir}/trivial_synth
%{_bindir}/less_trivial_synth
%{_bindir}/karplong

%files devel
%license COPYING
%doc doc/*.txt
%{_includedir}/dssi.h
%{_libdir}/pkgconfig/dssi.pc

%changelog
%autochangelog
