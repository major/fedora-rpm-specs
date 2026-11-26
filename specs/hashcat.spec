
%global makeflags PREFIX=%{_prefix} LIBRARY_FOLDER=%{_libdir} SHARED_ROOT_FOLDER=%{_libdir} DOCUMENT_FOLDER=%{_docdir}/hashcat-doc SHARED=1 USE_SYSTEM_OPENCL=1 MAINTAINER_MODE=1

Name: hashcat
Version: 8.0.0
Release: %autorelease

License: MIT AND LicenseRef-Fedora-Public-Domain AND BSD-2-Clause AND Apache-2.0
URL: https://github.com/%{name}/%{name}
Summary: Advanced password recovery utility

Source0: https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: opencl-headers
%ifarch aarch64
BuildRequires: sse2neon-devel
%endif

BuildRequires: gcc
BuildRequires: make
BuildRequires: chrpath

Provides: bundled(scrypt-jane)
Provides: bundled(yescrypt)
Provides: bundled(libargon2) = 20190702
Provides: bundled(7zip) = 26.02

Recommends: %{name}-doc
Recommends: xz-libs%{?_isa}
Recommends: zlib-ng-compat%{?_isa}
Recommends: libzstd%{?_isa}
Recommends: python3
Recommends: openssl-libs%{?_isa}

# Upstream does not support Big Endian architectures.
# Upstream source code does not longer build for ppc64le: https://bugzilla.redhat.com/show_bug.cgi?id=2407234
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86} ppc64 s390x ppc64le

%description
Hashcat is the world's fastest and most advanced password recovery
utility, supporting five unique modes of attack for over 200
highly-optimized hashing algorithms. hashcat currently supports
CPUs, GPUs, and other hardware accelerators on Linux, Windows,
and Mac OS, and has facilities to help enable distributed password
cracking.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%package doc
Summary: Documentation files for %{name}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch

%description doc
%{summary}.

%prep
%autosetup -p1
rm -rf deps/{OpenCL-Headers,litepcie-2026.08,sse2neon}
sed -e 's/\.\/hashcat/hashcat/' -i *.sh
chmod -x *.sh
rm -f modules/.lock

%build
%set_build_flags
%make_build %{makeflags} DEBUG=1

%install
%make_install %{makeflags}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -m 0744 -p extra/tab_completion/hashcat.sh %{buildroot}%{_datadir}/bash-completion/completions/%{name}
find %{buildroot}%{_libdir}/%{name}/ -name '.gitkeep' -type f -delete
find %{buildroot}%{_bindir} -name '*hashcat.pl' -type f -delete
find %{buildroot}%{_bindir} -name '*hashcat.py' -type f -delete
find %{buildroot}%{_libdir}/%{name}/modules -name '*.so' -type f -exec chrpath --delete {} \;
find %{buildroot}%{_libdir}/%{name}/bridges -name '*.so' -type f -exec chrpath --delete {} \;
find %{buildroot}%{_libdir}/%{name}/feeds -name '*.so' -type f -exec chrpath --delete {} \;
find %{buildroot}%{_libdir}/%{name} -name '*.so' -type f -exec chmod 0755 {} +
chrpath --delete %{buildroot}%{_bindir}/%{name}
rm -rf %{buildroot}%{_docdir}/%{name}-doc/extra
rm -rf %{buildroot}%{_libdir}/%{name}/extra

%files
%license docs/license.txt
%doc README.md
%{_libdir}/lib%{name}.so.8{,.*}
%{_libdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%files doc
%doc docs/ charsets/ masks/ rules/ tables/
%doc example.dict example*.sh example*.hash

%changelog
%autochangelog
