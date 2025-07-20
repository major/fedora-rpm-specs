%global debug_package %{nil}
%global mver 3.0

Name:           haunt
Version:        0.3.0
Release:        %{autorelease}
Summary:        Hackable static site generator in guile scheme

# Code is GPL-3.0-or-later
# Documentation is GFDL-1.3-or-later
License:        GPL-3.0-or-later AND GFDL-1.3-or-later
URL:            https://dthompson.us/projects/haunt.html
Source0:        https://files.dthompson.us/releases/haunt/haunt-%{version}.tar.gz
Source1:        https://files.dthompson.us/releases/haunt/haunt-%{version}.tar.gz.asc
# https://keyserver.ubuntu.com/pks/lookup?search=8CCBA7F552B9CBEAE1FB29158328C7470FF1D807&fingerprint=on&op=index
Source2:        8ccba7f552b9cbeae1fb29158328c7470ff1d807.asc

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  guile30-devel
BuildRequires:  gnupg2
BuildRequires:  guile-commonmark
BuildRequires:  guile-reader-devel
# hut is not available in i686
%ifnarch %{ix86}
BuildRequires:   hut
%endif
BuildRequires:   make
BuildRequires:   rsync
BuildRequires:   tar
BuildRequires:   texinfo
Requires:       guile-commonmark
Requires:       guile-reader
%ifnarch %{ix86}
Requires:       hut
%endif
Requires:       rsync
Requires:       tar
# post.scm test fails
ExcludeArch:  %{ix86}

%description
Haunt is a simple, functional, hackable static site generator that gives
authors the ability to treat websites as Scheme programs.

By giving authors the full expressive power of Scheme, they are able to
control every aspect of the site generation process. Haunt provides a simple,
functional build system that can be easily extended for this purpose.

Haunt has no opinion about what markup language authors should use to write
posts, though it comes with support for the popular Markdown format. Likewise,
Haunt has no opinion about how authors structure their sites. Though it comes
with support for building simple blogs or Atom feeds, authors should feel
empowered to tweak, replace, or create builders to do things that aren't
provided out-of-the-box.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%build
autoreconf -vif
%configure
%make_build
make info

%install
%make_install
DESTDIR=%{buildroot} make install-info
test -f %{buildroot}/%{_infodir}/dir && rm %{buildroot}/%{_infodir}/dir

%check
make check

%files
%license COPYING
%doc README
%{_bindir}/haunt
%{_infodir}/haunt.info*
%dir %{_datadir}/guile
%dir %{_datadir}/guile/site
%dir %{_datadir}/guile/site/%{mver}/
%dir %{_datadir}/guile/site/%{mver}/haunt
%{_datadir}/guile/site/%{mver}/haunt/*.scm
%dir %{_datadir}/guile/site/%{mver}/haunt/builder
%{_datadir}/guile/site/%{mver}/haunt/builder/*.scm
%dir %{_datadir}/guile/site/%{mver}/haunt/publisher
%{_datadir}/guile/site/%{mver}/haunt/publisher/*.scm
%dir %{_datadir}/guile/site/%{mver}/haunt/reader
%{_datadir}/guile/site/%{mver}/haunt/reader/*.scm
%dir %{_datadir}/guile/site/%{mver}/haunt/serve
%{_datadir}/guile/site/%{mver}/haunt/serve/*.scm
%dir %{_datadir}/guile/site/%{mver}/haunt/skribe
%{_datadir}/guile/site/%{mver}/haunt/skribe/*.scm
%dir %{_datadir}/guile/site/%{mver}/haunt/ui
%{_datadir}/guile/site/%{mver}/haunt/ui/*.scm
%dir %{_datadir}/guile/site/%{mver}/haunt/watch
%{_datadir}/guile/site/%{mver}/haunt/watch/*.scm
%{_datadir}/haunt/
%dir %{_libdir}/guile/%{mver}/site-ccache/haunt/
%{_libdir}/guile/%{mver}/site-ccache/haunt/*.go
%dir %{_libdir}/guile/%{mver}/site-ccache/haunt/builder
%{_libdir}/guile/%{mver}/site-ccache/haunt/builder/*.go
%dir %{_libdir}/guile/%{mver}/site-ccache/haunt/publisher
%{_libdir}/guile/%{mver}/site-ccache/haunt/publisher/*.go
%dir %{_libdir}/guile/%{mver}/site-ccache/haunt/reader
%{_libdir}/guile/%{mver}/site-ccache/haunt/reader/*.go
%dir %{_libdir}/guile/%{mver}/site-ccache/haunt/serve
%{_libdir}/guile/%{mver}/site-ccache/haunt/serve/*.go
%dir %{_libdir}/guile/%{mver}/site-ccache/haunt/skribe
%{_libdir}/guile/%{mver}/site-ccache/haunt/skribe/*.go
%dir %{_libdir}/guile/%{mver}/site-ccache/haunt/ui
%{_libdir}/guile/%{mver}/site-ccache/haunt/ui/*.go
%dir %{_libdir}/guile/%{mver}/site-ccache/haunt/watch
%{_libdir}/guile/%{mver}/site-ccache/haunt/watch/*.go

%changelog
%autochangelog 
