Name:           pdfpc
Version:        4.6.0
Release:        %autorelease
Summary:        A GTK based presentation viewer application for GNU/Linux

License:        GPL-3.0-or-later
URL:            https://%{name}.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz

# https://github.com/pdfpc/pdfpc/pull/687
Patch0:         https://patch-diff.githubusercontent.com/raw/pdfpc/pdfpc/pull/687.patch
BuildRequires:  git-core

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  json-glib-devel
BuildRequires:  libmarkdown-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libgee-devel
BuildRequires:  pango-devel
BuildRequires:  poppler-glib-devel
# disable until upstream finishes porting to libsoup3
# https://github.com/pdfpc/pdfpc/issues/671
# https://github.com/pdfpc/pdfpc/issues/664
#BuildRequires:  pkgconfig(libsoup3)
#BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  vala libvala-devel
BuildRequires:  qrencode-devel

%description
pdfpc is a GTK based presentation viewer application for GNU/Linux which uses
Keynote like multi-monitor output to provide meta information to the speaker
during the presentation. It is able to show a normal presentation window on one
screen, while showing a more sophisticated overview on the other one providing
information like a picture of the next slide, as well as the left over time
till the end of the presentation. The input files processed by pdfpc are PDF
documents, which can be created using nearly any of today's presentation
software.

%prep
%autosetup -n %{name}-%{version} -S git

%build
# temporarily disable REST until it is ported to libsoup3
# disable markdown view until it is ported to webkit2gtk-4.1
%cmake -DSYSCONFDIR=/etc -DREST=OFF -DMDVIEW=OFF .
%cmake_build


%install
%cmake_install


%files
%doc README.rst CHANGELOG.rst
%{_bindir}/%{name}
%license LICENSE.txt
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*
%{_datadir}/%{name}


%changelog
%autochangelog
