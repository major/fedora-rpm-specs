%define fedora_dist_version 45
%define rhel_dist_version 11

%global dist %{?eln:.eln%{eln}}

# Changes should be submitted as pull requests under
#     https://src.fedoraproject.org/rpms/fedora-eln-release

Summary:        Fedora ELN release files
Name:           fedora-eln-release
Version:        11.0
Release:        %autorelease -p
License:        MIT
URL:            https://fedoraproject.org/

Source1:        LICENSE
Source2:        Fedora-Legal-README.txt

Source8:        fedora-eln.repo

Source14:       80-server.preset
Source19:       distro-template.swidtag
Source31:       20-fedora-defaults.conf
Source32:       75-eln.preset

BuildArch:      noarch

BuildRequires:  redhat-rpm-config > 121-1
BuildRequires:  systemd-rpm-macros

Provides:       fedora-release = %{fedora_dist_version}-%{release}
Obsoletes:      fedora-release-common < 46
Obsoletes:      fedora-release-eln < 46
Obsoletes:      fedora-release-identity-eln < 46

Provides:       system-release = %{version}-%{release}
Provides:       system-release(releasever) = eln
Provides:       system-release(%{rhel_dist_version})
Conflicts:      system-release

Provides:       redhat-release = %{rhel_dist_version}

Requires:       fedora-eln-repos = %{version}-%{release}

# We need to ensure that the systemd presets common to all Fedora installs are
# pulled in here. Spin-specific ones are located further below. These are kept
# in a separate file to make life easier for Fedora Remixes to reuse them.
Requires:       redhat-systemd-presets

# When running a compose for ELN, we want to make sure that we pull in the
# correct templates when lorax is installed. This Suggests: will clue
# libdnf to use this set of templates instead of lorax-templates-generic.
Suggests: lorax-templates-rhel

# Both netcat and nmap-ncat provide /usr/bin/nc, so prefer the latter like
# RHEL does.
Suggests: nmap-ncat

# Prefer over original standalone versions (without pipewire- prefix)
Suggests: pipewire-jack-audio-connection-kit
Suggests: pipewire-jack-audio-connection-kit-devel
Suggests: pipewire-pulseaudio

# Prefer over Lmod for Provides: environment(modules)
Suggests: environment-modules

# Prefer over elinks, w3m for Provides: text-www-browser
Suggests: lynx

# Prefer over bind9-next and its subpackages
Suggests: bind
Suggests: bind-devel
Suggests: bind-dnssec-utils
Suggests: bind-utils

# Default OpenJDK version, prefer over other versions for
# Provides: java, java-devel, java-headless, maven-jdk-binding, etc.
Suggests: java-25-openjdk
Suggests: java-25-openjdk-devel
Suggests: java-25-openjdk-headless
Suggests: maven-openjdk25
Suggests: maven4-openjdk25

# Default Node.js version, prefer over other versions for
# nodejs(api), nodejs(engine), /usr/bin/node, /usr/bin/npm
Suggests: nodejs24
Suggests: nodejs24-bin
Suggests: nodejs24-npm
Suggests: nodejs24-npm-bin

# Prefer over Fedora freeipa (same code, different name, each Provides the other)
Suggests: ipa-client
Suggests: ipa-client-common
Suggests: ipa-client-epn
Suggests: ipa-client-samba
Suggests: ipa-common
Suggests: ipa-selinux
Suggests: ipa-server
Suggests: ipa-server-common
Suggests: ipa-server-dns
Suggests: ipa-server-trust-ad
Suggests: ipa-healthcheck
Suggests: ipa-healthcheck-core

# Prefer over exim, opensmtpd, sendmail for Provides: MTA smtpd smtpdaemon server(smtp)
Suggests: postfix

# Prefer over cdrkit/genisoimage for /usr/bin/mkisofs
Suggests: xorriso

# Prefer over sdubby which also Provides: grubby
Suggests: grubby

# Prefer over arptables-legacy, ebtables-legacy, and iptables-legacy
# for Provides: arptables-helper, ebtables, or iptables
Suggests: iptables-nft

# Prefer over blis for libblas*.so.3()(64bit)
Suggests: blas
Suggests: blas64

# Prefer over wget2-wget for wget
Suggests: wget1-wget

# Prefer over fedora-logos(-httpd) for system-logos(-httpd)
Suggests: fedora-eln-logos
Suggests: fedora-eln-logos-httpd

%description
Fedora ELN release files such as various /etc/ files that define the release
and systemd preset files that determine which services are enabled by default.
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/DefaultServices/ for details.

%package -n fedora-eln-repos
Summary:        Fedora ELN package repositories
Provides:       system-repos = %{version}-%{release}
Provides:       fedora-eln-repos(%{rhel_dist_version}) = %{version}
Provides:       fedora-repos-eln = %{fedora_dist_version}-%{release}
Obsoletes:      fedora-repos-eln < 46
Requires:       fedora-gpg-keys = %{fedora_dist_version}

%description -n fedora-eln-repos
This package provides the package repository files for Fedora ELN.


%prep
mkdir -p licenses
cp %{SOURCE1} licenses/LICENSE
cp %{SOURCE2} licenses/Fedora-Legal-README.txt

%build

%install
install -d %{buildroot}%{_prefix}/lib
echo "Fedora ELN %{rhel_dist_version}" > %{buildroot}%{_prefix}/lib/fedora-release
echo "cpe:/o:fedoraproject:fedora-eln:%{rhel_dist_version}" > %{buildroot}%{_prefix}/lib/system-release-cpe

# Symlink the -release files
install -d %{buildroot}%{_sysconfdir}
ln -s ../usr/lib/fedora-release %{buildroot}%{_sysconfdir}/fedora-release
ln -s ../usr/lib/system-release-cpe %{buildroot}%{_sysconfdir}/system-release-cpe
ln -s fedora-release %{buildroot}%{_sysconfdir}/redhat-release
ln -s fedora-release %{buildroot}%{_sysconfdir}/system-release

# -------------------------------------------------------------------------
# Definitions for /etc/os-release and for macros in macros.dist.  These
# macros are useful for spec files where distribution-specific identifiers
# are used to customize packages.

# Name of vendor / name of distribution. Typically used to identify where
# the binary comes from in --help or --version messages of programs.
# Examples: gdb.spec, clang.spec
%global dist_vendor Fedora
%global dist_name   Fedora ELN

# The namespace for purl
# https://github.com/package-url/purl-spec
# for example as in: pkg:rpm/fedora/python-setuptools@69.2.0-10.fc41?arch=src"
# Note that we use "fedora" even for Fedora ELN
%global dist_purl_namespace fedora

# URL of the homepage of the distribution
# Example: gstreamer1-plugins-base.spec
%global dist_home_url https://fedoraproject.org/

# Bugzilla / bug reporting URLs shown to users.
# Examples: gcc.spec
%global dist_bug_report_url https://bugzilla.redhat.com/

# debuginfod server, as used in elfutils.spec.
%global dist_debuginfod_url ima:enforcing https://debuginfod.fedoraproject.org/ ima:ignore
# -------------------------------------------------------------------------

cat <<EOF >os-release
NAME="%{dist_name}"
VERSION="%{rhel_dist_version}"
RELEASE_TYPE=development
ID=eln
ID_LIKE="rhel centos fedora"
VERSION_ID=%{rhel_dist_version}
PRETTY_NAME="Fedora ELN %{rhel_dist_version}"
ANSI_COLOR="0;31"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora-eln:%{rhel_dist_version}"
DEFAULT_HOSTNAME="eln"
VENDOR_NAME="%{dist_vendor}"
VENDOR_URL="%{dist_home_url}"
HOME_URL="%{dist_home_url}"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/eln/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="%{dist_bug_report_url}"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=rawhide
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=rawhide
VARIANT="ELN"
VARIANT_ID=eln
EOF

# Create the symlink for /etc/os-release
ln -s ../usr/lib/os-release %{buildroot}%{_sysconfdir}/os-release

# Create the common /etc/issue
echo "\S" > %{buildroot}%{_prefix}/lib/issue
echo "Kernel \r on \m (\l)" >> %{buildroot}%{_prefix}/lib/issue
echo >> %{buildroot}%{_prefix}/lib/issue
ln -s ../usr/lib/issue %{buildroot}%{_sysconfdir}/issue

# Create /etc/issue.net
echo "\S" > %{buildroot}%{_prefix}/lib/issue.net
echo "Kernel \r on \m (\l)" >> %{buildroot}%{_prefix}/lib/issue.net
ln -s ../usr/lib/issue.net %{buildroot}%{_sysconfdir}/issue.net

# Create /etc/issue.d
mkdir -p %{buildroot}%{_sysconfdir}/issue.d

# ELN installs the Server presets as well
install -Dm0644 %{SOURCE14} -t %{buildroot}%{_presetdir}/

# ELN may override some presets from Fedora to simplify branching for CentOS Stream
install -Dm0644 %{SOURCE32} -t %{buildroot}%{_presetdir}/

# Set up the dist tag macros
install -d -m 755 %{buildroot}%{_rpmconfigdir}/macros.d
cat >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.dist << EOF
# dist macros.

%%__bootstrap         ~bootstrap
%%rhel              %{rhel_dist_version}
%%el%{rhel_dist_version}                1
# Although eln is set in koji tags, we put it in the macros.dist file for local and mock builds.
%%eln              %{eln}
%%distcore            .eln%%{eln}
%%dist                %%{!?distprefix0:%%{?distprefix}}%%{expand:%%{lua:for i=0,9999 do print("%%{?distprefix" .. i .."}") end}}%%{distcore}%%{?with_bootstrap:%%{__bootstrap}}%%{?buildrelease:+build%%{buildrelease}}
%%dist_vendor         %{dist_vendor}
%%dist_name           %{dist_name}
%%dist_purl_namespace %{dist_purl_namespace}
%%dist_home_url       %{dist_home_url}
%%dist_bug_report_url %{dist_bug_report_url}
%%dist_debuginfod_url %{dist_debuginfod_url}
EOF

# Create distro-level SWID tag file
install -d %{buildroot}%{_swidtagdir}
sed -e "s#\$version#%{rhel_dist_version}#g" -e 's/<!--.*-->//;/^$/d' %{SOURCE19} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-ELN-%{rhel_dist_version}.swidtag
install -d %{buildroot}%{_sysconfdir}/swid/swidtags.d
ln -s --relative %{buildroot}%{_swidtagdir} %{buildroot}%{_sysconfdir}/swid/swidtags.d/fedoraproject.org

# Install DNF 5 configuration defaults
install -Dm0644 %{SOURCE31} -t %{buildroot}%{_prefix}/share/dnf5/libdnf.conf.d/

# Install DNF repo file
install -Dm0644 %{SOURCE8} -t %{buildroot}%{_sysconfdir}/yum.repos.d/


%files
%license licenses/LICENSE licenses/Fedora-Legal-README.txt
%{_prefix}/lib/fedora-release
%{_prefix}/lib/system-release-cpe
%{_sysconfdir}/os-release
%{_sysconfdir}/fedora-release
%{_sysconfdir}/redhat-release
%{_sysconfdir}/system-release
%{_sysconfdir}/system-release-cpe
%attr(0644,root,root) %{_prefix}/lib/issue
%config(noreplace) %{_sysconfdir}/issue
%attr(0644,root,root) %{_prefix}/lib/issue.net
%config(noreplace) %{_sysconfdir}/issue.net
%dir %{_sysconfdir}/issue.d
%attr(0644,root,root) %{_rpmconfigdir}/macros.d/macros.dist
%dir %{_swidtagdir}
%{_swidtagdir}/org.fedoraproject.Fedora-ELN-%{rhel_dist_version}.swidtag
%dir %{_sysconfdir}/swid
%{_sysconfdir}/swid/swidtags.d
%{_prefix}/share/dnf5/libdnf.conf.d/20-fedora-defaults.conf
%{_presetdir}/80-server.preset
%{_presetdir}/75-eln.preset

%files -n fedora-eln-repos
%{_sysconfdir}/yum.repos.d/fedora-eln.repo


%changelog
%autochangelog
