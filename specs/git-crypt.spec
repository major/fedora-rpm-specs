Name:       git-crypt
Version:    0.8.0
Release:    %autorelease
Summary:    Transparent file encryption in git

# MIT/X11 (BSD like): fhstream.{hpp|cpp} and parse_options.{hpp|cpp}
# GPLv3+: all other source files
License:    GPL-3.0-or-later AND X11
URL:        https://www.agwa.name/projects/git-crypt
Source0:    %{URL}/downloads/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  make

Requires:       git

%description
git-crypt enables transparent encryption and decryption of files in a
git repository. Files which you choose to protect are encrypted when
committed, and decrypted when checked out. git-crypt lets you freely
share a repository containing a mix of public and private
content. git-crypt gracefully degrades, so developers without the
secret key can still clone and commit to a repository with encrypted
files. This lets you store your secret material (such as keys or
passwords) in the same repository as your code, without requiring you
to lock down your entire repository.

%prep
%autosetup
sed -i "s|^\tinstall -|\t\$(INSTALL) -|" Makefile

%build
export DOCBOOK_XSL=%{_datadir}/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl
export ENABLE_MAN=yes
export CXXFLAGS="%{optflags} -DOPENSSL_API_COMPAT=0x30000000L"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
%make_install ENABLE_MAN=yes PREFIX=%{_prefix}

%files
%license COPYING
%doc README README.md
%{_bindir}/%{name}
%{_mandir}/man1/git-crypt.1*


%changelog
%autochangelog
