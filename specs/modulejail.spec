Name:           modulejail
Version:        1.6.3
Release:        %{autorelease}
Summary:        Shrink Linux kernel-module attack surface

License:        GPL-3.0-only
URL:            https://modulejail.com
Source0:        https://github.com/jnuyens/modulejail/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        https://github.com/jnuyens/modulejail/releases/download/v%{version}/v%{version}.tar.gz.sig
# The repository documents the signing key ID is 095F 5C8B 39AF 010E 7B61  5CD4 487B C00D 69C2 A955
#
# At the time I fetched this, the following signing key was present:
#
# sq inspect --cert=095F5C8B39AF010E7B615CD4487BC00D69C2A955 --keyring ./jnuyens.gpg
#  OpenPGP Certificate.
#
#        Fingerprint: 095F5C8B39AF010E7B615CD4487BC00D69C2A955
#    Public-key algo: RSA
#    Public-key size: 4096 bits
#      Creation time: 2026-05-24 19:26:07 UTC
#          Key flags: certification, signing
Source2:        https://github.com/jnuyens.gpg

BuildArch:      noarch
BuildRequires:  openpgpverify
Requires:       coreutils
Requires:       findutils
Requires:       gawk
Recommends:     curl

%global _description %{expand:
ModuleJail snapshots the set of currently loaded modules and writes a
modprobe.d blacklist for every kernel module not currently in use,
minus a built-in baseline and an optional sysadmin-supplied whitelist.

Aimed at Linux fleet operators who need to harden many servers against
the wave of AI-assisted kernel privilege-escalation discoveries. Every
additional loaded module is additional latent attack surface for the
next disclosed CVE.

No daemon, no continuous monitoring, no AI inside the tool. One shell
script, run once on a steady-state host, that writes one modprobe.d
blacklist file.}

%description %{_description}


%prep
%{openpgpverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version} -p1


%build
sed -i 's/__VERSION__/%{version}/' man/modulejail.8.in
sed -i "s/__DATE__/$(date -u -d @${SOURCE_DATE_EPOCH} +%Y-%m-%d)/" man/modulejail.8.in
# Updates are shipped via dnf
sed -i 's/^UPDATE_CHECK_DEFAULT=1$/UPDATE_CHECK_DEFAULT=0/' modulejail


%install
install -Dm755 modulejail   %{buildroot}%{_bindir}/modulejail
install -Dm644 man/modulejail.8.in %{buildroot}%{_mandir}/man8/modulejail.8
# Stage the dracut strip hook so the package owns it (see gh #19 and
# docs/DEFENSE-IN-DEPTH.md). It keeps the blacklist out of rebuilt
# initramfs images; dracut picks it up on the next kernel install.
./modulejail --install-initramfs-hook --initramfs-builder dracut --destdir %{buildroot}


%files
%license LICENSE
%doc README.md
%{_bindir}/modulejail
%{_mandir}/man8/modulejail.8*
%dir %{_prefix}/lib/dracut/modules.d/99modulejail-strip
%{_prefix}/lib/dracut/modules.d/99modulejail-strip/module-setup.sh

%changelog
%{autochangelog}
