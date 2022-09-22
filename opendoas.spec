

Name:           opendoas
Version:        6.8.2
Release:        %autorelease
Summary:        Portable fork of the OpenBSDs doas command

# ISC: main program
# BSD-3-Clause: libopenbsd
License:        ISC AND BSD-3-Clause
URL:            https://github.com/Duncaen/OpenDoas
Source0:        %url/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %url/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:        https://xn--1xa.duncano.de/duncan.asc
# Remove chown from Makefile install as it is not permitted in mock
Patch0:         01-patch-makefile-to-remove-chown.patch

BuildRequires:  byacc
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pam-devel

Provides:       doas = %{version}-%{release}
Provides:       bundled(libopenbsd)

%description
doas is a minimal replacement for the venerable sudo. It was initially written
by Ted Unangst of the OpenBSD project to provide 95% of the features of sudo
with a fraction of the codebase.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%set_build_flags
# Non standard build script
./configure --prefix=%{_prefix} --with-timestamp --with-pam
%make_build

%install
%make_install

mkdir -p  %{_sysconfdir}
cat > %{buildroot}%{_sysconfdir}/doas.conf << EOF
# Allow wheel by default
permit :wheel
EOF

mkdir -p  %{buildroot}%{_sysconfdir}/pam.d
cat > %{buildroot}%{_sysconfdir}/pam.d/doas << EOF
#%%PAM-1.0
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    optional     pam_keyinit.so revoke
session    required     pam_limits.so
session    include      system-auth
EOF

%files
%license LICENSE
%doc README.md
%attr(4755,root,root) %{_bindir}/doas
%config(noreplace) %{_sysconfdir}/doas.conf
%config(noreplace) %{_sysconfdir}/pam.d/doas
%{_mandir}/man1/doas.1*
%{_mandir}/man5/doas.conf.5*

%changelog
%autochangelog
