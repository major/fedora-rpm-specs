Name:           libocxl
Version:        1.2.1
Release:        11%{?dist}
Summary:        Allows to implement a user-space driver for an OpenCAPI accelerator

License:        Apache-2.0
URL:            https://github.com/OpenCAPI/libocxl
Source0:        https://github.com/OpenCAPI/libocxl/archive/%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  ppc64le

BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  perl(English)
# for tests
BuildRequires:  fuse-devel

%description
Access library which allows to implement a user-space
driver for an OpenCAPI accelerator.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     %{name}-docs

%package        docs
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    devel
The *-devel package contains header file and man pages for
developing applications that use %{name}.

%description    docs
The *-docs package contains doxygen pages for
developing applications that use %{name}.


%prep
%autosetup -p1

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%check
%undefine _auto_set_build_flags
make testobj/unittests V=1


%files
%license COPYING
%doc README.md
%{_libdir}/libocxl.so.*

%files devel
%{_includedir}/*
%{_libdir}/libocxl.so
%{_mandir}/man3/*

%files docs
%{_pkgdocdir}


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 08 2024 Than Ngo <than@redhat.com> - 1.2.1-10
- rebuilt against new doxygen

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Dan Horák <dan[at]danny.cz> - 1.2.1-1
- updated to 1.2.1

* Tue May 11 2021 Timm Bäder <tbaeder@redhat.com> - 1.1.0-8
- Use %%make_build macro

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Michel Normand <normand@linux.vnet.ibm.com> 1.1.0-5
- Add remove_2_backslashes_in_shell_call.patch
  Add remove_eng_inc_in_version_pl.patch
  to avoid f33 build failure

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 michel normand <normand@linux.vnet.ibm.com> 1.1.0-1
- updated to 1.1.0
  Requires Linux headers >= 4.18 to compile
  Add support for POWER9 wake_host_thread/wait
   (requires a compiler with GNU extensions for inline assembler)
  Generate warnings on ignored return values
  Use opaque structs rather than void pointers for ocxl handles
   (this should be transparent to callers)
  Verified GCC 4-8 & Clang 3.6.2-6.0.1 produce correct machine code
   for OpenCAPI, and whitelisted them
  Verify & enforce that we compile with strict ANSI C (2011)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Dan Horák <dan[at]danny.cz> - 1.0.0-1
- updated to 1.0.0 final

* Tue Apr 10 2018 michel normand <normand@linux.vnet.ibm.com> 1.0.0-0.1
- new package and spec file of libocxl from upstream
  url: https://github.com/OpenCAPI/libocxl
