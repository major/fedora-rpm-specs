Name:           aoetools
Version:        37
Release:        %autorelease
Summary:        Tools for using ATA over Ethernet
License:        GPL-2.0-only
URL:            https://github.com/OpenAoE/aoetools

%global git_tag %{name}-%{version}
Source0:        https://github.com/OpenAoE/aoetools/archive/%{git_tag}/%{name}-%{git_tag}.tar.gz
Source1:        60-aoe.rules

Patch0:         %{name}-makefile.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

%description
The aoetools are programs that assist in using ATA over Ethernet on 
systems with version 2.6 and newer Linux kernels.

%prep
%autosetup -p1 -n %{name}-%{git_tag}

%build
%make_build

%install
%make_install SBINDIR="%{_bindir}"
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/60-aoe.rules

%check
# Basic sanity check to ensure binaries are built and have correct permissions
for cmd in aoeping aoecfg aoe-sancheck aoe-discover aoe-interfaces \
           aoe-mkshelf aoe-revalidate aoe-flush aoe-stat aoe-mkdevs \
           aoe-version coraid-update; do
    test -x %{buildroot}%{_bindir}/$cmd
done

%files
%license COPYING
%doc HACKING NEWS README devnodes.txt
%{_bindir}/aoe*
%{_bindir}/coraid-update
%{_mandir}/man8/aoe*.8*
%{_mandir}/man8/coraid-update.8*
%{_udevrulesdir}/60-aoe.rules

%changelog
%autochangelog
