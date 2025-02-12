Name: catatonit
Version: 0.2.1
Summary: A signal-forwarding process manager for containers
License: GPL-3.0-or-later
Release: %autorelease
%if %{defined copr_username}
# Set copr rpm build epoch to a very high value
Epoch: 101
%else
%if %{defined rhel}
# Bump epoch to 5 for RHEL
# Ref: https://bugzilla.redhat.com/show_bug.cgi?id=2257446
Epoch: 5
%endif
%endif
%if %{defined golang_arches_future}
ExclusiveArch: %{golang_arches_future}
%else
ExclusiveArch: aarch64 ppc64le s390x x86_64
%endif
URL: https://github.com/openSUSE/%{name}
# Tarball fetched from upstream
Source0: %{url}/archive/v%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: file
BuildRequires: libtool
Provides: podman-%{name} = %{version}-%{release}
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: glibc-static
BuildRequires: make

%description
Catatonit is a %{_sbindir}/init program for use within containers. It
forwards (almost) all signals to the spawned child, tears down
the container when the spawned child exits, and otherwise
cleans up other exited processes (zombies).

This is a reimplementation of other container init programs (such as
"tini" or "dumb-init"), but uses modern Linux facilities (such as
signalfd(2)) and has no additional features.

%prep
%autosetup -Sgit %{name}-%{version}

%build
./autogen.sh
%configure
CFLAGS="%{optflags} -fPIE -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE"
%{__make} %{?_smp_mflags}

# Make sure we *always* build a static binary. Otherwise we'll break containers
# that don't have the necessary shared libs.
file ./%{name} | grep 'statically linked'
if [ $? != 0 ]; then
   echo "ERROR: %{name} binary must be statically linked!"
   exit 1
fi

%install
install -dp %{buildroot}%{_libexecdir}/%{name}
install -p %{name} %{buildroot}%{_libexecdir}/%{name}
install -dp %{buildroot}%{_libexecdir}/podman
ln -s %{_libexecdir}/%{name}/%{name} %{buildroot}%{_libexecdir}/podman/%{name}

%check

%files
%license COPYING
%doc README.md
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/%{name}

%changelog
%autochangelog
