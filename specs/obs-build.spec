# Sadness, this directory is hardcoded everywhere
%global _libdir /usr/lib

# SUSE guys use OBS to automatically handle release numbers,
# when rebasing check what they are using on
# https://download.opensuse.org/repositories/openSUSE:/Tools/Fedora_41/src/
# update the obsrel to match the upstream release number
%global obsrel 465.1

Name:           obs-build
Version:        20250206
Release:        %{obsrel}.%{autorelease}
Summary:        A generic package build script

License:        (GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-build

# Tarball retrieved from
# https://build.opensuse.org/package/show/openSUSE:Tools/build
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Potentially not upstreamable patches
## Restore shebang to openstack-console script
Patch0501:      0501-Revert-Drop-shebang-line-from-openstack-console.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  /usr/bin/prove
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(FindBin)
BuildRequires:  (perl(YAML::PP) or perl(YAML::XS))
BuildRequires:  perl(POSIX)
Requires:       bash, perl-interpreter, binutils, tar
Requires:       gzip, bzip2, xz, zstd
Requires:       python3-websocket-client
Recommends:     perl(Archive::Tar)
Recommends:     /sbin/mkfs.ext3
Recommends:     /usr/bin/qemu-kvm
Recommends:     bsdtar
Recommends:     qemu-linux-user
Recommends:     zstd
Recommends:     perl(Config::IniFiles)
Recommends:     perl(Date::Language)
Recommends:     perl(Date::Parse)
Recommends:     perl(LWP::UserAgent)
Recommends:     perl(Net::SSL)
Recommends:     perl(Pod::Usage)
Recommends:     perl(Time::Zone)
Recommends:     perl(URI)
Recommends:     perl(XML::Parser)
Recommends:     perl(YAML::LibYAML)
Requires:       perl(POSIX)

Provides:       build = %{version}-%{release}
Requires:       %{name}-mkbaselibs = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     %{name}-mkdrpms = %{version}-%{release}
%endif

%description
This package provides a script for building packages in a chroot environment.
It is commonly used with the Open Build Service as the engine for building
packages for a wide variety of distributions.

%package mkbaselibs
Summary:        Tools to generate base library packages
Provides:       build-mkbaselibs = %{version}-%{release}
AutoReq:        no

%description mkbaselibs
This package contains the parts which may be installed in the inner build
system for generating base library packages.

%package mkdrpms
Summary:        Tools to generate DeltaRPMs
Provides:       build-mkdrpms = %{version}-%{release}
Requires:       deltarpm
Requires:       %{name} = %{version}-%{release}

%description mkdrpms
This package contains the parts which may be installed in the inner build
system for generating DeltaRPM packages.

%prep
%autosetup -p1


%build
# Nothing to do here


%install
%make_install
pushd %{buildroot}%{_libdir}/build/configs/
touch default.conf
test -e default.conf
popd

# Install man pages
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 build.1* %{buildroot}%{_mandir}/man1/
install -m 0644 buildvc.1* %{buildroot}%{_mandir}/man1/
install -m 0644 unrpm.1* %{buildroot}%{_mandir}/man1/

# Fix Python shebang for openstack-console
sed -e "s|#!/usr/bin/python|#!%{__python3}|" \
    -i %{buildroot}%{_libdir}/build/openstack-console

%check
%make_build test

%files
%license COPYING
%doc README.md
%{_bindir}/build
%{_bindir}/buildvc
%{_bindir}/unrpm
%{_bindir}/pbuild
%{_libdir}/build
%{_mandir}/man1/build.1*
%{_mandir}/man1/buildvc.1*
%{_mandir}/man1/unrpm.1*
%{_mandir}/man1/pbuild.1*
%exclude %{_libdir}/build/mkbaselibs
%exclude %{_libdir}/build/baselibs*
%exclude %{_libdir}/build/mkdrpms

%files mkbaselibs
%{_libdir}/build/mkbaselibs
%{_libdir}/build/baselibs*

%files mkdrpms
%{_libdir}/build/mkdrpms


%changelog
%autochangelog
