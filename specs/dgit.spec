Name:           dgit
Version:        13.17
Release:        %autorelease
Summary:        Integration between git and Debian-style archives
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://browse.dgit.debian.org/dgit.git/
Source0:        https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.gz
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  make
Requires:       devscripts
Requires:       curl
Requires:       git
Requires:       dpkg-dev
Requires:       tar
Requires:       coreutils
BuildArch:      noarch

%description
dgit (with the associated infrastructure) makes it possible to
treat the Debian archive as a git repository:

"dgit push" constructs uploads from git commits

"dgit clone" and "dgit fetch" construct git commits from uploads.


%prep
%autosetup -n work

%build


%check
# dput is not packaged,
# possibly need Internet connectivity anyway
#EMAIL=jello.biafra@dead.kennedys \
#       tests/using-intree make -f tests/Makefile


%install
# We don't do an install-infra, not sure if the Debian specific
# infrastructure tools would make sense to be packaged in Fedora.
make install DESTDIR="%{buildroot}" \
        prefix="%{_prefix}" \
        bindir="%{_bindir}" \
        mandir="%{_mandir}" \
        perldir="%{perl_vendorlib}" \
        infraexamplesdir="%{_pkgdocdir}/examples"


%files
%{_bindir}/dgit
%{_bindir}/git-playtree-setup
%{_bindir}/mini-git-tag-fsck
%{_bindir}/tag2upload-obtain-origs
%{_datadir}/%{name}
%{_mandir}/man1/dgit*.1*
%{_mandir}/man7/dgit*.7*
%{perl_vendorlib}/Debian
%doc debian/changelog README.*
%license debian/copyright

%changelog
%autochangelog
