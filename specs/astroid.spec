Name:           astroid
Version:        0.17
Release:        %{autorelease}
Summary:        Notmuch e-mail client

License:        GPL-3.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause
URL:            https://github.com/astroidmail/astroid
Source0:        %{url}/archive/v%{version}/astroid-%{version}.tar.gz
Source1:        astroid.metainfo.xml

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel
BuildRequires:  gmime30-devel
BuildRequires:  gnupg2
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  libsass-devel
BuildRequires:  libpeas-devel
BuildRequires:  ninja-build
BuildRequires:  notmuch-devel
BuildRequires:  protobuf-devel
BuildRequires:  scdoc
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  vte291-devel
# test requirements
BuildRequires:  cmark
BuildRequires:  desktop-file-utils
BuildRequires:  gnupg2-gpg-agent
BuildRequires:  libappstream-glib
BuildRequires:  w3m
BuildRequires:  xorg-x11-server-Xvfb
Requires: hicolor-icon-theme

%description
Astroid is a lightweight and fast Mail User Agent that provides a graphical
interface to searching, displaying and composing email, organized in threads
and tags. Astroid uses the notmuch backend for blazingly fast searches
through tons of email. Astroid searches, displays and composes emails - and
rely on other programs for fetching, syncing and sending email.

%prep
%autosetup

# Ensure library gets installed in correct location
sed -i "s|lib/astroid/web-extensions|%{_lib}/astroid/web-extensions|g" CMakeLists.txt

%build
%cmake -G Ninja
%cmake_build


%install
%cmake_install
mkdir -p  %{buildroot}/%{_metainfodir}/
install -Dpm0644 %{SOURCE1} %{buildroot}/%{_metainfodir}/

%check
xvfb-run %__ctest \
         --test-dir "%{__cmake_builddir}" \
         --output-on-failure \
         --force-new-ctest-process \
         --timeout 6000 \
         -j1
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/astroid.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/astroid.desktop

%files
%license LICENSE.md
%license COPYING.GPL-3.0+
%license COPYING.LGPL-2.1+
%doc README.md
%doc History.txt
%{_bindir}/astroid
%dir %{_libdir}/astroid
%dir %{_libdir}/astroid/web-extensions
%{_libdir}/astroid/web-extensions/libtvextension.so
%{_datadir}/astroid/
%{_mandir}/man1/astroid.1*
%{_metainfodir}/astroid.metainfo.xml
%{_datadir}/applications/astroid.desktop
%{_datadir}/icons/hicolor/scalable/apps/astroid.svg
%{_datadir}/icons/hicolor/512x512/apps/astroid.png

%changelog
%autochangelog 
