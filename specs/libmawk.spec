Name:           libmawk
Version:        1.0.3
Release:        10%{?dist}
Summary:        Embed awk scripting language in any application written in C

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://repo.hu/projects/libmawk
Source0:        http://repo.hu/projects/libmawk/releases/%{name}-%{version}.tar.gz
Patch0: libmawk-configure-c99.patch
Patch1: libmawk-c99.patch

BuildRequires:  gcc
BuildRequires:  make

%description
Libmawk is a fork of mawk 1.3.3 restructured for embedding.
This means the user gets libmawk.h and libmawk.so and can embed
awk scripting language in any application written in C.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
HTML documentation for %{name}.


%prep
%autosetup -p1


%build
# This ./configure command refers to scconfig. See http://repo.hu/projects/scconfig/
./"configure" --prefix=%{_prefix} --libarchdir=%{_lib} --symbols \
  --CFLAGS="%{build_cflags}" --LDFLAGS="%{build_ldflags}"
%make_build


%install
%make_install LIBARCHDIR=%{buildroot}/%{_libdir} LIBPATH=%{buildroot}/%{_libdir}/%{name}


%files
%license src/libmawk/COPYING
%doc AUTHORS README Release_notes
%{_libdir}/*.so.1
%{_libdir}/*.so.1.0*
%{_bindir}/lmawk
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.awk
%{_mandir}/man1/*

%files devel
%{_mandir}/man3/*
%{_mandir}/man7/*
%{_includedir}/*
%{_libdir}/*.so

%files doc
%doc %{_docdir}/%{name}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.3-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Florian Weimer <fweimer@redhat.com> - 1.0.3-3
- C99 compatibility fixes (#2160704)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Alain <avigne@fedoraproject.org> - 1.0.3-1
- New upstream release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Alain <alain vigne 14 AT gmail com> - 1.0.2-4
- Fix the libdir install, depending on arch
- Patch source code to comply with gcc -fno-common

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Alain <alain vigne 14 AT gmail com> - 1.0.2-1
- New upstream release
- Add build flags to local "configure"
- Own libdir/name directory

* Sun Mar 17 2019 Alain <alain vigne 14 AT gmail com> - 1.0.1-2
- use proper libarchdir ./configure switch

* Thu Feb 28 2019 Alain <alain vigne 14 AT gmail com> - 1.0.1-1
- New upstream release
- Install awklib library
- Install man pages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 01 2018 Alain <alain vigne 14 AT gmail com> - 1.0.0-1
- Initial proposal
