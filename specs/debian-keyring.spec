%global upstreamname debian-archive-keyring

Name:           debian-keyring
Version:        2025.1
Release:        %autorelease
Summary:        GnuPG archive keys of the Debian archive

License:        LicenseRef-Fedora-Public-Domain
URL:            http://packages.debian.org/unstable/admin/%{upstreamname}
Source0:        http://ftp.debian.org/debian/pool/main/d/%{upstreamname}/%{upstreamname}_%{version}.tar.xz
# Use gpg2
Patch0:         debian-keyring_gpg2.patch

BuildArch:      noarch
BuildRequires:  jetring
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  keyrings-filesystem
Requires:       keyrings-filesystem
# Add virtual Provides for the package name used in Debian
Provides:       %{upstreamname} = %{version}-%{release}

%description
The Debian project digitally signs its Release files. This package contains the
archive keys used for that.

%prep
%autosetup -p1 -n %{upstreamname}


%build
make


%install
%make_install


%files
%doc README
%exclude %{_sysconfdir}/apt/trusted.gpg.d
%{_keyringsdir}/*.gpg
%{_keyringsdir}/*.pgp


%changelog
%autochangelog
