Name:           pdbg
Version:        3.6
Release:        9%{?dist}
Summary:        PowerPC FSI Debugger

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/open-power/pdbg
Source0:        https://github.com/open-power/pdbg/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf automake libtool
BuildRequires:  dtc
BuildRequires:  make
BuildRequires:  ragel
BuildRequires:  libfdt-devel

# makes sense only on the host (Power-based) and the BMC (usually an embedded Arm system)
ExclusiveArch:  ppc64le

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        libs
Summary:        Library files for %{name}

%description    libs
The %{name}-libs package contains libraries for %{name}.


%description
pdbg is a simple application to allow debugging of the host POWER processors
from the BMC and the host itself. It works in a similar way to JTAG programmers
for embedded system development in that it allows you to access GPRs, SPRs and
system memory.


%prep
%autosetup -p1


%build
sh ./bootstrap.sh
%configure --disable-static
%make_build


%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la


%files
%doc README.md
%{_bindir}/%{name}

%files libs
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.6-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 27 2022 Dan Horák <dan@danny.cz> - 3.6-1
- updated to 3.6

* Tue May 17 2022 Dan Horák <dan@danny.cz> - 3.5-1
- updated to 3.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Dan Horák <dan@danny.cz> - 3.4-1
- updated to 3.4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Dan Horák <dan@danny.cz> - 3.3-1
- updated to 3.3

* Wed Feb 03 2021 Dan Horák <dan@danny.cz> - 3.2-2
- review feedback

* Tue Jan 12 2021 Dan Horák <dan@danny.cz> - 3.2-1
- updated to 3.2

* Tue Oct 13 2020 Dan Horák <dan@danny.cz> - 3.1-1
- updated to 3.1

* Thu Sep 10 2020 Dan Horák <dan@danny.cz> - 3.0-1
- initial Fedora package
