Name:               sshuttle
Version:            1.2.0
Release:            %autorelease
Summary:            Transparent Proxy VPN
Source0:            https://github.com/sshuttle/sshuttle/archive/refs/tags/v%{version}.tar.gz
URL:                https://github.com/%{name}/%{name}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:            LGPL-2.0-or-later
BuildArch:          noarch

BuildRequires:      make
BuildRequires:      python3-devel
BuildRequires:      texinfo
BuildRequires:      python3-sphinx

%if 0%{?fedora}
# For tests on fedora
# We don't run tests on epel due to missing requirements
# We specify tests here because upstream doesn't split them out in pyproject
BuildRequires:      python3-pytest
BuildRequires:      python3-pytest-cov
BuildRequires:      python3-pytest-mock
BuildRequires:      python3-psutil
%endif

Requires:           iptables
Requires:           openssh-clients

%description
Transparent proxy server that works as a poor man's VPN. Forwards over ssh.
Doesn't require admin. Works with Linux and MacOS. Supports DNS tunneling.

%prep
%autosetup -p1 -n %{name}-%{version}
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Build docs
pushd docs
make man
make info
popd


%install
%pyproject_install
%pyproject_save_files -L sshuttle

# Install docs
pushd docs
# Man
mkdir -p %{buildroot}/%{_mandir}/man1
mv _build/man/%{name}.1 %{buildroot}/%{_mandir}/man1
# Info
mkdir -p %{buildroot}/%{_infodir}
mv _build/texinfo/%{name}.info %{buildroot}/%{_infodir}
popd


%check
%if 0%{?fedora}
%{pytest}
%endif

%files -f %{pyproject_files}
%license LICENSE
%{_mandir}/man1/%{name}.1.*
%{_infodir}/%{name}.info.*
%{_bindir}/sshuttle


%changelog
%autochangelog
