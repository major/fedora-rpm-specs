# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Logic for creating an unversioned symlink to %%{_pkgdocdir}
# in case %%{_pkgdocdir} is actually a versioned directory.
# %%global doesn't work here as we need lazy expansion.
%define doc_symlink %{lua:if rpm.expand("%{_pkgdocdir}") ~= rpm.expand("%{_docdir}/%{name}") then print (1) end}

# Setup macros for compile flags if not defined already.
%{!?build_cflags:%global build_cflags %{optflags}}
%{!?build_ldflags:%global build_ldflags %{?__global_ldflags}}

# Construct the distribution string for BUILD_ID.
# Please alter them, if you are building packages
# for third-party repositories from this spec file.
%if 0%{?fedora}
%global dist_string Fedora
%else
%if 0%{?rhel}
%global dist_string Fedora EPEL
%else
%global dist_string UNKNOWN
%endif
%endif

# Some general used defines to reduce boilerplate.
%global git_url https://github.com/%{name}/%{name}

%global make_opts BUILD_ID="%{dist_string} %{version}-%{release}" \\\
LDFLAGS="%{build_ldflags}" USER_CFLAGS="%{build_cflags}"

%global dir_opts PREFIX="%{_prefix}" bindir="%{_bindir}" \\\
datadir="%{_datadir}/%{name}" htmldir="%{_pkgdocdir}/html" \\\
infodir="%{_infodir}"

# Run check target by default.
%bcond_without check

# Workaround for texinfo 7.0.x issue - allow disabling docs in info format
# https://bugzilla.redhat.com/show_bug.cgi?id=2188018
%bcond_with info


Name:           cc65
Version:        2.19
Release:        12%{?dist}
Summary:        A free C compiler for 6502 based systems

# For license clarification see:
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=714058#30
License:        zlib
URL:            https://cc65.github.io
Source0:        %{git_url}/archive/V%{version}/%{name}-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=2253946
Patch0:         cc65-c99.patch

# Backported from upstream.
# none

BuildRequires:  gcc
BuildRequires:  make

Requires:       %{name}-common = %{version}-%{release}

%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Recommends:     %{name}-doc = %{version}-%{release}
Recommends:     %{name}-utils%{?_isa} = %{version}-%{release}
%endif

%description
cc65 is a complete cross development package for 65(C)02 systems,
including a powerful macro assembler, a C compiler, linker,
librarian and several other tools.

cc65 has C and runtime library support for many of the old 6502
machines, including

- the following Commodore machines:
  - VIC20
  - C16/C116 and Plus/4
  - C64
  - C128
  - CBM 510 (aka P500)
  - the 600/700 family
  - newer PET machines (not 2001).
- the Apple ]\[+ and successors.
- the Atari 8 bit machines.
- the Atari 2600 console.
- the Atari 5200 console.
- GEOS for the C64, C128 and Apple //e.
- the Bit Corporation Gamate console.
- the NEC PC-Engine (aka TurboGrafx-16) console.
- the Nintendo Entertainment System (NES) console.
- the Watara Supervision console.
- the VTech Creativision console.
- the Oric Atmos.
- the Oric Telestrat.
- the Lynx console.
- the Ohio Scientific Challenger 1P.


%package        devel
Summary:        Development files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-common = %{version}-%{release}

%description    devel
This package contains the development files needed to
compile and link applications for the 65(C)02 CPU with
the %{name} cross compiler toolchain.


%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

BuildRequires:  linuxdoc-tools
BuildRequires:  texinfo

%description    doc
This package contains the documentation files for %{name}.


%package        utils
Summary:        Additional utilities for %{name}
BuildRequires:  zlib-devel

%description    utils
This package contains the additional utilities for %{name}.

They are not needed for compiling applications with %{name},
but might be handy for some additional tasks.

Since these utility programs have some heavier dependencies,
and also can be used without the need of installing %{name},
they have been split into this package.


%prep
%autosetup -p 1


%build
# Parallel build sometimes fails.
# It finishes fine in a second run, tho.
%make_build %{make_opts} %{dir_opts} || \
%make_build %{make_opts} %{dir_opts}

# Build some additional utils.
%{__mkdir_p} util_bin
%{__cc} %{build_cflags} util/atari/ataricvt.c \
  -o util_bin/ataricvt65 %{build_ldflags}
%{__cc} %{build_cflags} util/cbm/cbmcvt.c \
  -o util_bin/cbmcvt65 %{build_ldflags}
%{__cc} %{build_cflags} util/gamate/gamate-fixcart.c \
  -o util_bin/gamate-fixcart65 %{build_ldflags}
%{__cc} %{build_cflags} util/zlib/deflater.c \
  -o util_bin/deflater65 %{build_ldflags} -lz

# Build the documentation.
%if %{with info}
%make_build doc
%else
%make_build html
%endif


%install
%make_install %{make_opts} %{dir_opts}

# Install additional utils.
%{__install} -p -m 0755 util/ca65html %{buildroot}%{_bindir}
%{__install} -p -m 0755 util_bin/* %{buildroot}%{_bindir}

# Install more documentation.
%{__mv} %{buildroot}%{_datadir}/%{name}/samples %{buildroot}%{_pkgdocdir}
%{__install} -p -m 0644 README.md %{buildroot}%{_pkgdocdir}
%if !(0%{?fedora} >= 21 || 0%{?rhel} >= 7)
%{__install} -p -m 0644 LICENSE %{buildroot}%{_pkgdocdir}
%endif
%if 0%{doc_symlink}
%{__ln_s} %{_pkgdocdir} %{buildroot}%{_docdir}/%{name}
%endif


%if %{with check}
%check
# We need a clean build without PREFIX et all defined
# to successfully run the tests from inside the builddir.
# Unfortunately the testsuite cannot be run threaded.  -_-
%{__make} clean
%make_build %{make_opts} || \
%make_build %{make_opts}
%{__make} -C test QUIET=1
%endif


%files
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%license LICENSE
%else
%doc %{_pkgdocdir}/LICENSE
%endif
%if 0%{doc_symlink}
%doc %{_docdir}/%{name}
%endif
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%{_bindir}/ar65
%{_bindir}/ca65
%{_bindir}/cc65
%{_bindir}/chrcvt65
%{_bindir}/cl65
%{_bindir}/co65
%{_bindir}/da65
%{_bindir}/grc65
%{_bindir}/ld65
%{_bindir}/od65
%{_bindir}/sim65
%{_bindir}/sp65


%files devel
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%else
%doc %{_pkgdocdir}/LICENSE
%endif
%if 0%{doc_symlink}
%doc %{_docdir}/%{name}
%endif
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%{_datadir}/%{name}


%files doc
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%endif
%if 0%{doc_symlink}
%doc %{_docdir}/%{name}
%endif
%doc %{_pkgdocdir}
%if %{with info}
%{_infodir}/*.info*
%endif


%files utils
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%else
%doc %{_pkgdocdir}/LICENSE
%endif
%if 0%{doc_symlink}
%doc %{_docdir}/%{name}
%endif
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%{_bindir}/ataricvt65
%{_bindir}/ca65html
%{_bindir}/cbmcvt65
%{_bindir}/deflater65
%{_bindir}/gamate-fixcart65


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Florian Weimer <fweimer@redhat.com> - 2.19-8
- Build testsuite reference in C89 mode

* Thu Jul 20 2023 Dan Horák <dan[at]danny.cz> - 2.19-7
- don't build docs in info format as a workaround (rhbz#2188018)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 13 2021 Dan Horák <dan[at]danny.cz> - 2.19-1
- updated to 2.19

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Björn Esser <besser82@fedoraproject.org> - 2.18-12
- Add several bugfix patches from upstream

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-10
- Add several bugfix patches from upstream

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-8
- Add a set of upstream patches to fix several minor bugs

* Mon Jul 15 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-7
- Add two upstream patches for minor fixes

* Fri Jul 05 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-6
- Clarify the purpose of the devel package in its %%description
  a bit more verbose

* Fri Jul 05 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-5
- Add an upstream patch to fix ld65 behaviour

* Sun Jun 23 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-4
- Add some stuff for backwards compatibility
- Add an unversioned symlink to %%{_pkgdocdir} if needed

* Wed Jun 19 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-3
- Replace Patch1000 with actual upstream commits

* Sat Jun 15 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-2
- Update Patch1000
- Add an option to disable %%check target

* Tue Jun 11 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-1
- Initial import (#1718684)

* Tue Jun 11 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-0.6
- Add a link for clarifying the actual license
- Remove the %%{name} prefix from binaries in the utils package
  and suffix them with 65 for a more uniform experience
- Add a few comments
- Optimize some global definitions to be more vasatile

* Tue Jun 11 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-0.5
- Fix use of a macro
- Remove hiphen separator from binaries in utils package
- Fix an entry in %%changelog

* Mon Jun 10 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-0.4
- Update Patch1000

* Mon Jun 10 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-0.3
- Adapt BUILD_ID to be architecture independent
- Drop Patches 1001 and 2000 as they are not needed anymore

* Sun Jun 09 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-0.2
- Add downstream patch to undefine a macro mangling version string

* Sat Jun 08 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-0.1
- Initial rpm release (#1718684)
