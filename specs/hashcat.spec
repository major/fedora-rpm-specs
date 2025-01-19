# hashcat require an ancient version of minizip.
# On Fedora we can use compatibility package, but
# on RHEL we must use bundled version.
%if 0%{?fedora}
%bcond_without zlib
%else
%bcond_with zlib
%endif

%global makeflags PREFIX=%{_prefix} LIBRARY_FOLDER=%{_libdir} SHARED_ROOT_FOLDER=%{_libdir} DOCUMENT_FOLDER=%{_docdir}/hashcat-doc SHARED=1 USE_SYSTEM_OPENCL=1 USE_SYSTEM_XXHASH=1 ENABLE_UNRAR=0

%if %{with zlib}
%global makeflags %(echo %{makeflags} USE_SYSTEM_ZLIB=1)
%else
%global makeflags %(echo %{makeflags} USE_SYSTEM_ZLIB=0)
%endif

Name: hashcat
Version: 6.2.6
Release: 8%{?dist}

License: MIT AND LicenseRef-Fedora-Public-Domain
URL: https://github.com/%{name}/%{name}
Summary: Advanced password recovery utility

# The official upstream tarball contains some non-free components.
# We cannot use it on Fedora for legal reasons.
# Use ./make_tarball.sh to generate a new stripped tarball.
Source0: %{name}-%{version}-clean.tar.xz
Source1: make_tarball.sh
Patch0: %{name}-build-fixes.patch

BuildRequires: opencl-headers
BuildRequires: xxhash-devel
BuildRequires: gcc
BuildRequires: make

%if %{with zlib}
BuildRequires: zlib-devel
BuildRequires: minizip-compat-devel
%else
Provides: bundled(zlib) = 1.2.11
Provides: bundled(minizip) = 1.2.11
%endif

%if 0%{?fedora}
Recommends: mesa-libOpenCL%{?_isa}
Recommends: pocl%{?_isa}
Recommends: %{name}-doc = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

# Upstream does not support Big Endian architectures.
ExcludeArch: ppc64 s390x

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
rm -rf deps/{OpenCL-Headers,xxHash}
%if %{with zlib}
rm -rf deps/zlib
%endif
sed -e 's/\.\/hashcat/hashcat/' -i *.sh
chmod -x *.sh
rm -f modules/.lock

%build
%set_build_flags
%make_build %{makeflags}

%install
%make_install %{makeflags}
ln -s lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -m 0744 -p extra/tab_completion/hashcat.sh %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%license docs/license.txt
%doc README.md
%{_datadir}/bash-completion/
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/%{name}/
%{_bindir}/%{name}

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%files doc
%doc docs/ charsets/ layouts/ masks/ rules/
%doc example.dict example*.sh

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Lukas Javorsky <ljavorsk@redhat.com> - 6.2.6-4
- Rebuilt for minizip-ng transition Fedora change
- Fedora Change: https://fedoraproject.org/wiki/Changes/MinizipNGTransition

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 6.2.6-1
- Updated to version 6.2.6.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 6.2.5-1
- Updated to version 6.2.5.

* Mon Aug 30 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 6.2.4-1
- Updated to version 6.2.4.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 6.2.3-1
- Updated to version 6.2.3.

* Sun Jun 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 6.2.2-1
- Updated to version 6.2.2.

* Sat May 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 6.2.1-1
- Updated to version 6.2.1.
