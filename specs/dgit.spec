Name:           dgit
Version:        15.3
Release:        %autorelease
Summary:        Integration between git and Debian-style archives
License:        GPL-3.0-or-later
URL:            https://browse.dgit.debian.org/dgit.git/
Source0:        https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
Requires:       coreutils
Requires:       curl
Requires:       devscripts
Requires:       dpkg-dev
Requires:       git
Requires:       tar
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
%make_install \
        prefix="%{_prefix}" \
        bindir="%{_bindir}" \
        mandir="%{_mandir}" \
        perldir="%{perl_vendorlib}" \
        infraexamplesdir="%{_pkgdocdir}/examples"

# Create dummy man pages for binaries that lack them, to silence rpmlint warnings.
# These will be symlinked to the main dgit man page.
for bin in git-playtree-setup mini-git-tag-fsck tag2upload-fetch-inputs tag2upload-obtain-origs; do
    echo ".so man1/dgit.1" > %{buildroot}%{_mandir}/man1/${bin}.1
done


%files
%{_bindir}/dgit
%{_bindir}/git-playtree-setup
%{_bindir}/mini-git-tag-fsck
%{_bindir}/tag2upload-fetch-inputs
%{_bindir}/tag2upload-obtain-origs
%{_datadir}/%{name}
%{_mandir}/man1/dgit*.1*
%{_mandir}/man1/git-playtree-setup.1*
%{_mandir}/man1/mini-git-tag-fsck.1*
%{_mandir}/man1/tag2upload-fetch-inputs.1*
%{_mandir}/man1/tag2upload-obtain-origs.1*
%{_mandir}/man7/dgit*.7*
%{perl_vendorlib}/Debian
%doc debian/changelog README.*
%license debian/copyright

%changelog
%autochangelog
