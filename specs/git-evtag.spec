Summary: Strong GPG verification of git tags
Name: git-evtag
Version: 2022.1
Release: %autorelease

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
#VCS: https://github.com/cgwalters/git-evtag
URL: https://github.com/cgwalters/git-evtag
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc

BuildRequires: meson
BuildRequires: /usr/bin/xsltproc
BuildRequires: docbook-style-xsl
BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(gio-2.0)

Requires: git
Requires: gnupg2

%description
git-evtag wraps "git tag" functionality, adding stronger checksums
that cover the complete content.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/git-evtag.1*

%changelog
%autochangelog
